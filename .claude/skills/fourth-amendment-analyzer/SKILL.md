---
name: fourth-amendment-analyzer
description: Analyzes searches and seizures under the Fourth Amendment and Mo. Const. art. I, sec. 15 - stops, arrests, warrants, warrant exceptions, standing, and the exclusionary rule. Use for "illegal search", "traffic stop", "no warrant", "probable cause", "consent search", "fruit of the poisonous tree".
---

# Fourth Amendment Analyzer

Runs a search-and-seizure fact pattern through the threshold, justification, and remedy questions in the order courts decide them, so a suppression motion or 1983 claim rests on the right test.

## When to use
- A stop, frisk, arrest, home entry, vehicle search, phone search, or data acquisition (cell-site, GPS) is in question.
- Deciding whether evidence can be suppressed, or whether a seizure supports a civil-rights claim.
- Testing whether a warrant was supported by probable cause or was executed within its scope.
- Not for: attacking false statements inside a warrant affidavit (use `franks-affidavit-challenge`); drafting the Missouri suppression motion itself (use `mo-motion-to-suppress`).

## Gather first
- Exact sequence of events with times: initial contact, what officers said and did, when the person was told they were free to leave (or not), what was searched, what was found.
- Any warrant, affidavit, return, body-cam/dash-cam, CAD log, police report, and consent form.
- Who owned, possessed, or had control of the place or item searched (standing).

## Workflow
1. **Government action.** Was the actor a government agent or a private party acting at government direction? Purely private searches are outside the Fourth Amendment.
2. **Was there a "search"?** Apply both tests:
   - Reasonable expectation of privacy (Katz v. United States, 389 U.S. 347 (1967), Harlan concurrence).
   - Physical intrusion on a constitutionally protected area (Florida v. Jardines, 569 U.S. 1 (2013) - curtilage).
   - Digital: cell-phone contents need a warrant (Riley v. California, 573 U.S. 373 (2014)); historical cell-site location data is a search (Carpenter v. United States, 585 U.S. 296 (2018)).
   - Not searches: open fields, abandoned property, items in plain view from a lawful vantage point.
3. **Was there a "seizure"?** Classify the encounter:
   - Consensual encounter (no seizure) - would a reasonable person feel free to leave or decline?
   - Investigative stop/frisk - reasonable suspicion of criminal activity; frisk requires reasonable belief the person is armed and dangerous (Terry v. Ohio, 392 U.S. 1 (1968)).
   - Arrest - probable cause required.
   - Traffic stop - cannot be prolonged beyond its mission absent independent reasonable suspicion (Rodriguez v. United States, 575 U.S. 348 (2015)).
4. **Standing.** The challenger must show their own privacy or property interest was invaded (Rakas v. Illinois, 439 U.S. 128 (1978)). Passengers can challenge the stop of the car but usually not the search of areas they have no interest in.
5. **Warrant analysis (if a warrant exists).**
   - Probable cause under the totality of the circumstances (Illinois v. Gates, 462 U.S. 213 (1983)); review is limited to the four corners of the affidavit unless a Franks showing is made.
   - Particularity of place and items; nexus between crime, items, and place; staleness.
   - Execution: scope, knock-and-announce, time of day if restricted.
6. **Warrantless - test each exception the state may claim; state bears burden:**
   - Consent: voluntary under totality (Schneckloth v. Bustamonte, 412 U.S. 218 (1973)); scope; authority of consenter.
   - Search incident to arrest; vehicle limited to Arizona v. Gant, 556 U.S. 332 (2009) (arrestee unsecured within reach, or reason to believe evidence of the offense of arrest is in the vehicle).
   - Automobile exception (probable cause the vehicle contains contraband/evidence).
   - Exigent circumstances, hot pursuit, emergency aid.
   - Plain view (lawful position, lawful access, incriminating character immediately apparent).
   - Inventory (standardized policy, not a pretext for investigation).
   - Home entry: warrant required absent exigency or consent (Payton v. New York, 445 U.S. 573 (1980)).
7. **Remedy.**
   - Exclusionary rule applies to the states (Mapp v. Ohio, 367 U.S. 643 (1961)); derivative evidence suppressed as fruit (Wong Sun v. United States, 371 U.S. 471 (1963)).
   - Limits: good-faith reliance on a warrant (United States v. Leon, 468 U.S. 897 (1984)) and its four exceptions; independent source; inevitable discovery; attenuation (Utah v. Strieff, 579 U.S. 232 (2016)).
   - Civil: a 1983 damages claim faces qualified immunity and Heck v. Humphrey limits (see related skills).
8. **Missouri overlay.** Mo. Const. art. I, sec. 15 is generally construed coextensively with the Fourth Amendment - argue it separately only with Missouri authority. Missouri's suppression statute is RSMo 542.296 (motion, hearing, burden on the state); federal suppression motions must be raised pretrial under Fed. R. Crim. P. 12(b)(3)(C).

## Output
- Event timeline table: | Time | Police action | Legal character (encounter/stop/arrest/search) | Justification claimed | Supported? |
- Issue list ranked by strength, each with: test, facts for, facts against, burden holder.
- Evidence-to-suppress list linking each item to the illegality it flows from and any exception the state will argue.

## Pitfalls
- Skipping standing - courts deny suppression without reaching the merits.
- Arguing an officer's subjective motive; pretextual stops are valid if objectively justified (Whren v. United States, 517 U.S. 806 (1996)).
- Not raising suppression before trial and not renewing the objection when the evidence is offered at trial (Missouri requires a trial objection to preserve).
- Conceding consent was voluntary in a report or testimony without contesting scope or authority.
- Treating "no warrant" as the end of the analysis - most fights are about exceptions.

## Verify before relying
- Pull verbatim RSMo 542.296, Mo. Const. art. I sec. 15, and Fed. R. Crim. P. 12 via `statute-lookup` (or Descrybe `search_laws_and_rules`).
- Check every case is still good law and find a controlling Missouri appellate or 8th Circuit case applying the test to similar facts (CourtListener / Descrybe treatment).
- Recompute the pretrial-motion deadline from the scheduling order or arraignment date.
- Legal information, not legal advice; consult counsel or a public defender before a suppression hearing.

## Related skills
- `franks-affidavit-challenge` - attacks falsehoods and omissions in the affidavit.
- `mo-motion-to-suppress` - Missouri motion structure, hearing, and preservation.
- `malicious-prosecution-false-arrest` - civil claims arising from an unlawful seizure.
- `section-1983-claim-builder` / `qualified-immunity-analyzer` - damages route.
- `lexcore` - warrant/affidavit and suppression co-counsel workflow.
