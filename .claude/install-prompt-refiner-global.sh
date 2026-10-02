#!/usr/bin/env bash
# Install the prompt-refiner skill + hook into ~/.claude so it runs in EVERY project.
set -euo pipefail

SRC="$(cd "$(dirname "$0")" && pwd)"
DEST="$HOME/.claude"
SETTINGS="$DEST/settings.json"

mkdir -p "$DEST/skills/prompt-refiner" "$DEST/hooks"
cp "$SRC/skills/prompt-refiner/SKILL.md" "$DEST/skills/prompt-refiner/SKILL.md"
cp "$SRC/hooks/prompt-refiner.py" "$DEST/hooks/prompt-refiner.py"
chmod +x "$DEST/hooks/prompt-refiner.py"

# Merge the hook into ~/.claude/settings.json without clobbering existing settings.
python3 - "$SETTINGS" <<'PY'
import json, os, sys
path = sys.argv[1]
cmd = 'python3 "$HOME/.claude/hooks/prompt-refiner.py"'
settings = {}
if os.path.exists(path):
    with open(path) as f:
        settings = json.load(f)
groups = settings.setdefault("hooks", {}).setdefault("UserPromptSubmit", [])
if not any(h.get("command") == cmd for g in groups for h in g.get("hooks", [])):
    groups.append({"hooks": [{"type": "command", "command": cmd}]})
with open(path, "w") as f:
    json.dump(settings, f, indent=2)
    f.write("\n")
PY

echo "prompt-refiner installed globally in $DEST"
echo "Note: inside this repo the project-level hook also fires; that's harmless (same instruction)."
