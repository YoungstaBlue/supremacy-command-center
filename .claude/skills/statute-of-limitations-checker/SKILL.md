---
name: statute-of-limitations-checker
description: Finds the limitations period, accrual, tolling, and last filing day for Missouri claims (RSMo ch. 516 and claim-specific statutes) and federal claims, including Missouri's 5-year period for 1983 and Heck deferral. Use for "statute of limitations", "is it too late to sue", or "when does my claim expire".
---

# Statute of Limitations Checker

Computes, claim by claim, how long the user has to file, when the clock started, what paused it, and the last safe filing date - before any drafting starts.

## When to use
- Any new claim or potential lawsuit, or a defense that a claim against the user is time-barred
- Deciding whether to file in state or federal court when deadlines differ
- After a dismissal without prejudice (savings statute) or when adding parties/claims (relation back)
- Not for: procedural deadlines inside a pending case (use `mo-deadline-calculator`); administrative charge deadlines for job claims (use `employment-discrimination-claims`)

## Gather first
- Each claim theory and each defendant (private, government, federal)
- Key dates: the wrongful act, when injury occurred, when it was discovered or capable of ascertainment, any prior filing and dismissal dates, end of any criminal case
- Facts bearing on tolling: plaintiff's age or incapacity at accrual, defendant concealment or absence, prior suits

## Workflow
1. **Assign each claim its Missouri period** (pull current text for each):
   - 2 years, RSMo 516.140: libel, slander, injurious falsehood, assault, battery, false imprisonment, criminal conversation, malicious prosecution.
   - 2 years, RSMo 516.105: medical malpractice (with statutory exceptions for foreign objects, failure to diagnose, and minors - verify).
   - 3 years, RSMo 537.100: wrongful death.
   - 4 years, RSMo 400.2-725: breach of a contract for the sale of goods.
   - 5 years, RSMo 516.120: contracts not covered by 516.110, statutory liabilities other than penalties, trespass, injury to property, any other injury to the person or rights of another not arising on contract (general negligence, IIED, conversion), and fraud (accrues on discovery, with a 10-year outer limit).
   - 10 years, RSMo 516.110: writings for the payment of money or property, and certain other actions.
   - Claim-specific statutes override the general ones - always search for a period inside the statute creating the claim.
2. **Fix accrual (Missouri).** RSMo 516.100: a cause of action accrues not when the wrong is done but when the damage is sustained and capable of ascertainment. Powel v. Chaminade College Preparatory, Inc., 197 S.W.3d 576 (Mo. banc 2006) frames this as when a reasonable person would have been put on notice that an injury and substantial damages may have occurred and would have undertaken to ascertain the extent. Continuing-wrong theories apply only narrowly - test carefully.
3. **Apply Missouri tolling and extensions.**
   - Minority and mental incapacity at accrual: RSMo 516.170 (does not apply to every claim - e.g., medical malpractice has its own rules).
   - Defendant's improper acts preventing suit (concealment, absconding): RSMo 516.280.
   - Defendant's absence from the state: RSMo 516.200 - narrow where the defendant remains amenable to service; verify.
   - Savings statute: RSMo 516.230 permits refiling within one year after a nonsuit (voluntary or involuntary dismissal not on the merits) if the first suit was timely - usable once.
4. **Federal claims.**
   - 42 U.S.C. 1983 borrows the state's general personal-injury period (Wilson v. Garcia, 471 U.S. 261 (1985); Owens v. Okure, 488 U.S. 235 (1989)). In Missouri the Eighth Circuit applies the 5-year period of RSMo 516.120(4) - Sulik v. Taney County, 393 F.3d 765 (8th Cir. 2005).
   - Accrual is a federal question: when the plaintiff has a complete and present cause of action (Wallace v. Kato, 549 U.S. 384 (2007) - false arrest accrues when legal process begins). Claims that would imply the invalidity of a conviction do not accrue until it is invalidated (Heck v. Humphrey, 512 U.S. 477 (1994)); fabricated-evidence claims accrue on favorable termination (McDonough v. Smith, 588 U.S. 109 (2019)).
   - Tolling for 1983 is borrowed from state law unless inconsistent with federal policy (Board of Regents v. Tomanio, 446 U.S. 478 (1980); Hardin v. Straub, 490 U.S. 536 (1989)).
   - Federal statutes enacted after December 1, 1990 without their own period: 4 years, 28 U.S.C. 1658(a).
   - FTCA: administrative claim within 2 years and suit within 6 months of denial, 28 U.S.C. 2401(b).
   - Supplemental state claims dismissed from federal court: 28 U.S.C. 1367(d) stops the clock while pending plus 30 days (Artis v. District of Columbia, 583 U.S. 71 (2018)).
5. **Adding parties or claims later.** Relation back under Missouri Rule 55.33(c) or FRCP 15(c) - new defendants relate back only if notice and mistake-of-identity requirements are met. Do not count on naming "John Doe" to preserve claims against later-identified officers.
6. **Government defendants.** Pre-suit notice statutes and administrative claim requirements may impose shorter effective deadlines - run `government-notice-of-claim`.
7. **Compute the last day.** Count from accrual using the applicable computation rule (Missouri Rule 44.01 / RSMo 1.040 for state; FRCP 6 for federal); if the last day is a weekend or legal holiday, it rolls forward. Set an internal target well before it.

## Output
- Limitations table: | Claim | Defendant | Statute and period | Accrual date and why | Tolling applied | Last filing day | Safe target date | Confidence |
- Red-flag list: claims expiring within 90 days; claims likely already barred; claims dependent on uncertain tolling
- One-paragraph explanation of the accrual theory for any contested claim

## Pitfalls
- Using the 5-year personal-injury period for battery, false imprisonment, defamation, or malicious prosecution (2 years)
- Assuming the 1983 period starts when the criminal case ends - false arrest runs from arraignment/legal process
- Relying on a savings-statute refiling twice, or after a merits dismissal
- Waiting for an internal complaint or bar complaint to "toll" a lawsuit - they generally do not
- Treating Doe defendants as preserving claims against unnamed officers
- Missing a claim-specific period hidden in the statute that creates the right

## Verify before relying
- Pull verbatim RSMo 516.100, 516.105, 516.110, 516.120, 516.140, 516.170, 516.200, 516.230, 516.280, 537.100, 400.2-725 and Rule 55.33 via `statute-lookup` (or Descrybe `search_laws_and_rules`)
- Check the cited cases remain good law and look for newer accrual decisions (CourtListener / Descrybe)
- Recompute every date from the actual event, discovery, or dismissal date
- Legal information, not legal advice; when a deadline is close or contested, consult counsel or legal aid immediately

## Related skills
- `mo-deadline-calculator` - day-counting mechanics inside a case
- `government-notice-of-claim` - pre-suit notice deadlines
- `section-1983-claim-builder` - federal civil-rights claims
- `wrongful-death-and-survival-mo` - death claims
- `filing-followup` - track whether a time-sensitive filing actually went in
