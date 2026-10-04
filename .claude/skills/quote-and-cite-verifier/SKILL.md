---
name: quote-and-cite-verifier
description: Verifies every quotation, pin cite, case name, and characterized holding in a draft against the actual source text, catching fabricated or AI-hallucinated citations before filing. Use for "check my citations", "verify these quotes", "is this case real", "cite check", or before filing any brief or motion.
---

# Quote and Cite Verifier

A line-by-line cite check: every authority in a draft must exist, say what the draft says it says, and appear at the page cited.

## When to use
- Before filing any document that cites or quotes authority — mandatory for anything drafted with AI assistance.
- "Is this case real?", "Does this case actually say that?", "Check my pin cites."
- Reviewing the other side's brief for misquotes or mischaracterized holdings.
- Not for: whether the authority is still good law (use `good-law-checker`) or citation format (use `legal-citation-formatter`).

## Gather first
- The draft document.
- Access to the sources: CourtListener / Descrybe for cases, `statute-lookup` for statutes and rules, or the user's own copies.
- Which filing and court, so the stakes and any local rules on citation are known.

## Workflow
1. **Extract every citation and quotation.** Number each: case cites, statute/rule cites, record cites, quotations (with or without a cite), and every sentence that characterizes what an authority holds. CourtListener `extract_citations` can pull case citations from text.
2. **Existence check (cases).** Resolve each case by citation and by name (CourtListener `search` with `citation`; Descrybe `find_case_from_reference`). Confirm: party names, court, year, volume, reporter, first page. Any mismatch is a red flag. If the case cannot be found at all, mark it **NOT FOUND** — do not "fix" it by guessing a nearby citation.
3. **Quotation check.** Pull the opinion text (CourtListener `read_document` / `search_document`; Descrybe `verify_quote` or `get_case_passages`). For each quotation confirm:
   - The words match exactly, including punctuation and emphasis.
   - Omissions are marked with ellipses and alterations with brackets.
   - The quote is from the majority opinion, not a dissent, concurrence, headnote, or syllabus — or is labeled accordingly.
   - The quoted language is not stripped of a qualifier that changes its meaning.
4. **Pin cite check.** Confirm the quoted or paraphrased material appears on the cited page in the cited reporter.
5. **Characterization check.** For each "the court held" or parenthetical, confirm it is the holding (not dicta, not a statement of a party's argument, not a rule the court rejected). Confirm the procedural posture matches how the draft uses it.
6. **Statutes and rules.** Compare every quoted statute or rule word for word with the text from `statute-lookup`, for the correct version date. Check subsection numbers.
7. **Record cites.** Confirm each factual statement's record cite (exhibit, transcript page, legal-file page) actually supports it.
8. **Classify each item:** Verified / Corrected (minor error fixed from source) / Mischaracterized (rewrite needed) / Not found (remove).
9. **Fix by removal, not invention.** If a proposition has no verified support, remove the citation and either find real authority through research or rewrite the sentence as argument.

## Output
| # | Location in draft | Citation / quote | Exists? | Quote exact? | Pin correct? | Holding accurate? | Status | Fix |
|---|---|---|---|---|---|---|---|---|

Then a summary: count by status, every NOT FOUND item listed first, and a corrected passage for each Corrected or Mischaracterized item.

## Pitfalls
- Trusting a citation because it looks properly formatted; fabricated citations often look perfect.
- Verifying that a case exists but not that it says what the draft claims.
- Quoting a headnote or syllabus as the court's words.
- Repairing a bad citation with a guessed volume or page number.
- Signing a filing with unverified citations: Missouri Rule 55.03 and Federal Rule of Civil Procedure 11 make the signer certify that legal contentions are warranted by existing law, and courts have sanctioned self-represented litigants and lawyers for nonexistent AI-generated citations.
- Skipping the check on "obvious" or famous cases; pin cites and quotations are where errors hide.

## Verify before relying
- Pull verbatim text of every statute/rule cited via `statute-lookup` (or Descrybe `search_laws_and_rules`); check case law is still good law (CourtListener / Descrybe treatment) before citing.
- When a source cannot be accessed, mark the item unverified; never report it as verified.
- Legal information, not legal advice; recommend counsel/legal aid for high-stakes decisions.

## Related skills
- `good-law-checker` — validity check for each verified authority.
- `legal-citation-formatter` — format the verified citations.
- `statute-lookup` — verbatim statute and rule text.
- `lawmind-legal-research` — find real authority to replace anything removed.
- `filing-followup` — after the user files the verified document.
