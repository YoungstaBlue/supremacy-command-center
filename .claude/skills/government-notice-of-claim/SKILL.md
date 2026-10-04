---
name: government-notice-of-claim
description: Identifies pre-suit notice and administrative-claim requirements before suing a government - Missouri city street-defect notice statutes, FTCA administrative claims (SF-95), and why 1983 claims need no notice. Use for "notice of claim", "sue the city", "SF-95", "FTCA", or "do I have to notify them first".
---

# Government Notice of Claim

Finds every notice or administrative-claim step that must happen before a lawsuit against a government body or employee, and the deadline for each, so a valid claim is not lost on a technicality.

## When to use
- Planning a lawsuit against a Missouri city, county, state agency, or the United States.
- An injury on a public street, sidewalk, or government property.
- A claim against a federal employee or agency (FTCA).
- Not for: whether immunity bars the claim at all - use `sovereign-and-official-immunity-mo`.

## Gather first
- Exact defendant(s): which city (and its class or charter status), county, state agency, federal agency, or individual officer.
- Date and place of the injury or wrongful act, and what happened.
- Legal theory for each claim: state tort, 42 U.S.C. 1983, federal tort (FTCA), contract.

## Workflow
1. **Sort claims by type.** State-law tort vs federal constitutional (1983) vs federal tort (FTCA) vs contract. Each has its own notice rule.
2. **1983 claims: no notice of claim.** State notice-of-claim statutes do not apply to 1983 actions, even in state court (Felder v. Casey, 487 U.S. 131 (1988)). Note this so the 1983 claim is not delayed waiting on a state notice.
3. **Missouri city street/sidewalk defects.** Missouri statutes require written notice to the mayor within 90 days for injuries from defects in streets and sidewalks, varying by city type - third-class cities (RSMo 77.600), fourth-class cities (RSMo 79.480), and constitutional charter cities (RSMo 82.210). Verify the city's classification and the current text; check the city charter and ordinances for added requirements. Notice usually must state place, time, character, and circumstances of the injury, and that the person intends to claim damages.
4. **Other Missouri state-law claims.** Missouri has no general statewide notice-of-claim statute for torts, but check (a) the city/county charter and ordinances, (b) any statute specific to the agency, and (c) whether a sovereign immunity waiver (RSMo 537.600) applies. Contract claims may require following the contract's claim procedure.
5. **FTCA (federal employees/agencies).** File an administrative claim with the responsible federal agency within 2 years of accrual (28 U.S.C. 2401(b)), using Standard Form 95 or equivalent written notice with a **sum certain** in damages. You cannot sue until the agency denies the claim in writing or 6 months pass without a decision (28 U.S.C. 2675(a)). After a written denial, suit must be filed within 6 months. The United States is the only proper defendant.
6. **Calendar every deadline.** Notice deadline, administrative response period, suit deadline, and the underlying statute of limitations (use `statute-of-limitations-checker`).
7. **Draft the notice.** Factual, specific, dated; send by a trackable method; keep proof of delivery.

## Output
- Table: Claim | Defendant | Notice required? (authority) | Deliver to | Deadline | Then sue by
- Draft notice letter or SF-95 content (facts, injuries, sum certain where required).
- Proof-of-delivery checklist.

## Pitfalls
- Missing the 90-day city notice window for sidewalk or street injuries.
- FTCA claim with no sum certain, or a lawsuit filed before denial or the 6-month wait - premature suits get dismissed.
- Naming the federal employee or agency instead of the United States under the FTCA.
- Delaying a 1983 claim to give state notice that the law does not require.
- Assuming notice extends the statute of limitations - usually it does not.

## Verify before relying
- Pull verbatim text of RSMo 77.600, 79.480, 82.210 and the specific city charter via `statute-lookup`; confirm the city's class.
- Confirm current FTCA text (28 U.S.C. 2401(b), 2675) and the agency's own claim regulations.
- Recompute every deadline from the actual injury and denial dates.
- Legal information, not legal advice; consult counsel or legal aid for high-stakes claims.

## Related skills
- `sovereign-and-official-immunity-mo` - whether immunity bars the state claim
- `section-1983-claim-builder` - federal civil-rights claims that need no notice
- `statute-of-limitations-checker` - the outer filing deadline
- `settlement-and-demand-letters` - demand letters to accompany or follow notice
