---
name: mo-post-trial-motions
description: Drafts and times Missouri post-trial motions - motion for new trial, motion to amend the judgment, JNOV - under Rules 72.01, 73.01, 75.01, 78.04, 78.07 and 81.05. Use for "motion for new trial", "amend the judgment", "30-day window", "preserve error for appeal", or a judgment just entered.
---

# Missouri Post-Trial Motions

Identify, time, and draft the after-trial motions that keep a Missouri judgment open, preserve error for appeal, and control when the appeal clock starts.

## When to use
- A judgment was just entered (or is about to be) in a Missouri circuit or associate circuit case.
- The user asks about a motion for new trial, motion to amend/modify the judgment, JNOV, or the court's 30-day control period.
- The user needs to know when the judgment becomes final and when the notice of appeal is due.
- Not for: drafting the appeal itself - use `mo-appeals-procedure`; setting aside a default judgment - use `mo-default-judgment-set-aside`.

## Gather first
- The exact date the judgment was entered (file stamp / docket entry), and whether the document is denominated "judgment" and signed.
- Jury trial, bench trial, or advisory jury; whether a motion for directed verdict was made at the close of all evidence.
- The specific errors (rulings on evidence, instructions, findings, form of judgment, weight/sufficiency of evidence).

## Workflow
1. Confirm there is a final, appealable judgment: denominated "judgment" or "decree" and signed (Rule 74.01(a)); if fewer than all claims/parties are resolved, check for an express "no just reason for delay" finding (Rule 74.01(b)). If not final, post-trial motions may be premature - flag it.
2. Calendar the 30-day deadline from entry of judgment. A motion for new trial and a motion to amend the judgment are due within 30 days after entry (Rule 78.04). A JNOV motion is due within 30 days after entry and requires a prior directed-verdict motion at the close of all evidence (Rule 72.01). The court cannot extend these deadlines (Rule 44.01(b)).
3. Choose the right motion(s):
   - Jury case: errors you want reviewed on appeal generally must be listed in a motion for new trial (Rule 78.07(a)). Sufficiency-of-evidence challenges ride on the directed-verdict/JNOV route.
   - Bench case: a new-trial or amend motion is generally not needed to preserve error (Rule 78.07(b)), EXCEPT errors in the form or language of the judgment, including missing statutorily required findings, which must be raised in a motion to amend in every case (Rule 78.07(c)).
   - Court-tried findings: if specific findings were wanted, they must have been requested under Rule 73.01 before evidence was introduced; a post-trial motion cannot cure a missing request.
4. Draft each allegation of error with particularity: what ruling, where in the record, why it was wrong, and the prejudice. Vague "the verdict is against the law and evidence" grounds preserve little.
5. Attach supporting affidavits (e.g., juror misconduct, newly discovered evidence) with the motion; newly discovered evidence must show it was not discoverable with diligence, is material, not cumulative, and would likely change the result.
6. Track the court's ruling window. If the court does not rule within 90 days after the motion is filed, it is deemed overruled (Rule 78.06). Note the court's own 30-day control period over the judgment (Rule 75.01) and that a timely authorized motion extends its jurisdiction until ruling or deemed denial.
7. Compute finality (Rule 81.05(a)): no timely authorized motion = final 30 days after entry; timely motion = finality is tied to the ruling on the last motion or the 90-day deemed-denial date, whichever comes first. Read the verbatim text of Rule 81.05(a)(2) before computing - the exact trigger depends on how and when the court disposes of each motion. Notice of appeal is due within 10 days after the judgment becomes final (Rule 81.04(a)).
8. If the court amends the judgment, treat it as a new judgment and recompute all deadlines.

## Output
- Deadline table: Entry date | Motion due (30 days) | Deemed-denied date (90 days after filing) | Finality date | Notice of appeal due (10 days after finality).
- Draft motion with headings: Caption; Introduction; Procedural History; Grounds (numbered, one error per point, with record cites); Supporting Affidavits; Relief Requested; Signature; Certificate of Service.
- A preservation checklist: each error -> where objected at trial -> listed in motion (Y/N).

## Pitfalls
- Filing on day 31: the court has no power to extend; the error may be unpreserved and the appeal timeline shifts.
- Filing a post-trial motion against a non-final "order" not denominated a judgment - it may be a nullity.
- Omitting form-of-judgment complaints from a motion to amend in a bench case (waived under Rule 78.07(c)).
- Raising a new objection in the motion that was never made at trial - a post-trial motion does not cure failure to object.
- Assuming the 10-day appeal clock runs from the judgment date when a timely motion was filed.
- Calling a motion by the wrong name; courts look at substance, but an unauthorized motion (e.g., "motion to reconsider") may not extend finality.
- Serving the motion on the other side late or not at all - include a certificate of service and serve the same day it is filed.
- Forgetting that a party who wants findings or a new trial in a court-tried case must still meet any rule-based request deadline; check the judge's order.
- Treating the deemed-overruled date as optional - the appeal clock starts whether or not the court issues a written ruling.

## Verify before relying
- Pull verbatim text of Rules 72.01, 73.01, 74.01, 75.01, 78.04, 78.06, 78.07, 81.04, and 81.05 via `statute-lookup` before quoting.
- Check any case cited for the standard (e.g., newly discovered evidence test) on CourtListener for subsequent treatment.
- Recompute every deadline from the actual file-stamped entry date, using `mo-deadline-calculator`.
- Legal information, not legal advice; consult counsel or legal aid before an appeal decision.

## Related skills
- `mo-deadline-calculator` - computes the 30/90/10-day chain.
- `mo-appeals-procedure` - notice of appeal and record after finality.
- `standard-of-review-finder` - frames each error the way the appellate court will review it.
- `lawmind-god-drafter` - assembles the motion with companion documents.
- `filing-followup` - tracks whether the motion was actually filed.
