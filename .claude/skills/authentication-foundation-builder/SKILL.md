---
name: authentication-foundation-builder
description: Builds foundation question scripts to authenticate exhibits - documents, text messages, emails, photos, video, audio, social media, business records - under FRE 901-902 and Missouri common law. Use for "lay a foundation", "authenticate these texts", "get this video admitted", or self-authenticating records.
---

# Authentication and Foundation Builder

Produces the foundation needed to get an exhibit admitted: who can authenticate it, what they must say, and
which self-authentication or certification route avoids live testimony.

## When to use
- Getting screenshots, texts, emails, social media posts, recordings, body-cam or surveillance video admitted
- Preparing a business-records affidavit or certification
- Anticipating an authentication objection from the other side
- Not for: whether the content is hearsay (use `hearsay-analyzer`); numbering and binders (use `exhibit-list-and-trial-binder`)

## Gather first
- The exhibit, how it was obtained, who created it, and who has personal knowledge of it
- Original vs. copy; metadata, chain of custody, or platform records available
- Forum (federal or Missouri) and the hearing/trial date (affidavit notice periods run from it)

## Workflow
1. Standard: the proponent must produce evidence sufficient to support a finding that the item is what it is
   claimed to be (FRE 901(a)). This is a low threshold; weight disputes go to the factfinder. Missouri applies a
   similar common-law standard.
2. Choose the route:
   - Witness with knowledge (901(b)(1)): the author, recipient, or someone who saw it made.
   - Distinctive characteristics (901(b)(4)): content, nicknames, facts only the sender would know, replies in
     the thread, phone number or account linked to the person.
   - Voice identification (901(b)(5)); telephone conversations (901(b)(6)).
   - Process or system (901(b)(9)): reliable process producing an accurate result (surveillance systems, logs).
   - Self-authenticating (FRE 902): certified public records (902(4)), official publications (902(5)), certified
     business records (902(11)), certified electronic records from a system/process (902(13)) and data copied
     from a device by hash verification (902(14)). 902(11), (13), and (14) require advance written notice.
   - Missouri business records: RSMo 490.680 foundation by the custodian or other qualified witness, or affidavit
     under RSMo 490.692 served on all parties in advance of trial (confirm the current notice period).
3. Foundation scripts by type (ask open questions; witness must have personal knowledge):
   - Text messages: Do you recognize Exhibit __? What is it? Whose number sent these? How do you know that
     number belongs to them? Did you receive these on your phone? Is this screenshot a fair and accurate copy of
     what appeared on your phone? Has it been altered? Content showing identity (references, replies)?
   - Email: same pattern plus address, prior correspondence from that address, reply chain, signature block.
   - Social media: account name/photo, prior interactions, content only the person would know, admission by the
     user, or platform records. Expect a stronger showing because accounts can be faked.
   - Photo or video: Are you familiar with the scene/events shown? Does this fairly and accurately depict it as
     it was on [date]? (Pictorial testimony.) If no eyewitness, use the "silent witness" route: system
     description, operation, retrieval, chain of custody, no editing.
   - Audio recording: identify voices; recording device worked; no alteration; complete or explain gaps. Note
     Missouri is a one-party-consent state for recording conversations (verify RSMo 542.402 before relying).
   - Physical evidence: readily identifiable item, or chain of custody for fungible items (drugs, samples).
4. Best evidence (FRE 1001-1008; Missouri common law): if proving the contents of a writing, recording, or photo,
   use the original or an admissible duplicate unless an exception applies.
5. Pair each exhibit with its hearsay route and relevance purpose.

## Output
- Per exhibit: Exhibit no. / Description / Claimed identity / Authenticating witness or 902 route / Foundation
  questions (numbered) / Notice or affidavit deadline / Best-evidence note / Hearsay route / Anticipated objection and response

## Pitfalls
- Offering a screenshot through someone who never saw the original on the device.
- Missing the advance-notice requirement for 902(11)/(13)/(14) certifications or the 490.692 affidavit.
- Assuming a printout of a social media page proves who wrote it; authorship needs more.
- Edited or clipped video without explaining the edits.
- Asking leading foundation questions on direct; expect sustained objections.

## Verify before relying
- Pull current text of FRE 901, 902, 1001-1008 and RSMo 490.680, 490.692, 542.402 via `statute-lookup`.
- Check local rules and scheduling orders for exhibit exchange and objection deadlines.
- Recompute affidavit/notice deadlines from the actual trial setting.
- Legal information, not legal advice.

## Related skills
- `hearsay-analyzer` — admissibility of the content
- `exhibit-list-and-trial-binder` — organizing and pre-marking exhibits
- `witness-examination-planner` — fitting foundation into direct exam
- `objection-playbook` — responding to authentication objections
- `mo-evidence-rules` — Missouri source map
