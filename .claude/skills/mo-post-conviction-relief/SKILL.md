---
name: mo-post-conviction-relief
description: Plans Missouri post-conviction relief under Rule 24.035 (guilty plea) and Rule 29.15 (trial) - Form 40 deadlines, all-claims rule, amended motions, and ineffective assistance under Strickland and Hill v. Lockhart. Use for "Rule 29.15", "Rule 24.035", "Form 40", "PCR motion", or "my lawyer was ineffective".
---

# Missouri Post-Conviction Relief (Rules 24.035 and 29.15)

Gets a timely, complete Form 40 motion on file and frames each claim - especially ineffective assistance of counsel - so it survives the no-hearing and clearly-erroneous standards.

## When to use
- A felony conviction by guilty plea (Rule 24.035) or after trial (Rule 29.15), and the sentence has been entered
- "Form 40", "PCR", "post-conviction", "ineffective assistance", "my lawyer never told me", "illegal sentence"
- Calculating whether a PCR motion is still timely
- Not for: direct appeal (use `mo-appeals-procedure`); federal habeas after state remedies (use `federal-habeas-2254`); misdemeanor convictions, which these rules do not cover (Rules 24.035(a), 29.15(a) are limited to felonies)

## Gather first
- Date sentence was entered; whether a direct appeal was taken; date the appellate mandate issued
- Plea or trial transcript, sentencing transcript, plea agreement, and the judgment
- Every complaint about counsel, the court, or the sentence, with what evidence would prove it

## Workflow
1. **Pick the rule.** Guilty plea: Rule 24.035. Conviction after trial: Rule 29.15. Each is the "exclusive procedure" in the sentencing court for constitutional claims, ineffective assistance of trial and appellate counsel, lack of jurisdiction, and sentences exceeding the maximum.
2. **Compute the deadline (both rules, subdivision (b)):** no appeal - within 180 days of the date sentence is entered; appeal affirmed - within 90 days after the appellate mandate issues; remand - 180 days from the new judgment if not appealed, or 90 days after the mandate if appealed. A motion mailed first-class, correctly addressed with postage, on or before the last day is timely; a legible USPS postmark is prima facie evidence of the date. Untimely filing is a "complete waiver" of the right and every claim. Verify which rule version applies: subdivision (m) ties the version to the sentencing date for sentences on or after January 1, 2018.
3. **File substantially in the form of Criminal Procedure Form No. 40**, with two copies, no cost deposit (subdivisions (b)-(c)). Plead facts showing timeliness on the face of the motion.
4. **Include every known claim** and the required declaration that all known claims are listed and unlisted known claims are waived (subdivision (d)). Successive motions are not entertained (subdivision (l)).
5. **Counsel and amended motion.** For an indigent movant, counsel is appointed within 30 days (subdivision (e)). The amended motion or statement in lieu is due within 120 days of the later of transcript filing or mandate together with appointment/entry of appearance, and the court cannot extend it (subdivision (g)). The amended motion may not incorporate the pro se motion by reference. If counsel misses it, the court must inquire into abandonment. The movant may reply within 10 days to a statement in lieu.
6. **Ineffective assistance.** Strickland v. Washington, 466 U.S. 668 (1984): (a) counsel's performance fell below an objective standard of reasonableness, overcoming the presumption of reasonable strategy; and (b) prejudice - a reasonable probability of a different result. For pleas, prejudice means a reasonable probability the movant would have rejected the plea and insisted on trial (Hill v. Lockhart, 474 U.S. 52 (1985)). Lost-plea-offer claims: Missouri v. Frye, 566 U.S. 134 (2012). Plead each claim as: specific act or omission; what reasonable counsel would have done; what evidence or witness would have shown (name the witness, that they were available, would have testified, and what they would have said); how it changed the outcome.
7. **Hearing standards.** No hearing if the files and records conclusively show no entitlement to relief (subdivision (h)) - so plead facts, not conclusions, that the record does not refute. At a hearing the movant bears the burden by a preponderance (subdivision (i)); the hearing is confined to claims in the last timely motion.
8. **Findings and appeal.** The court must issue findings on all issues, including timeliness and abandonment (subdivision (j)); Rule 78.07(c) applies - move to amend if findings are missing. Appellate review is for clear error (subdivision (k)).
9. **Federal habeas clock.** A properly filed state PCR motion tolls the one-year federal limitation (28 U.S.C. 2244(d)(2)), but time before filing counts. Track both clocks.

## Output
- **Deadline computation:** trigger event, date, rule subdivision, due date, mailing plan
- **Claims inventory:** | Claim | Type (IAC trial / IAC appellate / plea involuntary / jurisdiction / illegal sentence) | Facts | Proof | Record refutes? |
- Form 40 claim paragraphs drafted in fact-pleading style
- List of transcripts and records to request

## Pitfalls
- Missing the 180/90-day deadline - waiver is complete and courts do not extend it.
- Leaving a known claim out; there is no second motion.
- Conclusory claims ("counsel was ineffective") that are denied without a hearing.
- Claims contradicted by the movant's own sworn answers at the plea colloquy.
- Raising trial errors that should have been raised on direct appeal; PCR is not a substitute for appeal.

- Mailing on the last day without proof of mailing; keep a postmarked receipt.
- Waiting for appointed counsel to add claims the movant already knows; the pro se motion must list them.
- Missing that claims about a plea are judged by the colloquy record and must explain any contradiction.
- Filing in the wrong court; the motion goes to the sentencing court.
- Assuming the federal habeas clock pauses before the Form 40 is filed; it does not.

## Verify before relying
- Pull the version of Rule 24.035 or 29.15 in effect on the sentencing date via `statute-lookup` or Descrybe `search_laws_and_rules` (amended 2018, 2021, 2023).
- Check Strickland-line Missouri decisions for current treatment (CourtListener / Descrybe) before citing.
- Recompute every deadline from the actual sentence-entry or mandate date.
- Legal information, not legal advice; request appointed counsel and keep copies of everything mailed.

## Related skills
- `federal-habeas-2254` - next step and AEDPA timing
- `mo-plea-and-sentencing` - what the plea record shows
- `mo-appeals-procedure` - direct appeal versus PCR
- `sixth-amendment-counsel-confrontation` - right-to-counsel issues
- `quote-and-cite-verifier` - check transcript quotes before filing
