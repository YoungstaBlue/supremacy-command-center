---
name: mo-municipal-ordinance-defense
description: Defends Missouri municipal ordinance and traffic cases under Rule 37 - initial appearance, change of judge, discovery, jury certification, ability-to-pay protections (Rule 37.65), and the 10-day trial de novo (RSMo 479.200). Use for "traffic ticket", "municipal court", "ordinance violation", or "trial de novo".
---

# Missouri Municipal Ordinance Defense

Handles a city or county ordinance case in a Missouri municipal division from first appearance through trial de novo, including protection against jail for inability to pay.

## When to use
- A municipal summons, uniform citation, or ordinance-violation warrant (traffic, nuisance, disorderly conduct, code violations)
- "Fight a speeding ticket", "municipal court date", "failure to appear warrant", "can't pay my fines", "appeal a municipal conviction"
- Deciding between pleading, trial before the municipal judge, jury demand, and trial de novo
- Not for: state misdemeanor or felony charges (use `mo-criminal-case-roadmap`); expunging municipal records (use `mo-expungement`)

## Gather first
- The citation or information: ordinance number, charging language, court date, municipality
- Whether jail is a possible penalty, and the fine and point exposure
- Any judgment date, payments made, and outstanding fines or warrants

## Workflow
1. **Get the ordinance text.** Obtain the exact ordinance the city charged (municipal code online or from the city clerk) and break it into elements. Check the information identifies the ordinance and the facts.
2. **Know your rights.** Rule 37 governs (Rule 37.01). The municipal division must provide a written notice of rights (Rule 37.04, Appendix C). On arrest on a municipal warrant, an initial appearance is required within 48 hours, excluding weekends and holidays (Rule 37.47(a)); the judge must advise of the charge, the right to counsel, appointed counsel if indigent and jail is possible, and the right to silence (Rule 37.47(b)).
3. **Arraignment.** The defendant gets a reasonable time to examine the charge before pleading (Rule 37.48).
4. **Change of judge.** A no-cause application must be filed not later than 10 days after the initial plea (special timing if the judge is designated later); one per party, plus for-cause at any time (Rule 37.53(c)).
5. **Discovery and motions.** Discovery is permitted only in the judge's discretion (Rule 37.54) - file a short motion naming specific items (bodycam, radar/lidar calibration and certification, officer training logs, dashcam). Motions to suppress go before trial (Rule 37.52).
6. **Choose the forum.** Options: (a) negotiate with the city prosecutor (amendment to a non-moving or lesser violation is common in traffic cases); (b) bench trial before the municipal judge; (c) timely jury demand, which certifies the case to the circuit court (see Rule 37.61). Note that a guilty plea or a jury verdict forecloses trial de novo (RSMo 479.200.2).
7. **Trial preparation.** Elements chart; cross-examination of the officer on observation, measurement method, device calibration, and location; exhibits (photos, maps, video). The city must prove each element - confirm the applicable burden in current authority.
8. **Ability to pay.** If the defendant says they cannot pay, the judge must inquire (Rule 37.65(a)); if unable to pay, alternatives include waiver, reduction, community service, or programs (Rule 37.65(c)). Jail for nonpayment requires notice, a hearing, and written findings of willfulness or inadequacy of alternatives (Rule 37.65(d), (f)), with a 30-day cap on contempt incarceration (Rule 37.65(g)). Prepare a financial statement.
9. **Trial de novo.** After a bench trial, file the application for trial de novo within 10 days after judgment (RSMo 479.200.2). No judge may extend that time (Rule 37.71(a)). Do not pay any part of the fine or costs first - payment bars trial de novo, except costs paid after an SIS (Rule 37.71(b)). The de novo trial proceeds as a misdemeanor trial in circuit court (Rule 37.74).
10. **Collateral consequences.** For moving violations, check driver's license point exposure under the Department of Revenue point system (RSMo 302.302 - verify) before pleading.

## Output
- **Case snapshot:** ordinance, elements, penalty range, points, court dates
- **Decision matrix:** | Option | Outcome range | Points | Record | Preserves de novo? |
- Motion for discovery (specific items), application for change of judge, application for trial de novo - short captioned drafts
- Financial statement outline for a Rule 37.65 ability-to-pay hearing

## Pitfalls
- Paying the fine "to get it over with" and then trying to appeal - payment bars trial de novo.
- Missing the 10-day de novo deadline; it cannot be extended.
- Missing a court date - a failure-to-appear warrant and possibly a separate charge follow.
- Pleading guilty to a moving violation without checking points and insurance consequences.
- Going to trial without the ordinance text or the officer's measurement records.

- Ignoring a show-cause order on unpaid fines; appear and bring proof of finances (Rule 37.65(d)).
- Missing the 10-day window for a no-cause change of judge after the initial plea (Rule 37.53(c)).
- Assuming discovery is automatic in municipal court; it is discretionary (Rule 37.54).

## Verify before relying
- Pull current Rule 37 provisions and RSMo 479.200 via `statute-lookup` or Descrybe `search_laws_and_rules`; obtain the ordinance text from the municipality.
- Confirm local municipal division procedures with the clerk.
- Recompute the 10-day de novo period from the judgment date.
- Legal information, not legal advice.

## Related skills
- `mo-criminal-case-roadmap` - if the case is certified or refiled as a state charge
- `mo-motion-to-suppress` - stop and search issues
- `mo-expungement` - clearing municipal records later
- `mo-pro-se-courtroom-procedure` - conduct at the bench trial
- `fourth-amendment-analyzer` - legality of the traffic stop
