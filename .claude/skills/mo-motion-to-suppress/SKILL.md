---
name: mo-motion-to-suppress
description: Drafts a Missouri motion to suppress under RSMo 542.296 and Rule 24.05 - standing, grounds, timing, the state's preponderance burden, hearing prep, and renewing the objection at trial. Use for "motion to suppress", "suppression hearing", "throw out the evidence", or an illegal search in a Missouri case.
---

# Missouri Motion to Suppress

Turns a Fourth Amendment or Mo. Const. art. I, sec. 15 problem into a properly pleaded, timely, and preserved Missouri suppression motion, and prepares the hearing.

## When to use
- Evidence or statements were obtained from a stop, search, arrest, or warrant that may be unlawful
- "Motion to suppress", "suppression hearing", "the search was illegal", "fruit of the poisonous tree"
- Preparing to cross-examine the officer at a suppression hearing
- Not for: deciding whether a search was unconstitutional in the first place (use `fourth-amendment-analyzer`); attacking a false warrant affidavit (use `franks-affidavit-challenge`); statements and Miranda (use `miranda-and-confessions`)

## Gather first
- Police reports, warrant and affidavit (if any), bodycam/dashcam, CAD logs, inventory and consent forms
- Exactly what the defense wants suppressed (physical items, statements, observations, derivative evidence)
- Trial setting date (the motion must precede trial)

## Workflow
1. **Standing.** RSMo 542.296.1: a person "aggrieved by an unlawful seizure" with a pending criminal proceeding growing out of it may move to suppress. Plead the defendant's own privacy or possessory interest in the place or item.
2. **Grounds.** RSMo 542.296.5 lists the grounds: search without a warrant or lawful authority; warrant improper on its face or illegally issued; property seized not described in the warrant; warrant illegally executed; any violation of Mo. Const. art. I, sec. 15 or the Fourth and Fourteenth Amendments. Plead each applicable ground with specific facts - who, when, what was done, and why it lacked authority.
3. **Timing.** File before trial (Rule 24.05; RSMo 542.296.3), unless the defendant was unaware of the grounds or had no opportunity. The court may entertain a mid-trial motion in its discretion - do not rely on that. Give the prosecutor notice of the date, time, place, and nature of the hearing (542.296.4).
4. **Burden.** RSMo 542.296.6: "The burden of going forward with the evidence and the risk of nonpersuasion shall be upon the state to show by a preponderance of the evidence that the motion to suppress should be overruled." Say this in the motion and at the hearing - the state must call witnesses; the defense need not testify.
5. **Structure the argument** issue by issue in the order events happened: initial stop or encounter (reasonable suspicion), expansion or prolongation, arrest (probable cause), search (warrant or exception: consent, search incident to arrest, automobile, inventory, plain view, exigency), then derivative evidence (Wong Sun v. United States, 371 U.S. 471 (1963)). Anticipate the state's exceptions (good faith, inevitable discovery, attenuation, independent source) and answer each.
6. **Hearing preparation.** Subpoena the officers and the recordings; prepare exhibit list; draft cross on: basis for the stop in the officer's own words, timeline in minutes from CAD/bodycam, what consent was asked and given, scope of search versus the warrant. Defendant testimony at the hearing is risky; get advice before deciding.
7. **Ask for findings.** Request findings of fact and conclusions of law on each issue so the record is reviewable.
8. **Preserve.** The pretrial ruling is interlocutory. At trial, object each time the challenged evidence or testimony about it is offered, citing the motion, or the issue is lost. Then include the issue in the motion for new trial (Rule 29.11(d)). A suppression order is one the state may seek interlocutory review of (Rule 30.02).

## Output
- **Motion to Suppress** headings: Introduction (items to suppress); Facts (numbered, with record sources); Standing; Grounds under RSMo 542.296.5; Argument (one subsection per seizure event); State's Burden; Relief Requested (list every item and derivative evidence); Request for Hearing and Findings; Certificate of Service; Notice of Hearing
- Hearing outline: witness order, exhibits, cross-examination topics
- Trial preservation card: the exact objection sentence to repeat

## Pitfalls
- Conclusory motions ("the search was illegal") without facts - courts deny or refuse a hearing.
- Filing after trial starts, or not noticing the hearing.
- Forgetting to renew the objection at trial - the most common preservation failure.
- Omitting derivative evidence (later statements, items found because of the first search) from the relief requested.
- Conceding standing facts carelessly (e.g., denying ownership of the bag).

- Testifying at the hearing without understanding how the testimony could be used later.
- Relying on a mid-trial motion instead of the pretrial one; the court has discretion to refuse it.
- Failing to request findings, leaving the appellate court to presume findings for the state.
- Not subpoenaing the recordings and the officer, so the state's burden is met by an unchallenged report.
- Forgetting to include the suppression issue in the motion for new trial in a jury case (Rule 29.11(d)).
- Treating 542.296 notice as optional - give written notice of the hearing to the prosecutor.

## Verify before relying
- Pull current RSMo 542.296, Rule 24.05, Rule 30.02 text via `statute-lookup` or Descrybe `search_laws_and_rules`.
- Check every search-and-seizure case for current treatment (CourtListener / Descrybe); Missouri courts generally construe art. I, sec. 15 coextensively with the Fourth Amendment - confirm with current authority before arguing otherwise.
- Recompute the filing date against the trial setting.
- Legal information, not legal advice.

## Related skills
- `fourth-amendment-analyzer` - substantive search and seizure analysis
- `franks-affidavit-challenge` - false or omitted facts in the warrant affidavit
- `miranda-and-confessions` - suppressing statements
- `objection-playbook` - renewing the objection at trial
- `lawmind-strategy-engine` - stress-test against the state's exceptions
