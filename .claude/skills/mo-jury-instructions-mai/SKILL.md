---
name: mo-jury-instructions-mai
description: Selects, modifies, and objects to Missouri Approved Instructions (MAI) in civil jury trials under Rules 70.02 and 70.03 - verdict directors, converses, damages, not-in-MAI instructions, preserving error. Use for "jury instructions", "MAI", "verdict director", or "instruction conference".
---

# Missouri Jury Instructions (MAI)

Build a correct Missouri civil instruction packet from MAI, and preserve every instruction objection for appeal.

## When to use
- A Missouri civil jury trial is set and proposed instructions are due.
- The user must object to the opponent's instructions at the instruction conference.
- An appeal or new-trial motion turns on instructional error.
- Not for: Missouri criminal cases (MAI-CR applies, with Rule 28 procedure) - flag and research separately; federal trials (Eighth Circuit Model Civil Jury Instructions) - see `federal-civil-discovery` and trial skills.

## Gather first
- The pleaded claims and affirmative defenses, and the evidence actually admitted (instructions must be supported by substantial evidence).
- The court's deadline and format for proposed instructions (numbering, copies, citations to MAI on the court's copy only, clean jury copies).
- The current MAI edition and supplements available to the user (Missouri Courts publishes MAI).

## Workflow
1. Rule 70.02: whenever MAI contains an instruction applicable to the case, use it to the exclusion of other instructions; modify only as the Notes on Use permit. Giving an instruction in violation of the rule is presumed prejudicial error unless shown otherwise (verify the text on prejudice). Where MAI has no applicable instruction, a not-in-MAI instruction must be simple, brief, impartial, free from argument, and not submit detailed evidentiary facts.
2. Assemble the packet in the order MAI's general instructions prescribe: introductory and general instructions, burden of proof, verdict director(s), converse(s), affirmative defense instructions, damages, comparative fault if applicable, and verdict forms. Read each instruction's Notes on Use and Committee Comment before modifying.
3. Verdict director: one per claim against each defendant; each paragraph submits an ultimate fact that the evidence supports. Disjunctive submissions require evidence supporting each alternative. Tie each paragraph to a pleaded element.
4. Converse instructions: a defendant may submit converse instructions per MAI's rules (true converse vs. affirmative converse); check limits on the number and form.
5. Damages: select the MAI damages instruction matching the claim; punitive damages require a separate submission and verdict form (and the statutory pleading/proof rules for punitive damages - see `damages-calculator`).
6. Prepare the court's copy (with MAI number and "modified" notation, party designation) and a clean jury copy for each instruction, per local practice.
7. Instruction conference: object to each opposing instruction on the record, specifically, before the jury retires; state the distinct grounds (Rule 70.03). A general objection preserves nothing. Make sure the refused instruction you tendered is in the record.
8. Post-trial preservation: in jury cases, instructional error must also be raised in the motion for new trial (Rule 70.03; Rule 78.07). Plain error review is rare.
9. Review tests to argue: whether the instruction was supported by substantial evidence, misstated the law, misdirected or confused the jury, and whether prejudice resulted.

## Output
- Instruction packet index: No. | MAI number / not-in-MAI | Title | Offered by | Given/Refused/Modified | Objection made (Y/N, grounds).
- Element-to-paragraph map for each verdict director.
- Objection script for the conference: "Plaintiff objects to Instruction No. __ because [specific ground]; it [misstates law / lacks evidentiary support / deviates from MAI __ Notes on Use] and is prejudicial because [reason]."

## Pitfalls
- Drafting a custom instruction when an MAI instruction applies.
- Modifying MAI language beyond what the Notes on Use permit.
- Submitting a theory with no substantial evidence supporting every element.
- Making only general objections, or objecting after the jury retires.
- Failing to repeat instruction objections in the motion for new trial.
- Not ensuring refused instructions are marked and kept in the legal file.
- Using an outdated MAI version.
- Submitting a verdict director that assumes a disputed fact instead of requiring the jury to find it.
- Forgetting that the verdict form must match the instructions submitted (parties, claims, comparative fault).
- Not reading the opposing packet until the conference - review it as soon as it is exchanged.

## Verify before relying
- Pull verbatim Rules 70.02, 70.03, 78.07 via `statute-lookup`; check the current MAI instruction, Notes on Use, and Committee Comment from the official Missouri Courts publication.
- Confirm any case cited on instructional error on CourtListener for subsequent treatment.
- Recompute instruction submission deadlines from the trial order.
- Legal information, not legal advice; instruction errors are a top reason for retrial - consider counsel.

## Related skills
- `mo-pretrial-and-trial-prep` - schedule and packet deadlines.
- `elements-checklist-builder` - elements that drive the verdict director.
- `mo-post-trial-motions` - preserving instruction error in the new-trial motion.
- `damages-calculator` - damages and punitive damages submissions.
- `standard-of-review-finder` - how instruction error is reviewed.
