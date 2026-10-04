---
name: settlement-and-demand-letters
description: Drafts demand letters, settlement offers, negotiation plans, settlement agreements, and releases under Missouri and federal law - FRE 408, RSMo 537.058 time-limited demands, RSMo 537.060 releases, offers of judgment. Use for "demand letter", "settle my case", "settlement agreement", or "release".
---

# Settlement and Demand Letters

Converts the case's value and leverage into a written demand, a negotiation plan with a walk-away number, and a settlement agreement whose release language does not give away more than intended.

## When to use
- Sending a pre-suit demand to a person, business, insurer, or government entity
- Responding to or making a settlement offer during litigation, including mediation prep
- Reviewing or drafting a settlement agreement, release, or stipulated dismissal
- Not for: computing damages themselves (use `damages-calculator`); strategy on whether to settle at all (use `lawmind-strategy-engine`); severance/ADEA waivers (start with `employment-discrimination-claims`)

## Gather first
- Claims, key facts, and evidence; damages figures with documentation (bills, receipts, wage records)
- Opponent's identity, insurer (claim number), and any prior offers; whether a government entity is involved (notice-of-claim rules)
- Deadlines in play: limitations period, scheduled trial, pending motions

## Workflow
1. **Value the case.** Pull the damages model from `damages-calculator`; discount for liability risk, collectability (insurance limits, judgment-proof defendant), costs, and time. Set three numbers: opening demand, target, and walk-away (BATNA — what happens if no deal).
2. **Protect deadlines first.** A demand does not toll the statute of limitations or any notice-of-claim deadline. If the limitations date is near, file first and negotiate after (check `statute-of-limitations-checker`, `government-notice-of-claim`).
3. **Settlement-communication protection.** Label offers "For settlement purposes only — subject to FRE 408." FRE 408 bars using compromise offers and statements to prove or disprove the validity or amount of a disputed claim, with exceptions (e.g., bias, obstruction). Missouri state courts apply a similar common-law exclusion — verify current Missouri authority. Do not put admissions you cannot afford to have used in other ways (e.g., impeachment in some contexts, criminal matters) into the letter.
4. **Draft the demand letter.**
   - Heading: date, recipient, claim number, method of delivery (keep proof)
   - Facts: short, dated, neutral, provable
   - Liability: each claim and why it is met, with key evidence (attach selectively)
   - Damages: itemized table plus non-economic description
   - Demand: specific amount and any non-monetary terms
   - Deadline for response and statement of next step if no response (only steps the user actually intends)
   - Personal injury / wrongful death against insured tortfeasors: RSMo 537.058 imposes specific content, delivery, and minimum-open-period requirements for time-limited demands — pull the current text and comply exactly or the demand may be unenforceable. RSMo 408.040 links prejudgment interest in tort cases to a qualifying written demand — check its requirements.
5. **Avoid extortion lines.** Never threaten criminal prosecution, a bar or licensing complaint, or public exposure to gain civil money; demand only what the claim supports.
6. **Negotiation moves.** Respond to offers in writing; make concessions in decreasing increments; justify each number with evidence; ask for the basis of their number. Consider mediation if the court offers it.
7. **Offers of judgment.** Federal FRCP 68: defendant's offer served at least 14 days before trial; if not accepted within 14 days and the final judgment is not more favorable, plaintiff pays post-offer costs. Missouri has an offer-of-judgment rule (Rule 77.04) — pull current text for timing and consequences.
8. **Settlement agreement checklist.**
   - Parties (including insurers/affiliates being released) and consideration; payment amount, method, and deadline
   - Release scope: specific claims and dates vs. "any and all claims known or unknown" — narrow to the incident; carve out claims not being released
   - Multiple defendants: in Missouri, a release of one tortfeasor reduces claims against others by the stated amount or consideration paid (RSMo 537.060) — state amounts clearly and reserve claims against non-settling parties
   - Dismissal: with or without prejudice, who files, each side bears own fees/costs (or not)
   - Confidentiality, non-disparagement, no-admission clauses — check they do not bar truthful testimony or complaints to agencies
   - Liens: medical providers, Medicare (Medicare Secondary Payer rules, 42 U.S.C. 1395y(b)), Medicaid, child support — who pays and indemnity
   - Taxes: damages for physical injury are generally excluded from income (26 U.S.C. 104(a)(2)); other amounts may be taxable — consult a tax professional
   - Minors or incapacitated persons: court approval required — verify the governing statute and procedure
   - Default/enforcement clause and court retaining jurisdiction to enforce
9. **Before signing**, read every term against the checklist; get the payment before or simultaneously with filing the dismissal where possible.

## Output
- Valuation sheet: opening / target / walk-away with reasoning
- Demand letter draft with headings above and itemized damages table
- Settlement agreement or term-sheet draft, plus a release-scope review table: | Clause | Risk | Suggested edit |

## Pitfalls
- Letting the limitations or notice-of-claim deadline pass during negotiations
- Overbroad releases that waive unrelated or unknown claims, or release non-settling defendants
- Ignoring liens (especially Medicare), leaving the user personally liable
- Threats tied to criminal or disciplinary action
- Accepting an oral deal without written terms; dismissing before payment
- Non-compliant time-limited demand under RSMo 537.058

## Verify before relying
- Pull verbatim FRE 408, FRCP 68, Missouri Rule 77.04, RSMo 537.058, 537.060, 408.040 via `statute-lookup` (or Descrybe `search_laws_and_rules`); confirm case law is still good law.
- Recompute limitations, offer, and acceptance deadlines from actual dates.
- Legal information, not legal advice; for significant settlements, have counsel review the agreement.

## Related skills
- `damages-calculator` — the numbers behind the demand
- `statute-of-limitations-checker` / `government-notice-of-claim` — deadlines negotiations do not stop
- `lawmind-strategy-engine` — leverage and settle-or-try analysis
- `court-document-formatting` — stipulated dismissal and proposed order formatting
