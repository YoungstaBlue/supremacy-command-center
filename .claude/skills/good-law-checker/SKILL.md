---
name: good-law-checker
description: Confirms a case, statute, or rule is still good law before citing it - overruled, reversed, vacated on transfer, superseded, amended, repealed, or held unconstitutional. Use for "is this still good law", "Shepardize", "KeyCite", "was this overruled", or "was this statute amended".
---

# Good Law Checker

Runs a validity check on every authority before it goes into a filing, so nothing overruled, vacated, amended, or repealed is relied on.

## When to use
- Before filing anything that cites cases, statutes, or rules.
- "Is this case still good law?", "Was this statute changed?", "Is this the current rule?"
- The opposing party cites an old case or a case from a court of appeals that may have been transferred.
- Not for: confirming a quotation or pin cite matches the source (use `quote-and-cite-verifier`).

## Gather first
- The list of authorities with full citations (or the draft containing them).
- The relevant date: when the events occurred (which version of a statute applies) and the filing date.
- The proposition each authority is cited for — a case can be good law on one point and overruled on another.

## Workflow
1. **Resolve each citation.** Confirm the case exists with that name, court, year, volume, and page (CourtListener `search` with `citation`, or Descrybe `find_case_from_reference`). If it cannot be found, stop: treat it as unverified and do not cite it.
2. **Case history (direct).** Check what happened to the same case later:
   - Reversed, vacated, or modified on appeal.
   - Missouri: a Court of Appeals opinion in a case later transferred to the Supreme Court of Missouri is vacated by the transfer — cite the Supreme Court opinion instead.
   - Rehearing granted or opinion withdrawn and substituted.
   - Federal: cert. granted and decided; en banc rehearing vacating a panel opinion.
3. **Case treatment (indirect).** Search for later cases citing it (CourtListener citing opinions / Descrybe `find_cases_that_cite`) and look for: "overruled", "abrogated", "disapproved", "superseded by statute", "no longer good law", "limited to its facts", "declined to follow". Focus on higher and same-level courts in the controlling jurisdiction.
   - Missouri Supreme Court opinions sometimes overrule lists of older court of appeals cases "to the extent" they conflict; check whether the case appears in such a list.
   - A federal decision on a federal question can be displaced by a later U.S. Supreme Court decision without naming it — check whether the controlling test changed.
4. **Statutes.**
   - Confirm the current text and the version in force on the relevant date via `statute-lookup` (check the history/amendment notes).
   - Look for repeal, renumbering, amendment, or transfer to another section.
   - Search for decisions holding the statute (or part of it) unconstitutional or preempted.
   - For criminal statutes, use the version in effect on the offense date.
5. **Court rules.** Missouri Supreme Court Rules and federal rules are amended periodically (federal amendments usually take effect December 1). Confirm the current text and the effective date of the last amendment; confirm local rules and standing orders are current.
6. **Proposition check.** Confirm the case still supports the specific proposition — a later case may have narrowed that point even if it did not overrule the case.
7. **Status label.** Assign each authority one status: Good / Caution (negative treatment on other points, or narrowed) / Bad (overruled, reversed, vacated, repealed) / Unverified (could not confirm).

## Output
| Authority | Proposition cited for | Direct history | Negative treatment found | Statute/rule version check | Status | Replacement authority |
|---|---|---|---|---|---|---|

Then: authorities to remove, authorities to replace (with the replacement only if verified), and anything that needs a human check in Westlaw/Lexis or the court's own website.

## Pitfalls
- Assuming a frequently cited case is good law; older Missouri appellate cases are regularly overruled.
- Citing a Missouri Court of Appeals opinion that was vacated when the Supreme Court took transfer.
- Quoting the current version of a statute when an earlier version governs the events.
- Treating absence of results in a free database as proof of validity; free tools have coverage gaps. Say so when a check is incomplete.
- Missing implicit overruling when the controlling test itself changed (for example, Chevron deference ended with Loper Bright Enterprises v. Raimondo, 603 U.S. 369 (2024)).
- Not disclosing adverse controlling authority; courts expect candor even from self-represented parties.

## Verify before relying
- Pull verbatim text of every statute/rule cited via `statute-lookup` (or Descrybe `search_laws_and_rules`); check case law is still good law (CourtListener / Descrybe treatment) before citing.
- If a check is incomplete, label the authority "Unverified" rather than "Good".
- Legal information, not legal advice; recommend counsel/legal aid for high-stakes decisions.

## Related skills
- `quote-and-cite-verifier` — confirm quotes and pin cites after validity is confirmed.
- `statute-lookup` — current and historical statute text.
- `legal-citation-formatter` — add subsequent history in proper form.
- `lawmind-legal-research` — find replacement authority for anything that fails.
