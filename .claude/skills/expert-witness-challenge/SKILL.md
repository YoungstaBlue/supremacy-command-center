---
name: expert-witness-challenge
description: Builds or defends challenges to expert testimony under FRE 702 and Daubert and Missouri RSMo 490.065 - qualifications, reliability, fit, and disclosure. Use for "Daubert motion", "exclude their expert", "motion to strike expert", "is my expert qualified", 490.065, or cross-examining an expert.
---

# Expert Witness Challenge

Tests an expert opinion against the admissibility standard and builds a motion to exclude (or a response),
plus a cross-examination plan when exclusion is unlikely.

## When to use
- Opposing party disclosed an expert (medical, accident reconstruction, forensic, damages, police practices)
- You need to confirm your own expert will survive a challenge
- A lay witness is drifting into opinion that requires expertise
- Not for: general witness outlines (use `witness-examination-planner`)

## Gather first
- Expert disclosure/report, CV, materials relied on, deposition if taken, and the specific opinions offered
- Forum and case type (Missouri RSMo 490.065 has different subsections for different case types)
- Scheduling order deadlines for expert disclosures and Daubert/exclusion motions

## Workflow
1. Identify each opinion separately. Challenge opinion by opinion, not the expert as a whole.
2. State the standard:
   - Federal: FRE 702 (as amended effective Dec. 1, 2023, the proponent must show it is more likely than not that)
     (a) specialized knowledge will help the trier of fact; (b) testimony rests on sufficient facts or data;
     (c) it is the product of reliable principles and methods; (d) the opinion reflects a reliable application of
     those methods to the facts. Daubert v. Merrell Dow Pharmaceuticals, Inc., 509 U.S. 579 (1993) (judge as
     gatekeeper; factors: testability, peer review, error rate, standards, general acceptance); Kumho Tire Co. v.
     Carmichael, 526 U.S. 137 (1999) (applies to all expert testimony, not only scientific); General Electric Co.
     v. Joiner, 522 U.S. 136 (1997) (abuse-of-discretion review; court may exclude where there is too great an
     analytical gap between data and opinion).
   - Missouri: RSMo 490.065, amended in 2017 to adopt language modeled on FRE 702-705 for most civil and criminal
     cases; a separate subsection preserves the older standard for certain case types (read the current text to
     see which). Missouri courts look to federal Daubert case law as persuasive when applying the amended statute.
3. Qualifications: knowledge, skill, experience, training, or education in the specific area of the opinion. A
   general credential does not qualify an expert in every subfield.
4. Reliability: method, data, error rate, whether the expert followed their own field's standards, whether the
   opinion was developed for litigation, whether alternative explanations were ruled out.
5. Fit/helpfulness: does the opinion address a fact in issue, and is it beyond common knowledge? Experts may not
   offer legal conclusions or tell the jury what result to reach; FRE 704(b) bars opinions on a criminal
   defendant's mental state constituting an element.
6. Basis: FRE 703 permits reliance on inadmissible facts if experts in the field reasonably rely on them, but the
   underlying facts are not automatically admissible. Missouri's 490.065 contains parallel basis provisions.
7. Disclosure: check compliance with FRCP 26(a)(2) (written report for retained experts; default timing 90 days
   before trial absent an order) or Missouri Rule 56.01(b)(4) and any court order. Nondisclosure can itself support
   exclusion (FRCP 37(c)(1)).
8. Decide: motion to exclude (all or part), request for a hearing, or cross-examination plus contrary evidence.

## Output
- Opinion table: Opinion / Basis stated / Qualification problem / Reliability problem / Fit problem / Disclosure problem / Remedy sought
- Motion skeleton: Introduction; Opinions challenged; Legal standard (702/Daubert or 490.065); Argument by opinion;
  Request for hearing; Relief (exclude or limit)
- Cross outline: concessions to obtain (no testing, assumptions, fees, prior inconsistent opinions, missing data)

## Pitfalls
- Filing after the scheduling-order deadline; untimely challenges are often denied outright.
- Attacking the conclusion instead of the method; courts review methodology and application, not correctness.
- Missing that the proponent bears the burden on admissibility (by a preponderance) in federal court.
- Failing to object at trial when the pretrial challenge was denied in Missouri state court (in limine rulings preserve nothing there).
- Using the wrong 490.065 subsection for the case type.

## Verify before relying
- Pull current text of RSMo 490.065, FRE 702-705, FRCP 26(a)(2), and Missouri Rule 56.01 via `statute-lookup`.
- Check recent 8th Circuit and Missouri appellate treatment of the 2023 FRE 702 amendment and amended 490.065 on CourtListener.
- Recompute disclosure/motion deadlines from the scheduling order.
- Legal information, not legal advice.

## Related skills
- `witness-examination-planner` — cross-examination structure
- `impeachment-and-credibility` — bias and prior statements of the expert
- `mo-evidence-rules` — Missouri source map
- `federal-summary-judgment` — excluded expert often means no triable issue
- `lawmind-strategy-engine` — stress-test whether to challenge or cross
