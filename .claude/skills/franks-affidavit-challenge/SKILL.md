---
name: franks-affidavit-challenge
description: Builds a Franks v. Delaware challenge to a search or arrest warrant affidavit - deliberate or reckless false statements and material omissions, the substantial preliminary showing, and the corrected-affidavit test. Use for "Franks hearing", "lying affidavit", "officer left out facts", "warrant affidavit false".
---

# Franks Affidavit Challenge

Structures an attack on the truthfulness of a warrant affidavit so the request clears the high threshold for an evidentiary hearing and shows that the corrected affidavit lacks probable cause.

## When to use
- A warrant affidavit contains statements the defendant can show are false, or leaves out facts that undercut probable cause.
- Preparing a motion for a Franks hearing in Missouri state court or federal court (E.D./W.D. Mo.).
- Evaluating a 1983 claim that an officer obtained a warrant through falsehoods.
- Not for: a facial "four corners" probable-cause challenge with no falsity claim (use `fourth-amendment-analyzer`).

## Gather first
- The complete affidavit, warrant, application, and return - exact wording matters.
- The proof of falsity: reports, recordings, CAD/dispatch logs, informant records, prior statements, records contradicting the affiant.
- Who the affiant was and what the affiant knew at the time (falsity by an informant alone is not enough).

## Workflow
1. **Know the standard (Franks v. Delaware, 438 U.S. 154 (1978)).** A defendant is entitled to an evidentiary hearing only on a substantial preliminary showing that:
   - the affiant included a false statement knowingly and intentionally, or with reckless disregard for the truth; and
   - the false statement was necessary to the finding of probable cause.
   The affidavit is presumed valid. Allegations of negligence or innocent mistake are insufficient. The challenge must point to the specific portions claimed false, be accompanied by a statement of supporting reasons, and include offers of proof - affidavits or otherwise reliable witness statements, or an explanation of their absence.
2. **Itemize each challenged statement.** For every sentence: what the affidavit says, what the truth is, the source proving it, and why the affiant knew or recklessly disregarded it.
3. **Omissions.** Federal circuits, including the 8th Circuit, extend Franks to omissions made with intent to mislead or reckless disregard of whether they make the affidavit misleading. Show the omitted fact, how the affiant knew it, and why a reasonable affiant would know a judge would want it (e.g., informant's unreliability, contradictory evidence, exculpatory results). Find and cite a controlling 8th Circuit or Missouri case before relying on omission doctrine.
4. **Mental state evidence.** Recklessness can be inferred where the affiant had obvious reasons to doubt the truth of the statement, or where the omitted fact was clearly critical. Pattern evidence (same affiant, same boilerplate) helps.
5. **Materiality - the corrected affidavit test.** Strike every false statement and insert every omitted fact; then ask whether the remaining content still establishes probable cause under the totality of the circumstances. If yes, the challenge fails no matter how false the statement. Draft the corrected affidavit in full.
6. **Informant layer.** Franks reaches only the affiant's falsity or recklessness, not the informant's. Attack the affiant's representations about the informant (track record, corroboration, basis of knowledge) instead.
7. **Hearing burden.** If a hearing is granted, the defendant must prove perjury or reckless disregard by a preponderance of the evidence; if proven and the corrected affidavit lacks probable cause, the warrant is voided and its fruits excluded. Good-faith reliance under United States v. Leon, 468 U.S. 897 (1984) does not save a warrant procured by knowing or reckless falsity.
8. **Missouri procedure.** Raise through a pretrial motion to suppress under RSMo 542.296 and request the evidentiary hearing expressly; Missouri courts apply the Franks framework. In federal court, file before the pretrial-motion deadline (Fed. R. Crim. P. 12(b)(3)(C)).

## Output
- Franks table: | Affidavit paragraph | Statement or omission | Truth | Proof (exhibit) | Mental state evidence | Material? |
- The "corrected affidavit" - full text with strikes and insertions shown.
- Motion outline: Introduction; Facts; Standard (Franks); Specific false statements; Specific omissions; Offer of proof (attached affidavits/exhibits); Corrected affidavit lacks probable cause; Request for evidentiary hearing; Relief (suppress all fruits).

## Pitfalls
- Conclusory allegations ("the officer lied") without an offer of proof - hearing denied.
- Challenging immaterial details; if probable cause survives the correction, the motion fails.
- Attacking the informant's honesty rather than the affiant's.
- Omitting a sworn declaration or other reliable proof - attach it or explain why it cannot be obtained.
- Missing the pretrial motion deadline; Franks issues are generally waived if not raised before trial.
- Overlooking the warrant's other paragraphs: courts read the corrected affidavit as a whole, so independent corroboration can sink the motion.
- Waiting to request the hearing at trial; ask for it in the written motion and again at the suppression hearing.
- Filing a 1983 Franks-type claim without addressing qualified immunity and the Heck bar.

## Verify before relying
- Pull verbatim RSMo 542.296 and Fed. R. Crim. P. 12 via `statute-lookup` (or Descrybe `search_laws_and_rules`).
- Read Franks itself for the exact quoted standard; locate and verify current 8th Circuit and Missouri cases on omissions and recklessness before citing (CourtListener / Descrybe treatment).
- Recompute the motion deadline from the scheduling order.
- Legal information, not legal advice; a Franks hearing is high-stakes - seek counsel or the public defender.

## Related skills
- `fourth-amendment-analyzer` - full search-and-seizure framework and remedies.
- `mo-motion-to-suppress` - Missouri motion structure and hearing preparation.
- `quote-and-cite-verifier` - match every quoted affidavit line to the source.
- `malicious-prosecution-false-arrest` - civil claims for warrants obtained by falsehood.
- `lexcore` - affidavit and Franks co-counsel workflow.
