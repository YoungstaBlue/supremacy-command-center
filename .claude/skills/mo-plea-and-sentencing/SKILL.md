---
name: mo-plea-and-sentencing
description: Evaluates Missouri plea offers and sentencing - Rule 24.02 colloquy and plea agreement types, SIS vs SES (RSMo 557.011), sentencing assessment reports, probation terms, and 120-day programs. Use for "plea deal", "SIS", "SES", "probation", "sentencing hearing", or "should I plead guilty".
---

# Missouri Plea and Sentencing

Breaks down a plea offer, the guilty plea procedure, and the sentencing dispositions available in Missouri so the defendant understands exactly what is being given up and what can result.

## When to use
- The state made a plea offer, or the defendant is considering an open plea
- "What is an SIS?", "will this be on my record?", "can I withdraw my plea?", "what happens at sentencing?", "probation terms"
- Preparing a sentencing memorandum or reviewing a sentencing assessment report
- Not for: attacking a plea after sentencing (use `mo-post-conviction-relief`); municipal tickets (use `mo-municipal-ordinance-defense`)

## Gather first
- The written offer: charges pleaded to, charges dismissed, recommended disposition, and whether it is a recommendation or a binding specific sentence
- Charge classes, range of punishment, any mandatory minimum or enhancement, and prior record
- Collateral concerns: immigration status, professional licenses, driver's license, firearms, housing, sex-offender registration

## Workflow
1. **Classify the agreement under Rule 24.02(d)(1):** (A) dismiss other charges; (B) a non-binding recommendation or agreement not to oppose; (C) an agreed specific sentence; (D) other disposition. Critical difference: if a (B) recommendation is not followed, the plea cannot be withdrawn (Rule 24.02(d)(2)); if the court rejects an (A), (C), or (D) agreement, the defendant must be offered the chance to withdraw (Rule 24.02(d)(4)).
2. **Know the colloquy (Rule 24.02(b)-(c), (e)).** The court must personally advise of the nature of the charge, mandatory minimum and maximum penalty, right to counsel, right to plead not guilty and to a jury trial with confrontation and no self-incrimination, and that a guilty plea waives trial; it must find the plea voluntary and a factual basis exists. The plea must be knowing and voluntary (Boykin v. Alabama, 395 U.S. 238 (1969)). Answers given under oath at the plea will be used against any later claim - answer truthfully, and raise any misunderstanding before the plea is accepted.
3. **Plea negotiations are inadmissible** against the defendant, with a perjury exception (Rule 24.02(d)(5)). The state must keep its promises (Santobello v. New York, 404 U.S. 257 (1971)).
4. **Compare dispositions (RSMo 557.011.2):** prison or jail (chapter 558); fine (chapter 560); suspended imposition of sentence (SIS) with or without probation; suspended execution of sentence (SES) with probation; detention as a probation condition (559.026). An SIS is not a conviction for most purposes and records close when the case terminates (RSMo 610.105); a probation violation can lead to any sentence in the full range. An SES is a conviction; violation means the pronounced sentence is executed.
5. **Probation terms (RSMo 559.016.1):** felony 1-5 years; misdemeanor 6 months-2 years; infraction 6 months-1 year.
6. **Sentencing assessment report (RSMo 557.026):** required in felony cases unless the defendant waives it; for class A misdemeanors only if the court directs. The defendant is entitled to see the complete report before sentencing. Review it line by line and file written corrections.
7. **120-day options (RSMo 559.115):** the court may grant probation within 120 days of delivery to DOC on its own motion, and may place the offender in a 120-day treatment or structured program, with a release recommendation process. Ask whether the plea contemplates this.
8. **Counsel duties.** Counsel must communicate formal offers (Missouri v. Frye, 566 U.S. 134 (2012)) and advise of clear immigration consequences (Padilla v. Kentucky, 559 U.S. 356 (2010)).
9. **Sentencing presentation.** Mitigation evidence, letters, treatment records, employment, restitution plan; written allocution; requested disposition with reasons.

## Output
- **Offer analysis table:** | Item | Offer | If convicted at trial (range) | Notes |
- Plain-language explanation of SIS vs. SES vs. prison for this offer
- Plea-day checklist of the Rule 24.02 advisements with a column for "understood / question"
- **Sentencing memorandum** headings: Background; Offense; Report Corrections; Mitigation; Requested Disposition; Conditions Proposed

## Pitfalls
- Treating a (B) recommendation as a guarantee - the judge can exceed it and the plea stands.
- Saying "yes" at the colloquy to things not understood; those answers defeat later claims.
- Ignoring collateral consequences (immigration, licenses, registration) until after the plea.
- Assuming an SIS erases everything - it remains visible to some agencies and a violation exposes the full range.
- Waiving the sentencing assessment report without weighing whether it would help.

- Not asking whether the plea preserves any issue for appeal; a guilty plea generally waives non-jurisdictional defects.
- Overlooking restitution, costs, and fees that can block later expungement until paid.
- Not reading every probation condition before the plea; violation exposes the defendant to the full range under an SIS.
- Skipping written corrections to the sentencing assessment report before the hearing.
- Missing the chance to ask for a 559.115 program or an SIS when the record supports it.
- Accepting an offer without knowing the parole-eligibility consequences of the conviction class.

## Verify before relying
- Pull current Rule 24.02 and RSMo 557.011, 557.026, 559.016, 559.115, 610.105 text via `statute-lookup` or Descrybe `search_laws_and_rules`; confirm ranges of punishment in chapters 558 and 560 for the charged class.
- Check cited cases for treatment (CourtListener / Descrybe).
- Legal information, not legal advice; a plea decision is high stakes - consult counsel or the public defender.

## Related skills
- `mo-post-conviction-relief` - challenging the plea later (Rule 24.035)
- `mo-expungement` - future record relief
- `mo-criminal-case-roadmap` - where the plea fits
- `lawmind-strategy-engine` - weigh the offer against trial risk
