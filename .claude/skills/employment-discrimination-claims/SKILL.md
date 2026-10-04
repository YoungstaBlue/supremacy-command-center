---
name: employment-discrimination-claims
description: Plans employment discrimination, harassment, and retaliation claims under the Missouri Human Rights Act (RSMo 213) and Title VII/ADA/ADEA - charge deadlines, MCHR/EEOC dual filing, right-to-sue timing, proof frameworks. Use for "fired because of", "EEOC charge", "MCHR", "right to sue", or "hostile work environment".
---

# Employment Discrimination Claims

Protects the claim first (charge deadlines are the most common way these cases die), then frames it under the correct statute and proof framework.

## When to use
- Termination, demotion, discipline, pay, or failure to hire/promote believed tied to race, color, religion, national origin, sex, ancestry, age, disability, or pregnancy
- Harassment / hostile work environment, or retaliation for complaining or participating in an investigation
- Received an EEOC or MCHR right-to-sue letter, or the employer responded to a charge
- Not for: wage-and-hour, whistleblower, or workers' compensation retaliation claims (different statutes); public-employee First Amendment retaliation (use `first-amendment-analyzer`)

## Gather first
- Date of each adverse act (termination date, demotion date, last harassing incident) and whether any charge was filed and when
- Employer size (number of employees) and whether public or private
- Protected trait, any complaint made to the employer (date, to whom, written?), and comparators treated better

## Workflow
1. **Run the clock immediately.**
   - MHRA: file a verified complaint with the Missouri Commission on Human Rights (MCHR) within 180 days of the alleged act (RSMo 213.075).
   - Title VII / ADA: file an EEOC charge within 180 days, extended to 300 days where a state agency (like MCHR) exists (42 U.S.C. 2000e-5(e)(1)). Missouri is a deferral state, so 300 days generally applies to federal claims — but the 180-day MHRA deadline is shorter. Target 180 days.
   - Dual filing: a charge filed with one agency is ordinarily cross-filed with the other under the worksharing agreement; confirm on the intake form.
   - Each discrete act (termination, failure to promote) starts its own clock; a hostile-environment claim is timely if one contributing act falls in the window (National R.R. Passenger Corp. v. Morgan, 536 U.S. 101 (2002)).
2. **Coverage.** MHRA employer: 6 or more employees in Missouri (RSMo 213.010 — verify). Title VII and ADA: 15 or more (42 U.S.C. 2000e(b)). ADEA: 20 or more, age 40+. Individual supervisors are not personally liable under Title VII; the 2017 MHRA amendments also excluded individual employees from the employer definition (verify current 213.010).
3. **Right to sue.**
   - MHRA: may request a right-to-sue letter after 180 days from filing; suit must be filed within 90 days of the letter and no later than two years after the alleged violation (RSMo 213.111 — verify).
   - Title VII/ADA: suit within 90 days of receiving the EEOC notice of right to sue (42 U.S.C. 2000e-5(f)(1)). Calendar from actual receipt; keep the envelope/email.
   - ADEA: may sue 60 days after filing the charge without a right-to-sue letter; 90-day window after notice of dismissal still applies.
   - The charge-filing requirement is a mandatory claim-processing rule, not jurisdictional, so it is forfeited if the employer does not raise it timely (Fort Bend County v. Davis (U.S. 2019)).
4. **Causation standard.** MHRA as amended in 2017 requires the protected trait to be the motivating factor ("because of"), a stricter standard than before (verify current 213.010 definition). Title VII status claims allow "motivating factor" (42 U.S.C. 2000e-2(m)); Title VII retaliation and ADEA require but-for causation.
5. **Choose the proof framework.**
   - Direct evidence (statements tying the decision to the trait), or
   - McDonnell Douglas Corp. v. Green, 411 U.S. 792 (1973): (a) protected class; (b) qualified / meeting legitimate expectations; (c) adverse action; (d) circumstances suggesting discrimination (e.g., similarly situated comparator outside the class treated better). Employer articulates a legitimate reason; plaintiff shows pretext.
   - Adverse action for discriminatory transfers requires only "some harm" to a term or condition of employment (Muldrow v. City of St. Louis (U.S. 2024) — verify reporter cite).
   - Retaliation: protected activity, materially adverse action that might dissuade a reasonable worker (Burlington N. & Santa Fe Ry. v. White, 548 U.S. 53 (2006)), causal link (timing plus other evidence).
   - Hostile environment: unwelcome conduct based on the trait, severe or pervasive enough to alter conditions; employer liability rules differ for supervisor vs. coworker harassment (Faragher/Ellerth defense for supervisors without a tangible action).
6. **Parallel and alternative claims.** 42 U.S.C. 1981 (race; no charge requirement, longer limitations period); 1983 for public employers; ADA failure to accommodate (interactive process).
7. **Damages map.** Back pay, front pay, compensatory and punitive damages subject to caps scaled by employer size (Title VII: 42 U.S.C. 1981a(b)(3); MHRA has its own caps added in 2017 — verify 213.111). Duty to mitigate by seeking comparable work.

## Output
- Deadline card: act date | MHRA 180-day date | EEOC 300-day date | charge filed | RTS received | 90-day suit date | MHRA two-year outside date
- Charge narrative draft (who, what, when, protected trait, comparators, complaint history), each act dated separately
- Elements-to-evidence table for each claim

## Pitfalls
- Waiting for the federal 300 days and losing the MHRA claim at 180
- Leaving acts or theories (e.g., retaliation) out of the charge; suit scope is limited to the charge and what reasonably grows from it — amend the charge if new retaliation occurs
- Missing the 90-day suit window after a right-to-sue notice
- Naming only individuals, or suing under Title VII an employer with under 15 employees
- Signing a severance release without reading the waiver (ADEA waivers have special requirements)

## Verify before relying
- Pull verbatim RSMo 213.010, 213.055, 213.070, 213.075, 213.111 and 42 U.S.C. 2000e-5 via `statute-lookup` (or Descrybe `search_laws_and_rules`); confirm cases are good law.
- Recompute every deadline from the actual act date and actual receipt of notices.
- Legal information, not legal advice; many employment lawyers take cases on contingency — consult one early.

## Related skills
- `statute-of-limitations-checker` — 1981/1983 alternatives
- `elements-checklist-builder` — map evidence to McDonnell Douglas steps
- `damages-calculator` — back pay and caps
- `settlement-and-demand-letters` — severance and settlement negotiation
