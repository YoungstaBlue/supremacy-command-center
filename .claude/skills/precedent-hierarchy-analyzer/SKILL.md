---
name: precedent-hierarchy-analyzer
description: Sorts authority into binding versus persuasive for Missouri state courts, federal courts in Missouri, the 8th Circuit, and the U.S. Supreme Court, and builds arguments to distinguish or follow cases. Use for "is this case binding", "which court controls", "distinguish this case", or conflicting cases.
---

# Precedent Hierarchy Analyzer

Determines how much weight each case or authority carries in the specific court where the argument will be made, and how to follow, distinguish, or limit it.

## When to use
- Deciding whether a case the other side cited actually binds the judge.
- Choosing which of several cases to lead with.
- Handling conflicting appellate decisions, or a federal decision on a Missouri-law question (or vice versa).
- Distinguishing an adverse case on its facts or reasoning.
- Not for: checking whether a case has been overruled (use `good-law-checker`).

## Gather first
- The court hearing the argument: Missouri associate circuit / circuit court (and which appellate district covers it), Missouri Court of Appeals, Supreme Court of Missouri, U.S. District Court (E.D. or W.D. Mo.), 8th Circuit.
- Whether the issue is one of Missouri law or federal law.
- The full citations of the cases in play (court and year matter).

## Workflow
1. **Classify the question:** Missouri law (state statutes, common law, Missouri Constitution) or federal law (U.S. Constitution, federal statutes, federal rules).
2. **Missouri law in Missouri state courts:**
   - Supreme Court of Missouri decisions are controlling in all other Missouri courts (Mo. Const. art. V, § 2).
   - Missouri Court of Appeals has three districts (Eastern, Western, Southern). Trial courts follow court of appeals decisions; when districts conflict and the Supreme Court has not resolved it, confirm how courts in your district handle the conflict and lead with your own district's cases. Confirm which district covers your county.
   - Court of appeals opinions vacated by a grant of transfer to the Supreme Court are not authority; cite the Supreme Court opinion.
   - Unpublished memorandum decisions and orders (e.g., under Rule 84.16(b) in civil appeals) are not precedent and should not be cited as authority — verify the current rule text.
3. **Federal law in Missouri state courts:** U.S. Supreme Court decisions on federal law bind. Lower federal court decisions, including the 8th Circuit, are generally persuasive only in state court, though often given significant weight. Missouri courts may give the Missouri Constitution a broader reading than its federal counterpart, but often construe parallel provisions coextensively — check for Missouri cases on the point.
4. **Federal law in federal courts in Missouri:** U.S. Supreme Court, then published 8th Circuit opinions, bind the district courts. One 8th Circuit panel generally cannot overrule another; only the court en banc (or the Supreme Court) can. District court opinions bind no one, including the same court. Unpublished 8th Circuit opinions are not precedent (check 8th Cir. R. 32.1A and FRAP 32.1 for citation rules).
5. **Missouri law in federal court:** Federal courts apply Missouri substantive law as the Supreme Court of Missouri has declared it (Erie R.R. Co. v. Tompkins, 304 U.S. 64 (1938)). Absent a controlling decision, the federal court predicts how that court would rule, often looking to Missouri Court of Appeals decisions. An 8th Circuit prediction of Missouri law does not bind Missouri state courts.
6. **Persuasive authority ranking** (when nothing binds): Supreme Court of Missouri dicta → Missouri Court of Appeals → 8th Circuit → other federal circuits and states with similar statutes → treatises and Restatements. Note that Missouri courts often follow federal interpretations when a Missouri rule is patterned on a federal rule, but are not required to.
7. **Holding versus dicta.** Isolate the holding: the rule necessary to the result on the facts presented. Statements beyond that are dicta and persuasive only.
8. **Distinguishing a binding adverse case.** Identify (a) material factual differences that the case's own reasoning treats as important, (b) a different procedural posture or standard of review, (c) a different statute or version, (d) later authority narrowing it. Explain why the distinction matters under the case's reasoning, not just that facts differ.
9. **Following a favorable case.** Show that the material facts match and the reasoning applies with equal or greater force.

## Output
| Case | Court / year | Issue type | Binding here? | Holding (one line) | Use: follow / distinguish / limit | Reason |
|---|---|---|---|---|---|---|

Then a short **argument plan**: lead authority, supporting authority, adverse authority and how each is handled.

## Pitfalls
- Telling a Missouri trial judge an 8th Circuit case "requires" a result on federal law; it is persuasive in state court.
- Citing a court of appeals opinion that was transferred and vacated, or citing a memorandum decision as precedent.
- Relying on a federal case to define Missouri law when a Missouri appellate case is directly on point.
- Distinguishing a case on facts its reasoning does not treat as relevant; judges see through it.
- Ignoring adverse binding authority; candor obligations apply to pro se litigants too.
- Treating dicta as holding.

## Verify before relying
- Pull verbatim text of every statute/rule cited via `statute-lookup` (or Descrybe `search_laws_and_rules`); check case law is still good law (CourtListener / Descrybe treatment) before citing.
- Confirm the publication status and subsequent history of every case.
- Legal information, not legal advice; recommend counsel/legal aid for high-stakes decisions.

## Related skills
- `good-law-checker` — confirm each case is still good law.
- `legal-citation-formatter` — cite each authority correctly, with court and year visible.
- `irac-analysis` — use the ranked authority in the Rule step.
- `lawmind-legal-research` — find Missouri cases on point.
