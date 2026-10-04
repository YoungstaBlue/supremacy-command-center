---
name: mo-appeals-procedure
description: Walks through Missouri state appeals - final judgment, Rule 81.04 notice of appeal timing, late notice by special order, record on appeal, briefing schedule, Rule 84.04 points relied on, rehearing and transfer. Use for "appeal my judgment", "notice of appeal", "Court of Appeals", or "record on appeal".
---

# Missouri Appeals Procedure

Gets a Missouri appeal filed on time and kept alive: confirms an appealable final judgment, computes the notice deadline, assembles the record, and tracks briefing through rehearing and transfer.

## When to use
- A Missouri circuit or associate circuit judgment was entered and the user wants to appeal or defend an appeal
- Unsure whether a ruling is final/appealable, or a deadline may have been missed
- Building the legal file and transcript, or calendaring briefs
- Not for: writing the brief itself (use `appellate-brief-writer`); federal appeals (use `federal-appeals-8th-circuit`); agency decisions (use `mo-administrative-appeals`)

## Gather first
- The judgment document, its entry date, and whether it is titled "Judgment"
- Whether any after-trial motion (new trial, amend, JNOV) was filed, and when
- Civil or criminal, and which court entered it (circuit judge vs. associate circuit judge, small claims, municipal)

## Workflow
1. **Is there an appealable judgment?**
   - Right to appeal: RSMo 512.020 (aggrieved party; final judgment and listed interlocutory orders).
   - The writing must be signed and denominated "judgment" or "decree" (Rule 74.01(a)); docket entries and orders titled "order" are generally not appealable.
   - Must resolve all claims as to all parties, unless the court expressly certifies "no just reason for delay" under Rule 74.01(b) — and even then it must dispose of a distinct judicial unit.
   - Associate circuit / small claims: check whether the route is trial de novo in circuit court rather than appeal (RSMo 512.180 — verify which judgments qualify). Municipal: see `mo-municipal-ordinance-defense`.
2. **When does the judgment become final?** (Rule 81.05(a))
   - No timely authorized after-trial motion: 30 days after entry.
   - Timely after-trial motion filed: when ruled on, or 90 days after the motion was filed (overruled by operation of law), whichever is earlier.
3. **Notice of appeal deadline (civil).** No later than 10 days after the judgment becomes final (Rule 81.04(a)). File in the trial court with the docket fee (or poor person request). Typical no-motion case: day 30 + 10 = day 40 after entry — recompute with Rule 44.01. A premature notice is generally treated as filed after finality (Rule 81.05(b) — verify).
4. **Missed it?** Civil: motion in the appellate court for special order to file late notice within 6 months after the judgment became final, showing the delay was not due to culpable negligence (Rule 81.07 — verify). Criminal: notice of appeal within 10 days after sentence/judgment (Rule 30.01), late notice by special order within 12 months (Rule 30.03 — verify). These are the only rescue paths.
5. **Where it goes.** Court of Appeals district (Eastern, Western, Southern) by the trial county; Supreme Court has exclusive jurisdiction over validity of a U.S. statute or treaty, validity of a Missouri statute or constitutional provision, construction of state revenue laws, title to state office, and death sentences (Mo. Const. art. V, sec. 3). A colorable constitutional-validity challenge must be raised at the earliest opportunity below.
6. **Stay of judgment.** Appeal does not stop enforcement of a money judgment unless a supersedeas bond is posted and approved (Rule 81.09 — verify).
7. **Record on appeal** (Rule 81.12). Legal file (pleadings, judgment, notice of appeal, motions and rulings at issue) plus transcript of proceedings. Order the transcript promptly from the court reporter and pay or seek poor-person status; appellant bears the burden to provide a record sufficient for review — missing transcript means presumed-correct rulings. Calendar the record deadline (Rule 81.19 — verify current period and extension practice).
8. **Briefing schedule** (Rule 84.05 — verify periods): appellant's brief after the record is filed, respondent's brief, then reply. Extensions by motion before the deadline. Briefs must comply with Rule 84.04 and 84.06; noncompliance can mean dismissal — pro se appellants are held to the same rules.
9. **Points relied on** (Rule 84.04(d)): each point must (a) identify the ruling challenged, (b) state the legal reasons for reversible error, (c) explain in summary why, in the context of the case, those reasons support reversible error — template: "The trial court erred in [ruling], because [legal reasons], in that [facts showing why]." Hand off drafting to `appellate-brief-writer`.
10. **After the opinion.** Motion for rehearing and/or application for transfer in the Court of Appeals within the short window in Rule 84.17 / 83.02; then application to the Supreme Court under Rule 83.04 (verify the 15-day windows before relying). Mandate issues after these periods expire.

## Output
- Appealability checklist with yes/no and source for each item
- Deadline card: entry date | after-trial motion filed | finality date | notice due | late-notice outer date | record due | brief due
- Record designation list (documents + transcript dates)

## Pitfalls
- Appealing an "order" or a judgment that leaves claims pending
- Counting 10 days from entry instead of from finality, or assuming a pending motion extends time when it was untimely or unauthorized
- No transcript, or a partial transcript omitting the hearing that matters
- Points relied on that only say "the court erred" without the ruling, reason, and in-that clause — abandoned/unreviewable
- Failing to preserve below (objection, offer of proof, motion for new trial in jury cases) — limited to plain error

## Verify before relying
- Pull current text of Rules 30.01, 30.03, 74.01, 81.04, 81.05, 81.07, 81.09, 81.12, 81.19, 83.02, 83.04, 84.04, 84.05, 84.17 and RSMo 512.020/512.180 via `statute-lookup` (or Descrybe `search_laws_and_rules`); check the district's local rules.
- Recompute every deadline from the actual entry date under Rule 44.01.
- Legal information, not legal advice; appellate deadlines are unforgiving — contact appellate counsel or legal aid quickly.

## Related skills
- `mo-post-trial-motions` — what extends finality and preserves error
- `mo-deadline-calculator` — Rule 44.01 counting
- `appellate-brief-writer` — draft the brief and points relied on
- `standard-of-review-finder` — standard per point
- `writs-mandamus-prohibition` — when no appeal is available
