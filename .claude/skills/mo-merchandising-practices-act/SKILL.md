---
name: mo-merchandising-practices-act
description: Builds or defends Missouri Merchandising Practices Act claims (RSMo 407.020, 407.025) - unlawful practice, household purchase, ascertainable loss, 2020 reasonable-consumer elements, punitive damages, fees. Use for "MMPA", "consumer fraud", "dealer lied", "deceptive practice", or "scammed by a business".
---

# Missouri Merchandising Practices Act

Tests a consumer-deception claim against the elements of RSMo 407.025 as amended in 2020, and pleads it with facts that survive a motion to dismiss.

## When to use
- A seller, dealer, contractor, lender, or servicer misrepresented or concealed a material fact in a consumer transaction
- Adding an MMPA count to a contract, warranty, repossession, or debt dispute
- Defending against, or counterclaiming in, a collection or deficiency suit arising from a consumer sale
- Not for: purely commercial (business-purpose) purchases (use `contract-breach-analyzer`); debt-collector conduct (use `fdcpa-fcra-consumer-defense`)

## Gather first
- The transaction documents, advertisements, and the exact statements or omissions (who, what, when, how communicated)
- Why the purchase or lease was primarily for personal, family, or household purposes
- The loss in money or property and the documents that quantify it

## Workflow
1. **Merchandise and sale.** "Merchandise" and "sale" are defined broadly in RSMo 407.010 (goods, services, intangibles, real estate, commodities). Confirm the transaction fits and check exemptions in 407.020 (certain regulated entities and media publishers - read the current list).
2. **Unlawful practice (RSMo 407.020.1).** Deception, fraud, false pretense, false promise, misrepresentation, unfair practice, or concealment, suppression, or omission of any material fact, in connection with the sale or advertisement of merchandise. Attorney General regulations define these terms: 15 CSR 60-7 through 60-9 (verify chapter numbers). "In connection with" reaches conduct after the sale; loan servicing was held to be in connection with the original loan in Conway v. CitiMortgage, Inc., 438 S.W.3d 410 (Mo. banc 2014).
3. **Private-action elements (RSMo 407.025.1).** Plaintiff (a) purchased or leased merchandise (b) primarily for personal, family, or household purposes, and (c) suffered an ascertainable loss of money or property (d) as a result of an unlawful practice. Since the 2020 amendments plaintiff must also establish: acted as a reasonable consumer would; the practice would cause a reasonable person to enter the transaction; and individual damages with sufficiently definitive and objective evidence to calculate the loss with reasonable certainty. The court may dismiss where the claim fails to show a likelihood the practice would mislead a reasonable consumer.
4. **What is not required.** Pre-2020 Missouri Supreme Court authority holds the MMPA does not require proof of the common-law fraud elements of intent to defraud or reliance. Hess v. Chase Manhattan Bank, USA, N.A., 220 S.W.3d 758 (Mo. banc 2007). Read Hess against the 2020 reasonable-consumer language before relying on it. The voluntary-payment doctrine is not a defense to an MMPA claim, and MMPA protections cannot be waived. Huch v. Charter Communications, Inc., 290 S.W.3d 721 (Mo. banc 2009).
5. **Ascertainable loss.** Usually benefit-of-the-bargain: value as represented minus value as received. Out-of-pocket payments, repair costs, and charges paid also count. Emotional distress alone does not.
6. **Remedies (RSMo 407.025).** Actual damages; in its discretion the court may award punitive damages, attorney fees to the prevailing party based on time reasonably expended, and equitable relief (407.025.2). Fee-shifting runs to the "prevailing party," so a losing plaintiff faces fee exposure. Punitive damages also must satisfy RSMo 510.261-510.265 procedure. No MMPA action for personal injury or death claims covered by chapter 538 (407.025.3). Class actions are authorized with specific pleading requirements (407.025.5).
7. **Venue, accrual, and limitations.** Venue is in the county where the seller or lessor resides or where the transaction took place (407.025.1). The claim accrues on the date of purchase or lease or upon receipt of notice of the unlawful practice (407.025.4). The limitations period is generally treated as five years under RSMo 516.120 (liability created by statute) - confirm with `statute-of-limitations-checker`.
8. **Pleading.** Plead each act or omission with who, what, when, where, and how; plead the household purpose, reasonable-consumer facts, and the damages computation. Courts often apply fraud-style particularity to misrepresentation-based MMPA counts.

## Output
- Element table: | Element (407.025.1 and 2020 additions) | Facts | Evidence | Gap |
- Unlawful-practice list: each statement or omission, date, speaker, why false or material, regulation it matches
- Loss computation: represented value, actual value, payments, total ascertainable loss
- Draft MMPA count (caption-ready) for `mo-petition-drafting` - user files

## Pitfalls
- Business-purpose purchases are outside the private action.
- Pleading "they lied" without the specific statement, speaker, and date.
- Damages theories without objective proof - the 2020 amendment invites dismissal or summary judgment.
- Forgetting the RSMo 510.261 et seq. procedure before seeking punitive damages.
- Treating a lender or servicer as automatically exempt without reading 407.020's exemptions.
- Missing the accrual trigger in 407.025.4 when computing limitations.
- Seeking damages for personal injury or death claims covered by chapter 538, which 407.025.3 excludes.
- Overlooking fee exposure: fees go to the prevailing party, which can be the defendant.
- Conceding a contractual waiver of MMPA rights; under Huch, MMPA protections cannot be waived by contract or by voluntary payment.
- Pleading only the 407.020 statute without tying conduct to a specific 15 CSR 60 definition.

## Verify before relying
- Pull verbatim text of RSMo 407.010, 407.020, 407.025, and 15 CSR 60-7 to 60-9 via `statute-lookup` or Descrybe `search_laws_and_rules`; confirm the 2020 amendment language and effective date.
- Check Conway, Hess, and Huch treatment (CourtListener / Descrybe), especially after the 2020 amendments.
- Recompute limitations from the transaction or loss date.
- Legal information, not legal advice; recommend counsel or legal aid for high-stakes decisions.

## Related skills
- `contract-breach-analyzer` - parallel contract count
- `ucc-article-2-sales` - warranty claims in the same sale
- `fdcpa-fcra-consumer-defense` - collection-stage misconduct
- `damages-calculator` - actual and punitive damages
- `mo-petition-drafting` - plead the count
