---
name: brady-giglio-demands
description: Drafts specific Brady/Giglio demands for exculpatory and impeachment evidence and builds violation motions - favorability, suppression, materiality, remedies. Use for "Brady request", "Giglio material", "prosecutor hid evidence", "informant deal", or a late disclosure in a criminal case.
---

# Brady / Giglio Demands

Turns the prosecution's constitutional disclosure duty into specific written demands, then into a violation motion if evidence surfaces late or not at all.

## When to use
- Early in a criminal case to demand favorable evidence in writing, specific to the case.
- Evidence favorable to the defense was disclosed late, mid-trial, or after conviction.
- A state witness has a deal, a record, prior inconsistent statements, or a disciplinary history.
- Not for: general Missouri criminal discovery mechanics (use `mo-criminal-discovery`); civil discovery (use `mo-discovery-requests` or `federal-civil-discovery`).

## Gather first
- Charging document, witness list, police reports, and what discovery has already been produced (with dates).
- Who the key state witnesses are (officers, informants, co-defendants, experts, lab).
- For a violation claim: what was withheld, when the defense learned of it, and how it would have changed strategy or outcome.

## Workflow
1. **The duty.** Due process requires the prosecution to disclose evidence favorable to the accused that is material to guilt or punishment, regardless of good or bad faith (Brady v. Maryland, 373 U.S. 83 (1963)). It includes impeachment evidence, including promises to witnesses (Giglio v. United States, 405 U.S. 150 (1972); United States v. Bagley, 473 U.S. 667 (1985)) and covers evidence known to police and others acting on the government's behalf (Kyles v. Whitley, 514 U.S. 419 (1995)). The duty exists even without a request (United States v. Agurs, 427 U.S. 97 (1976)).
2. **Three components of a violation (Strickler v. Greene, 527 U.S. 263 (1999)).**
   - Favorable: exculpatory or impeaching.
   - Suppressed by the state, willfully or inadvertently.
   - Prejudice/materiality: a reasonable probability of a different result - a probability sufficient to undermine confidence in the outcome (Bagley; Kyles). Assessed cumulatively, not item by item. Not a sufficiency-of-evidence test.
3. **Related doctrines.**
   - Knowing use of false testimony, or failure to correct it (Napue v. Illinois, 360 U.S. 264 (1959); Giglio) - a lower materiality bar applies.
   - Destroyed potentially useful evidence requires bad faith (Arizona v. Youngblood, 488 U.S. 51 (1988)).
   - Impeachment material need not be disclosed before a guilty plea (United States v. Ruiz, 536 U.S. 622 (2002)) - demand it before plea negotiations conclude anyway.
4. **Draft a specific demand.** Generic "all Brady material" requests are weak. List categories tied to the case:
   - Witness deals, payments, immunity, charging or sentencing consideration, informant files and reliability history.
   - Criminal histories, pending charges, probation status of state witnesses.
   - Prior inconsistent statements, notes, recordings, drafts of reports.
   - Officer disciplinary, credibility, or "Brady list" findings.
   - Alternative suspects, failed identifications, exculpatory lab results, contrary expert opinions.
   - Body-cam, dash-cam, CAD, 911, and dispatch records.
   - Evidence supporting mitigation at sentencing.
5. **Procedural vehicles.**
   - Missouri: request disclosure in writing under Rule 25.03 (which lists mandatory disclosures on request, including favorable information); seek sanctions under the Rule 25 provision for failure to comply (verify current rule number) - remedies include continuance, exclusion, or dismissal.
   - Federal: Fed. R. Crim. P. 16; Jencks Act, 18 U.S.C. 3500, and Fed. R. Crim. P. 26.2 for witness statements after direct testimony; Fed. R. Crim. P. 5(f) requires the court to issue an oral and written order confirming the prosecutor's Brady obligation - point to that order.
6. **Timing remedies.** Late disclosure: request continuance, recall of witnesses, exclusion, or a mistrial; the question is whether the defense could still use it effectively. Post-trial: motion for new trial (watch strict Missouri post-trial deadlines) or post-conviction/habeas claim.
7. **Materiality write-up.** Explain concretely how the evidence would have been used: impeach which witness on which point, support which defense theory, alter which investigative step - then assess cumulatively against the strength of the state's case (Wearry v. Cain, 577 U.S. 385 (2016); Smith v. Cain, 565 U.S. 73 (2012)).

## Output
- Specific Brady/Giglio demand letter or motion: caption; legal basis; numbered categories tied to named witnesses and events; request for a continuing-duty order and in camera review of disputed items.
- Violation chart: | Item | Favorable how | When/where known to state | When disclosed | Prejudice/use | Remedy sought |
- Violation motion headings: Facts; Brady standard; Favorable; Suppressed; Material (cumulative); Remedy.

## Pitfalls
- Vague demands that let the state say it was unaware of what you wanted.
- Not acting promptly on late disclosure - failing to seek a continuance can forfeit the claim.
- Arguing materiality item by item instead of cumulatively.
- Treating Brady as a general discovery rule; it covers only favorable, material evidence.
- Missing Missouri motion-for-new-trial or post-conviction deadlines when a violation surfaces after trial.

## Verify before relying
- Pull verbatim Missouri Rule 25.03 and the Rule 25 sanctions provision, Fed. R. Crim. P. 5(f), 16, 26.2, and 18 U.S.C. 3500 via `statute-lookup` (or Descrybe `search_laws_and_rules`).
- Confirm each case's continued validity and find a Missouri or 8th Circuit case on similar facts (CourtListener / Descrybe).
- Recompute post-trial deadlines from the actual verdict/judgment date.
- Legal information, not legal advice; consult counsel or the public defender.

## Related skills
- `mo-criminal-discovery` - Rule 25.03 mechanics and nondisclosure sanctions.
- `impeachment-and-credibility` - using Giglio material at trial.
- `mo-post-trial-motions` / `mo-post-conviction-relief` - post-verdict vehicles.
- `federal-habeas-2254` - Brady as a federal habeas claim.
- `lexcore` - Brady/Giglio discovery demand workflow.
