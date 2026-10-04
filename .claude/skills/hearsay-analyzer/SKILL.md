---
name: hearsay-analyzer
description: Analyzes whether a statement is hearsay and finds exclusions and exceptions under FRE 801-807 and Missouri common law, plus Confrontation Clause limits. Use for "is this hearsay", "hearsay objection", excited utterance, business records exception, party admission, or police report hearsay.
---

# Hearsay Analyzer

Runs a statement through the hearsay definition, the non-hearsay exclusions, the exceptions, and (in criminal
cases) the Confrontation Clause, and says how to offer it or object to it in federal and Missouri courts.

## When to use
- Deciding whether a text, email, report, 911 call, recording, or out-of-court remark can come in
- Preparing a hearsay objection or response before a hearing or trial
- Layered statements (a report quoting a witness)
- Not for: the general Missouri evidence landscape (use `mo-evidence-rules`); authenticity of the item (use `authentication-foundation-builder`)

## Gather first
- Exact words of the statement, who said it, to whom, when, and the circumstances (stress, time lapse, purpose)
- What it is offered to prove, and by which party
- Forum (federal or Missouri) and case type (civil or criminal)

## Workflow
1. Is it a "statement"? An assertion, oral, written, or assertive conduct (FRE 801(a)). Questions, commands,
   and non-assertive conduct usually are not.
2. Is it offered for its truth? If offered for effect on the listener, notice, knowledge, verbal act (contract
   words, threats, defamatory words), or impeachment, it is not hearsay. Request a limiting instruction (FRE 105).
3. Exclusions (FRE 801(d)) — not hearsay by definition:
   - 801(d)(1): prior statement of a testifying witness subject to cross: inconsistent and under oath at a prior
     proceeding; consistent and offered to rebut fabrication or rehabilitate; identification.
   - 801(d)(2): opposing party's statement: own statement, adopted, authorized, agent/employee within scope,
     coconspirator during and in furtherance.
   - Missouri: party admissions are admissible at common law; prior inconsistent statements are substantive
     evidence (RSMo 491.074 in criminal cases; Rowe v. Farmers Ins. Co., 699 S.W.2d 423 (Mo. banc 1985) in civil),
     broader than FRE 801(d)(1)(A).
4. Exceptions regardless of availability (FRE 803) — most used: present sense impression (1), excited utterance
   (2), then-existing state of mind or condition (3), medical diagnosis/treatment (4), recorded recollection (5),
   business records (6) with absence of record (7), public records (8), learned treatises (18), judgment of
   previous conviction (22).
   - Missouri recognizes most of these at common law; business records are statutory (RSMo 490.680, 490.692).
     Confirm Missouri case law for any exception before relying on the FRE label.
5. Exceptions requiring unavailability (FRE 804): first establish unavailability under 804(a) (privilege,
   refusal, lack of memory, death/illness, absence despite process). Then: former testimony (b)(1), dying
   declaration (b)(2), statement against interest (b)(3) (criminal-exposure statements offered to exculpate need
   corroboration), forfeiture by wrongdoing (b)(6).
6. Residual exception (FRE 807): federal only; requires sufficient guarantees of trustworthiness, more probative
   than other reasonably available evidence, and advance written notice. Missouri has no general residual exception.
7. Hearsay within hearsay (FRE 805): every layer needs its own exclusion or exception. Police reports commonly
   fail at the bystander layer.
8. Criminal cases — Confrontation Clause: testimonial hearsay of a non-testifying declarant is barred unless the
   declarant is unavailable and the defendant had a prior opportunity to cross-examine. Crawford v. Washington,
   541 U.S. 36 (2004). Statements to police to meet an ongoing emergency are generally nontestimonial; statements
   describing past events for prosecution are testimonial. Davis v. Washington, 547 U.S. 813 (2006).
   Missouri Constitution art. I, section 18(a) also guarantees confrontation.

## Output
| # | Statement (quoted) | Declarant | Offered for | Hearsay? | Exclusion/exception | Foundation needed | Confrontation issue | Ruling risk |
|---|---|---|---|---|---|---|---|---|
- Then a short script: the objection ("Objection, hearsay") or the offer ("Offered not for its truth but to show...").

## Pitfalls
- Objecting only "hearsay" when the real problem is a second layer or a confrontation violation; state each ground.
- Assuming every business record qualifies: the maker must have a business duty, and the record must be made at
  or near the time in the regular course. Litigation-prepared documents are suspect.
- Not laying the stress/time foundation for an excited utterance.
- Forgetting that "not for the truth" evidence still needs relevance for that non-truth purpose.
- Failing to give 807 notice in federal court.

## Verify before relying
- Pull current text of FRE 801-807 and RSMo 490.680, 490.692, 491.074 via `statute-lookup` or the official source.
- Check Crawford/Davis progeny for the specific statement type (lab reports, forensic interviews) on CourtListener.
- Legal information, not legal advice.

## Related skills
- `mo-evidence-rules` — Missouri source map and FRE differences
- `authentication-foundation-builder` — proving the item is what you claim
- `objection-playbook` — timing and preserving the objection
- `sixth-amendment-counsel-confrontation` — deeper Confrontation Clause analysis
- `impeachment-and-credibility` — prior inconsistent statements used to impeach
