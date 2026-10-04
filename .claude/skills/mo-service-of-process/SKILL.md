---
name: mo-service-of-process
description: Plans and checks Missouri service of process under Rule 54 - summons, sheriff or special process server, abode service, corporations, LLCs, government entities, out-of-state, mail, publication, and returns. Use for "serve the defendant", "summons expired", "bad service".
---

# Missouri Service of Process

Gets the summons and petition validly served on every defendant, documented by a proper return, and identifies defective service you can attack or must cure.

## When to use
- Plaintiff needs to serve a new petition or an amended pleading adding parties
- A summons came back "non est" (not found) or expired unserved
- Defendant (you) was served improperly and wants to raise insufficiency of process or service
- Not for: serving later papers on parties who have appeared (that is Rule 43 service - see `court-document-formatting`)

## Gather first
- Defendant type (individual, corporation, LLC, partnership, government body, state agency, minor/incompetent) and exact legal name
- Every known address: home, workplace, registered agent (Missouri Secretary of State business search)
- Whether the defendant is in Missouri, out of state, or cannot be located

## Workflow
1. **Request summons.** The clerk issues a summons for each defendant on filing (Rule 54.01). Prepare one copy of the petition and exhibits per defendant plus service fees.
2. **Choose who serves.** Sheriff of the county where the defendant is found, or a non-party adult appointed by the court as special process server (file a motion/request naming the server). Check local rules on approved private servers.
3. **Pick the method by defendant type (Rule 54.13 - verify subsections):**
   - Individual: personal delivery; or leaving copies at the dwelling or usual place of abode with a family member over age 15 who resides there (verify age in current rule); or delivery to an agent authorized by appointment or law.
   - Corporation, partnership, unincorporated association: an officer, partner, managing or general agent, or registered agent; or as the rule otherwise allows at the business office (verify).
   - LLC and other statutory entities: registered agent first; check the entity's governing chapter of RSMo for alternatives.
   - Public or municipal corporations and state officials: follow the specific Rule 54.13 subsection for public entities and any statute naming who must be served (verify).
4. **Out-of-state defendant.** Personal service outside Missouri is governed by Rule 54.14 and the long-arm statute RSMo 506.500 (verify); the petition must plead facts supporting long-arm jurisdiction.
5. **Service by mail.** Rule 54.16 allows mailing with an acknowledgment form; service is complete only if the acknowledgment is signed and returned. If not returned, serve by another method (verify cost-shifting provisions).
6. **Publication or posting.** Available only in limited actions (for example, actions affecting property or status, or where the rule authorizes it) and requires a verified motion showing diligent search and a court order (verify Rules 54.12 and 54.17). It does not support a personal money judgment against an absent defendant.
7. **Track the summons deadline.** A summons is returnable within a set period after issuance (verify Rule 54.21). If it expires, request an alias or pluries summons promptly and document diligence.
8. **Return of service.** Sheriff's return, or the special process server's affidavit, must state the date, place, manner, and person served (Rule 54.20 - verify). Read it for defects the moment it is filed.
9. **Calendar the answer date.** Answer is due 30 days after service of summons and petition (Rule 55.25(a) - verify; recompute with `mo-deadline-calculator`).
10. **If you are the defendant attacking service.** Raise insufficiency of process or service in your first Rule 55.27 motion or answer or it is waived (see `mo-motion-to-dismiss`). Note that appearing and seeking affirmative relief can waive the objection.

## Output
- Service plan table: | Defendant | Type | Method | Address | Server | Summons issued | Return due | Status |
- Draft request for special process server or alias summons, if needed
- Return-of-service audit checklist: correct person, correct place, correct date, signed, sworn, within summons period

## Pitfalls
- Leaving papers with a co-worker, receptionist, or non-resident relative at an individual's home is not valid abode service.
- Serving a corporate employee who is not an officer or authorized agent.
- Assuming a filed petition stops limitations if service is never diligently pursued - lack of diligence can defeat tolling.
- Default judgment entered on defective service is vulnerable as void (see `mo-default-judgment-set-aside`).
- Publication used where personal service was possible; courts scrutinize the diligent-search affidavit.
- Plaintiffs personally serving defendants - a party cannot be the server.

## Verify before relying
- Pull verbatim Rules 54.01, 54.12-54.21 and RSMo 506.500 via `statute-lookup` (or Descrybe `search_laws_and_rules`); subsection numbering in this skill is unconfirmed.
- Check case law on diligence and waiver is still good law (CourtListener / Descrybe treatment).
- Recompute any deadline from the actual service date shown on the return.
- Legal information, not legal advice; recommend counsel or legal aid for high-stakes decisions.

## Related skills
- `mo-petition-drafting` - the pleading being served
- `mo-answer-affirmative-defenses` - what the defendant files next
- `mo-motion-to-dismiss` - attacking process and service
- `mo-deadline-calculator` - computing answer dates
- `jurisdiction-and-venue-analyzer` - long-arm and personal jurisdiction
