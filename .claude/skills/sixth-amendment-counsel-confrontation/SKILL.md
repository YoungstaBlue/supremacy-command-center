---
name: sixth-amendment-counsel-confrontation
description: Analyzes Sixth Amendment rights in criminal cases - appointed or chosen counsel, attachment, self-representation and waiver (Faretta), standby counsel, and Confrontation Clause limits on testimonial hearsay (Crawford). Use for "represent myself", "waive counsel", "Crawford", "lab report without analyst".
---

# Sixth Amendment: Counsel and Confrontation

Handles the two Sixth Amendment questions a pro se criminal defendant meets most: whether and how to proceed without a lawyer, and whether the prosecution can use out-of-court statements without live cross-examination.

## When to use
- Deciding to waive counsel, asking for standby counsel, or challenging a denial of appointed or chosen counsel.
- Police or informants questioned the accused after charges were filed.
- The state plans to use a lab report, 911 call, police interview, or statement of an absent witness.
- Not for: pre-charge custodial questioning (use `miranda-and-confessions`); ineffective-assistance claims after conviction (use `mo-post-conviction-relief`); general hearsay rules (use `hearsay-analyzer`).

## Gather first
- Charges and potential sentence (determines whether counsel must be appointed).
- Dates: arrest, first appearance, charging document, any questioning after charging.
- For confrontation: the exact statement, who made it, to whom, under what circumstances, and whether the declarant will testify.

## Workflow
### A. Right to counsel
1. **Scope.** Applies to criminal prosecutions where actual imprisonment results or a suspended sentence may be activated (Gideon v. Wainwright, 372 U.S. 335 (1963); Argersinger v. Hamlin, 407 U.S. 25 (1972); Scott v. Illinois, 440 U.S. 367 (1979); Alabama v. Shelton, 535 U.S. 654 (2002)). No Sixth Amendment right in civil cases.
2. **Attachment.** At the initiation of adversary judicial proceedings - including the first appearance before a magistrate where the accused learns the charge and liberty is restricted (Rothgery v. Gillespie County, 554 U.S. 191 (2008)). It is offense-specific.
3. **Critical stages.** After attachment, government agents may not deliberately elicit statements outside counsel's presence (Massiah v. United States, 377 U.S. 201 (1964)); the accused can waive after warnings (Montejo v. Louisiana, 556 U.S. 778 (2009)).
4. **Counsel of choice.** Erroneous denial of retained counsel of choice is structural error (United States v. Gonzalez-Lopez, 548 U.S. 140 (2006)); no right to choose appointed counsel.

### B. Self-representation
5. **Faretta v. California, 422 U.S. 806 (1975).** Right to self-representation upon a timely, clear, unequivocal request and a knowing, intelligent, voluntary waiver after the court warns of the dangers and disadvantages.
6. **Limits.** A court may require counsel for a defendant competent to stand trial but not competent to conduct trial himself (Indiana v. Edwards, 554 U.S. 164 (2008)). No constitutional right to hybrid representation; standby counsel may be appointed but cannot destroy the jury's perception that the defendant controls the case (McKaskle v. Wiggins, 465 U.S. 168 (1984)). Disruptive conduct can forfeit the right.
7. **Missouri.** Missouri requires a written waiver of counsel in specified circumstances - verify current RSMo 600.051 and Rule 31 text via `statute-lookup`. Mo. Const. art. I, sec. 18(a) independently guarantees the right to appear and defend in person and by counsel and to meet witnesses face to face.
8. **Consequences to warn about.** A defendant who self-represents cannot later claim ineffective assistance of himself; must follow rules of evidence and procedure; preserves error only by timely, specific objections.

### C. Confrontation Clause
9. **Testimonial?** Testimonial hearsay of an absent witness is admissible only if the witness is unavailable and the defendant had a prior opportunity to cross-examine (Crawford v. Washington, 541 U.S. 36 (2004)). Primary-purpose test: statements to police to meet an ongoing emergency are nontestimonial; statements to establish past events for prosecution are testimonial (Davis v. Washington, 547 U.S. 813 (2006)).
10. **Forensic reports.** Lab certificates are testimonial (Melendez-Diaz v. Massachusetts, 557 U.S. 305 (2009)); a surrogate analyst cannot substitute (Bullcoming v. New Mexico, 564 U.S. 647 (2011)); an expert who relays an absent analyst's statements as the basis of opinion is conveying them for their truth (Smith v. Arizona, 602 U.S. 779 (2024)).
11. **Door-opening and forfeiture.** Forfeiture by wrongdoing requires intent to prevent testimony (Giles v. California, 554 U.S. 353 (2008)). The "opening the door" rule cannot override confrontation (Hemphill v. New York, 595 U.S. 140 (2022)).
12. **Preserve.** Object specifically on Confrontation Clause grounds (not only hearsay) when the statement is offered; demand the analyst's live testimony if a notice-and-demand procedure applies.

## Output
- Counsel decision memo: charges/exposure; attachment date; waiver colloquy checklist; standby counsel request; risks.
- Confrontation chart: | Statement | Declarant | Testifying? | Testimonial (primary purpose)? | Prior cross? | Objection grounds |
- Draft headings for a motion in limine to exclude testimonial hearsay.

## Pitfalls
- Equivocal requests to proceed pro se - courts may deny them; make the request clear and early.
- Asking for "co-counsel" status - there is no right to hybrid representation.
- Objecting only "hearsay" and losing the constitutional ground on appeal.
- Missing any statutory notice-and-demand deadline for lab analysts.
- Assuming the Sixth Amendment applies in a civil or traffic-fine-only case.

## Verify before relying
- Pull verbatim RSMo 600.051, Mo. Const. art. I sec. 18(a), and applicable Missouri rules via `statute-lookup` (or Descrybe `search_laws_and_rules`).
- Confirm each case is good law (CourtListener / Descrybe).
- Recompute any notice or motion deadline from the scheduling order.
- Legal information, not legal advice; strongly consider counsel before waiving it.

## Related skills
- `miranda-and-confessions` - pre-charge interrogation rules.
- `hearsay-analyzer` - non-constitutional admissibility.
- `mo-post-conviction-relief` - Strickland ineffective-assistance claims.
- `mo-pro-se-courtroom-procedure` - conducting trial as a self-represented defendant.
- `lexcore` - criminal co-counsel workflow.
