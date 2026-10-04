---
name: contract-breach-analyzer
description: Analyzes contract disputes under Missouri law - formation, terms, breach, defenses (statute of frauds, waiver, impossibility), limitations, and remedies. Use for "breach of contract", "they didn't pay", "is this contract enforceable", "verbal agreement", "sue for breach", or defending a contract claim.
---

# Contract Breach Analyzer

Tests a contract claim or defense element by element under Missouri common law, picks the right limitations period, and sizes the available remedies before anything is drafted.

## When to use
- Deciding whether a breach-of-contract count can be pleaded and proved
- Defending a contract suit (including collection suits on a written instrument or account)
- Checking enforceability of an oral, emailed, or partly written agreement
- Choosing between contract, quantum meruit/unjust enrichment, and fraud theories
- Not for: sales of goods (use `ucc-article-2-sales`); promissory notes and checks (use `ucc-article-3-negotiable-instruments`); consumer deception claims (use `mo-merchandising-practices-act`)

## Gather first
- The agreement itself (every writing, email, text, invoice, signed page) and who signed it
- What each side promised, what each side actually did, and the date of the first breach
- The loss claimed and how it is calculated (invoices, payments, lost profits records)

## Workflow
1. **Classify the transaction.** Goods (UCC Article 2), negotiable instrument (Article 3), lease of real property (landlord-tenant law plus contract), services/other (common law). Mixed deals: apply the predominant-purpose test and note it.
2. **Formation.** Offer, acceptance (mirror image at common law), consideration, mutual assent on essential terms, capacity, legality. Identify the moment and medium of acceptance.
3. **Enforceability screens.**
   - Statute of frauds: RSMo 432.010 (e.g., agreements not performable within one year, interests in land, promises to answer for another's debt; verify the full list). Missouri's credit-agreement statute bars a debtor from suing on, or defending with, a credit agreement (an agreement to lend, forbear, or extend credit) unless it is in a qualifying writing (RSMo 432.047 - read its signature and notice requirements). Statute of frauds is an affirmative defense that must be pleaded (Rule 55.08).
   - Parol evidence rule: integrated writing bars prior/contemporaneous inconsistent terms; ambiguity is a question of law for the court first.
   - Unconscionability, illegality, fraud in the inducement, duress, mistake.
4. **Elements of breach (Missouri).** (1) existence and terms of a contract; (2) plaintiff performed or tendered performance; (3) defendant breached; (4) damages. Keveney v. Missouri Military Academy, 304 S.W.3d 98, 104 (Mo. banc 2010). Map each element to a specific exhibit or testimony.
5. **Breach analysis.** Material vs. minor breach (materiality excuses the other side's further performance); anticipatory repudiation (must be clear and unequivocal); conditions precedent (pleaded generally, denied specifically). Implied covenant of good faith and fair dealing applies to discretion granted by the contract, not to add new terms.
6. **Defenses checklist.** Prior material breach by plaintiff; waiver or estoppel; modification or accord and satisfaction; payment; impossibility/impracticability/frustration; failure of a condition; statute of limitations; release. Each affirmative defense must be pleaded with facts.
7. **Limitations.** RSMo 516.110(1): ten years for an action upon a writing for the payment of money or property. RSMo 516.120(1): five years for other contract actions, express or implied. Sales of goods: four years (RSMo 400.2-725). Determine which applies; the writing must itself contain the promise to pay for the 10-year period. Hand off to `statute-of-limitations-checker` for accrual and tolling.
8. **Remedies.** Expectation damages (benefit of the bargain), reliance damages, restitution; consequential damages only if foreseeable at contracting and proved with reasonable certainty; duty to mitigate; liquidated damages enforceable only if a reasonable forecast and actual damages hard to estimate (penalties void). Specific performance for unique property where damages inadequate. Attorney fees only if the contract or a statute provides (American Rule). Prejudgment interest: RSMo 408.020 allows nine percent per annum where no other rate is agreed, on written contracts once due, and on accounts after due and demand of payment.
9. **Alternative counts.** Unjust enrichment/quantum meruit may be pleaded in the alternative, but generally cannot be recovered where an express contract covers the same subject.

## Output
- Element table: | Element | Facts | Evidence (exhibit/witness) | Strength (strong/contested/missing) |
- Defenses table: | Defense | Available to | Facts supporting | Must be pleaded? | Risk |
- Limitations line: period, statute, accrual date, last day to file (flag "recompute")
- Remedies estimate: category, amount, proof source, recoverable? (Y/N/uncertain)
- Recommended counts or defenses with one-sentence rationale each

## Pitfalls
- Suing on a contract without attaching or setting out the writing in the petition.
- Forgetting to plead statute of frauds, payment, release, or other Rule 55.08 defenses - unpleaded affirmative defenses are waived.
- Claiming lost profits without records showing them with reasonable certainty.
- Assuming the 10-year statute applies to every written contract; it requires a written promise to pay money or property.
- Asking for attorney fees with no fee-shifting clause or statute.
- Ignoring mitigation; unmitigated losses are cut from the award.

## Verify before relying
- Pull verbatim text of RSMo 432.010, 432.047, 516.110, 516.120, 408.020 and Rule 55.08 via `statute-lookup` (or Descrybe `search_laws_and_rules`).
- Check Keveney and any other case used is still good law (CourtListener / Descrybe treatment) and pin-cite the page used.
- Recompute every limitations date from the actual breach date.
- Legal information, not legal advice; recommend counsel or legal aid for high-stakes decisions.

## Related skills
- `elements-checklist-builder` - full proof matrix per count
- `mo-petition-drafting` - turn the element table into a fact-pleaded count
- `mo-answer-affirmative-defenses` - plead the defenses identified here
- `statute-of-limitations-checker` - accrual and tolling detail
- `damages-calculator` - compute the remedy figures
- `settlement-and-demand-letters` - demand before suit
