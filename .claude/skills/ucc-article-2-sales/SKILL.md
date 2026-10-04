---
name: ucc-article-2-sales
description: Analyzes sale-of-goods disputes under UCC Article 2 as enacted in Missouri (RSMo 400.2-101 et seq.) - warranties, disclaimers, rejection, revocation, cure, and buyer/seller remedies. Use for "defective product", "warranty claim", "lemon car", "reject the goods", "breach of warranty", or "seller won't refund".
---

# UCC Article 2 Sales

Works a goods-sale dispute through Missouri's enacted Article 2: was there a contract, what warranties attach, did the buyer accept or properly reject, and which Code remedy fits.

## When to use
- Defective or nonconforming goods (vehicles, appliances, equipment, inventory)
- Buyer wants to reject, revoke acceptance, or recover the price; seller wants payment or resale damages
- Warranty disclaimer or "as is" questions; written-warranty claims under Magnuson-Moss
- Not for: services or real estate contracts (use `contract-breach-analyzer`); financing and repossession (use `ucc-article-9-secured-transactions`); dealer deception (pair with `mo-merchandising-practices-act`)

## Gather first
- Purchase documents (bill of sale, buyer's order, invoice, written warranty, any "as is" sticker or disclaimer)
- Timeline: delivery date, date defect discovered, every notice/complaint to the seller and repair attempt
- Whether the seller is a merchant in goods of that kind and whether the goods are still in buyer's possession

## Workflow
1. **Scope.** Goods = things movable at the time of identification to the contract (RSMo 400.2-105). Mixed goods/services: predominant-purpose test. Note whether either party is a merchant (400.2-104); several rules turn on it.
2. **Formation and terms.** Contract may be formed in any manner showing agreement (400.2-204). Battle of the forms: 400.2-207. Statute of frauds: price of $500 or more requires a signed writing sufficient to indicate a contract, subject to exceptions (400.2-201). Unconscionability: 400.2-302.
3. **Warranties.**
   - Express warranty: affirmation of fact, promise, description, sample or model that is part of the basis of the bargain (400.2-313). Puffing is not a warranty.
   - Implied warranty of merchantability: only if seller is a merchant with respect to goods of that kind (400.2-314).
   - Implied warranty of fitness for a particular purpose: seller has reason to know the purpose and buyer relies on seller's skill (400.2-315).
   - Warranty of title: 400.2-312.
4. **Disclaimers and limits.** 400.2-316: merchantability disclaimer must mention merchantability and, if written, be conspicuous; "as is" can exclude implied warranties. Limitation of remedy (e.g., repair-or-replace only) under 400.2-719; if it fails of its essential purpose, general remedies return. Magnuson-Moss: a supplier giving a written warranty cannot disclaim implied warranties (15 U.S.C. 2308) and a consumer may sue with fee-shifting (15 U.S.C. 2310(d)).
5. **Buyer's options - pick one path and document it.**
   - Reject before acceptance: perfect tender rule (400.2-601); reject within a reasonable time and seasonably notify seller (400.2-602); state the defects (400.2-605).
   - Acceptance occurs after a reasonable opportunity to inspect without rejecting, or by acts inconsistent with seller's ownership (400.2-606).
   - After acceptance: buyer must notify seller of breach within a reasonable time or be barred from any remedy (400.2-607(3)(a)).
   - Revoke acceptance if nonconformity substantially impairs value and acceptance was based on assumption of cure or difficulty of discovery; revoke within a reasonable time and before substantial change in the goods (400.2-608).
   - Seller's right to cure: 400.2-508.
   - Insecurity and repudiation: adequate assurance (400.2-609); anticipatory repudiation (400.2-610).
6. **Buyer's remedies.** Cancel and recover price paid (400.2-711); cover damages (400.2-712) or market-price damages (400.2-713); damages for accepted goods - difference in value as warranted vs. as accepted (400.2-714); incidental and consequential damages (400.2-715).
7. **Seller's remedies.** 400.2-703 index; resale damages (400.2-706); market/lost-profit damages (400.2-708); action for the price (400.2-709).
8. **Limitations.** Four years from tender of delivery for breach of warranty, regardless of knowledge; may be shortened by agreement to not less than one year (400.2-725). Check for a future-performance warranty exception in the same section.
9. **Excuse.** Commercial impracticability (400.2-615); casualty to identified goods (400.2-613).

## Output
- Path memo headings: Transaction and Scope / Warranties Created / Disclaimers and Limits / Acceptance-Rejection-Revocation Status / Notice Given / Remedies Available / Limitations Date
- Notice-of-breach or revocation letter draft (dated, specific defects, remedy demanded) - for the user to send
- Damages worksheet by Code section

## Pitfalls
- Continuing to use goods after rejection or revocation (can be treated as acceptance).
- No timely notice of breach under 400.2-607(3)(a) - an outright bar to recovery.
- Suing a non-merchant private seller for breach of merchantability.
- Missing the four-year limit because the defect was found late; accrual is at tender, not discovery.
- Ignoring a valid "as is" clause or a conspicuous disclaimer, or failing to argue failure of essential purpose.

## Verify before relying
- Pull verbatim text of each RSMo 400.2- section cited (Missouri numbering mirrors the uniform text but confirm Missouri variations) via `statute-lookup` or Descrybe `search_laws_and_rules`; pull 15 U.S.C. 2308 and 2310 for Magnuson-Moss.
- Check any case relied on for "reasonable time" or merchant status is still good law (CourtListener / Descrybe).
- Recompute the 400.2-725 date from actual tender of delivery.
- Legal information, not legal advice; recommend counsel or legal aid for high-stakes decisions.

## Related skills
- `contract-breach-analyzer` - non-goods contract claims and common-law defenses
- `mo-merchandising-practices-act` - deceptive sales practices in the same transaction
- `ucc-article-9-secured-transactions` - financed goods, repossession
- `damages-calculator` - compute cover, market, and incidental figures
- `settlement-and-demand-letters` - demand before suit
