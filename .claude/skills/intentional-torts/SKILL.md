---
name: intentional-torts
description: Analyzes and pleads Missouri intentional torts - battery, assault, false imprisonment, intentional infliction of emotional distress (IIED), conversion, and trespass - with elements, privileges, defenses, and limitations periods. Use for "he hit me", "I was detained", "they took my property", "outrageous conduct", or "trespassing".
---

# Intentional Torts

Maps intentional-conduct facts to the right Missouri tort, its elements, the defenses and privileges that defeat it, and the limitations period that governs it.

## When to use
- Physical contact or threat (battery, assault), unlawful detention (false imprisonment), seizure of property (conversion), entry onto land (trespass)
- Extreme conduct causing severe distress (IIED) or negligent infliction (NIED) questions
- Pairing state torts with a 42 U.S.C. 1983 claim against officers
- Not for: arrest or prosecution without probable cause as a federal claim (use `malicious-prosecution-false-arrest`); careless conduct (use `negligence-claim-builder`)

## Gather first
- Date of each act (2-year vs 5-year limitations split matters immediately)
- Who acted, in what capacity (private person, employee, police/public employee, merchant)
- Proof: video, witnesses, medical records, police reports, property ownership documents

## Workflow
1. **Pick the tort(s).** Elements below; plead each as a separate count with ultimate facts.
   - **Battery:** intended, offensive (or harmful) bodily contact with the plaintiff. Intent to make the contact is enough; intent to injure is not required.
   - **Assault:** an act intended to cause apprehension of imminent harmful or offensive contact, and the plaintiff reasonably apprehended it. Words alone usually insufficient without an apparent present ability.
   - **False imprisonment:** confinement or restraint of the plaintiff against their will, without legal justification. Any duration counts; awareness of confinement generally required. Shopkeeper's privilege: RSMo 537.125 permits a merchant to detain on reasonable grounds, in a reasonable manner, for a reasonable time - see Highfill v. Hale, 186 S.W.3d 277 (Mo. banc 2006).
   - **IIED:** (a) extreme and outrageous conduct, (b) intentional or reckless, (c) causing severe emotional distress that results in bodily harm. Missouri adds that where the conduct is also another traditional tort, IIED lies only if the conduct was intended solely to cause extreme emotional distress - Gibson v. Brewer, 952 S.W.2d 239 (Mo. banc 1997). Expect courts to dismiss IIED that duplicates battery or defamation.
   - **NIED (companion):** Missouri requires emotional distress that is medically diagnosable and medically significant - Bass v. Nooney Co., 646 S.W.2d 765 (Mo. banc 1983).
   - **Conversion:** plaintiff owned or had right to possess the property; defendant exercised unauthorized dominion inconsistent with plaintiff's rights. If defendant's original possession was lawful, a demand and refusal is usually needed. Money is convertible only if a specific, identifiable fund.
   - **Trespass to land:** unauthorized, intentional entry onto land in plaintiff's possession. Damages presumed (at least nominal). Trespass to chattels for interference short of conversion.
2. **Privileges and defenses.** Consent (scope matters), self-defense/defense of others (reasonable force, proportionate), defense of property (no deadly force for property alone), lawful arrest authority, merchant's privilege, parental discipline, necessity. Defendant bears the burden on privileges pleaded as affirmative defenses (Rule 55.08).
3. **Limitations.** RSMo 516.140 sets 2 years for assault, battery, false imprisonment, libel, slander, and malicious prosecution. Conversion, trespass, and IIED generally fall under RSMo 516.120's 5-year period. Confirm accrual with `statute-of-limitations-checker`.
4. **Government actors.** Police and public employees: official immunity does not protect conduct done in bad faith or with malice; entity sovereign immunity under RSMo 537.600 generally bars intentional-tort claims against the entity. Run `sovereign-and-official-immunity-mo`. Consider parallel 1983 excessive-force (Fourth Amendment objective reasonableness) or unlawful-seizure claims.
5. **Damages.** Actual (medical, property value at time of conversion plus interest, emotional distress), nominal where contact or entry is proven without measurable harm, and punitive where conduct was intentional and without just cause (leave of court required - see `damages-calculator`).
6. **Evidence plan.** Tie each element to a document or witness; flag gaps.

## Output
- Tort selection table: | Tort | Elements met? | Key facts | Evidence | Limitations deadline | Defense risk |
- One draft count per viable tort, captioned "COUNT __ - BATTERY (against ___)" etc.
- Privilege/defense rebuttal list
- Note on whether to add punitive damages later by motion for leave

## Pitfalls
- Filing battery or false imprisonment after 2 years because the 5-year personal-injury period was assumed
- Pleading IIED as a catch-all on top of battery - dismissed under the Gibson "solely to cause distress" rule
- Claiming conversion of a general debt or unidentified money
- No demand-and-refusal when defendant first held property lawfully
- Suing the city itself for an officer's battery without addressing sovereign immunity
- Asserting punitive damages in the initial petition (RSMo 510.261 requires leave)

## Verify before relying
- Pull verbatim RSMo 516.140, 516.120, 537.125, 510.261 via `statute-lookup` (or Descrybe `search_laws_and_rules`)
- Confirm Highfill, Gibson, and Bass are still good law and check newer Missouri appellate treatment (CourtListener / Descrybe)
- Recompute each limitations deadline from the actual act date
- Legal information, not legal advice; consult counsel or legal aid for serious claims

## Related skills
- `malicious-prosecution-false-arrest` - Fourth Amendment and state malicious-prosecution claims
- `section-1983-claim-builder` - federal counterpart for official misconduct
- `negligence-claim-builder` - alternative pleading if intent is hard to prove
- `damages-calculator` - punitive leave procedure and caps
- `mo-replevin-and-property-recovery` - getting the property back, not just damages
