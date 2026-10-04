---
name: sovereign-and-official-immunity-mo
description: Analyzes Missouri sovereign immunity (RSMo 537.600 vehicle and dangerous-condition waivers, 537.610 insurance waiver), official immunity, and the public duty doctrine, contrasted with 1983 rules. Use for "sue the city", "sue the county", "sovereign immunity", or "official immunity".
---

# Sovereign and Official Immunity (Missouri)

Decides whether a Missouri state-law tort claim can proceed against a government entity or a public employee, and what must be pleaded to get past immunity.

## When to use
- Any state-law tort claim naming the State, a state agency, county, city, school district, or other public entity
- Claims against police officers, public employees, or officials individually under state law
- Responding to a motion to dismiss or summary judgment asserting sovereign or official immunity or the public duty doctrine
- Not for: qualified immunity in federal civil-rights suits (use `qualified-immunity-analyzer`)

## Gather first
- Exact defendant(s): the entity's legal name and type (state agency, county, city class, special district) and each employee's role
- What caused the injury: a vehicle, a condition of public property, or an employee's act or decision
- Whether the entity carries liability insurance or participates in a self-insurance pool (request the policy in discovery)

## Workflow
1. **Separate state-law and federal claims.** State immunity doctrines do not defeat a 1983 claim (Howlett v. Rose, 496 U.S. 356 (1990)); but states, state agencies, and state officials in their official capacity are not "persons" subject to 1983 damages (Will v. Michigan Department of State Police, 491 U.S. 58 (1989)), and municipalities are liable only under Monell. Route federal claims to `section-1983-claim-builder` and `qualified-immunity-analyzer`.
2. **Entity sovereign immunity - start from immunity.** RSMo 537.600 preserves sovereign immunity as it existed at common law before September 12, 1977, except as waived. The plaintiff must plead facts bringing the claim within a waiver; immunity is the default, not an affirmative defense to be proved.
3. **Waiver 1 - motor vehicles.** RSMo 537.600.1(1): injuries directly resulting from the negligent acts or omissions of public employees arising out of the operation of motor vehicles or motorized vehicles within the course of employment. Plead the vehicle, the operator, scope of employment, and the negligent operation.
4. **Waiver 2 - dangerous condition of property.** RSMo 537.600.1(2) requires pleading and proving: (a) the property was in a dangerous condition at the time of injury; (b) the injury directly resulted from the dangerous condition; (c) the condition created a reasonably foreseeable risk of harm of the kind incurred; and (d) either a public employee's negligent or wrongful act or omission created the condition, or the entity had actual or constructive notice in time to have taken measures against it. A physical defect in the property itself is usually required - a pure failure to supervise or to provide services typically does not qualify.
5. **Waiver 3 - insurance and self-insurance.** RSMo 537.610 waives immunity to the extent of liability insurance or a self-insurance plan for the type of claim covered; policies that expressly preserve immunity are generally honored. RSMo 537.610 also caps recoveries per person and per occurrence (adjusted annually - pull the current figures). Municipal insurance provisions (e.g., RSMo 71.185) may apply - verify.
6. **Municipal proprietary functions.** Cities (not the State or counties) historically lack immunity for proprietary functions (commercial-type activities for the city's own benefit) as opposed to governmental functions. Classify the function with current case law.
7. **Official immunity (employees individually).** Protects public employees from personal liability for discretionary acts within the scope of their authority, but not for ministerial acts, and not for acts done in bad faith or with malice - Southers v. City of Farmington, 263 S.W.3d 603 (Mo. banc 2008). Analyze each challenged act:
   - Discretionary: requires judgment about whether or how to act (e.g., emergency response decisions).
   - Ministerial: clerical duty performed in a prescribed manner on a given state of facts, without regard to judgment.
   - Bad faith/malice: plead specific facts of conscious wrongdoing or intent to injure, not labels.
8. **Public duty doctrine.** A public employee is not liable for breach of a duty owed to the public generally rather than to the particular plaintiff (Southers discusses its scope and relationship to official immunity). Identify any duty owed specifically to the plaintiff.
9. **Other statutory protections.** Check statutes covering specific officials, volunteers, or functions, and the State Legal Expense Fund (RSMo 105.711) for state employees - verify applicability.
10. **Pre-suit and procedural traps.** City notice statutes (`government-notice-of-claim`), service on the correct official (`mo-service-of-process`), and the 537.610 caps on any judgment.

## Output
- Defendant matrix: | Defendant | Type | Claim | Immunity asserted | Waiver/exception relied on | Facts pleaded | Gap |
- Waiver-pleading paragraphs ready for the petition (motor vehicle or dangerous-condition elements)
- Act-by-act official-immunity chart: | Act | Discretionary or ministerial | Malice/bad-faith facts | Result |
- Federal-claim routing note (what moves to 1983)

## Pitfalls
- Pleading a negligence claim against a city without pleading facts within a 537.600 waiver - dismissed
- Treating sovereign immunity as the defendant's burden to prove
- "Dangerous condition" theories based on employee conduct with no defect in the property
- Conclusory "malice" allegations to defeat official immunity
- Naming the State or a state official in official capacity for 1983 damages
- Overlooking the 537.610 damages cap when valuing the case

## Verify before relying
- Pull verbatim RSMo 537.600, 537.610, 71.185, and 105.711 via `statute-lookup` (or Descrybe `search_laws_and_rules`), including current cap amounts
- Confirm Southers is still good law and check later Missouri Supreme Court official-immunity decisions (CourtListener / Descrybe)
- Recompute limitations and any notice deadline from the injury date
- Legal information, not legal advice; immunity cases are frequently lost at the pleading stage - consider counsel

## Related skills
- `government-notice-of-claim` - pre-suit notice to public entities
- `qualified-immunity-analyzer` - federal individual-capacity defense
- `section-1983-claim-builder` - Monell and official-capacity claims
- `premises-and-landlord-liability` - dangerous-condition facts
- `mo-motion-to-dismiss` - opposing immunity-based dismissal
