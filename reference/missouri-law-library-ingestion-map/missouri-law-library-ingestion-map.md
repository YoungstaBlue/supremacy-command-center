---
title: "Missouri Law Library — Ingestion Map"
source: https://claude.ai/artifact/5hPcFHoerc9wu8s8GDtCu1
shelf: "Hubs and indexes"
synced: 2026-10-06
---
# Missouri Law Library — Ingestion Map

2026-09-27 · Tyler R Garner

## Where things stand

Most of the RSMo is already loaded. What's left is 11 missing chapters, a data-quality cleanup, and everything outside the statutes (constitution, court rules, regulations, case law). All counts below were checked live today.

| Store | What's in it | Count | Source |
| --- | --- | --- | --- |
| Supabase `statute_sections` (Missouri) | RSMo sections, 457 chapters | 29,324 | 29,309 from the vaquill/open-us-law bulk pull (9/24); 15 from Legal Data Hunter (9/9) |
| Supabase `statute_sections` (federal) | 18, 34 and 42 U.S.C. | 1,641 | uscode.house.gov (OLRC), 9/8 |
| Supabase `rsmo_sections`, `rsmo_capture_queue`, `rsmo_change_log`, `statute_change_log` | The verbatim-from-revisor archive and update tracking | 0 (empty) | Built but never filled |
| LawMind (Base44) `Statute` | Hand-picked MO and federal sections | 500+ (query capped at 500) | Earlier curator batches |
| LawMind `CaseSummary` | MO, federal and some Kentucky cases | 500+ | CourtListener batches |
| LawMind `LegalTerm` / `EncyclopediaArticle` | Wex terms and articles | 500+ each | Cornell LII Wex |
| LawMind `LatinTerm` | Latin maxims | 219 | Seed data |
| OneDrive `03_REFERENCE_LIBRARY` | Cornell LII dictionary PDF (2,380 terms) + 48 encyclopedia `.md` exports | 49 files | Local backups |

The 29,309 bulk rows came from a third-party mirror (vaquill/open-us-law), not straight from revisor.mo.gov. Treat that as the working copy. The official, hashed archive goes into `rsmo_sections`, which is still empty.

## RSMo: coverage and gaps

The [revisor.mo.gov chapter index](https://revisor.mo.gov/main/Home.aspx) lists 468 chapters. The database has 457 of them. Every chapter in the database appears in the official list, so the gap is 11 chapters and nothing extra.

| Missing chapter | Title (per revisor) | Why it matters |
| --- | --- | --- |
| 400 | Uniform Commercial Code | High. The whole UCC; the curator's UCC source depends on it |
| 564 | Inchoate Offenses | High. Criminal code (attempt, conspiracy) |
| 560 | Fines | High. Criminal sentencing |
| 460 | Estates of Convicts | Medium |
| 152 | Private Car Tax | Low |
| 280 | Treated Timber Products | Low |
| 312 | Nonintoxicating Beer | Low |
| 318 | Pool Tables | Low |
| 342 | Stationary Engineers | Low |
| 203 | Air Conservation (transferred to Ch. 643) | Stub only |
| 255 | Division of Commerce (transferred to Ch. 625) | Stub only |

Data-quality flags in what's already loaded:

- **467**** sections are marked ****`mislabeled_in_source`****.** The mirror filed them under the wrong heading, e.g. 452.375, 455-series, 571.x, 610.x. They need re-pulling from revisor before anyone cites them.
- **15 section numbers appear twice.** Examples: 455.050, 455.085, 565.056, 610.140, 610.122 and 575.150. The two copies are the bulk row and the LDH row. Keep one per section.
- **Only 6 rows have an effective date.** Revisor pages carry the effective date and the history note. The re-verification pass should fill both.
- **14 more "operative"**** rows are ****flagg****ed not current. Th****ose 14, plus the 467 above,**** need a check against revisor for repealed or superseded status.**

## Other Missouri sources to ingest

None of these are in Supabase yet. The court rules and the constitution come first because every filing leans on them.

| Priority | Source | Official publisher | Approx. size | Notes |
| --- | --- | --- | --- | --- |
| 1 | Missouri Constitution (1945, as amended) | revisor.mo.gov (constitution view) | ~14 articles, ~300 sections | Small, stable, high value |
| 1 | Supreme Court Rules: Criminal (19–36), Civil (41–101, incl. Rule 55 pleadings and Rules 80–84 appeals), Juvenile (110–128) | courts.mo.gov | Several hundred rules | Drives every deadline and the `deadlines.controlling_rule` field |
| 1 | Court Operating Rules (COR), incl. COR 2 | courts.mo.gov | ~30 rules | Governs e-filing and Case.net access |
| 2 | Local rules: 10th Circuit (Marion Co.), 45th Circuit (Pike Co.), Court of Appeals Eastern District | Each court's site | Dozens of rules each | Circuit numbers to confirm before pulling |
| 2 | MO Supreme Court + Court of Appeals opinions | courts.mo.gov; CourtListener (courts `mo`, `moctapp`) | Tens of thousands; ingest by topic | Start with cases cited in Tyler's filings |
| 3 | Code of State Regulations (CSR) | sos.mo.gov/adrules | ~12,000+ rules | Only the titles tied to active matters (e.g. corrections, child support) |
| 3 | Missouri Register (proposed/emergency rules) | sos.mo.gov | Rolling | Change feed for CSR |
| 3 | Attorney General opinions | ago.mo.gov | Hundreds | Persuasive only |
| 3 | Court forms (self-represented litigant packets) | courts.mo.gov | ~100 forms | Store as documents, not statute rows |
| Hold | MAI jury instructions | Thomson Reuters publishes the official set | — | Licensing question; don't bulk-ingest without checking |

Skill 28 in your skills folder already names the three official publishers: revisor.mo.gov, courts.mo.gov and sos.mo.gov. Any scraper should pass through its terms and rate-limit gate first.

## Federal and Eighth Circuit sources

Titles 18, 34 and 42 are loaded (1,641 sections). The civil-rights and federal-court matters still need the procedure layer.

| Priority | Source | Where from | Why |
| --- | --- | --- | --- |
| 1 | 28 U.S.C. (Judiciary and Judicial Procedure) | uscode.house.gov, same pipeline as the existing titles | Jurisdiction, IFP (§ 1915), habeas, removal |
| 1 | Federal Rules of Civil Procedure + Evidence | uscode.house.gov (Title 28 appendix) | Every federal filing |
| 1 | E.D. Mo. local rules | moed.uscourts.gov | Formatting and motion practice in the federal case |
| 2 | Federal Rules of Appellate Procedure + 8th Cir. local rules | uscode.house.gov; ca8.uscourts.gov | If anything goes up on appeal |
| 2 | 8th Circuit + E.D./W.D. Mo. opinions on § 1983, Monell and Franks | CourtListener (`ca8`, `moed`, `mowd`) | Case law behind the pleaded theories |
| 3 | Rest of 42 U.S.C. ch. 21 (civil rights) cross-check | Already loaded; verify completeness | Confirm §§ 1981–1988 are all present |

## LawMind reference library

The library-curator entities live in the Base44 app. They're reachable through the The7Garner_Law4Firm connector, not through the direct Base44 tools, which returned "no access" for app 6a53429210c1ce40398a53a8 today. Each entity already has 500+ records except LatinTerm (219).

| Entity | Next source | Batch size | Dedup key |
| --- | --- | --- | --- |
| `Statute` | Stop hand-loading. Point LawMind at Supabase `statute_sections` instead of copying RSMo into Base44 twice | — | `citation` |
| `Statute` (UCC) | RSMo ch. 400 by article (1, 2, 3, 4, 4A, 5, 7, 8, 9); Article 6 is repealed in MO | One article per batch | `citation` |
| `CaseSummary` | CourtListener, MO + 8th Cir., by topic (protective orders, paternity, § 1983, Franks) | 20–30 | `citation` |
| `LegalTerm` | Cornell LII Wex, letter by letter; diff against the 2,380-term PDF in OneDrive | 20–30 | `term` |
| `EncyclopediaArticle` | Wex long-form pages (500+ characters) | 20–30 | `title` |
| `LatinTerm` | Fill in the ~30 rows with no category, then add maxims | 20–30 | `term` |

About 31 LatinTerm rows have no category. Also, some CaseSummary rows are tagged Kentucky. Check whether those belong or were pulled by mistake.

## Where each source lands

Statutes already have a home. Everything else needs one of four new tables, all shaped like `statute_sections`: verbatim text, `official_url`, `sha256`, `retrieved_at`, `effective_date`, `is_current`, plus a generated `search_vector`.

| Source | Target table | Natural key | Status |
| --- | --- | --- | --- |
| RSMo, official verbatim | `rsmo_sections` (queue: `rsmo_capture_queue`, diffs: `rsmo_change_log`) | `section_number` (unique) | Exists, empty |
| RSMo, working copy + federal USC | `statute_sections` (diffs: `statute_change_log`) | `jurisdiction` + `section_number` | Exists, loaded; needs a unique key to stop the 15 dupes |
| MO Constitution | new `constitution_sections` | `article` + `section` | To create |
| Supreme Court Rules, COR, local rules, FRCP/FRE/FRAP | new `court_rules` | `rule_set` + `rule_number` | To create |
| CSR regulations | new `regulations` | CSR cite (e.g. 13 CSR 30-2.010) | To create |
| Opinions (MO + federal) | new `opinions` | `court` + docket/citation | To create |
| Terms, Latin, encyclopedia | LawMind entities (Base44) | per table above | Exists |

One gap to fix: `statute_sections.jurisdiction` only allows `federal` or `missouri`. That's fine for statutes. It's the reason rules and the constitution need their own tables instead of being wedged in.

## Ingestion order

Each step is one bounded batch with a stop-and-report and a written "left off at" note. Nothing runs unattended unless you set up a scheduled task for it.

1. **Close the RSMo gaps.** Pull chapters 400, 564, 560 and 460 from revisor, then the 7 low-priority ones. The 400 pull splits into UCC articles.
2. **Clean the working copy.** Re-pull the 467 mislabeled sections and the 14 stale ones. Drop the 15 duplicates. Add a unique key on `jurisdiction` + `section_number`.
3. **Start the official archive.** Load `rsmo_capture_queue` from revisor's 468-chapter index. Capture into `rsmo_sections` with hashes, criminal and family chapters first (452–455, 210–211, 556–600). Pace it through Skill 28.
4. **Constitution.** One batch.
5. **Court rules.** MO Supreme Court Rules, then COR, then local rules for the circuits you're in.
6. **Federal procedure.** 28 U.S.C., FRCP, FRE, then E.D. Mo. local rules.
7. **Case law by topic,** tied to the live matters, 20–30 opinions per batch.
8. **Reference library top-ups** (Wex terms and articles, Latin clean-up), one small batch at a time.
9. **Update watch.** Once `rsmo_sections` is full, a scheduled re-hash compares against revisor and logs changes to `rsmo_change_log`. The RSMo usually changes each August 28 after session.

## Open decisions

- [ ] Is Supabase the system of record for statutes, with LawMind reading from it? Or do both keep copies?
- [ ] Do you want the verbatim official archive (`rsmo_sections`) at all, or is the cleaned mirror enough? The archive is what you'd cite from.
- [ ] Confirm the circuits and appellate district for the local-rules pull (Marion = 10th, Pike = 45th, Court of Appeals ED?).
- [ ] Which CSR titles and which case-law topics matter to the active matters?
- [ ] Should the Kentucky case summaries stay in LawMind?
- [ ] Should step 9 run as a scheduled task, and how often (weekly, or around August 28)?

## Sources

- [Revisor of Statutes, RSMo chapter index](https://revisor.mo.gov/main/Home.aspx), fetched 9/27 (468 chapters)
- Supabase project "law shit": live queries against `statute_sections` and the RSMo tables, 9/27
- LawMind entities through the The7Garner_Law4Firm connector, 9/27
- `open-us-law-main/coverage.yml` and `scripts/statutes/ingest_mo_bulk.py` on your computer
- Skill 28 (official Missouri law ingestion manager) and the lawmind-library-curator source guide
