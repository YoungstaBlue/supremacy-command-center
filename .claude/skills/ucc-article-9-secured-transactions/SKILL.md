---
name: ucc-article-9-secured-transactions
description: Analyzes UCC Article 9 secured transactions in Missouri (RSMo 400.9) - attachment, perfection, priority, repossession, notice of sale, deficiency defenses, and the RSMo 408.555 right to cure. Use for "repossession", "car repossessed", "deficiency balance", "lien priority", "UCC-1", or "breach of the peace".
---

# UCC Article 9 Secured Transactions

Tests whether a creditor's security interest attached and was perfected, who has priority, and whether repossession, sale, and any deficiency claim complied with Article 9 and Missouri consumer credit law.

## When to use
- A vehicle or other collateral was repossessed or is threatened with repossession
- Defending a deficiency suit after a repossession sale
- Competing liens on the same property (lender vs. lender, lien creditor, buyer)
- Not for: whether the note itself is enforceable (use `ucc-article-3-negotiable-instruments`); warranty problems with the goods (use `ucc-article-2-sales`); collector harassment (use `fdcpa-fcra-consumer-defense`)

## Gather first
- Security agreement / retail installment contract, any UCC-1 filing or certificate of title showing the lien
- Payment history, default date, every notice received (right to cure, notice of sale, post-sale explanation) with dates and envelopes
- How the repossession happened (time, place, objection made, police present) and the sale price obtained

## Workflow
1. **Scope and classification.** Article 9 applies to security interests in personal property by contract (400.9-109). Classify collateral: consumer goods, equipment, inventory, accounts, etc. (400.9-102); consumer-goods transactions get extra protections.
2. **Attachment (400.9-203(b)).** Value given; debtor has rights in the collateral; and an authenticated security agreement describing the collateral (or possession/control). Description must reasonably identify (400.9-108); "all personal property" is insufficient in the security agreement itself.
3. **Perfection.** Filing a financing statement (400.9-310) with the proper office (400.9-501); automatic perfection for a purchase-money security interest in consumer goods (400.9-309(1)), except titled goods. Motor vehicles: perfection is by notice of lien to the Director of Revenue under the certificate-of-title statute (400.9-311; RSMo 301.600 - notice delivered within 30 days relates back to creation). Financing statements lapse after five years unless continued (400.9-515).
4. **Priority.** Perfected beats unperfected; among perfected interests, first to file or perfect (400.9-322); PMSI super-priority rules (400.9-324); lien creditor vs. unperfected interest (400.9-317); buyer in ordinary course takes free of seller-created interests (400.9-320).
5. **Missouri consumer right to cure (check first in consumer credit).** After a payment default of ten days, the lender may send a notice of default and right to cure (RSMo 408.554). For a default consisting only of a missed payment, the lender may not accelerate or repossess until twenty days after that notice is given to the borrower and all cosigners; tender of past-due sums plus delinquency charges cures (RSMo 408.555). Confirm the transaction is a covered consumer credit transaction and read the exceptions.
6. **Repossession (400.9-609).** Secured party may take possession after default by judicial process or without it if it proceeds without breach of the peace. Breach of peace issues: entry into a closed garage, debtor's contemporaneous objection, use of police to intimidate. Personal property inside the vehicle must be returned.
7. **Disposition.** Every aspect must be commercially reasonable (400.9-610). Reasonable authenticated notice before disposition to debtor and secondary obligors (400.9-611); consumer-goods notice content (400.9-614). Debtor may redeem before disposition by paying the full obligation plus expenses (400.9-623). Proceeds applied per 400.9-615; consumer-goods post-sale explanation of surplus or deficiency (400.9-616).
8. **Deficiency and remedies.** Non-consumer: rebuttable-presumption rule - if the creditor cannot prove compliance, the deficiency is reduced (400.9-626(a)); for consumer transactions 400.9-626 leaves the rule to the courts, so research Missouri case law. Debtor damages for noncompliance (400.9-625(b)); in consumer-goods transactions a statutory minimum recovery is available (400.9-625(c)(2)). Pair with Missouri consumer statutes as counterclaims.

## Output
- Compliance checklist: | Step | Statute | Date / document | Complied? | Consequence if not |
- Priority ladder for competing creditors with the governing rule for each rung
- Deficiency-defense outline: Attachment / Perfection (if relevant) / Right-to-Cure Notice / Repossession Conduct / Notice of Disposition / Commercial Reasonableness / Calculation Errors / Counterclaim under 400.9-625

## Pitfalls
- Not raising defective notice or commercially unreasonable sale as an affirmative defense and counterclaim in the deficiency suit.
- Physically resisting a repossession instead of objecting clearly and documenting it.
- Assuming a UCC-1 perfects a lien on a titled vehicle (it does not; the title notation does).
- Missing the redemption window before the sale.
- Ignoring the 408.555 twenty-day cure period in consumer cases.
- Treating a voluntary surrender as waiving Article 9 rights; notice, commercially reasonable sale, and accounting duties still apply.
- Accepting the creditor's deficiency figure without demanding the sale documents, auction report, and itemized expenses.
- Overlooking cosigners and guarantors, who are secondary obligors entitled to their own notice of disposition.
- Waiting to raise breach of peace; capture witness statements, photos, and police call records immediately.
- Assuming a strict-foreclosure proposal (keeping collateral in satisfaction) can be accepted silently in consumer cases without reading 400.9-620.
- Forgetting that the right to redeem can be cut off by the sale itself; calendar the sale date from the notice.

## Verify before relying
- Pull verbatim text of RSMo 400.9- sections cited, RSMo 301.600, and RSMo 408.554-408.555 via `statute-lookup` or Descrybe `search_laws_and_rules`.
- Research current Missouri case law on the consumer deficiency rule and breach of peace; check treatment before citing.
- Recompute notice and cure dates from actual mailing/delivery dates.
- Legal information, not legal advice; recommend counsel or legal aid for high-stakes decisions.

## Related skills
- `ucc-article-3-negotiable-instruments` - enforceability of the note
- `mo-merchandising-practices-act` - deceptive financing or sale practices
- `fdcpa-fcra-consumer-defense` - repo agents and collectors; credit reporting of the deficiency
- `mo-replevin-and-property-recovery` - recovering personal property or wrongfully taken collateral
- `mo-answer-affirmative-defenses` - plead the defenses and counterclaims
