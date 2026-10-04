---
name: federal-tro-preliminary-injunction
description: Builds federal TRO and preliminary injunction motions under FRCP 65 using the Eighth Circuit Dataphase factors, plus notice, bond, and order requirements. Use for "federal TRO", "preliminary injunction", "Dataphase", "emergency injunction", "Rule 65", or opposing an injunction motion.
---

# Federal TRO and Preliminary Injunction

Seeks (or opposes) emergency federal injunctive relief with the evidence and procedural steps Rule 65 and the Eighth Circuit require.

## When to use
- Ongoing or imminent harm that money damages after trial cannot fix (speech restrictions, loss of housing, retaliation, unconstitutional enforcement)
- Opposing a TRO or preliminary injunction motion
- Not for: Missouri state-court TROs under Rule 92 — use `mo-temporary-restraining-order`; stopping a pending state prosecution — check Younger in `federal-subject-matter-jurisdiction` first

## Gather first
- The precise conduct to be stopped or required, by whom, and when the harm will occur
- Sworn evidence: declarations, documents, photos, video, communications
- Whether and how the opposing party has been notified, and their counsel's contact information

## Workflow
1. **Threshold.** A pending complaint stating the claims the injunction protects; subject-matter jurisdiction; no Younger, Anti-Injunction Act (28 U.S.C. 2283), or sovereign-immunity bar to the specific relief (state officials can be enjoined prospectively in official capacity).
2. **The four factors.** Dataphase Sys., Inc. v. C L Sys., Inc., 640 F.2d 109 (8th Cir. 1981) (en banc): (1) threat of irreparable harm to the movant; (2) balance between that harm and the injury the injunction would inflict on other parties; (3) probability of success on the merits; (4) public interest. The Supreme Court frames the same inquiry in Winter v. NRDC, 555 U.S. 7 (2008): irreparable harm must be likely, not merely possible. The Eighth Circuit treats likelihood of success as the most significant factor (verify a current circuit citation for this phrasing).
3. **Heightened showing.** Where the injunction would block enforcement of a duly enacted statute, the movant must show it is likely to prevail on the merits, not merely a fair chance. Planned Parenthood Minn., N.D., S.D. v. Rounds, 530 F.3d 724 (8th Cir. 2008) (en banc). Mandatory injunctions (ordering affirmative action) and relief that gives the movant everything it would win at trial face closer scrutiny.
4. **Irreparable harm evidence.** Specific, imminent, and not compensable by damages. Loss of constitutional freedoms such as First Amendment rights, even briefly, is commonly treated as irreparable. Delay in seeking relief undercuts urgency — explain any delay.
5. **Government defendants.** When the government is the opposing party, the balance-of-harms and public-interest factors merge. Nken v. Holder, 556 U.S. 418 (2009).
6. **TRO without notice (Rule 65(b)(1)).** Only if (A) specific facts in an affidavit or verified complaint clearly show immediate and irreparable injury before the adverse party can be heard, and (B) the movant certifies in writing efforts made to give notice and why it should not be required. Courts strongly prefer notice; send the papers to the other side and say so.
7. **Duration and hearing.** A TRO without notice expires at the time set by the court, not to exceed 14 days, extendable once for good cause for a like period or by consent (65(b)(2)); the preliminary-injunction hearing is set at the earliest possible time, and the adverse party may move to dissolve on 2 days' notice. A preliminary injunction requires notice to the adverse party (65(a)(1)); the court may consolidate with trial on the merits (65(a)(2)).
8. **Bond (65(c)).** Security in an amount the court considers proper. Ask for a nominal or zero bond with reasons: indigence, public-interest litigation, minimal risk of harm to defendant.
9. **Order contents (65(d)).** The order must state reasons, state terms specifically, and describe the acts restrained in reasonable detail without referring to another document. Draft a proposed order meeting these terms.
10. **Appeal.** Orders granting, refusing, modifying, or dissolving injunctions are immediately appealable (28 U.S.C. 1292(a)(1)); denial of a TRO generally is not, unless it functions as a preliminary-injunction denial.

## Output
- Motion packet outline: Motion; Memorandum (Facts with record cites; Legal Standard; Dataphase factor-by-factor argument; Bond; Relief Requested); Declarations; Rule 65(b)(1)(B) certification of notice efforts; Proposed Order
- Factor table:

| Factor | Key facts | Evidence (Ex.) | Best authority | Weakness / response |
|---|---|---|---|---|

- Proposed order specifying exactly what is restrained, whom it binds, duration, and bond

## Pitfalls
- Asking for broad relief ("stop violating my rights") — orders must be specific
- No sworn evidence; unverified allegations do not support a TRO
- Waiting weeks or months, then claiming emergency
- Seeking to enjoin a pending state criminal case or state-court judgment (Younger / Rooker-Feldman)
- Ignoring the bond issue, leading to an unaffordable security requirement
- Asking for damages in a TRO motion; injunctions address future harm

## Verify before relying
- Pull FRCP 65, 28 U.S.C. 1292(a)(1), 2283 and local rules on emergency motions verbatim via `statute-lookup` or Descrybe `search_laws_and_rules`.
- Confirm Dataphase, Rounds, and any newer Eighth Circuit injunction authority are cited accurately and still good law via CourtListener.
- Track the 14-day TRO expiration and any hearing date from the actual entry time.
- Legal information, not legal advice; emergency injunction practice is a strong reason to contact counsel or a civil-rights organization.

## Related skills
- `mo-temporary-restraining-order` — state-court counterpart
- `federal-subject-matter-jurisdiction` — Younger and Anti-Injunction Act screens
- `section-1983-claim-builder` — the underlying claim supporting likelihood of success
- `first-amendment-analyzer` — frequent basis for irreparable-harm arguments
- `federal-appeals-8th-circuit` — interlocutory appeal of injunction rulings
