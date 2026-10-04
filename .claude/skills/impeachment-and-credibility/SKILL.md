---
name: impeachment-and-credibility
description: Analyzes attacking or supporting witness credibility - bias, prior inconsistent statements, prior convictions (RSMo 491.050 vs FRE 609), character for truthfulness, contradiction, and rehabilitation. Use for "impeach the witness", "he lied before", "prior conviction", "bias", or "prior inconsistent statement".
---

# Impeachment and Credibility

Identifies every lawful way to undermine (or rehabilitate) a witness's credibility, the foundation each
method requires, and the key Missouri-federal differences.

## When to use
- A witness's testimony conflicts with a report, deposition, text, recording, or earlier testimony
- A witness has a criminal record, a deal with the prosecution, money at stake, or a relationship to a party
- Your own witness is about to be impeached and needs rehabilitation
- Not for: building the full question outline (use `witness-examination-planner`)

## Gather first
- Every prior statement of the witness with exact source and pinpoint
- Criminal history records (convictions only, with dates and dispositions) and any benefits, deals, or pending charges
- Forum (Missouri or federal) and civil or criminal case

## Workflow
1. Bias, interest, motive: always relevant and provable by extrinsic evidence after foundation. Includes deals,
   leniency, pending charges, payment, employment, relationships, hostility. United States v. Abel, 469 U.S. 45
   (1984). In criminal cases, cutting off bias cross can violate confrontation: Davis v. Alaska, 415 U.S. 308 (1974).
   Prosecutors must disclose impeachment material (see `brady-giglio-demands`).
2. Prior inconsistent statements:
   - Foundation (commit, credit, confront): pin down current testimony, establish the prior statement's time,
     place, and circumstances, then confront with it.
   - Missouri: lay the foundation with the witness before offering extrinsic proof. Prior inconsistent statements
     are admissible as substantive evidence, not just impeachment: RSMo 491.074 (criminal cases) and Rowe v.
     Farmers Ins. Co., 699 S.W.2d 423 (Mo. banc 1985) (civil).
   - Federal: FRE 613; extrinsic evidence admissible only if the witness gets a chance to explain or deny and the
     adverse party can examine. Substantive use only if the statement was under penalty of perjury at a prior
     proceeding (FRE 801(d)(1)(A)); otherwise impeachment only, with a limiting instruction.
   - Extrinsic evidence is not allowed on collateral matters.
3. Prior convictions:
   - Missouri: RSMo 491.050 allows proof of prior criminal convictions to affect credibility in civil and criminal
     cases. Misdemeanors count, and there is generally no prejudice balancing, unlike FRE 609. Inquiry is usually
     limited to the nature, date, place, and sentence of the conviction; details open up only in limited
     circumstances (verify current case law). A suspended imposition of sentence is generally not a conviction for
     this purpose (verify).
   - Federal: FRE 609: felonies (balancing; stricter test for a criminal defendant), any crime whose elements
     required proof of a dishonest act or false statement (automatic), and a presumptive bar on convictions over
     10 years old absent notice and a specific showing. Juvenile adjudications are restricted.
4. Character for truthfulness: opinion or reputation for untruthfulness (FRE 608(a)). Specific instances of
   untruthful conduct may be asked about on cross in the court's discretion but not proved by extrinsic evidence
   (FRE 608(b)). Missouri case law is generally more restrictive about specific-act inquiries; verify.
5. Capacity: perception (lighting, distance, intoxication, vantage point), memory, and ability to communicate.
6. Contradiction: other evidence (video, documents, other witnesses) showing the testimony is wrong.
7. Report omissions: a detail critical to the testimony that is missing from a report the witness wrote to record
   the facts can be treated as an inconsistency.
8. Impeaching your own witness: allowed in federal court (FRE 607). Missouri historically limited this; check
   current Missouri law before attempting it.
9. Rehabilitation: only after attack. Prior consistent statements to rebut a charge of recent fabrication or
   improper motive (FRE 801(d)(1)(B) requires the statement to predate the motive); evidence of truthful
   character only after character for truthfulness is attacked (FRE 608(a)).

## Output
| Witness | Method | Testimony expected | Impeaching fact/statement | Source + pinpoint | Foundation steps | Extrinsic proof allowed? | Substantive or impeachment only | Risk |
|---|---|---|---|---|---|---|---|---|
- Then impeachment cards for trial: testimony to lock in, exact prior quote, page/line, exhibit number.

## Pitfalls
- Confronting without first committing the witness to today's version.
- Paraphrasing the prior statement instead of reading it verbatim.
- Offering extrinsic proof on a collateral point, or before the foundation is laid in Missouri.
- Using arrests, charges without convictions, or SIS dispositions as "convictions."
- Applying FRE 609 balancing arguments in Missouri state court, or 491.050 in federal court.
- Opening the door: impeaching a witness can allow the other side to rehabilitate with otherwise inadmissible evidence.

## Verify before relying
- Pull verbatim RSMo 491.050 and 491.074 and FRE 607-609, 613, 801(d)(1) via `statute-lookup`.
- Confirm Missouri case law on conviction-impeachment scope, SIS status, and impeaching one's own witness on CourtListener.
- Verify every conviction against certified court records before using it.
- Legal information, not legal advice.

## Related skills
- `witness-examination-planner` — fitting impeachment into the cross outline
- `brady-giglio-demands` — obtaining impeachment material from the prosecution
- `evidence-timeline-builder` — finding inconsistencies across sources
- `hearsay-analyzer` — substantive use of prior statements
- `mo-evidence-rules` — Missouri sources and FRE differences
