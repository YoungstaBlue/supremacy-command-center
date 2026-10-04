---
name: equal-protection-analyzer
description: Analyzes Equal Protection claims and defenses - classification, discriminatory intent, tiers of scrutiny, class-of-one claims, and selective enforcement or prosecution. Use for "equal protection", "treated differently", "singled out", "selective prosecution", "racial profiling", "class of one".
---

# Equal Protection Analyzer

Identifies the classification at issue, proves (or rebuts) intent, and applies the correct level of scrutiny - the three choices that decide almost every equal protection case.

## When to use
- A law, policy, or official treated the person differently from others similarly situated.
- Claims of selective enforcement (police, code enforcement, licensing) or selective prosecution.
- Challenging a statute or ordinance that classifies by race, sex, alienage, or another trait.
- Not for: claims about a hearing or fair process (use `due-process-analyzer`); jury-selection strikes are a specialized Batson issue (Batson v. Kentucky, 476 U.S. 79 (1986)).

## Gather first
- The specific differential treatment: who was treated worse, who was treated better, and how they compare.
- Identified comparators (names or descriptions, dates, conduct, outcome) - the claim usually turns on them.
- Evidence of motive: statements, statistics, departures from normal procedure, sequence of events, history.

## Workflow
1. **State action and classification.** Is there government action, and does it classify on its face, or is it neutral on its face but applied or adopted with discriminatory purpose?
2. **Intent is required for facially neutral actions.** Disparate impact alone is not enough (Washington v. Davis, 426 U.S. 229 (1976)). Purpose means action "because of," not merely "in spite of," its effects (Personnel Administrator of Mass. v. Feeney, 442 U.S. 256 (1979)). Prove intent with the Village of Arlington Heights v. Metropolitan Housing Development Corp., 429 U.S. 252 (1977) factors: impact; historical background; sequence of events; departures from normal procedure or substance; legislative or administrative history and statements. Extreme patterns can show intent (Yick Wo v. Hopkins, 118 U.S. 356 (1886)).
3. **Choose the tier.**
   - Strict scrutiny (race, national origin, alienage in most state contexts; fundamental rights): narrowly tailored to a compelling interest (Adarand Constructors, Inc. v. Pena, 515 U.S. 200 (1995); Students for Fair Admissions v. President & Fellows of Harvard College, 600 U.S. 181 (2023)).
   - Intermediate (sex; nonmarital children): substantially related to an important interest; for sex, an "exceedingly persuasive justification" (United States v. Virginia, 518 U.S. 515 (1996); Craig v. Boren, 429 U.S. 190 (1976)).
   - Rational basis (everything else, including disability, age, wealth, criminal history): rationally related to any legitimate interest; the challenger must negate every conceivable basis (FCC v. Beach Communications, Inc., 508 U.S. 307 (1993)). Animus can defeat a rational basis (City of Cleburne v. Cleburne Living Center, Inc., 473 U.S. 432 (1985)).
4. **Class-of-one.** Plaintiff intentionally treated differently from others similarly situated with no rational basis for the difference (Village of Willowbrook v. Olech, 528 U.S. 562 (2000)). Not available in the public-employment context (Engquist v. Oregon Dept. of Agriculture, 553 U.S. 591 (2008)). Courts require comparators that are similar in all material respects, and many courts resist class-of-one claims against inherently discretionary decisions - check 8th Circuit law on discretionary policing before relying on it.
5. **Selective enforcement / prosecution.** Discriminatory effect (similarly situated persons of a different class were not prosecuted or stopped) and discriminatory purpose (Wayte v. United States, 470 U.S. 598 (1985)). Discovery on a selective-prosecution claim requires a credible showing of different treatment of similarly situated persons (United States v. Armstrong, 517 U.S. 456 (1996)). Pretext for a stop is an equal protection issue, not a Fourth Amendment one (Whren v. United States, 517 U.S. 806 (1996)).
6. **Missouri.** Mo. Const. art. I, sec. 2 guarantees equal rights and opportunity under the law; Missouri courts generally apply the federal framework. Statutory routes (e.g., Missouri Human Rights Act, Title VI/VII) may be stronger than a constitutional claim for employment, housing, or public accommodations.
7. **Vehicle and remedy.** 1983 for damages/injunction against state and local actors; suppression is generally not a remedy for selective enforcement - dismissal or civil damages are the usual relief.

## Output
- Comparator table: | Person | Protected trait / class | Conduct | Decision-maker | Treatment | Material differences |
- Intent evidence list keyed to each Arlington Heights factor.
- Scrutiny box: classification, tier, government interest asserted, fit analysis.
- Complaint or brief headings: Differential treatment; Similarly situated comparators; Discriminatory purpose (or no rational basis); Injury; Relief.

## Pitfalls
- No comparators, or comparators who differ in material ways - the most common reason these claims fail.
- Relying on statistics alone without intent evidence for facially neutral action.
- Pleading conclusions ("because of my race") without facts showing purpose - dismissed under Iqbal/Rule 55.
- Using class-of-one in a public employment dispute.
- Expecting suppression of evidence as the remedy for profiling.
- Overlooking that the government need not state its actual reason under rational basis; any conceivable basis suffices.
- Not requesting discovery early enough to obtain comparator data (stop data, enforcement logs) through records requests or discovery.
- Bringing a selective-prosecution claim at trial instead of by pretrial motion.

## Verify before relying
- Pull verbatim Mo. Const. art. I sec. 2 and any challenged statute via `statute-lookup` (or Descrybe `search_laws_and_rules`).
- Confirm each case is good law and find 8th Circuit authority on class-of-one and selective enforcement (CourtListener / Descrybe).
- Check the applicable limitations period for the vehicle used (1983 borrows Missouri's personal-injury period).
- Legal information, not legal advice; consult counsel or a civil-rights organization.

## Related skills
- `section-1983-claim-builder` - pleading the claim and Monell liability.
- `due-process-analyzer` - process-based theories.
- `employment-discrimination-claims` - MHRA/Title VII statutory alternatives.
- `qualified-immunity-analyzer` - individual-officer defense.
- `lawmind-legal-research` - grounded research on Missouri applications.
