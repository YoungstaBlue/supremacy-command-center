---
name: malicious-prosecution-false-arrest
description: Builds or tests false arrest, false imprisonment, and malicious prosecution claims after criminal charges - Missouri torts and 1983 Fourth Amendment claims - with probable cause, favorable termination, Heck, accrual, and limitations. Use for "false arrest", "charges dropped", "malicious prosecution".
---

# Malicious Prosecution and False Arrest

Sorts an unlawful-arrest or baseless-charge grievance into the right claims (state tort vs. federal 1983, arrest vs. prosecution), tests each against probable cause, and fixes the accrual date and deadline.

## When to use
- Arrested without a warrant or probable cause, or held without legal authority.
- Criminal charges were dismissed, nolle prossed, or ended in acquittal and the person wants to sue.
- A defendant (police, complainant, store) is raising probable cause or immunity against such a claim.
- Not for: civil suits brought to harass (malicious civil prosecution, abuse of process) - use `abuse-of-process-and-civil-conspiracy`; pending criminal cases (use `fourth-amendment-analyzer` and `mo-motion-to-suppress` first).

## Gather first
- Arrest date, whether by warrant, who instigated (officer, private complainant), what the arresting officer knew, and the charge.
- How and when the criminal case ended (certified docket or judgment): dismissal type, acquittal, plea, diversion, SIS.
- Evidence of falsity or malice: reports, body-cam, witness statements, the complainant's statements to police.

## Workflow
1. **Separate the claims by stage.**
   - False arrest / false imprisonment: detention without legal justification, up to the point of legal process (arraignment, warrant, probable cause determination).
   - Malicious prosecution: detention or prosecution pursuant to legal process that lacked probable cause.
   - Fabricated evidence: due process claim where false evidence was used to deprive liberty.
2. **Missouri false arrest / false imprisonment.** Elements: the plaintiff was confined or restrained against their will, and the confinement was unlawful (without legal justification). Defendants who instigated or encouraged the arrest can be liable, not just officers. Probable cause or a facially valid warrant is a justification; verify current Missouri formulation with `lawmind-legal-research`.
3. **Missouri malicious prosecution.** Missouri disfavors the tort and requires strict compliance with its elements (Sanders v. Daniel International Corp., 682 S.W.2d 803 (Mo. banc 1984)): (1) commencement or prosecution of the proceedings against plaintiff; (2) defendant instigated it; (3) termination in plaintiff's favor; (4) absence of probable cause; (5) malice; (6) damages. Probable cause is judged by what defendant reasonably believed at the time; malice may be inferred from lack of probable cause in criminal-based claims but proof of each element is required. A full and fair disclosure of facts to a prosecutor who independently decides to charge is a common defense. Missouri courts look at how the case ended - a dismissal that reflects a compromise or does not reach the merits may not satisfy favorable termination; research current Missouri law on nolle prosequi and dismissals.
4. **1983 Fourth Amendment claims.**
   - False arrest: lack of probable cause for any offense, not just the one charged (Devenpeck v. Alford, 543 U.S. 146 (2004)); probable cause is a practical, totality assessment (District of Columbia v. Wesby, 583 U.S. 48 (2018)); arrests for minor fine-only offenses are permitted if probable cause exists (Atwater v. City of Lago Vista, 532 U.S. 318 (2001)).
   - Pretrial detention after legal process without probable cause violates the Fourth Amendment (Manuel v. City of Joliet, 580 U.S. 357 (2017)).
   - Malicious prosecution under 1983: favorable termination requires only that the prosecution ended without a conviction, not an affirmative indication of innocence (Thompson v. Clark, 596 U.S. 36 (2022)). A valid charge does not insulate a baseless one brought alongside it (Chiaverini v. City of Napoleon, 602 U.S. 556 (2024)).
   - Individual defendants will raise qualified immunity ("arguable probable cause"); municipalities require Monell policy or custom.
5. **Heck bar.** A 1983 claim that would necessarily imply the invalidity of an outstanding conviction or sentence is barred until it is reversed, expunged, or otherwise invalidated (Heck v. Humphrey, 512 U.S. 477 (1994)). Guilty pleas and convictions on related counts are common traps; SIS dispositions require careful research.
6. **Accrual and limitations.**
   - 1983 false arrest accrues when the detention becomes pursuant to legal process, e.g., arraignment - not when charges are dropped (Wallace v. Kato, 549 U.S. 384 (2007)).
   - 1983 malicious prosecution and fabricated-evidence claims accrue at favorable termination (McDonough v. Smith, 588 U.S. 109 (2019)).
   - 1983 borrows Missouri's general personal-injury period (five years under RSMo 516.120 - verify).
   - Missouri tort: false imprisonment is a two-year claim under RSMo 516.140; verify via `statute-lookup` which RSMo ch. 516 period governs malicious prosecution before relying on a longer one.
   - Claims against public entities face sovereign immunity (RSMo 537.600) and officers raise official immunity - see related skills.
7. **Damages.** Loss of liberty, emotional distress, reputation, lost wages, defense attorney fees and bond costs; punitive damages require proof under Missouri's punitive-damages statutes (RSMo 510.261 et seq.).

## Output
- Claim matrix: | Claim | Forum/vehicle | Defendant | Elements met? | Probable cause analysis | Accrual date | Deadline | Barriers (Heck, immunity) |
- Probable-cause worksheet: facts known to the officer/complainant at the moment of arrest or charge, offense by offense.
- Petition/complaint headings per count, with favorable-termination proof attached (certified docket).

## Pitfalls
- Counting the false-arrest deadline from dismissal instead of arraignment.
- Suing on a 1983 theory while a conviction on related conduct stands (Heck).
- Ignoring probable cause for an uncharged or lesser offense.
- Assuming any dismissal is a favorable termination under Missouri tort law.
- Naming only the city without facts showing a policy, or only officers without addressing immunity.

## Verify before relying
- Pull verbatim RSMo 516.120, 516.140, 537.600, and 510.261 et seq. via `statute-lookup` (or Descrybe `search_laws_and_rules`).
- Confirm Sanders and each federal case remain good law; find current Missouri appellate cases on false arrest elements and favorable termination (CourtListener / Descrybe).
- Recompute every deadline from the certified arraignment and termination dates.
- Legal information, not legal advice; civil-rights counsel often take these cases on contingency.

## Related skills
- `section-1983-claim-builder` / `qualified-immunity-analyzer` - federal vehicle and defense.
- `fourth-amendment-analyzer` - seizure and probable cause doctrine.
- `abuse-of-process-and-civil-conspiracy` - civil-proceeding counterparts.
- `sovereign-and-official-immunity-mo` / `statute-of-limitations-checker` - state-law barriers and deadlines.
- `damages-calculator` - quantifying the claim.
