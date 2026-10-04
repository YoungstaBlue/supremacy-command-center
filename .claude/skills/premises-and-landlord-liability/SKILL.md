---
name: premises-and-landlord-liability
description: Analyzes Missouri premises liability - invitee, licensee, and trespasser duties, dangerous conditions, notice, open-and-obvious defense - and landlord liability for common areas, latent defects, and repair promises. Use for "slip and fall", "trip and fall", "injured on property", "landlord negligence", or "unsafe stairs".
---

# Premises and Landlord Liability

Determines what duty a Missouri possessor of land owed the injured person, whether it was breached, and when a landlord (rather than a tenant) is liable.

## When to use
- Injury from a condition of property: wet floor, broken step, ice, poor lighting, falling object, dog on premises, defective railing
- Injury at a rental property, apartment common area, or business
- Injury on public property (sidewalk, government building)
- Not for: injuries from someone's activity rather than a property condition (use `negligence-claim-builder`); eviction, deposits, and habitability rent disputes (use `mo-landlord-tenant-eviction`)

## Gather first
- Exact location, date, time, and what the condition was; photos taken at or near the time
- Why the injured person was there (customer, guest, worker, tenant, no permission) - this sets the duty
- Who owned, controlled, and maintained the area (owner, tenant, management company, government)

## Workflow
1. **Identify the possessor.** Liability follows possession and control, not bare title. For rentals, decide whether the area was leased to the tenant or retained by the landlord.
2. **Classify the entrant.**
   - Invitee: on the land for a business purpose of the possessor or because the land is held open to the public.
   - Licensee: present with permission for their own purposes - Missouri treats social guests as licensees (Carter v. Kinney, 896 S.W.2d 926 (Mo. banc 1995)).
   - Trespasser: no permission.
3. **Apply the duty.**
   - Invitee: ordinary care to make the premises reasonably safe. Elements (Harris v. Niehaus, 857 S.W.2d 222 (Mo. banc 1993)): (a) a dangerous condition existed that made the premises not reasonably safe; (b) defendant knew or by using ordinary care could have known of it; (c) defendant failed to use ordinary care to remove, remedy, barricade, or warn; (d) plaintiff was injured as a result.
   - Licensee: warn of or make safe dangerous conditions the possessor actually knows of and the licensee does not, where the licensee would not discover the risk.
   - Trespasser: generally only refrain from intentional, willful, or wanton injury; heightened duties for discovered or frequent trespassers and for trespassing children under the attractive-nuisance doctrine (Restatement (Second) of Torts sec. 339 approach - verify Missouri adoption details).
4. **Notice.** Actual notice (complaints, employee knowledge, defendant created the condition) or constructive notice (condition existed long enough that reasonable inspection would have found it). Build a timeline: when created, last inspection, when the fall occurred. Surveillance video and inspection logs are key discovery targets.
5. **Open and obvious.** Possessor generally need not warn of dangers so open and obvious that invitees would be expected to discover them, unless the possessor should anticipate harm despite obviousness. In a pure comparative-fault state, obviousness often goes to the plaintiff's fault percentage - argue both ways.
6. **Landlord rules.** General rule: a landlord who surrenders possession is not liable for conditions within the leased premises. Recognized exceptions to evaluate: (a) common areas the landlord retained control of; (b) known, dangerous latent defects not disclosed to the tenant; (c) landlord undertook or contracted to repair and did so negligently or failed to; (d) premises leased for a public purpose; (e) violation of a code or ordinance (negligence per se analysis). Verify each exception against current Missouri case law before relying.
7. **Special statutes and defendants.**
   - Recreational use statute, RSMo 537.345-537.348: limits owner liability to those using land for recreation without charge - check exceptions (charge, willful/malicious failure to guard or warn).
   - Public property: dangerous-condition waiver of sovereign immunity, RSMo 537.600.1(2) - run `sovereign-and-official-immunity-mo`; check city notice statutes with `government-notice-of-claim`.
   - Workers on premises: independent-contractor and workers' compensation exclusivity issues.
8. **Comparative fault.** Plaintiff's inattention, footwear, or knowledge reduces but does not bar recovery (pure comparative fault).
9. **Limitations.** Generally 5 years, RSMo 516.120; shorter and notice-based rules can apply against governments.

## Output
- Duty classification box: entrant status, possessor, applicable duty, source
- Elements table: | Element | Facts | Evidence | Gap |
- Notice timeline (creation, inspections, warnings, incident)
- Discovery list: incident report, video retention, inspection and cleaning logs, prior complaints, maintenance contracts, lease terms
- Draft count heading: "COUNT __ - PREMISES LIABILITY (against ___)"

## Pitfalls
- Suing the title owner when a tenant or management company controlled the area (or missing one of them)
- Failing to send a preservation letter before surveillance video is overwritten
- Pleading invitee duties for a social guest (licensee)
- No evidence of how long the condition existed (constructive notice failure)
- Ignoring the lease's allocation of repair responsibility
- Missing a city notice-of-claim deadline for a sidewalk defect

## Verify before relying
- Pull verbatim RSMo 516.120, 537.345-537.348, and 537.600 via `statute-lookup` (or Descrybe `search_laws_and_rules`)
- Confirm Harris and Carter remain good law and check current treatment of open-and-obvious and landlord exceptions (CourtListener / Descrybe)
- Locate the applicable MAI premises-liability verdict director with `mo-jury-instructions-mai`
- Recompute limitations from the injury date
- Legal information, not legal advice; consult counsel or legal aid for significant injuries

## Related skills
- `negligence-claim-builder` - general negligence framework and comparative fault
- `mo-landlord-tenant-eviction` - lease, habitability, and possession issues
- `sovereign-and-official-immunity-mo` - public-property claims
- `government-notice-of-claim` - pre-suit notice to cities
- `damages-calculator` - medical specials and pain and suffering
