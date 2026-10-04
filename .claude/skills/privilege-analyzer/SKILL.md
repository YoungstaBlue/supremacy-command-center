---
name: privilege-analyzer
description: Analyzes evidentiary privileges and protections - attorney-client, work product, spousal, physician-patient, clergy, and the Fifth Amendment - including waiver and privilege logs. Use for "is this privileged", "work product", "privilege log", "plead the Fifth", or "can my spouse testify".
---

# Privilege Analyzer

Determines whether a communication, document, or testimony is protected, who holds the protection, whether it
was waived, and how to assert or challenge it in Missouri and federal courts.

## When to use
- Responding to discovery or a subpoena that reaches protected material
- Deciding whether to answer deposition or trial questions that could incriminate
- Challenging an opponent's privilege log or privilege assertion
- Not for: hearsay or relevance objections (use `hearsay-analyzer`, `objection-playbook`)

## Gather first
- The communication or document: who, to whom, when, purpose, and who else saw it
- Forum and the claims at issue (federal question vs. state-law claims change which privilege law applies)
- Any pending criminal exposure for the person asked to testify

## Workflow
1. Choose the governing law. Federal court: federal common law of privilege (FRE 501) for federal claims; state
   privilege law for state-law claims and defenses. Missouri court: Missouri statutes and common law.
2. Attorney-client privilege elements: (a) communication; (b) between client and lawyer (or their agents); (c)
   made in confidence; (d) for the purpose of legal advice. Corporate employees can be covered: Upjohn Co. v.
   United States, 449 U.S. 383 (1981). Missouri codifies attorney competency on client communications in
   RSMo 491.060. Pro se note: a self-represented party's notes are not attorney-client communications, but may be work product.
3. Work product: documents and tangible things prepared in anticipation of litigation by or for a party or its
   representative. Hickman v. Taylor, 329 U.S. 495 (1947); FRCP 26(b)(3); Missouri Rule 56.01(b)(3). Ordinary
   work product yields to substantial need and undue hardship; opinion work product (mental impressions, legal
   theories) is nearly absolute.
4. Spousal privileges:
   - Federal: adverse spousal testimony privilege belongs to the witness spouse. Trammel v. United States, 445
     U.S. 40 (1980). Separate marital communications privilege for confidential communications during marriage.
   - Missouri criminal cases: RSMo 546.260 (spouse may not be compelled to testify against the defendant, with
     statutory exceptions, such as certain offenses against children; read the current text).
5. Other Missouri statutory privileges: physician-patient, clergy, and others listed in RSMo 491.060 (read
   current subsections). Federal psychotherapist-patient privilege: Jaffee v. Redmond, 518 U.S. 1 (1996). Placing
   one's own medical condition at issue usually waives the medical privilege for that condition.
6. Fifth Amendment / Mo. Const. art. I, section 19: protects against compelled testimonial self-incrimination
   where there is a real danger of incrimination. Hoffman v. United States, 341 U.S. 479 (1951). Must be asserted
   question by question, not as a blanket refusal. In civil cases the factfinder may draw an adverse inference
   from invocation: Baxter v. Palmigiano, 425 U.S. 308 (1976) (check Missouri case law on adverse inference in state
   civil cases). Immunity must be at least use and derivative-use: Kastigar v. United States, 406 U.S. 441 (1972).
   Does not cover physical evidence or most pre-existing documents' contents.
7. Waiver: voluntary disclosure to third parties; putting advice at issue; failure to assert timely; inadvertent
   production (FRE 502(b) protects if reasonable steps were taken to prevent and promptly rectify; check for a
   502(d) order or clawback agreement).
8. Assertion mechanics: object specifically and serve a privilege log describing each withheld item without
   revealing the protected content (FRCP 26(b)(5)(A); check Missouri Rule 56.01 for the parallel requirement).
   Request in camera review when disputed.

## Output
- Privilege log rows: Bates/ID / Date / Author / Recipients / Type / Subject (non-revealing) / Privilege asserted / Basis
- Analysis table: Item / Privilege / Elements met? / Holder / Waiver risk / Recommendation (withhold, produce, redact, seek protective order)
- For Fifth Amendment: list of questions to answer vs. decline, with the danger-of-incrimination basis

## Pitfalls
- Blanket objections or no privilege log; courts treat that as waiver.
- Copying third parties (friends, family) on communications with a lawyer, destroying confidentiality.
- Testifying in part about a subject, then invoking the Fifth on the rest; partial disclosure can waive.
- Assuming the privilege covers underlying facts; only the communication is protected.
- Ignoring the civil adverse inference before invoking the Fifth in a civil deposition.

## Verify before relying
- Pull verbatim RSMo 491.060, 546.260, FRE 501-502, FRCP 26(b)(3) and (5), and Missouri Rule 56.01 via `statute-lookup`.
- Confirm Missouri treatment of each privilege and any exceptions with current case law on CourtListener.
- Where criminal exposure exists, recommend consulting a criminal defense lawyer before testifying.
- Legal information, not legal advice.

## Related skills
- `mo-discovery-requests` and `federal-civil-discovery` — objections and logs in discovery
- `miranda-and-confessions` — custodial statements and self-incrimination
- `sixth-amendment-counsel-confrontation` — right to counsel
- `objection-playbook` — asserting privilege at trial
