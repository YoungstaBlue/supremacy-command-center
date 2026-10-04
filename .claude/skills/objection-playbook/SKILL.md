---
name: objection-playbook
description: Gives a trial and hearing objection playbook - common objections and grounds, when and how to object, offers of proof, and preserving error for appeal in Missouri and federal court. Use for "how do I object", "objection list", "preserve error", "offer of proof", "motion in limine", or "plain error".
---

# Objection Playbook

Tells you what to say, when to say it, and what else must happen so an evidentiary ruling can be reviewed on
appeal.

## When to use
- Preparing for a trial, evidentiary hearing, deposition, or bench trial
- Responding when the other side objects to your evidence
- Checking whether an issue was preserved before a post-trial motion or appeal
- Not for: deep analysis of a single ground (use `hearsay-analyzer`, `authentication-foundation-builder`, `privilege-analyzer`)

## Gather first
- Forum (Missouri or federal) and civil or criminal; jury or bench
- Any rulings on motions in limine and the pretrial order
- The specific evidence or questions you expect to fight about

## Workflow
1. Preservation rule: object timely (as soon as the ground is apparent, before the answer if possible) and
   specifically (state the ground). Get a ruling. If the objection is sustained against your evidence, make an
   offer of proof. FRE 103(a); Missouri common law is similar and stricter in practice.
2. Motions in limine:
   - Missouri: a ruling in limine is interlocutory and preserves nothing. Object again at trial when the evidence
     is offered, and make an offer of proof when your evidence is excluded.
   - Federal: once the court rules definitively on the record, a party need not renew the objection or offer
     (FRE 103(b)). If the ruling is tentative, renew at trial.
3. Common objections (state the word, then the short ground):
   - Form: leading (on direct), compound, assumes facts not in evidence, calls for speculation, argumentative,
     asked and answered, narrative, vague/ambiguous, misstates the evidence.
   - Substance: relevance (FRE 401-402); unfair prejudice/confusion/waste (FRE 403); hearsay (FRE 802); lack of
     personal knowledge (FRE 602); improper lay opinion (FRE 701); improper expert opinion or undisclosed opinion
     (FRE 702, 26(a)(2)); lack of foundation/authentication (FRE 901); best evidence (FRE 1002); character or
     other-acts evidence (FRE 404); privilege (FRE 501); subsequent remedial measures (FRE 407); settlement
     communications (FRE 408); improper impeachment (FRE 608-609, 613); beyond the scope of direct (FRE 611(b)).
   - Missouri: use the same plain-language grounds and cite Missouri case law or statute rather than FRE numbers.
4. Responding to an objection: state the purpose and route ("offered for notice, not truth"; "business record,
   foundation laid by custodian"), or rephrase. Ask to approach if argument is needed outside the jury's hearing.
5. Offer of proof when excluded: (a) question-and-answer with the witness outside the jury's presence, or (b) a
   specific narrative statement of what the evidence would show, its purpose, and why it is admissible. Mark and
   tender excluded exhibits so they are in the record.
6. Continuing objection: request one on the record for a line of questioning so you need not object repeatedly.
7. After the verdict:
   - Missouri jury-tried civil cases: allegations of error must be in a timely motion for new trial to be
     preserved (Rule 78.07); criminal: Rule 29.11(d). Check Rule 78.07 for the bench-trial differences.
   - Federal: no new-trial motion is needed to preserve evidentiary error for appeal.
8. Unpreserved error: review only for plain error resulting in manifest injustice or miscarriage of justice
   (Missouri Rules 84.13(c) civil, 30.20 criminal; federal FRE 103(e), Fed. R. Crim. P. 52(b)). Rarely granted.

## Output
- One-page objection card: Objection / Say this / Rule (forum-specific) / Typical response
- Preservation checklist per contested item: Motion in limine filed / Ruling / Objected at trial / Ruling /
  Offer of proof made / Exhibit tendered / In motion for new trial (Missouri) / Status
- Offer-of-proof script for each piece of evidence at risk of exclusion

## Pitfalls
- Relying on a Missouri in limine ruling and not objecting at trial.
- General "objection" with no ground, or the wrong ground; on appeal you are limited to the ground stated.
- Excluded evidence with no offer of proof, leaving the appellate court nothing to review.
- Objecting so often that the jury turns against you; save it for things that matter.
- Omitting an error from the Missouri motion for new trial in a jury case.
- Arguing with the judge after a ruling instead of making the record and moving on.

## Verify before relying
- Pull current text of FRE 103 and the cited FRE, and Missouri Rules 78.07, 29.11, 84.13, 30.20 via `statute-lookup`.
- Confirm Missouri preservation case law on CourtListener for the specific issue.
- Recompute the motion-for-new-trial deadline from the judgment date.
- Legal information, not legal advice.

## Related skills
- `mo-pro-se-courtroom-procedure` — making a record and courtroom conduct
- `mo-post-trial-motions` — motion for new trial content and timing
- `hearsay-analyzer` — the most common ground in detail
- `standard-of-review-finder` — what review the preserved error receives
- `mo-evidence-rules` — Missouri sources to cite instead of FRE
