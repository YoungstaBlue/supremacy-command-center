---
name: mo-garnishment-and-execution
description: Guides collecting or defending Missouri money judgments - execution, wage and bank garnishment (Rule 90, RSMo ch. 525), exemptions (RSMo 513.430), judgment interest, and revival. Use for "garnishment", "bank levy", "exemption", "collect my judgment", or "judgment debtor exam".
---

# Missouri Garnishment and Execution

Collect a Missouri money judgment lawfully, or protect exempt income and property when a judgment is being enforced against you.

## When to use
- The user holds a judgment and wants to collect (wages, bank accounts, personal property).
- The user received a garnishment notice, bank freeze, or execution and wants to claim exemptions or object.
- The user asks about judgment interest, renewal/revival, or a debtor examination.
- Not for: defending the underlying debt lawsuit - use `fdcpa-fcra-consumer-defense`; vacating the judgment itself - use `mo-default-judgment-set-aside`.

## Gather first
- The judgment: court, case number, date entered, amount, and whether it is final (no pending post-trial motion or appeal bond).
- For debtors: sources of income (wages, Social Security, SSI, VA, unemployment, child support, pension) and which account each is deposited into; head-of-family status.
- Any notice received: date served, garnishee name, and the response deadline stated on it.

## Workflow
1. Confirm enforceability: the judgment is final and not stayed (an appeal with a supersedeas bond stays execution). Check whether it has been satisfied, discharged in bankruptcy, or is too old - Missouri judgments are presumed paid after a period unless revived (RSMo 516.350; revival procedure in Rule 74.09 - verify both).
2. Interest: post-judgment interest is set by RSMo 408.040; compute from the judgment date at the rate stated in the judgment or the statute.
3. Creditor tools:
   - Execution (Rule 76): writ directing the sheriff to levy on non-exempt property.
   - Garnishment (Rule 90; RSMo ch. 525): writ served on a third party holding the debtor's money (employer, bank). Garnishee answers interrogatories; the court orders payment.
   - Debtor examination: Rule 76 provides for examining the judgment debtor about assets - verify the specific rule number and procedure.
4. Debtor exemptions - identify each that applies and claim it in writing:
   - Personal property exemptions in RSMo 513.430 (household goods, vehicle, tools of trade, certain benefits, retirement plans, and more - read the current dollar caps), plus the additional head-of-family exemption (RSMo 513.440 - verify).
   - Homestead exemption (RSMo 513.475 - verify current amount).
   - Wage limits: federal law caps garnishment of disposable earnings (15 U.S.C. 1673); RSMo 525.030 sets Missouri's limits, including a lower percentage for a head of family residing in Missouri - read the current text.
   - Federal benefits: Social Security and SSI are protected from garnishment by federal law (42 U.S.C. 407 for Social Security); banks must protect certain directly deposited federal benefits under Treasury rules (31 C.F.R. part 212 - verify).
   - Property held as tenants by the entirety may be protected from one spouse's individual debts.
5. Debtor procedure: file the exemption claim/request for hearing within the deadline on the notice; attach proof (benefit award letters, bank statements tracing deposits, pay stubs, head-of-family facts). Ask the court to release exempt funds and to stop future withholding as to exempt sources.
6. Creditor compliance: serve notices exactly as required, honor exemption claims pending hearing, and file returns and satisfactions. Wrongful garnishment of exempt funds creates exposure.
7. Satisfaction: once paid, the creditor must file a satisfaction of judgment; a debtor can move to compel it.
8. Consider bankruptcy counsel if multiple judgments exist - the automatic stay halts collection.

## Output
- Status snapshot: Judgment date | Amount | Interest rate and accrued | Revival/presumption-of-payment date | Stays.
- Exemption worksheet: Asset/income source | Amount | Exemption claimed (statute) | Proof attached | Notes.
- Draft documents (as needed): Request for Exemption Hearing; Motion to Release Exempt Funds; Application for Writ of Garnishment/Execution; Satisfaction of Judgment.

## Pitfalls
- Missing the short deadline on a garnishment notice to claim exemptions.
- Commingling exempt benefits with other funds without records to trace them.
- Assuming a wage percentage without checking head-of-family status and current statute text.
- Creditors levying on obviously exempt property or garnishing after the judgment is satisfied.
- Ignoring that bankruptcy discharge or an appeal bond may bar collection.
- Letting a judgment lapse without timely revival.

## Verify before relying
- Pull verbatim Rules 74.09, 76, 90 and RSMo 408.040, 513.430, 513.440, 513.475, 516.350, 525.030 via `statute-lookup` - exemption amounts change.
- Confirm federal provisions (15 U.S.C. 1673, 42 U.S.C. 407, 31 C.F.R. part 212) via Descrybe or official sources.
- Recompute response deadlines from the actual service date.
- Legal information, not legal advice; legal aid often handles exemption claims.

## Related skills
- `fdcpa-fcra-consumer-defense` - collector misconduct during collection.
- `mo-default-judgment-set-aside` - attacking the judgment itself.
- `mo-deadline-calculator` - exemption and hearing deadlines.
- `damages-calculator` - judgment interest computations.
- `lawmind-god-drafter` - assembles exemption request with supporting affidavit.
