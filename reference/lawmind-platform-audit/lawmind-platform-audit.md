---
title: "LawMind Platform Audit"
source: https://claude.ai/artifact/XJF4CBRr46iBWfT1s3BPjo
shelf: "LawMind platform notes"
synced: 2026-10-15
---
Read-only audit · Base44 workspace

# LawMind Platform Audit

Security, data-integrity and automation review of 🔯The7Garner🔱Law4Firm🔯 — the Missouri legal case-management platform, its 16 super-agents, and the 76 workflows running behind them.

**App** 6a53429210c1ce40398a53a8
**Audited** 3 September 2026
**Method** static read + live entity queries

**Nothing was changed.** Every tool call in this audit was a read. No entity, function, workflow, agent or file was created, edited or deleted. Fixes below are recommendations only, pending your go-ahead.

## What's in the system

Two smaller apps (PayloadForge, Untitled) were inventoried but not audited — this report covers the legal platform only.

54

Entities

164

Backend fns

76

Workflows

16

Agents

17

Connectors

~1,184

Sched. runs/day

## Broken right now

Live `SyncHeartbeat` state, queried directly. Five sources have been dead for 20 days and the system has stopped reporting it — `sync-watchdog` skips any source at 5 consecutive stalls, and `system-health` doubles the alert threshold on each repeat, so these rows have escalated themselves into silence.

Sync sources downlast heartbeat 2026-08-14 · verified 2026-09-03

| Source | Recovery fn | Stalls | Threshold | Last error |
| --- | --- | --- | --- | --- |
| court_docket_sync | `sync-court-dockets` | 5 | 720m | HTTP 524 |
| library_scraper | `bulk-scrape-library` | 5 | 720m | HTTP 524 |
| echo_system | `echo-orchestrator` | 5 | 720m | HTTP 524 |
| drive_backup | `backup-library-to-drive` | 5 | 1440m | HTTP 524 |
| superagent_sync | `superagent-sync` | 5 | 720m | HTTP 502 |
| pending_sync_queue | `process-pending-sync-queue` | 0 | 15m | reports **active** — see W-4 |

**court_docket_sync is the feed for court deadlines.** It has not run since 14 August. Anything downstream that assumes docket freshness — deadline monitors, calendar sync, the urgent drafter — has been working from three-week-old data.

## Critical

Ordered by what a competent attacker or a bad day reaches first. Each finding cites the file and line it came from.

SEC-1The email intake endpoint has no authentication

`email-case-intake` has no `base44.auth.me()` call anywhere in the file. A comment asserts it "runs as service role — triggered by workflows, not end users," but nothing enforces that. It then reads arbitrary Gmail message IDs as service role and returns sender, subject and an LLM summary of the body in the HTTP response.

export default async function (req: Request): Promise<Response> {
const base44 = createClientFromRequest(req);
const body = await req.json().catch(() => ({}));
const messageIds: string[] = body.message_ids || [];

**Why it's certain:** `approve-pending-email` uses the identical function shape and *does* check auth and admin — which proves this shape is HTTP-routable and that auth is the function's own job.

**Impact:** unauthenticated read of privileged attorney-client email, plus service-role writes to `CaseDocument` and `Notification`.

base44/functions/email-case-intake/entry.ts:75-79

AI-1A scheduled job writes AI-invented case law into the research library

`AutoCaseGenerator` runs **every 5 minutes** and asks an LLM for "20 real, accurate appellate case summaries," then bulk-creates the result straight into `CaseSummary` with **no citation verification** — even though `verify-citations-courtlistener` exists in this same codebase.

Those rows are indistinguishable from genuinely scraped CourtListener records. They feed `link-casesummary-findings`, `evidence-precedent-match`, and document drafting. At full rate that is **5,760 synthetic case summaries per day**.

Your own `PROJECT_KNOWLEDGE.txt` forbids exactly this: *"Prioritize Retrieval-Augmented Generation over free-form generative text for factual accuracy"* and *"never hallucinate attorneys/parties."*

**This is the finding I would act on first.** Fabricated authority sitting in the library is how a bad citation reaches a filed pleading.

base44/workflows/AutoCaseGenerator.jsonc · functions/auto-generate-cases/entry.ts

AI-2An LLM silently rewrites statutory text every morning

`LibraryContentVerification` fires daily at 09:00 and runs `verify-library-content` with `auto_fix: true`. On medium-or-high model confidence it writes `verdict.corrected_content` directly into `Statute.body`, `CaseSummary.summary`, `LegalTerm.definition` and `EncyclopediaArticle.body` — then sends a notification after the fact.

It also calls `InvokeLLM` directly rather than `guardedInvokeLLM`, so this spend is uncapped and invisible to the credit ledger.

**Fix shape:** corrections should queue for human review, not overwrite primary law in place.

base44/functions/verify-library-content/entry.ts

AG-1The one agent with no honesty guardrails is the one with drafting tools

Fifteen of your sixteen agents carry an explicit anti-fabrication rule. `library_curator` carries none — no "never fabricate a citation," no retrieval-first rule, no verbatim-quote rule, no disclaimer. Its only honesty instruction concerns ingestion bookkeeping.

It nonetheless holds `generate-legal-document`, `generateAffidavit`, `legalAnalysis` and `organize-case-docs`.

legal_research "NEVER invent a statute, case name, citation, date, or definition"
chief_justice "NEVER fabricate a date, citation, party, or fact"
god_drafter "Never invent citations — cite only retrieved records verbatim"
library_curator — none —

base44/agents/library_curator.jsonc

AG-2No prompt-injection defense exists, and the scraper agent is told to act on what it ingests

A grep of the entire repository for `ignore previous`, `prompt injection`, `untrusted` and `injection` returns two hits, both unrelated. There is no injection handling anywhere.

`library_curator` scrapes untrusted external text at scale — Cornell LII, govinfo, CourtListener, the ~6.7M-case Caselaw Access Project — and is then instructed:

"NEVER ask the user 'should I continue?' between scrapers — just chain them"
"use your new cross-node tools (legalAnalysis, generate-legal-document,
organize-case-docs) to kick off analysis/drafting/organization on the
freshly ingested material... without handing back to the user between steps."

Combined with AG-1, that is untrusted third-party text flowing into a drafting tool with no adversarial handling and no guardrails in between. The filing gate (below) stops it becoming a filing — but it will poison the library that every other agent treats as ground truth.

OPS-1Synthetic case generation is eating the credit budget the deadline drafter needs

Live `CreditUsage` shows repeated cap breaches: `2026-09-01` at 105/100 with **398 blocked calls**; also 08-21 (103/100), 08-17 (101/50), 08-14 (103/100), 08-10 (109/100). A code comment in `system-health` cites 1,046 blocked calls on 2026-07-24.

The mechanism is a timezone mismatch. `AutoCaseGenerator` runs on **UTC** 5-minute intervals and the cap resets on UTC date, so it drains the budget from 00:00 UTC. `UrgentDeadlineDrafter` (06:00 Chicago) and `BlackAndBlueCannons` (12:00 Chicago) both fire *after* the money is gone and throw `CreditLimitError`.

**A court-deadline drafting system is being starved by a workflow that invents case law.** Both critical findings resolve with the same switch.

*Currently mitigated:* no CreditUsage rows for 09-02 or 09-03 and the watchdog reads 0/100, so AutoCaseGenerator appears paused — but the configuration is intact and will recur if re-enabled.

OPS-2Failure alerting is structurally disabled after five stalls

Once a sync source reaches 5 consecutive stalls, `sync-watchdog` skips it permanently and never alerts again:

if (hb.status === 'error' && hb.consecutive_stalls >= 5) continue; // exhausted

`system-health` compounds it by doubling the alert threshold on each repeat — `Math.min((h.threshold_minutes || 15) * 2, 720)` — which is why the dead rows now sit at 720 and 1440 minutes. The system is currently incapable of telling you that docket sync is down.

base44/functions/sync-watchdog/entry.ts:36 · functions/system-health/entry.ts

## High

SEC-2PACER and eFiling passwords are stored in plaintext and sent to the browser

Both credential entities declare the password as a bare `"type": "string"` — no encryption, no hashing, no write-only marker. The frontend then reads them back on every Settings load and renders them into an input with a reveal toggle.

pacer_password: list[0].pacer_password || '', // PacerCredentialsSettings.jsx:27
mo_efile_password: ... // MoEfileCredentialsSettings.jsx:21

**Correctly scoped, wrongly stored.** RLS on both entities is owner-only on all four operations — `{"read": {"created_by_id": "{{user.id}}"}}` — so this is not cross-user exposure. But the secret never needs to leave the server.

SEC-3The MCP server's write denylist is defeated on the read path

`mcp-server` defines `ALL_ENTITIES` and a `WRITE_DENYLIST` that explicitly protects `PacerCredential` and `MoEfileCredential`. But `ALL_ENTITIES` is never used for validation — its only reference in the file is `total: ALL_ENTITIES.size`. The read tools accept any entity name:

const ent = base44.entities[entity];
if (!ent) return err(`Unknown entity "${entity}". ...`);

Any connected MCP client calling `lawmind_query_entity({entity:"PacerCredential"})` gets the row back with the password in cleartext — into a third-party model's context and transcript.

base44/functions/mcp-server/entry.ts:36,39,162

SEC-4Inbound email can exfiltrate the case roster and misfile itself

`email-intake-utils.ts` loads 300 Cases and 500 CaseRosters into the classification prompt alongside attacker-controlled body text, then uses the model's `matched_case_id` and `summary` without validation. A crafted email can instruct the model to emit the roster into `summary` (stored as `ai_summary`, echoed into a Notification) or route hostile content into any case.

Independent of SEC-1 — this survives fixing the auth hole.

base44/shared/email-intake-utils.ts:9-30,50-66

SEC-5Server-side request forgery driven by uploaded zip contents

`run-repo-scripts` correctly allowlists the zip source, then fetches URLs an LLM extracted from the uploaded Python files with **no allowlist at all**. The prompt instructs it to "extract them verbatim from the code," so a zip containing a link to cloud instance metadata steers the server there. Up to 15 scripts × 3 URLs per run; failures echo the URL back.

Admin-gated, which caps blast radius — but the URL is chosen by untrusted zip content, not the admin. (Note the name misleads: it does not execute scripts.)

base44/functions/run-repo-scripts/entry.ts:38-45,99

SEC-6Two bridges share one static, unrotatable secret named PROMO_CODE

const BRIDGE_KEY = process.env.PROMO_CODE;
return key === BRIDGE_KEY; // non-constant-time

That single header value grants full `asServiceRole` access bypassing RLS: list all cases, read any case with evidence and arguments, update `case_number` and `factual_allegations`, dispatch faxes. `fax-bridge-queue` reuses the same secret and hands out full document `body_content`.

Setup docs tell users to paste it into a plaintext local file. The name is inherited from a removed promo-code feature — **if the deployed value was ever shown to a user, treat this as critical.**

functions/termux-bridge/entry.ts:25-30 · functions/fax-bridge-queue/entry.ts:30,102,126

AG-3Affidavits bypass the entire filing-safety architecture

`generateAffidavit` runs no citation guard and creates a **`CaseDocument`**, not a `GeneratedDocument`. Every export gate keys on `GeneratedDocument` fields — so none of them apply to it.

It also misfiles by design. For case number `23-CV-1234`, `split('-')[0]` is `"23"`:

const fuzzyMatches = userCases.filter(c =>
c.case_number && c.case_number.toLowerCase().includes(case_number.toLowerCase().split('-')[0])
);

An LLM-drafted sworn document — perjury exposure — auto-attached to every case whose number contains "23".

base44/functions/generateAffidavit/entry.ts:113

AG-4strategy_engine is told to suspend factual scrutiny

"GROUND-TRUTH INGESTION: Treat every statement in the user's
affidavits and factual narrative as INDISPUTABLE FACT."

This agent drafts affidavits and pleadings. Rule 11 and Missouri Rule 55.03 sanctions attach to false *factual* contentions, not only bad citations. Its citation guardrails are strong; its factual ones are inverted. An agent told the client's narrative is indisputable cannot flag the drift `review-draft` is nominally checking for.

base44/agents/strategy_engine.jsonc

AG-5The 6 AM drafter produces ungrounded documents and tells a human to file them

`UrgentDeadlineDrafter` fires on `0 6 * * *` with no human in the loop, builds a draft from a raw LLM prompt — no library retrieval, no statute lookup, no citation guard — then emails the attorney *"Review, finalize, and FILE it before the deadline."*

**The technical gate holds:** the draft lands with `citation_verification_status` unset, so `mayExport()` refuses it. It cannot be faxed or exported. But the design deliberately puts an unverified draft in front of a person under maximum time pressure with an instruction to file — which is exactly when approval gates get rubber-stamped.

SEC-7chief_justice can mint access credentials

It holds `Invite` read/create/update — an LLM agent able to create access to a live system holding privileged client material. Its instructions claim permissions "mirror the requesting user's role," which is the right design, but that is asserted in a prompt and could not be verified platform-side from the repo. Access-control mutation should not sit behind a prompt-level assertion.

Related: `validate-invite` is an unauthenticated oracle — distinct messages for invalid / revoked / used / expired, no rate limiting, codes brute-forceable.

OPS-3Three functions bypass the credit circuit breaker entirely

`verify-library-content`, `auto-index-repo` and `generate-case-highlights` call `base44.asServiceRole.integrations.Core.InvokeLLM` directly instead of `guardedInvokeLLM`. Their spend is uncapped, uncounted, and absent from the `CreditUsage` ledger — so the Credit Watchdog under-reports real spend by an unknown margin.

## Automation load

49 scheduled workflows produce ~1,184 runs/day. Four of them account for 81% of it. Several are outright redundant — `sync-watchdog` already invokes `process-pending-sync-queue` at 3× the rate the separate schedule does, and `system-health` invokes both watchdogs hourly on top of their own 5-minute crons.

| Workflow | Schedule | Runs/day | Share |
| --- | --- | --- | --- |
| AutoCaseGenerator | `*/5 min` UTC | 288 |  |
| SyncWatchdog | `*/5 * * * *` UTC | 288 |  |
| PipelineWatchdog | `*/5 * * * *` UTC | 288 |  |
| EightTitleScraperRotation | `hourly` ×9 fns | 216 |  |
| ProcessPendingSyncQueue | `*/15 * * * *` | 96 |  |
| BulkLibraryScraper | `hourly` ×4 fns | 96 |  |

**Consolidation available:** retiring `AutoCaseGenerator`, merging the two 5-minute watchdogs, dropping the redundant queue schedule, and folding the scraper, health-check, backup, deadline and SuperAgent families into single drivers takes you from ~1,184 to ~357 runs/day — a **70% reduction**, 49 scheduled workflows down to about 22.

W-4A permanent recovery loop reports success 288 times a day

`pending_sync_queue` shows `status: active, consecutive_stalls: 0` with `last_recovered_at` of today — but `last_heartbeat` still reads **2026-08-14T10:55**. `process-pending-sync-queue` never writes the heartbeat back, so every 5-minute watchdog run finds it stalled, "recovers" it, and marks it active again.

W-5One uploaded document triggers roughly three uncapped LLM calls

`InstantDriveMatterRouting` and `RouteDriveFileToMatter` call the same function on the same trigger — only the second has a guard condition. Each update re-fires `GenerateCaseHighlights`, which has no trigger condition and calls `InvokeLLM` unguarded. The loop terminates only because `route-drive-file-to-matter` checks `drive_organized` — an idempotency check inside a function is the sole thing preventing an infinite entity-trigger loop.

W-6The repo indexer duplicates itself into the library daily

`auto-index-repo` de-dupes only within a batch and never checks existing records before `bulkCreate`. Every day at 10:00 it re-creates the same Statute / LegalTerm / CaseSummary / GeneratedDocument rows. Each new GeneratedDocument then fires backup *and* calendar workflows — so duplicate junk becomes Google Calendar events.

DATA-1Loose ends in the data model

`User` is the only entity with **no RLS block at all**, and it carries the `role` field. Worth confirming platform-side that role is not user-writable — that would be privilege escalation to admin.

`ToolRequest` and `tool-request` are duplicate entities with identical 12-field shapes. 25 fields across the schema store JSON inside string columns — the same pattern that silently lost 159 documents per your own notes; `Case.linked_articles` still uses it (capped at 15, which mitigates it).

The `CreditUsage` ledger is polluted: rows with `date: "llm_cache:gemini_3_1_pro:1m8etpw"` — cache keys written into the date field. `purge-credit-usage-duplicates` exists but is wired to no workflow.

W-7Documented dead ends still running

`PROJECT_KNOWLEDGE.txt` lists SuperAgent as *"DO NOT RETRY"*, yet three workflows plus `system-health` still call it and its heartbeat has been erroring since 14 August. `DailyMissouriCaseNetCheck` runs daily against a source your notes record as permanently CAPTCHA-blocked — 365 guaranteed failures a year.

## What's built well

### The filing gate is the strongest thing in this system

- **Nothing reaches a court without a human click.** `send-fax` and `fax-bridge-queue` are the only paths out, and **neither appears in any of the 16 agents' tool configs** — no agent can fax. Both enforce four conditions: `ready_to_file`, empty `unverified_citations`, `mayExport()` passing, and `human_approved_at` set.
- **`human_approved_at` is written in exactly one place in the entire codebase** — `DraftReview.jsx:178`, a person clicking approve. No backend function and no agent can set it.
- **The citation guard fails closed.** `citation-guard.ts` uses exact structured-key matching rather than substring, pages the full corpus, treats `corpus_incomplete` as unverified, and documents its own contract: *"A guard that throws means UNVERIFIED, never clean."* It's also honest about its limit — it checks a citation exists, not that it says what the draft claims.
- **The gate was hardened after a real bypass.** A comment in `fax-bridge-queue` records the fix: *"A draft could be queued and printed at a clerk's office without a person ever reading it."*
- **No fabricated odds.** A grep for probability, odds, likelihood and win-rate language across all 16 agents returns nothing. The only quantitative legal output is `tort_law`'s Low/Mid/High damages ranges, and sourcing is required against RSMo § 538 caps. For legal software this is the right call and it looks deliberate.
- **The 8 specialty lenses are correctly scoped** — read-only on every entity, zero backend functions, zero write access, each carrying a retrieval-first rule and a disclaimer.
- **Clean on the usual suspects:** no hardcoded secrets (both matches are placeholders), no zip-slip, no SQL/NoSQL injection across 108 template-literal fetches, and the PACER password is never logged and only ever sent to `pacer.login.uscourts.gov` over TLS.
- **Real resilience where it counts:** `scrape-courtlistener` handles 429 with pre-flight quota checks and inter-request sleeps; `bulk-scrape-cap` is time-budgeted with resumable cursors; `master-legal-pipeline` uses circuit breakers.

## Suggested fix order

Sequenced by risk removed per unit of effort. Nothing here has been done — say the word on any line and I'll take it.

1. **Disable AutoCaseGenerator.** One toggle. Stops fabricated case law entering the library, frees the credit budget the deadline drafter needs, and removes 288 runs/day.Resolves AI-1 and OPS-1
2. **Reset the five exhausted heartbeats and fix the `continue`-past-exhausted logic** so failures alert again. Court docket sync has been dark for 20 days.Resolves OPS-2, restores visibility on the deadline feed
3. **Add an auth check to `email-case-intake`.** A few lines, matching the pattern already in `approve-pending-email`.Resolves SEC-1
4. **Set `auto_fix: false` on LibraryContentVerification** and queue corrections for review instead of overwriting statutes.Resolves AI-2
5. **Enforce `ALL_ENTITIES` as a read allowlist in `mcp-server`** and exclude both credential entities.Resolves SEC-3
6. **Make the two password fields write-only server-side** and stop the Settings components reading them back.Resolves SEC-2
7. **Give `library_curator` the anti-fabrication block the other fifteen agents have** — or remove its drafting tools. Either closes it.Resolves AG-1, reduces AG-2
8. **Point `generateAffidavit` at `GeneratedDocument`** so the filing gate applies, and fix the `split('-')[0]` case match.Resolves AG-3
9. **Rotate the bridge secret off `PROMO_CODE`** to a dedicated, rotatable key with constant-time comparison.Resolves SEC-6
10. **Route the three unguarded functions through `guardedInvokeLLM`** so the credit ledger tells the truth.Resolves OPS-3
11. **Then the structural merges** — watchdogs, scrapers, backups, deadline family. Lower risk, 70% fewer scheduled runs.~827 runs/day saved

**Coverage, stated honestly.** Read in full: all 54 entity schemas, all 16 agent definitions, all 76 workflows, 25 high-risk backend functions, `citation-guard.ts`, `email-intake-utils.ts`, `silent-sync.ts`, `credit-guard.ts`, and the settings components. Grepped across the remaining ~135 functions for auth presence, secrets, credential handling, `mayExport` enforcement and unsanitized URL interpolation — their business logic was not read line by line. Live queries against `SyncHeartbeat`, `CreditUsage`, `PendingEmailApproval` and `CaseSummary`. Not examined: `src/` beyond the two settings components, the connector configs, and the two other apps in the workspace. One item I could not verify from the repo and flag as open: whether `User.role` is writable by its owner, and whether the four highest-privilege agents' `include_other_conversation_context` key is a real schema field or an inert typo — both need a platform-side check.
