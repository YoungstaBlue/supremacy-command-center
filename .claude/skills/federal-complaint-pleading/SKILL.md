---
name: federal-complaint-pleading
description: Drafts and audits federal civil complaints under FRCP 8, 10, and 11 and the Twombly/Iqbal plausibility standard, with pro se liberal construction. Use for "federal complaint", "draft my complaint for federal court", "is my complaint plausible", "Iqbal", or fixing a complaint before a Rule 12(b)(6) motion.
---

# Federal Complaint Pleading

Builds a federal complaint that survives screening and Rule 12(b)(6): short and plain, but with enough non-conclusory facts that each claim is plausible against each defendant.

## When to use
- Drafting a new complaint for E.D. Mo., W.D. Mo., or any U.S. district court
- Auditing an existing complaint for plausibility gaps before or after a motion to dismiss
- Preparing an amended complaint after a dismissal without prejudice or a 28 U.S.C. 1915(e) screening order
- Not for: Missouri state-court petitions (fact pleading under Rule 55) — use `mo-petition-drafting`

## Gather first
- Who did what, when, where — per defendant — and the documents that show it
- The legal claims intended (constitutional, statutory, state-law) and the relief wanted
- Whether the plaintiff is proceeding IFP or is a prisoner (triggers 1915/1915A screening)

## Workflow
1. **Confirm the court can hear it.** Subject-matter jurisdiction (federal question or diversity), personal jurisdiction, and venue (28 U.S.C. 1391). Run `federal-subject-matter-jurisdiction` if any doubt.
2. **Apply the pleading standard.**
   - Rule 8(a): (1) short and plain statement of jurisdiction, (2) short and plain statement of the claim showing entitlement to relief, (3) demand for relief.
   - Bell Atlantic Corp. v. Twombly, 550 U.S. 544 (2007), and Ashcroft v. Iqbal, 556 U.S. 662 (2009): disregard legal conclusions and "formulaic recitation of the elements"; ask whether the remaining well-pleaded facts make liability plausible, not merely possible.
   - Pro se pleadings are construed liberally. Erickson v. Pardus, 551 U.S. 89 (2007); Haines v. Kerner, 404 U.S. 519 (1972). Liberal construction does not supply missing facts.
   - Heightened particularity only where required: Rule 9(b) fraud or mistake (who, what, when, where, how).
3. **Plead facts per defendant.** Iqbal requires each government official's own conduct; group pleading ("Defendants violated my rights") fails. One paragraph per act, naming the actor.
4. **Structure the document (Rule 10).**
   - Caption with court name, all parties' names, title "Complaint," and "Jury Trial Demanded" if wanted.
   - Numbered paragraphs, each limited as far as practicable to a single set of circumstances.
   - Sections: Parties; Jurisdiction and Venue; Facts (chronological); Counts (one claim per count, against named defendants, incorporating only the facts that support it); Prayer for Relief; Jury Demand; Signature.
5. **Map elements to facts.** For each count, list the elements and cite the paragraph numbers that satisfy each. Any element with no paragraph is a gap — add facts or drop the count. Use `elements-checklist-builder`.
6. **Capacity and parties.** For government defendants, state individual and/or official capacity expressly (see `section-1983-claim-builder`). Check joinder: claims against multiple defendants must arise from the same transaction or occurrence with a common question (Rule 20); unrelated claims against different defendants belong in separate suits.
7. **Relief.** Specify damages (compensatory, punitive where available), declaratory, and injunctive relief separately. Do not demand relief that is barred (e.g., damages against a State).
8. **Rule 11 and Rule 5.2.** Sign with address, email, phone. Every factual contention must have or likely have evidentiary support. Redact SSNs, birth dates, minors' names, and financial account numbers to the Rule 5.2 format.
9. **Local practice.** Check the district's local rules for required forms for self-represented civil-rights plaintiffs, civil cover sheet, and summons forms. Service must be made within 90 days of filing (Rule 4(m)).
10. **Jury demand.** Serve a demand no later than 14 days after the last pleading directed to the issue (Rule 38(b)); simplest is to include it in the complaint.

## Output
- Complaint draft with the section headings above
- Elements-to-paragraph table:

| Count | Defendant | Element | Supporting paragraph(s) | Gap? |
|---|---|---|---|---|

- A list of conclusory sentences flagged for replacement with specific facts

## Pitfalls
- Labels instead of facts ("unlawfully," "conspired," "maliciously" with nothing behind them)
- Suing supervisors or a city with no facts about their own conduct or policy
- Shotgun pleading: every count incorporating every prior paragraph, making claims indistinguishable
- Including legal argument and case citations in the complaint body; save them for briefs
- Missing the Rule 4(m) service deadline or forgetting summons for each defendant
- Filing a 100-page narrative; length is not plausibility
- Leaving claims unexhausted where exhaustion is required (e.g., prisoner claims under the PLRA, Title VII charges)

## Verify before relying
- Pull current text of FRCP 8, 9, 10, 11, 20, 38, 4(m), 5.2 and the district's local rules via `statute-lookup` or Descrybe `search_laws_and_rules`.
- Confirm Twombly/Iqbal-era Eighth Circuit authority applied in your argument is still good law via CourtListener.
- Recompute the service and jury-demand deadlines from the actual filing/answer dates.
- Legal information, not legal advice; consider legal aid or a court pro se clinic before filing.

## Related skills
- `section-1983-claim-builder` — elements for civil-rights counts
- `federal-subject-matter-jurisdiction` — confirm jurisdiction before drafting
- `federal-ifp-1915` — screening the complaint will face if filed IFP
- `federal-rule-12-motions` — what the defendant will attack next
- `lawmind-god-drafter` — companion documents for the filing bundle
