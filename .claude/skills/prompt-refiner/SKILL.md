---
name: prompt-refiner
description: Reads, analyzes, and rewrites every user prompt into its most precise, sophisticated form before acting on it — sharpening intent, filling in implied context, and surfacing ambiguity. Runs automatically on each message via the UserPromptSubmit hook in .claude/settings.json; also use it when the user says "refine this prompt", "make this clearer", "what do I actually mean", or "improve my wording".
---

# Prompt Refiner

Every message the user sends goes through this skill before you act on it.
Your job is to read the prompt, work out what the user actually wants, rewrite it
as the best possible instruction for that intent, and then do the work from the
rewritten version.

The aim is **precision, not decoration**. Here "sophisticated" means exact,
unambiguous, and complete. It does not mean longer or more formal. A refined
prompt names the deliverable, the scope, the constraints, and what "done" means.

## When to skip

Pass the prompt through unchanged, with no Refined Intent block, when it is:

- a slash command (`/foo ...`), or starts with `!raw`. Strip the `!raw` and act on the rest verbatim.
- a short conversational reply: "yes", "go ahead", "thanks", "option 2", "stop".
- an answer to a question you just asked.
- already precise. If you can't improve it in a meaningful way, don't pretend to.

## The process

### 1. Read

Take in the literal text, then the surrounding context: the conversation so far,
the current repo and branch (and its CLAUDE.md / AGENTS.md), open files, the
user's known projects and skills (for example, their LawMind / Base44 legal work,
statute archive, or OSINT skills), and anything they said earlier that still applies.

### 2. Analyze

Answer these silently:

| Question | Why it matters |
|---|---|
| **Goal**: what outcome does the user want, beyond the literal words? | The literal ask is often a means to an end. |
| **Deliverable**: what artifact or answer should exist at the end? | Code change, document, answer, plan, PR, filing… |
| **Scope**: which files, repos, cases, or systems? What is out of scope? | Prevents over- and under-reach. |
| **Constraints**: format, length, tone, jurisdiction, deadlines, tools, conventions. | Includes implied ones from context. |
| **Success criteria**: how will we know it is done and correct? | Tests pass, citations verified, filed-ready, etc. |
| **Ambiguities**: where could two reasonable readings lead to different work? | Decide which ones matter. |
| **Unstated assumptions**: what am I assuming that the user didn't say? | Make them visible. |

### 3. Rewrite

Write the refined prompt as a direct, imperative instruction:

- Swap vague verbs ("fix", "handle", "do something with") for specific ones
  ("reproduce, root-cause, and patch", "draft and format for filing").
- Name concrete nouns: file paths, entity names, case numbers, statutes, tools.
- State the deliverable and the done-criteria explicitly.
- Put constraints and exclusions in as short clauses.
- Keep the user's own voice and every requirement they gave. **Never drop,
  soften, or reinterpret a requirement.** Only add precision.
- Never invent facts. If something is unknown, mark it as an assumption or ask.

### 4. Decide: proceed or ask

- If the remaining ambiguities would **not** change the work much, pick the most
  sensible reading, list it under *Assumptions*, and proceed.
- If one ambiguity **would** send the work somewhere materially different
  (wrong repo, wrong case, destructive versus non-destructive, one document versus
  a full bundle), ask **one** focused question before doing the work. Give the
  options and say which one you recommend.

### 5. Show, then act

Start your reply with a compact block, then carry out the refined prompt in the
same turn (unless you had to ask):

```
**Refined intent**
> <the rewritten prompt — 1–4 sentences, imperative, precise>

*Assumptions:* <only if any — one line each>
```

Keep the block short. It exists to confirm intent, not to show off. Then do the
work as you normally would, using the refined prompt as your instruction.

## Examples

**Original:** "fix the login thing"
**Refined intent**
> Reproduce the login failure in this repo's auth flow, find the root cause, patch
> it with the smallest correct change, and confirm it with the repo's own
> lint, typecheck, test, and build checks.
*Assumptions:* "login thing" refers to the auth error discussed earlier in this session.

**Original:** "write a motion for my case"
→ Ask: "Which case, and which motion? For example, a motion to dismiss in the
landlord case versus a motion to compel discovery. These lead to very different
filings. I'd suggest starting with ___ based on your open deadlines."

**Original:** "make the readme better"
**Refined intent**
> Revise `README.md` so a new contributor can set up, run, and use this project
> without outside help. Check every command against the repo, fix inaccuracies,
> add missing env-var notes (no secret values), and keep the existing structure and tone.

**Original:** "thanks!" → skip and reply normally.
