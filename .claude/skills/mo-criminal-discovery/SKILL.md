---
name: mo-criminal-discovery
description: Drafts Missouri criminal discovery requests under Rule 25.03, tracks Rule 25.02 deadlines, plans Rule 25.12 defense depositions, and seeks Rule 25.18 sanctions for nondisclosure. Use for a criminal "discovery request", "bodycam", "police reports", "state won't turn over", or "depose the officer".
---

# Missouri Criminal Discovery

Gets the state's evidence on the record through written Rule 25 requests, defense depositions, and sanctions motions when the state fails to disclose.

## When to use
- Any pending Missouri misdemeanor or felony after the initial appearance
- "Request for discovery", "get the bodycam/dashcam", "the prosecutor hasn't given me anything", "late disclosure", "depose the witness"
- Responding to the state's request for defense disclosure
- Not for: crafting targeted exculpatory-evidence demands or Brady violation motions (use `brady-giglio-demands`); municipal cases, where discovery is discretionary (Rule 37.54)

## Gather first
- Charging document type (felony complaint vs. information/indictment) and filing dates
- Arraignment date (the 20-day request clock runs from it)
- What has already been produced, with dates received

## Workflow
1. **Pick the right stage.** After a felony complaint, Rule 25.03(a) entitles the defense on written request to reports, statements, documents, photographs, video, and electronic data relating to the offense in the prosecutor's possession; the state must respond within 14 days of service (Rule 25.02(a)). After indictment or information, use the full Rule 25.03(b) list.
2. **Calendar the request deadline.** Rule 25.02(b): requests "shall be made not later than twenty days after arraignment"; answers due within 14 days of service; the court may enlarge or shorten. File early.
3. **Draft the request tracking Rule 25.03(b)(1)-(9)** item by item: (1) reports, statements, documents, photos, video, electronic data; (2) witness names, addresses, and their statements and summaries; (3) defendant's, co-defendant's, and co-actor's statements and witnesses to them; (4) relevant grand jury transcripts; (5) preliminary hearing and prior trial transcripts; (6) expert reports, examinations, and test results; (7) items the state intends to introduce or that belong to the defendant; (8) witnesses' prior convictions; (9) surveillance of the defendant. Name specific items you know exist (CAD logs, 911 audio, bodycam for each officer, lab bench notes, chain of custody).
4. **File and serve.** Rule 25.03(c): file the request in the court where the case is pending and serve the prosecutor. Keep proof of service.
5. **Brady/Giglio without request.** Rule 25.03(g) requires disclosure, without written request, of material that negates guilt, mitigates the offense, or reduces punishment, and anything required by Brady v. Maryland, 373 U.S. 83 (1963) and Giglio v. United States, 405 U.S. 150 (1972). Still make a specific written demand to create a record.
6. **Redactions.** The state may redact listed identifiers (Rule 25.03(d)) and provide a "Defendant's Copy" (Rule 25.03(e)); a pro se defendant should expect the court to manage access to redacted material. Unredacted information requires a good-cause showing (Rule 25.03(f)).
7. **Depositions.** After indictment or information, the defense may depose any person (Rule 25.12(a)), governed by civil deposition rules; the defendant is not physically present absent agreement or a good-cause order (Rule 25.12(c)); expert depositions generally require paying a reasonable fee (Rule 25.12(d)). Use depositions for officers and key civilian witnesses.
8. **Reciprocal duties.** Review the defense disclosure obligations (Rules 25.05-25.06), the continuing duty to disclose (Rule 25.08), matters not subject to disclosure such as work product (Rule 25.10), and protective orders (Rule 25.11).
9. **Enforce.** Send a written follow-up listing missing items, then move under Rule 25.18(a): the court may order disclosure, grant a continuance, exclude the evidence, or enter another just order. Willful violations may draw sanctions (Rule 25.18(b)). At trial, object at the moment undisclosed evidence is offered and request exclusion or a continuance - the remedy must be requested to preserve the issue. Prejudice (fundamental unfairness) is usually what reviewing courts look for.

## Output
- **Request for Disclosure** captioned for the court, numbered items tracking Rule 25.03(b), with a specific-items schedule and certificate of service
- **Discovery tracker:** | Item | Requested (date) | Due | Received | Gap / follow-up |
- **Motion for sanctions** headings: Request and Service; Deadline; Items Not Produced; Prejudice; Requested Remedy under Rule 25.18
- Deposition notice and outline list

## Pitfalls
- Missing the 20-day-after-arraignment request deadline and relying only on informal "open file" access.
- Generic requests that do not name the bodycam, 911 call, or lab file - harder to prove the state knew what was sought.
- Failing to object and request a specific remedy at trial when undisclosed evidence appears.
- Using discovery material outside the case or sharing redacted information in violation of Rule 25.03(e).
- Asking for exclusion without showing prejudice; ask for a continuance in the alternative.

- Not documenting what was received and when; a sanctions motion needs dates.
- Overlooking defense disclosure duties and reciprocal deadlines (Rules 25.05-25.06), which can lead to exclusion of defense evidence.
- Waiting until trial week to raise a gap; courts favor continuances over exclusion when the issue surfaces late.
- Deposing a witness without a plan, giving the state a preview of cross-examination.
- Forgetting the continuing duty to disclose (Rule 25.08) - renew requests before trial.

## Verify before relying
- Pull current Rule 25.02, 25.03, 25.12, 25.18 text via `statute-lookup` or Descrybe `search_laws_and_rules` (Rule 25 was amended in 2018 and 2022).
- Check any sanctions case for current treatment (CourtListener / Descrybe) before citing.
- Recompute 20-day and 14-day periods from the actual arraignment and service dates (Rule 20.01).
- Legal information, not legal advice.

## Related skills
- `brady-giglio-demands` - specific exculpatory/impeachment demands and violation motions
- `mo-criminal-case-roadmap` - discovery in the timeline
- `evidence-timeline-builder` - organize what was produced
- `mo-motion-to-suppress` - discovery that feeds suppression issues
