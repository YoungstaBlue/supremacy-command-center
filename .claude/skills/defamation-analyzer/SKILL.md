---
name: defamation-analyzer
description: Analyzes Missouri libel and slander claims - the six Overcast elements, fact vs opinion, absolute and qualified privilege, public-figure actual malice, anti-SLAPP, the 2-year limit, and proof of reputational damages. Use for "defamation", "libel", "slander", "false statements about me", or "they posted lies online".
---

# Defamation Analyzer

Tests whether a statement is actionable defamation under Missouri law and the First Amendment, and identifies the privileges and defenses that will be raised against it.

## When to use
- Someone published a false statement about the user (post, review, letter, report, spoken statement)
- The user is being threatened with or sued for defamation
- Statements made in police reports, court filings, employer communications, or online
- Not for: retaliation for the user's own speech by government (use `first-amendment-analyzer`)

## Gather first
- The exact words, verbatim, and a copy/screenshot with date and URL or recipient list
- Date of first publication (2-year limitations period runs from it)
- Who the user is relative to the subject (private person, public official, public figure, involved in a public controversy)

## Workflow
1. **Elements.** Missouri requires: (1) publication, (2) of a defamatory statement, (3) that identifies the plaintiff, (4) that is false, (5) published with the requisite degree of fault, and (6) that damages the plaintiff's reputation - Overcast v. Billings Mutual Insurance Co., 11 S.W.3d 62 (Mo. banc 2000). Build a row for each.
2. **Publication.** Communicated to at least one third party. Each republication can be a separate publication; identify the original speaker versus republishers.
3. **Defamatory meaning.** Read the statement in context, as a whole, giving words their plain and ordinary meaning; does it tend to harm reputation or deter others from dealing with the plaintiff?
4. **Fact vs opinion.** Only statements that are provably false (or imply provably false facts) are actionable. Milkovich v. Lorain Journal Co., 497 U.S. 1 (1990) rejects a blanket opinion privilege but protects statements not provably false and rhetorical hyperbole. "I think he is a thief" still implies a fact; "worst landlord ever" does not.
5. **Falsity.** Truth (including substantial truth) defeats the claim. On matters of public concern, plaintiff carries the burden of proving falsity.
6. **Fault level.**
   - Public official/public figure: actual malice - knowledge of falsity or reckless disregard - by clear and convincing evidence (New York Times Co. v. Sullivan, 376 U.S. 254 (1964)).
   - Private figure: at least negligence (Gertz v. Robert Welch, Inc., 418 U.S. 323 (1974) lets states set the standard but bars liability without fault).
   - Limited-purpose public figure: voluntarily injected into a particular controversy - actual malice applies only to statements about that controversy.
7. **Privileges.**
   - Absolute: statements in judicial proceedings that are relevant to the proceeding (pleadings, testimony, filings); legislative statements; certain official statements. Defamation claims over what was said in a lawsuit usually fail here.
   - Qualified: common-interest communications (employer references, reports to police or authorities made in good faith). Plaintiff defeats it by showing actual malice/abuse of the privilege.
   - Fair report of official proceedings.
   - Missouri anti-SLAPP statute, RSMo 537.528: covers statements made in connection with a public hearing or public meeting; allows a special motion to dismiss with expedited handling and fee shifting. Narrower than many states - check whether the statement fits.
8. **Damages.** Missouri abolished the per se/per quod distinction and requires proof of actual damage to reputation - Nazeri v. Missouri Valley College, 860 S.W.2d 303 (Mo. banc 1993). Gather evidence of lost jobs, customers, relationships, community standing. Emotional distress alone, without reputational harm, is weak. Punitive damages require actual malice and leave of court (RSMo 510.261).
9. **Limitations.** RSMo 516.140: 2 years for libel and slander. Run `statute-of-limitations-checker` for accrual (generally first publication).
10. **Alternatives.** Injurious falsehood (also 2 years under 516.140), false light (Missouri recognition is limited - verify), tortious interference, IIED (barred where duplicative).

## Output
- Statement-by-statement table: | Exact words | Publisher | Audience | Date | Fact or opinion | Provably false? | Privilege | Fault level | Damage proof |
- Viability rating per statement (strong / weak / barred) with reason
- Draft count quoting the statement verbatim, pleading falsity, fault, and specific reputational harm
- Defense list if the user is the defendant (truth, opinion, privilege, anti-SLAPP motion window)

## Pitfalls
- Paraphrasing the statement - plead the exact words
- Suing over statements in court filings or testimony (absolute privilege)
- Missing the 2-year deadline, especially for older posts
- No evidence of reputational harm, only hurt feelings
- Treating a public-figure case as a negligence case
- Ignoring that a truthful but embarrassing statement is not defamation

## Verify before relying
- Pull verbatim RSMo 516.140, 537.528, 510.261 via `statute-lookup` (or Descrybe `search_laws_and_rules`)
- Confirm Overcast, Nazeri, and the U.S. Supreme Court cases remain good law; check recent Missouri treatment of opinion and privilege (CourtListener / Descrybe)
- Recompute limitations from the first-publication date
- Legal information, not legal advice; defamation suits carry fee-shifting and counterclaim risk - consider counsel

## Related skills
- `first-amendment-analyzer` - constitutional limits on speech liability
- `intentional-torts` - IIED and related claims
- `statute-of-limitations-checker` - publication accrual
- `damages-calculator` - reputational and punitive damages
- `lawmind-strategy-engine` - weigh counterclaim and anti-SLAPP exposure
