---
name: mo-wills-trusts-probate
description: Guides Missouri wills, trusts, powers of attorney, beneficiary deeds, intestacy, small estate affidavits (RSMo 473.097), and probate deadlines - presentment, creditor claims, will contests. Use for "probate", "small estate affidavit", "will", "trust", "power of attorney", or "contest a will".
---

# Missouri Wills, Trusts, and Probate

Checks Missouri execution formalities for estate documents and walks an estate through the correct probate path with its hard deadlines.

## When to use
- Drafting or reviewing a will, revocable trust, durable power of attorney, or beneficiary (transfer-on-death) deed
- A relative died: deciding between no probate, small estate affidavit, or full administration
- Creditor claims, will contests, spousal elective share, and family allowances
- Not for: divorce property division (use `mo-family-law-dissolution-custody`); wrongful death claims arising from the death (use `wrongful-death-and-survival-mo`)

## Gather first
- Date of death, county of domicile, and whether an original will exists and where
- Inventory of assets with how each is titled (sole name, joint, beneficiary designation, TOD/POD, trust) and approximate values, liens, and debts
- Surviving spouse and descendants (and their ages), and any notice of letters already published

## Workflow
1. **Execution formalities.**
   - Will: in writing, signed by the testator (or by another at the testator's direction and in the testator's presence), attested by two or more competent witnesses subscribing in the testator's presence (RSMo 474.320). Self-proving by acknowledgment of testator and witnesses before an officer authorized to administer oaths, with the officer's certificate (RSMo 474.337).
   - Durable power of attorney: in writing, containing statutory durability language in substance, subscribed, dated, and acknowledged like a real-estate conveyance (RSMo 404.705). General powers: RSMo 404.710. Health-care decisions require the separate durable power of attorney for health care provisions (verify sections in RSMo ch. 404).
   - Trusts: Missouri Uniform Trust Code, RSMo 456.1-101 et seq.
   - Beneficiary deed: conveys real property effective on the owner's death if executed and recorded with the recorder of deeds before death (RSMo 461.025).
2. **Sort probate vs. nonprobate assets.** Joint-with-survivorship, beneficiary-designated, TOD/POD, beneficiary-deeded, and trust assets pass outside probate (Nonprobate Transfers Law, RSMo ch. 461). Only the remainder needs a probate path.
3. **Small estate (RSMo 473.097).** Available if the entire estate, less liens, debts, and encumbrances, does not exceed $40,000; 30 days have passed since death; no application for letters is pending or granted; and a bond approved by the probate judge or clerk, in at least the value of the personal property, is filed (check the statute for any current exception). Read the statute for affidavit contents, publication, and the bond rule before filing.
4. **Will presentment (RSMo 473.050).** A will must be presented to and admitted to probate to be effective. Deadline: within six months after first publication of notice of letters (or 30 days after a will contest is commenced, if later); if no notice of letters was given, within one year after death. A will not presented in time is forever barred. Letters of administration generally must be applied for within one year after death.
5. **Creditor claims (RSMo 473.360).** Claims not filed within six months after first publication of notice of letters - or within two months after notice was mailed or served on a creditor, whichever is later - are forever barred, subject to the statute's exceptions. Separate one-year-from-death outside bar (RSMo 473.444 - verify text).
6. **Will contest (RSMo 473.083).** A petition contesting a probated will, or seeking probate of a rejected will, must be filed within six months after probate or rejection or after first publication of notice of letters, whichever is later. Grounds: lack of capacity, undue influence, improper execution, revocation, fraud. Check for a no-contest clause and the safe-harbor petition procedure (RSMo 474.395).
7. **Intestacy (RSMo 474.010).** Spouse's share depends on whether the decedent left descendants and whether they are also the spouse's descendants; then descendants, parents, siblings, and further kin per the statute.
8. **Spousal and family protections.** Elective share against the will: one-half if no lineal descendants, one-third if there are lineal descendants, subject to claims (RSMo 474.160 - check election deadline in related sections). Exempt property (474.250), one-year support allowance (474.260), homestead allowance (474.290).

## Output
- Asset map: | Asset | Title / designation | Probate or nonprobate | Value | Passes to |
- Path decision: no probate / small estate affidavit / full administration, with the controlling statute and reasons
- Deadline calendar: date of death, 30-day small-estate date, publication date, six-month claim and presentment dates, one-year dates
- Execution checklist for any document drafted (signatures, witnesses, notary, required statutory language)

## Pitfalls
- Holding the original will instead of delivering it to the probate division promptly.
- Using a small estate affidavit when nonprobate-excluded assets push the probate estate over the limit, or skipping the bond.
- Missing the six-month claim or will-contest window - these are hard bars.
- A power of attorney without the durability language or acknowledgment, which ends at incapacity.
- Recording a beneficiary deed after death (too late).
- Paying estate debts out of order or distributing before the claim period closes, creating personal liability for the representative.

## Verify before relying
- Pull verbatim text of RSMo 404.705, 404.710, 456.1-101, 461.025, 473.050, 473.083, 473.097, 473.360, 473.444, 474.010, 474.160, 474.250, 474.260, 474.290, 474.320, 474.337, 474.395 via `statute-lookup` or Descrybe `search_laws_and_rules`.
- Check any probate case relied on for current treatment (CourtListener / Descrybe); use the probate division's current forms.
- Recompute every deadline from the actual death and publication dates.
- Legal information, not legal advice; estate planning and contested estates warrant counsel or legal aid.

## Related skills
- `contract-breach-analyzer` - claims by or against the estate on contracts
- `mo-declaratory-judgment` - construing a will or trust provision
- `wrongful-death-and-survival-mo` - survival claims belonging to the estate
- `mo-deadline-calculator` - probate deadline math
- `lawmind-god-drafter` - estate document packages
