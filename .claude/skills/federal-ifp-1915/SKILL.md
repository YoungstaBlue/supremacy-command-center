---
name: federal-ifp-1915
description: Prepares a federal in forma pauperis application under 28 U.S.C. 1915 and readies the complaint for 1915(e)(2)/1915A screening, Marshal service, three strikes, IFP on appeal, and counsel requests. Use for "IFP", "can't afford federal filing fee", "AO 240", or "1915 screening".
---

# Federal IFP Under 28 U.S.C. 1915

Gets a federal case filed without prepaying fees and past the court's initial screening, which dismisses many pro se complaints before any defendant is served.

## When to use
- Filing a federal civil action or appeal without paying the filing fee up front
- A court entered a screening order or 1915(e)(2) dismissal
- Asking the court to request counsel or to order Marshal service
- Not for: Missouri state-court fee waivers under RSMo 514.040 — use `mo-poor-person-filing`

## Gather first
- Monthly income from all sources, assets, debts, dependents, and monthly expenses (exact figures)
- Whether the filer is a prisoner (changes fee rules and adds 1915A screening and 1915(g))
- The draft complaint, and any prior federal cases the filer brought and how they ended

## Workflow
1. **Application (1915(a)(1)).** An affidavit listing all assets and stating inability to pay fees or give security, the nature of the action, and belief of entitlement to redress. Use the district's form (commonly the AO 240 short form or AO 239 long form — check which the district requires). Indigence need not be absolute destitution. Adkins v. E.I. DuPont de Nemours & Co., 335 U.S. 331 (1948).
2. **Accuracy.** Answer every question; write "0" or "none" rather than leaving blanks; explain irregular income and support from others. The court must dismiss at any time if the allegation of poverty is untrue (1915(e)(2)(A)), and false statements under penalty of perjury carry their own risk.
3. **Prisoners.** Attach a certified trust-account statement for the 6 months before filing (1915(a)(2)). Prisoners still owe the full fee: an initial partial fee (20 percent of the greater of average monthly deposits or average monthly balance), then monthly payments of 20 percent of the preceding month's income when the account exceeds $10 (1915(b)). Prisoner complaints against government entities or employees are also screened under 28 U.S.C. 1915A, and PLRA exhaustion applies.
4. **Three strikes (1915(g)).** A prisoner with three prior dismissals as frivolous, malicious, or for failure to state a claim cannot proceed IFP unless under imminent danger of serious physical injury. A dismissal counts even while on appeal (Coleman v. Tollefson, 575 U.S. 532 (2015)) and even if without prejudice for failure to state a claim (Lomax v. Ortiz-Marquez, 590 U.S. 595 (2020)).
5. **Screening (1915(e)(2)(B)).** The court shall dismiss at any time if the action (i) is frivolous or malicious, (ii) fails to state a claim, or (iii) seeks monetary relief against an immune defendant.
   - Frivolous: lacks an arguable basis in law or fact. Neitzke v. Williams, 490 U.S. 319 (1989). Factual frivolousness means fanciful, fantastic, or delusional allegations. Denton v. Hernandez, 504 U.S. 25 (1992).
   - Failure to state a claim: the Twombly/Iqbal standard, with liberal construction for pro se filings.
   - Pre-screen the complaint: name only proper, non-immune defendants (no judges for judicial acts, no prosecutors for charging decisions, no State for damages); plead each defendant's specific acts; state capacity.
6. **After a screening order.** Courts often dismiss some defendants and allow others, or grant leave to file an amended complaint by a deadline. Meet the deadline; the amended complaint replaces the original entirely. Dismissal without prejudice usually allows refiling, but limitations keep running.
7. **Service.** When IFP is granted, court officers issue and serve process (1915(d)); the court must order service by the U.S. Marshal or a deputy if requested (FRCP 4(c)(3)). Provide complete, accurate addresses for each defendant; bad addresses are the plaintiff's responsibility to cure.
8. **Counsel.** The court may request an attorney to represent an IFP litigant (1915(e)(1)); it cannot compel one (Mallard v. U.S. Dist. Court, 490 U.S. 296 (1989)). There is no general right to counsel in civil cases. A motion should address factual and legal complexity, ability to investigate, conflicting testimony, and the litigant's ability to present the claims; verify the current Eighth Circuit factor list before citing it.
9. **IFP on appeal.** FRAP 24(a): a party allowed IFP in district court may proceed on appeal without further authorization unless the district court certifies the appeal is not taken in good faith or finds the party no longer qualifies (see also 1915(a)(3)). If certified as not in good faith, a motion may be filed in the court of appeals within 30 days after service of that notice.

## Output
- Completed financial worksheet mirroring the district's IFP form, with every line filled
- Screening pre-check table:

| Defendant | Immune? | Specific acts pleaded? | Capacity stated? | Claim plausible? | Fix |
|---|---|---|---|---|---|

- If screened: list of court-ordered deadlines and what each requires
- Optional motion for appointment of counsel addressing the complexity factors

## Pitfalls
- Leaving blanks or understating income/assets (dismissal under 1915(e)(2)(A))
- Naming judges, prosecutors, or the State for damages — triggers 1915(e)(2)(B)(iii) dismissal
- Ignoring a screening order's amendment deadline
- Prisoners: filing weak suits that accumulate strikes
- Assuming IFP waives all costs; costs may still be taxed against a losing IFP party

## Verify before relying
- Pull 28 U.S.C. 1915 and 1915A, FRCP 4(c)(3), FRAP 24, and the district's local IFP rules verbatim via `statute-lookup` or Descrybe `search_laws_and_rules`.
- Confirm current filing fee amounts and IFP forms on the district court website.
- Compute any screening-order or FRAP 24 deadline from the actual service date.
- Legal information, not legal advice; ask the clerk's pro se office about local procedures.

## Related skills
- `mo-poor-person-filing` — state-court counterpart
- `federal-complaint-pleading` — survive the 1915(e)(2)(B)(ii) review
- `section-1983-claim-builder` — proper defendants and capacities
- `federal-appeals-8th-circuit` — IFP status on appeal
