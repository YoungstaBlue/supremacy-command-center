---
name: damages-calculator
description: Quantifies damages for Missouri tort and 1983 claims - economic and non-economic losses, punitive damages (RSMo 510.261-510.265), fault and settlement offsets, and judgment interest. Use for "how much can I get", "damages", "prayer for relief", "punitive damages", or "settlement value".
---

# Damages Calculator

Builds a sourced, category-by-category damages model that supports a prayer for relief, a demand letter, or a settlement range - with every number tied to a document.

## When to use
- Drafting a prayer for relief or a damages section of a petition, complaint, or demand letter
- Valuing a case for settlement or mediation
- Deciding whether and when to seek leave to plead punitive damages
- Answering a damages interrogatory or preparing a damages exhibit for trial
- Not for: drafting the demand letter itself (use `settlement-and-demand-letters`)

## Gather first
- Bills, receipts, pay records, tax returns, repair estimates, and any amounts actually paid by insurance
- The claims pleaded (tort, contract, 1983, wrongful death) - each has different recoverable categories
- Dates: injury date, demand dates and how sent (prejudgment interest turns on them)

## Workflow
1. **List recoverable categories by claim.**
   - Economic: past medical, future medical (needs a medical basis), past lost wages, lost earning capacity, property damage (repair cost or diminished value), out-of-pocket costs.
   - Non-economic: pain and suffering, emotional distress, loss of enjoyment of life, disfigurement, loss of consortium (spouse's separate claim).
   - Nominal: where a right was violated without provable loss (trespass, 1983 - Carey v. Piphus, 435 U.S. 247 (1978)).
   - Punitive: only on proper showing (step 5).
   - Wrongful death categories differ - use `wrongful-death-and-survival-mo`.
2. **Document every economic number.** Each line gets a source exhibit. Use amounts actually paid or owed where Missouri's collateral-source statute applies - RSMo 490.715 was amended in 2017 to address evidence of actual medical costs; pull the current text before valuing medical specials.
3. **Future losses.** Require reasonable certainty: medical opinion for future treatment, work-life and wage evidence for earning capacity. Reduce to present value where required; note when an economist is needed.
4. **Non-economic.** No formula in Missouri law. Support with testimony about daily-life impact, treatment duration, and permanency. Per-diem arguments are risky - check current Missouri treatment before using.
5. **Punitive damages (Missouri).**
   - Standard: RSMo 510.261 requires clear and convincing evidence that the defendant intentionally harmed the plaintiff without just cause or acted with deliberate and flagrant disregard for the safety of others (verify current wording).
   - Pleading: RSMo 510.261 bars a punitive claim in the initial pleading; a later pleading requires leave of court on a motion filed by a deadline tied to the pretrial conference or trial setting - pull the statute for the exact timing.
   - Trial: RSMo 510.263 provides a bifurcated procedure for punitive damages.
   - Cap: RSMo 510.265 caps punitive awards at the greater of $500,000 or five times the net judgment, with statutory exceptions. Lewellen v. Franklin, 441 S.W.3d 136 (Mo. banc 2014) held the cap unconstitutional as applied to a common-law fraud claim - check current treatment before relying on either the cap or the exception.
   - Constitutional limits: ratio and reprehensibility guideposts in BMW of North America, Inc. v. Gore, 517 U.S. 559 (1996) and State Farm Mutual Automobile Insurance Co. v. Campbell, 538 U.S. 408 (2003).
6. **1983 damages.** Compensatory damages for actual injury; no damages for the abstract value of a constitutional right (Memphis Community School District v. Stachura, 477 U.S. 299 (1986)); punitive damages against individual officers for reckless or callous indifference (Smith v. Wade, 461 U.S. 30 (1983)) but not against municipalities. Fee-shifting under 42 U.S.C. 1988 generally does not pay a non-attorney pro se litigant attorney fees; costs remain recoverable.
7. **Medical malpractice.** Statutory noneconomic caps under RSMo 538.210 (adjusted annually) - verify current figure.
8. **Offsets.**
   - Comparative fault: reduce by plaintiff's percentage (pure comparative fault).
   - Joint tortfeasor settlements: RSMo 537.060 reduces the claim against remaining defendants by settlement amounts.
   - Mitigation: unreasonable failure to mitigate reduces recovery.
9. **Interest.** Prejudgment interest in tort cases under RSMo 408.040 depends on a written demand meeting statutory requirements (method of delivery, how long it stays open, amount) - draft any demand to satisfy the current statute. Contract and liquidated sums: RSMo 408.020 (9%). Post-judgment interest: RSMo 408.040 sets different rates for tort and non-tort judgments - pull the current text.
10. **Build the range.** Low (documented specials only), likely (specials plus supported non-economic), high (all categories including punitive if leave is likely). State assumptions.

## Output
- Damages table: | Category | Amount | Basis/assumption | Source exhibit | Recoverable under which count |
- Offsets table: comparative fault %, settlement credits, mitigation
- Interest computation with start date, rate, and statutory source
- Low / likely / high range with assumptions
- Draft prayer for relief paragraph (no punitive demand in an initial Missouri petition)

## Pitfalls
- Pleading punitive damages in the initial Missouri petition instead of moving for leave
- Claiming billed amounts without accounting for the collateral-source statute
- Future damages with no medical or economic foundation
- Asking for damages for the "value" of a constitutional right
- A demand letter that fails 408.040 formalities, forfeiting prejudgment interest
- Ignoring settlement credits from co-defendants

## Verify before relying
- Pull verbatim RSMo 510.261, 510.263, 510.265, 408.020, 408.040, 490.715, 537.060, 538.210 via `statute-lookup` (or Descrybe `search_laws_and_rules`) - several were amended recently
- Confirm Lewellen and the federal damages cases are still good law (CourtListener / Descrybe)
- Recompute interest from actual demand and judgment dates
- Legal information, not legal advice; valuation of serious-injury cases warrants counsel

## Related skills
- `negligence-claim-builder` - liability side of the case
- `wrongful-death-and-survival-mo` - death-case damages under RSMo 537.090
- `settlement-and-demand-letters` - turn the model into a demand
- `section-1983-claim-builder` - federal claim damages
- `lawmind-strategy-engine` - settlement leverage analysis
