---
name: mo-answer-affirmative-defenses
description: Drafts a Missouri answer paragraph by paragraph, pleads Rule 55.08 affirmative defenses with supporting facts, and flags compulsory counterclaims under Rule 55.32 and waiver risks. Use for "answer the petition", "I got sued in Missouri", "affirmative defenses", "counterclaim", or "deadline to answer".
---

# Missouri Answer, Affirmative Defenses, and Counterclaims

Produces a timely Missouri answer that admits or denies every averment, preserves every defense that must be pleaded or is lost, and asserts any counterclaim that must be brought now.

## When to use
- Served with a Missouri petition and the 30-day answer clock is running
- Answering an amended petition, a counterclaim (reply), or a cross-claim
- Auditing an answer already filed for missing affirmative defenses (and moving to amend)
- Not for: deciding whether to move to dismiss first (use `mo-motion-to-dismiss`); small claims, where formal answers are generally not required (use `mo-small-claims-associate-circuit`)

## Gather first
- The petition with every numbered paragraph, plus the date and manner of service
- Your version of the facts and any documents (contracts, payments, releases, prior judgments)
- Any claim you have against the plaintiff arising from the same events

## Workflow
1. **Compute the deadline.** Answer due 30 days after service of summons and petition (Rule 55.25(a) - verify). If a Rule 55.27 motion is filed instead, the answer is due a short period after the court rules (verify Rule 55.25). Recompute with `mo-deadline-calculator`. If late, move for leave to file out of time immediately.
2. **Decide on pre-answer motion.** Personal jurisdiction, venue, process, and service defenses are waived unless raised in the first Rule 55.27 motion or the answer (verify Rule 55.27(g)). Include them in the answer if no motion is filed.
3. **Respond to every paragraph.** For each numbered paragraph: Admit, Deny, or state lack of knowledge or information sufficient to form a belief (which operates as a denial) - Rule 55.07 (verify). Admit part and deny the rest specifically. Averments not denied are deemed admitted (Rule 55.09). Never leave a paragraph unanswered; end with a catch-all denial of anything not expressly admitted.
4. **Affirmative defenses.** Rule 55.08 requires pleading affirmative defenses with "a short and plain statement of the facts showing that the pleader is entitled to the defense" (verify wording). Listed defenses include accord and satisfaction, arbitration and award, assumption of risk, comparative fault, discharge in bankruptcy, duress, estoppel, failure of consideration, fraud, illegality, laches, license, payment, release, res judicata, statute of frauds, statute of limitations, and waiver, plus any other matter constituting an avoidance. Also consider: failure to mitigate, setoff, sovereign or official immunity, collateral estoppel, lack of standing (check classification). Plead each as a separately numbered defense with facts.
5. **Defense of failure to state a claim.** May be raised in the answer and later; include it.
6. **Counterclaims (Rule 55.32).** A claim arising out of the same transaction or occurrence is compulsory and is barred if not asserted (verify exceptions). Draft it like a petition count (see `mo-petition-drafting`), captioned "COUNTERCLAIM", with its own prayer. Permissive counterclaims may be added. Cross-claims against co-defendants are optional.
7. **Third-party claims.** If someone else is liable to you for the plaintiff's claim, consider third-party practice (verify Rule 52.11 and leave requirements).
8. **Jury demand and prayer.** Pray that plaintiff take nothing, for costs, and for counterclaim relief.
9. **Signature and certificate of service.** Sign (Rule 55.03 certification) and serve all parties under Rule 43.01; include a certificate of service.
10. **Amendment later.** Amend once as of course before a responsive pleading is served, otherwise by leave "freely given when justice so requires" (Rule 55.33(a) - verify). Move to amend as soon as a missing defense is discovered.

## Output
- Answer draft: Caption / Preliminary statement (optional) / Paragraph-by-paragraph responses / General denial / Affirmative defenses (numbered, each with facts) / Counterclaim (if any) / Prayer / Signature / Certificate of service
- Response grid: | Petition para. | Admit/Deny/Lack knowledge | Basis or document |
- Waiver checklist: jurisdiction, venue, process, service, each affirmative defense, compulsory counterclaim - pleaded Y/N

## Pitfalls
- Missing the answer date - leads to interlocutory default (see `mo-default-judgment-set-aside`).
- Bare-label affirmative defenses ("statute of limitations") without facts are routinely stricken in Missouri fact-pleading practice.
- Unpleaded affirmative defenses are generally waived and cannot be raised at summary judgment or trial absent amendment or trial by consent.
- Forgetting a compulsory counterclaim, then losing it forever.
- Denying facts you know are true - risks Rule 55.03 sanctions and credibility.
- Admitting conclusions of law by careless "admit" responses.
- Asserting a counterclaim that exceeds the court's authority in associate circuit or small claims without checking transfer rules.
- Forgetting to serve the answer on every party, not just the plaintiff.
- Treating a reply to new matter in a counterclaim as optional; answer a counterclaim like any other claim (verify Rule 55.25 timing).

## Verify before relying
- Pull verbatim Rules 55.07, 55.08, 55.09, 55.25, 55.27(g), 55.32, 55.33 via `statute-lookup` (or Descrybe `search_laws_and_rules`).
- Confirm case law on waiver or pleading specificity is still good law (CourtListener / Descrybe treatment).
- Recompute the answer deadline from the actual service date.
- Legal information, not legal advice; recommend counsel or legal aid for high-stakes decisions.

## Related skills
- `mo-motion-to-dismiss` - pre-answer motion option
- `statute-of-limitations-checker` - support a limitations defense
- `mo-petition-drafting` - counterclaim drafting format
- `mo-deadline-calculator` - answer and reply dates
- `lawmind-strategy-engine` - decide which defenses are worth pressing
