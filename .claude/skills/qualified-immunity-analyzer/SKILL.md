---
name: qualified-immunity-analyzer
description: Analyzes qualified immunity in 1983 and Bivens cases: the two-prong test, clearly established law as of the conduct date, Eighth Circuit approach, and interlocutory appeals. Use for "qualified immunity", "clearly established law", "officer claims immunity", or opposing a QI motion.
---

# Qualified Immunity Analyzer

Tests whether an individual government official can claim qualified immunity, and builds the plaintiff's (or defendant's) clearly-established-law showing.

## When to use
- A defendant raises qualified immunity in a Rule 12 motion, answer, or summary-judgment motion
- Planning which individual-capacity claims will survive before filing
- Finding factually similar precedent to show the right was clearly established
- Not for: Missouri official immunity or sovereign immunity on state-law claims — use `sovereign-and-official-immunity-mo`

## Gather first
- The exact date of the conduct (clearly established is measured as of that date)
- A precise, fact-specific description of what each official did and knew
- Procedural posture: motion to dismiss (pleadings only) or summary judgment (record evidence)

## Workflow
1. **Confirm QI applies.** It protects individual government officials sued for damages in their individual capacities. It does not apply to official-capacity claims, to municipalities, or to claims for injunctive/declaratory relief. Absolute immunity (judges, prosecutors acting as advocates, witnesses testifying) is a separate, stronger defense.
2. **State the test.** Officials are immune unless (1) the facts, taken in the light most favorable to the plaintiff, show a violation of a constitutional or statutory right, and (2) the right was clearly established at the time of the conduct. Harlow v. Fitzgerald, 457 U.S. 800 (1982); Saucier v. Katz, 533 U.S. 194 (2001). Courts may address the prongs in either order. Pearson v. Callahan, 555 U.S. 223 (2009).
3. **Prong one — violation.** Apply the substantive standard (e.g., Fourth Amendment objective reasonableness for force, probable cause for arrest; arguable probable cause is the common framing for QI on arrests in the Eighth Circuit). Analyze each defendant separately.
4. **Prong two — clearly established.**
   - The right must be defined with specificity, not at a high level of generality. Ashcroft v. al-Kidd, 563 U.S. 731 (2011); Mullenix v. Luna, 577 U.S. 7 (2015); District of Columbia v. Wesby, 583 U.S. 48 (2018).
   - A case directly on point is not required if existing precedent placed the question beyond debate; obvious violations can be clearly established without a factually identical case. Hope v. Pelzer, 536 U.S. 730 (2002); Taylor v. Riojas, 592 U.S. 7 (2020).
   - Sources in the Eighth Circuit: Supreme Court and Eighth Circuit published decisions first; otherwise a robust consensus of persuasive authority. District-court and unpublished decisions carry little weight. Verify the current Eighth Circuit statement of this rule before citing.
   - Search for cases decided before the conduct date with closely analogous facts (same type of officer action, same justification offered).
5. **Burden.** Defendant raises QI; once raised, courts generally require the plaintiff to show the law was clearly established. Facts are viewed in the plaintiff's favor, but at summary judgment the plaintiff needs record evidence (affidavits, video, documents).
6. **Posture strategy.**
   - At Rule 12: argue the complaint's specific facts state a violation of clearly established law; QI is often hard for defendants to win on thin records.
   - At summary judgment: identify genuine disputes of material fact that, if resolved for the plaintiff, defeat immunity; a court cannot resolve those disputes in the officer's favor. Tolan v. Cotton, 572 U.S. 650 (2014). Video that blatantly contradicts a version of events controls. Scott v. Harris, 550 U.S. 372 (2007).
7. **Interlocutory appeal.** Denial of QI on a question of law is immediately appealable by the defendant under the collateral-order doctrine. Mitchell v. Forsyth, 472 U.S. 511 (1985). Denials resting on fact disputes ("evidence sufficiency") are not. Johnson v. Jones, 515 U.S. 304 (1995). Expect a stay of the case during such an appeal.
8. **Preserve alternatives.** Official-capacity/Monell claims, injunctive relief, and state-law claims (subject to Missouri immunity rules) survive even if QI is granted.

## Output
- Per-defendant QI table:

| Defendant | Conduct (date) | Right at specific level | Prong 1 result | Closest pre-conduct authority | Prong 2 result |
|---|---|---|---|---|---|

- A one-paragraph "clearly established" argument per right, citing only verified cases decided before the conduct date
- List of factual disputes that matter for immunity (for summary-judgment opposition)

## Pitfalls
- Defining the right broadly ("right to be free from unreasonable force") — courts reject this
- Citing cases decided after the incident
- Relying on out-of-circuit or district cases without showing a consensus
- Conceding the officer's version of facts at summary judgment
- Treating QI as defeating Monell or injunctive claims (it does not)
- Missing that the defendant can appeal a QI denial immediately, freezing the case

## Verify before relying
- Confirm every case's holding, date, and current treatment via CourtListener or Descrybe; QI doctrine moves quickly.
- Pull 42 U.S.C. 1983 verbatim via `statute-lookup` if quoting it.
- Check the deadline for any interlocutory appeal or cross-appeal from the order's entry date (FRAP 4(a)).
- Legal information, not legal advice; QI litigation is a strong reason to seek civil-rights counsel.

## Related skills
- `section-1983-claim-builder` — the underlying claim and defendant selection
- `federal-summary-judgment` — QI most often decided at Rule 56
- `federal-appeals-8th-circuit` — interlocutory appeals of QI denials
- `fourth-amendment-analyzer` — prong-one analysis for search, seizure, and force
- `lawmind-legal-research` — finding analogous pre-incident precedent
