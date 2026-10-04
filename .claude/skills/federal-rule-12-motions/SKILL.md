---
name: federal-rule-12-motions
description: Drafts, opposes, and times federal Rule 12 motions - 12(b)(1)-(7), 12(c), 12(e), 12(f) - and the Rule 15 amendment response, including waiver under 12(g)-(h). Use for "motion to dismiss" in federal court, "failure to state a claim", "12(b)(6)", "respond to motion to dismiss", or "amend my complaint".
---

# Federal Rule 12 Motions

Handles pre-answer motions in federal court from either side, and the most common winning response for plaintiffs: a timely amended complaint.

## When to use
- Defendant filed a federal motion to dismiss, for judgment on the pleadings, more definite statement, or to strike
- Deciding which Rule 12 defenses to raise (and which are waived if omitted)
- Deciding whether to amend as of right or seek leave under Rule 15
- Not for: Missouri state-court motions to dismiss under Rule 55.27 — use `mo-motion-to-dismiss`

## Gather first
- Date of service of the complaint or the motion (and how served)
- The complaint and every exhibit attached to it, and the motion and supporting memorandum
- Whether any amendment has already been made, and whether an answer has been filed

## Workflow
1. **Timing (verify current text of Rule 12(a)).**
   - Answer or Rule 12 motion: 21 days after service of summons and complaint; 60 days after the request was sent if service was waived under Rule 4(d); United States, its agencies, officers: 60 days.
   - After the court denies or postpones a Rule 12 motion: responsive pleading due 14 days after notice of the court's action, unless the court sets another time.
   - Response and reply deadlines to motions come from the district's local rules (E.D. Mo. / W.D. Mo.) and any court order — check them; they are short.
2. **Grounds.** 12(b)(1) lack of subject-matter jurisdiction; (2) personal jurisdiction; (3) improper venue; (4) insufficient process; (5) insufficient service of process; (6) failure to state a claim; (7) failure to join a Rule 19 party. Also 12(c) judgment on the pleadings (after pleadings close), 12(e) more definite statement (pleading too vague to respond to), 12(f) strike redundant, immaterial, impertinent, or scandalous matter.
3. **Waiver map (Rule 12(g)-(h)).**
   - 12(b)(2)-(5) are waived if omitted from a first Rule 12 motion or, absent a motion, from the answer.
   - 12(b)(6), failure to join, and failure to state a legal defense survive to the pleadings, 12(c), or trial.
   - Lack of subject-matter jurisdiction can be raised at any time; the court must dismiss whenever it finds it lacking.
   - Generally only one pre-answer Rule 12 motion; consolidate defenses.
4. **Standards.**
   - 12(b)(6)/12(c): accept well-pleaded facts as true, draw reasonable inferences for the plaintiff, disregard conclusions; ask whether the claim is plausible. Bell Atlantic Corp. v. Twombly, 550 U.S. 544 (2007); Ashcroft v. Iqbal, 556 U.S. 662 (2009). Pro se complaints construed liberally. Erickson v. Pardus, 551 U.S. 89 (2007).
   - 12(b)(1): facial attack (pleadings taken as true) vs factual attack (court may weigh evidence outside the pleadings); plaintiff bears the burden of establishing jurisdiction.
   - 12(b)(2): plaintiff must make a prima facie showing of jurisdiction; affidavits are permitted.
5. **Outside matters (Rule 12(d)).** If matters outside the pleadings are presented and not excluded on a 12(b)(6)/12(c) motion, the motion becomes one for summary judgment and all parties get a reasonable opportunity to present material. Documents attached to or necessarily embraced by the complaint and public records generally do not trigger conversion.
6. **Opposing a 12(b)(6) motion.** For each argued deficiency: (a) quote the complaint paragraphs that supply the element; (b) show the inference is reasonable; (c) distinguish defendant's cases on posture/facts; (d) in the alternative, request leave to amend and describe the additional facts.
7. **Amendment (Rule 15).**
   - As a matter of course, once: within 21 days after serving the pleading, or, if a responsive pleading is required, 21 days after service of the responsive pleading or a 12(b), (e), or (f) motion, whichever is earlier.
   - Otherwise: written consent of the opposing party or leave of court, freely given when justice so requires; denial requires a reason such as undue delay, bad faith, repeated failure to cure, undue prejudice, or futility. Foman v. Davis, 371 U.S. 178 (1962).
   - Attach the complete proposed amended complaint to any motion for leave; an amended complaint supersedes the original, so restate everything.
   - An amendment often moots the pending motion to dismiss.
   - Relation back for limitations purposes: Rule 15(c).
8. **Dismissal with vs without prejudice.** Ask the court, in the alternative, for dismissal without prejudice and leave to amend; with-prejudice dismissal ends the claim and is appealable after final judgment.

## Output
- Deadline line: served date, response due date, amendment-as-of-right window end date
- Opposition outline: Introduction; Standard of Review; Argument (one heading per challenged count, element-by-element with paragraph cites); Alternative Request for Leave to Amend; Conclusion
- Or, for defense: motion listing every Rule 12(b) ground being preserved, with a memorandum per local rules

## Pitfalls
- Letting the 21-day amend-as-of-right window lapse while drafting an opposition
- Arguing new facts in the opposition brief instead of amending — courts look only at the complaint
- An amended complaint that refers back to the original ("as stated before") instead of standing alone
- Defendants: omitting service or personal-jurisdiction defenses from the first motion (waived)
- Ignoring local-rule page limits, memorandum requirements, and response deadlines
- Treating a 12(b)(1) factual attack as if allegations must be accepted as true

## Verify before relying
- Pull current FRCP 12, 15, 4(d) and the district local rules verbatim via `statute-lookup` or Descrybe `search_laws_and_rules`.
- Check that any Eighth Circuit authority cited is still good law (CourtListener / Descrybe).
- Recompute every deadline from the actual service date; account for Rule 6 computation and Rule 6(d) only where service was by mail.
- Legal information, not legal advice.

## Related skills
- `federal-complaint-pleading` — fixing the complaint in an amendment
- `federal-subject-matter-jurisdiction` — 12(b)(1) attacks
- `qualified-immunity-analyzer` — QI raised in a 12(b)(6) motion
- `federal-summary-judgment` — when 12(d) conversion occurs
- `mo-motion-to-dismiss` — state-court counterpart
