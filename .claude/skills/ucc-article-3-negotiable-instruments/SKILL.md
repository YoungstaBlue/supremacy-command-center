---
name: ucc-article-3-negotiable-instruments
description: Analyzes promissory notes and checks under UCC Article 3 as enacted in Missouri (RSMo 400.3) - negotiability, indorsements, person entitled to enforce, holder in due course, defenses, limitations. Use for "promissory note", "holder in due course", "who owns my note", "lost note", or a suit on a note.
---

# UCC Article 3 Negotiable Instruments

Determines whether a writing is a negotiable instrument, who may enforce it, and which defenses survive against that person.

## When to use
- Being sued on a promissory note, or suing on one
- Challenging a debt buyer's or servicer's standing to enforce a note
- Checks: dishonor, stop payment, "paid in full" check used as accord and satisfaction
- Indorsement chains, allonges, lost or destroyed notes
- Not for: security interests in collateral (use `ucc-article-9-secured-transactions`); credit-card debt suits that are not on a note (use `fdcpa-fcra-consumer-defense`)

## Gather first
- A copy of the instrument, front and back, plus any allonge, and who has physical possession now
- The chain of transfers or assignments claimed by the party seeking to enforce
- Payment history, the default date, and any acceleration notice

## Workflow
1. **Negotiability test (RSMo 400.3-104).** Unconditional promise or order to pay a fixed amount of money, with or without interest; payable to bearer or to order; payable on demand or at a definite time; no other undertaking or instruction beyond those the section permits. If not negotiable, ordinary contract and assignment law governs, and holder-in-due-course protection is unavailable.
2. **Identify the parties.** Maker/drawer, payee, indorsers, accommodation parties (400.3-419), drawee bank.
3. **Transfer and negotiation.** Negotiation = transfer of possession plus any necessary indorsement (400.3-201). Special vs. blank indorsement (400.3-205); a blank-indorsed note is payable to bearer. Restrictive indorsements (400.3-206). Transfer without negotiation still vests the transferor's rights (400.3-203, "shelter").
4. **Person entitled to enforce (400.3-301).** (i) holder; (ii) nonholder in possession with rights of a holder (must prove the transfer chain); (iii) person not in possession entitled under 400.3-309 (lost, destroyed, stolen) or 400.3-418. Lost-instrument enforcement requires proof of terms and right to enforce, and the court may require protection for the obligor against double liability (400.3-309).
5. **Burden on signatures (400.3-308).** Authenticity of signatures is admitted unless specifically denied in the pleadings; once signatures are admitted, a plaintiff who produces the instrument is entitled to payment unless the defendant proves a defense. Deny specifically if genuinely disputed.
6. **Holder in due course (400.3-302).** Took the instrument for value, in good faith, without notice of overdue/dishonor, unauthorized signature or alteration, or any claim or defense; no apparent irregularity. Debt buyers who took with notice of default generally fail the "without notice that it is overdue" element.
7. **Defenses (400.3-305).**
   - Real defenses good even against an HDC: infancy, duress/incapacity/illegality that nullifies the obligation, fraud in the factum, discharge in insolvency proceedings.
   - Personal defenses and claims in recoupment: good against a non-HDC (failure of consideration, fraud in the inducement, breach of the underlying contract).
   - Consumer credit: if the instrument carries the FTC Holder Rule notice (16 C.F.R. 433.2), the holder is subject to all claims and defenses the consumer has against the seller; see 400.3-106(d) on the effect of that notice.
8. **Discharge and payment.** Payment to a person entitled to enforce discharges (400.3-602). Accord and satisfaction by "paid in full" check requires good faith tender, bona fide dispute, and a conspicuous full-satisfaction statement (400.3-311). Effect of taking an instrument on the underlying obligation (400.3-310).
9. **Indorser and drawer liability.** Indorser's obligation is conditioned on dishonor and, where required, notice of dishonor (400.3-415, 400.3-503). Check bounced-check civil penalty statutes separately (verify current RSMo section before citing).
10. **Limitations (400.3-118).** Missouri's version sets ten years after the stated or accelerated due date for a note payable at a definite time and displaces chapter 516 for that action; other subsections cover demand notes, drafts, and certified checks. Confirm the subsection that fits.

## Output
- Negotiability finding with each 400.3-104 element marked met/not met
- Standing table: | Transfer step | Date | Document proving it | Indorsement type | Gap |
- Defense table: | Defense | Real or personal | Good against this plaintiff? | Facts | Pleaded? |
- Draft answer paragraphs specifically denying signatures or standing where facts support it (user files)

## Pitfalls
- Admitting the signature by general denial and then trying to contest it at trial.
- Conceding the plaintiff's holder status without demanding the original note and the indorsement chain.
- Assuming every plaintiff is a holder in due course; most debt buyers are not.
- Ignoring the FTC Holder Rule notice in consumer financing paperwork.
- Using a 5-year chapter 516 period when 400.3-118 sets a different one.

## Verify before relying
- Pull verbatim text of RSMo 400.3-104, -118, -203, -205, -301, -302, -305, -308, -309, -311, -415 and 16 C.F.R. 433.2 via `statute-lookup` or Descrybe `search_laws_and_rules`.
- Check any Missouri case on standing to enforce a note is still good law (CourtListener / Descrybe).
- Recompute the 400.3-118 date from the actual due or acceleration date.
- Legal information, not legal advice; recommend counsel or legal aid for high-stakes decisions.

## Related skills
- `contract-breach-analyzer` - non-negotiable instruments and underlying contract claims
- `ucc-article-9-secured-transactions` - collateral securing the note
- `fdcpa-fcra-consumer-defense` - collector conduct in the same suit
- `mo-answer-affirmative-defenses` - plead denials and defenses correctly
