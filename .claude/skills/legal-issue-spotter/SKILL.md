---
name: legal-issue-spotter
description: Finds every possible claim, defense, procedural issue, and deadline in a fact pattern or document set before any research or drafting begins. Use for "what claims do I have", "spot the issues", "what can they sue me for", "what defenses do I have", or a new set of facts, a complaint, or a charging document.
---

# Legal Issue Spotter

Turns a raw fact pattern into a complete, ranked inventory of legal issues so nothing is missed before research, strategy, or drafting starts.

## When to use
- A new matter, incident, or document (petition, complaint, charge, notice, letter) arrives and the issues are not yet mapped.
- "What claims do I have?", "What can they get me for?", "What defenses apply?", "What am I missing?"
- Before drafting, to make sure every count and every affirmative defense is considered.
- Not for: deep analysis of one issue (use `irac-analysis`) or adversarial testing of a chosen theory (use `lawmind-strategy-engine`).

## Gather first
- The facts in chronological order: who, what, when, where, and what documents or recordings exist.
- The procedural posture: nothing filed yet, sued, charged, judgment entered, on appeal — and the key dates (incident, service, entry of judgment).
- Which side the user is on and what outcome they want (money, dismissal, property back, injunction, record cleared).

## Workflow
1. **Build the timeline.** List each event with its date and source document. Flag any date that is uncertain; dates drive limitations and deadlines.
2. **Identify actors and their capacity.** For each person or entity: private individual, business, government body, government employee (and acting in what capacity), court officer. Government involvement triggers constitutional claims, immunities, and notice requirements.
3. **Sweep by category.** Run every fact through each lens and write down any plausible issue:
   - Constitutional: Fourth (search/seizure), Fifth (self-incrimination, takings, due process), Sixth (counsel, confrontation, speedy trial), Eighth, Fourteenth (due process, equal protection), First (speech, petition, retaliation); Missouri Constitution counterparts.
   - Criminal: elements of each charged offense, lesser-included offenses, suppression issues, discovery/Brady, speedy trial, bond.
   - Torts: negligence, intentional torts, defamation, malicious prosecution, abuse of process, conversion, civil conspiracy.
   - Contract / UCC / consumer: formation, breach, warranty, debt collection, merchandising practices.
   - Property / landlord-tenant / family / probate.
   - Statutory civil rights: 42 U.S.C. § 1983 against state actors; employment and housing discrimination statutes.
   - Government process: sovereign/official immunity, notice-of-claim requirements, Sunshine Law, administrative exhaustion.
4. **Sweep for procedure.** For each potential case: which court has jurisdiction, venue, service problems, standing, ripeness/mootness, statute of limitations, prior judgments (res judicata/collateral estoppel), pending parallel proceedings, and any deadline already running.
5. **Sweep for defenses the other side will raise** against each claim, and affirmative defenses the user must plead or lose (in Missouri, affirmative defenses must be pleaded with supporting facts in the answer).
6. **Triage.** For each issue rate: legal viability (strong / plausible / weak), evidence available (have / obtainable / missing), urgency (deadline date), and value (what relief it yields).
7. **Flag immediate deadlines** at the top of the output — anything within 30 days, and any deadline whose start date is unknown.

## Output
- **Urgent deadlines** (date, what is due, source of the deadline — marked "verify").
- **Issue inventory table:** `# | Issue | Category | Claim or defense | Key facts | Evidence status | Viability | Deadline/limitations | Next skill`
- **Facts needed** — the questions whose answers would change the analysis (max 3 asked now).
- **Recommended order of work** — which issues to research first and why.

## Pitfalls
- Stopping at the obvious claim; the overlooked procedural issue (service, limitations, notice) is often the one that decides the case.
- Treating every grievance as a claim; a wrong without a legal cause of action, damages, or a proper defendant goes nowhere.
- Missing immunity: suing a government body or official without checking sovereign, official, judicial, prosecutorial, or qualified immunity.
- Missing the limitations period because the accrual date was assumed rather than determined.
- Failing to plead affirmative defenses or compulsory counterclaims in the first responsive pleading, which can waive them.
- Mixing federal and Missouri standards (e.g., federal notice pleading versus Missouri fact pleading).

## Verify before relying
- Pull verbatim text of every statute/rule cited via `statute-lookup` (or Descrybe `search_laws_and_rules`); check case law is still good law (CourtListener / Descrybe treatment) before citing.
- Recompute any deadline from the actual service/entry date.
- Legal information, not legal advice; recommend counsel/legal aid for high-stakes decisions.

## Related skills
- `elements-checklist-builder` — break each surviving issue into provable elements.
- `irac-analysis` — analyze one issue in depth.
- `jurisdiction-and-venue-analyzer` — decide where each claim belongs.
- `lawmind-strategy-engine` — stress-test the chosen theory against the other side.
- `omni-juris` — run the whole matter end to end once issues are mapped.
