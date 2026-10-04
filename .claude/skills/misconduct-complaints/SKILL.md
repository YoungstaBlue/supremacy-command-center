---
name: misconduct-complaints
description: Drafts factual, rule-based misconduct complaints against judges (Missouri CRRD, federal 28 U.S.C. 351), attorneys and prosecutors (Missouri OCDC), and police (internal affairs, POST licensing, DOJ). Use for "file a bar complaint", "complain about the judge", "report the officer", or "prosecutor misconduct".
---

# Misconduct Complaints

Routes a grievance to the body that can actually act on it and drafts a complaint built on dated facts and specific rule violations, not adjectives — while keeping it separate from the remedies available in the case itself.

## When to use
- A judge's conduct (bias, ex parte contacts, demeanor, delay, conflicts) rather than a ruling the user disagrees with
- An attorney or prosecutor lied to the court, withheld evidence, mishandled funds, or communicated improperly
- A police officer used force, falsified a report, or violated department policy
- Not for: reversing a ruling (use `mo-appeals-procedure` or `writs-mandamus-prohibition`); recusing a judge in a pending case (use `mo-change-of-judge-venue`); suing for damages (use `section-1983-claim-builder`)

## Gather first
- Who (name, role, agency/court), what happened, and exact dates, with document or transcript cites
- What outcome is wanted (discipline, investigation, policy change) and whether a related case is pending
- Any prior complaints and their outcomes

## Workflow
1. **Separate merits from misconduct.** Disciplinary bodies do not review the correctness of rulings. A federal judicial complaint "directly related to the merits of a decision or procedural ruling" is dismissed (28 U.S.C. 352(b)). Strip legal-error arguments out; keep conduct.
2. **Pick the forum.**
   | Target | Body | Governing rules |
   |---|---|---|
   | Missouri state judge | Commission on Retirement, Removal and Discipline (CRRD) | Supreme Court Rule 12; Code of Judicial Conduct, Rule 2 |
   | Missouri attorney or prosecutor | Office of Chief Disciplinary Counsel (OCDC) | Rule 5 (discipline); Rules of Professional Conduct, Rule 4 |
   | Federal judge | Circuit clerk (8th Cir. for E.D./W.D. Mo.) | Judicial Conduct and Disability Act, 28 U.S.C. 351-364, and the circuit's rules |
   | Federal prosecutor | DOJ Office of Professional Responsibility (and OCDC for the license) | Agency policy; Rule 4 |
   | Local police officer | Department internal affairs / civilian review board; Missouri POST (license discipline under RSMo ch. 590) | Department policy; RSMo 590.080 (verify) |
   | Pattern of civil-rights violations | U.S. DOJ Civil Rights Division; FBI for color-of-law crimes | 34 U.S.C. 12601; 18 U.S.C. 242 |
3. **Identify the rule violated.** Quote the specific rule: e.g., Rule 2 canons on impartiality, ex parte communications, disqualification; Rule 4-3.3 (candor to tribunal), 4-3.4 (fairness to opposing party), 4-3.8 (special responsibilities of a prosecutor, including timely disclosure of exculpatory evidence), 4-8.4 (dishonesty, conduct prejudicial to the administration of justice). Pull the current text before quoting.
4. **Build the fact section.** Numbered, dated, first-person paragraphs; each fact tied to an exhibit (transcript page, docket entry, email, video timestamp). No speculation about motive; state what was said/done and where it is documented.
5. **Draft.** Use the body's official form if one exists (OCDC, CRRD, and the 8th Circuit publish forms). Attach only copies; keep originals. Include a short statement of the rule violated per incident.
6. **Calibrate expectations.** Proceedings are typically confidential until formal charges; complainants are usually not parties and have no appeal of a dismissal (verify each body's rules). A complaint does not stay or change the underlying case, and it does not toll any deadline.
7. **Strategic check before sending.** Consider whether filing against a sitting judge or opposing counsel mid-case helps or creates distraction; consider whether a motion (recusal, sanctions, Brady motion) is the faster remedy. The user decides and submits.

## Output
- Forum memo: target, body, rule(s), what the body can and cannot do
- Complaint draft: identifying information; background (one paragraph); numbered dated facts with exhibit cites; rules violated per incident; relief requested; verification/signature block as the form requires
- Exhibit index

## Pitfalls
- Rearguing the case; dismissal for being merits-related
- Sending to the wrong body (e.g., OCDC for a judge, CRRD for a prosecutor) and assuming it will be forwarded
- Inflammatory language, conclusions without facts, or accusations not supported by exhibits
- Filing instead of the in-case remedy (recusal, appeal, sanctions) and missing that deadline
- Publicly posting the complaint or confidential proceedings; possible defamation exposure for statements outside the privileged complaint process
- Assuming a complaint creates a damages claim or reopens a judgment

## Verify before relying
- Pull current text of Rules 2, 4, 5, 12, RSMo ch. 590, and 28 U.S.C. 351-364 via `statute-lookup` (or Descrybe `search_laws_and_rules`); download the body's current complaint form.
- Confirm any filing window in the body's rules (some police departments have short complaint windows).
- Legal information, not legal advice.

## Related skills
- `mo-change-of-judge-venue` — in-case remedy for judicial bias
- `brady-giglio-demands` — in-case remedy for withheld evidence
- `sunshine-and-foia-requests` — obtain police records and bodycam to support a complaint
- `section-1983-claim-builder` — damages claims for constitutional violations
