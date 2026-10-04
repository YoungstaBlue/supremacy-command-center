---
name: appellate-brief-writer
description: Drafts Missouri (Rule 84.04/84.06) and Eighth Circuit (FRAP 28/32) appellate briefs - jurisdictional statement, facts, points relied on, standard of review and preservation per point, argument, reply. Use for "write my appellate brief", "points relied on", "appellant's brief", or "reply brief".
---

# Appellate Brief Writer

Turns preserved trial-court errors into a rule-compliant appellate brief, point by point, with the correct standard of review and preservation statement for each, so the court reaches the merits instead of dismissing for briefing defects.

## When to use
- Drafting an appellant's, respondent's, or reply brief in the Missouri Court of Appeals or Supreme Court
- Drafting an opening or reply brief in the Eighth Circuit
- Fixing a brief the court or opponent says violates Rule 84.04
- Not for: deadlines, notice of appeal, or the record (use `mo-appeals-procedure` / `federal-appeals-8th-circuit`); trial-level motions (use `legal-memo-writer` or the motion skills)

## Gather first
- The record on appeal (legal file and transcript) with page numbers — every fact needs a record cite
- The judgment appealed and the list of rulings the user believes were wrong
- How each error was preserved (objection, offer of proof, motion, motion for new trial) with record cites

## Workflow
1. **Issue triage.** For each candidate error, record: ruling, record cite, preservation, standard of review, prejudice. Keep the strongest 2-5 points; weak points dilute strong ones. Unpreserved points survive only under plain error (civil Rule 84.13(c); criminal Rule 30.20), which requires manifest injustice or miscarriage of justice.
2. **Standard of review per point.**
   - Court-tried case (Missouri): affirm unless no substantial evidence supports the judgment, it is against the weight of the evidence, or it erroneously declares or applies the law (Murphy v. Carron, 536 S.W.2d 30 (Mo. banc 1976)).
   - Questions of law, statutory interpretation, summary judgment: de novo.
   - Admission/exclusion of evidence, most trial management: abuse of discretion plus prejudice.
   - Jury instruction error: reviewed de novo whether the instruction was proper; reversal requires prejudice.
   - Criminal sufficiency: whether a reasonable juror could find each element beyond a reasonable doubt, viewing evidence favorably to the verdict.
   - Use `standard-of-review-finder` to confirm per issue.
3. **Missouri brief structure (Rule 84.04(a) — verify order):** table of contents and table of authorities; jurisdictional statement (84.04(b)); statement of facts (84.04(c)); points relied on (84.04(d)); argument (84.04(e)); conclusion stating the precise relief; certificate of compliance (84.06(c)); certificate of service; appendix (84.04(h): judgment, rulings at issue, and the text of statutes/rules relied on).
4. **Statement of facts.** Fair and concise, facts relevant to the questions presented, no argument, every sentence cited to the record (e.g., "(L.F. 12)", "(Tr. 45)" — follow the court's citation format). Include facts unfavorable to the user; omitting them costs credibility and can violate 84.04(c).
5. **Points relied on (84.04(d)(1)).** Template:
   "The trial court erred in [identify the ruling or action challenged], because [state concisely the legal reasons for the claim of reversible error], in that [explain why, in the context of the case, those legal reasons support the claim of reversible error]."
   - One ruling per point; multifarious points (several rulings in one point) may be reviewed only in part or not at all.
   - After each point list up to four principal authorities (84.04(d)(5) — verify).
6. **Argument (84.04(e)).** Each argument section restates its point, then gives (a) the standard of review and (b) a statement of whether and how the error was preserved, with record cites (verify current wording of 84.04(e)), then the analysis: rule from authority, application to record facts, prejudice. Argue only what the point raises.
7. **Eighth Circuit differences.** FRAP 28(a) sections: corporate disclosure (if applicable), tables, jurisdictional statement, statement of issues (with most apposite cases — check 8th Cir. R. 28A), statement of the case, summary of argument, argument with standard of review for each issue, conclusion, certificates. Word limit for a principal brief 13,000 words, reply 6,500 (FRAP 32(a)(7)(B)); 14-point proportional font (FRAP 32(a)(5)). Addendum requirements are in 8th Cir. R. 28A — pull current text.
8. **Respondent/appellee.** Restate points favorably, defend on any ground supported by the record (judgment may be affirmed on any basis), attack preservation and prejudice.
9. **Reply.** Answer only new matters raised by the respondent; no new points.
10. **Final checks.** Word count and font per Rule 84.06 / FRAP 32; every quote and pin cite verified; every case still good law; record cites spot-checked.

## Output
- Issue triage table: | # | Ruling | Record | Preserved how | Standard | Prejudice | Keep? |
- Full brief draft in required section order, with each point in the 84.04(d) template
- Certificate of compliance and service blocks (see `court-document-formatting`)

## Pitfalls
- Points relied on lacking the ruling / because / in-that structure — dismissal or plain-error-only review
- Facts without record cites, or argumentative facts
- Raising issues not preserved below, or switching theories on appeal
- Ignoring the standard of review (e.g., rearguing credibility in a court-tried case)
- Exceeding word limits or omitting required appendix materials
- Failing to show prejudice from the error

## Verify before relying
- Pull current Rules 84.04, 84.06, 84.13, 30.20 and FRAP 28, 32 plus 8th Cir. local rules via `statute-lookup` (or Descrybe `search_laws_and_rules`); check the specific district's special rules.
- Run every case through `good-law-checker` and every quote through `quote-and-cite-verifier`.
- Legal information, not legal advice; consider appellate counsel or a law school appellate clinic.

## Related skills
- `mo-appeals-procedure` — deadlines, record, and post-opinion steps
- `standard-of-review-finder` — standard per issue
- `legal-citation-formatter` — Missouri and Bluebook citation form
- `quote-and-cite-verifier` — check every quotation and pin cite
- `federal-appeals-8th-circuit` — federal procedure
