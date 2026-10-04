---
name: federal-habeas-2254
description: Plans a 28 U.S.C. 2254 habeas petition for a Missouri state prisoner - custody, the AEDPA one-year limit and tolling, exhaustion, procedural default and gateways, 2254(d) deference, successive-petition bars. Use for "habeas petition", "2254", "AEDPA deadline", "exhaustion", "procedural default".
---

# Federal Habeas (28 U.S.C. 2254)

Maps whether and when a state-court conviction can be challenged in federal court, and frames each claim so it survives the AEDPA gatekeeping rules that defeat most petitions.

## When to use
- After a Missouri conviction once direct appeal and/or Rule 29.15 / 24.035 post-conviction proceedings are done or underway.
- Computing the one-year AEDPA deadline or checking whether it has run.
- Deciding whether a claim was properly presented in state court.
- Not for: Missouri post-conviction motions themselves (use `mo-post-conviction-relief`); federal prisoners (28 U.S.C. 2255 is a different statute).

## Gather first
- Dates: judgment and sentence; direct-appeal decision and mandate; any transfer application; post-conviction motion filing, ruling, appeal decision and mandate; any other state filings (Rule 91 habeas).
- Every claim raised at each level of state court, with the briefs - exhaustion depends on exact presentation.
- Current custody status (prison, parole, probation) and place of conviction.

## Workflow
1. **Custody.** Petitioner must be "in custody" under the challenged state judgment when filing (Maleng v. Cook, 490 U.S. 488 (1989)); parole and probation count; fully expired sentences generally do not. Claims must allege a violation of federal law - errors of state law are not cognizable.
2. **One-year limitation - 28 U.S.C. 2244(d)(1).** Runs from the latest of: (A) finality of the judgment on direct review or expiration of time to seek it; (B) removal of a state-created impediment; (C) a newly recognized, retroactive constitutional right; (D) when the factual predicate could have been discovered with due diligence.
   - Finality: if the petitioner did not seek review in the state's highest court, finality is when the time to seek it expired (Gonzalez v. Thaler, 565 U.S. 134 (2012)); if the highest state court ruled, add the 90-day period for a certiorari petition.
3. **Statutory tolling - 2244(d)(2).** Time is tolled while a "properly filed" application for state post-conviction or collateral review is pending. An untimely state motion is not properly filed (Pace v. DiGuglielmo, 544 U.S. 408 (2005)). No tolling for a cert petition from state post-conviction (Lawrence v. Florida, 549 U.S. 327 (2007)). Days between finality and the Rule 29.15/24.035 filing count against the year - compute the gap.
4. **Equitable tolling / actual innocence.** Equitable tolling requires diligence plus an extraordinary circumstance (Holland v. Florida, 560 U.S. 631 (2010)). A credible actual-innocence showing under the Schlup standard can overcome the time bar (McQuiggin v. Perkins, 569 U.S. 383 (2013); Schlup v. Delo, 513 U.S. 298 (1995)).
5. **Exhaustion - 2254(b)(1).** Each claim must be fairly presented, with its federal basis and operative facts, through one complete round of the state's established appellate review (O'Sullivan v. Boerckel, 526 U.S. 838 (1999)). Missouri has provided by rule that a transfer application to the Supreme Court of Missouri is not required for exhaustion - confirm the current Rule 83.04 text. Mixed petitions: Rose v. Lundy, 455 U.S. 509 (1982); stay-and-abeyance only for good cause, potentially meritorious claims, and no dilatory tactics (Rhines v. Weber, 544 U.S. 269 (2005)).
6. **Procedural default.** A claim the state courts rejected on an independent and adequate state procedural ground - or that can no longer be raised in state court (e.g., not included in the post-conviction appeal) - is defaulted (Coleman v. Thompson, 501 U.S. 722 (1991)). Gateways: cause and prejudice; fundamental miscarriage of justice (actual innocence). Ineffective post-conviction counsel can be cause for defaulting a substantial trial-IAC claim when the initial-review collateral proceeding was the first chance to raise it (Martinez v. Ryan, 566 U.S. 1 (2012)); but federal evidentiary development is limited by 2254(e)(2) (Shinn v. Ramirez, 596 U.S. 366 (2022)).
7. **Merits standard - 2254(d).** For claims adjudicated on the merits, relief only if the state decision was (1) contrary to or an unreasonable application of clearly established Supreme Court law, or (2) based on an unreasonable determination of facts in light of the state record. "Unreasonable" means beyond fairminded disagreement (Harrington v. Richter, 562 U.S. 86 (2011)); review under (d)(1) is limited to the state-court record (Cullen v. Pinholster, 563 U.S. 170 (2011)). State factual findings are presumed correct, rebuttable by clear and convincing evidence (2254(e)(1)). IAC claims are "doubly deferential" (Strickland plus AEDPA). Harmless error: Brecht v. Abrahamson, 507 U.S. 619 (1993).
8. **Second or successive.** One full round. A second petition needs prior authorization from the court of appeals (2244(b)(3)) and must meet 2244(b)(2). Put every claim in the first petition.
9. **Filing mechanics.** Use the district's 2254 form (Rules Governing Section 2254 Cases, Rule 2); venue in the district of conviction or confinement (28 U.S.C. 2241(d)) - E.D. or W.D. Mo.; name the custodian (warden) as respondent; IFP under 28 U.S.C. 1915 if needed. Appeal requires a certificate of appealability (28 U.S.C. 2253(c)).

## Output
- AEDPA clock table: | Event | Date | Days run | Days tolled | Running total of 365 |
- Claim exhaustion matrix: | Claim | Federal basis stated? | Trial | Direct appeal | PCR motion | PCR appeal | Status (exhausted/defaulted/unexhausted) | Gateway |
- Petition outline: custody; procedural history; timeliness; grounds (each: federal right, facts, state-court ruling, why 2254(d) is met); request for hearing; relief.

## Pitfalls
- Waiting until state proceedings end without tracking days already used before the PCR motion.
- Relying on an untimely or improperly filed state motion for tolling.
- Raising a claim in the 29.15 motion but dropping it on the post-conviction appeal - defaulted.
- Presenting only state-law grounds in state court - not fairly presented as federal.
- Filing piecemeal petitions and triggering the successive-petition bar.
- Assuming a Rule 91 state habeas petition revives an expired AEDPA clock - tolling cannot restart a period that already ran.
- Forgetting to add the 90-day certiorari window only when the state's highest court actually decided the case.
- Naming the State of Missouri instead of the custodian (warden) as respondent.
- Skipping a Martinez cause argument for a trial-IAC claim post-conviction counsel failed to raise.
- Expecting new evidence to be heard on 2254(d)(1) review; build the state-court record first.

## Verify before relying
- Pull verbatim 28 U.S.C. 2244, 2253, 2254, 2241(d), Missouri Rules 29.15, 24.035, 83.04 via `statute-lookup` (or Descrybe `search_laws_and_rules`).
- Confirm each case is good law and check current 8th Circuit treatment of Missouri tolling and default questions (CourtListener / Descrybe).
- Recompute the one-year deadline from actual file-stamped dates and mandate dates.
- Legal information, not legal advice; contact the Federal Public Defender or a habeas clinic - the deadline is unforgiving.

## Related skills
- `mo-post-conviction-relief` - Rule 29.15 / 24.035 claims that must come first.
- `brady-giglio-demands` / `sixth-amendment-counsel-confrontation` - common habeas grounds.
- `federal-ifp-1915` - fee status for the petition.
- `federal-appeals-8th-circuit` - COA and appeal mechanics.
