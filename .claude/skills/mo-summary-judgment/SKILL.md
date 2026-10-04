---
name: mo-summary-judgment
description: Drafts and opposes Missouri summary judgment under Rule 74.04 - statement of uncontroverted material facts, numbered responses with record cites, affidavits, ITT Commercial Finance burdens. Use for "summary judgment", "74.04", "statement of uncontroverted facts", "respond to their motion".
---

# Missouri Summary Judgment

Builds or defeats a Rule 74.04 motion using Missouri's strict numbered-paragraph format, where an improper response is treated as an admission.

## When to use
- Moving for summary judgment on a claim, counterclaim, or affirmative defense in Missouri state court
- Responding to an opponent's motion and statement of uncontroverted material facts
- Seeking more time for discovery before responding
- Not for: federal Rule 56 practice (use `federal-summary-judgment`); attacks limited to the face of the petition (use `mo-motion-to-dismiss`)

## Gather first
- The motion, statement of facts, and every exhibit (or, if moving, the full discovery record)
- The operative pleadings, including affirmative defenses actually pleaded
- Date the motion was served and any hearing date set

## Workflow
1. **Timing.** A claimant may move after the period stated in Rule 74.04(a) (verify); a defending party may move at any time (Rule 74.04(b) - verify). The response is due 30 days after service of the motion (Rule 74.04(c)(2) - verify); check local rules and any court order.
2. **Know the burden framework (ITT Commercial Finance Corp. v. Mid-America Marine Supply Corp., 854 S.W.2d 371 (Mo. banc 1993)).**
   - Claimant moving: must establish, with undisputed facts, every element of its claim, and (where pleaded) that affirmative defenses fail.
   - Defending party moving: may prevail by showing (a) facts negating any one element of the claimant's claim; (b) that the claimant, after adequate time for discovery, cannot produce evidence sufficient to allow a factfinder to find any one element; or (c) undisputed facts establishing each element of a properly pleaded affirmative defense.
   - A "genuine issue" exists when the record shows two plausible but contradictory accounts of the essential facts; the record is viewed in the light most favorable to the non-movant. Appellate review is de novo.
3. **Moving: the statement of uncontroverted material facts (Rule 74.04(c)(1) - verify).** Separately numbered paragraphs, one fact each, each with specific references to the pleadings, discovery, exhibits, or affidavits that prove it; attach the referenced materials. File the motion stating the legal basis, plus suggestions (memorandum) in support.
4. **Affidavits.** Must be made on personal knowledge, set forth facts that would be admissible in evidence, and show the affiant is competent (Rule 74.04(e) - verify). Conclusions and hearsay are disregarded. Sworn discovery responses, deposition excerpts, and authenticated documents qualify; unsworn statements and pleadings alone usually do not.
5. **Responding (Rule 74.04(c)(2) - verify).** Respond to each numbered paragraph in a document that restates each paragraph and then admits or denies it. Every denial must cite specific record references (discovery, exhibits, affidavits) showing a genuine dispute. A denial without record support, or no response, admits the fact. You may add your own numbered statement of additional material facts that defeat the motion.
6. **Need more discovery.** If you cannot yet present facts essential to opposing the motion, file an affidavit explaining what discovery is needed and why (verify Rule 74.04(f)); request denial or continuance.
7. **Reply.** The movant may reply to additional facts in the same numbered format (verify Rule 74.04(c)(3)).
8. **Partial summary judgment.** Interlocutory unless the court certifies under Rule 74.01(b) that there is no just reason for delay (verify); otherwise not appealable until final judgment.
9. **Hearing and judgment.** Judgment is entered if the record shows no genuine issue of material fact and the movant is entitled to judgment as a matter of law (Rule 74.04(c)(6) - verify). Ask for findings identifying the basis if useful for appeal.

## Output
- Moving: motion / statement of uncontroverted material facts (numbered, each cited) / suggestions in support (Intro, Facts, Standard, Argument per element or defense, Conclusion) / exhibit index
- Responding: response restating each paragraph with Admitted / Denied plus record cite / statement of additional material facts / suggestions in opposition / Rule 74.04(f) affidavit if needed
- Element map: | Element or defense | SUMF para. | Record cite | Disputed? | Counter-evidence |

## Pitfalls
- Responding with argument or "denied" without record citations - deemed admitted. This is the most common way pro se parties lose summary judgment in Missouri.
- Relying on your own pleading or unsworn statements to create a dispute.
- Affidavits with conclusions, speculation, or hearsay.
- Moving on an affirmative defense that was never pleaded.
- Missing the 30-day response deadline without seeking an extension.
- Treating a partial grant as immediately appealable.
- Citing exhibits that were never filed or attached to the response - the court reviews only what is in the summary-judgment record.

## Verify before relying
- Pull verbatim Rule 74.04 (all subdivisions) and Rule 74.01(b) via `statute-lookup` (or Descrybe `search_laws_and_rules`); subdivision references here need confirmation.
- Confirm ITT Commercial Finance remains controlling and check pin cites before quoting (CourtListener / Descrybe treatment).
- Recompute the response deadline from the actual service date.
- Legal information, not legal advice; recommend counsel or legal aid for high-stakes decisions.

## Related skills
- `elements-checklist-builder` - map elements to record evidence
- `mo-discovery-requests` - build the record before the motion
- `authentication-foundation-builder` - make exhibits admissible
- `quote-and-cite-verifier` - check record cites and quotations
- `federal-summary-judgment` - federal counterpart
