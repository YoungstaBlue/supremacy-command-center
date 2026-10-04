---
name: mo-speedy-trial
description: Analyzes Missouri speedy trial rights - the RSMo 545.780 request, Barker v. Wingo factors, the Rule 33.01(d) 120-day demand for detained defendants, and detainers (RSMo 217.460, IAD 217.490). Use for "speedy trial", "case keeps getting continued", "dismiss for delay", or "detainer".
---

# Missouri Speedy Trial

Asserts and litigates the right to a speedy trial in Missouri state court, separating the statutory request, the constitutional claim, and the detainer statutes, each with different triggers and remedies.

## When to use
- The case has been pending a long time or repeatedly continued by the state
- "File a speedy trial request", "dismiss for speedy trial violation", "I'm in prison with a detainer from another county/state"
- A detained defendant under Rule 33.01(d) wants trial within 120 days
- Not for: federal Speedy Trial Act cases (18 U.S.C. 3161 governs)

## Gather first
- Dates: arrest, charge filed, arraignment, every continuance (who asked, why, on the record or not), any speedy trial request filed
- Custody history (jail, DOC, out-of-state prison, detainer lodged)
- Concrete prejudice: lost witness, lost evidence, job/housing loss, anxiety, pretrial jail time

## Workflow
1. **Statutory request (RSMo 545.780).** If the defendant announces ready for trial and files a request for speedy trial, the court "shall set the case for trial as soon as reasonably possible." Enforceable by mandamus. Failure to comply is not grounds for dismissal unless the court also finds a constitutional speedy trial violation (545.780.2). File the request early and re-assert it; it also serves as the Barker "assertion" factor.
2. **Detained defendant (Rule 33.01(d)).** A defendant ordered detained may, by written request filed after arraignment, demand trial within 120 days of the request (or of a change-of-venue order, whichever is later). Any defense request to continue beyond 120 days waives it.
3. **Constitutional test.** Sixth Amendment and Mo. Const. art. I, sec. 18(a). Apply Barker v. Wingo, 407 U.S. 514 (1972): (a) length of delay - the threshold trigger; if not presumptively prejudicial, analysis stops (Doggett v. United States, 505 U.S. 647 (1992), noting delay approaching one year is generally presumptively prejudicial); (b) reason for delay - deliberate state delay weighs heavily against the state, negligence and crowded dockets less so, defense-caused delay against the defendant; (c) assertion of the right; (d) prejudice - oppressive pretrial incarceration, anxiety, and impairment of the defense (the most serious).
4. **Delay accounting.** Build a day-by-day table attributing each period to the state, the defense, or the court. Defense continuances and motions are charged to the defense; unexplained gaps go to the state.
5. **Intrastate detainer (UMDDL).** A DOC prisoner with an untried Missouri charge may request disposition; trial within 180 days after the court and prosecutor receive the request and certificate (RSMo 217.460). Dismissal with prejudice under the current statute requires also finding a constitutional speedy trial violation. Confirm the request was delivered to the right court and prosecutor and the certificate attached (procedure in RSMo 217.450-217.485).
6. **Interstate detainer (IAD, RSMo 217.490).** Prisoner-initiated request: trial within 180 days of delivery of written notice (Art. III). State-initiated transfer: trial within 120 days of arrival (Art. IV). Remedy for violation: dismissal with prejudice (Art. V). Strict compliance with notice procedure matters.
7. **Motion to dismiss.** Lead with the Barker analysis and the delay table; attach the 545.780 request and any detainer paperwork.

## Output
- **Request for Speedy Trial** (one page: ready-for-trial announcement, request, signature, certificate of service)
- **Delay attribution table:** | Period | Days | Cause | Attributed to | Record cite |
- **Motion to Dismiss** headings: Facts and Timeline; Statutory Request; Barker Factors (four subsections); Detainer Statute (if any); Prejudice; Relief
- **Detainer checklist** for UMDDL or IAD

## Pitfalls
- Requesting or agreeing to continuances while claiming speedy trial; those periods count against the defendant.
- Expecting dismissal from 545.780 alone - it requires a constitutional violation.
- Asserting prejudice generally instead of naming the lost witness or evidence.
- Detainer requests sent to the wrong office or without the required certificate.
- Raising speedy trial for the first time on appeal; file the motion and obtain a ruling before trial.

- Counting from arrest when the right has not attached; attachment generally runs from arrest or formal charge, whichever is first - confirm with current authority.
- Treating a dismissed and refiled charge as one continuous period without checking how courts count the gap.
- Assuming the IAD covers pretrial detainees or probation-violation detainers; it applies to prisoners serving a term with untried charges - confirm coverage.
- Making the request but then announcing not ready at a setting.
- Leaving out the record cites for each continuance; the appellate court relies on the docket.
- Skipping mandamus when the court ignores a 545.780 request; dismissal requires the constitutional violation.
- Not documenting anxiety, job loss, and lost evidence contemporaneously.

## Verify before relying
- Pull current RSMo 545.780, 217.450-217.485, 217.490, and Rule 33.01(d) text via `statute-lookup` or Descrybe `search_laws_and_rules`; 217.460's remedy was amended.
- Check Missouri appellate treatment of Barker factors (CourtListener / Descrybe) before citing any state case.
- Recompute every 120/180-day period from actual receipt dates.
- Legal information, not legal advice.

## Related skills
- `mo-criminal-case-roadmap` - case timeline
- `mo-bond-pretrial-release` - detention and the 120-day request
- `writs-mandamus-prohibition` - mandamus to enforce 545.780
- `mo-deadline-calculator` - day counting
