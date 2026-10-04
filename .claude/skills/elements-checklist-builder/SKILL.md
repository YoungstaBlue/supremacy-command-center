---
name: elements-checklist-builder
description: Breaks a civil claim, criminal offense, or defense into its required elements, sets the burden and standard of proof for each, and maps every element to specific evidence with gaps flagged. Use for "what do I have to prove", "elements of", "build an elements chart", "proof matrix", or checking a count before filing.
---

# Elements Checklist Builder

Converts a cause of action, charged crime, or defense into a proof matrix: every element, who must prove it, to what standard, and which evidence proves it.

## When to use
- Before filing a count or answering one: "What do I have to prove for conversion?"
- Defending a charge: "What must the State prove for this offense?"
- Preparing for summary judgment, trial, or a directed-verdict/acquittal motion.
- Auditing a petition or complaint to confirm each element is pleaded with facts.
- Not for: spotting which claims exist in the first place (use `legal-issue-spotter`).

## Gather first
- The exact claim, offense (with statute section), or defense, and the jurisdiction.
- The evidence list: documents, recordings, photos, witnesses, admissions, discovery responses.
- The stage: pleading, discovery, summary judgment, trial, or appeal.

## Workflow
1. **Find the authoritative element source**, in this order:
   - The statute defining the claim or offense (verbatim via `statute-lookup`).
   - Missouri civil: the Missouri Approved Instructions (MAI) verdict director for that claim, which courts treat as the elements a plaintiff must submit; supplemented by Supreme Court of Missouri cases.
   - Missouri criminal: the MAI-CR verdict director for the offense plus the statute and its culpable mental state; check RSMo chapter 562 for mental-state definitions and defaults.
   - Federal civil: the controlling U.S. Supreme Court / 8th Circuit statement of elements.
   - Federal criminal: the statute and the Eighth Circuit Manual of Model Criminal Jury Instructions.
   Do not rely on a single court of appeals summary when a pattern instruction or higher court states the elements.
2. **List elements atomically.** Split compound elements ("knowingly and unlawfully") into separate rows. Include the mental state, causation, and damages as their own elements where required.
3. **Assign burden and standard** for each element:
   - Civil default: preponderance (greater weight) on the plaintiff.
   - Punitive damages in Missouri: clear and convincing evidence (verify the current statute in RSMo 510.261–.265).
   - Criminal: the State proves every element beyond a reasonable doubt; note which defenses the defendant must inject or prove (Missouri distinguishes "special negative defenses" and "affirmative defenses" — check RSMo 556.051 and the specific defense statute).
   - Affirmative defenses in civil cases: burden on the party asserting them.
4. **Map evidence** to each element: exhibit/witness, what it shows, admissibility concerns (hearsay, authentication, foundation), and strength.
5. **Find the gaps.** Mark each element Proven / Partial / Missing. For Missing: the discovery request, subpoena, records request, or witness that could fill it.
6. **Map the opponent's attack.** For each element, the fact or defense the other side will use to negate it.
7. **Pleading check (if drafting).** Missouri requires fact pleading — ultimate facts supporting each element must appear in the petition (Rule 55.05). Federal court requires plausible factual allegations under Rule 8. Confirm each element has a pleaded fact.

## Output
| # | Element | Source (statute / MAI / case) | Burden & standard | Evidence | Admissibility issue | Status | Gap fix | Opponent's attack |
|---|---|---|---|---|---|---|---|---|

Then: **Defenses table** (same columns), **Damages/relief elements**, and a **Top 3 gaps** list with the concrete next step for each.

## Pitfalls
- Leaving out the mental-state or causation element; these are where most claims and prosecutions fail.
- Using an outdated MAI or a superseded statute version; elements change when statutes are amended. Check the offense date for criminal charges.
- Treating evidence as proof without checking admissibility; inadmissible evidence proves nothing at trial or on summary judgment.
- Pleading conclusions ("defendant was negligent") instead of facts for each element under Missouri fact pleading.
- Forgetting that damages is an element for many torts; no proof of damages can defeat an otherwise complete claim.
- Not pleading affirmative defenses in the answer, which can waive them.

## Verify before relying
- Pull verbatim text of every statute/rule cited via `statute-lookup` (or Descrybe `search_laws_and_rules`); check case law is still good law (CourtListener / Descrybe treatment) before citing.
- Confirm the MAI or model instruction version is current.
- Recompute any deadline from the actual service/entry date.
- Legal information, not legal advice; recommend counsel/legal aid for high-stakes decisions.

## Related skills
- `legal-issue-spotter` — find the claims and defenses first.
- `irac-analysis` — deep analysis of a contested element.
- `statute-lookup` — verbatim statute text for the element source.
- `lawmind-god-drafter` — draft the pleading once every element has facts.
- `lexcore` — criminal-defense workflows built on the element chart.
