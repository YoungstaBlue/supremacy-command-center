---
name: legal-citation-formatter
description: Formats and cleans legal citations in briefs, motions, and memos using Bluebook style and Missouri court conventions (Mo. banc, Mo. App. E.D./W.D./S.D., RSMo, Supreme Court Rules), including short forms, id., signals, and record cites. Use for "fix my citations", "Bluebook", "cite this case", or "how do I cite RSMo".
---

# Legal Citation Formatter

Puts every citation in a filing into consistent, court-appropriate form so the judge can find each authority and the filing reads as competent work.

## When to use
- Before filing any brief, motion, petition, or memo with legal authority in it.
- "How do I cite this Missouri case / statute / rule?"
- Converting a draft with inconsistent or incomplete citations.
- Not for: confirming that a citation is real and accurate (use `quote-and-cite-verifier`) or still good law (use `good-law-checker`).

## Gather first
- The draft (or the list of authorities) and the court it will be filed in.
- The court's local rules or any standing order on citation format.
- For record cites on appeal: how the legal file and transcript are paginated.

## Workflow
1. **Confirm every citation is real first.** Formatting a fabricated or wrong citation makes it look more credible, not less. Run `quote-and-cite-verifier` before or alongside this skill.
2. **Missouri cases.** Pattern: *Case Name*, [vol.] S.W.[2d/3d] [first page], [pin] ([court] [year]).
   - Supreme Court of Missouri: `(Mo. banc 2009)` for en banc decisions.
   - Court of Appeals: `(Mo. App. E.D. 2015)`, `(Mo. App. W.D. 2015)`, `(Mo. App. S.D. 2015)`. Always include the district.
   - Example form: *Parktown Imports, Inc. v. Audi of America, Inc.*, 278 S.W.3d 670, [pin] (Mo. banc 2009).
3. **Federal cases.**
   - U.S. Supreme Court: *Name*, [vol.] U.S. [page], [pin] ([year]). Use S. Ct. only if no U.S. Reports page exists yet.
   - 8th Circuit: *Name*, [vol.] F.3d / F.4th [page], [pin] (8th Cir. [year]).
   - District courts: *Name*, [vol.] F. Supp. 3d [page] (E.D. Mo. [year]); unreported: case number, WL or LEXIS cite, and exact date.
4. **Statutes and rules.**
   - Missouri statutes: `§ 508.010, RSMo` with the revision or supplement year where it matters (e.g., `RSMo 2016` or `RSMo Cum. Supp. [year]`). Missouri courts commonly write "Section 508.010, RSMo 2016" in text; use one style consistently.
   - Missouri Supreme Court Rules: `Rule 55.27(a)(6)`; Missouri courts cite these as "Rule __" without a source abbreviation.
   - Missouri Constitution: `Mo. Const. art. V, § 2`.
   - Federal: `42 U.S.C. § 1983`; `Fed. R. Civ. P. 12(b)(6)`; `Fed. R. Evid. 801(d)(2)`; `U.S. Const. amend. IV`.
5. **Pin cites.** Every proposition drawn from a case needs a pin cite to the page where it appears. A citation without a pin for a specific proposition is incomplete.
6. **Short forms.** After the first full cite: *Parktown*, 278 S.W.3d at [pin]. Use *Id.* only when citing the immediately preceding authority with no intervening citation. Statutes: `§ 508.010`.
7. **Signals.** No signal = authority directly states the proposition. *See* = supports it by inference. *See also*, *Cf.*, *But see* used accurately. Do not use a signal to dress up a weak cite.
8. **Parentheticals.** Add an explanatory parenthetical when the reason the case supports the point is not obvious; begin with a present participle ("holding", "finding").
9. **Subsequent history.** Include it when relevant (e.g., `aff'd`, `rev'd`, `cert. denied` only if recent and relevant). Never cite a vacated opinion without saying so.
10. **Record citations on appeal.** Missouri Rule 84.04 requires specific page references to the legal file or transcript for factual statements in briefs; use the format the record uses (e.g., "(L.F. 12)", "(Tr. 45)") — confirm the court's preferred abbreviations. Federal appeals cite the appendix or record per local rule.
11. **Final pass.** Italicize or underline case names consistently, check every party name spelling against the source, and build a table of authorities if the brief requires one.

## Output
- The corrected citations in place, or a table: `Original | Corrected | Problem fixed | Needs verification?`
- A list of citations that could not be completed (missing pin, unknown reporter page, unclear court) for the user to fill from the source.

## Pitfalls
- Omitting the Court of Appeals district or the "banc" designation; Missouri courts expect it.
- Citing a case without a pin cite for a specific proposition.
- Misusing *Id.* after an intervening citation.
- Citing unpublished or memorandum decisions as if they were precedent.
- Formatting a citation the user has not verified exists — never fill in a volume or page number from memory.
- Mixing citation styles within one filing.

## Verify before relying
- Pull verbatim text of every statute/rule cited via `statute-lookup` (or Descrybe `search_laws_and_rules`); check case law is still good law (CourtListener / Descrybe treatment) before citing.
- Check local rules for any required citation form.
- Legal information, not legal advice; recommend counsel/legal aid for high-stakes decisions.

## Related skills
- `quote-and-cite-verifier` — confirm each cite and quote is accurate before formatting.
- `good-law-checker` — add subsequent history and confirm validity.
- `precedent-hierarchy-analyzer` — decide which authorities to cite at all.
- `lawmind-god-drafter` — drafting the filing the citations go into.
