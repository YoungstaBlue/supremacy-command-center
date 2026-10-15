---
title: "LawMind Architecture Deep Dive"
source: https://claude.ai/artifact/4GiGKsgVugXafS6Ui39HND
shelf: "LawMind platform notes"
synced: 2026-10-15
---
[LawMind Reference Library](https://claude.ai/code/artifact/e649cd75-64e4-4061-91f9-f037f4a0bb6d) · research

# LawMind Architecture Deep Dive

What good practice says about the pipeline repairs made in September 2026, an honest read of the “elite system” blueprints already in the Drive, and five scoped proposals now sitting in the app's ToolRequest queue.

**Prepared:** 3 September 2026
**Scope:** validation of the in-flight sync/watchdog repair; an honest verdict on the two "Elite blueprint" sheets; directly-usable OCR/dedup heuristics for the dictionary import; and five new capability proposals logged to `ToolRequest`.

**How to read this:** Section A is about work already underway. Section B is about Tyler's own blueprint sheets. Section C is for whoever is importing the dictionaries today. Section D is the proposal list. Nothing here was built — everything actionable is logged as `ai_scoped` and awaits a human yes.

---

## A. Is the sync/watchdog repair approach right?

**Short answer: yes, and it is already the house pattern. But the watchdog fix as scoped will leave the more dangerous half of the bug in place.**

### A1. Time budget + resumable cursor — correct, and already proven in this codebase

The approach matches current best practice for serverless work under hard execution limits, and — more usefully — it matches what LawMind already does successfully elsewhere. The convention exists in-repo:

| File | Pattern |
| --- | --- |
| `base44/functions/bulk-scrape-cap/entry.ts` | `TIME_BUDGET_MS = 100_000`, `while (Date.now() - start < TIME_BUDGET_MS)`, persisted cursor |
| `base44/functions/scrape-missouri-chapters/entry.ts` | Same budget, `break` at both loop levels, reports `ranOutOfBudget` |
| `base44/functions/cross-reference-terms/entry.ts` | `TIME_BUDGET_MS = 90_000`, returns `timed_out` in the response |
| `base44/functions/backup-library-to-drive/entry.ts` | `TIME_BUDGET_MS = 80_000`, labelled `break outer` |

So the library scraper and court-docket syncer fixes are not inventing anything — they are bringing two stragglers into line with a convention that four other functions already follow. That is the cheapest possible kind of correctness fix and I would not change the approach at all.

Two details worth copying deliberately rather than by accident:

- **Return the timeout flag, don't just break.** `cross-reference-terms` returns `timed_out: true` and `scrape-missouri-chapters` returns `ranOutOfBudget`. A budget exhaustion that is invisible to the caller looks identical to "finished the work." Make both new budgets report it.
- **Budget below the platform ceiling, not at it.** The existing budgets (80–100s) leave headroom for the final write and the response. Keep that margin; a budget that expires exactly at the platform limit still gets killed mid-write.

### A2. At-least-once, not exactly-once — and this has a live consequence

Current guidance is unambiguous: **do not chase exactly-once. Design for at-least-once delivery with idempotent writes**, using deterministic keys and UPSERT-or-unique-constraint semantics so a duplicate write is harmless rather than prevented. ([Cloud Run Jobs idempotency guide](https://tomodahinata.com/en/blog/google-cloud-run-jobs-workflows-batch-async-idempotent-guide), [Idempotent AI agents](https://www.buildmvpfast.com/blog/idempotent-ai-agent-retry-safe-patterns-production-workflow-2026))

This is not abstract for LawMind. `sync-watchdog` re-invokes a source's `recovery_function` **every 5 minutes** for as long as it looks stalled. If the recovery function is a scraper whose writes are not keyed, every recovery cycle re-writes rows. LawMind already knows this pattern — `CaseCalendarEntry` carries an `idempotency_key`, and `sync-doc-dates-to-calendar` explicitly uses it as the dedupe mechanism. But the library entities (`Statute`, `LegalTerm`, `LatinTerm`, `CaseSummary`) have no equivalent. That gap is Proposal 3.

### A3. Bounded backoff instead of permanent lockout — correct, and the current code confirms the bug

`base44/functions/sync-watchdog/entry.ts` line 35:

```
if (hb.status === 'error' && hb.consecutive_stalls >= 5) continue; // exhausted, needs manual attention
```

That is a permanent lockout with no time-based re-entry. A source that fails five times is skipped forever, even if the underlying cause (an API quota window, a transient outage) clears ten minutes later. Replacing it with exponential backoff plus jitter and a half-open probe is exactly right — that is the standard circuit breaker, and the half-open state is the part that makes a breaker a breaker rather than a fuse. ([Retry + circuit breaker](https://oneuptime.com/blog/post/2026-01-30-go-retry-circuit-breaker-pattern/view), [Backoff with jitter](https://web-alert.io/blog/retry-storms-exponential-backoff-jitter-explained))

Add jitter specifically. All 14 sources share one 5-minute cron tick; without jitter, a common upstream failure makes all of them retry in lockstep, which is the retry-storm shape backoff is meant to avoid.

### A4. What I would do differently — the false-healthy loop

This is the most important thing in this section.

The repair was scoped as "a watchdog that never marked recoveries as healthy." Reading the live code, the failure mode is the **opposite**, and it is worse:

```
if (hb.recovery_function) {
  await base44.asServiceRole.functions.invoke(hb.recovery_function, {});
}
// If we got here without throwing, recovery was dispatched
await base44.asServiceRole.entities.SyncHeartbeat.update(hb.id, {
  status: 'active', consecutive_stalls: 0, last_recovered_at: nowIso, last_error: ''
});
recovered.push(hb.source);
```

The watchdog declares the source **healthy** and resets `consecutive_stalls` to **zero** purely because `invoke()` did not throw. It never checks that the heartbeat actually advanced. Dispatching a recovery is not the same as recovering. Three consequences:

1. **A permanently broken source looks fine forever.** It stalls, gets "recovered," stalls again 5 minutes later, gets "recovered" again — indefinitely.
2. **It can never reach the 5-stall threshold**, because every cycle resets the counter to 0. So the lockout bug in A3 and this bug partially mask each other: sources that fail *loudly* (invoke throws) get locked out permanently; sources that fail *quietly* (invoke returns an error payload without throwing) are never escalated at all.
3. **No one is ever told.** The alert only fires when `failed.length > 0`. A source in the quiet-failure loop produces `failed.length === 0` on every tick, so no email is ever sent. This is not alert fatigue — it is alert *starvation*, and it is harder to notice because the dashboard reads green.

The fix is a two-phase confirmation, which is standard heartbeat-monitoring practice: record `last_heartbeat` at dispatch time, leave the source in `recovering`, and only promote it to `active` on a **later tick** once the heartbeat timestamp has actually moved past the recorded value. Recovery is confirmed by observed evidence, never by the absence of an exception. That is Proposal 5.

I have logged Proposal 5 flagged as **possibly-duplicate** — if the in-flight fix already adds heartbeat-advance confirmation, decline it as a duplicate. But if the fix only changes *when* a source is marked healthy without changing *what counts as evidence of health*, this bug survives the fix.

---

## B. Verdict on the two blueprint sheets

Both sheets are short — a 6-row gap-analysis table and a 4-row setup table. I read both in full; there is no hidden content. They are aspirational sketches, not specs, and I have treated them that way.

An important framing point up front: **the sheets substantially understate what LawMind already is.** The "Current Base 44 Environment" column describes a single-agent orchestrator running shell scripts sequentially. The actual app has 16 agents, ~175 backend functions, ~75 workflows, 54 entities, a resumable 14-source ingestion system, and a fail-closed citation guard. Several "High" gaps are already closed. Judging LawMind against this table would send you rebuilding things you have.

### Sheet 1 — "Master System Blueprint vs. Current Base 44 Environment"

| Blueprint row | Verdict | Why |
| --- | --- | --- |
| **3-tiered architecture** (Jurisdictional Core / Domain Expert / Self-Audit), gap rated "High" | **Already covered** | `base44/agents/` holds `master_orchestrator` plus eight domain specialists — `missouri_law`, `federal_law`, `tort_law`, `ucc_law`, `civil_litigation`, `criminal_law`, `common_law`, `specialized_law` — plus `chief_justice` (37KB of instructions) as the review layer, and `SystemSelfDiagnostic` / `IntegrityAuditRoutine` workflows as self-audit. This is the three tiers, built. The gap rating is stale. |
| **AST structural chunking** | **Not practical, and a category error** | AST parsing is for *source code* — you parse a syntax tree because code has one. Statutes and opinions do not. The legally meaningful structure here is title → chapter → section → subsection, which LawMind already keys on directly (`recordCitationKeys` builds `rsmo:571.030` and `usc:42|1983` keys). Adopting "AST chunking" would mean inventing a parse tree for documents that already carry a better, citable structure. Skip it. |
| **Hybrid dense/sparse retrieval, cosine sim ≥ 0.82** | **Not practical as stated; and the threshold is actively dangerous here** | Base44 has MongoDB-style document entities and no native vector database, so there is nowhere to put an index or run an ANN query. You could bolt on an external vector store, but consider what it buys: for *citation verification* a similarity threshold is precisely the wrong tool. The guard's own header comment records that a fuzzy substring match previously let fabricated citations pass, and calls that "worse than no check at all." A 0.82 cosine threshold reintroduces exactly that failure class — a fabricated cite that is 0.85-similar to a real one would verify. Exact structured-key matching is the correct design for verification and it is already in place. Semantic retrieval could help *discovery* ("find me cases about X"), but that is a different job and should never share a code path with verification. |
| **Parallel fan-out to 32 sub-agents (TIRO)** | **Not practical at 32; partially covered at a sane width** | Deno serverless functions have hard execution limits — the same constraint driving the time-budget fixes in Section A. Thirty-two concurrent sub-agents each doing LLM work would blow both the time budget and the credit budget (`CreditUsage` and `CreditWatchdog` exist because cost is already a live concern). An `orchestrate-8-agents` function already exists, which is the right order of magnitude. The genuine insight in this row — that long sequential runs are a single point of failure — is real, and is better addressed by the resumable-cursor work in Section A than by fan-out width. |
| **Pydantic JSON-schema validation + chunk-ID source attribution** | **Partly covered; the attribution half is the valuable half** | Structured-output validation already happens in places (`bulk-draft-month` and others pass `response_json_schema` to the LLM). Pydantic itself is Python and irrelevant to a Deno/TypeScript runtime, but the principle is sound and partly implemented. The *source attribution* half is the genuinely valuable idea and it is where the real remaining gap is — see Proposal 2. Note `DataProvenanceLog` sounds like it covers this but does not: it logs entity/record/field change hashes, i.e. database mutation auditing, not "which source supports this sentence." |
| **Automated rule mapping / affirmative defense matrix / countersuit engine** | **Mostly already covered** | `compute-mo-deadline` + `shared/mo-deadline-engine.ts` + the `RuleTrigger` library do rules-based deadline computation with a `ComputedDeadline` entity, and notably refuse to persist a deadline derived from an unverified rule. `RebuttalMatrix`, `CaseArgument`, and `draft-counterclaim` cover the defense/countersuit ground. The one real gap adjacent to this row — modelling the *opponent's* best case — is already logged as "Adversarial Read Generator" (`ToolRequest` 6a770ef321a643c3f3ff9f00, status `new`). Approve that one rather than building anything new here. |
| **Strict single-checkpoint HITL** (`01_Pending_Approval` + notifications) | **Already covered, and better than the blueprint** | LawMind's human-in-the-loop gate is stronger than a staging folder: `GeneratedDocument.citation_status` plus `mayExport()` in `shared/citation-guard.ts` is a fail-closed gate enforced *in code* at every exit point (`export-to-google-docs`, `send-fax`, `build-master-pdf`). A folder convention can be bypassed by moving a file; a code gate cannot. `PendingEmailApproval` and `AssistanceRequest` cover the notification side. Do not replace a code gate with a folder gate. |

### Sheet 2 — "Elite setup instructions"

| Component | Verdict |
| --- | --- |
| **Base44 SuperAgent system instructions** | **Already covered.** `SuperAgentConversation` and `superagent-send-message` exist and are wired. Pasting a new instruction block over the existing agents would overwrite `chief_justice`'s 37KB of accumulated, case-specific rules — including the Kruse safety rules. Do not paste over them. |
| **Base44 App Builder 5-part prompt** ("auto-generate the UI pages, data tables, and background triggers") | **Not practical — actively risky now.** This instruction is written for a greenfield app. LawMind has 54 entities, ~175 functions and ~75 workflows in production. Running a generative App Builder prompt against a live app of this size invites schema collisions and duplicate triggers. There is already evidence of exactly this drift: two near-duplicate entities, `ToolRequest` (used) and `tool-request` (dead), and 106 `LegalModule` rows with press-release names and no mapped function. This is how that happens. |
| **OpenRouter gateway with `response_format: json_schema`** | **Not worth it.** The stated benefit — schema-constrained JSON output — is already available through Base44's own LLM integration (`response_json_schema` is in use today). Adding a separate gateway means a second API key, a second billing surface, a second failure mode, and a second thing for `CreditWatchdog` not to be watching. The one legitimate reason to add a gateway is model routing/failover; that is not what the sheet asks for. |
| **Google Workspace / PortEden OAuth, folders `00_Master_Statute_Database`–`07_Manual_Review`** | **Partly covered; the folder taxonomy is the leftover.** Google Drive is connected and heavily used — `DailyLibraryDriveBackup`, `DriveInboxScanner`, `RouteDriveFileToMatter`, `backup-library-to-drive`, `DailyGoogleDriveBackup` all exist. What does not exist is that specific numbered folder taxonomy. That is a filing-convention decision, not an engineering task, and it is cheap if Tyler wants it. Verifying OAuth folder permissions is sensible housekeeping regardless. |

**Blueprint bottom line.** The two sheets contain one genuinely valuable idea that LawMind has not yet built: **source attribution at the level of individual assertions** (the "chunk ID source attribution" half of the verification row). Everything else is either already built, already logged, or a poor fit for Base44's actual runtime. The sheets' framing — that LawMind is a single agent running shell scripts — is far behind the real app, and following them literally would mean overwriting working safety infrastructure.

---

## C. OCR and dedup heuristics for the dictionary import

For whoever is importing the two legal-dictionary sheets right now. These are ordered by value-per-effort. Grounded in the [post-OCR processing survey](https://adammo12.github.io/adamjatowt/cs21.pdf) and [Cleaning Dirty Books](https://arxiv.org/abs/2110.11934).

**Two facts to know before you start:**

1. `base44/functions/detect-duplicates/entry.ts` **does not cover `LegalTerm` or `LatinTerm`.** There is no dedup safety net on these entities. Anything you import lands unchecked.
2. `LegalTerm` has **no provenance field** — no `source_url`, no `import_batch`, no `verified_at`. Once these rows are in, there is no way to tell them from hand-curated rows, and no way to roll back one bad batch. **Stamp a batch identifier on every row you import, even into a spare text field, before you run the import.** That single move preserves your ability to undo this.

### C1. Alphabetical-neighbour check — highest value, nearly free

A dictionary is sorted. That sortedness is a free correctness oracle, and it is the single best artifact detector you have.

For each entry, compare its headword to the entries immediately before and after in source order. If a headword sorts outside its neighbours' range, it is almost always a scan artifact — a caught column header, a running footer, a page number, or text bled in from an adjacent column.

```
prev: "abandonment"
this: "eous conduct"      <- flag: sorts wrong AND starts mid-word
next: "abatement"
```

Tune it so a single out-of-order entry is *flagged*, not deleted — genuine dictionaries do contain legitimate ordering quirks (cross-references, "See also" stubs, alternate spellings).

### C2. Mid-word start detection

Flag any headword that:
- begins with a lowercase letter where the surrounding entries begin with capitals (or vice versa, inconsistently);
- begins with a fragment that is not a plausible word onset (`eous`, `tion`, `ment`, `ance` as an opening);
- is shorter than 3 characters, or is a single character plus punctuation;
- contains digits in a position no legal term would (`ab4ndonment`) — classic OCR character confusion.

Combined with C1 this catches most line-wrap and column-bleed damage.

### C3. De-hyphenation of line-wrapped text

Scanned columns break words at line ends. Join `(\w+)-\s*\n\s*(\w+)` into one token — **but only when the joined form is a known word and the hyphenated form is not.** Legal English has real hyphenated compounds (`quasi-contract`, `cross-claim`, `attorney-client`, `self-executing`) and blindly stripping hyphens corrupts them. The survey's guidance applies: treat hyphen-separated segments as *candidate* boundaries requiring separate validation, not as automatic joins.

Practical rule: join if `joined ∈ dictionary` and `hyphenated ∉ dictionary`; keep the hyphen if both are known; flag for review if neither is.

### C4. Canonicalising Latin maxims

Latin entries need their own normalisation pass because OCR mangles them more than English (unfamiliar to the engine's language model, often italicised, often with diacritics).

- Normalise whitespace and strip trailing punctuation before comparing.
- Case-fold and strip diacritics for the *match key*, but preserve the original for display.
- Expect and merge orthographic variants: `res judicata` / `res adjudicata`, `mens rea` / `mens-rea`, `certiorari` / `certiorari` with a broken `t`.
- Watch the `rn` → `m` and `cl` → `d` confusions, which are the two most common OCR bigram errors and both produce plausible-looking Latin.
- Build a match key of `lowercase + strip non-alphanumeric` (the same `squash()` approach `shared/citation-guard.ts` already uses) and dedupe on that, not on the raw string.

### C5. Known-term list matching

This is the survey's core technique and it is worth the setup. Any token not in the dictionary is a **non-word error** and is trivially detectable; errors that produce *real* words need context and are much harder. So:

- Validate each headword against a legal-term lexicon. **You already have one in the app** — the existing `LegalTerm`, `LatinTerm`, and `LegalThesaurus` rows are a ready-made known-term list. Use them.
- For a non-matching headword, generate candidates within Damerau–Levenshtein distance 2 and rank by frequency plus OCR-confusion weighting (`rn`/`m`, `cl`/`d`, `1`/`l`/`I`, `0`/`O`, `5`/`S`).
- **Flag, don't auto-correct.** The survey's own guidance is that threshold-based filtering reduces false positives; for a legal reference library the cost of a silent wrong "correction" is much higher than the cost of a review queue. Auto-correct only on an exact single-edit match to a known term with no competing candidate.

### C6. Deduplication

- Dedupe on the normalised match key from C4, not the raw headword.
- When two entries collide, keep the one with the **longer, better-formed definition** — the "canonical version" strategy from *Cleaning Dirty Books*, which picks the highest-quality digitisation among duplicates. Do not merge definitions; keep one and record the other's existence.
- Both source sheets may cover overlapping term sets. Run the dedup *across* both sheets and against the existing library, not just within each sheet.

### C7. Quality gate

Do not write low-confidence entries straight into the live library. Give each row a confidence score from C1–C5 and route anything below threshold to a review state. If there is no review state yet, that is Proposal 3 — but in the interim, **a batch stamp (C-preamble) plus a spreadsheet of flagged rows is enough** to keep this reversible.

---

## D. Five capability proposals

All five are logged in `ToolRequest` with `status: 'ai_scoped'`. None were built. Each closes a gap I verified in the code, not a gap I inferred.

I checked each against the existing queue and registry. Deliberately **not** proposed because they are already logged: citation verification at synthesis time and CourtListener quota backoff (both in `ToolRequest` 6a9678e11a1ed7af874fc11a), unsourced damages figures (6a770ef321a643c3f3ff9f01), cross-case daily brief (6a770ef321a643c3f3ff9eff), opponent's-best-case modelling (6a770ef321a643c3f3ff9f00), and module registry triage (6a770ef321a643c3f3ff9f02, already built).

### D1. Citation Guard Corpus Health Monitor — `backend_function`, moderate

**Gap:** The citation guard silently converts into a total export lockout as the case-law library grows, and nothing is watching for it.

`shared/citation-guard.ts` loads the full `Statute` + `CaseSummary` corpus on **every call**, bounded by `CORPUS_TIME_BUDGET_MS = 20000` and `MAX_PAGES_PER_ENTITY = 40`. If either bound is hit, `complete` goes false, status becomes `corpus_incomplete`, **every citation is flagged**, and `mayExport()` returns false — so nothing can be exported, faxed, or filed.

That is correct fail-closed design and I would not weaken it. The problem is that it is a **cliff, not a slope**, and it is on a collision course with the CAP bulk case-law ingestion that is actively running. The day the corpus stops loading in 20 seconds, every document in the app becomes unexportable at once, with no warning and no obvious cause. The failure will present as "the app stopped letting me file things," probably at the worst possible moment.

This is the highest-priority item in this report.

### D2. Quote and Pincite Verification Stage — `backend_function`, complex

**Gap:** The citation guard verifies that a case *exists* but not that it *says what the draft claims* — and existence-checking alone is documented as insufficient.

The guard's own header says so: *"SCOPE LIMIT: this checks that a citation EXISTS in the library. It cannot check that the cited authority says what the draft claims it says."* The 2026 benchmark literature confirms this is the binding limitation. [Who Checks the Citations?](https://arxiv.org/html/2606.21155v1) defines five error classes — non-existent citation, case-name mismatch, incorrect pincite, verbatim misquote, and content misrepresentation — and finds that detecting non-existent cases alone is not enough, with pincite verification often gated behind Westlaw/Lexis access.

LawMind currently catches classes 1 and 2 and is blind to 3, 4, and 5. The practical opening: the **Descrybe Legal Engine connector already exposes `verify_quote` and `get_case_passages`**, which addresses verbatim misquotes without a Westlaw subscription. That makes the hardest-to-reach error class reachable with a connector that is already available.

Given that this app exists to support pro se litigation, and that [roughly 1,490 decisions worldwide now involve AI-hallucinated material](https://gc.ai/blog/ai-hallucination-legal-cases), this is the substantive version of the blueprint's "source attribution" idea.

### D3. Reference-Library Provenance and Idempotency Keys — `entity`, moderate

**Gap:** Library entities have no provenance and no deterministic dedupe key, so imports cannot be attributed, audited, rolled back, or safely retried.

Two verified problems converge here:

- `LegalTerm` has no `source_url`, `import_batch`, or `verified_at` field. After today's dictionary import, an OCR-corrupted definition will be indistinguishable from a hand-curated one, and there will be no way to roll back one batch.
- More seriously: `sync-watchdog` re-invokes each stalled source's `recovery_function` **every 5 minutes**. Current best practice is at-least-once delivery with idempotent writes, and the app already knows this pattern — `CaseCalendarEntry` has an `idempotency_key`. The library entities do not. Every watchdog recovery cycle on an ingestion source is therefore a potential duplicate-row generator.

This is prerequisite for D4 and directly relevant to the import happening today.

### D4. Reference-Library OCR Artifact Scanner — `backend_function`, moderate

**Gap:** `detect-duplicates` does not cover `LegalTerm` or `LatinTerm`, so scanned-dictionary artifacts have no automated detection anywhere in the app.

Implements Section C as a re-runnable sweep: alphabetical-neighbour ordering, mid-word starts, de-hyphenation candidates, Latin canonicalisation, and known-term matching against the existing library. Flags rather than deletes.

Worth building even though the current import will be cleaned by hand — `DailyLegalTermScraper`, `ContinuousLegalTermScrape`, and `DailyEncyclopediaScraper` all keep adding entries indefinitely, so this is a recurring need, not a one-off.

### D5. Watchdog Recovery Confirmation — `backend_function`, quick — *possibly duplicate, see note*

**Gap:** `sync-watchdog` marks a source healthy because `invoke()` did not throw, never checking that the heartbeat actually advanced.

Full analysis in Section A4. Two-phase confirmation: leave the source in `recovering` after dispatch, record the pre-dispatch heartbeat value, and promote to `active` on a later tick only once the heartbeat has moved. Escalate on unconfirmed recoveries so a quietly-failing source produces an alert instead of a green dashboard.

**Note for triage:** this overlaps the in-flight watchdog repair. If that fix already confirms heartbeat advance before marking healthy, **decline this as a duplicate.** If it only changes *when* a source is marked healthy without changing *what counts as evidence*, this survives the fix.

---

## Sources

- [Cloud Run Jobs / Workflows: idempotent and resumable batch design](https://tomodahinata.com/en/blog/google-cloud-run-jobs-workflows-batch-async-idempotent-guide)
- [Idempotent AI agents: retry-safe patterns for production](https://www.buildmvpfast.com/blog/idempotent-ai-agent-retry-safe-patterns-production-workflow-2026)
- [Batch processing retry strategies](https://oneuptime.com/blog/post/2026-01-30-batch-processing-retry-strategies/view)
- [Retry with circuit breaker pattern](https://oneuptime.com/blog/post/2026-01-30-go-retry-circuit-breaker-pattern/view)
- [Exponential backoff with jitter: retry storms explained](https://web-alert.io/blog/retry-storms-exponential-backoff-jitter-explained)
- [Health checks vs heartbeats](https://blog.levelupcoding.com/p/health-checks-vs-heartbeats)
- [Survey of post-OCR processing approaches](https://adammo12.github.io/adamjatowt/cs21.pdf)
- [Cleaning Dirty Books: post-OCR processing for previously scanned texts](https://arxiv.org/abs/2110.11934)
- [Who Checks the Citations? Benchmarking legal hallucination detection](https://arxiv.org/html/2606.21155v1)
- [AI hallucination legal cases: a sanctions tracker (2026)](https://gc.ai/blog/ai-hallucination-legal-cases)
- [Kruse v. Karlen, ED111172 (Mo. App. E.D. Feb. 13, 2024)](https://caselaw.findlaw.com/court/mis-crt-app-eas-dis-div-two/115816278.html) — pro se appellant, appeal dismissed, $10,000 in Rule 84.19 damages for AI-fabricated citations. The safety comments throughout the codebase cite this accurately.
