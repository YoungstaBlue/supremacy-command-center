---
name: mo-evidence-rules
description: Explains Missouri evidence law (common law plus RSMo chapters 490 and 491) and how it differs from the Federal Rules of Evidence. Use for "Missouri rules of evidence", "is this admissible in Missouri court", business records affidavit, RSMo 490.692, or comparing MO and FRE.
---

# Missouri Evidence Rules

Missouri has no comprehensive evidence code. Admissibility in Missouri state court comes from case law plus
scattered statutes (mainly RSMo chapters 490 and 491, with some in chapters 546 and others). This skill maps
a question to the right Missouri source and flags where it departs from the FRE.

## When to use
- "Is this admissible in Missouri?" or "what rule of evidence applies in circuit court?"
- Preparing evidence for a Missouri trial, hearing, or summary judgment record
- Translating an FRE-based argument into Missouri terms
- Not for: federal court evidence questions (use `hearsay-analyzer`, `authentication-foundation-builder`, which cover FRE)

## Gather first
- Court: Missouri circuit/associate circuit (civil or criminal) or federal court. In federal court the FRE apply,
  except state privilege law governs state-law claims (FRE 501).
- The item of evidence and what it is offered to prove
- Whether the case is jury or bench tried (bench trials get more latitude; judges are presumed to disregard improper evidence)

## Workflow
1. Confirm forum. If federal, stop and apply FRE; note FRE 501 and 601 defer to state law on privilege and
   competency for state-law claims in diversity/supplemental cases.
2. Relevance: Missouri tests logical relevance (tends to make a fact more or less probable) and legal relevance
   (probative value outweighs unfair prejudice, confusion, cumulativeness). Both are common law, not a numbered rule.
3. Identify the governing source by topic:
   - Expert testimony: RSMo 490.065 (amended 2017 to track FRE 702-705 for most cases; certain case types keep
     the older standard; read the current subsections). See `expert-witness-challenge`.
   - Business records: RSMo 490.680 (Uniform Business Records as Evidence Law) and 490.692 (records by affidavit,
     with advance service on other parties before trial; check the notice period in the current text).
   - Impeachment by prior conviction: RSMo 491.050. See `impeachment-and-credibility`.
   - Prior inconsistent statements as substantive evidence: RSMo 491.074 (criminal cases); civil cases follow
     Rowe v. Farmers Ins. Co., 699 S.W.2d 423 (Mo. banc 1985).
   - Child victim statements: RSMo 491.075 (criminal; notice and hearing on reliability required).
   - Competency and certain privileges: RSMo 491.060 (attorney, physician, clergy, and others). Spousal
     privilege in criminal cases: RSMo 546.260. See `privilege-analyzer`.
   - Hearsay exceptions, authentication, best evidence, character evidence: Missouri common law (case law).
4. Compare with the FRE equivalent and note the difference explicitly (table below).
5. Plan the record: offer, objection, ruling, and offer of proof if excluded. See `objection-playbook`.

## Key Missouri vs. FRE differences (verify each against current law)
| Topic | Missouri | FRE |
|---|---|---|
| Source | Case law + statutes | Codified rules |
| Conviction impeachment | Any prior conviction, misdemeanor included, generally no balancing (491.050) | FRE 609 balancing, felony or dishonesty crimes, 10-year limit |
| Prior inconsistent statements | Substantive evidence (491.074 criminal; Rowe civil) | Substantive only if under oath at prior proceeding (801(d)(1)(A)) |
| Expert standard | 490.065 (2017 amendment modeled on FRE 702, with carve-outs) | FRE 702 / Daubert |
| Motion in limine | Preserves nothing; must object at trial | Definitive pretrial ruling can preserve (FRE 103(b)) |
| Post-trial preservation | Jury-tried civil: allegations of error must be in motion for new trial (Rule 78.07); criminal: Rule 29.11(d) | No new-trial motion required to preserve for appeal |
| Residual hearsay | No general catch-all | FRE 807 |

## Output
- Short memo: Question / Forum / Governing Missouri source / Rule statement / FRE comparison / Application /
  Foundation or objection needed / Open verification items

## Pitfalls
- Citing FRE numbers in a Missouri state brief as if binding. They are at most persuasive.
- Relying on a motion in limine ruling without a timely trial objection (Missouri treats in limine rulings as interlocutory).
- Failing to make an offer of proof when evidence is excluded; without it, the exclusion is usually unreviewable.
- Missing the advance-service requirement for a 490.692 business records affidavit.
- Treating a suspended imposition of sentence (SIS) as a "conviction" for 491.050 impeachment; Missouri case law
  generally holds it is not. Verify current authority.

## Verify before relying
- Pull verbatim text of RSMo 490.065, 490.680, 490.692, 491.050, 491.060, 491.074, 491.075, 546.260 and
  Rules 78.07 / 29.11 via `statute-lookup`.
- Check Rowe and any other case for subsequent treatment on CourtListener before citing.
- Legal information, not legal advice; consult counsel or legal aid for high-stakes decisions.

## Related skills
- `hearsay-analyzer` — detailed hearsay exceptions, FRE and MO
- `authentication-foundation-builder` — foundation scripts for exhibits
- `objection-playbook` — making and preserving objections
- `statute-lookup` — verbatim RSMo text
- `lawmind-legal-research` — grounded research in the user's library
