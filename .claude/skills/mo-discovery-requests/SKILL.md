---
name: mo-discovery-requests
description: Drafts and answers Missouri civil discovery under Rules 56-59 - interrogatories (25 limit), requests for production, requests for admission, depositions, objections, privilege logs. Use for "interrogatories", "request for production", "requests for admission", "deposition", "answer their discovery".
---

# Missouri Discovery Requests and Responses

Plans discovery around the elements you must prove or disprove, drafts compliant requests, and answers incoming discovery on time without waiving objections.

## When to use
- Building the evidentiary record for summary judgment or trial in Missouri state court
- Served with interrogatories, requests for production, or requests for admission
- Planning or noticing a deposition
- Not for: enforcing discovery the other side ignored (use `mo-motion-to-compel-sanctions`); federal discovery (use `federal-civil-discovery`); criminal discovery (use `mo-criminal-discovery`)

## Gather first
- The operative pleadings and the elements of each claim and defense
- Any scheduling or case-management order setting discovery deadlines
- For incoming requests: date and method of service

## Workflow
1. **Scope (Rule 56.01(b) - verify current text).** Any non-privileged matter relevant to a claim or defense; check whether the current rule includes a proportionality limit. Work product and expert discovery have special rules within Rule 56.01. Protective orders are available on good cause (Rule 56.01(c) - verify).
2. **Plan by element.** Use `elements-checklist-builder`: for each element, list what fact you need, who has it, and which tool gets it (interrogatory for identities and contentions, production for documents, admissions to eliminate undisputed issues, depositions for testimony).
3. **Interrogatories (Rule 57.01 - verify).** Limited to 25 including discrete subparts unless the court allows more. Answered separately and fully in writing under oath within 30 days after service. Draft short, single-subject questions with definitions; leave space for answers if local practice requires.
4. **Requests for production (Rule 58.01 - verify).** Describe each category with reasonable particularity; specify time, place, and manner (electronic production format). Response due in 30 days, stating for each item whether it will be produced or the specific objection.
5. **Requests for admission (Rule 59.01 - verify).** Each matter is admitted unless a written answer or objection is served within 30 days. Use them for authenticity of documents and narrow facts. When answering, admit, deny, or explain in detail why you cannot; a party who unreasonably denies something later proved may pay the cost of proof (check Rule 61.01).
6. **Depositions (Rule 57.03 - verify).** Reasonable written notice to every party; subpoena required for non-parties (Rule 57.09 - verify). Arrange an officer and court reporter or other authorized recording method. Prepare an outline by element (see `witness-examination-planner`).
7. **Subpoenas for non-party records.** Use a subpoena duces tecum with notice to other parties; follow the rule for records-only subpoenas.
8. **Answering incoming discovery.** Calendar 30 days (plus any Rule 44.01 mail add-on - verify with `mo-deadline-calculator`). Object specifically, not with boilerplate; answer the unobjectionable part. Sign interrogatory answers under oath. Serve a privilege log describing withheld items.
9. **Supplementation.** Missouri imposes a duty to supplement certain responses (witness and expert identities, responses known to be incorrect) - verify the current Rule 56.01(e) text and comply before trial.
10. **Serve, do not file.** Discovery requests and responses are generally served on parties and not filed; file a certificate of service if local rules require.

## Output
- Discovery plan table: | Element | Fact needed | Source | Tool | Request no. | Due |
- Drafts: Interrogatories / Requests for Production / Requests for Admission, each with caption, definitions, instructions, numbered requests, signature, certificate of service
- Response templates with per-request objection and answer, verification page, and privilege log

## Pitfalls
- Missing the 30-day deadline on requests for admission - the matters are deemed admitted and can decide the case. Move promptly to withdraw or amend admissions if this happens.
- Exceeding 25 interrogatories by stacking subparts.
- Boilerplate objections ("overly broad, unduly burdensome") without explanation may be treated as no objection.
- Unsigned or unsworn interrogatory answers.
- Waiting until the discovery cutoff to serve requests that cannot be answered in time.
- Failing to supplement, then having witnesses or documents excluded at trial.
- Producing documents without Bates numbers or a production log, making later disputes impossible to resolve.
- Answering for the other side's convenience instead of the question asked; answer exactly and completely.
- Overlooking privacy redaction (Social Security, account, and medical identifiers) in produced records.

## Verify before relying
- Pull verbatim Rules 56.01, 57.01, 57.03, 57.09, 58.01, 59.01, 61.01 via `statute-lookup` (or Descrybe `search_laws_and_rules`).
- Check local circuit rules and any scheduling order for limits and filing practice.
- Recompute response deadlines from the actual service date and method.
- Legal information, not legal advice; recommend counsel or legal aid for high-stakes decisions.

## Related skills
- `mo-motion-to-compel-sanctions` - when responses are late or deficient
- `elements-checklist-builder` - target discovery at elements
- `privilege-analyzer` - objections and privilege logs
- `mo-summary-judgment` - using discovery as record support
- `witness-examination-planner` - deposition outlines
