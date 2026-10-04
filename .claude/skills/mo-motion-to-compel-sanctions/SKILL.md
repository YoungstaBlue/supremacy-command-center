---
name: mo-motion-to-compel-sanctions
description: Enforces Missouri civil discovery - golden-rule letter, good-faith conferral, motion to compel, Rule 61.01 sanctions (fees, exclusion, striking pleadings, default) - and defends against sanctions. Use for "motion to compel", "golden rule letter", "discovery sanctions", "they won't answer discovery".
---

# Missouri Motion to Compel and Discovery Sanctions

Moves a stalled discovery dispute from a documented conferral attempt to an order compelling responses, then to proportionate Rule 61.01 sanctions if the order is ignored.

## When to use
- Discovery responses are late, missing, evasive, unsigned, or loaded with boilerplate objections
- A deponent failed to appear or refused to answer
- The other side violated a discovery order
- You are facing a motion to compel or sanctions and must respond
- Not for: drafting the original requests (use `mo-discovery-requests`); federal Rule 37 practice (use `federal-civil-discovery`)

## Gather first
- The exact requests served, the date and method of service, and any responses received
- All correspondence about the dispute (letters, emails, call notes with dates)
- Any scheduling order, discovery deadline, or prior discovery order

## Workflow
1. **Diagnose each deficiency.** For each request: no response, late response, incomplete answer, improper objection, unsigned or unverified, documents promised but not produced, privilege claimed without a log.
2. **Golden-rule letter.** Missouri practitioners send a "golden rule" letter before moving: identify each deficient request by number, explain why the response is deficient with the rule requirement, state what you need, and set a reasonable date (often 10 days) to cure. Offer a phone conference. Keep it factual and courteous - the judge may read it.
3. **Confer in good faith.** Many Missouri circuits require a certificate that the movant conferred or attempted to confer before filing a discovery motion - check the local rules for your circuit and follow the exact wording required. Document dates, method, and outcome.
4. **Motion to compel.** Caption; numbered paragraphs reciting the requests, service date, deficiencies, conferral efforts; the relief sought (order compelling complete, verified answers and production within a set number of days); request for expenses; certificate of conferral; proposed order. Attach the requests, responses, and golden-rule letter.
5. **Sanctions framework (Rule 61.01 - verify subdivisions).** Rule 61.01 addresses failure to answer interrogatories, produce documents, appear for deposition, and admit matters later proved, and authorizes orders such as: deeming facts established, barring evidence or witnesses, striking pleadings, staying proceedings, dismissing the action, entering default judgment, contempt (except for physical/mental examinations - verify), and reasonable expenses including attorney's fees. Courts generally move progressively: order compelling first, then escalating sanctions for disobedience.
6. **Proportionality and prejudice.** Trial courts have broad discretion, reviewed for abuse of discretion; severe sanctions (dismissal, default, exclusion of key evidence) are typically tied to willful or repeated noncompliance and prejudice. Show the history of noncompliance and specific prejudice (missed depositions, inability to prepare for trial).
7. **Request for admission costs.** If a party denied a request for admission and you later prove the matter, move for the reasonable cost of that proof (verify the Rule 61.01 subdivision and its exceptions).
8. **Defending a motion.** Respond promptly: cure the deficiencies if possible before the hearing, explain good cause, propose a schedule, and show that sanctions requested are disproportionate. Never ignore an order compelling discovery.
9. **Hearing.** Bring copies of the requests, responses, letter, and a one-page chart of deficiencies. Ask for a specific compliance deadline in the order.

## Output
- Golden-rule letter draft with a per-request deficiency list and cure date
- Motion to compel (or for sanctions) with certificate of conferral, exhibit list, and proposed order
- Deficiency chart: | Request no. | Response | Deficiency | Rule requirement | Relief sought |

## Pitfalls
- Filing without a conferral attempt or without the local-rule certificate - motions get denied or continued.
- Asking for dismissal or default as the first sanction; courts rarely grant it without a prior order.
- Vague motions that do not identify specific requests and specific deficiencies.
- Moving to compel after the discovery cutoff or on the eve of trial without explanation.
- As the responding party, ignoring an order compelling discovery - this is how claims and defenses are stricken.
- Hostile or personal letters that undercut credibility with the judge.
- Not requesting expenses in the motion itself, then being unable to show the amount at the hearing.
- Failing to bring the proposed order; ask for a date-certain compliance deadline so noncompliance is clear.

## Verify before relying
- Pull verbatim Rule 61.01 and the discovery rules involved (57.01, 58.01, 59.01) via `statute-lookup` (or Descrybe `search_laws_and_rules`).
- Read the local circuit rules for conferral and discovery-motion requirements.
- Confirm any case law on sanctions standards is still good law (CourtListener / Descrybe treatment).
- Recompute response and compliance deadlines from actual service and order dates.
- Legal information, not legal advice; recommend counsel or legal aid for high-stakes decisions.

## Related skills
- `mo-discovery-requests` - the underlying requests and responses
- `mo-deadline-calculator` - when responses became late
- `privilege-analyzer` - testing privilege objections and logs
- `court-document-formatting` - captions, proposed orders, certificates
- `lawmind-strategy-engine` - whether to escalate to sanctions
