---
name: wrongful-death-and-survival-mo
description: Analyzes Missouri wrongful death claims (RSMo 537.080-537.095) - who may sue by class, the single-action rule, 3-year limit, recoverable damages, aggravating circumstances, court-approved settlements - plus survival of claims and 1983 death cases. Use for "wrongful death", "my family member died", or "survival action".
---

# Wrongful Death and Survival (Missouri)

Determines who can bring a Missouri wrongful death claim, what must be proven, what damages are recoverable, and the deadlines, and separates it from survival claims and federal civil-rights death cases.

## When to use
- A person died from someone's wrongful act, negligence, or a constitutional violation.
- Deciding which relative can sue, or whether a relative was left out.
- Settling a death claim (court approval required).
- Not for: injury claims where the person survived - use `negligence-claim-builder` or `intentional-torts`.

## Gather first
- Date and cause of death; date of the underlying injury; who caused it.
- Family tree: spouse, children (including adopted), descendants of deceased children, parents, siblings.
- Whether the decedent could have sued had they lived (the claim depends on that).

## Workflow
1. **Underlying wrong.** Wrongful death exists when the death was caused by an act or failure that would have let the decedent sue had death not occurred (RSMo 537.080). Prove the underlying tort's elements first.
2. **Who may sue, by class (RSMo 537.080).**
   - Class 1: spouse, children (including adopted), surviving descendants of deceased children, or parents.
   - Class 2: if no Class 1 member, siblings or their descendants.
   - Class 3: if neither, a plaintiff ad litem appointed by the court.
   A member of a higher class excludes lower classes.
3. **Single-action rule.** Only one wrongful death action is allowed per death. Any class member may bring it but must give notice to other class members and join or account for them. Check whether someone else has already filed.
4. **Deadline.** Generally 3 years from death (RSMo 537.100), with limited tolling. Medical negligence deaths have their own rules (RSMo ch. 538) - verify.
5. **Damages (RSMo 537.090).** Pecuniary losses; funeral expenses; reasonable value of services, consortium, companionship, comfort, instruction, guidance, counsel, training, and support lost; and the decedent's pain and suffering and medical expenses between injury and death (RSMo 537.085). The jury may consider aggravating circumstances. Medical-negligence caps on non-economic damages may apply (RSMo 538.210) - verify current text.
6. **Defenses carry over.** Defenses good against the decedent (comparative fault, immunity, release) generally apply (RSMo 537.085).
7. **Settlement requires court approval.** A court must approve the settlement and apportion it among the class (RSMo 537.095).
8. **Survival vs wrongful death.** Under RSMo 537.020, personal injury claims survive death. When the injury caused the death, the decedent's pre-death losses are recovered within the wrongful death action (537.085), not in a separate survival suit. Claims for injuries unrelated to the death survive through the estate.
9. **Federal civil-rights deaths.** A 1983 claim for a death in police custody or by excessive force uses 42 U.S.C. 1988 to borrow state survival and wrongful-death law where it does not undercut 1983's purposes - research the 8th Circuit approach and who is the proper plaintiff before filing.

## Output
- Class determination: proper plaintiff(s) and who must get notice.
- Elements chart for the underlying wrong.
- Damages table by category with evidence source.
- Deadline calendar (3-year limit, any notice of claim, med-mal requirements).

## Pitfalls
- A lower-class relative suing when a higher-class member exists.
- Filing a second wrongful death action; failing to notify other class members.
- Treating the 3-year period as running from the injury rather than the death.
- Settling without court approval and apportionment.
- Missing medical-negligence pre-suit requirements (e.g., health care affidavit, RSMo 538.225).

## Verify before relying
- Pull verbatim RSMo 537.020, 537.080, 537.085, 537.090, 537.095, 537.100, and ch. 538 provisions via `statute-lookup`.
- Confirm current case law on the single-action rule and 1983 death claims (CourtListener / Descrybe treatment).
- Recompute deadlines from the death certificate date.
- Legal information, not legal advice; wrongful death cases are high stakes - strongly consider counsel (often contingency-fee).

## Related skills
- `negligence-claim-builder` - underlying negligence elements
- `section-1983-claim-builder` - constitutional death claims
- `damages-calculator` - quantifying losses
- `statute-of-limitations-checker` - deadlines and tolling
- `government-notice-of-claim` - notice when a government caused the death
