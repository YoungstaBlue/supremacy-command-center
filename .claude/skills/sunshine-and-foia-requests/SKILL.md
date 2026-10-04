---
name: sunshine-and-foia-requests
description: Drafts Missouri Sunshine Law (RSMo ch. 610) records requests and federal FOIA (5 U.S.C. 552) requests, fee waivers, appeals, and enforcement plans. Use for "Sunshine request", "FOIA request", "open records", police reports, bodycam, denied request, or records appeal.
---

# Sunshine Law and FOIA Requests

Gets government records into the user's hands: picks the right law (Missouri Sunshine Law vs. federal FOIA), drafts a precise request, tracks the response clock, and builds the appeal or enforcement path when the agency stalls or denies.

## When to use
- Requesting records from a Missouri city, county, police department, school district, state agency, or board
- Requesting records from a federal agency (FBI, DOJ, SSA, VA, DHS, etc.)
- An agency missed its deadline, demanded large fees, redacted heavily, or denied the request
- Not for: records held by the opposing party in a lawsuit (use `mo-discovery-requests` / `federal-civil-discovery`); court case files (use Case.net / PACER and the clerk)

## Gather first
- Which body holds the records (exact agency name, division, custodian of records if known)
- What records, with date range, names, incident/report numbers, and preferred format (electronic)
- Whether the records relate to a pending case or criminal investigation (affects closure exceptions)

## Workflow
1. **Pick the statute.**
   - Missouri state/local "public governmental body" -> Sunshine Law, RSMo 610.010-610.035. Courts are covered only when acting in an administrative capacity; adjudicative case records go through the court clerk (verify the current definition in 610.010).
   - Federal executive agency -> FOIA, 5 U.S.C. 552. FOIA does not reach Congress, federal courts, or state/local agencies.
   - Privacy Act (5 U.S.C. 552a) is an additional route for records about yourself held by a federal agency; cite both in a first-party request.
2. **Identify the custodian.** Sunshine: each body must designate a custodian; address the request to that person (in writing, email acceptable, keep proof of receipt). FOIA: use the agency's FOIA office or portal listed on its FOIA page; follow the agency's own FOIA regulations in the CFR.
3. **Draft a request that cannot be misread.**
   - Reasonably describe records: type, date range, subject, names, report numbers. Avoid "any and all documents" with no limits; it invites delay and fees.
   - Ask for electronic copies in native format where possible.
   - Ask that any withheld portion be identified with the specific exemption claimed and that reasonably segregable portions be released.
   - Sunshine: cite RSMo 610.023 response duty; ask for a fee estimate before costs exceed a stated amount (fees governed by 610.026 — pull current text for rate limits).
   - FOIA: state fee category (individual = "all other" requester), request a fee waiver under 552(a)(4)(A)(iii) if disclosure is in the public interest and not primarily commercial; request expedited processing under 552(a)(6)(E) only if you can certify a compelling need.
4. **Calendar the response clock.**
   - Sunshine: custodian must act no later than the end of the third business day after receipt, or explain the delay and give the earliest available date (610.023 — verify).
   - FOIA: agency determination due within 20 business days (552(a)(6)(A)(i)); may extend 10 business days for "unusual circumstances" with written notice (552(a)(6)(B)).
5. **Police and investigative records (Missouri).** RSMo 610.100 treats arrest and incident reports as generally open and investigative reports as closed until the investigation becomes inactive. Request incident report and arrest report separately from investigative file. Note statutory paths for persons involved in an incident to obtain closed records — pull 610.100 verbatim before relying.
6. **Handle denial or silence.**
   - Sunshine: no administrative appeal is required. Ask the custodian in writing for the specific closure provision (610.023 requires a written explanation on request). Options: complaint to the Missouri Attorney General's Sunshine Law office, or suit in circuit court under RSMo 610.027 (penalties and fee-shifting for knowing or purposeful violations; strict limitations period — verify the current period in 610.027 before relying).
   - FOIA: file an administrative appeal within the agency's stated window (statute requires at least 90 days after adverse determination, 552(a)(6)(A)(i)(III)(aa)). Appeal decision due in 20 business days. Exhaust, then sue in federal district court (552(a)(4)(B)); review is de novo and the agency bears the burden to justify withholding. In litigation, request a Vaughn index (Vaughn v. Rosen, 484 F.2d 820 (D.C. Cir. 1973)).
   - FOIA mediation: Office of Government Information Services (OGIS) is a non-binding option; it does not toll your suit rights.
7. **Map exemptions.** Sunshine: closure grounds listed in RSMo 610.021 (e.g., litigation, personnel, legal work product) are permissive, not mandatory, and construed narrowly (610.011). FOIA: nine exemptions in 552(b)(1)-(9); for law-enforcement records, (b)(7)(A)-(F). Identify which ones the agency likely claims and pre-argue why they do not fit.

## Output
- Request letter: heading (agency, custodian, date), statutory basis, numbered record descriptions, format, fee language, segregability request, contact block
- Tracking table: | Request | Sent | Method/proof | Due date | Response | Next step |
- If denied: appeal letter (FOIA) or demand/complaint outline (Sunshine) with exemption-by-exemption rebuttal

## Pitfalls
- Sending to the wrong body or not to the custodian; no proof of receipt
- Vague, unlimited requests that generate huge fee estimates
- Missing the FOIA appeal window or suing before exhausting (FOIA)
- Missing the short Sunshine suit limitations period
- Using Sunshine/FOIA as substitute discovery while a case is pending without telling the court when required; agencies may invoke the litigation closure ground
- Expecting FOIA to reach state police or county jails, or Sunshine to reach a federal agency

## Verify before relying
- Pull verbatim text of RSMo 610.010, 610.021, 610.023, 610.026, 610.027, 610.100 and 5 U.S.C. 552 via `statute-lookup` (or Descrybe `search_laws_and_rules`); check the agency's own FOIA regulations.
- Recompute every deadline in business days from actual receipt date.
- Legal information, not legal advice; for litigation over withheld records consider counsel or a transparency clinic.

## Related skills
- `misconduct-complaints` — records often feed police or official misconduct complaints
- `evidence-timeline-builder` — log produced records into the chronology
- `section-1983-claim-builder` — records requests to support civil-rights claims
- `statute-lookup` — verbatim Chapter 610 and 552 text
