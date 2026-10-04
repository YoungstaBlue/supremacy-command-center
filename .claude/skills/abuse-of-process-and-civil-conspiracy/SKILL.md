---
name: abuse-of-process-and-civil-conspiracy
description: Builds and tests Missouri abuse of process, malicious prosecution (civil and criminal), and civil conspiracy claims, plus federal 1983/1985(3) conspiracy - elements, pleading specificity, and common defenses. Use for "abuse of process", "they sued me to harass me", "malicious prosecution", "conspired against me", or "civil conspiracy".
---

# Abuse of Process and Civil Conspiracy

Separates three often-confused claims - abuse of process, malicious prosecution, and civil conspiracy - and pleads only the ones the facts actually support.

## When to use
- Someone used a lawsuit, subpoena, garnishment, protective order, or criminal complaint for a purpose other than its proper one
- A prior case or charge ended in the user's favor and was brought without probable cause
- Multiple people (private and/or government) acted together to injure the user
- Not for: a Fourth Amendment malicious-prosecution or false-arrest claim against officers (use `malicious-prosecution-false-arrest`)

## Gather first
- The process used (case number, type of filing, dates filed and resolved) and how the earlier proceeding ended
- What the defendant actually did with the process, and what they wanted to achieve by it
- For conspiracy: specific facts showing an agreement - communications, coordinated timing, who did which overt act

## Workflow
1. **Classify the grievance.**
   - Filing a baseless case is malicious prosecution, not abuse of process.
   - Using properly issued process to accomplish a collateral goal it was not designed for (extortion, leverage in an unrelated dispute) is abuse of process.
   - Conspiracy is never a stand-alone claim; it attaches to an underlying tort.
2. **Abuse of process elements** (Ritterbusch v. Holt, 789 S.W.2d 491 (Mo. banc 1990)): (1) an illegal, improper, or perverted use of process - a use neither warranted nor authorized by the process; (2) an improper purpose in doing so; (3) resulting damage. Key test: if the action is confined to its regular function, there is no abuse even with bad motive. Plead the specific collateral demand or act (e.g., "dismiss your claim or I will keep the garnishment").
3. **Malicious prosecution elements** (Sanders v. Daniel International Corp., 682 S.W.2d 803 (Mo. banc 1984)): (1) commencement or prosecution of a proceeding against the plaintiff; (2) instigated by the defendant; (3) termination in the plaintiff's favor; (4) lack of probable cause; (5) malice; (6) damages. Missouri disfavors this tort and requires strict compliance with each element. Termination must reflect on the merits/innocence - a settlement or compromise usually does not qualify. Reliance on advice of counsel after full disclosure, or a grand-jury indictment / probable-cause finding, is strong evidence of probable cause. Limitations: 2 years under RSMo 516.140, generally from favorable termination.
4. **Civil conspiracy (Missouri)** (Oak Bluff Partners, Inc. v. Meyer, 3 S.W.3d 777 (Mo. banc 1999)): (1) two or more persons, (2) with an unlawful objective, (3) after a meeting of the minds, (4) committed at least one act in furtherance, (5) causing damage. It extends liability to co-conspirators for the underlying tort; if the underlying tort fails, conspiracy fails. Limitations follows the underlying tort.
5. **Intracorporate conspiracy check.** A corporation and its own employees/agents acting within scope generally cannot conspire with each other. Also applied to employees of a single government entity in many federal cases - verify current Eighth Circuit treatment.
6. **Federal conspiracy options.**
   - 1983 conspiracy: agreement between state actors (or a private party jointly engaged with state actors) to deprive a constitutional right, an overt act, and an actual deprivation. Private parties who conspire with officials act under color of law - Dennis v. Sparks, 449 U.S. 24 (1980).
   - 42 U.S.C. 1985(3): requires racial or otherwise class-based, invidiously discriminatory animus - Griffin v. Breckenridge, 403 U.S. 88 (1971). Without class-based animus, do not plead 1985(3).
   - Plead specific facts of agreement; bare allegations of conspiracy fail Twombly/Iqbal.
7. **Defenses to anticipate.** Absolute privilege for statements in judicial proceedings (defeats defamation-style theories, not abuse of process itself); Noerr-Pennington petitioning immunity; judicial and prosecutorial absolute immunity; probable cause; intracorporate doctrine; limitations.
8. **Counterclaim timing.** Malicious prosecution cannot be brought as a counterclaim in the same case it attacks - it requires the prior case to have ended. Abuse of process may be pleaded while the underlying case is pending; check compulsory-counterclaim rules (Rule 55.32).

## Output
- Classification memo: which of the three claims fit, and why the others do not
- Elements table per claim: | Element | Facts | Evidence | Gap |
- Conspiracy fact sheet: each conspirator, each communication or coordinated act, date, source document
- Draft count headings ("COUNT __ - ABUSE OF PROCESS", "COUNT __ - CIVIL CONSPIRACY TO COMMIT [underlying tort]")

## Pitfalls
- Calling a meritless lawsuit "abuse of process" - it is malicious prosecution and needs favorable termination
- Pleading conspiracy alone with no underlying tort
- Conclusory "they conspired" allegations - dismissed for lack of specific agreement facts
- Filing malicious prosecution while the underlying case is still pending
- Pleading 1985(3) without class-based animus
- Suing judges or prosecutors for in-court acts (absolute immunity)

## Verify before relying
- Pull verbatim RSMo 516.140 and Rule 55.32 via `statute-lookup` (or Descrybe `search_laws_and_rules`); confirm the limitations period for abuse of process specifically
- Confirm Ritterbusch, Sanders, Oak Bluff, Dennis, and Griffin are still good law (CourtListener / Descrybe)
- Recompute limitations from favorable termination or the abusive act
- Legal information, not legal advice; these claims invite fee and sanctions motions - consider counsel

## Related skills
- `malicious-prosecution-false-arrest` - Fourth Amendment version against officers
- `section-1983-claim-builder` - color of law and personal involvement
- `qualified-immunity-analyzer` - official defendants
- `intentional-torts` - underlying torts for a conspiracy count
- `federal-complaint-pleading` - plausibility for conspiracy facts
