---
name: mo-small-claims-associate-circuit
description: Guides Missouri small claims ($5,000 limit, RSMo 482) and associate circuit civil cases (RSMo 517) - forum choice, filing, counterclaims, hearing prep, trial de novo vs appeal. Use for "small claims", "associate circuit", "sue for under $5,000", "trial de novo".
---

# Missouri Small Claims and Associate Circuit Cases

Chooses between small claims and regular associate circuit filing, prepares the case for an informal hearing, and preserves the right to a trial de novo or appeal.

## When to use
- Suing or being sued for a modest money claim in Missouri
- A case set in the associate circuit division (including landlord-tenant cases under RSMo ch. 534/535)
- Lost in small claims or associate circuit and need to know whether to seek trial de novo or appeal
- Not for: eviction-specific defenses (use `mo-landlord-tenant-eviction`); municipal ordinance cases (use `mo-municipal-ordinance-defense`)

## Gather first
- Amount claimed (including whether it can be stated as a sum certain) and the type of claim
- Where the defendant lives or where the transaction occurred (for venue)
- Judgment date, if one has already been entered, and whether a record (court reporter or recording) was made

## Workflow
1. **Pick the forum.**
   - Small claims: civil claims for money up to $5,000 exclusive of interest and costs (RSMo 482.305 - verify current limit). Simplified forms, lawyers optional, judge decides, no jury, limited discovery. Check annual filing limits on number of small claims per person (verify RSMo 482.300-.365).
   - Regular associate circuit civil case: governed by RSMo ch. 517 and the Supreme Court Rules as applied to associate circuit cases (verify which rules apply under RSMo 517.011 and Rule 41.01). Use when the claim exceeds the small-claims limit or you need formal discovery, a jury, or non-money relief the associate division can grant.
   - Circuit division: larger or complex claims; full Rules 41-101 practice.
2. **Venue and parties.** File in the county where the defendant resides or where the claim arose, per the small-claims venue provision or RSMo 508.010 (verify). Use exact legal names; individual owners vs. business entities matter.
3. **Filing.** Small claims petition form (from the clerk or courts.mo.gov), filing fee or poor-person request (`mo-poor-person-filing`), service by certified mail or sheriff (verify). Associate circuit petitions follow fact-pleading norms (`mo-petition-drafting`).
4. **Defendant's response.** In small claims a written answer is generally not required - appear at the hearing (verify). Counterclaims within the small-claims limit can be heard; a counterclaim over the limit may require transfer to a regular docket (verify the transfer rule). In associate circuit cases, check whether ch. 517 requires a written answer; filing one is the safer practice.
5. **Hearing prep.** Two-page timeline (`evidence-timeline-builder`), three copies of each exhibit, receipts and estimates for damages, witnesses present in person (subpoena if needed). Business records may need a records affidavit (see `mo-evidence-rules`). Prepare a 2-minute opening summary.
6. **At the hearing.** Rules of evidence are relaxed in small claims but not absent; stay on the elements. If a party fails to appear, a default or dismissal may be entered - always arrive early.
7. **After judgment - trial de novo vs appeal.**
   - Small claims and certain associate circuit cases tried without a jury (including ch. 534 cases) carry a right to a trial de novo in circuit court rather than an appeal on the record (RSMo 512.180 - verify). Application for trial de novo must be filed within a short period after judgment, generally 10 days (RSMo 512.190 / 482.365 - verify), with any required bond or fee.
   - Other associate circuit cases heard on the record (with a court reporter or recording, or assigned under circuit procedures) are appealed to the Court of Appeals (see `mo-appeals-procedure`).
   - A trial de novo starts over; prepare as if no hearing occurred.
8. **Collecting.** If the judgment is unpaid, see `mo-garnishment-and-execution`.

## Output
- Forum decision memo: | Option | Limit | Jury? | Discovery | After-judgment review | Fit |
- Small claims petition text or hearing packet: claim statement, damages computation, exhibit list, witness list, timeline
- Post-judgment deadline card: judgment date, trial de novo or appeal deadline, bond or fee

## Pitfalls
- Splitting one claim into multiple small claims to stay under the limit - generally not allowed and may waive the excess.
- Suing the wrong party (owner instead of LLC, or vice versa).
- Missing the short trial de novo deadline; it is counted in days, not weeks.
- Filing a notice of appeal where trial de novo is the remedy, or vice versa.
- Bringing no documentary proof of the amount of damages.
- Ignoring a small-claims counterclaim because "no answer is required."

## Verify before relying
- Pull verbatim RSMo 482.300-482.365, ch. 517 (especially 517.011), 512.180, 512.190, and the small claims court rules via `statute-lookup` (or Descrybe `search_laws_and_rules`).
- Check the local circuit's small claims procedures and forms.
- Recompute the trial de novo or appeal deadline from the actual judgment date.
- Legal information, not legal advice; recommend counsel or legal aid for high-stakes decisions.

## Related skills
- `mo-petition-drafting` - associate circuit petitions
- `mo-landlord-tenant-eviction` - rent and possession cases
- `mo-appeals-procedure` - on-the-record appeals
- `mo-deadline-calculator` - short post-judgment deadlines
- `mo-garnishment-and-execution` - collecting the judgment
