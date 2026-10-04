---
name: mo-default-judgment-set-aside
description: Handles Missouri default judgments - Rule 74.05 interlocutory default, Rule 74.05(d) set-aside (good cause plus meritorious defense, within one year), and Rule 74.06 relief for void or fraud-tainted judgments. Use for "default judgment", "set aside default", "I never got served".
---

# Missouri Default Judgment and Set-Aside

Identifies the correct vehicle and deadline to undo a default (or to obtain one properly), and builds the sworn factual showing Missouri courts require.

## When to use
- A default judgment or interlocutory order of default was entered against you
- You missed the answer date and no judgment has been entered yet
- You claim you were never properly served, or the judgment was obtained by fraud
- You are the plaintiff seeking a default judgment against a non-responding defendant
- Not for: post-trial motions after a contested trial (use `mo-post-trial-motions`); appeals (use `mo-appeals-procedure`)

## Gather first
- Exact date the default judgment (or interlocutory default) was entered, and whether it is final
- The return of service and the facts of how, or whether, you received the summons and petition
- Your defense to the claim on the merits, with supporting documents

## Workflow
1. **Identify the stage and the clock.**
   - No answer, no default yet: file the answer immediately with a motion for leave to file out of time.
   - Interlocutory order of default, no judgment: move to set it aside for good cause before judgment (verify Rule 74.05(c)).
   - Default judgment entered within the last 30 days: the trial court still controls its judgment (Rule 75.01 - verify); file the Rule 74.05(d) motion now, and consider whether a motion under the post-trial rules is also appropriate.
   - Default judgment up to one year old: Rule 74.05(d) motion, filed within a reasonable time not exceeding one year after entry (verify wording).
   - Judgment void (no valid service, no personal jurisdiction): Rule 74.06(b)(3) motion within a reasonable time; the one-year cap in Rule 74.06(c) applies to mistake and fraud grounds, not voidness (verify).
2. **Rule 74.05(d) elements.** Show (a) facts constituting a meritorious defense and (b) good cause. Good cause includes a mistake or conduct that is not intentionally or recklessly designed to impede the judicial process (verify current text). Courts generally construe good cause liberally in favor of trial on the merits, but negligence alone can fail if it is reckless.
3. **Meritorious defense.** State specific facts that, if believed, would defeat all or part of the claim (including damages amount). Conclusions are not enough. Attach the proposed answer.
4. **Make it sworn.** The motion does not prove itself; verify it or attach affidavits (and documents) establishing good cause and the defense facts, and be prepared to testify at the hearing.
5. **Rule 74.06(b) grounds (verify).** (1) mistake, inadvertence, surprise, or excusable neglect; (2) fraud, misrepresentation, or other misconduct of an adverse party; (3) the judgment is void; (4) satisfied, released, or discharged, or no longer equitable; plus the other grounds stated in the rule. Plead every ground that fits as alternatives.
6. **Attacking service.** Compare the return to Rule 54.13 requirements (see `mo-service-of-process`). A sheriff's return is given strong weight; rebutting it typically requires clear and convincing evidence - gather affidavits, residence proof, and work records.
7. **Damages-only challenge.** Even if liability default stands, unliquidated damages require evidence; contest an unsupported damages award.
8. **Plaintiff side.** Confirm valid service and the answer deadline passed, then request an interlocutory order of default and present evidence of damages at a hearing; a default judgment on bad service is vulnerable indefinitely.
9. **Appeal path.** A ruling on a Rule 74.05(d) or 74.06 motion is generally treated as appealable; calendar the notice-of-appeal deadline from the ruling (see `mo-appeals-procedure`, verify).
10. **Stop collection.** If garnishment or execution is underway, ask the court to stay enforcement pending the motion (see `mo-garnishment-and-execution`).

## Output
- Verified motion to set aside: Caption / Procedural history with dates / Good cause facts / Meritorious defense facts / Legal standard / Alternative Rule 74.06 grounds / Relief / Verification or affidavit / Certificate of service
- Attached proposed answer
- Deadline table: | Event | Date | Rule | Last day to act |

## Pitfalls
- Unverified motion with no affidavit - courts deny for lack of evidence.
- Waiting: "reasonable time" can be less than one year if you sat on known facts.
- Conclusory defenses ("I don't owe this") without specific facts.
- Assuming notice of the lawsuit is irrelevant - actual knowledge plus inaction undermines good cause.
- Filing a new lawsuit instead of a motion in the original case.
- Missing the appeal deadline after the motion is denied.

## Verify before relying
- Pull verbatim Rules 74.05, 74.06, 75.01, and 54.13 via `statute-lookup` (or Descrybe `search_laws_and_rules`); confirm subdivisions.
- Find current Missouri appellate authority on good cause and meritorious defense and confirm it is good law (CourtListener / Descrybe treatment) before citing any case.
- Recompute every deadline from the actual entry date of the judgment.
- Legal information, not legal advice; recommend counsel or legal aid for high-stakes decisions.

## Related skills
- `mo-service-of-process` - testing the validity of service
- `mo-answer-affirmative-defenses` - the proposed answer to attach
- `mo-post-trial-motions` - the 30-day control window
- `mo-appeals-procedure` - appealing the ruling
- `mo-deadline-calculator` - computing reasonable-time and one-year limits
