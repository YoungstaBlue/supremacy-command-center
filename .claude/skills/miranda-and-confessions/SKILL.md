---
name: miranda-and-confessions
description: Analyzes whether a defendant's statements are admissible - Miranda custody and interrogation, warnings, waiver, invoking silence or counsel, question-first tactics, and voluntariness. Use for "Miranda rights", "never read my rights", "confession", "suppress my statement", "asked for a lawyer".
---

# Miranda and Confessions

Works through the separate Miranda and voluntariness doctrines to decide whether a statement can be suppressed and what use the prosecution may still make of it.

## When to use
- A statement to police (written, recorded, or reported) will be used in a criminal case.
- The person was questioned without warnings, kept talking after asking for a lawyer, or was pressured, threatened, or promised leniency.
- Not for: physical evidence from an illegal search (use `fourth-amendment-analyzer`); questioning after charges by a government agent, which raises the Sixth Amendment (use `sixth-amendment-counsel-confrontation`).

## Gather first
- Recording or transcript of the questioning; reports; the signed waiver form if any.
- Setting: location, duration, number of officers, restraints, whether told free to leave, whether under arrest, age and condition of the person.
- Exact words of any request for a lawyer or to stop talking, and what officers did next.

## Workflow
1. **Two separate tracks.** Miranda (Fifth Amendment prophylactic rule, Miranda v. Arizona, 384 U.S. 436 (1966)) and due-process voluntariness. Run both; a Mirandized statement can still be involuntary.
2. **Custody (objective).** Would a reasonable person have felt not free to terminate questioning and leave, and does the environment present the coercive pressures of station-house questioning (Howes v. Fields, 565 U.S. 499 (2012))? Factors: told free to leave or not; restraints; duration; location; number of officers; police-dominated atmosphere; whether arrested at the end. A child's age is relevant when known or objectively apparent (J.D.B. v. North Carolina, 564 U.S. 261 (2011)). Ordinary traffic stops are generally not custody unless they escalate.
3. **Interrogation.** Express questioning or its functional equivalent - words or actions the police should know are reasonably likely to elicit an incriminating response (Rhode Island v. Innis, 446 U.S. 291 (1980)). Volunteered statements are not interrogation. Booking questions are usually excluded.
4. **Warnings adequate?** Right to remain silent; anything said can be used; right to an attorney present; appointed if indigent. Exact wording not required if the substance is conveyed.
5. **Waiver.** State must show by a preponderance that waiver was knowing, intelligent, and voluntary (Colorado v. Connelly, 479 U.S. 157 (1986); Lego v. Twomey, 404 U.S. 477 (1972) on preponderance). Waiver can be implied from understanding plus a course of conduct (Berghuis v. Thompkins, 560 U.S. 370 (2010)).
6. **Invocation.**
   - Counsel: must be unambiguous (Davis v. United States, 512 U.S. 452 (1994)); then questioning must stop and cannot resume unless the suspect initiates (Edwards v. Arizona, 451 U.S. 477 (1981)); Edwards protection lapses after a 14-day break in custody (Maryland v. Shatzer, 559 U.S. 98 (2010)).
   - Silence: must also be unambiguous (Berghuis); police must "scrupulously honor" it (Michigan v. Mosley, 423 U.S. 96 (1975)).
7. **Two-step / question-first.** Deliberate unwarned questioning followed by warnings and repetition can require suppression of the warned statement (Missouri v. Seibert, 542 U.S. 600 (2004)); absent deliberate strategy, a later warned statement may be admissible (Oregon v. Elstad, 470 U.S. 298 (1985)).
8. **Exceptions.** Public safety (New York v. Quarles, 467 U.S. 649 (1984)). Unwarned but voluntary statements may be used to impeach a testifying defendant (Harris v. New York, 401 U.S. 222 (1971)).
9. **Voluntariness (due process).** Totality: police coercion is required (Connelly), plus the person's characteristics (age, education, intoxication, mental illness), length, deprivation of sleep/food, threats, promises of leniency. Involuntary statements are inadmissible for any purpose, including impeachment. Defendant is entitled to a hearing and a ruling on voluntariness before the jury hears it (Jackson v. Denno, 378 U.S. 368 (1964)).
10. **Remedy limits.** A Miranda violation is a suppression remedy, not a basis for a 1983 damages claim (Vega v. Tekoh, 597 U.S. 134 (2022)); coercion claims may still proceed under other theories.

## Output
- Custody factor table: | Factor | Facts | Points toward custody? |
- Statement-by-statement chart: | Time | Statement | Custody? | Interrogation? | Warned? | Waived? | Invoked? | Voluntary? | Admissible for what purpose |
- Suppression argument outline with requested findings for the court.

## Pitfalls
- Assuming "no warnings" alone means suppression - no custody or no interrogation means no Miranda violation.
- Ambiguous invocations ("maybe I should get a lawyer") are not invocations.
- Forgetting that physical fruits of a voluntary unwarned statement are generally admissible.
- Failing to file pretrial and to object again at trial (Missouri requires a timely trial objection to preserve).
- Testifying at trial and opening the door to impeachment with a suppressed (but voluntary) statement.
- Arguing the officer's subjective belief about custody; the test is objective.
- Overlooking that a request for a lawyer must be made during or in anticipation of custodial interrogation to trigger Edwards.
- Not requesting a recording of the full interview; gaps in the recording are key voluntariness evidence.
- Ignoring juvenile-specific statutes and parental-notification rules when the person was a minor.

## Verify before relying
- Pull verbatim RSMo 542.296 and any rule cited via `statute-lookup` (or Descrybe `search_laws_and_rules`).
- Check each case for subsequent treatment and find a Missouri or 8th Circuit case applying custody factors to similar facts before citing (CourtListener / Descrybe).
- Recompute pretrial motion deadlines from the court's order.
- Legal information, not legal advice; consult counsel or the public defender.

## Related skills
- `mo-motion-to-suppress` - Missouri motion format and hearing prep.
- `sixth-amendment-counsel-confrontation` - post-charge right to counsel during questioning.
- `fourth-amendment-analyzer` - statements as fruit of an illegal arrest.
- `lexcore` - criminal suppression co-counsel workflow.
