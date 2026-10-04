---
name: court-document-formatting
description: Formats Missouri and federal court filings - captions, titles, numbered paragraphs, signature blocks, certificates of service, privacy redaction, exhibits, font and page rules, local rules. Use for "format my motion", "caption", "certificate of service", "signature block", or "will the clerk accept this".
---

# Court Document Formatting

Makes a filing look and function like what the clerk and judge expect: correct caption, structure, signature, service certificate, redactions, and exhibits — so it is not rejected or discounted on form.

## When to use
- Finalizing any pleading, motion, brief, notice, or proposed order before the user files it
- Converting a draft into the format of a specific court (circuit, associate circuit, Court of Appeals, E.D./W.D. Mo., 8th Cir.)
- Building certificates of service, exhibit cover sheets, or proposed orders
- Not for: substantive content (use the drafting skills); appellate brief section requirements (use `appellate-brief-writer`); citation style (use `legal-citation-formatter`)

## Gather first
- Court name, county/division, case number, judge/division number, and exact party names as they appear in the existing caption
- Document type and what relief it seeks; whether it is filed on paper or through e-filing
- Who must be served and how (e-filing system, mail, email by agreement, hand delivery)

## Workflow
1. **Pull the local rules first.** Missouri: the Supreme Court Rules plus the circuit's local rules (court website). Federal: the FRCP/FRAP plus the district's local rules (E.D. Mo. or W.D. Mo.) and any judge-specific requirements. Local rules control page limits, memorandum requirements, proposed orders, and courtesy copies.
2. **Caption.**
   - Missouri trial court: "IN THE CIRCUIT COURT OF [COUNTY] COUNTY, MISSOURI" (add division / associate circuit as used on the docket); parties as styled in the petition; "Case No." Copy the existing caption exactly after the first filing.
   - Federal: "UNITED STATES DISTRICT COURT FOR THE [EASTERN/WESTERN] DISTRICT OF MISSOURI" and division; caption must name the court, title, file number, and Rule 7(a) designation; the complaint names all parties, later filings may use the first party and "et al." (FRCP 10(a)).
   - Appellate writs in Missouri use "State ex rel. [Relator] v. [Respondent]".
3. **Title.** Specific and descriptive: "Plaintiff's Motion to Compel Answers to First Interrogatories," not "Motion." Include "and Suggestions in Support" or "Memorandum in Support" when combined, as local practice requires (Missouri state courts commonly use "Suggestions"; federal courts "Memorandum").
4. **Body structure.** Numbered paragraphs for pleadings, each limited as far as practicable to a single set of circumstances (FRCP 10(b); Missouri fact pleading follows the same convention). Separate counts for separate claims. Motions state the rule relied on, the grounds with particularity, and the relief sought (FRCP 7(b)(1)). End with "WHEREFORE" prayer in Missouri pleadings.
5. **Typography (unless local rules differ).** Letter-size paper, readable 12-13 point font, double-spaced body, 1-inch margins, page numbers. Appellate: Missouri Rule 84.06 and FRAP 32 set specific font and word limits — follow them exactly.
6. **Signature block.** Every filing signed by the self-represented party with name, mailing address, email, and telephone (FRCP 11(a); Missouri Rule 55.03(a) — verify). Signing certifies the Rule 11 / Rule 55.03(c) representations (proper purpose, warranted by law, factual support). Use "Plaintiff, pro se" or "Self-Represented."
7. **Verification / affidavit** when a rule or statute requires a verified pleading (e.g., certain petitions, TRO requests): sworn before a notary or under penalty of perjury as the court allows (federal: 28 U.S.C. 1746 declaration). Confirm Missouri's accepted form for the specific filing.
8. **Certificate of service.** After the signature: "I certify that on [date] a copy of the foregoing was served on [name, role] by [method: court e-filing system / U.S. Mail to address / email by consent]." Required for papers served after the original process (FRCP 5(d)(1); Missouri Rule 43.01). Service of the initial petition/complaint is by summons, not certificate.
9. **Privacy redaction.** Federal: redact to last four digits of SSN and financial account numbers, birth year only, and minors' initials (FRCP 5.2). Missouri: confidential identifiers are kept out of public filings and supplied through the court's confidential information form (verify the current operating rule and form). Also check for sealed/confidential case types (juvenile, protection orders).
10. **Exhibits.** Label consistently (Exhibit A, B or 1, 2), reference each in the text, attach a short exhibit index, and file as separate attachments when e-filing. Do not attach originals.
11. **Proposed order.** Many judges want one; draft it with a caption, the relief in plain terms, and a signature line for the judge.
12. **Final checklist pass**, then hand to the user to file. Never file or serve on their behalf.

## Output
- Formatted document skeleton: caption block, title, body headings, WHEREFORE/relief, signature block, certificate of service
- Checklist: | Item | Rule source | Done |
- Exhibit index and proposed order, if needed

## Pitfalls
- Caption or case number not matching the docket — misfiled or rejected
- Unsigned filings, or signature block missing contact information
- No certificate of service, or certifying service that did not happen
- Unredacted SSNs, birth dates, account numbers, or minors' names
- Ignoring local page limits, memorandum requirements, or judge-specific procedures
- Combining unrelated requests in one motion when local rules require separate motions

## Verify before relying
- Pull current text of FRCP 5, 5.2, 7, 10, 11; Missouri Rules 43.01, 55.03, 84.06; and the applicable local rules via `statute-lookup` (or Descrybe `search_laws_and_rules`) and court websites.
- Confirm the due date from the actual service/entry date before finalizing.
- Legal information, not legal advice.

## Related skills
- `legal-citation-formatter` — citation form inside the document
- `appellate-brief-writer` — appellate brief sections and certificates
- `lawmind-god-drafter` — companion documents a filing requires
- `filing-followup` — track whether the document was filed
