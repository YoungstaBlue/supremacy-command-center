---
name: statutory-interpretation-canons
description: Interprets statutes and court rules using plain meaning, textual and substantive canons, Missouri's plain and ordinary meaning rule (RSMo 1.090), lenity, and legislative history. Use for "what does this statute mean", "ambiguous statute", "how will the court read this", or competing readings.
---

# Statutory Interpretation Canons

Reads a statute, ordinance, or court rule the way Missouri and federal courts do, producing the strongest textual argument for a reading and anticipating the opposing reading.

## When to use
- The parties dispute what a statute, ordinance, rule, or contract-like regulation means.
- A word in a statute is undefined, vague, or has multiple meanings.
- Arguing that a criminal statute does not reach the conduct (lenity), or that a statute does not apply retroactively.
- Not for: retrieving the text itself (use `statute-lookup`) or checking whether it was amended (use `good-law-checker`).

## Gather first
- The verbatim text of the provision, its definitions section, and the surrounding sections — for the version in effect on the relevant date.
- The competing readings each side advances.
- Whether the provision is criminal, civil, remedial, procedural, or a waiver of sovereign immunity (the canons differ).

## Workflow
1. **Get the right text.** Use the version in force when the events occurred (criminal: offense date; civil: usually when the claim arose; procedural rules: often the version in force when the step is taken). Read the whole section and the chapter's definitions.
2. **Statutory definitions control.** If the legislature defined the term, use that definition, even if it differs from ordinary usage.
3. **Plain and ordinary meaning.**
   - Missouri: RSMo 1.090 directs that words be taken in their plain or ordinary and usual sense, with technical words given their technical meaning. Missouri courts frequently use a standard dictionary to find ordinary meaning. Courts state that the primary rule is to ascertain legislative intent from the language used, and that when the language is plain and unambiguous there is no room for construction (see Parktown Imports, Inc. v. Audi of America, Inc., 278 S.W.3d 670 (Mo. banc 2009)).
   - Federal: ordinary meaning at the time of enactment, read in context.
4. **Textual canons** (use only those that fit):
   - Whole-act / in pari materia: read related provisions together and harmonize them.
   - Surplusage: give effect to every word; avoid readings that make words meaningless.
   - Expressio unius: listing some items implies exclusion of others.
   - Ejusdem generis: general words after a specific list are limited to things of the same kind.
   - Noscitur a sociis: a word is known by its neighbors.
   - Specific governs general; later-enacted governs earlier when truly in conflict.
   - Consistent usage: the same word means the same thing throughout the act.
   - Grammar and punctuation (last-antecedent rule), applied cautiously.
5. **Substantive canons.**
   - Rule of lenity: genuinely ambiguous criminal statutes are construed in the defendant's favor (both Missouri and federal courts apply it, but only after ordinary tools leave real ambiguity).
   - Constitutional avoidance: prefer a reading that avoids a serious constitutional question.
   - Remedial statutes construed liberally; statutes in derogation of the common law construed strictly (Missouri adopts the common law by RSMo 1.010 except as changed by statute).
   - Waivers of sovereign immunity construed strictly.
   - Presumption against retroactivity; note Mo. Const. art. I, § 13 bars laws retrospective in operation (substantive versus procedural distinction).
6. **Extrinsic sources, only if ambiguous.**
   - Missouri: there is generally little recorded legislative history; courts look to the statute's title, prior versions and amendments, the problem addressed, and related statutes. Bill summaries are weak evidence.
   - Federal: committee reports and statutory history, with the weight disputed; agency interpretations no longer receive Chevron deference after Loper Bright Enterprises v. Raimondo, 603 U.S. 369 (2024) — courts decide the best reading themselves.
7. **Absurdity.** Courts avoid readings producing absurd results, but the bar is high; do not lead with it.
8. **Build both readings.** For each, list the canons supporting it, then explain why yours wins (text and structure first, purpose last).

## Output
- **Provision** (verbatim, version date).
- **Competing readings** (one sentence each).
- **Canon table:** `Canon | Supports reading A or B | Explanation | Authority`
- **Recommended argument** in order: definitions → plain meaning → structure/canons → substantive canons → history.
- **Weak points** in the recommended reading and the best response.

## Pitfalls
- Arguing purpose or fairness before text; Missouri and federal courts start, and usually end, with the words.
- Quoting the current version when an earlier version governs the events.
- Invoking lenity before showing genuine ambiguity after applying ordinary tools.
- Citing a canon without explaining how it applies to these exact words.
- Ignoring a statutory definition section in favor of a dictionary.
- Relying on Chevron deference in federal court; it was overruled in 2024.

## Verify before relying
- Pull verbatim text of every statute/rule cited via `statute-lookup` (or Descrybe `search_laws_and_rules`); check case law is still good law (CourtListener / Descrybe treatment) before citing.
- Confirm the version in effect on the relevant date.
- Legal information, not legal advice; recommend counsel/legal aid for high-stakes decisions.

## Related skills
- `statute-lookup` — verbatim text, including prior versions.
- `good-law-checker` — confirm the provision has not been amended, repealed, or held unconstitutional.
- `precedent-hierarchy-analyzer` — weigh cases that already construed the provision.
- `lawmind-legal-research` — find appellate decisions interpreting the statute.
