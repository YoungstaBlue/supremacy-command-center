#!/usr/bin/env python3
"""Extract the reference library (reference/) into the row-oriented JSON datasets behind the
Legal Reference Library dashboard (https://claude.ai/artifact/QdUBvmcsUVYabF7YVP4agF).

Usage: python3 scripts/reference-sync/dashboard_extract.py reference out/

After a re-sync, run this, upload each out/*.json as an asset of the dashboard and update the
matching dataset's file url. Files must stay under 8 MB each (rsmo.json is the tightest).
"""
import json, re, sys, os
from collections import Counter

REF = sys.argv[1]
OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)

def md_entries(slug):
    text = open(f"{REF}/{slug}/{slug}.md", encoding="utf-8").read()
    parts = re.split(r"\n## ", "\n" + text)
    out = []
    for p in parts[1:]:
        lines = p.split("\n", 1)
        head = lines[0].strip()
        body = lines[1] if len(lines) > 1 else ""
        paras = [re.sub(r"\s+", " ", x).strip() for x in re.split(r"\n\s*\n", body)]
        paras = [x for x in paras if x]
        out.append((head, paras))
    return out

def clip(s, n):
    s = (s or "").strip()
    if len(s) <= n: return s
    cut = s[: n - 1]
    sp = cut.rfind(" ")
    if sp > n * 0.6: cut = cut[:sp]
    return cut + "…"

def strip_link(s):
    return re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)

def link_url(s):
    m = re.search(r"\]\((https?://[^)]+)\)", s)
    return m.group(1) if m else ""

def dump(name, rows):
    path = f"{OUT}/{name}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, separators=(",", ":"))
    print(f"{name}: {len(rows)} rows, {os.path.getsize(path)/1e6:.2f} MB")
    return rows

counts = {}

# ---------- Dictionary (Vols 1-4 + shelf dictionary + glossary + annotated definitions + master glossary)
SOURCE_PAT = re.compile(r"^(Black's Law|\[?Cornell LII Wex|LawMind library|Cornell)")
dict_rows = []
n = 0
for slug, vol in [("dictionary-a-c", "Vol. 1 A–C"), ("dictionary-d-i", "Vol. 2 D–I"), ("dictionary-j-p", "Vol. 3 J–P"), ("dictionary-q-z", "Vol. 4 Q–Z")]:
    ents = md_entries(slug)
    counts[slug] = len(ents)
    for head, paras in ents:
        src, defn, url = "", "", ""
        if paras and (SOURCE_PAT.match(paras[0]) or (len(paras[0]) < 70 and paras[0].startswith("["))):
            src = strip_link(paras[0]); url = link_url(paras[0]); paras = paras[1:]
        if paras: defn = strip_link(paras[0])
        n += 1
        dict_rows.append({"id": f"d{n}", "term": head, "definition": clip(defn, 220), "source": clip(src, 40) or "LawMind Dictionary", "volume": vol, "url": url, "letter": (head[:1].upper() if head[:1].isalpha() else "#")})
sh = json.load(open(f"{REF}/statute-shelf/data.json"))
for e in sh["DICTIONARY"]:
    n += 1
    dict_rows.append({"id": f"d{n}", "term": e["t"], "definition": clip(e["d"], 220), "source": "Statute Shelf, Vol. II", "volume": "Statute Shelf", "url": "", "letter": e["t"][:1].upper()})
gl = json.load(open(f"{REF}/legal-terms-glossary/data.json"))
for e in gl["DATA"]:
    n += 1
    dict_rows.append({"id": f"d{n}", "term": e["term"], "definition": clip(e["def"], 220), "source": f"Glossary · {e.get('cite','')}".strip(" ·"), "volume": "Legal Terms Glossary", "url": e.get("url", ""), "letter": e["term"][:1].upper()})
asb = json.load(open(f"{REF}/annotated-statute-book/data.json"))
for e in asb["definitions"]:
    n += 1
    dict_rows.append({"id": f"d{n}", "term": e["term"], "definition": clip(e["definition"], 220), "source": clip(f"Annotated Statute Book · {e.get('kind','')}", 40), "volume": "Annotated Statute Book", "url": "", "letter": e["term"][:1].upper()})
mli = json.load(open(f"{REF}/master-legal-index/data.json"))["MASTER"]
msec = {s["id"]: s for s in mli["sections"]}
for e in msec["glossary"]["items"]:
    n += 1
    dict_rows.append({"id": f"d{n}", "term": e["k"], "definition": clip(e["d"], 220), "source": "Master Legal Index", "volume": "Master Legal Index", "url": "", "letter": e["k"][:1].upper()})
dict_rows.sort(key=lambda r: r["term"].lower())
half = [r for r in dict_rows if r["letter"] <= "I" or r["letter"] == "#"]
rest = [r for r in dict_rows if not (r["letter"] <= "I" or r["letter"] == "#")]
dump("dictionary_a_i", half)
dump("dictionary_j_z", rest)

# ---------- Latin
latin = []
n = 0
ents = md_entries("latin-maxims"); counts["latin-maxims"] = len(ents)
for head, paras in ents:
    literal, plain, example, pron = "", "", "", ""
    if paras:
        first = paras[0]
        if not first.startswith(("Pronunciation", "Plain language")):
            literal = first; paras = paras[1:]
    for p in paras:
        m = re.search(r"Pronunciation ([^*]+?)\s*\*\*Plain language:\*\*\s*(.*?)(?:\s*\*\*Example:\*\*\s*(.*))?$", p)
        if m: pron, plain, example = m.group(1).strip(), m.group(2).strip(), (m.group(3) or "").strip()
        elif p.startswith("Plain language"): plain = p[len("Plain language"):].strip()
    n += 1
    latin.append({"id": f"l{n}", "term": head, "literal": clip(literal, 200), "plain": clip(plain, 220), "example": clip(example, 200), "pronunciation": pron, "source": "LawMind Latin Maxims (Vol. 5)"})
for e in asb["latin"]:
    n += 1
    latin.append({"id": f"l{n}", "term": e["term"], "literal": clip(e.get("literal", ""), 200), "plain": clip(e.get("meaning", ""), 220), "example": clip(e.get("mo", "") or e.get("note", ""), 200), "pronunciation": "", "source": "Annotated Statute Book"})
for e in sh["LATIN"]:
    n += 1
    latin.append({"id": f"l{n}", "term": e["p"], "literal": clip(e["m"], 200), "plain": clip(e["d"], 220), "example": "", "pronunciation": "", "source": "Statute Shelf, Vol. IV"})
latin.sort(key=lambda r: r["term"].lower())
dump("latin", latin)

# ---------- Encyclopedia
enc = []
n = 0
ents = md_entries("encyclopedia"); counts["encyclopedia"] = len(ents)
for head, paras in ents:
    cat, jur, short = "", "", ""
    for p in paras:
        m = re.match(r"Category (.*?) \*\*Jurisdiction:\*\* (.*?)(?: \*\*Copies merged:\*\*.*)?$", p)
        if m: cat, jur = m.group(1).strip(), m.group(2).strip(); continue
        if p.startswith("In short"): short = p[len("In short"):].strip(); continue
        if not short and not p.startswith("Category"): short = p
    n += 1
    enc.append({"id": f"e{n}", "topic": head, "category": cat or "General Law", "jurisdiction": jur or "General", "summary": clip(short, 240), "source": "LawMind Encyclopedia (Vol. 6)"})
for e in asb["encyclopedia"]:
    n += 1
    enc.append({"id": f"e{n}", "topic": e["topic"], "category": "Missouri practice", "jurisdiction": e.get("jurisdiction", "Missouri"), "summary": clip(e.get("overview", ""), 240), "source": "Annotated Statute Book"})
enc.sort(key=lambda r: r["topic"].lower())
dump("encyclopedia", enc)

# ---------- Statutes: LawMind federal + Missouri/UCC volumes
stat = []
n = 0
for slug, vol in [("federal-statutes-1", "Vol. 8·I"), ("federal-statutes-2", "Vol. 8·II"), ("federal-statutes-3", "Vol. 8·III"), ("missouri-ucc-statutes", "Vol. 7")]:
    ents = md_entries(slug); counts[slug] = len(ents)
    for head, paras in ents:
        jur, cat, snippet, url = "", "", "", ""
        for p in paras:
            m = re.match(r"Jurisdiction (\w+)(?: Category (.*?))?(?: Source (.*))?$", p)
            if m and not snippet:
                jur = m.group(1); cat = (m.group(2) or "").strip();
                if m.group(3): url = link_url(m.group(3))
                continue
            if p.startswith("Effective "): continue
            if not snippet: snippet = strip_link(p)
        cat = re.sub(r"\s*\[\d+ identical copies.*\]", "", cat)
        if not cat:
            cat = "Missouri CSR" if " CSR " in head else ("UCC" if head.startswith("UCC") else ("RSMo" if head.startswith(("RSMo", "Mo", "MO")) else "Other"))
        n += 1
        stat.append({"id": f"s{n}", "cite": clip(head, 160), "jurisdiction": jur or ("Federal" if vol.startswith("Vol. 8") else "Missouri"), "category": clip(cat, 40), "snippet": clip(snippet, 200), "volume": vol, "url": url})
dump("statutes_lawmind", stat)

# ---------- Missouri Law Library: every RSMo section + constitution
idx = json.load(open(f"{REF}/missouri-law-library/source/data/index.json"))
rsmo = []
chapters = []
title_rows = []
n = 0
for t in idx["titles"]:
    tsec = 0
    for ch in t["chs"]:
        cn = str(ch["c"]); cname = ch["n"]; secs = ch.get("s", [])
        chapters.append({"id": f"ch{cn}", "title": t["r"], "titleName": t["n"].title(), "chapter": cn, "chapterName": cname, "sections": len(secs), "url": f"https://revisor.mo.gov/main/PageSelect.aspx?chapter={cn}"})
        tsec += len(secs)
        for s in secs:
            n += 1
            rsmo.append({"id": f"r{n}", "section": s[0], "heading": clip(s[1], 160), "effective": s[2] if len(s) > 2 else "", "chapter": cn, "chapterName": cname, "title": t["r"], "source": "RSMo"})
    title_rows.append({"id": f"t{t['r']}", "title": t["r"], "titleName": t["n"].title(), "chapters": len(t["chs"]), "sections": tsec})
const = json.load(open(f"{REF}/missouri-law-library/source/data/constitution.json"))
cn_ = 0
for a in const["arts"]:
    for s in a["s"]:
        n += 1; cn_ += 1
        rsmo.append({"id": f"r{n}", "section": f"Art. {a['a']}, § {s['sec']}", "heading": clip(s.get("title", ""), 160), "effective": "", "chapter": f"Art. {a['a']}", "chapterName": a["n"], "title": "Const.", "source": "Mo. Const."})
title_rows.append({"id": "tConst", "title": "Const.", "titleName": "Missouri Constitution", "chapters": len(const["arts"]), "sections": cn_})
counts["missouri-law-library"] = len(rsmo)
dump("rsmo", rsmo)
dump("rsmo_chapters", chapters)
dump("rsmo_titles", title_rows)

# ---------- Cases
cases = []
n = 0
for slug, vol in [("case-summaries-a-l", "Vol. 9"), ("case-summaries-m-z", "Vol. 10")]:
    ents = md_entries(slug); counts[slug] = len(ents)
    for head, paras in ents:
        cite, court, year, jur, holding = "", "", "", "", ""
        if paras:
            bits = [b.strip() for b in paras[0].split(" · ")]
            if len(bits) >= 3:
                cite = bits[0]; court = bits[1]; year = bits[2] if len(bits) > 2 else ""; jur = bits[3] if len(bits) > 3 else ""
                paras = paras[1:]
        for p in paras:
            if p.startswith("Holding:"): holding = p[len("Holding:"):].strip(); break
            if p.startswith("Citation record only"): break
            if not holding: holding = p
        n += 1
        cases.append({"id": f"c{n}", "name": clip(head, 140), "cite": cite, "court": clip(court, 60), "year": int(year) if year.isdigit() else None, "jurisdiction": jur or "—", "holding": clip(holding, 220), "summary": "yes" if holding else "citation only", "volume": vol})
for e in asb["cases"]:
    n += 1
    cases.append({"id": f"c{n}", "name": clip(e["name"], 140), "cite": e.get("cite", ""), "court": clip(e.get("court", ""), 60), "year": e.get("year"), "jurisdiction": "Missouri" if "Mo." in e.get("cite", "") else "Federal", "holding": clip(e.get("principle", ""), 220), "summary": "yes", "volume": "Annotated Statute Book"})
dump("cases", cases)

# ---------- Thesaurus
th = []
for i, e in enumerate(sh["THESAURUS"], 1):
    th.append({"id": f"th{i}", "term": e["h"], "synonyms": ", ".join(e["syn"]), "note": clip(e.get("note", ""), 220)})
dump("thesaurus", th)

# ---------- Rules, statutes, claims and cases cited across the matters (Master Legal Index + Annotated Statute Book + browsers)
rules = []
n = 0
labels = {"mo-civ": "Missouri Rules of Civil Procedure", "mo-crim": "Missouri criminal rules", "mo-stat": "RSMo (cited)", "fed-rules": "Federal Rules of Civil Procedure", "fed-stat": "Federal statutes and regulations", "const": "Constitutional provisions", "claims": "Claim and defense elements", "fed-cases": "Federal case law", "mo-cases": "Missouri case law"}
for sid, label in labels.items():
    for e in msec[sid]["items"]:
        n += 1
        rules.append({"id": f"m{n}", "group": label, "jurisdiction": e.get("j") or "—", "cite": e["k"], "title": e.get("t", ""), "note": clip(e.get("d", ""), 240), "source": "Master Legal Index"})
for e in asb["statutes"]:
    n += 1
    rules.append({"id": f"m{n}", "group": "Annotated statutes and rules", "jurisdiction": "Federal" if "U.S.C." in e["cite"] or "Fed." in e["cite"] else "MO", "cite": e["cite"], "title": e.get("title", ""), "note": clip(e.get("summary", ""), 240), "source": "Annotated Statute Book"})
msb = json.load(open(f"{REF}/missouri-statute-browser/data.json"))
for e in msb["DATA"]:
    n += 1
    rules.append({"id": f"m{n}", "group": "Full-text statutes cited in the matters", "jurisdiction": "MO", "cite": e["sec"], "title": e.get("title", ""), "note": clip(e.get("cat", ""), 240), "source": "Missouri Statute Browser"})
for head, paras in md_entries("missouri-statutes-cited"):
    if not head.startswith("§"): continue
    n += 1
    rules.append({"id": f"m{n}", "group": "Cited sections, verified (Master Doc 007)", "jurisdiction": "MO", "cite": head.split(".", 2)[0] + "." + head.split(".", 2)[1] if "." in head else head, "title": head.split(". ", 1)[1] if ". " in head else "", "note": clip(paras[0] if paras else "", 240), "source": "Missouri Statutes, Cited Sections"})
for head, paras in md_entries("us-code-verbatim"):
    if not head.startswith("§"): continue
    n += 1
    rules.append({"id": f"m{n}", "group": "Cited sections, verified (Master Doc 007)", "jurisdiction": "FED", "cite": head.split(". ", 1)[0], "title": head.split(". ", 1)[1] if ". " in head else "", "note": clip(paras[0] if paras else "", 240), "source": "U.S. Code Verbatim Archive"})
dump("cited_authorities", rules)

# ---------- Deadlines
dl = []
n = 0
for e in asb["deadlines"]:
    n += 1
    dl.append({"id": f"dl{n}", "event": e["event"], "deadline": clip(e["deadline"], 220), "authority": e.get("authority", ""), "area": e.get("area", ""), "note": clip(e.get("note", ""), 200), "source": "Annotated Statute Book"})
for e in msec["deadlines"]["items"]:
    n += 1
    dl.append({"id": f"dl{n}", "event": e["e"], "deadline": clip(f"Missouri: {e['m']}  ·  Federal: {e['f']}", 220), "authority": "", "area": "Comparison", "note": "", "source": "Master Legal Index"})
dump("deadlines", dl)

# ---------- Volumes catalog
man = json.load(open(f"{REF}/manifest.json"))["artifacts"]
src = {s["slug"]: s for s in json.load(open(f"{REF}/../scripts/reference-sync/sources.json"))["sources"]}
entry_counts = dict(counts)
entry_counts.update({"statute-shelf": len(sh["STATUTES"]) and sum(len(c["sections"]) for c in sh["STATUTES"]) + len(sh["DICTIONARY"]) + len(sh["THESAURUS"]) + len(sh["LATIN"]) + len(sh["CATALOG"]),
                     "legal-terms-glossary": len(gl["DATA"]), "annotated-statute-book": sum(len(asb[k]) for k in ("statutes", "definitions", "encyclopedia", "cases", "latin", "deadlines")),
                     "master-legal-index": sum(len(s.get("items", [])) for s in mli["sections"]), "missouri-statute-browser": len(msb["DATA"]),
                     "missouri-statutes-cited": sum(1 for h, _ in md_entries("missouri-statutes-cited") if h.startswith("§")),
                     "us-code-verbatim": sum(1 for h, _ in md_entries("us-code-verbatim") if h.startswith("§"))})
kind_names = {"html": "Web volume", "jsdata": "Data browser", "jsonblock": "Data browser", "slides": "Slide deck", "docs": "Claude Doc", "rsmo": "Statute archive"}
order = ["Hubs and indexes", "LawMind Reference Library", "Missouri primary law", "Federal primary law", "Glossaries"]
vols = []
for slug, m in man.items():
    s = src.get(slug, {})
    vols.append({"id": slug, "shelf": m["shelf"], "volume": m.get("volume") or "", "title": m["title"], "note": m.get("note") or s.get("note") or "", "kind": kind_names.get(m["kind"], m["kind"]), "entries": entry_counts.get(slug, 0), "sourceMB": round(m["source_bytes"] / 1e6, 2), "synced": m["synced"][:10], "url": m["url"]})
vols.sort(key=lambda v: (order.index(v["shelf"]), v["volume"], v["title"]))
dump("volumes", vols)
print(json.dumps(entry_counts, indent=1))
