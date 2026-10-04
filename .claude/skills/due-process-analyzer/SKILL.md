---
name: due-process-analyzer
description: Analyzes procedural due process (protected interest, Mathews v. Eldridge balancing, notice and hearing, post-deprivation remedies) and substantive due process (fundamental rights, shocks the conscience) under the 14th Amendment and Mo. Const. art. I, sec. 10. Use for "due process violation", "no hearing".
---

# Due Process Analyzer

Separates procedural from substantive due process and runs each through the controlling test, so a claim or defense rests on the right theory and survives the doctrines that commonly defeat it.

## When to use
- Government took or terminated property, benefits, a license, employment, or liberty without notice or a hearing.
- A court, agency, or official denied a fair opportunity to be heard.
- A statute or official act is challenged as arbitrary, vague, or infringing a fundamental right.
- Not for: claims governed by a more specific amendment such as unreasonable seizure (use `fourth-amendment-analyzer`) or discrimination (use `equal-protection-analyzer`).

## Gather first
- What was taken (property, liberty, benefit, license, job) and the source of the entitlement (statute, contract, ordinance, policy).
- What process was given: notice (date, content, method), hearing (when, before whom), appeal options used or available.
- Who acted and whether the action followed established procedure or was a random, unauthorized departure.

## Workflow
1. **State action.** Due process limits governments, not private actors (1983 requires action under color of state law).
2. **Pick the more specific provision first.** Where a particular amendment provides explicit protection (e.g., the Fourth Amendment for arrests and pretrial detention), analyze under it rather than generalized due process (Graham v. Connor, 490 U.S. 386 (1989); Albright v. Oliver, 510 U.S. 266 (1994)).
### Procedural due process
3. **Protected interest.** Property interests require a legitimate claim of entitlement grounded in an independent source such as state law, not a unilateral expectation (Board of Regents v. Roth, 408 U.S. 564 (1972)). Liberty includes freedom from bodily restraint and certain state-created interests; in prison, only atypical and significant hardships (Sandin v. Conner, 515 U.S. 472 (1995)). Reputation alone is not enough - stigma plus a change in legal status is required (Paul v. Davis, 424 U.S. 693 (1976)).
4. **Deprivation.** Intentional or at least more than negligent; negligent acts do not "deprive" (Daniels v. Williams, 474 U.S. 327 (1986)).
5. **What process is due - Mathews v. Eldridge, 424 U.S. 319 (1976).** Balance (a) the private interest affected; (b) the risk of erroneous deprivation under current procedures and the value of additional safeguards; (c) the government's interest, including administrative burden.
   - Baseline: notice reasonably calculated to apprise the party and an opportunity to respond (Mullane v. Central Hanover Bank & Trust Co., 339 U.S. 306 (1950)).
   - Public employees with property interest: pre-termination notice and opportunity to respond (Cleveland Bd. of Educ. v. Loudermill, 470 U.S. 532 (1985)).
   - Welfare benefits: pre-termination evidentiary hearing (Goldberg v. Kelly, 397 U.S. 254 (1970)).
6. **Post-deprivation remedy defense.** For random and unauthorized deprivations, an adequate state post-deprivation remedy satisfies due process (Parratt v. Taylor, 451 U.S. 527 (1981); Hudson v. Palmer, 468 U.S. 517 (1984)). Not so where the deprivation was predictable and pre-deprivation process was feasible, especially when officials had authority to provide it (Zinermon v. Burch, 494 U.S. 113 (1990)). Identify Missouri remedies (replevin, RSMo 536 review, tort claims) and argue why they are or are not adequate.
7. **Failure to use available procedures.** Courts often reject claims where the plaintiff skipped an available hearing or appeal - explain why the process offered was inadequate, not just unused.
### Substantive due process
8. **Legislative acts.** Fundamental right (deeply rooted in history and tradition, carefully described) triggers strict scrutiny (Washington v. Glucksberg, 521 U.S. 702 (1997), reaffirmed in Dobbs v. Jackson Women's Health Org., 597 U.S. 215 (2022)); otherwise rational basis.
9. **Executive acts.** Must "shock the conscience" (County of Sacramento v. Lewis, 523 U.S. 833 (1998)); deliberate indifference may suffice where time to deliberate existed, intent to harm required in rapid-response situations.
10. **Vagueness.** A law is void for vagueness if it fails to give ordinary people fair notice or invites arbitrary enforcement (Kolender v. Lawson, 461 U.S. 352 (1983)).
11. **Missouri.** Mo. Const. art. I, sec. 10 ("No person shall be deprived of life, liberty or property without due process of law") is usually read in step with the federal clause; raise it separately and at the earliest opportunity, since Missouri courts treat constitutional issues not timely raised as waived.

## Output
- Procedural DP table: | Interest | Source of entitlement | Deprivation (act, date, actor) | Process given | Process due (Mathews factors) | Post-deprivation remedy adequate? |
- Substantive DP box: right claimed (carefully described), tier of review, government interest, fit.
- Pleading or brief headings: Protected interest; Deprivation; Constitutionally inadequate process; Damages/relief.

## Pitfalls
- Claiming a "right" to a job, permit, or benefit with no entitlement source in law or contract.
- Calling every unfair act substantive due process - courts disfavor expansion and require the conscience-shocking standard.
- Ignoring Parratt/Hudson when the official acted outside established procedure.
- Using due process when the Fourth Amendment or Equal Protection Clause governs.
- Failing to raise the constitutional issue at the first opportunity in Missouri state proceedings.

## Verify before relying
- Pull verbatim Mo. Const. art. I sec. 10 and any statute creating the entitlement via `statute-lookup` (or Descrybe `search_laws_and_rules`).
- Confirm each case remains good law and locate 8th Circuit or Missouri cases on the specific interest (CourtListener / Descrybe).
- Recompute any administrative appeal or limitations deadline from the decision or notice date.
- Legal information, not legal advice; consult counsel or legal aid for significant deprivations.

## Related skills
- `section-1983-claim-builder` - the vehicle for damages and injunctions.
- `qualified-immunity-analyzer` - individual-capacity defense.
- `mo-administrative-appeals` - RSMo 536 review as the state process.
- `equal-protection-analyzer` - when the complaint is unequal treatment.
- `lawmind-strategy-engine` - stress-test the theory against the opposing side.
