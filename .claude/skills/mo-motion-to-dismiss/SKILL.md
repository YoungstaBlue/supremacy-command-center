---
name: mo-motion-to-dismiss
description: Drafts and opposes Missouri Rule 55.27 motions to dismiss - failure to state a claim under fact pleading (Nazeri), jurisdiction, venue, process, service - plus waiver and leave to amend. Use for "motion to dismiss", "55.27", "failure to state a claim", "respond to motion to dismiss".
---

# Missouri Motion to Dismiss

Builds or answers a Rule 55.27 motion by testing the petition's ultimate facts against each element, identifying waivable defenses, and planning amendment if the motion is granted.

## When to use
- Defendant evaluating whether a Missouri petition can be dismissed before answering
- Plaintiff responding to a motion to dismiss, or deciding to amend instead
- Judgment on the pleadings, motion to strike, or motion for more definite statement questions
- Not for: federal Rule 12 motions (use `federal-rule-12-motions`); motions relying on evidence outside the petition (that becomes `mo-summary-judgment`)

## Gather first
- The petition (and exhibits attached to it) exactly as filed
- Date of service and whether any answer or other motion has already been filed
- For each count, the claim type, so elements can be listed

## Workflow
1. **Timing.** File before or with the answer, within the 30-day answer period (Rule 55.25 - verify). Filing a Rule 55.27 motion generally suspends the answer deadline until the ruling (verify the post-ruling period).
2. **Choose grounds (Rule 55.27(a) - verify numbering).** Lack of subject-matter jurisdiction; lack of personal jurisdiction; improper venue (note Rule 51.045 transfer procedure - verify); insufficiency of process; insufficiency of service of process; failure to state a claim upon which relief can be granted (Rule 55.27(a)(6)); failure to join a necessary party; lack of capacity; another action pending for the same cause; and the other grounds listed in the current rule.
3. **Apply the waiver rule.** Personal jurisdiction, venue, process, and service objections are waived if omitted from the first Rule 55.27 motion or not pleaded in the answer (verify Rule 55.27(g)). Failure to state a claim can be raised later (judgment on the pleadings, at trial). Subject-matter jurisdiction is never waived, but under J.C.W. ex rel. Webb v. Wyciskalla, 275 S.W.3d 249 (Mo. banc 2009), Missouri circuit courts' subject-matter jurisdiction is constitutional and broad - most "jurisdiction" arguments are really about statutory authority or other defenses. Do not mislabel them.
4. **Standard for failure to state a claim.** The motion "is solely a test of the adequacy of the plaintiff's petition"; the court assumes all averments true, gives the plaintiff all reasonable inferences, does not weigh credibility, and asks whether the facts alleged meet the elements of a recognized cause of action. Nazeri v. Missouri Valley College, 860 S.W.2d 303, 306 (Mo. banc 1993) (verify pin cite). Conclusions unsupported by facts are disregarded because Missouri is a fact-pleading state; Twombly/Iqbal plausibility is not the Missouri test.
5. **Element-by-element test.** List the elements of each count (`elements-checklist-builder`). For each element, find the petition paragraph pleading an ultimate fact. Any element with only a conclusion or nothing is a dismissal ground for that count.
6. **Affirmative defenses on the face.** Limitations, immunity, or res judicata support dismissal only if established on the face of the petition; otherwise plead them in the answer.
7. **No outside evidence.** If matters outside the pleadings are presented and not excluded, the motion is treated as one for summary judgment under Rule 74.04 and parties must get the chance to present summary-judgment material (Rule 55.27(a) - verify). Keep the motion confined to the petition and its exhibits.
8. **Drafting the motion.** Caption, motion (numbered grounds), and separate suggestions in support (Missouri term for supporting brief) with: introduction, the petition's allegations, legal standard, argument count by count, conclusion stating relief (dismissal of named counts).
9. **Opposing.** Show each element is pleaded with facts, cite paragraph numbers, argue liberal inferences, and request leave to amend in the alternative. Courts are to freely grant leave to amend on sustaining a motion to dismiss and set a time for it (Rule 67.06 - verify).
10. **Effect of dismissal.** Involuntary dismissal is without prejudice unless the court specifies otherwise (Rule 67.03 - verify). A dismissal without prejudice is generally not appealable unless it effectively ends the action; if you choose to stand on the petition, ask for a dismissal with prejudice or a final judgment so you can appeal (see `mo-appeals-procedure`).

## Output
- Motion plus suggestions in support (or suggestions in opposition), using the headings above
- Element test table: | Count | Element | Petition para. | Ultimate fact or conclusion? | Pass/Fail |
- Waiver checklist and a recommendation: move, answer, or amend

## Pitfalls
- Arguing the facts are untrue - the court must accept them at this stage.
- Attaching affidavits or evidence and accidentally converting the motion.
- Omitting service or venue objections from the first motion and waiving them.
- Plaintiff failing to request leave to amend, or failing to amend within the time given.
- Appealing a without-prejudice dismissal that is not final.
- Using federal plausibility case law as the Missouri standard.
- Filing a speaking motion on limitations when the accrual date is not apparent from the petition.
- Ignoring a motion to dismiss as plaintiff; the court may rule without a hearing once the response time passes - check local motion practice.
- Treating the ruling as the end: calendar the answer deadline that runs after denial.

## Verify before relying
- Pull verbatim Rules 55.25, 55.27, 51.045, 67.03, 67.06, 74.04 via `statute-lookup` (or Descrybe `search_laws_and_rules`).
- Confirm Nazeri and J.C.W. remain good law and check pin cites (CourtListener / Descrybe treatment).
- Recompute deadlines from the actual service and ruling dates.
- Legal information, not legal advice; recommend counsel or legal aid for high-stakes decisions.

## Related skills
- `mo-petition-drafting` - curing deficiencies by amendment
- `mo-answer-affirmative-defenses` - what to file if the motion fails
- `mo-summary-judgment` - when facts outside the petition matter
- `jurisdiction-and-venue-analyzer` - personal jurisdiction and venue analysis
- `standard-of-review-finder` - de novo review of dismissals on appeal
