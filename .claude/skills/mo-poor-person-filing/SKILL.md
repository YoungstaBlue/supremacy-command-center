---
name: mo-poor-person-filing
description: Prepares a Missouri request to proceed as a poor person under RSMo 514.040 - indigency affidavit, financial disclosure, waiver of filing, service, and appeal costs. Use for "poor person", "can't afford the filing fee", "fee waiver", or "in forma pauperis in Missouri state court".
---

# Missouri Poor Person Filing

Build a complete, truthful Missouri poor-person application so court costs and service fees are waived without delaying the case.

## When to use
- Starting a Missouri state-court case and unable to pay the filing fee or sheriff/service costs.
- Appealing, or needing a transcript, without funds.
- A poor-person request was denied and the user wants to renew it or respond to the court.
- Not for: federal court fee waivers under 28 U.S.C. 1915 - use `federal-ifp-1915`.

## Gather first
- Household income (all sources, monthly), household size and dependents, assets (cash, accounts, vehicles, property), debts, and monthly expenses.
- Whether the user receives means-tested benefits (SNAP, SSI, Medicaid, TANF) - useful supporting proof.
- The court and case stage (new petition, pending case, appeal) and whether the user is incarcerated (separate statutory rules apply to offender suits - locate them with `statute-lookup`).

## Workflow
1. Confirm the legal basis. RSMo 514.040 lets a court, if satisfied a party is a poor person unable to pay the costs of the suit, permit the party to commence and prosecute the action as a poor person, with process and proceedings without fees. It is discretionary. Read the verbatim current text - note who it covers (the text speaks to the plaintiff) and what it says about counsel and cost recovery.
2. Get the court's form. Missouri courts commonly use a statewide motion/affidavit to proceed as a poor person (check the Missouri Courts forms page and the local circuit clerk). Use the court's form if one exists; a homemade motion is a fallback.
3. Complete the financial affidavit truthfully and completely: income, assets, expenses, dependents, benefits. Every blank answered; "0" or "none" rather than empty. The affidavit is sworn - false statements risk perjury and dismissal.
4. Write a short motion: request leave to file and prosecute without prepayment of fees and costs, including service by sheriff or special process server; cite RSMo 514.040; reference the attached affidavit; request waiver of service fees specifically if the form does not.
5. File the motion with (or before) the petition. Ask the clerk whether the petition will be held pending ruling or filed on the date received - this matters for limitations deadlines. If a deadline is close, ask the clerk how to protect the filing date.
6. Service: once granted, request that summons issue and that the sheriff serve without prepayment. Confirm in writing that the order covers service fees.
7. Appeal stage: poor-person status in the trial court may not automatically carry to the appeal or transcript costs. Check the appellate rules for the docket fee and file a separate motion in the appropriate court if needed.
8. If denied: request findings or a hearing, supplement the affidavit with documentation (benefit letters, pay stubs, bank statements), or pay and preserve the issue. Calendar any order to pay by a date certain - failure can lead to dismissal.
9. Keep the order: attach a copy to later requests (subpoenas, certified copies, transcripts) so the clerk applies the waiver.

## Output
- Completed checklist of the court's form fields with the user's figures (no invented numbers).
- Draft motion headings: Caption; Motion to Proceed as a Poor Person; Grounds (inability to pay, summary of affidavit); Authority (RSMo 514.040); Relief Requested (waiver of filing fee, service costs, other costs); Verification/Signature; Certificate of Service (if case pending).
- Supporting-documents list to attach.

## Pitfalls
- Leaving blanks or understating assets - courts deny incomplete affidavits and may question credibility.
- Assuming the fee waiver covers sheriff service, transcripts, or appeal fees when the order does not say so.
- Missing a limitations deadline while the poor-person motion is pending.
- Ignoring an order to pay a partial fee by a deadline.
- Not updating the court if finances materially improve while the case is pending.
- Costs may still be taxed at the end of a case - poor-person status is a waiver of prepayment, not necessarily immunity from a costs judgment; read the statute.
- Filing the affidavit unsigned or without the notarization or declaration the form requires.
- Asking for appointed counsel in a civil case as a matter of right - civil appointment is rare and discretionary; ask legal aid instead.
- Omitting household members' income when the form asks for household income.
- Forgetting to ask separately for transcript cost relief before an appeal.

## Verify before relying
- Pull verbatim RSMo 514.040 and any applicable offender-litigation statutes via `statute-lookup`.
- Check the current circuit court form and local rules with the clerk.
- Check any case cited on the court's discretion for subsequent treatment (CourtListener).
- Legal information, not legal advice; legal aid offices can often help complete fee-waiver paperwork.

## Related skills
- `federal-ifp-1915` - the federal counterpart.
- `mo-petition-drafting` - the petition filed with the motion.
- `mo-service-of-process` - service once fees are waived.
- `lawmind-god-drafter` - bundles the application with the petition and companion papers.
- `filing-followup` - tracks the filing and the court's ruling.
