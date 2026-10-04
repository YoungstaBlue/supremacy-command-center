---
name: fdcpa-fcra-consumer-defense
description: Analyzes debt collection and credit reporting problems under the FDCPA, Regulation F, and FCRA, and builds defenses to debt-buyer suits in Missouri courts. Use for "debt collector", "validation letter", "sued for credit card debt", "credit report dispute", "FDCPA violation", or "time-barred debt".
---

# FDCPA, FCRA, and Debt-Suit Defense

Spots collector and credit-reporting violations, plans disputes that preserve claims, and organizes the defense of a collection lawsuit, including FDCPA/FCRA counterclaims where appropriate.

## When to use
- Collector calls, letters, texts, or lawsuits; requests for debt validation
- Inaccurate or outdated items on a credit report; disputes ignored
- Defending a debt-buyer or original-creditor suit in associate circuit court
- Not for: suits on a promissory note (pair with `ucc-article-3-negotiable-instruments`); repossession and deficiency (use `ucc-article-9-secured-transactions`); seller deception (use `mo-merchandising-practices-act`)

## Gather first
- Every collection communication with dates (letters with envelopes, call log, voicemails, texts) and the summons/petition if sued
- Credit reports from all three bureaus, any dispute letters sent, and bureau/furnisher responses with dates
- Account history: original creditor, last payment date, charge-off date, any writing signed

## Workflow
1. **Coverage (FDCPA).** "Debt" is a consumer obligation for personal, family, or household purposes; "debt collector" is a person whose principal purpose is collecting debts or who regularly collects debts owed another (15 U.S.C. 1692a). Original creditors generally are not covered. A buyer collecting debts it owns is not a debt collector under the "owed another" prong. Henson v. Santander Consumer USA Inc., 582 U.S. 79 (2017) - check the "principal purpose" prong separately. Lawyers who regularly collect through litigation can be debt collectors. Heintz v. Jenkins, 514 U.S. 291 (1995).
2. **Violations checklist (FDCPA).** Communications limits - time, place, workplace, represented consumer, cease request (1692c); harassment or abuse (1692d); false or misleading representations, including the amount or legal status of the debt and threatening action not intended or legally allowed (1692e); unfair practices, including collecting unauthorized amounts (1692f); validation notice and verification (1692g - dispute in writing within the 30-day period to trigger verification and pause collection). Regulation F, 12 C.F.R. part 1006, adds call-frequency and validation-notice content rules.
3. **FDCPA remedies and timing.** Actual damages, statutory damages up to $1,000 per action for an individual, costs and reasonable attorney fees (1692k). Suit within one year from the date of the violation (1692k(d)); there is no general discovery rule. Rotkiske v. Klemm, 589 U.S. 8 (2019).
4. **FCRA disputes.** Dispute to the consumer reporting agency in writing; the agency must reinvestigate, generally within 30 days (15 U.S.C. 1681i). The furnisher's duty to investigate is triggered by notice from the agency (1681s-2(b)); there is no private right of action for violations of the furnisher accuracy duties in 1681s-2(a). Most negative items age off after seven years (1681c). Keep copies and proof of mailing.
5. **FCRA remedies and timing.** Willful noncompliance: actual or statutory damages, punitive damages, fees (1681n). Negligent: actual damages and fees (1681o). Suit within two years after discovery of the violation, but no later than five years after it occurred (1681p).
6. **Standing in federal court.** A bare procedural violation is not enough; plead concrete harm (money lost, inaccurate report sent to third parties, real-world consequences). TransUnion LLC v. Ramirez, 594 U.S. 413 (2021). State court may be an alternative forum.
7. **Defending the debt suit (Missouri).**
   - Calendar the return/appearance date on the summons. In associate circuit cases, affirmative defenses and counterclaims must be filed in writing by the return date unless the court grants leave; other allegations are deemed denied if no responsive pleading is filed (RSMo 517.031). Appear in person regardless.
   - Defenses: plaintiff's standing and chain of assignment (demand the bill of sale and the account-level schedule); lack of proof of the account and the balance (business-records foundation for a debt buyer's records); limitations - typically five years for open accounts and implied contracts (RSMo 516.120), ten years for a written promise to pay money (RSMo 516.110); payment; identity theft; unauthorized fees or interest.
   - Counterclaims: FDCPA (suing or threatening on time-barred debt, misstating the amount) and MMPA where the facts fit; watch the one-year FDCPA limit.
   - Discovery to the plaintiff: assignment documents, original agreement and terms, full transaction history.
8. **Settlement discipline.** Get any deal in writing: amount, payment schedule, dismissal with prejudice, credit-reporting treatment, and no further sale of the account.

## Output
- Violation table: | Date | Communication | Statute/section | Violation theory | Evidence | Limit deadline |
- Dispute letter drafts (debt validation under 1692g; CRA dispute under 1681i) - for the user to send
- Debt-suit defense outline: Return date / Defenses with facts / Counterclaims / Discovery requests / Settlement terms

## Pitfalls
- Missing the return date and suffering a default judgment; see `mo-default-judgment-set-aside` if it already happened.
- Making a payment or written acknowledgment on an old debt without first checking whether it affects limitations or revives collection.
- Disputing only with the furnisher; the 1681s-2(b) private claim requires a dispute through a consumer reporting agency.
- Filing FDCPA claims after the one-year limit.
- Suing an original creditor under the FDCPA when it does not meet the statutory definition.
- Sending dispute letters without keeping proof of mailing and copies of enclosures.
- Disputing by phone or online portal only, leaving no clean written record of what was disputed and when.

## Verify before relying
- Pull verbatim text of 15 U.S.C. 1692a, 1692c-1692g, 1692k, 1681c, 1681i, 1681n-1681p, 1681s-2, 12 C.F.R. part 1006, and RSMo 516.110, 516.120, 517.031 via `statute-lookup` or Descrybe `search_laws_and_rules`.
- Check Henson, Heintz, Rotkiske, and TransUnion treatment and 8th Circuit applications (CourtListener / Descrybe).
- Recompute every limitations date from the actual violation or discovery date.
- Legal information, not legal advice; recommend counsel or legal aid for high-stakes decisions.

## Related skills
- `mo-small-claims-associate-circuit` - procedure for associate circuit debt suits
- `mo-default-judgment-set-aside` - if a default already entered
- `mo-garnishment-and-execution` - exemptions after judgment
- `statute-of-limitations-checker` - accrual and revival questions
- `mo-merchandising-practices-act` - parallel state consumer claim
