---
name: federal-summary-judgment
description: Drafts and opposes federal summary judgment under FRCP 56 - burden shifting, genuine dispute of material fact, admissible evidence, declarations, Rule 56(d), and E.D./W.D. Mo. statements of fact. Use for "summary judgment" in federal court, "Rule 56", "statement of material facts", or "oppose their MSJ".
---

# Federal Summary Judgment

Wins or survives Rule 56 by organizing admissible evidence around each material fact, in the exact format the district's local rule demands.

## When to use
- Defendant or plaintiff moved for summary judgment in federal court
- Deciding whether to move for summary judgment after discovery
- Qualified-immunity summary-judgment motions
- Not for: Missouri state-court summary judgment under Rule 74.04 — use `mo-summary-judgment`

## Gather first
- The motion, memorandum, statement of facts, and every exhibit; the date served
- The scheduling order (dispositive-motion deadline, discovery cutoff)
- The plaintiff's own evidence: declarations, deposition transcripts, documents, video, discovery responses

## Workflow
1. **Standard (Rule 56(a)).** Summary judgment is granted only if there is no genuine dispute as to any material fact and the movant is entitled to judgment as a matter of law.
   - Material: might affect the outcome under the governing law. Genuine: a reasonable jury could return a verdict for the nonmovant. Anderson v. Liberty Lobby, Inc., 477 U.S. 242 (1986).
   - Burden: movant shows the absence of a genuine dispute (or that the nonmovant lacks evidence on an element it must prove); the nonmovant must then designate specific facts showing a genuine issue for trial. Celotex Corp. v. Catrett, 477 U.S. 317 (1986). Metaphysical doubt is not enough. Matsushita Elec. Indus. Co. v. Zenith Radio Corp., 475 U.S. 574 (1986).
   - Evidence and reasonable inferences are viewed in the nonmovant's favor; courts do not weigh credibility. Tolan v. Cotton, 572 U.S. 650 (2014). Exception: a version of events blatantly contradicted by the record (e.g., unchallenged video) need not be credited. Scott v. Harris, 550 U.S. 372 (2007).
2. **Timing.** Unless a local rule or order says otherwise, a motion may be filed at any time until 30 days after the close of all discovery (Rule 56(b)). The response deadline is set by local rule or order — check it immediately; it is short.
3. **Local-rule statements of fact.** Both Missouri federal districts require a separately numbered statement of material facts with record citations, and a response that admits or disputes each paragraph with citations (verify the current E.D. Mo. Local Rule 4.01 and W.D. Mo. Local Rule 56.1 text). Facts not specifically controverted with record citations may be deemed admitted. This is where most pro se oppositions lose.
4. **Evidence that counts (Rule 56(c)).**
   - Cite particular parts of materials: depositions, documents, ESI, affidavits or declarations, stipulations, admissions, interrogatory answers.
   - Affidavits/declarations must be made on personal knowledge, set out facts admissible in evidence, and show competence (56(c)(4)). An unsworn declaration signed under penalty of perjury in the form of 28 U.S.C. 1746 substitutes for a notarized affidavit.
   - A party may object that cited material cannot be presented in admissible form (56(c)(2)).
   - A sworn (verified) complaint may function as a declaration to the extent it meets 56(c)(4) — verify Eighth Circuit authority before relying on this.
   - Conclusory or speculative statements, and declarations contradicting prior deposition testimony without explanation, are disregarded.
5. **Rule 56(d).** If the nonmovant cannot present essential facts, show by affidavit or declaration the specific facts sought, why they are essential, and why they could not be obtained; the court may defer, deny, or allow discovery.
6. **Opposition structure.** (a) Response to movant's statement, paragraph by paragraph: "Admitted," "Denied — see Ex. __ at __," or "Admitted in part"; (b) Statement of additional material facts precluding summary judgment, numbered, with citations; (c) Memorandum: standard, element-by-element argument showing disputes, legal errors in movant's theory, 56(d) request if applicable.
7. **Moving for summary judgment.** Only where the record on an element is truly one-sided. Build the statement of facts from undisputed documents and the opponent's own admissions; avoid credibility-dependent facts.
8. **Court's options (56(e)-(g)).** If a fact is not properly addressed, the court may give an opportunity to correct, consider it undisputed, grant the motion if supported, or issue another order; it may grant summary judgment for a nonmovant after notice; it may enter an order stating material facts not genuinely in dispute.
9. **Afterward.** Grant of full summary judgment is a final judgment (appeal under FRAP 4(a)); partial grants usually are not final absent Rule 54(b) certification. Standard of review on appeal is de novo.

## Output
- Response-to-statement table:

| Movant para. | Admit/Deny | Record cite (Ex., page:line) | Explanation |
|---|---|---|---|

- Statement of additional material facts (numbered, each with a cite)
- Memorandum outline with element-by-element dispute map
- Declaration draft(s) in 28 U.S.C. 1746 form limited to personal knowledge

## Pitfalls
- Responding with argument instead of paragraph-by-paragraph admissions/denials with record cites (facts deemed admitted)
- Relying on the complaint's allegations without sworn evidence
- Declarations full of opinion, hearsay, or legal conclusions
- Failing to request Rule 56(d) relief before the ruling when discovery was cut short
- Missing the local-rule response deadline or page limits
- Ignoring video evidence that contradicts your account

## Verify before relying
- Pull current FRCP 56, 28 U.S.C. 1746, and the district's local rule on summary judgment verbatim via `statute-lookup` or Descrybe `search_laws_and_rules`.
- Check Eighth Circuit treatment of any case relied on (CourtListener / Descrybe).
- Recompute the response deadline from the actual service date and any court order.
- Legal information, not legal advice.

## Related skills
- `qualified-immunity-analyzer` — QI at summary judgment
- `federal-civil-discovery` — building the record; Rule 56(d)
- `authentication-foundation-builder` — making exhibits admissible
- `evidence-timeline-builder` — source-cited facts for the statement
- `mo-summary-judgment` — state-court counterpart
