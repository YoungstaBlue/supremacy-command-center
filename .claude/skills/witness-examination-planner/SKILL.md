---
name: witness-examination-planner
description: Plans direct and cross-examination outlines - witness goals, question order, leading-question rules, refreshing recollection, and impeachment with prior statements. Use for "cross-examine the officer", "direct exam outline", "questions for my witness", "deposition prep", or "how do I question a witness".
---

# Witness Examination Planner

Builds a written outline for each witness: what the testimony must prove, the questions in order, the exhibits
and prior statements at hand, and the impeachment ready if the witness strays.

## When to use
- Trial, evidentiary hearing, preliminary hearing, or deposition preparation
- Cross-examining a police officer, opposing party, or expert
- Calling a hostile or adverse witness
- Not for: the detailed law of impeachment (use `impeachment-and-credibility`); expert admissibility (use `expert-witness-challenge`)

## Gather first
- The witness's prior statements (reports, depositions, affidavits, recordings, texts) with page/line or timestamp
- The elements chart showing what this witness must prove or disprove
- Whether the witness is friendly, neutral, adverse/hostile, or an expert

## Workflow
1. Set goals: list 3-5 facts this witness must establish (direct) or concede (cross), each tied to an element or credibility point.
2. Direct examination:
   - Non-leading open questions (who, what, when, where, how, describe, explain). Leading is generally allowed
     only for preliminary matters, or with a hostile witness, adverse party, or someone identified with an adverse
     party (FRE 611(c); Missouri common law follows the same approach).
   - Order: introduce and humanize; set the scene; the event in chronological sequence; exhibits through the
     witness with foundation (see `authentication-foundation-builder`); close on the strongest point.
   - Front damaging facts briefly yourself.
   - Refreshing recollection: if the witness forgets, show a writing, let them read silently, take it back, ask if
     memory is refreshed (FRE 612; the other side may inspect it). If memory is not refreshed, consider recorded
     recollection (FRE 803(5)).
3. Cross-examination:
   - Leading questions only, one fact per question, answers you can prove. Scope is limited to the subject of
     direct and credibility in federal court (FRE 611(b)); Missouri permits cross on any matter in the case, but
     confirm current case law and the judge's practice.
   - Chapters: build concessions first (helpful facts the witness must admit), then attack (bias, perception,
     memory, inconsistency, omissions in reports, lack of personal knowledge).
   - Do not ask "why" or a question whose answer you do not know; do not ask the one question too many.
   - Officers: compare testimony to the report, the body-cam/dash-cam timestamps, CAD logs, and training/policy;
     omissions from a report written for the purpose of recording facts are fair game.
4. Impeachment with a prior inconsistent statement (commit, credit, confront): lock in today's testimony; build
   up the prior statement (when, where, purpose, accuracy, signed or under oath); read it verbatim and ask the
   witness to confirm. Missouri requires laying this foundation before extrinsic proof; FRE 613(b) requires an
   opportunity to explain or deny. See `impeachment-and-credibility`.
5. Redirect: only to repair cross; limited to its scope.
6. Depositions: broader, open-ended questions to discover; lock down every version of the story; get every
   document identified.
7. Rehearse your own witnesses without scripting their answers; advise them to tell the truth, listen to the
   question, and say "I don't know" when true.

## Output
- Per witness: Goals (numbered, tied to elements) / Exhibits to use (Ex. No., purpose) / Prior statements index
  (source, pinpoint, key quote) / Outline in chapters with questions numbered / Expected objections and responses
  / Impeachment cards (testimony expected, prior statement, cite)
- Cross questions written as one-fact leading statements ("You arrived at 10:42 p.m., correct?")

## Pitfalls
- Leading on direct; sustained objections break the narrative.
- Open-ended questions on cross that let the witness explain.
- Impeaching on trivial inconsistencies; it looks petty and wastes credibility.
- Not having the prior statement physically ready with the page and line.
- Witness coaching that crosses into suggesting false testimony; never do this.
- Forgetting to move exhibits into evidence after the witness identifies them.

## Verify before relying
- Pull current text of FRE 611-613 and 803(5) via `statute-lookup`; confirm Missouri scope-of-cross and
  impeachment foundation rules with current case law.
- Check the judge's procedures on time limits, approaching witnesses, and use of exhibits.
- Legal information, not legal advice.

## Related skills
- `impeachment-and-credibility` — legal rules for each impeachment method
- `objection-playbook` — objections during examination
- `evidence-timeline-builder` — prior statements and conflicts indexed
- `exhibit-list-and-trial-binder` — outlines and exhibits in the binder
- `mo-preliminary-hearing` — cross-examination to lock in testimony early
