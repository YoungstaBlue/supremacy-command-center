---
name: first-amendment-analyzer
description: Analyzes free speech, retaliation, and petition-clause issues - protected speech, content-based vs neutral rules, public forums, public-employee speech, retaliatory arrest. Use for "First Amendment", "free speech", "retaliation for complaining", "arrested for filming police", "blocked by official".
---

# First Amendment Analyzer

Classifies the speech and the government action, then applies the matching framework - retaliation, forum, content regulation, or public-employee speech - so the claim is pleaded under the right test.

## When to use
- Government retaliated after speech, a complaint, a lawsuit, a records request, or a grievance.
- Arrest, citation, or ban linked to protest, criticism, recording officials, or speaking at a public meeting.
- A rule, permit scheme, or order restricts speech; a public official blocked or deleted comments.
- Not for: defamation claims between private parties (use `defamation-analyzer`); unequal treatment without a speech component (use `equal-protection-analyzer`).

## Gather first
- The exact speech or petitioning activity (words, medium, place, date) and the audience.
- The adverse action (arrest, citation, firing, ban, denial) with date, actor, and stated reason.
- Evidence linking the two: timing, statements by officials, treatment of others who did not speak, and whether probable cause existed for any arrest.

## Workflow
1. **State action.** Only government actors are bound. For officials' social media, the account conduct is state action only if the official had actual authority to speak for the state on the matter and purported to exercise it (Lindke v. Freed, 601 U.S. 187 (2024)).
2. **Is the speech protected?** Unprotected or less-protected categories are narrow: incitement to imminent lawless action likely to produce it (Brandenburg v. Ohio, 395 U.S. 444 (1969)); true threats, requiring at least recklessness as to the threatening nature (Counterman v. Colorado, 600 U.S. 66 (2023)); fighting words; obscenity; defamation; speech integral to crime. Offensive or profane criticism of officials is generally protected (Cohen v. California, 403 U.S. 15 (1971)). Filing lawsuits and grievances is protected petitioning (BE&K Construction Co. v. NLRB, 536 U.S. 516 (2002)).
3. **Retaliation claim (general framework).** Plaintiff must show: (a) protected activity; (b) adverse action that would chill a person of ordinary firmness from continuing; (c) causal connection - the protected activity was a but-for cause. Government may defeat liability by showing it would have taken the same action anyway (Mt. Healthy City School Dist. Bd. of Educ. v. Doyle, 429 U.S. 274 (1977)). Find the 8th Circuit's formulation before pleading.
4. **Retaliatory arrest.** Probable cause generally defeats the claim (Nieves v. Bartlett, 587 U.S. 391 (2019)), except where the plaintiff presents objective evidence that similarly situated people not engaged in protected speech were not arrested; that evidence need not be a strict comparator (Gonzalez v. Trevino, 602 U.S. 653 (2024)). An official municipal policy of retaliation can be challenged despite probable cause (Lozman v. Riviera Beach, 585 U.S. 87 (2018)).
5. **Retaliatory prosecution.** Plaintiff must plead and prove the absence of probable cause (Hartman v. Moore, 547 U.S. 250 (2006)).
6. **Public employees.** Speech pursuant to official duties is unprotected (Garcetti v. Ceballos, 547 U.S. 410 (2006)). Speech as a citizen on a matter of public concern is weighed against the employer's interest in efficient operations (Pickering v. Board of Education, 391 U.S. 563 (1968)); sworn testimony outside ordinary duties is citizen speech (Lane v. Franks, 573 U.S. 228 (2014)). Petition-clause claims by employees also require a matter of public concern (Borough of Duryea v. Guarnieri, 564 U.S. 379 (2011)).
7. **Speech regulations.**
   - Content-based (on its face or by purpose) triggers strict scrutiny (Reed v. Town of Gilbert, 576 U.S. 155 (2015)).
   - Content-neutral time, place, manner rules: narrowly tailored to a significant interest, leaving ample alternative channels (Ward v. Rock Against Racism, 491 U.S. 781 (1989)).
   - Forum: traditional and designated public forums get the full test; limited and nonpublic forums allow reasonable, viewpoint-neutral restrictions (Perry Educ. Ass'n v. Perry Local Educators' Ass'n, 460 U.S. 37 (1983)); restrictions must be capable of reasoned application (Minnesota Voters Alliance v. Mansky, 585 U.S. 1 (2018)). Public-comment periods at meetings are typically limited forums - viewpoint discrimination is still barred.
   - Prior restraints and permit schemes with unbridled discretion are heavily disfavored.
8. **Missouri.** Mo. Const. art. I, sec. 8 (speech) and sec. 9 (assembly and petition). Missouri has an anti-SLAPP statute for speech at public meetings and hearings (verify scope of RSMo 537.528 via `statute-lookup`) - useful when sued for speaking.
9. **Vehicle.** 1983 for damages or injunction; facial vs as-applied challenge; preliminary injunction where speech is ongoing (loss of First Amendment freedoms is commonly treated as irreparable harm).

## Output
- Retaliation chart: | Protected activity (date) | Adverse action (date, actor) | Chill to ordinary person | Causation evidence | Probable cause? | Same-decision defense risk |
- Regulation analysis: content-based or neutral; forum type; tier; tailoring; alternatives.
- Complaint headings per count: Protected activity; Adverse action; Causation; Damages; Relief.

## Pitfalls
- Ignoring probable cause in retaliatory-arrest and prosecution claims - it usually ends the claim.
- Relying on timing alone without other causation evidence.
- Public employees pleading speech that was part of their job duties.
- Treating threats or harassment as protected speech without analyzing the categories.
- Suing private platforms or businesses under the First Amendment.
- Delaying a challenge to an ongoing restriction; delay undercuts claimed irreparable harm.
- Overlooking viewpoint discrimination in limited forums, which remains unconstitutional even where content limits are allowed.
- Missing preservation: raise state constitutional speech claims separately in Missouri court.

## Verify before relying
- Pull verbatim Mo. Const. art. I secs. 8-9, RSMo 537.528, and any challenged ordinance via `statute-lookup` (or Descrybe `search_laws_and_rules`).
- Confirm each case's status and find the controlling 8th Circuit retaliation formulation (CourtListener / Descrybe).
- Check the 1983 limitations period and any notice-of-claim requirement for related state claims.
- Legal information, not legal advice; consult counsel or a civil-liberties organization.

## Related skills
- `section-1983-claim-builder` / `qualified-immunity-analyzer` - vehicle and defense.
- `malicious-prosecution-false-arrest` - probable cause analysis for arrests and charges.
- `federal-tro-preliminary-injunction` - stopping ongoing speech restrictions.
- `defamation-analyzer` - when the dispute is about false statements.
