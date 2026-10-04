---
name: evidence-timeline-builder
description: Builds a source-cited chronology from case evidence - documents, texts, emails, video, reports, testimony - flagging conflicts, gaps, and deadlines. Use for "build a timeline", "chronology of events", "put my evidence in order", "what happened when", or preparing a statement of facts for a motion or trial.
---

# Evidence Timeline Builder

Turns a pile of evidence into a single chronology where every entry is tied to a pinpoint source, conflicts
between sources are surfaced, and missing proof is listed as gaps to fill.

## When to use
- Starting a new matter or organizing discovery
- Drafting a statement of facts, summary judgment statement of uncontroverted facts, or trial outline
- Preparing to impeach a witness whose account conflicts with documents
- Checking limitations or notice deadlines that run from an event date
- Not for: legal analysis of the events (use `legal-issue-spotter` or `elements-checklist-builder`)

## Gather first
- The evidence set (file list or uploaded documents) and the key people involved
- The claims/charges at issue, so the timeline can be tagged to elements
- Time zone of each digital source (phone exports, body-cam, server logs often differ)

## Workflow
1. Inventory every source with a short ID (e.g., EX-01, TXT-03, VID-02, DEP-Smith). Record the source's own date
   (created/sent/recorded) separately from the dates of events it describes.
2. Extract events. One row per discrete event: date, time (with zone), actor, action, location, and the exact
   source with pinpoint (page, line, timestamp, message number, Bates number). Quote short key language verbatim.
3. Normalize: convert times to one zone; mark approximate dates ("on or about") and their basis; never fill a
   date by inference without labeling it inferred.
4. Classify reliability: document created at the time, later recollection, party statement, third-party record,
   or unverified. Note whether each source is likely admissible and how (see `hearsay-analyzer`,
   `authentication-foundation-builder`).
5. Detect conflicts: where two sources disagree on time, sequence, or content, keep both rows and flag the
   conflict with both citations. These are impeachment and credibility points.
6. Detect gaps: periods with no evidence, events asserted without a source, elements with no supporting row.
   List what evidence would fill each gap (records request, subpoena, deposition, Sunshine/FOIA request).
7. Tag deadlines: compute any limitations, notice-of-claim, answer, or appeal deadlines that run from a timeline
   event, and route the computation to the deadline skill rather than estimating.
8. Tag each row to the claim element(s) or defense it supports.

## Output
| # | Date | Time (zone) | Event | Actor(s) | Source ID + pinpoint | Verbatim excerpt | Reliability | Element(s) | Conflict/Gap flag |
|---|---|---|---|---|---|---|---|---|---|
- Then: Conflicts list (row pairs and why they matter); Gaps list (what is missing and how to get it);
  Deadline triggers (event, rule to check, computed by which skill); Source index (ID, description, location).
- Optionally a narrative statement of facts where every sentence carries a citation to the source index.

## Pitfalls
- Unsourced facts in a statement of facts; courts disregard them, and summary judgment facts need record citations.
- Mixing the date a document was created with the date of the event it describes.
- Time-zone errors in phone and video data that create false contradictions.
- Smoothing over conflicts; the other side will find them. Flag them.
- Including personal identifiers (SSNs, minors' names, account numbers) that must be redacted in court filings.

## Verify before relying
- Re-check each pinpoint against the source before the timeline is used in a filing.
- Recompute any deadline from the actual event and service dates with the deadline skill.
- Legal information, not legal advice.

## Related skills
- `exhibit-list-and-trial-binder` — convert sources into numbered exhibits
- `impeachment-and-credibility` — use flagged conflicts
- `elements-checklist-builder` — map rows to elements
- `mo-deadline-calculator` and `statute-of-limitations-checker` — compute deadlines from events
- `lawmind-case-tools-manager` — file and name the underlying documents
