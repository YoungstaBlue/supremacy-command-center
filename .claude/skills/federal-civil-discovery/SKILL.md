---
name: federal-civil-discovery
description: Plans, drafts, and answers federal discovery under FRCP 26-37 and 45 - 26(f) conference, initial disclosures, proportionality, interrogatories, document requests, admissions, depositions, subpoenas, protective orders, motions to compel. Use for "federal discovery", "initial disclosures", or "motion to compel".
---

# Federal Civil Discovery

Runs discovery in a federal civil case so that each claim element and defense gets evidence, objections are preserved, and motions to compel or for protection are properly teed up.

## When to use
- After a federal case moves past pleadings and a Rule 26(f) conference or scheduling order is due
- Drafting or answering interrogatories, requests for production, requests for admission, or deposition notices
- Discovery disputes: deficient responses, privilege logs, protective orders, third-party subpoenas
- Not for: Missouri state-court discovery under Rules 56-61 — use `mo-discovery-requests` and `mo-motion-to-compel-sanctions`

## Gather first
- The scheduling order (or date of the Rule 26(f) conference) and the discovery cutoff
- The claims and defenses with elements, and what evidence each side likely holds
- Any discovery already served or received, with service dates and method

## Workflow
1. **Sequence.** No discovery from any source before the Rule 26(f) conference except where exempt or by order/stipulation (Rule 26(d)(1)); early Rule 34 requests may be delivered more than 21 days after service and are deemed served at the conference (26(d)(2)). The court issues a Rule 16(b) scheduling order with deadlines — those control.
2. **Rule 26(f) conference and report.** Confer on claims, defenses, settlement, initial disclosures, a discovery plan (subjects, phases, ESI, privilege/clawback, limits). File the joint report as the court directs.
3. **Initial disclosures (26(a)(1)).** Due at or within 14 days after the 26(f) conference unless ordered otherwise. Names/contact of witnesses with discoverable information the party may use, copies or descriptions of documents the party may use, computation of each category of damages with supporting documents, and insurance agreements. Certain proceedings are exempt (26(a)(1)(B)), including actions brought without an attorney by a person in government custody — non-incarcerated pro se parties are not exempt.
4. **Scope (26(b)(1)).** Nonprivileged matter relevant to any party's claim or defense and proportional to the needs of the case, considering importance of the issues, amount in controversy, relative access to information, resources, importance of the discovery, and whether burden outweighs benefit. Need not be admissible.
5. **Tools and limits (verify current text).**
   - Interrogatories (Rule 33): 25 including discrete subparts without leave; answers and objections within 30 days; objections stated with specificity or waived unless good cause; answered under oath.
   - Requests for production (Rule 34): response within 30 days; state whether responsive materials are being withheld on the basis of each objection; produce as kept or organized by request.
   - Requests for admission (Rule 36): matter is admitted unless answered or objected to within 30 days; lack of knowledge requires reasonable inquiry; costs of proving an unreasonably denied matter may be shifted (37(c)(2)).
   - Depositions (Rule 30): 10 per side without leave; one day of 7 hours; 30(b)(6) for organizations with described topics; reasonable written notice.
   - Subpoenas to non-parties (Rule 45): notice to other parties before serving a document subpoena; avoid undue burden; non-party may object in writing.
6. **Drafting requests.** Build from an elements matrix: each request targets a specific element or defense; define terms tightly; specify date ranges; request ESI in a usable format; avoid compound interrogatories that blow the 25 limit.
7. **Responding.** Calendar 30 days (plus 3 days only if served by mail or another Rule 6(d) method). Answer what is not objectionable; make specific objections; produce a privilege log describing withheld items without revealing privileged content (26(b)(5)); supplement when responses become incomplete or incorrect (26(e)).
8. **Disputes.**
   - Meet and confer in good faith first; a motion to compel must include a certification of that effort (37(a)(1)). Many local rules impose additional conferral and formatting requirements — check them (E.D. Mo. and W.D. Mo. both have discovery-motion rules; verify current numbers).
   - Evasive or incomplete answers are treated as failures to answer (37(a)(4)).
   - Expenses are presumptively awarded against the losing side unless substantially justified (37(a)(5)).
   - Protective orders for good cause to prevent annoyance, embarrassment, oppression, or undue burden, with conferral certification (26(c)).
   - Failure to disclose bars use of that information or witness unless substantially justified or harmless (37(c)(1)); ESI preservation failures are governed by 37(e).
9. **Filing.** Discovery requests and responses are generally not filed with the court until used in the proceeding (Rule 5(d)(1)(A)); attach only relevant excerpts to motions.

## Output
- Discovery plan table:

| Element/defense | Evidence needed | Holder | Tool (33/34/36/30/45) | Request no. | Due date | Status |
|---|---|---|---|---|---|---|

- Draft requests with definitions and instructions, or draft responses with objections stated per request
- Golden-rule / meet-and-confer letter identifying each deficient response and the cure requested
- Motion to compel outline: certification, request text, response text, why deficient, relief and expenses

## Pitfalls
- Letting requests for admission go unanswered past 30 days (deemed admitted, often case-ending)
- Boilerplate "overly broad, unduly burdensome" objections with no specifics (waived or overruled)
- Serving discovery after the cutoff, or so late that responses fall after it
- Skipping meet-and-confer before a motion to compel
- Forgetting initial disclosures, then being barred from using witnesses or documents
- Withholding documents without saying so or without a privilege log

## Verify before relying
- Pull current FRCP 16, 26, 30, 33, 34, 36, 37, 45 and district local rules verbatim via `statute-lookup` or Descrybe `search_laws_and_rules`.
- Recompute every response deadline from the actual service date and method under Rule 6.
- Check any case cited on proportionality or sanctions is still good law in the Eighth Circuit.
- Legal information, not legal advice.

## Related skills
- `elements-checklist-builder` — tie each request to an element
- `privilege-analyzer` — objections and privilege logs
- `federal-summary-judgment` — Rule 56(d) when discovery is incomplete
- `mo-discovery-requests` — state-court counterpart
- `evidence-timeline-builder` — organize what discovery produces
