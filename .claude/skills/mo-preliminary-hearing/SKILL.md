---
name: mo-preliminary-hearing
description: Prepares for a Missouri felony preliminary hearing under Rule 22.09 - timing, probable cause standard, waive-or-hold decision, and a cross-examination plan to lock in testimony and discover the state's case. Use for "preliminary hearing", "prelim", "bound over", or "should I waive my prelim".
---

# Missouri Preliminary Hearing

Plans the felony preliminary hearing: whether to hold or waive it, how to use cross-examination to test probable cause and preserve testimony, and what follows a bind-over or discharge.

## When to use
- A felony complaint is pending and a preliminary hearing is set or must be set
- "Should I waive the prelim?", "what happens at the preliminary hearing?", "can I get the case dismissed for no probable cause?"
- Drafting cross-examination outlines for the arresting officer or complaining witness
- Not for: suppression of evidence (use `mo-motion-to-suppress`); misdemeanors (no preliminary hearing)

## Gather first
- Felony complaint and probable cause statement (Rule 22.03), initial appearance date, custody status
- Every police report, video, and witness statement available (Rule 25.03(a) disclosure is available after the felony complaint - see `mo-criminal-discovery`)
- The elements of each charged offense

## Workflow
1. **Check timing.** Rule 22.09(a): hearing within a reasonable time, no later than 30 days after the initial appearance if in custody, 60 days if not. Extensions require good cause, up to 30/60 days each. On any extension request, the defendant may ask the court to review detention or release conditions under Rule 33.05 - do so.
2. **Decide on change of judge.** Rule 32.06: a no-cause application before the preliminary examination must be filed at least 10 days before the initial setting or within 10 days of the judge's designation, whichever is later, and before the examination begins.
3. **Know the standard.** The court decides whether there is probable cause to believe a felony was committed and the defendant committed it (Rule 22.09(b)). It is not proof beyond a reasonable doubt; credibility attacks rarely win discharge, but missing elements or identity can.
4. **Hold-or-waive analysis.** Reasons to hold: test an element the state cannot show; discover the state's theory and witnesses; obtain sworn testimony for later impeachment; the preliminary hearing is a critical stage requiring counsel (Coleman v. Alabama, 399 U.S. 1 (1970)). Reasons to waive: a plea offer conditioned on waiver; risk the state adds charges or prepares its witness; hearing would only educate the state. Record the reasons for the decision.
5. **Build an elements chart.** For each element, list the state's expected proof and the gap. Cross-examination targets the gaps.
6. **Cross-examination plan.** Leading, one fact per question. Goals in order: (a) lock in the witness's account (who, what, when, where, what they saw versus were told); (b) expose hearsay and lack of personal knowledge; (c) establish facts favorable to later suppression (no warrant, no consent, timing of stop, statements before warnings); (d) identify every report, recording, and person not yet disclosed. Do not argue with witnesses.
7. **Defense evidence.** The defendant may cross-examine and introduce evidence (Rule 22.09(b)). Calling the defendant is almost always a mistake.
8. **Make a record.** Arrange a court reporter or recording; the transcript is discoverable (Rule 25.03(b)(5)) and is the impeachment source. Order it promptly.
9. **Argument.** Element-by-element: "No evidence was offered that [element]." Ask for discharge or reduction to a lesser offense supported by the evidence.
10. **After.** Bound over: appearance in the trial division within 40 days (Rule 22.09(c)); information due within 10 days of the bind-over order unless extended (Rule 23.03). Discharged: the state may refile; note it.

## Output
- Hold/waive memo: 5-line recommendation with reasons
- Elements chart: | Element | State's expected proof | Weakness | Cross question numbers |
- Cross-examination outline per witness, numbered leading questions
- Closing argument bullets keyed to elements

## Pitfalls
- Waiving reflexively at the first setting without seeing the reports.
- Letting the defendant testify or speak about the facts.
- Asking open-ended "why" questions that let the officer repair the case.
- Failing to order the transcript, losing the impeachment value.
- Missing the Rule 32.06 change-of-judge window, which closes before the hearing.

- Assuming discharge ends the case; the state can refile or seek an indictment.
- Using the hearing to argue credibility the judge will not resolve at the probable cause stage.
- Skipping the request to review detention when the state seeks an extension (Rule 22.09(a)).

## Verify before relying
- Pull current Rule 22.09, 23.03, and 32.06 text via `statute-lookup` or Descrybe `search_laws_and_rules` (22.09 was amended effective 2022).
- Confirm offense elements from the current statute and MAI-CR instruction.
- Recompute 30/60/40/10-day periods from actual dates.
- Legal information, not legal advice; the right to counsel attaches here - request appointed counsel.

## Related skills
- `mo-criminal-case-roadmap` - overall timeline
- `elements-checklist-builder` - element-to-evidence chart
- `witness-examination-planner` - cross-examination outlines
- `mo-motion-to-suppress` - use prelim testimony to build the suppression record
