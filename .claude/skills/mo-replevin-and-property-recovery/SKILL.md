---
name: mo-replevin-and-property-recovery
description: Plans recovery of wrongfully held personal property in Missouri - demand letters, replevin under Rule 99 and RSMo ch. 533, conversion damages, police-held property, and bond requirements. Use for "replevin", "get my property back", "they won't return my stuff", "car being held", "conversion", or "seized property".
---

# Missouri Replevin and Property Recovery

Choose the fastest lawful route to get specific personal property back (or its value) and draft the papers for it.

## When to use
- Someone (ex-partner, landlord, business, tow lot, pawn shop, government agency) holds the user's personal property and refuses to return it.
- The user wants the item itself back, not just money.
- The user is defending a replevin action.
- Not for: real property possession - use `mo-landlord-tenant-eviction`; repossession of collateral by a secured creditor - use `ucc-article-9-secured-transactions`; criminal forfeiture - research the forfeiture statute separately.

## Gather first
- Description of each item (serial/VIN, photos), its approximate value, and proof of ownership or right to possession (title, receipts, bank records).
- Who holds it, where, since when, and how the holder got it.
- Any demand made and the response (dates, texts, letters).

## Workflow
1. Identify the right remedy:
   - Replevin: recovers specific property; plaintiff must show a right to immediate possession and wrongful detention. Governed by Supreme Court Rule 99 and RSMo ch. 533.
   - Conversion (tort): damages for the value of property wrongfully taken or withheld; elements generally are ownership/right to possession, defendant's unauthorized exercise of control, and demand/refusal where possession was originally lawful. See `intentional-torts`.
   - Property held by police or a prosecutor as evidence: start with a written request to the agency and, if criminal charges exist, a motion for return of property in that criminal case; identify the statutory procedure for the particular seizure.
2. Make a written demand first. A clear demand and refusal establishes wrongful detention and supports conversion. Include item list, basis of ownership, deadline, and a pickup method. Keep proof of delivery.
3. Pick the court. Associate circuit divisions commonly hear replevin; check the amount-in-controversy and local practice. Verify whether small claims can order return of property or only money - do not assume.
4. Draft the petition with Rule 55 fact pleading: ownership/right to possession, description and value of each item, wrongful detention, demand and refusal, damages for detention. Add a conversion count in the alternative.
5. Pre-judgment possession: Rule 99 provides for an order of delivery before judgment on an affidavit and a plaintiff's bond, with an opportunity for the defendant to be heard and to post a counter-bond to keep the property. Read the verbatim rule for the affidavit contents, hearing requirements, and bond amount before drafting.
6. Judgment: in replevin the judgment typically awards possession or, if the property cannot be delivered, its value, plus damages for wrongful detention. Ask for both in the alternative.
7. Enforcement: the sheriff executes the order/writ. Do not use self-help that breaches the peace; a "civil standby" by law enforcement may help for voluntary pickups.
8. Defending: challenge plaintiff's ownership or right to possession, assert a lien (e.g., repair, storage, or towing lien statutes), contest valuation, and seek damages on the bond if the order of delivery was wrongful.

## Output
- Remedy decision table: Route | Gets property back? | Speed | Bond needed | Fits facts?
- Demand letter draft: item list, ownership basis, deadline, pickup method, consequence (suit for replevin and conversion).
- Petition outline: Caption; Parties; Jurisdiction/Venue; Facts; Count I Replevin; Count II Conversion (alternative); Prayer (possession or value, detention damages, costs); Verification; affidavit for order of delivery if seeking pre-judgment possession.

## Pitfalls
- Suing without a documented demand where possession was initially lawful.
- Vague item descriptions the sheriff cannot identify.
- Overstating value (affects bond and credibility) or understating it (limits recovery).
- Self-help retrieval that leads to trespass, breach-of-peace, or criminal charges.
- Ignoring a holder's statutory lien that must be satisfied or contested.
- Waiting too long: conversion and replevin claims are subject to limitations periods - check with `statute-of-limitations-checker`.
- Not photographing or documenting the property's condition before and after recovery - damage claims need proof.
- Forgetting to name the actual possessor (e.g., the tow company, not the property owner who called the tow).

## Verify before relying
- Pull verbatim Rule 99 and RSMo ch. 533 (and any lien statute raised) via `statute-lookup`.
- Confirm conversion elements and any case cited are current on CourtListener.
- Confirm the court's jurisdictional limits with the clerk.
- Legal information, not legal advice; for high-value property or police-held evidence, consult counsel or legal aid.

## Related skills
- `intentional-torts` - conversion and trespass to chattels.
- `mo-small-claims-associate-circuit` - forum choice and procedure.
- `mo-petition-drafting` - fact-pleading the counts.
- `settlement-and-demand-letters` - polishing the demand.
- `lawmind-god-drafter` - bundles petition, affidavit, bond, and summons papers.
