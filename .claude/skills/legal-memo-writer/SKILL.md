---
name: legal-memo-writer
description: Writes objective legal research memos - question presented, brief answer, facts, discussion with verified citations, counterarguments, conclusion - for Missouri and federal issues. Use for "write a legal memo", "research memo", "memo on whether", or research before drafting a motion.
---

# Legal Memo Writer

Produces an objective, predictive research memo: what the law is, how a court is likely to apply it to these facts, and how confident that prediction is — with every authority verified, so the memo can safely feed a motion or brief.

## When to use
- the user needs to know whether a claim, defense, or motion is viable before drafting it
- Summarizing the law on a question for the case file
- Comparing Missouri and federal law on an issue
- Not for: persuasive filings (use `appellate-brief-writer` or the motion skills); quick single-issue analysis (use `irac-analysis`); finding sources in the LawMind library (use `lawmind-legal-research`)

## Gather first
- The precise question, the jurisdiction/court, and the procedural posture (pre-suit, motion to dismiss, summary judgment, appeal)
- The relevant facts, with source documents, including bad facts
- Any authority already found, and the deadline the memo serves

## Workflow
1. **Frame the question.** One sentence per issue combining the legal rule and the key facts: "Under [law], does [legal standard] when [key facts]?" Split compound questions.
2. **Research in hierarchy order.** Constitution and statutes/rules (verbatim via `statute-lookup`), then controlling cases (Missouri Supreme Court, then the Court of Appeals district; for federal issues, U.S. Supreme Court and 8th Circuit), then persuasive authority. Use `precedent-hierarchy-analyzer` for binding vs. persuasive.
3. **Extract the rule.** State elements or factors with their source; note burden of proof and standard (preponderance, clear and convincing, beyond reasonable doubt) and the procedural standard (e.g., facts taken as true on a motion to dismiss).
4. **Apply objectively.** Element by element: facts that satisfy it, facts that cut against it, analogous and distinguishable cases. Mark facts that are disputed or unproven.
5. **Counterarguments.** State the strongest opposing argument and how a court would likely resolve it. Do not omit adverse controlling authority.
6. **Predict.** Give a calibrated conclusion (likely / uncertain / unlikely) with the reason and what additional facts or authority would change it.
7. **Verify every citation** before finalizing: existence, correct reporter/pin cite, quotation accuracy, and treatment (not overruled, statute not amended). Drop anything that cannot be confirmed; say "authority not located" rather than guess.
8. **Next steps.** List the practical actions the analysis supports (motion to file, evidence to obtain, deadline to calendar).

## Output
Memo headings, in order:
- **To / From / Date / Re**
- **Question(s) Presented** — one per issue
- **Brief Answer(s)** — yes/no/probably plus one- to three-sentence reason
- **Statement of Facts** — objective, with source cites; flag assumptions
- **Discussion** — one subsection per issue: Rule (with citations) -> Application -> Counterarguments -> Mini-conclusion
- **Conclusion** — overall prediction and confidence
- **Next Steps / Open Questions**
- **Authorities Verified** — table: | Authority | Pin cite | Verified via | Treatment checked (date) |

## Pitfalls
- Advocacy disguised as analysis — leaving out adverse authority or bad facts
- Questions presented so abstract they could fit any case, or brief answers that never commit
- Citing a case for a proposition from a headnote or summary without reading the opinion
- Using out-of-state or federal authority as if binding in Missouri state court
- Missing the procedural standard (what a court can consider at this stage)
- Unverified or hallucinated citations; outdated statute versions

## Verify before relying
- Pull verbatim text of every statute/rule cited via `statute-lookup` (or Descrybe `search_laws_and_rules`); check case law is still good law (CourtListener / Descrybe treatment) before citing.
- Recompute any deadline mentioned from the actual service/entry date.
- Legal information, not legal advice; recommend counsel/legal aid for high-stakes decisions.

## Related skills
- `irac-analysis` — single-issue structured analysis inside the Discussion
- `good-law-checker` / `quote-and-cite-verifier` — citation verification
- `lawmind-legal-research` — retrieve authority from the LawMind library
- `lawmind-strategy-engine` — turn the memo into strategy
- `legal-citation-formatter` — final citation form
