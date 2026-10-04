---
name: negligence-claim-builder
description: Builds or attacks a Missouri negligence claim element by element - duty, breach, causation, damages - and applies pure comparative fault and joint-and-several rules. Use for car wrecks, slip-and-fall, negligent hiring, negligence per se, res ipsa, or "was this negligence" questions.
---

# Negligence Claim Builder

Turns a fact pattern into a pleadable Missouri negligence count (or a defense map against one), with each element tied to evidence and the comparative-fault consequences spelled out.

## When to use
- Drafting a negligence count for a Rule 55 fact-pleaded petition, or a federal complaint with supplemental state claims
- Evaluating whether a negligence claim survives a motion to dismiss or summary judgment
- Negligence per se (statute/ordinance violation), res ipsa loquitur, negligent hiring/supervision/entrustment
- Defending: identifying missing elements and comparative-fault arguments
- Not for: land-condition cases (use `premises-and-landlord-liability`); intentional conduct (use `intentional-torts`)

## Gather first
- What happened, where, when (exact date - drives limitations), and who did what
- The injury and how it is documented (medical records, bills, repair estimates, wage loss)
- Whether any defendant is a government entity or employee (immunity and notice issues change everything)

## Workflow
1. **Screen threshold issues first.** Limitations (generally 5 years for personal injury under RSMo 516.120; 2 years for medical malpractice under RSMo 516.105) - run `statute-of-limitations-checker`. Government defendant - run `sovereign-and-official-immunity-mo`. Workers' compensation exclusivity if the injury is work-related.
2. **Duty.** Identify the source: general duty of ordinary care (foreseeability of harm to this class of plaintiff), a special relationship, a voluntarily assumed duty, or a statute/ordinance. Duty is a question of law for the court - state the legal source explicitly.
3. **Standard of care.** Ordinary care (what an ordinarily careful person would do), highest degree of care (Missouri applies this to motor vehicle operators and some other activities - confirm the applicable MAI definition), or professional standard (needs expert testimony).
4. **Breach.** List the specific acts or omissions. Missouri fact pleading requires the ultimate facts of each negligent act - not "defendant was negligent." Plead each specification of negligence separately; each must be supported by evidence at trial or it cannot be submitted.
5. **Causation.** Cause-in-fact ("but for") and proximate cause (natural and probable consequence; no superseding intervening cause). Missouri uses but-for causation as the general test - Callahan v. Cardinal Glennon Hospital, 863 S.W.2d 852 (Mo. banc 1993). Identify whether expert testimony is needed (medical causation usually requires it unless obvious).
6. **Damages.** Actual injury is an element; nominal damages do not support negligence. Inventory categories with `damages-calculator`.
7. **Special doctrines.**
   - Negligence per se: (a) violation of a statute/ordinance, (b) plaintiff in the class protected, (c) injury of the kind the law was designed to prevent, (d) violation proximately caused injury. Excuse/justification may rebut.
   - Res ipsa loquitur: (a) occurrence does not ordinarily happen without negligence, (b) instrumentality under defendant's control, (c) defendant has superior knowledge or means of information about the cause. Permits an inference, not a presumption.
   - Negligent hiring/retention/entrustment: employer knew or should have known of the dangerous propensity; that propensity caused the harm. Watch the admission-of-agency issue when respondeat superior is admitted.
8. **Comparative fault.** Missouri adopted pure comparative fault in Gustafson v. Benda, 661 S.W.2d 11 (Mo. banc 1983): plaintiff's recovery is reduced by plaintiff's percentage of fault, never barred. Joint and several liability: under RSMo 537.067 a defendant is jointly and severally liable only if 51% or more at fault (verify current text); otherwise liable only for its own percentage. Comparative fault is an affirmative defense - must be pleaded (Rule 55.08).
9. **Defenses checklist.** Comparative fault; assumption of risk (express and primary implied survive; implied secondary merges into comparative fault); limitations; immunity; failure to mitigate; intervening cause; lack of duty.
10. **Instructions.** Map each element to the Missouri Approved Instruction (MAI) verdict director you will need - use `mo-jury-instructions-mai`. Drafting the petition with the MAI in mind prevents a variance between pleading and submission.

## Output
- Elements table: | Element | Legal source | Facts | Evidence (exhibit/witness) | Gap |
- Specifications of negligence, numbered, each a pleadable ultimate fact
- Comparative-fault exposure note (who else is at fault, likely percentages, effect of RSMo 537.067)
- Draft count heading: "COUNT __ - NEGLIGENCE (against Defendant ___)" with paragraphs for duty, breach (each specification), causation, damages, prayer

## Pitfalls
- Conclusory pleading ("defendant negligently caused injury") fails Missouri fact pleading
- Submitting a specification of negligence with no supporting evidence is reversible error - prune before trial
- Missing medical causation expert in non-obvious injury cases is a summary-judgment loser
- Forgetting to plead comparative fault (defense) or to join all at-fault parties
- Suing a government entity without checking immunity waivers and notice statutes
- Treating res ipsa as a separate cause of action - it is a method of proving negligence

## Verify before relying
- Pull verbatim text of RSMo 516.120, 516.105, 537.067, and Rule 55.08 via `statute-lookup` (or Descrybe `search_laws_and_rules`)
- Confirm Gustafson and Callahan remain good law and check for newer Missouri Supreme Court refinements (CourtListener / Descrybe treatment)
- Recompute limitations from the actual injury/ascertainment date
- Legal information, not legal advice; consult counsel or legal aid for serious-injury claims

## Related skills
- `elements-checklist-builder` - generic element-to-evidence mapping
- `mo-petition-drafting` - Rule 55 count formatting
- `damages-calculator` - quantify each damages category
- `statute-of-limitations-checker` - accrual and tolling
- `mo-jury-instructions-mai` - verdict directors and comparative-fault instructions
- `lawmind-strategy-engine` - stress-test against the defense's comparative-fault theory
