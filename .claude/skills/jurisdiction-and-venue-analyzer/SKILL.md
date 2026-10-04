---
name: jurisdiction-and-venue-analyzer
description: Decides which court can hear a case - Missouri small claims, associate circuit, circuit, or federal court - testing subject-matter and personal jurisdiction, venue, and removal. Use for "which court do I file in", "personal jurisdiction", "wrong venue", "out-of-state defendant", or "remove to federal court".
---

# Jurisdiction and Venue Analyzer

Picks the correct court and county/division before filing, and tests the other side's court choice, so the case is not dismissed, transferred, or voided for being in the wrong place.

## When to use
- Before filing: "Where do I file this?", "State or federal court?", "Small claims or circuit?"
- Defending: the case was filed in the wrong county, the wrong court, or against a defendant with no Missouri contacts.
- A defendant removed the case to federal court, or the user wants to remove or remand.
- Not for: deep federal subject-matter questions such as Rooker-Feldman, Younger, or standing (use `federal-subject-matter-jurisdiction`).

## Gather first
- Each party's state of residence/citizenship (for entities: state of incorporation or organization and principal place of business; for LLCs, every member's citizenship).
- Where the events happened and where the injury was first suffered, and the amount or type of relief sought.
- The legal basis of each claim (Missouri law, federal statute, U.S. Constitution) and, if already sued, the date of service.

## Workflow
1. **Subject-matter jurisdiction — Missouri.** Circuit courts have original jurisdiction over all cases and matters, civil and criminal (Mo. Const. art. V, § 14). Missouri treats subject-matter jurisdiction as constitutional; many statutory limits are about a court's authority, not its jurisdiction (see J.C.W. ex rel. Webb v. Wyciskalla, 275 S.W.3d 249 (Mo. banc 2009)).
2. **Choose the Missouri division.**
   - Small claims: claims at or below the statutory limit (RSMo 482.305 — verify current dollar limit); simplified procedure, limited discovery, no jury; a party may seek trial de novo. Check limits on how often a party may file.
   - Associate circuit division: handles cases under RSMo chapter 517 procedure (including landlord-tenant and smaller civil claims) — verify the current monetary threshold and local assignment practice.
   - Circuit division: larger civil claims, equity (injunctions, declaratory judgment), and felony trials. Local court rules govern assignment.
3. **Subject-matter jurisdiction — federal.**
   - Federal question: the claim arises under federal law (28 U.S.C. § 1331), e.g., 42 U.S.C. § 1983 claims. Judged by the well-pleaded complaint, not by anticipated defenses.
   - Diversity: complete diversity of citizenship and more than $75,000 in controversy (28 U.S.C. § 1332).
   - Supplemental: related state-law claims forming part of the same case or controversy (28 U.S.C. § 1367), which the court may decline after dismissing federal claims.
   - Bars to check: Rooker-Feldman (no federal review of state-court judgments, Exxon Mobil Corp. v. Saudi Basic Industries Corp., 544 U.S. 280 (2005)); Younger abstention for ongoing state criminal and certain civil proceedings (Younger v. Harris, 401 U.S. 37 (1971)); Eleventh Amendment immunity for the State and its agencies.
4. **Personal jurisdiction.**
   - Missouri long-arm statute: RSMo 506.500 (transaction of business, making a contract, tortious act in Missouri, and others). The claim must arise from the enumerated act.
   - Due process: minimum contacts so suit does not offend traditional notions of fair play and substantial justice (International Shoe Co. v. Washington, 326 U.S. 310 (1945)). General jurisdiction over a corporation is usually limited to its place of incorporation and principal place of business (Daimler AG v. Bauman, 571 U.S. 117 (2014)). Specific jurisdiction requires a claim arising out of or relating to forum contacts (Ford Motor Co. v. Montana Eighth Judicial District Court, 592 U.S. 351 (2021); Bristol-Myers Squibb Co. v. Superior Court, 582 U.S. 255 (2017)).
   - Registering to do business in Missouri does not by itself establish consent to general jurisdiction under Missouri's registration statute (State ex rel. Norfolk Southern Railway Co. v. Dolan, 512 S.W.3d 41 (Mo. banc 2017)); Mallory v. Norfolk Southern Railway Co., 600 U.S. 122 (2023), upheld a different state's consent-by-registration statute — check current Missouri law.
   - Federal courts in Missouri generally use the Missouri long-arm statute plus due process (Fed. R. Civ. P. 4(k)(1)(A)).
   - Individuals served while physically present in Missouri are generally subject to jurisdiction.
5. **Venue — Missouri.** RSMo 508.010 governs most civil venue (for torts, the county where the plaintiff was first injured is the key rule; for other cases it depends on defendant residence and the type of defendant — verify the applicable subsection). Special venue statutes apply to some actions (e.g., against the state, municipalities, or under particular statutes). Change of venue and change of judge are governed by Rule 51 with strict timing.
6. **Venue — federal.** 28 U.S.C. § 1391(b): where any defendant resides (if all reside in the state), where a substantial part of the events occurred, or a fallback. Missouri has two districts (Eastern and Western), each with divisions; check the local rule assigning counties to divisions. Transfer: § 1404(a) (convenience) and § 1406(a) (wrong venue).
7. **Removal and remand.** A defendant may remove a case that could have been filed in federal court (28 U.S.C. § 1441), generally within 30 days after service of the initial pleading (§ 1446(b)). Diversity cases cannot be removed if any properly joined and served defendant is a Missouri citizen (§ 1441(b)(2)). A motion to remand for non-jurisdictional defects must be filed within 30 days after removal; lack of subject-matter jurisdiction can be raised anytime (§ 1447(c)).
8. **Waiver timing.** Personal jurisdiction, venue, process, and service defenses are waived if not raised in the first motion or responsive pleading — Missouri Rule 55.27(g) and Federal Rule 12(h)(1). Subject-matter jurisdiction is never waived.

## Output
- **Recommended court and venue** with a one-paragraph reason.
- **Checklist table:** `Question | Answer | Facts relied on | Authority | Risk`, covering SMJ, division, PJ (per defendant), venue, removal/remand, waiver deadlines.
- **Alternatives** (other proper courts) and the strategic trade-offs (jury pool, procedure, speed, appeal route).

## Pitfalls
- Filing a § 1983 claim in state court without considering that the defendant may remove it — or filing in federal court without checking Rooker-Feldman and Younger.
- Pleading diversity without alleging each party's citizenship (not residence) and every LLC member's citizenship.
- Missing the 30-day removal or remand windows.
- Answering on the merits before raising personal jurisdiction or venue, which waives them.
- Choosing small claims for a claim above the limit, or not understanding what is given up there.
- Suing an out-of-state defendant with no Missouri contacts related to the claim.

## Verify before relying
- Pull verbatim text of every statute/rule cited via `statute-lookup` (or Descrybe `search_laws_and_rules`); check case law is still good law (CourtListener / Descrybe treatment) before citing.
- Confirm current dollar limits and local division assignments with the court clerk or local rules.
- Recompute any deadline from the actual service/entry date.
- Legal information, not legal advice; recommend counsel/legal aid for high-stakes decisions.

## Related skills
- `federal-subject-matter-jurisdiction` — removal, remand, abstention, and standing in depth.
- `mo-change-of-judge-venue` — Rule 51 changes once a case is filed.
- `mo-small-claims-associate-circuit` — small-claims and associate-circuit procedure.
- `legal-issue-spotter` — find all claims before picking the court.
- `lawmind-god-drafter` — draft the petition or complaint once the court is chosen.
