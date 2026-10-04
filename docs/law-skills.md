# Law Skill Pack

100 Claude Code skills for Missouri and federal litigation, written for pro se use. Each lives in `.claude/skills/<name>/SKILL.md` and loads automatically in Claude Code sessions in this repo.

Every skill ends with a **Verify before relying** step: pull verbatim statute and rule text with `statute-lookup`, confirm case law is still good law, and recompute deadlines from real dates. Numbers marked "verify" in a skill were not confirmed against the source when written. These skills give legal information, not legal advice.

## Legal method

- [`legal-issue-spotter`](../.claude/skills/legal-issue-spotter/SKILL.md) — find every claim/defense/procedural issue in a fact pattern
- [`irac-analysis`](../.claude/skills/irac-analysis/SKILL.md) — structured Issue/Rule/Application/Conclusion analysis
- [`elements-checklist-builder`](../.claude/skills/elements-checklist-builder/SKILL.md) — break a claim/crime/defense into elements mapped to evidence
- [`statutory-interpretation-canons`](../.claude/skills/statutory-interpretation-canons/SKILL.md) — plain meaning, canons, MO "plain and ordinary meaning", legislative history
- [`precedent-hierarchy-analyzer`](../.claude/skills/precedent-hierarchy-analyzer/SKILL.md) — binding vs persuasive authority in MO courts, 8th Cir., SCOTUS; distinguishing cases
- [`legal-citation-formatter`](../.claude/skills/legal-citation-formatter/SKILL.md) — Bluebook + Missouri citation conventions for briefs
- [`good-law-checker`](../.claude/skills/good-law-checker/SKILL.md) — confirm a case/statute is still good law (overruled, amended, superseded)
- [`quote-and-cite-verifier`](../.claude/skills/quote-and-cite-verifier/SKILL.md) — verify every quotation and pin cite in a draft against the source
- [`jurisdiction-and-venue-analyzer`](../.claude/skills/jurisdiction-and-venue-analyzer/SKILL.md) — which court (state/federal, circuit/associate), personal jurisdiction, venue
- [`standard-of-review-finder`](../.claude/skills/standard-of-review-finder/SKILL.md) — de novo, abuse of discretion, substantial evidence, plain error by issue type

## Missouri civil procedure I

- [`mo-petition-drafting`](../.claude/skills/mo-petition-drafting/SKILL.md) — Rule 55 fact pleading, counts, prayer, caption
- [`mo-service-of-process`](../.claude/skills/mo-service-of-process/SKILL.md) — Rule 54 service methods, summons, proof of service, service on entities
- [`mo-answer-affirmative-defenses`](../.claude/skills/mo-answer-affirmative-defenses/SKILL.md) — answers, Rule 55.08 affirmative defenses, counterclaims, waiver
- [`mo-motion-to-dismiss`](../.claude/skills/mo-motion-to-dismiss/SKILL.md) — Rule 55.27 grounds, failure to state a claim under MO fact pleading
- [`mo-summary-judgment`](../.claude/skills/mo-summary-judgment/SKILL.md) — Rule 74.04 statement of uncontroverted facts, responses, ITT Commercial Finance standard
- [`mo-discovery-requests`](../.claude/skills/mo-discovery-requests/SKILL.md) — interrogatories, requests for production, admissions, depositions (Rules 56–59)
- [`mo-motion-to-compel-sanctions`](../.claude/skills/mo-motion-to-compel-sanctions/SKILL.md) — Rule 61 sanctions, meet-and-confer, golden-rule letter
- [`mo-default-judgment-set-aside`](../.claude/skills/mo-default-judgment-set-aside/SKILL.md) — default entry, Rule 74.05(d) set-aside, Rule 74.06 relief
- [`mo-small-claims-associate-circuit`](../.claude/skills/mo-small-claims-associate-circuit/SKILL.md) — small claims limits, associate circuit procedure, trial de novo
- [`mo-change-of-judge-venue`](../.claude/skills/mo-change-of-judge-venue/SKILL.md) — Rule 51 change of judge/venue timing and grounds

## Missouri civil procedure II & deadlines

- [`mo-post-trial-motions`](../.claude/skills/mo-post-trial-motions/SKILL.md) — motion for new trial, amend judgment, Rule 75.01 control period, 78.04
- [`mo-deadline-calculator`](../.claude/skills/mo-deadline-calculator/SKILL.md) — Rule 44.01 computation, mail extension, holidays, jurisdictional vs claim deadlines
- [`mo-poor-person-filing`](../.claude/skills/mo-poor-person-filing/SKILL.md) — Missouri in forma pauperis (RSMo 514.040), fee waivers, affidavit content
- [`mo-temporary-restraining-order`](../.claude/skills/mo-temporary-restraining-order/SKILL.md) — Rule 92 TRO/preliminary injunction elements and bond
- [`mo-declaratory-judgment`](../.claude/skills/mo-declaratory-judgment/SKILL.md) — Rule 87 / RSMo ch. 527 justiciable controversy
- [`mo-replevin-and-property-recovery`](../.claude/skills/mo-replevin-and-property-recovery/SKILL.md) — recovering wrongfully held personal property
- [`mo-garnishment-and-execution`](../.claude/skills/mo-garnishment-and-execution/SKILL.md) — collecting/defending judgments, exemptions (RSMo 513.430, 525)
- [`mo-pretrial-and-trial-prep`](../.claude/skills/mo-pretrial-and-trial-prep/SKILL.md) — pretrial conference, witness/exhibit lists, jury vs bench, motions in limine
- [`mo-jury-instructions-mai`](../.claude/skills/mo-jury-instructions-mai/SKILL.md) — Missouri Approved Instructions selection and modification
- [`mo-pro-se-courtroom-procedure`](../.claude/skills/mo-pro-se-courtroom-procedure/SKILL.md) — conduct, courtroom etiquette, making a record, offers of proof

## Missouri criminal procedure

- [`mo-criminal-case-roadmap`](../.claude/skills/mo-criminal-case-roadmap/SKILL.md) — arrest → charge → arraignment → prelim → trial → sentence, with deadlines
- [`mo-bond-pretrial-release`](../.claude/skills/mo-bond-pretrial-release/SKILL.md) — Rule 33.01 factors, bond reduction motions
- [`mo-preliminary-hearing`](../.claude/skills/mo-preliminary-hearing/SKILL.md) — probable cause standard, cross-examination use
- [`mo-criminal-discovery`](../.claude/skills/mo-criminal-discovery/SKILL.md) — Rule 25.03 disclosures, sanctions for nondisclosure
- [`mo-speedy-trial`](../.claude/skills/mo-speedy-trial/SKILL.md) — RSMo 545.780, constitutional Barker v. Wingo factors, detainers/IAD
- [`mo-motion-to-suppress`](../.claude/skills/mo-motion-to-suppress/SKILL.md) — suppression motion structure in MO courts, burden on state, hearing prep
- [`mo-plea-and-sentencing`](../.claude/skills/mo-plea-and-sentencing/SKILL.md) — Rule 24.02 plea colloquy, SIS/SES, sentencing assessment report, probation
- [`mo-post-conviction-relief`](../.claude/skills/mo-post-conviction-relief/SKILL.md) — Rule 29.15 / 24.035 timelines, ineffective assistance (Strickland)
- [`mo-expungement`](../.claude/skills/mo-expungement/SKILL.md) — RSMo 610.140 eligibility, waiting periods, petition
- [`mo-municipal-ordinance-defense`](../.claude/skills/mo-municipal-ordinance-defense/SKILL.md) — municipal court procedure, trial de novo, traffic/ordinance defenses

## Federal civil

- [`federal-complaint-pleading`](../.claude/skills/federal-complaint-pleading/SKILL.md) — Rule 8, Twombly/Iqbal plausibility, pro se liberal construction
- [`section-1983-claim-builder`](../.claude/skills/section-1983-claim-builder/SKILL.md) — color of law, constitutional violation, causation, Monell municipal liability
- [`qualified-immunity-analyzer`](../.claude/skills/qualified-immunity-analyzer/SKILL.md) — clearly established law, two-prong test, 8th Cir. approach
- [`federal-rule-12-motions`](../.claude/skills/federal-rule-12-motions/SKILL.md) — 12(b)(1)-(6), 12(c), 12(e), responding and amending (Rule 15)
- [`federal-subject-matter-jurisdiction`](../.claude/skills/federal-subject-matter-jurisdiction/SKILL.md) — federal question, diversity, supplemental, removal/remand, Rooker-Feldman, Younger
- [`federal-ifp-1915`](../.claude/skills/federal-ifp-1915/SKILL.md) — 28 U.S.C. 1915 IFP application and frivolousness screening
- [`federal-civil-discovery`](../.claude/skills/federal-civil-discovery/SKILL.md) — Rules 26–37, initial disclosures, proportionality, protective orders
- [`federal-summary-judgment`](../.claude/skills/federal-summary-judgment/SKILL.md) — Rule 56, genuine dispute, local rule statements of fact
- [`federal-tro-preliminary-injunction`](../.claude/skills/federal-tro-preliminary-injunction/SKILL.md) — Rule 65, Dataphase factors (8th Cir.)
- [`federal-appeals-8th-circuit`](../.claude/skills/federal-appeals-8th-circuit/SKILL.md) — FRAP notice of appeal deadlines, final judgment rule, briefing

## Constitutional & criminal rights

- [`fourth-amendment-analyzer`](../.claude/skills/fourth-amendment-analyzer/SKILL.md) — search/seizure, warrants, exceptions, standing, exclusionary rule
- [`franks-affidavit-challenge`](../.claude/skills/franks-affidavit-challenge/SKILL.md) — Franks v. Delaware showing, false statements/omissions, warrant affidavit attack
- [`miranda-and-confessions`](../.claude/skills/miranda-and-confessions/SKILL.md) — custody + interrogation, waiver, voluntariness
- [`sixth-amendment-counsel-confrontation`](../.claude/skills/sixth-amendment-counsel-confrontation/SKILL.md) — right to counsel, self-representation (Faretta), Confrontation Clause (Crawford)
- [`brady-giglio-demands`](../.claude/skills/brady-giglio-demands/SKILL.md) — exculpatory/impeachment evidence demands and violation motions
- [`federal-habeas-2254`](../.claude/skills/federal-habeas-2254/SKILL.md) — AEDPA exhaustion, procedural default, 1-year limitation
- [`due-process-analyzer`](../.claude/skills/due-process-analyzer/SKILL.md) — procedural (Mathews v. Eldridge) and substantive due process
- [`equal-protection-analyzer`](../.claude/skills/equal-protection-analyzer/SKILL.md) — tiers of scrutiny, class-of-one, selective enforcement
- [`first-amendment-analyzer`](../.claude/skills/first-amendment-analyzer/SKILL.md) — speech, retaliation, petition clause, public forum
- [`malicious-prosecution-false-arrest`](../.claude/skills/malicious-prosecution-false-arrest/SKILL.md) — state tort and Fourth Amendment claims, probable cause defense

## Evidence & trial

- [`mo-evidence-rules`](../.claude/skills/mo-evidence-rules/SKILL.md) — Missouri evidence (common law + RSMo ch. 490/491), differences from FRE
- [`hearsay-analyzer`](../.claude/skills/hearsay-analyzer/SKILL.md) — definition, exclusions, exceptions (FRE 801–807 and MO counterparts)
- [`authentication-foundation-builder`](../.claude/skills/authentication-foundation-builder/SKILL.md) — laying foundation for documents, texts, emails, video, social media
- [`expert-witness-challenge`](../.claude/skills/expert-witness-challenge/SKILL.md) — Daubert/FRE 702 and RSMo 490.065
- [`privilege-analyzer`](../.claude/skills/privilege-analyzer/SKILL.md) — attorney-client, work product, spousal, Fifth Amendment
- [`evidence-timeline-builder`](../.claude/skills/evidence-timeline-builder/SKILL.md) — chronology from evidence with source citations and gaps
- [`exhibit-list-and-trial-binder`](../.claude/skills/exhibit-list-and-trial-binder/SKILL.md) — numbering, exhibit lists, binders, stipulations
- [`objection-playbook`](../.claude/skills/objection-playbook/SKILL.md) — common objections, when/how to object, preserving error
- [`witness-examination-planner`](../.claude/skills/witness-examination-planner/SKILL.md) — direct/cross outlines, impeachment with prior statements
- [`impeachment-and-credibility`](../.claude/skills/impeachment-and-credibility/SKILL.md) — bias, prior inconsistent statements, convictions (RSMo 491.050)

## Torts, damages, limitations, immunity

- [`negligence-claim-builder`](../.claude/skills/negligence-claim-builder/SKILL.md) — duty, breach, causation, damages; MO comparative fault
- [`intentional-torts`](../.claude/skills/intentional-torts/SKILL.md) — battery, assault, false imprisonment, IIED, conversion, trespass
- [`defamation-analyzer`](../.claude/skills/defamation-analyzer/SKILL.md) — MO defamation elements, privilege, public figures, damages
- [`abuse-of-process-and-civil-conspiracy`](../.claude/skills/abuse-of-process-and-civil-conspiracy/SKILL.md) — elements and pleading
- [`premises-and-landlord-liability`](../.claude/skills/premises-and-landlord-liability/SKILL.md) — invitee/licensee duties, dangerous condition
- [`damages-calculator`](../.claude/skills/damages-calculator/SKILL.md) — economic, non-economic, punitive (RSMo 510.261–.265), prejudgment interest
- [`statute-of-limitations-checker`](../.claude/skills/statute-of-limitations-checker/SKILL.md) — RSMo ch. 516, federal borrowing for 1983, tolling, accrual
- [`sovereign-and-official-immunity-mo`](../.claude/skills/sovereign-and-official-immunity-mo/SKILL.md) — RSMo 537.600 waivers, official immunity, public duty doctrine
- [`government-notice-of-claim`](../.claude/skills/government-notice-of-claim/SKILL.md) — notice requirements before suing governments, 1983 vs state claims
- [`wrongful-death-and-survival-mo`](../.claude/skills/wrongful-death-and-survival-mo/SKILL.md) — RSMo 537.080 claimants, damages, limitations

## Contracts, UCC, consumer, property, family

- [`contract-breach-analyzer`](../.claude/skills/contract-breach-analyzer/SKILL.md) — formation, breach, defenses, remedies under MO law
- [`ucc-article-2-sales`](../.claude/skills/ucc-article-2-sales/SKILL.md) — goods, warranties, acceptance/rejection, remedies
- [`ucc-article-3-negotiable-instruments`](../.claude/skills/ucc-article-3-negotiable-instruments/SKILL.md) — notes, holder in due course, endorsements
- [`ucc-article-9-secured-transactions`](../.claude/skills/ucc-article-9-secured-transactions/SKILL.md) — attachment, perfection, priority, repossession
- [`mo-merchandising-practices-act`](../.claude/skills/mo-merchandising-practices-act/SKILL.md) — RSMo 407.025 consumer fraud claims
- [`fdcpa-fcra-consumer-defense`](../.claude/skills/fdcpa-fcra-consumer-defense/SKILL.md) — debt collection violations, credit reporting disputes, debt suits defense
- [`mo-landlord-tenant-eviction`](../.claude/skills/mo-landlord-tenant-eviction/SKILL.md) — rent and possession, unlawful detainer (RSMo 534/535), defenses, deposits
- [`mo-family-law-dissolution-custody`](../.claude/skills/mo-family-law-dissolution-custody/SKILL.md) — dissolution (RSMo 452), parenting plans, Form 14 child support, modification
- [`mo-orders-of-protection`](../.claude/skills/mo-orders-of-protection/SKILL.md) — RSMo 455 adult/child orders, ex parte, full hearing
- [`mo-wills-trusts-probate`](../.claude/skills/mo-wills-trusts-probate/SKILL.md) — wills, trusts, POA, small estate affidavit (RSMo 473.097), probate basics

## Government, appeals, advocacy

- [`sunshine-and-foia-requests`](../.claude/skills/sunshine-and-foia-requests/SKILL.md) — MO Sunshine Law (RSMo 610) and federal FOIA requests and appeals
- [`mo-administrative-appeals`](../.claude/skills/mo-administrative-appeals/SKILL.md) — RSMo 536 judicial review, AHC, exhaustion
- [`employment-discrimination-claims`](../.claude/skills/employment-discrimination-claims/SKILL.md) — MHRA and Title VII charges, deadlines, right-to-sue
- [`misconduct-complaints`](../.claude/skills/misconduct-complaints/SKILL.md) — judicial, attorney (OCDC), and police misconduct complaints
- [`mo-appeals-procedure`](../.claude/skills/mo-appeals-procedure/SKILL.md) — Rule 81 notice of appeal, record on appeal, Rule 84.04 points relied on
- [`writs-mandamus-prohibition`](../.claude/skills/writs-mandamus-prohibition/SKILL.md) — extraordinary writs (Rules 94, 97), when available
- [`appellate-brief-writer`](../.claude/skills/appellate-brief-writer/SKILL.md) — structure, standard of review per point, preservation
- [`legal-memo-writer`](../.claude/skills/legal-memo-writer/SKILL.md) — objective research memo format with verified citations
- [`court-document-formatting`](../.claude/skills/court-document-formatting/SKILL.md) — captions, signature blocks, certificate of service, MO and federal local rules
- [`settlement-and-demand-letters`](../.claude/skills/settlement-and-demand-letters/SKILL.md) — demand letters, negotiation, settlement agreements, releases
