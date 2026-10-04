---
name: irac-analysis
description: Produces a structured Issue/Rule/Application/Conclusion analysis of one legal question, with the rule drawn from verified authority and the facts applied element by element. Use for "IRAC this", "analyze this issue", "does the law support my position", "apply the law to my facts", or a brief argument section.
---

# IRAC Analysis

Disciplined analysis of a single legal question: state the precise issue, the governing rule from verified authority, apply it fact by fact, and reach a qualified conclusion.

## When to use
- One defined question needs a reasoned answer ("Was the stop supported by reasonable suspicion?", "Is my claim time-barred?").
- Building the argument section of a motion, brief, or memo.
- Checking whether a draft argument actually connects the law to the facts.
- Not for: finding all issues in a fact pattern (use `legal-issue-spotter`) or a full research memo (use `legal-memo-writer`).

## Gather first
- The exact question and which side the user is on.
- The jurisdiction and court (Missouri state, federal district, 8th Circuit) — the rule depends on it.
- The relevant facts and the documents or testimony that prove them.

## Workflow
1. **Issue.** Frame it as a yes/no question that joins law and facts: "Under [rule], does [key fact] establish [element]?" Split compound issues into separate IRACs. Identify threshold issues (jurisdiction, standing, limitations, preservation) and analyze them first.
2. **Rule.** Build the rule in layers, highest authority first:
   - Constitution, statute, or court rule text (verbatim, via `statute-lookup`).
   - The controlling test from the highest binding court (Supreme Court of Missouri for Missouri law; U.S. Supreme Court and 8th Circuit for federal law in Missouri federal courts).
   - Elements or factors, burden of proof, who bears it, and the standard of review if on appeal.
   - Exceptions and defenses that limit the rule.
   Mark each source binding or persuasive (see `precedent-hierarchy-analyzer`).
3. **Rule explanation.** For each element, describe how courts have applied it: one or two cases where it was met and where it was not, with the facts that mattered. Use only cases you have verified.
4. **Application.** Go element by element. For each: the specific facts (with record or exhibit cite), the analogy to or distinction from the precedent, and the evidence that proves it. Then state the other side's best counter-argument and answer it. Do not skip an element because it seems obvious.
5. **Conclusion.** Give a qualified answer (likely / probably not / close question) and the reason. Identify the one fact or authority that would most change the result.
6. **Check the chain.** Every conclusion must trace to a stated rule and a stated fact. Delete any sentence that does neither.

## Output
```
ISSUE: [one sentence question]
SHORT ANSWER: [likely yes/no + one-sentence reason]
RULE: [text of law; controlling test; elements; burden] — each with citation and [binding]/[persuasive]
RULE EXPLANATION: [how courts applied each element]
APPLICATION:
  Element 1 — facts / precedent comparison / counter-argument / response
  Element 2 — ...
CONCLUSION: [qualified answer; key uncertainty]
OPEN QUESTIONS / FACTS NEEDED:
```
For a brief, convert to CRAC (conclusion first) with a persuasive point heading.

## Pitfalls
- Stating a rule from memory or from a secondary summary instead of the actual text and controlling case.
- Using the wrong jurisdiction's test, or the federal standard in a Missouri state court (and vice versa).
- Conclusory application: restating the rule with the party's name inserted instead of matching specific facts to each element.
- Ignoring the burden of proof or standard of review, which often decides close questions.
- Skipping threshold issues; a strong merits analysis is useless if the claim is unpreserved or time-barred.
- Citing a case for a proposition it does not hold, or quoting dicta as the holding.

## Verify before relying
- Pull verbatim text of every statute/rule cited via `statute-lookup` (or Descrybe `search_laws_and_rules`); check case law is still good law (CourtListener / Descrybe treatment) before citing.
- Recompute any deadline from the actual service/entry date.
- Legal information, not legal advice; recommend counsel/legal aid for high-stakes decisions.

## Related skills
- `elements-checklist-builder` — the element list that drives the Application step.
- `standard-of-review-finder` — the review standard for appellate IRACs.
- `quote-and-cite-verifier` — check every quotation and pin cite in the finished analysis.
- `lawmind-legal-research` — retrieve the authority for the Rule step.
- `lawmind-strategy-engine` — adversarial testing of the conclusion.
