---
name: mo-deadline-calculator
description: Computes Missouri court deadlines under Rule 44.01 - day counting, weekends, holidays, mail add-on days, and non-extendable post-trial and appeal deadlines. Use for "when is my answer due", "how many days do I have", "is it too late to file", or "compute the due date".
---

# Missouri Deadline Calculator

Compute a Missouri state-court deadline from a triggering event, show the math, and classify whether the deadline can be extended or is jurisdictional.

## When to use
- Any "when is X due" question in a Missouri circuit or associate circuit case.
- Checking whether a filing already made was timely.
- Building a case calendar after service, a judgment, or a discovery request.
- Not for: federal-court deadlines (FRCP 6 governs - see `federal-civil-discovery` / `federal-appeals-8th-circuit`); limitations periods for filing suit - use `statute-of-limitations-checker`.

## Gather first
- The triggering event and its exact date (service of summons, service of a paper, entry of judgment, filing of a motion).
- How the paper was served (personal, mail, e-filing system, email) and the court (circuit, associate circuit, appellate).
- The rule, statute, or order that sets the period (ask for the order if the judge set a custom date).

## Workflow
1. Identify the governing period and source. Common Missouri periods (verify each against current text):
   - Answer to petition: 30 days after service of summons and petition (Rule 55.25(a)); associate circuit cases under RSMo ch. 517 may instead require appearance on the return date - check the summons.
   - Responses to interrogatories, requests for production, requests for admission: 30 days after service (Rules 57.01, 58.01, 59.01). Unanswered requests for admission are deemed admitted.
   - Response to summary judgment motion: 30 days after service (Rule 74.04(c)(2)).
   - Motion for new trial / to amend judgment / JNOV: 30 days after entry of judgment (Rules 78.04, 72.01).
   - Notice of appeal: 10 days after the judgment becomes final (Rule 81.04(a); finality under Rule 81.05).
   - Change of judge application: see Rule 51.05 for the time limit tied to service or designation of the trial judge.
2. Count under Rule 44.01(a): exclude the day of the triggering event; include the last day; if the last day is a Saturday, Sunday, or legal holiday, the period runs to the end of the next day that is none of those. For periods under 7 days, intermediate Saturdays, Sundays, and legal holidays are excluded.
3. Legal holidays: use the Missouri statutory list (RSMo 9.010) plus any day the court is closed by order. Confirm the clerk's office was actually open.
4. Add service days if applicable: Rule 44.01(e) adds 3 days when a period runs from service of a paper and the paper was served by mail. Verify whether service through the e-filing system or email adds any time under the current rule text - do not assume it does.
5. Do not add mail days to periods that run from entry of judgment or filing (e.g., post-trial motions, notice of appeal) - those run from an act, not from service.
6. Classify extendability. Rule 44.01(b) lets the court enlarge most periods (on motion before expiry, or after expiry for excusable neglect), but bars enlarging the periods under Rules 52.13, 72.01, 73.01, 75.01, 78.04, 78.06, 81.04, and 81.07 except as those rules provide. Mark these "NON-EXTENDABLE".
7. Note late-appeal escape valve: Rule 81.07 special order for late notice of appeal (limited window after judgment final - verify current period). Treat as last resort, not a plan.
8. Produce a backward plan: draft-complete date, signature/notary date, filing date with at least two business days of margin.

## Output
- Computation table: Trigger event | Trigger date | Rule/source | Period | Service add-on | Raw end date | Weekend/holiday roll | FINAL DUE DATE | Extendable? (Y/N/jurisdictional).
- One-line plain statement: "Due no later than [day, date] - file by [margin date]."
- Assumptions list (service method, holiday list used, rule text version).

## Pitfalls
- Counting the trigger day as day 1.
- Adding mail days to judgment-based deadlines.
- Relying on an associate circuit summons return date while assuming the 30-day answer rule (or vice versa).
- Treating the notice-of-appeal deadline as running from the judgment date when a timely post-trial motion was filed.
- Believing a judge's informal statement extended a non-extendable deadline.
- Missing that a motion to extend must generally be filed before the deadline expires.
- E-filing after the clerk's cutoff time or on a day the system logs as the next day - check the e-filing timestamp rules.

## Verify before relying
- Pull verbatim text of Rule 44.01 and the period-setting rule via `statute-lookup`; rule amendments change add-on days.
- Recompute from the actual file-stamped or service date, not from when the user received the paper.
- Check local court rules and any scheduling order that overrides default periods.
- Legal information, not legal advice; for a deadline that may already have passed, contact counsel or legal aid immediately.

## Related skills
- `mo-post-trial-motions` - the 30/90-day post-judgment chain.
- `mo-appeals-procedure` - notice of appeal and briefing deadlines.
- `mo-default-judgment-set-aside` - what happens when the answer deadline was missed.
- `statute-of-limitations-checker` - deadlines to start a lawsuit.
- `filing-followup` - confirms filings were made on time.
