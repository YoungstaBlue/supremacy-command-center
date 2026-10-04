---
name: mo-administrative-appeals
description: Guides judicial review of Missouri agency decisions under RSMo chapter 536 - contested vs. noncontested cases, exhaustion, AHC (RSMo 621), deadlines, venue, and standard of review. Use for "appeal agency decision", "Administrative Hearing Commission", license revoked, benefits denied, or "petition for review".
---

# Missouri Administrative Appeals

Moves a Missouri agency decision into court correctly: classifies the case, confirms exhaustion and finality, finds the controlling review statute and deadline, and frames the issues under the right standard of review.

## When to use
- A Missouri state agency, board, commission, or local body denied, revoked, suspended, or fined
- Appealing to or from the Administrative Hearing Commission (AHC)
- Unemployment, workers' compensation, professional license, driver's license, Medicaid/benefits, or zoning decisions
- Not for: federal agency decisions (Administrative Procedure Act, 5 U.S.C. 701-706; consider `federal-subject-matter-jurisdiction`); appeals from a circuit court judgment (use `mo-appeals-procedure`)

## Gather first
- The final decision document and the exact date it was mailed or delivered
- Which agency and which statute authorized the decision (the program's own chapter)
- Whether there was an evidentiary hearing with a record (testimony, exhibits, transcript)

## Workflow
1. **Find the specific review statute first.** Many programs have their own review path that overrides chapter 536. Examples to check (pull text before relying):
   - Unemployment (Labor and Industrial Relations Commission) -> appeal to the Court of Appeals under RSMo 288.210, short deadline
   - Workers' compensation (Commission final award) -> Court of Appeals under RSMo 287.495
   - Driver's license suspension/revocation -> trial de novo in circuit court under the Chapter 302 provisions
   - Professional licensing -> AHC under RSMo chapter 621, then review under 621.145 / chapter 536
   If the program statute is silent, chapter 536 governs.
2. **Classify contested vs. noncontested** (RSMo 536.010 definitions).
   - Contested case: law requires a hearing where legal rights are determined after notice and an opportunity to be heard. Review is on the agency record (536.100-536.140).
   - Noncontested case: no required hearing. Review is by original action in circuit court under RSMo 536.150; the court hears evidence and decides whether the decision is unconstitutional, unlawful, unreasonable, arbitrary, capricious, or an abuse of discretion.
3. **Confirm exhaustion and finality.** 536.100 limits review to a person aggrieved by a final decision who has exhausted all administrative remedies. List every internal step (reconsideration, appeal to board/commission, AHC) and confirm each was used. Recognized exceptions are narrow (e.g., futility, facial constitutional challenge to a statute an agency cannot decide) — research before relying.
4. **Calendar the deadline.** Default contested-case petition for review: within 30 days after the mailing or delivery of notice of the final decision (RSMo 536.110). Program statutes often shorten this. Deadlines here are generally treated as jurisdictional — a late petition is dismissed. Use `mo-deadline-calculator`.
5. **Venue.** Under 536.110 venue is generally the circuit court of the county of the petitioner's residence or Cole County (verify current text and any program-specific venue rule).
6. **Draft the petition for review (contested).** Caption naming agency as respondent; agency decision identified and attached; jurisdiction/exhaustion/timeliness allegations; specific grounds tracking 536.140.2; relief (reverse, remand, or modify). Request the certified record from the agency.
7. **Frame the standard of review.** RSMo 536.140.2 lets the court decide whether the action:
   - violates constitutional provisions; exceeds statutory authority or jurisdiction; is unsupported by competent and substantial evidence on the whole record; is unauthorized by law; was made upon unlawful procedure or without a fair trial; is arbitrary, capricious, or unreasonable; or involves an abuse of discretion.
   - Review the whole record, not only evidence supporting the decision (Hampton v. Big Boy Steel Erection, 121 S.W.3d 220 (Mo. banc 2003), workers' compensation context). Credibility findings get deference; questions of law are reviewed de novo.
   - On further appeal, the appellate court reviews the agency decision, not the circuit court judgment (verify current rule for AHC-board cases).
8. **Stay.** Filing for review does not automatically stay the decision; request a stay from the agency or court under 536.120 if available (verify).
9. **Preserve.** Raise every issue, including constitutional issues, at the earliest agency stage; unraised issues are often waived on review.

## Output
- Classification memo: program statute, contested/noncontested, review court, deadline, venue
- Exhaustion checklist with dates
- Petition for review skeleton with 536.140.2 grounds as headings
- Issues table: | Issue | Record cite | Standard of review | Preserved? |

## Pitfalls
- Filing in circuit court when the program statute sends review to the Court of Appeals (or vice versa)
- Counting from the hearing date instead of mailing/delivery of the final decision
- Skipping a reconsideration or board-level appeal (failure to exhaust)
- Arguing new facts on a contested-case record review
- Treating a noncontested case like a record review and failing to present evidence in circuit court

## Verify before relying
- Pull verbatim RSMo 536.010, 536.100-536.150, 621.145 and the program statute via `statute-lookup` (or Descrybe `search_laws_and_rules`); check case law on exhaustion and standard of review is current.
- Recompute the deadline from the actual mailing/delivery date.
- Legal information, not legal advice; license and benefits losses are high-stakes — consider counsel or legal aid.

## Related skills
- `mo-deadline-calculator` — compute the petition deadline
- `standard-of-review-finder` — issue-by-issue standards
- `due-process-analyzer` — notice/hearing defects in the agency process
- `writs-mandamus-prohibition` — when an agency refuses to act at all
