---
name: federal-subject-matter-jurisdiction
description: Determines whether a federal court has and will exercise subject-matter jurisdiction - federal question, diversity, supplemental, standing, removal and remand, Rooker-Feldman, Younger. Use for "can I sue in federal court", "removal", "remand", "Rooker-Feldman", "Younger", or "diversity".
---

# Federal Subject-Matter Jurisdiction

Decides whether a case belongs in federal court at all, and spots the doctrines that make federal judges send cases back or decline them.

## When to use
- Choosing between Missouri circuit court and federal district court
- A case was removed from state court, or removal is being considered
- A federal suit attacks a state-court judgment or a pending state proceeding
- Not for: personal jurisdiction and venue analysis in general — use `jurisdiction-and-venue-analyzer`

## Gather first
- The claims (federal statutes/constitutional provisions and state-law theories) and relief sought
- Citizenship of every party (domicile for individuals; state of incorporation and principal place of business for corporations; every member's citizenship for LLCs) and the amount in controversy
- Any related state-court case: status (pending/final), what it decided, dates of judgment and service

## Workflow
1. **Start with the burden.** The party invoking federal jurisdiction must establish it; jurisdiction cannot be waived or created by consent, and the court must check it on its own. Steel Co. v. Citizens for a Better Environment, 523 U.S. 83 (1998).
2. **Standing (Article III).** Injury in fact (concrete, particularized, actual or imminent), traceable to the defendant, redressable by the relief requested. Lujan v. Defenders of Wildlife, 504 U.S. 555 (1992). Separate standing needed for injunctive relief (ongoing or imminent future harm).
3. **Federal question — 28 U.S.C. 1331.** The federal issue must appear on the face of a well-pleaded complaint; an anticipated federal defense does not count. Louisville & Nashville R.R. v. Mottley, 211 U.S. 149 (1908). A 1983 claim satisfies 1331.
4. **Diversity — 28 U.S.C. 1332.** Complete diversity (no plaintiff shares citizenship with any defendant) and amount in controversy exceeding $75,000, exclusive of interest and costs. Corporate principal place of business is the "nerve center." Hertz Corp. v. Friend, 559 U.S. 77 (2010). Domestic-relations decrees and probate administration are outside diversity jurisdiction. Ankenbrandt v. Richards, 504 U.S. 689 (1992); Marshall v. Marshall, 547 U.S. 293 (2006).
5. **Supplemental — 28 U.S.C. 1367.** State claims forming part of the same case or controversy as a federal claim may be heard; the court may decline under 1367(c) (novel state issues, state claims predominate, all federal claims dismissed, exceptional circumstances). Expect dismissal of state claims without prejudice if federal claims fall early; 1367(d) tolls the state limitations period while the claim is pending and for 30 days after dismissal unless state law provides longer.
6. **Removal — 28 U.S.C. 1441, 1446, 1447.**
   - Only defendants remove, to the district embracing the state court.
   - Notice within 30 days after the defendant receives the initial pleading (or a later paper first showing removability); all properly joined and served defendants must consent (1446(b)(2)(A)).
   - Diversity removal is barred if any properly joined and served defendant is a citizen of the forum state (1441(b)(2)) and generally limited to one year after commencement absent bad faith (1446(c)(1)).
   - Remand: motion based on any defect other than lack of subject-matter jurisdiction must be made within 30 days after the notice of removal is filed; lack of SMJ requires remand at any time (1447(c)). Remand orders are largely unreviewable (1447(d)), with exceptions.
7. **Rooker-Feldman.** Lower federal courts cannot hear cases brought by state-court losers complaining of injuries caused by state-court judgments rendered before the federal suit, inviting review and rejection of those judgments. Exxon Mobil Corp. v. Saudi Basic Indus. Corp., 544 U.S. 280 (2005). It is narrow: it does not bar independent claims, claims against the adverse party's conduct, or suits filed while the state case is pending (those raise preclusion or abstention instead). Remedy for a bad state judgment is the state appellate process, then certiorari.
8. **Younger abstention.** Federal courts abstain from enjoining or interfering with ongoing (a) state criminal prosecutions, (b) civil enforcement proceedings akin to prosecutions, and (c) civil proceedings involving orders uniquely in furtherance of state courts' judicial functions. Younger v. Harris, 401 U.S. 37 (1971); Sprint Commc'ns, Inc. v. Jacobs, 571 U.S. 69 (2013). Then ask whether the state proceeding implicates important state interests and offers an adequate opportunity to raise federal claims (Middlesex County Ethics Comm. v. Garden State Bar Ass'n, 457 U.S. 423 (1982)). Exceptions: bad faith, harassment, flagrant unconstitutionality. Damages claims are typically stayed, not dismissed.
9. **Other bars.** Eleventh Amendment immunity of States and arms of the State; Tax Injunction Act (28 U.S.C. 1341); Anti-Injunction Act (28 U.S.C. 2283) for injunctions against state proceedings.
10. **Decide and document.** Record each basis and each bar with the facts supporting the conclusion.

## Output
- Jurisdiction table:

| Basis or bar | Test | Facts | Result | Authority |
|---|---|---|---|---|

- Recommendation: federal, state, or split strategy, with the risk of each
- If removed: remand deadline (30 days from notice of removal for procedural defects) and grounds

## Pitfalls
- Asking a federal district court to "overturn" or "void" a Missouri judgment (Rooker-Feldman)
- Suing in federal court to stop a pending criminal case (Younger)
- Pleading LLC citizenship by state of organization instead of its members
- Missing the 30-day window to seek remand for a procedural removal defect
- Alleging amount in controversy with no factual basis
- Assuming federal court is better; state court may offer fact pleading leniency, local juries, and no Younger issue

## Verify before relying
- Pull 28 U.S.C. 1331, 1332, 1367, 1441, 1446, 1447 verbatim via `statute-lookup` or Descrybe `search_laws_and_rules`.
- Check Eighth Circuit application of Rooker-Feldman and Younger via CourtListener before citing circuit cases.
- Recompute removal/remand deadlines from actual receipt and filing dates.
- Legal information, not legal advice.

## Related skills
- `jurisdiction-and-venue-analyzer` — personal jurisdiction, venue, state court selection
- `federal-complaint-pleading` — the jurisdictional statement in the complaint
- `federal-rule-12-motions` — 12(b)(1) motions
- `section-1983-claim-builder` — federal-question claims against state actors
