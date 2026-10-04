---
name: mo-expungement
description: Screens eligibility and drafts a Missouri expungement petition under RSMo 610.140 - excluded offenses, 3-year felony and 1-year misdemeanor waiting periods, lifetime limits, named defendants, objection timeline - and closed records under 610.105. Use for "expungement", "expunge my record", or "clear my record".
---

# Missouri Expungement

Determines whether a Missouri arrest, plea, or conviction can be expunged under RSMo 610.140 and drafts the petition with the required parties and showings.

## When to use
- "Can I expunge this?", "clean my record", "background check shows an old charge", "seal an arrest"
- Planning when a person becomes eligible after completing a sentence
- Distinguishing expungement from records already closed after a dismissal, acquittal, nolle, or SIS
- Not for: municipal ordinance trial defense (use `mo-municipal-ordinance-defense`); federal records (no general federal expungement statute)

## Gather first
- For each offense: statute charged, class, court and case number, disposition (conviction, SIS, dismissal), date disposition was completed (probation ended, fines and restitution paid)
- Full criminal history, including any later convictions and any pending charges
- Prior expungements granted

## Workflow
1. **Check whether records are already closed.** RSMo 610.105: records close when a case is nolle prossed, dismissed, acquitted, or imposition of sentence is suspended, once finally terminated. Closed records may still be visible to some agencies; expungement may still be worth seeking.
2. **Screen for ineligible offenses (RSMo 610.140 exclusion list; confirm current subsection).** Categories include class A felonies, dangerous felonies, offenses requiring sex-offender registration, felonies with death as an element, felony assault, misdemeanor or felony domestic assault, felony kidnapping, listed chapter 566 offenses and other enumerated sections, intoxication-related traffic and boating offenses, and certain weapons offenses. Read the current list against the exact statute of conviction - it is long and specific.
3. **Count against lifetime limits (RSMo 610.140.13 or current subsection).** Generally no more than two felony offenses and three misdemeanor or ordinance offenses expunged in a lifetime; infractions are not limited. Offenses arising from the same course of conduct may count differently - read the text.
4. **Waiting periods (RSMo 610.140.6(1) or current subsection).** At least three years from completion of the authorized disposition for a felony; at least one year for a misdemeanor, ordinance violation, or infraction. Arrest-only records: no earlier than eighteen months after the arrest (with conditions). Count from completion of probation/payment, not the plea date.
5. **Required findings.** The court must find the petitioner: completed the disposition; has not been found guilty of another offense (other than certain infractions) during the waiting period; has satisfied all obligations including restitution; has no pending charges; has habits and conduct showing no threat to public safety; and that expungement is consistent with public welfare and the interests of justice.
6. **Draft the petition.** File in the circuit court of the county where the petitioner was charged. Name as defendants every law enforcement agency, court, prosecuting attorney, central state repository, and other entity the petitioner has reason to believe has records. List each offense with date, charge, case number, and agency.
7. **Timeline.** Serve each named entity. The prosecutor or other entity may object within 30 days after service. If an objection is filed, the court holds a hearing within 60 days; if none, the court may grant without a hearing.
8. **Fees.** A filing fee or surcharge applies and may be waived for indigency in some circumstances - confirm the current amount with the clerk.
9. **Marijuana offenses.** Mo. Const. art. XIV provides a separate expungement path for certain marijuana offenses; check whether that path applies before using 610.140.

## Output
- **Eligibility screen:** | Offense | Statute / class | Disposition completed | Excluded? | Waiting period met (date) | Counts toward limit |
- **Petition for Expungement** headings: Petitioner; Offenses (table); Defendants with Records; Eligibility; Statutory Findings (one paragraph each); Relief; Verification
- Service list and 30/60-day calendar

## Pitfalls
- Counting from the plea date instead of completion of probation and payment of all costs and restitution.
- Omitting an agency that holds records - that agency's records stay open.
- A new offense, even minor, during the waiting period.
- Assuming SIS dispositions are invisible; some agencies and licensing boards can still see closed records.
- Misreading the exclusion list by charge name rather than the exact statute and subsection.

- Filing before every fine, cost, and restitution balance is paid.
- Forgetting the 30-day objection window and missing the hearing notice.
- Petitioning for an offense that already used one of the lifetime slots.
- Using an outdated court form after statutory amendments.
- Not obtaining certified dispositions for each offense before drafting.
- Leaving out the DOR or highway patrol records where traffic-related.

## Verify before relying
- Pull current RSMo 610.140 and 610.105 text via `statute-lookup` or Descrybe `search_laws_and_rules`; subsection numbers and the exclusion list change with amendments.
- Confirm the court's current petition form and fee with the circuit clerk.
- Recompute the waiting period from documented completion dates.
- Legal information, not legal advice; legal aid clinics frequently assist with expungement.

## Related skills
- `mo-plea-and-sentencing` - how SIS/SES affects future eligibility
- `mo-municipal-ordinance-defense` - municipal records
- `sunshine-and-foia-requests` - obtaining records to confirm dispositions
- `statute-lookup` - verbatim 610.140 text
