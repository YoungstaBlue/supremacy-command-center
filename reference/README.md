# Reference Library

Every reference volume, statute archive and index built in Claude, synced into this repository so any
Claude Code session can read and grep it without opening the live artifacts. Each folder holds the exact
published files under `source/` (the lossless snapshot) and a generated Markdown rendering beside them.
`manifest.json` lists every file with its size and SHA-256.

Legal information, not legal advice. Statute and rule text here is a snapshot: confirm it against the
official publisher (revisor.mo.gov, courts.mo.gov, uscode.house.gov) before citing it in a filing.

## How to re-sync

In a Claude Code session on this repository:

1. Ask Claude to fetch every artifact in `scripts/reference-sync/sources.json` with the Artifact tool
   (`action: read` with `path: index.html`, plus the listed `files`) into `snapshots/<slug>/`.
   Docs-type entries are read through the Claude Docs connector; save the returned XML as `doc.xml`.
2. Run `python3 scripts/reference-sync/build.py --snapshots snapshots` (needs `beautifulsoup4`,
   `markdownify`, `lxml` and Node 18+).
3. Commit the result. `python3 scripts/reference-sync/build.py --verify` checks the tree against the manifest.

To add a volume, append an entry to `sources.json` with a `kind` of `html`, `jsdata`, `jsonblock`,
`slides`, `docs` or `rsmo` and repeat the steps above.

## Contents

24 artifacts · 121.9 MB of published source files · 109.3 MB of generated Markdown and JSON · last sync 2026-10-06

### Hubs and indexes

| Volume | Title | Read | Live artifact | Source size |
| --- | --- | --- | --- | --- |
|  | **Pinned Index** — Compiled table of contents for every pinned volume, tool and archive. | [pinned-index.md](pinned-index/pinned-index.md) | [open](https://claude.ai/artifact/DcLcETGacVTGCMALwawUGF) | 21.3 KB |
|  | **LawMind Reference Library** — Master index for the twelve LawMind volumes, with provenance and known-defect notes. | [lawmind-reference-library.md](lawmind-reference-library/lawmind-reference-library.md) | [open](https://claude.ai/artifact/VSM13DCS42DoMBRnPRp932) | 27.6 KB |
|  | **Master Legal Index** — Reference Volume I: Missouri and federal rules, statutes, claim elements, landmark cases, deadlines and terms. | [master-legal-index.md](master-legal-index/master-legal-index.md) | [open](https://claude.ai/artifact/LM4doubHgswPPA8U4jFwFh) | 47.0 KB |
|  | **The LawMind Compendium** — Slide deck tying the dictionaries, encyclopedia, statutes, case summaries and audits together. | [lawmind-compendium.md](lawmind-compendium/lawmind-compendium.md) | [open](https://claude.ai/artifact/KbFR8VxXTgxyK8FpGXE5Ma) | 64.2 KB |
|  | **Missouri Law Library — Ingestion Map** — Claude Doc: where every Missouri and federal source stands, gaps, and the ingestion order. | [missouri-law-library-ingestion-map.md](missouri-law-library-ingestion-map/missouri-law-library-ingestion-map.md) | [open](https://claude.ai/artifact/5hPcFHoerc9wu8s8GDtCu1) | 62.1 KB |

### LawMind Reference Library

| Volume | Title | Read | Live artifact | Source size |
| --- | --- | --- | --- | --- |
| Vol. 1 | **LawMind Dictionary A–C** | [dictionary-a-c.md](dictionary-a-c/dictionary-a-c.md) | [open](https://claude.ai/artifact/WfqU4uVNiFJh4BZE9fiLm6) | 5.6 MB |
| Vol. 2 | **LawMind Dictionary D–I** | [dictionary-d-i.md](dictionary-d-i/dictionary-d-i.md) | [open](https://claude.ai/artifact/GTjkqarjDYTh8VcsJYqt3i) | 6.9 MB |
| Vol. 3 | **LawMind Dictionary J–P** | [dictionary-j-p.md](dictionary-j-p/dictionary-j-p.md) | [open](https://claude.ai/artifact/AyuRcUqfUxzecAw6Aoq8et) | 6.1 MB |
| Vol. 4 | **LawMind Dictionary Q–Z** | [dictionary-q-z.md](dictionary-q-z/dictionary-q-z.md) | [open](https://claude.ai/artifact/1pJTUVUvj7dnkYhhYRjhr5) | 5.4 MB |
| Vol. 5 | **LawMind Latin Maxims** | [latin-maxims.md](latin-maxims/latin-maxims.md) | [open](https://claude.ai/artifact/3CPpV6VLEsKzqRnNj3iukF) | 97.4 KB |
| Vol. 6 | **LawMind Encyclopedia** | [encyclopedia.md](encyclopedia/encyclopedia.md) | [open](https://claude.ai/artifact/SS3tsJvyqUXNCQxhucfZiB) | 2.5 MB |
| Vol. 7 | **LawMind Missouri & UCC Statutes** | [missouri-ucc-statutes.md](missouri-ucc-statutes/missouri-ucc-statutes.md) | [open](https://claude.ai/artifact/XXTiorXmcmRCBnmKMxHLPd) | 1.4 MB |
| Vol. 8·I | **LawMind Federal Statutes I** | [federal-statutes-1.md](federal-statutes-1/federal-statutes-1.md) | [open](https://claude.ai/artifact/H2uWvAUjP8f2yeXgH45zdQ) | 7.5 MB |
| Vol. 8·II | **LawMind Federal Statutes II** | [federal-statutes-2.md](federal-statutes-2/federal-statutes-2.md) | [open](https://claude.ai/artifact/PhEj4efH9JhcmXui35oy5e) | 7.6 MB |
| Vol. 8·III | **LawMind Federal Statutes III** | [federal-statutes-3.md](federal-statutes-3/federal-statutes-3.md) | [open](https://claude.ai/artifact/5F9pi1TM343tpfwEx55oz1) | 7.8 MB |
| Vol. 9 | **LawMind Case Summaries A–L** | [case-summaries-a-l.md](case-summaries-a-l/case-summaries-a-l.md) | [open](https://claude.ai/artifact/8xfTaeco1b4VQdFN3wK9qu) | 5.4 MB |
| Vol. 10 | **LawMind Case Summaries M–Z** | [case-summaries-m-z.md](case-summaries-m-z/case-summaries-m-z.md) | [open](https://claude.ai/artifact/9vuqGv67JcEAp4snfQwEpz) | 5.9 MB |

### Missouri primary law

| Volume | Title | Read | Live artifact | Source size |
| --- | --- | --- | --- | --- |
|  | **Missouri Law Library** — Every RSMo section and every Missouri Constitution section as captured from revisor.mo.gov. | [missouri-law-library.md](missouri-law-library/missouri-law-library.md) | [open](https://claude.ai/artifact/VDHKvXbCV8VG68xufvh8vL) | 58.2 MB |
|  | **Annotated Statute Book** — Reference Volume III: statutes and rules the cases turn on, interpreting cases, definitions, encyclopedia, Latin, deadlines. | [annotated-statute-book.md](annotated-statute-book/annotated-statute-book.md) | [open](https://claude.ai/artifact/WTDztHyYz9nnPM73GDNutW) | 719.8 KB |
|  | **The Statute Shelf** — Five books: Missouri statutes, legal dictionary, thesaurus, Latin phrasebook, RSMo chapter catalog. | [statute-shelf.md](statute-shelf/statute-shelf.md) | [open](https://claude.ai/artifact/KgpnZbDueKbwyx8JY8xvkA) | 212.7 KB |
|  | **Missouri Statute Browser** — Full-text statutes cited across the matters, with revisor.mo.gov links. | [missouri-statute-browser.md](missouri-statute-browser/missouri-statute-browser.md) | [open](https://claude.ai/artifact/MrUhWNjSgPV7AqMzbwUjAn) | 56.1 KB |
|  | **Missouri Statutes, Cited Sections** — Master Doc 007, Missouri part: the fifteen RSMo sections cited in filings, checked against the citation log. | [missouri-statutes-cited.md](missouri-statutes-cited/missouri-statutes-cited.md) | [open](https://claude.ai/artifact/U2s6nSvToqLjdYCptWwU4p) | 89.1 KB |

### Federal primary law

| Volume | Title | Read | Live artifact | Source size |
| --- | --- | --- | --- | --- |
|  | **U.S. Code Verbatim Archive** — Master Doc 007, federal part: seven federal statutes captured from two official publishers and hashed. | [us-code-verbatim.md](us-code-verbatim/us-code-verbatim.md) | [open](https://claude.ai/artifact/1BcZCFXBQDepJHXUPzgxUm) | 57.6 KB |

### Glossaries

| Volume | Title | Read | Live artifact | Source size |
| --- | --- | --- | --- | --- |
|  | **Legal Terms Glossary** — Statutory and plain-English definitions of the key terms across the matters. | [legal-terms-glossary.md](legal-terms-glossary/legal-terms-glossary.md) | [open](https://claude.ai/artifact/S2zZ3h9Kj1iahnREptHKMt) | 42.2 KB |

## Layout

```
reference/
  README.md                 this index (generated)
  manifest.json             every file with bytes and sha256 (generated)
  <slug>/
    <slug>.md               Markdown rendering for reading and grep
    data.json               extracted data, where the page embedded it
    rsmo/title-*.md         Missouri Law Library only: one file per RSMo title
    constitution.md         Missouri Law Library only
    source/                 the artifact's published files, byte for byte
```
