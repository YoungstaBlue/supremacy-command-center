#!/usr/bin/env python3
"""Build the reference library in reference/ from artifact snapshots.

Pipeline
--------
1. A Claude Code session fetches each artifact listed in sources.json with the
   Artifact tool (``action: read`` with ``path``/``paths``) into
   ``snapshots/<slug>/``. Docs-type artifacts are read through the Claude Docs
   connector and the returned XML saved as ``snapshots/<slug>/doc.xml``.
2. ``build.py`` copies the raw files to ``reference/<slug>/source/`` (lossless
   snapshot), extracts any embedded data to ``reference/<slug>/data.json``, and
   renders ``reference/<slug>/<slug>.md`` (or a folder of Markdown files for the
   big statute library) so the material is greppable from any session.
3. ``reference/manifest.json`` records title, URL, kind, bytes, sha256 and the
   files produced; ``reference/README.md`` is regenerated as the human index.

usage:
  build.py --snapshots DIR            build everything from DIR
  build.py --snapshots DIR --only SLUG[,SLUG]
  build.py --verify                   recompute hashes and compare to manifest
  build.py --readme                   regenerate reference/README.md from the manifest
"""
from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import hashlib
import json
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
REF = REPO / "reference"
SOURCES = json.loads((HERE / "sources.json").read_text(encoding="utf-8"))["sources"]

# --------------------------------------------------------------------------- utils


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(REPO).as_posix()


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def tidy_md(text: str) -> str:
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def human_bytes(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:,.0f} {unit}" if unit == "B" else f"{n:,.1f} {unit}"
        n /= 1024
    return f"{n} B"


# ------------------------------------------------------------------ HTML -> Markdown


def html_to_markdown(html: str) -> str:
    from bs4 import BeautifulSoup
    from markdownify import markdownify

    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "svg", "link", "meta", "input", "button", "nav", "noscript"]):
        tag.decompose()
    for tag in soup.select(".search, .rail, [aria-hidden=true]"):
        tag.decompose()
    for title in soup.body.find_all("title") if soup.body else []:
        title.decompose()
    body = soup.body or soup
    md = markdownify(str(body), heading_style="ATX", bullets="-", escape_underscores=False, escape_asterisks=False)
    return tidy_md(md)


# ------------------------------------------------------------------ JSON -> Markdown

LABEL_KEYS = ("title", "term", "name", "t", "h", "p", "sec", "cite", "event", "topic", "chapter", "k", "label", "cname", "no", "text")
LONG_KEYS = {"text", "textExcerpt", "def", "definition", "d", "overview", "summary", "note", "meaning", "principle", "desc", "sum"}


def _label(item: dict) -> str | None:
    for key in LABEL_KEYS:
        value = item.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def _scalar(value) -> str:
    if isinstance(value, bool):
        return "yes" if value else "no"
    if value is None:
        return ""
    return str(value).strip()


def json_to_markdown(data, level: int = 2, title: str | None = None) -> str:
    """Render arbitrary reference JSON as readable Markdown.

    Dicts become sections, lists of dicts become one heading per item with the
    item's scalar fields as bullets and long text as paragraphs, lists of
    scalars become bullet lists.
    """
    out: list[str] = []
    hashes = "#" * min(level, 6)
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                out.append(f"{hashes} {key}\n")
                out.append(json_to_markdown(value, level + 1))
            else:
                out.append(f"- **{key}**: {_scalar(value)}")
        return "\n".join(out) + "\n"
    if isinstance(data, list):
        if all(isinstance(x, dict) for x in data):
            for index, item in enumerate(data, 1):
                label = _label(item) or f"Entry {index}"
                out.append(f"{hashes} {label}\n")
                for key, value in item.items():
                    if isinstance(value, str) and value.strip() == label and key in LABEL_KEYS:
                        continue
                    if isinstance(value, dict) or (isinstance(value, list) and any(isinstance(x, (dict, list)) for x in value)):
                        out.append(f"**{key}**\n")
                        out.append(json_to_markdown(value, level + 1))
                    elif isinstance(value, list):
                        if value:
                            out.append(f"- **{key}**: " + "; ".join(_scalar(v) for v in value))
                    elif key in LONG_KEYS and isinstance(value, str) and len(value) > 160:
                        out.append(f"\n{value.strip()}\n")
                    else:
                        text = _scalar(value)
                        if text:
                            out.append(f"- **{key}**: {text}")
                out.append("")
            return "\n".join(out) + "\n"
        return "\n".join(f"- {_scalar(x) if not isinstance(x, list) else ' · '.join(_scalar(y) for y in x)}" for x in data) + "\n"
    return _scalar(data) + "\n"


# --------------------------------------------------------------------- converters


def convert_html(src: dict, snap: Path, out: Path) -> list[Path]:
    html = (snap / "index.html").read_text(encoding="utf-8")
    md_path = out / f"{src['slug']}.md"
    write(md_path, frontmatter(src) + html_to_markdown(html))
    return [md_path]


def convert_jsdata(src: dict, snap: Path, out: Path) -> list[Path]:
    data_path = out / "data.json"
    data_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["node", str(HERE / "extract_js.mjs"), str(snap / "index.html"), str(data_path)], check=True)
    data = json.loads(data_path.read_text(encoding="utf-8"))
    md_path = out / f"{src['slug']}.md"
    write(md_path, frontmatter(src) + json_to_markdown(data))
    return [data_path, md_path]


def convert_jsonblock(src: dict, snap: Path, out: Path) -> list[Path]:
    html = (snap / "index.html").read_text(encoding="utf-8")
    match = re.search(r'<script type="application/json" id="data">(.*?)</script>', html, re.S)
    if not match:
        raise SystemExit(f"{src['slug']}: no <script type=application/json id=data> block")
    data = json.loads(match.group(1))
    data_path = out / "data.json"
    write(data_path, json.dumps(data, indent=1, ensure_ascii=False))
    md_path = out / f"{src['slug']}.md"
    write(md_path, frontmatter(src) + json_to_markdown(data))
    return [data_path, md_path]


def convert_slides(src: dict, snap: Path, out: Path) -> list[Path]:
    deck = json.loads((snap / "project" / "deck.json").read_text(encoding="utf-8"))
    parts = [frontmatter(src), f"# {deck.get('title', src['title'])}\n"]
    for index, slide_id in enumerate(deck["order"], 1):
        html = (snap / "project" / "slides" / f"{slide_id}.html").read_text(encoding="utf-8")
        body = html_to_markdown(html)
        parts.append(f"\n---\n\n## Slide {index}: {slide_id}\n\n{body}")
    md_path = out / f"{src['slug']}.md"
    write(md_path, tidy_md("\n".join(parts)))
    return [md_path]


def convert_docs(src: dict, snap: Path, out: Path) -> list[Path]:
    xml = (snap / "doc.xml").read_text(encoding="utf-8")
    md_path = out / f"{src['slug']}.md"
    write(md_path, frontmatter(src) + docs_xml_to_markdown(xml))
    return [md_path]


def convert_rsmo(src: dict, snap: Path, out: Path) -> list[Path]:
    data = snap / "data"
    index = json.loads((data / "index.json").read_text(encoding="utf-8"))
    produced: list[Path] = []
    chapters_by_title: dict[str, dict] = {t["r"]: t for t in index["titles"]}

    toc = [frontmatter(src), "# Missouri Law Library\n",
           f"Captured from revisor.mo.gov; index built {index.get('built', '?')}. "
           f"{index['stats']['sections']:,} RSMo sections in {index['stats']['chapters']} chapters across "
           f"{index['stats']['titles']} titles, plus {index['stats']['const']} Missouri Constitution sections.\n",
           "## Titles\n"]
    for title in index["titles"]:
        chapters = title.get("chs", [])
        toc.append(f"- [Title {title['r']} — {title['n'].title()}](rsmo/title-{title['r']}.md) · {len(chapters)} chapters")
    toc.append("- [Missouri Constitution](constitution.md)\n")
    if index.get("book"):
        toc.append("## Sections tracked for the active matters\n")
        toc.append(", ".join(index["book"]) + "\n")
    toc_path = out / f"{src['slug']}.md"
    write(toc_path, "\n".join(toc))
    produced.append(toc_path)

    for title_file in sorted((data / "t").glob("*.json")):
        roman = title_file.stem
        meta = chapters_by_title.get(roman, {"r": roman, "n": "", "chs": []})
        chapter_names = {str(c.get("c") or c.get("n") or c.get("ch") or ""): c for c in meta.get("chs", []) if isinstance(c, dict)}
        chapters = json.loads(title_file.read_text(encoding="utf-8"))
        lines = [f"# Title {roman} — {meta.get('n', '').title()}\n",
                 f"Source: {src['url']} (`data/t/{roman}.json`). Verify any section against revisor.mo.gov before citing.\n"]
        for chapter_number in sorted(chapters, key=lambda c: (len(c), c)):
            chapter_meta = chapter_names.get(chapter_number, {})
            chapter_name = chapter_meta.get("n") or chapter_meta.get("name") or chapter_meta.get("t") or ""
            lines.append(f"\n## Chapter {chapter_number}{(' — ' + chapter_name) if chapter_name else ''}\n")
            for section in chapters[chapter_number]:
                lines.append(f"\n### {section.get('sec', '')} {section.get('title', '').strip()}\n")
                text = (section.get("text") or "").strip()
                if text:
                    lines.append(text + "\n")
                meta_bits = []
                if section.get("eff"):
                    meta_bits.append(f"Effective {section['eff']}")
                if section.get("hist"):
                    meta_bits.append(section["hist"].strip())
                if meta_bits:
                    lines.append("*" + " · ".join(meta_bits) + "*\n")
        path = out / "rsmo" / f"title-{roman}.md"
        write(path, tidy_md("\n".join(lines)))
        produced.append(path)

    constitution = json.loads((data / "constitution.json").read_text(encoding="utf-8"))
    lines = ["# Missouri Constitution (1945, as amended)\n",
             f"Source: {src['url']} (`data/constitution.json`). Verify against revisor.mo.gov before citing.\n"]
    for article in constitution.get("arts", []):
        lines.append(f"\n## Article {article.get('a', '')} — {article.get('n', '')}\n")
        for section in article.get("s", []):
            if isinstance(section, dict):
                heading = section.get("sec") or section.get("s") or section.get("n") or ""
                title = section.get("title") or section.get("t") or ""
                lines.append(f"\n### Section {heading} {title}".rstrip() + "\n")
                text = (section.get("text") or section.get("x") or "").strip()
                if text:
                    lines.append(text + "\n")
                for note in section.get("notes") or []:
                    lines.append(f"> {str(note).strip()}\n")
                extra = [str(section[k]).strip() for k in ("eff", "hist", "source") if section.get(k)]
                if extra:
                    lines.append("*" + " · ".join(extra) + "*\n")
            else:
                lines.append(f"- {section}")
    path = out / "constitution.md"
    write(path, tidy_md("\n".join(lines)))
    produced.append(path)
    return produced


CONVERTERS = {
    "html": convert_html,
    "jsdata": convert_jsdata,
    "jsonblock": convert_jsonblock,
    "slides": convert_slides,
    "docs": convert_docs,
    "rsmo": convert_rsmo,
}


# ------------------------------------------------------------- Claude Docs XML -> MD


def docs_xml_to_markdown(xml: str) -> str:
    root = ET.fromstring(xml)

    def inline(node) -> str:
        parts: list[str] = []
        if node.text:
            parts.append(node.text)
        for child in node:
            tag = child.tag
            if tag == "text":
                parts.append(inline(child))
            elif tag == "bold":
                parts.append(f"**{inline(child)}**")
            elif tag == "italic":
                parts.append(f"*{inline(child)}*")
            elif tag == "code":
                parts.append(f"`{inline(child)}`")
            elif tag == "link":
                parts.append(f"[{inline(child)}]({child.get('href', '')})")
            elif tag == "date":
                parts.append(child.get("value", ""))
            elif tag == "mention":
                parts.append(child.get("name", ""))
            else:
                parts.append(inline(child))
            if child.tail:
                parts.append(child.tail)
        return "".join(parts)

    def block(node, depth: int = 0) -> list[str]:
        tag = node.tag
        if tag == "paragraph":
            text = inline(node).strip()
            heading = node.get("heading")
            if heading:
                return [f"{'#' * int(heading)} {text}", ""]
            return [text, ""] if text else []
        if tag == "table":
            rows = []
            for row in node.findall("row"):
                cells = [" ".join(" ".join(block(p, depth)).split()) for p in [c for c in row.findall("cell")]]
                rows.append(cells)
            if not rows:
                return []
            width = max(len(r) for r in rows)
            rows = [r + [""] * (width - len(r)) for r in rows]
            lines = ["| " + " | ".join(rows[0]) + " |", "| " + " | ".join("---" for _ in rows[0]) + " |"]
            lines += ["| " + " | ".join(r) + " |" for r in rows[1:]]
            return lines + [""]
        if tag == "cell":
            return [" ".join(" ".join(line for c in node for line in block(c, depth)).split())]
        if tag == "list":
            kind = node.get("kind", "bullet")
            lines = []
            for index, item in enumerate(node.findall("listItem"), 1):
                inner = [l for c in item for l in block(c, depth + 1) if l]
                head = inner[0] if inner else ""
                marker = f"{index}." if kind == "ordered" else ("- [ ]" if kind == "check" else "-")
                lines.append(f"{'  ' * depth}{marker} {head}")
                for extra in inner[1:]:
                    lines.append(f"{'  ' * (depth + 1)}{extra}")
            return lines + [""]
        out: list[str] = []
        for child in node:
            out += block(child, depth)
        return out

    return tidy_md("\n".join(block(root)))


# -------------------------------------------------------------------- frontmatter


def frontmatter(src: dict) -> str:
    lines = ["---", f"title: \"{src['title']}\"", f"source: {src['url']}", f"shelf: \"{src.get('shelf', '')}\""]
    if src.get("volume"):
        lines.append(f"volume: \"{src['volume']}\"")
    lines.append(f"synced: {dt.date.today().isoformat()}")
    lines.append("---\n")
    return "\n".join(lines)


# --------------------------------------------------------------------- snapshots


def snapshot_files(src: dict, snap: Path) -> list[Path]:
    wanted = ["index.html"] + list(src.get("files", []))
    if src["kind"] == "docs":
        wanted = ["index.html", "doc.xml"]
    files: list[Path] = []
    for pattern in wanted:
        matches = sorted(p for p in snap.rglob("*") if p.is_file() and fnmatch.fnmatch(p.relative_to(snap).as_posix(), pattern))
        if not matches:
            raise SystemExit(f"{src['slug']}: snapshot is missing {pattern}")
        files += matches
    return files


def build(snapshots: Path, only: set[str] | None) -> None:
    manifest_path = REF / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {"artifacts": {}}
    for src in SOURCES:
        slug = src["slug"]
        if only and slug not in only:
            continue
        snap = snapshots / slug
        if not snap.is_dir():
            raise SystemExit(f"{slug}: no snapshot at {snap}")
        out = REF / slug
        if out.exists():
            shutil.rmtree(out)
        source_dir = out / "source"
        copied: list[dict] = []
        for file in snapshot_files(src, snap):
            dest = source_dir / file.relative_to(snap)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file, dest)
            copied.append({"path": rel(dest), "bytes": dest.stat().st_size, "sha256": sha256(dest)})
        produced = CONVERTERS[src["kind"]](src, snap, out)
        manifest["artifacts"][slug] = {
            "title": src["title"],
            "url": src["url"],
            "kind": src["kind"],
            "shelf": src.get("shelf", ""),
            "volume": src.get("volume"),
            "note": src.get("note"),
            "synced": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "source_files": copied,
            "source_bytes": sum(f["bytes"] for f in copied),
            "generated": sorted(rel(p) for p in produced),
            "generated_bytes": sum(p.stat().st_size for p in produced),
        }
        print(f"built {slug}: {len(copied)} source file(s), {len(produced)} generated, {human_bytes(sum(f['bytes'] for f in copied))}")
    manifest["generated_by"] = "scripts/reference-sync/build.py"
    manifest["updated"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    write(manifest_path, json.dumps(manifest, indent=2, ensure_ascii=False))
    write(REF / "README.md", render_readme(manifest))


def verify() -> int:
    manifest = json.loads((REF / "manifest.json").read_text(encoding="utf-8"))
    bad = 0
    for slug, entry in manifest["artifacts"].items():
        for file in entry["source_files"]:
            path = REPO / file["path"]
            if not path.exists():
                print(f"MISSING  {file['path']}")
                bad += 1
            elif sha256(path) != file["sha256"]:
                print(f"CHANGED  {file['path']}")
                bad += 1
        for generated in entry["generated"]:
            if not (REPO / generated).exists():
                print(f"MISSING  {generated}")
                bad += 1
    total = sum(e["source_bytes"] for e in manifest["artifacts"].values())
    print(f"{len(manifest['artifacts'])} artifacts, {human_bytes(total)} of source snapshots, {bad} problem(s)")
    return 1 if bad else 0


# ------------------------------------------------------------------------ README


def render_readme(manifest: dict) -> str:
    shelves: dict[str, list[tuple[str, dict]]] = {}
    position = {src["slug"]: index for index, src in enumerate(SOURCES)}
    for slug, entry in sorted(manifest["artifacts"].items(), key=lambda kv: position.get(kv[0], len(position))):
        shelves.setdefault(entry.get("shelf") or "Other", []).append((slug, entry))
    order = ["Hubs and indexes", "LawMind Reference Library", "Missouri primary law", "Federal primary law", "Glossaries"]
    lines = [
        "# Reference Library",
        "",
        "Every reference volume, statute archive and index built in Claude, synced into this repository so any",
        "Claude Code session can read and grep it without opening the live artifacts. Each folder holds the exact",
        "published files under `source/` (the lossless snapshot) and a generated Markdown rendering beside them.",
        "`manifest.json` lists every file with its size and SHA-256.",
        "",
        "Legal information, not legal advice. Statute and rule text here is a snapshot: confirm it against the",
        "official publisher (revisor.mo.gov, courts.mo.gov, uscode.house.gov) before citing it in a filing.",
        "",
        "## How to re-sync",
        "",
        "In a Claude Code session on this repository:",
        "",
        "1. Ask Claude to fetch every artifact in `scripts/reference-sync/sources.json` with the Artifact tool",
        "   (`action: read` with `path: index.html`, plus the listed `files`) into `snapshots/<slug>/`.",
        "   Docs-type entries are read through the Claude Docs connector; save the returned XML as `doc.xml`.",
        "2. Run `python3 scripts/reference-sync/build.py --snapshots snapshots` (needs `beautifulsoup4`,",
        "   `markdownify`, `lxml` and Node 18+).",
        "3. Commit the result. `python3 scripts/reference-sync/build.py --verify` checks the tree against the manifest.",
        "",
        "To add a volume, append an entry to `sources.json` with a `kind` of `html`, `jsdata`, `jsonblock`,",
        "`slides`, `docs` or `rsmo` and repeat the steps above.",
        "",
    ]
    total_src = sum(e["source_bytes"] for e in manifest["artifacts"].values())
    total_gen = sum(e["generated_bytes"] for e in manifest["artifacts"].values())
    lines += [
        "## Contents",
        "",
        f"{len(manifest['artifacts'])} artifacts · {human_bytes(total_src)} of published source files · "
        f"{human_bytes(total_gen)} of generated Markdown and JSON · last sync {manifest.get('updated', '')[:10]}",
        "",
    ]
    for shelf in order + [s for s in shelves if s not in order]:
        if shelf not in shelves:
            continue
        lines += [f"### {shelf}", "", "| Volume | Title | Read | Live artifact | Source size |", "| --- | --- | --- | --- | --- |"]
        for slug, entry in shelves[shelf]:
            primary = next((g for g in entry["generated"] if g.endswith(f"{slug}.md")), entry["generated"][0])
            read = f"[{Path(primary).name}]({Path(primary).relative_to('reference').as_posix()})"
            lines.append(
                f"| {entry.get('volume') or ''} | **{entry['title']}**{(' — ' + entry['note']) if entry.get('note') else ''} "
                f"| {read} | [open]({entry['url']}) | {human_bytes(entry['source_bytes'])} |"
            )
        lines.append("")
    lines += [
        "## Layout",
        "",
        "```",
        "reference/",
        "  README.md                 this index (generated)",
        "  manifest.json             every file with bytes and sha256 (generated)",
        "  <slug>/",
        "    <slug>.md               Markdown rendering for reading and grep",
        "    data.json               extracted data, where the page embedded it",
        "    rsmo/title-*.md         Missouri Law Library only: one file per RSMo title",
        "    constitution.md         Missouri Law Library only",
        "    source/                 the artifact's published files, byte for byte",
        "```",
    ]
    return "\n".join(lines) + "\n"


# -------------------------------------------------------------------------- main


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--snapshots", type=Path, help="directory holding snapshots/<slug>/")
    parser.add_argument("--only", help="comma-separated slugs to rebuild")
    parser.add_argument("--verify", action="store_true", help="check reference/ against manifest.json")
    parser.add_argument("--readme", action="store_true", help="regenerate reference/README.md from manifest.json only")
    args = parser.parse_args()
    if args.verify:
        return verify()
    if args.readme:
        manifest = json.loads((REF / "manifest.json").read_text(encoding="utf-8"))
        write(REF / "README.md", render_readme(manifest))
        return 0
    if not args.snapshots:
        parser.error("--snapshots DIR is required unless --verify")
    build(args.snapshots.resolve(), set(args.only.split(",")) if args.only else None)
    return 0


if __name__ == "__main__":
    sys.exit(main())
