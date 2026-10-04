---
name: standard-of-review-finder
description: Identifies the appellate standard of review per issue - de novo, abuse of discretion, clear error, substantial evidence, plain error - in Missouri appellate courts and the 8th Circuit, tied to preservation. Use for "standard of review", "can I win on appeal", "plain error", or "was this preserved".
---

# Standard of Review Finder

Matches every appellate issue to the standard the appellate court will apply and to the preservation steps required, because the standard of review often decides the appeal before the merits are reached.

## When to use
- Drafting a brief: each point relied on (Missouri) or issue (federal) needs its standard of review.
- Deciding which issues are worth appealing, or whether to seek a writ instead.
- Checking whether an error was preserved, or whether only plain error review is available.
- Not for: overall brief structure (use `appellate-brief-writer`) or notice-of-appeal timing (use `mo-appeals-procedure` / `federal-appeals-8th-circuit`).

## Gather first
- The ruling being challenged (what the trial court did, when, and in what form — order, judgment, evidentiary ruling, instruction).
- How the issue was raised below: objection, motion, offer of proof, motion for new trial, motion to amend judgment — with record cites.
- Whether the case was tried to a jury, tried to the court, decided on summary judgment or dismissal, or is an administrative decision.

## Workflow
1. **Characterize the issue precisely.** Pure question of law, finding of fact, mixed question, discretionary ruling, or sufficiency of evidence. The same case can carry several standards.
2. **Apply the Missouri civil standards.**
   - Court-tried (bench) judgments: affirmed unless there is no substantial evidence to support it, it is against the weight of the evidence, or it erroneously declares or applies the law (Murphy v. Carron, 536 S.W.2d 30 (Mo. banc 1976)). Legal conclusions reviewed de novo; credibility deferred to the trial court. "Against the weight of the evidence" challenges are disfavored and require a specific multi-step argument — research the current framework before using it.
   - Summary judgment: de novo, viewing the record in the light most favorable to the non-movant (ITT Commercial Finance Corp. v. Mid-America Marine Supply Corp., 854 S.W.2d 371 (Mo. banc 1993)).
   - Motion to dismiss for failure to state a claim: de novo, accepting pleaded facts as true.
   - Admission or exclusion of evidence: abuse of discretion, plus prejudice; an appellate court will not reverse unless the error materially affected the merits (Rule 84.13(b)).
   - Jury instruction error: whether an instruction was proper is a question of law; reversal requires prejudice.
   - Statutory and constitutional interpretation: de novo.
   - Administrative decisions: whether supported by competent and substantial evidence on the whole record (Mo. Const. art. V, § 18; Hampton v. Big Boy Steel Erection, 121 S.W.3d 220 (Mo. banc 2003)); legal questions de novo.
3. **Apply the Missouri criminal standards.**
   - Sufficiency of evidence: whether any reasonable juror could have found guilt beyond a reasonable doubt, viewing evidence and inferences favorably to the verdict (State v. Grim, 854 S.W.2d 403 (Mo. banc 1993)).
   - Motion to suppress: deference to factual and credibility findings; whether the Fourth Amendment was violated is reviewed de novo.
   - Evidentiary rulings, mistrial denials, and similar trial management: abuse of discretion.
   - Unpreserved errors: plain error only (Rule 30.20) — requires evident, obvious, and clear error resulting in manifest injustice or miscarriage of justice.
4. **Apply preservation rules (Missouri).** Preservation determines whether the ordinary standard or plain error applies.
   - Timely, specific objection at trial; an offer of proof for excluded evidence.
   - Jury-tried civil cases: allegations of error must be in a motion for new trial to be preserved (Rule 78.07(a), with listed exceptions). Errors in the form or language of a judgment, including failure to make required findings, must be raised in a motion to amend the judgment (Rule 78.07(c)).
   - Jury-tried criminal cases: allegations of error must be in the motion for new trial (Rule 29.11(d)).
   - Civil plain error is discretionary and rarely granted (Rule 84.13(c)).
   - The point relied on must state the ruling, the legal reasons, and why those reasons support reversal (Rule 84.04(d)); a defective point can waive the issue.
5. **Apply federal standards (8th Circuit).**
   - Findings of fact in bench trials: clear error (Fed. R. Civ. P. 52(a)(6); Anderson v. City of Bessemer City, 470 U.S. 564 (1985)). Conclusions of law: de novo.
   - Summary judgment and Rule 12(b)(6) dismissals: de novo.
   - Discretionary rulings (evidence, discovery, sanctions, continuances, leave to amend): abuse of discretion (see Pierce v. Underwood, 487 U.S. 552 (1988)).
   - Reasonable suspicion and probable cause determinations: de novo, with deference to historical facts and local inferences (Ornelas v. United States, 517 U.S. 690 (1996)).
   - Criminal sufficiency: whether any rational trier of fact could have found the elements beyond a reasonable doubt (Jackson v. Virginia, 443 U.S. 307 (1979)).
   - Unpreserved error: plain error (Fed. R. Crim. P. 52(b); United States v. Olano, 507 U.S. 725 (1993)) — error, plain, affecting substantial rights, and seriously affecting the fairness, integrity, or public reputation of judicial proceedings. Civil jury-instruction plain error is governed by Fed. R. Civ. P. 51(d)(2).
   - Federal habeas review of state decisions: AEDPA deference under 28 U.S.C. § 2254(d).
6. **Assess the win probability by standard.** De novo issues are the strongest appellate issues; abuse of discretion and weight-of-the-evidence issues rarely win; plain error almost never does. Rank issues accordingly and consider dropping weak ones.

## Output
| Issue | Ruling below (record cite) | Characterization | Standard of review | Authority | Preserved? How (record cite) | Prejudice required? | Strength |
|---|---|---|---|---|---|---|---|

Then a draft standard-of-review paragraph for each issue the user keeps, ready to drop into the brief.

## Pitfalls
- Stating "de novo" for an issue that is actually discretionary; courts notice and it undermines credibility.
- Failing to preserve: no objection, no offer of proof, or the error omitted from the motion for new trial or motion to amend the judgment.
- Arguing the evidence differently than viewed in the light most favorable to the judgment or verdict.
- Raising an issue for the first time on appeal and expecting ordinary review.
- Writing a Missouri point relied on that does not comply with Rule 84.04(d).
- Ignoring the prejudice requirement; even a correct claim of error fails without it.

## Verify before relying
- Pull verbatim text of every statute/rule cited via `statute-lookup` (or Descrybe `search_laws_and_rules`); check case law is still good law (CourtListener / Descrybe treatment) before citing.
- Find a recent Missouri appellate or 8th Circuit case stating the standard for the specific issue type and cite it instead of relying only on the general cases above.
- Recompute any deadline from the actual service/entry date.
- Legal information, not legal advice; recommend counsel/legal aid for high-stakes decisions.

## Related skills
- `appellate-brief-writer` — put each standard into the points relied on and argument.
- `mo-post-trial-motions` — preserve issues in the motion for new trial or to amend.
- `mo-appeals-procedure` — notice of appeal and record on appeal.
- `objection-playbook` — preserve error at trial in the first place.
- `irac-analysis` — analyze each issue under its standard.
