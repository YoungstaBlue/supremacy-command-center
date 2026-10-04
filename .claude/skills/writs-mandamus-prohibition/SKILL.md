---
name: writs-mandamus-prohibition
description: Evaluates and drafts extraordinary writ petitions - Missouri mandamus (Rule 94), prohibition (Rule 97), appellate writ procedure (Rule 84.22-84.24), federal mandamus (28 U.S.C. 1651, 1361). Use for "writ of mandamus", "writ of prohibition", "judge won't rule", or "no adequate remedy by appeal".
---

# Writs of Mandamus and Prohibition

Decides whether an extraordinary writ is actually available — most requests fail because an appeal or a motion is an adequate remedy — and, if it is, drafts a petition that meets the strict pleading and record requirements.

## When to use
- A court or official refuses to perform a clear, non-discretionary duty (refuses to rule, to accept a filing, to set a hearing, to release a record the law requires)
- A trial court is about to act without jurisdiction or beyond its authority, and waiting for appeal would cause irreparable harm
- Denial of a motion to dismiss on an immunity, venue, or jurisdiction ground where appeal after trial is inadequate
- Not for: ordinary errors reviewable on appeal (use `mo-appeals-procedure`); detention challenges (habeas, Rule 91 / `federal-habeas-2254`); agency decisions with a review statute (use `mo-administrative-appeals`)

## Gather first
- The exact act or refusal, who did it (judge, clerk, official), and when; the order or docket entries
- What was requested below and how it was ruled on (a writ almost always requires asking the lower court/official first)
- Why appeal or other relief is inadequate and what harm occurs while waiting

## Workflow
1. **Pick the writ.**
   - Mandamus (Rule 94): compels performance of an existing, ministerial duty. Requires a clear, unequivocal, specific right to the act demanded and a corresponding duty; it cannot dictate how discretion is exercised, only that discretion be exercised when there is a duty to act.
   - Prohibition (Rule 97): stops a lower tribunal from acting. Missouri courts generally recognize it (a) where the court lacks personal or subject-matter jurisdiction or authority, (b) where it exceeds its authority or abuses discretion so clearly that it lacks power to act as intended, or (c) where a party will suffer irreparable harm without immediate relief and no adequate appellate remedy exists. Confirm this framing in a current Missouri Supreme Court writ opinion before citing.
   - Writs are discretionary even when the elements are met.
2. **Adequate-remedy screen.** No original remedial writ issues from an appellate court where adequate relief is available by appeal or by applying to a lower court (Rule 84.22). Ask: can I file a motion, appeal, or apply to the circuit court first? If yes, do that.
3. **Choose the court (Missouri).**
   - Against an official or inferior tribunal: petition in circuit court under Rule 94/97.
   - Against a circuit judge: petition first in the Court of Appeals district; if denied, a new petition in the Supreme Court (Rule 84.22-84.24 procedure; denial is not appealed, it is re-petitioned).
4. **Federal options.**
   - Federal officers or agencies: mandamus under 28 U.S.C. 1361 for a clear nondiscretionary duty.
   - Federal district court: petition the court of appeals under the All Writs Act, 28 U.S.C. 1651, and FRAP 21. Petitioner must show no other adequate means to attain relief, a clear and indisputable right, and that the writ is appropriate under the circumstances (Cheney v. U.S. Dist. Court, 542 U.S. 367 (2004)).
   - Federal courts generally lack mandamus power over state courts and state officials; do not seek a federal writ to compel a Missouri judge.
5. **Draft the petition (Rule 84.24 format for appellate writs — verify).** Caption "State ex rel. [Relator] v. [Respondent judge/official]"; jurisdictional statement; statement of facts with record cites; relief sought; reasons the writ should issue (each element); why no adequate remedy exists. Attach suggestions in support and an appendix with every order, motion, and transcript excerpt relied on — a writ court sees only what is attached. Serve respondent and real parties in interest.
6. **Process.** Court may deny summarily, issue a preliminary order (prohibition/mandamus) requiring an answer, then make the writ permanent or quash it. Ask for a stay of underlying proceedings in the petition if the harm is imminent.
7. **Delay as a mandamus target.** For a judge who will not rule, first file a written request/motion for ruling or notice of submission; document the time elapsed. Courts expect that before a writ.

## Output
- Availability memo: writ type, each element (met / not met / unclear), adequate-remedy analysis, correct court
- Petition skeleton with headings above
- Appendix index (A1, A2, ...) cross-referenced to the facts

## Pitfalls
- Using a writ to relitigate a discretionary ruling or ordinary trial error
- Treating denial of a writ petition as appealable instead of re-petitioning the higher court
- Skipping the lower court (Rule 84.22) or failing to ask the official to act first
- Thin appendix — missing the order or transcript being challenged
- Seeking a federal writ against a state judge
- Delay: waiting months undermines the claim of urgency and irreparable harm

## Verify before relying
- Pull current text of Rules 84.22-84.26, 94, 97 and 28 U.S.C. 1361, 1651, FRAP 21 via `statute-lookup` (or Descrybe `search_laws_and_rules`); find a current Missouri Supreme Court writ case stating the standard and confirm it is good law.
- Note any deadline in the underlying case; a writ petition does not toll it unless a stay issues.
- Legal information, not legal advice.

## Related skills
- `mo-appeals-procedure` — the ordinary remedy writs are measured against
- `jurisdiction-and-venue-analyzer` — jurisdiction and venue grounds for prohibition
- `sovereign-and-official-immunity-mo` — immunity denials often reviewed by prohibition
- `court-document-formatting` — captions and appendix formatting
