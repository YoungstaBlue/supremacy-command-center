---
name: mo-criminal-case-roadmap
description: Maps a Missouri criminal case stage by stage - arrest, initial appearance, bond, preliminary hearing, information, arraignment, discovery, motions, trial, new trial, sentencing, appeal - with each deadline. Use for "what happens next in my criminal case", "arraignment", "felony timeline", or a new charge.
---

# Missouri Criminal Case Roadmap

Locates a Missouri state criminal case on the procedural timeline, lists the deadlines that are running now, and routes each stage to the skill that handles it in depth.

## When to use
- A new arrest, summons, complaint, information, or indictment in a Missouri circuit or associate circuit court
- "What happens next?", "what is an arraignment?", "do I get a preliminary hearing?", "when is my deadline?"
- Building a case calendar for a pending felony or misdemeanor
- Not for: municipal ordinance or traffic tickets in a municipal division (use `mo-municipal-ordinance-defense`); federal charges (FRCrP governs)

## Gather first
- The charging document (complaint, information, or indictment), the case number, and whether the charge is a felony or misdemeanor
- Dates: arrest, initial appearance, any preliminary hearing setting, arraignment/plea entry, verdict, sentencing
- Custody status, bond conditions, and whether counsel is appointed, retained, or waived

## Workflow
1. **Identify the track.** A felony starts on a complaint (Rule 22) and must reach an information or indictment (Rule 23); a misdemeanor proceeds under Rule 21. Municipal ordinance cases run under Rule 37 instead.
2. **Arrest without warrant.** RSMo 544.170.1: a person arrested without a warrant must be released within 24 hours unless charged and held on a warrant. The Fourth Amendment separately requires a prompt judicial probable-cause determination (Gerstein v. Pugh, 420 U.S. 103 (1975); County of Riverside v. McLaughlin, 500 U.S. 44 (1991) - generally within 48 hours).
3. **Initial appearance.** Felony arrest on a warrant: appearance no later than 48 hours, excluding weekends and holidays, after confinement in the issuing county (Rule 22.07). At it the court advises of the charge, right to counsel, right to request appointed counsel, and right to silence, and addresses release conditions (Rule 22.08).
4. **Release/detention.** If still detained after the initial appearance, a release hearing must occur within 7 days excluding weekends and holidays, absent good cause (Rule 33.05). Route to `mo-bond-pretrial-release`.
5. **Preliminary hearing (felony complaint).** Within 30 days of initial appearance if in custody, 60 days if not, extendable for good cause (Rule 22.09(a)). Change of judge before the preliminary examination: Rule 32.06. Route to `mo-preliminary-hearing`.
6. **Bound over.** Court orders appearance in the trial division within 40 days of the hearing (Rule 22.09(c)); the information must be filed within 10 days of the bind-over order unless extended for good cause (Rule 23.03).
7. **Arraignment and plea.** Charge read or its substance stated; defendant gets a copy before pleading (Rule 24.01). Calendar from the plea date: change of judge application within 10 days after the initial plea (Rule 32.07(b)); discovery requests within 20 days after arraignment (Rule 25.02(b)).
8. **Pretrial motions.** Defects in institution of the prosecution or the charging document must be raised by motion before plea or within a reasonable time after, or they are waived; lack of jurisdiction and failure to charge an offense are never waived (Rule 24.04(b)). Suppression motions before trial (Rule 24.05; RSMo 542.296). Route to `mo-motion-to-suppress`, `mo-criminal-discovery`, `mo-speedy-trial`.
9. **Plea or trial.** Guilty plea colloquy under Rule 24.02 (route to `mo-plea-and-sentencing`). At trial, make objections and offers of proof contemporaneously.
10. **After verdict.** Motion for new trial within 15 days of the verdict, one extension up to 10 more days if requested within the first 15 (Rule 29.11(b)). In jury cases, errors not in the motion are not preserved except jurisdiction, charging sufficiency, and sufficiency of evidence (Rule 29.11(d)). Undecided after 90 days = denied (Rule 29.11(g)).
11. **Sentencing.** Felony sentencing assessment report unless waived (RSMo 557.026). Judgment is final at sentencing.
12. **Appeal and post-conviction.** Notice of appeal within 10 days after judgment becomes final (Rule 30.01 incorporating Rule 81.04); late notice only by appellate-court leave sought within 12 months (Rule 30.03). Post-conviction under Rules 24.035/29.15 - route to `mo-post-conviction-relief`.

## Output
- **Stage now:** one line
- **Deadline table:** | Event | Trigger date | Rule/statute | Due date | Extendable? |
- **Next 3 actions** in order, each tied to a sibling skill
- **Open questions** (max 3) for missing dates or documents

## Pitfalls
- Counting from the wrong trigger: discovery and change-of-judge deadlines run from arraignment/plea, not arrest.
- Waiving the preliminary hearing without understanding it is the only pre-trial chance to cross-examine under oath besides depositions.
- Letting Rule 24.04(b)(2) defects go unraised until trial - they are waived.
- Missing the 15-day new trial deadline; issues omitted from the motion are lost in jury cases.
- Assuming a pro se defendant gets more time - courts hold pro se litigants to the same rules.

- Ignoring bond conditions while the case is pending - a violation can mean a warrant and detention (Rule 33.06).
- Talking about the facts with police, jail callers, or on recorded jail phones; those statements are evidence.

## Verify before relying
- Pull current text of every rule and statute cited via `statute-lookup` (or Descrybe `search_laws_and_rules`); the Rule 22, 24, and 33 timelines were amended in 2019-2022.
- Recompute every deadline from the actual entry or service date using `mo-deadline-calculator` and Rule 20.01.
- Legal information, not legal advice; a person facing jail should request appointed counsel (public defender) at the initial appearance.

## Related skills
- `mo-bond-pretrial-release` - release hearing and bond reduction
- `mo-preliminary-hearing` - probable cause hearing strategy
- `mo-criminal-discovery` - Rule 25 requests and sanctions
- `mo-speedy-trial` - statutory and constitutional speedy trial
- `mo-deadline-calculator` - day counting
- `lexcore` - broader criminal co-counsel analysis
