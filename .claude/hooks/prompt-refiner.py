#!/usr/bin/env python3
"""UserPromptSubmit hook: route every substantive prompt through the prompt-refiner skill.

Claude Code pipes the hook event as JSON on stdin; any JSON we print with
hookSpecificOutput.additionalContext is injected alongside the user's prompt.
"""
import json
import re
import sys

SKIP_REPLIES = {
    "y", "yes", "yep", "yeah", "no", "nope", "ok", "okay", "k", "sure",
    "thanks", "thank you", "thx", "ty", "go", "go ahead", "continue",
    "proceed", "do it", "stop", "cancel", "done", "lgtm",
}


def should_skip(prompt: str) -> bool:
    p = prompt.strip()
    if not p:
        return True
    if p.startswith("/") or p.lower().startswith("!raw"):
        return True
    normalized = re.sub(r"[^\w\s]", "", p.lower()).strip()
    if normalized in SKIP_REPLIES:
        return True
    # Bare option picks like "2", "option b", "a".
    if re.fullmatch(r"(option\s+)?[a-d1-9]", normalized):
        return True
    return False


def main() -> None:
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return
    prompt = event.get("prompt", "")
    if should_skip(prompt):
        return
    context = (
        "PROMPT-REFINER: Before acting on this message, apply the `prompt-refiner` skill "
        "(.claude/skills/prompt-refiner/SKILL.md; load it via the Skill tool if not already loaded). "
        "Read and analyze the prompt for goal, deliverable, scope, constraints, success criteria and "
        "ambiguities; rewrite it as a precise imperative instruction without dropping or inventing any "
        "requirement; open your reply with a short 'Refined intent' block (plus assumptions, if any); "
        "then carry out the refined prompt. Ask one focused question first only if an ambiguity would "
        "materially change the work. Skip the block if the prompt is already precise."
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": context,
        }
    }))


if __name__ == "__main__":
    main()
