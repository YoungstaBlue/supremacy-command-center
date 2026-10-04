---
name: section-1983-claim-builder
description: Builds 42 U.S.C. 1983 civil-rights claims: color of state law, the constitutional violation, personal involvement, causation, capacity, and Monell municipal liability. Use for "1983 claim", "sue the police", "sue the city or county", "civil rights lawsuit", "Monell", or "official vs individual capacity".
---

# Section 1983 Claim Builder

Turns a civil-rights grievance against state or local actors into properly pleaded 1983 counts with the right defendants, capacities, and theory of liability.

## When to use
- Police, jail, prosecutor, city, county, school, or state-agency misconduct
- Deciding whom to sue, in what capacity, and for what relief
- Building a Monell (policy/custom/failure-to-train) theory against a city or county
- Not for: the immunity defense itself — use `qualified-immunity-analyzer`; federal officers — that is a Bivens question, which is sharply limited

## Gather first
- Each actor's name, employer, role, and the specific acts each took, with dates
- The constitutional right(s) at issue and any related criminal case and its outcome
- Any policy, prior incidents, training materials, or complaints showing a pattern

## Workflow
1. **Elements.** A plaintiff must show (a) deprivation of a right secured by the Constitution or federal law, (b) by a person acting under color of state law. West v. Atkins, 487 U.S. 42 (1988).
2. **Color of law.** Government employees acting in their official role qualify, even when abusing it. Private parties qualify only in narrow circumstances (joint action/conspiracy with state actors, public function, close nexus). Pleading a private-party conspiracy requires specific facts of agreement.
3. **Identify the right and its test.** Route to the substantive skill: Fourth Amendment (`fourth-amendment-analyzer`), due process (`due-process-analyzer`), equal protection (`equal-protection-analyzer`), First Amendment retaliation (`first-amendment-analyzer`), false arrest/malicious prosecution (`malicious-prosecution-false-arrest`). Excessive force by police in an arrest is analyzed under Fourth Amendment objective reasonableness; pretrial-detainee conditions under due process; convicted-prisoner conditions under the Eighth Amendment.
4. **Personal involvement.** No respondeat superior. Each individual defendant must have personally participated, directed, or (for supervisors) been deliberately indifferent to or tacitly authorized the violation. Ashcroft v. Iqbal, 556 U.S. 662 (2009).
5. **Proper defendants and capacity.**
   - A State and state agencies are not "persons" for damages. Will v. Michigan Dep't of State Police, 491 U.S. 58 (1989). State officials may be sued in official capacity for prospective injunctive relief only.
   - Official-capacity claims against local officials are claims against the entity. Kentucky v. Graham, 473 U.S. 159 (1985).
   - Individual-capacity claims reach the official personally. Hafer v. Melo, 502 U.S. 21 (1991). In the Eighth Circuit, if the complaint does not clearly state individual capacity, courts presume official capacity only — state "sued in his/her individual and official capacities" for each defendant.
   - Police departments and jails are usually not suable entities separate from the city/county; name the city or county.
   - Judges (judicial acts) and prosecutors (advocacy functions) have absolute immunity from damages.
6. **Monell liability (cities, counties, local entities).** Monell v. Department of Social Services, 436 U.S. 658 (1978). Plead one of:
   - an official policy that is itself unconstitutional;
   - a widespread, persistent custom known to policymakers (plead prior incidents);
   - a decision by a final policymaker (identify who under state/local law);
   - failure to train or supervise amounting to deliberate indifference. City of Canton v. Harris, 489 U.S. 378 (1989); Connick v. Thompson, 563 U.S. 51 (2011) (pattern of similar violations ordinarily required).
   - Plus "moving force" causation linking the policy to the injury. Bd. of Cnty. Comm'rs of Bryan Cnty. v. Brown, 520 U.S. 397 (1997).
   - No Monell liability without an underlying constitutional violation by someone.
7. **Bars to check.**
   - Heck v. Humphrey, 512 U.S. 477 (1994): if success would necessarily imply the invalidity of an outstanding conviction or sentence, the claim is not cognizable until the conviction is reversed, expunged, or otherwise invalidated.
   - Limitations: 1983 borrows the state personal-injury period (Owens v. Okure, 488 U.S. 235 (1989)); in Missouri that is generally five years under RSMo 516.120(4). Accrual is a federal question (Wallace v. Kato, 549 U.S. 384 (2007)) — for false arrest, when legal process begins.
   - Pending state prosecution: consider Younger abstention and a stay.
   - Prisoners: PLRA exhaustion of jail/prison grievances before suit (42 U.S.C. 1997e(a)).
8. **Damages and fees.** Compensatory, nominal, punitive (individuals only, not municipalities), and attorney's fees for prevailing parties under 42 U.S.C. 1988 (pro se non-attorneys generally cannot recover fees for their own time).

## Output
- Defendant matrix:

| Defendant | Entity/employer | Capacity | Acts (para. nos.) | Right violated | Immunity risk | Relief sought |
|---|---|---|---|---|---|---|

- One count per right per defendant group, each with elements mapped to facts
- Monell section: policy theory, policymaker, prior incidents, causation
- Bars checklist: Heck, limitations date, Younger, exhaustion — each marked clear/risk

## Pitfalls
- Suing "the Police Department" or the State for damages
- Omitting "individual capacity," leaving only an official-capacity (entity) claim
- Monell claims resting on a single incident with no policy or pattern facts
- Suing a supervisor purely because of rank
- Filing while a conviction stands that the claim would undermine (Heck)
- Mixing state-law torts in without checking Missouri sovereign/official immunity and notice rules

## Verify before relying
- Pull 42 U.S.C. 1983, 1988, 1997e and RSMo 516.120 verbatim via `statute-lookup`.
- Check Eighth Circuit treatment of every case relied on (CourtListener / Descrybe), especially capacity-pleading and Monell pattern cases.
- Compute the limitations date from the actual accrual event, not the date of discovery of a legal theory.
- Legal information, not legal advice; civil-rights counsel often take strong cases on contingency with fee-shifting.

## Related skills
- `qualified-immunity-analyzer` — the main defense to individual-capacity claims
- `federal-complaint-pleading` — plausibility and structure of the complaint
- `statute-of-limitations-checker` — accrual and tolling details
- `sovereign-and-official-immunity-mo` — parallel Missouri-law claims
- `lawmind-strategy-engine` — stress-test the claim against the defense
