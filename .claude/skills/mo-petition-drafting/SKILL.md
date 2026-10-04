---
name: mo-petition-drafting
description: Drafts and audits Missouri state-court petitions under Rule 55 fact pleading - caption, parties, jurisdiction and venue facts, separate counts per claim, element-by-element ultimate facts, and prayer. Use for "draft a petition", "file suit in Missouri circuit court", "is my petition sufficient", "add a count".
---

# Missouri Petition Drafting

Builds a Missouri circuit-court petition that pleads ultimate facts for every element of every count, so it survives a Rule 55.27(a)(6) motion and supports later summary judgment and trial.

## When to use
- Starting a new civil action in a Missouri circuit or associate circuit division
- Reviewing or amending an existing petition (adding counts, curing a dismissal)
- Converting a federal-style "notice pleading" complaint into Missouri fact pleading
- Not for: a federal complaint (use `federal-complaint-pleading`); full companion-filing bundles (use `lawmind-god-drafter`)

## Gather first
- Each claim you intend to bring and the facts (who, what, when, where) supporting each element
- Each defendant's correct legal name and type (individual, corporation, LLC, government entity) and where they reside or do business
- Key dates (injury, breach, discovery of harm) to check limitations, and any written contract or instrument the claim rests on

## Workflow
1. **Pick the court and confirm jurisdiction/venue.** Missouri circuit courts have general subject-matter jurisdiction (Mo. Const. art. V, sec. 14). Plead facts for personal jurisdiction and venue (venue statute is RSMo 508.010 - verify the subsection that fits: tort, contract, corporate defendant). See `jurisdiction-and-venue-analyzer`.
2. **Check limitations before drafting.** Run `statute-of-limitations-checker`; an action is commenced by filing the petition (Rule 53.01).
3. **Caption.** "IN THE CIRCUIT COURT OF ____ COUNTY, MISSOURI", division if known, plaintiff v. defendant(s) with service addresses or "Serve:" blocks for each defendant, "Case No. ____", and the document title "PETITION" (add "FOR DAMAGES", "FOR DECLARATORY JUDGMENT", etc.).
4. **Parties paragraph(s).** Identity, capacity, residence/principal place of business, registered agent for entities.
5. **Jurisdiction and venue paragraph(s).** Facts, not conclusions (where the conduct occurred, where defendant resides).
6. **Common facts.** Numbered paragraphs, one fact per paragraph, chronological, each stated as an ultimate fact (Rule 55.05 requires "a short and plain statement of the facts showing that the pleader is entitled to relief" - verify current wording).
7. **Counts.** One count per claim and per transaction or occurrence (Rule 55.11 - verify). Each count: heading ("COUNT I - Breach of Contract - against Defendant X"), incorporate prior paragraphs by number, then a paragraph for each element pleaded with specific facts. Build the element list with `elements-checklist-builder`.
8. **Special pleading.** Fraud and mistake: plead circumstances with particularity (verify Rule 55.15). Claims on a written instrument: attach or set out the instrument. Government defendants: plead the sovereign-immunity waiver or exception (see `sovereign-and-official-immunity-mo`).
9. **Prayer (wherefore clause) per count.** For unliquidated damages, Missouri bars stating a dollar figure except to establish jurisdictional authority; pray for "damages that are fair and reasonable" (Rule 55.05 / RSMo 509.050 - verify). Add costs, interest if allowed, and any equitable relief. Punitive damages have separate statutory pleading limits (RSMo 510.261 et seq. - verify before pleading).
10. **Signature block.** Self-represented party signs with name, address, phone, and email; signing certifies the Rule 55.03 representations (good-faith factual and legal basis).
11. **Companion filings.** Civil cover sheet/information form required by the circuit, summons request for each defendant, filing fee or poor-person application (`mo-poor-person-filing`), and service instructions (`mo-service-of-process`).

## Output
- Full petition draft in this order: Caption / Introduction / Parties / Jurisdiction and Venue / Facts Common to All Counts / Count I... / Prayer per count / Signature block / Verification (only if required for the claim type)
- Element-coverage table: | Count | Element | Paragraph no(s). | Evidence source | Gap? |
- List of exhibits to attach and companion filings needed

## Pitfalls
- Legal conclusions ("defendant was negligent") without underlying facts are disregarded under fact pleading; Twombly/Iqbal does not govern Missouri courts, but Missouri's standard is stricter on facts, not looser.
- Combining multiple claims or defendants in one count invites a motion to dismiss or to make more definite.
- Putting a dollar amount in the prayer for unliquidated damages.
- Suing the wrong entity name, a non-suable department, or omitting a necessary party.
- Pleading private information unnecessarily; follow redaction rules for Social Security and account numbers.
- Overpleading weak counts - each must satisfy Rule 55.03 or risk sanctions.
- Filing without checking for a pre-suit requirement (notice of claim to a government entity, administrative exhaustion, contractual arbitration clause).
- Forgetting that an amended petition supersedes the original - restate every count and fact you still rely on.

## Verify before relying
- Pull verbatim text of Rules 53.01, 55.03, 55.05, 55.11, 55.15 and RSMo 508.010 / 509.050 via `statute-lookup` (or Descrybe `search_laws_and_rules`); confirm subsections.
- Check any case law used for elements is still good law (CourtListener / Descrybe treatment).
- Check the local circuit's filing requirements (cover sheet, e-filing, number of copies).
- Legal information, not legal advice; recommend counsel or legal aid for high-stakes decisions.

## Related skills
- `elements-checklist-builder` - element lists for each count
- `mo-motion-to-dismiss` - test the draft against the likely attack
- `mo-service-of-process` - get the petition served
- `lawmind-god-drafter` - full filing bundle with companions
- `court-document-formatting` - caption, signature, certificate formats
