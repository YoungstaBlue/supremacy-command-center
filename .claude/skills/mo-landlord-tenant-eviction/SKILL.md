---
name: mo-landlord-tenant-eviction
description: Guides Missouri eviction and tenant disputes - rent and possession (RSMo 535), unlawful detainer (534), notices, lockouts, repair-and-deduct, habitability, security deposits, trial de novo, appeal bonds. Use for "eviction notice", "rent and possession", "landlord locked me out", or "security deposit".
---

# Missouri Landlord-Tenant and Eviction

Identifies which Missouri eviction action is in play, the defenses and timelines that apply, and the tenant's or landlord's affirmative claims (deposit, lockout, repairs).

## When to use
- Served with a rent-and-possession or unlawful-detainer summons, or a notice to vacate
- Landlord changed locks, removed belongings, or cut utilities
- Security deposit not returned or improperly withheld; repair problems and habitability
- Not for: injuries on rental property (use `premises-and-landlord-liability`); commercial lease disputes (use `contract-breach-analyzer`)

## Gather first
- The summons and petition (court date, case type), the lease, and every notice received with delivery dates
- Rent ledger and proof of payments or tenders; any subsidy (Section 8, public housing, federally backed mortgage)
- Photos, code-inspection reports, repair requests with dates; move-out date and deposit amount for deposit claims

## Workflow
1. **Identify the action.**
   - Rent and possession (RSMo 535.010-535.040): for nonpayment; requires that rent was due and demanded. Summons served at least four days before the court date (535.030).
   - Unlawful detainer (RSMo 534.030): holding over after the term ends or after proper termination, or after foreclosure with required notice. Service at least four days before court date (534.090).
   - Forcible entry and detainer: a landlord lockout or utility shutoff without judicial process is deemed forcible entry and detainer (RSMo 441.233).
2. **Check the termination notice (unlawful detainer).** Month-to-month and other tenancies of less than one year (and tenancies at will or sufferance) require one month's written notice to vacate (RSMo 441.060). Read the lease for any additional notice terms. For properties covered by the federal CARES Act, a 30-day notice to vacate may be required for nonpayment (15 U.S.C. 9058(c) - verify current applicability and coverage). Subsidized housing: check program-specific notice rules.
3. **Rent-and-possession defenses.**
   - Tender: if the rent due plus all costs is tendered before the judge at the hearing, judgment for possession should not enter (RSMo 535.040). Bring certified funds and a ledger.
   - No demand for rent; amount claimed includes non-rent charges; payments not credited; landlord refused tender.
   - Implied warranty of habitability as a defense or offset where conditions violate housing codes. King v. Moorehead, 495 S.W.2d 65 (Mo. App. 1973). Document code violations and notice to the landlord.
4. **Unlawful-detainer defenses.** Defective or insufficient termination notice; tenancy not actually ended; acceptance of rent after termination (waiver argument - fact-specific); improper party or wrong premises. Damages for unlawful detainer can be doubled in the judgment (RSMo 534.330), so assess exposure.
5. **Repair and deduct (RSMo 441.234).** Available only to a tenant who has lawfully resided six consecutive months, paid all rent, and has no uncured written lease-violation notice. Condition must affect habitability, sanitation, or security and violate a local housing or building code; cost under $300 or half the periodic rent, whichever is greater, not exceeding one month's rent. Written notice to the landlord, 14 days (or prompt in an emergency) to fix, then workmanlike repair and itemized receipts. Read the statute's remaining conditions before advising.
6. **Security deposit (RSMo 535.300).** Max two months' rent. Within 30 days after the tenancy ends, landlord must return the deposit or send an itemized list of damages with the balance. Allowed deductions: unpaid rent, restoring the unit beyond ordinary wear and tear, and actual damages from inadequate notice to terminate. Tenant may attend the move-out inspection after reasonable written notice. Wrongful withholding: tenant recovers twice the amount wrongfully withheld. The deposit cannot be applied by the tenant in lieu of rent.
7. **Lockouts and property.** Removal or exclusion without court order, or interruption of essential utilities, is forcible entry and detainer (441.233); a separate abandonment procedure exists (RSMo 441.065) - check whether the landlord met it.
8. **After judgment.** For cases heard by an associate circuit judge under chapter 535, the losing party has a right to trial de novo (RSMo 512.180); file the application within ten days after judgment (RSMo 512.190). A trial de novo or appeal does not stay execution unless the defendant posts the required bond within ten days of judgment and pays accruing rent into court (RSMo 535.110; for unlawful detainer see 534.380). Verify current bond rules with the clerk.

## Output
- Case-type determination with the governing statute and hearing date
- Defense checklist: | Defense | Facts | Evidence | Raise at hearing (Y/N) |
- Tender worksheet: rent due, costs, amount to bring
- Deposit demand letter or repair notice draft (for the user to send), with statutory deadlines computed

## Pitfalls
- Missing the hearing; eviction cases move in days, not weeks.
- Withholding rent without following 441.234 exactly, which gives the landlord a nonpayment case.
- Arriving without the full rent and costs when relying on tender.
- Letting the ten-day trial de novo / bond window pass.
- Landlords: self-help lockouts and utility shutoffs create liability.

## Verify before relying
- Pull verbatim text of RSMo 441.060, 441.065, 441.233, 441.234, 512.180, 512.190, 534.030, 534.090, 534.330, 534.380, 535.010-535.040, 535.110, 535.300, and 15 U.S.C. 9058 via `statute-lookup` or Descrybe `search_laws_and_rules`.
- Check King v. Moorehead and any later habitability cases for current treatment (CourtListener / Descrybe); note a case annotation questioning the appeal-bond requirement and confirm current enforceability.
- Recompute every deadline from the actual service, judgment, or move-out date; check local court rules.
- Legal information, not legal advice; legal aid offices handle many evictions - recommend contacting one quickly.

## Related skills
- `mo-small-claims-associate-circuit` - associate circuit procedure and trial de novo
- `premises-and-landlord-liability` - injuries from unsafe conditions
- `mo-deadline-calculator` - compute the ten-day and 30-day windows
- `mo-pro-se-courtroom-procedure` - presenting the defense at the hearing
- `settlement-and-demand-letters` - move-out or payment agreements
