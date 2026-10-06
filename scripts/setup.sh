#!/usr/bin/env bash
# SessionStart hook and local bootstrap for this repository.
#
# Runs at the start of every Claude Code session (see .claude/settings.json) so
# a fresh container is ready without prompting: it confirms the tool chain the
# reference-sync pipeline needs, installs the three Python packages it depends
# on when they are missing, and checks the reference library against its
# manifest. It never touches the network when nothing is missing, and it never
# fails the session: problems are printed as warnings for Claude to act on.
set -u

cd "$(dirname "$0")/.." || exit 0

warn() { printf 'setup: %s\n' "$*" >&2; }

# --- tool chain -------------------------------------------------------------
if ! command -v python3 >/dev/null 2>&1; then
  warn "python3 is not installed; scripts/reference-sync/build.py needs it"
fi
if ! command -v node >/dev/null 2>&1; then
  warn "node is not installed; scripts/reference-sync/extract_js.mjs needs Node 18+"
fi

# --- python deps for build.py (bs4 + markdownify + lxml) -------------------
if command -v python3 >/dev/null 2>&1; then
  missing=$(python3 - <<'EOF'
import importlib.util
mods = {"bs4": "beautifulsoup4", "markdownify": "markdownify", "lxml": "lxml"}
print(" ".join(pkg for mod, pkg in mods.items() if importlib.util.find_spec(mod) is None))
EOF
)
  if [ -n "${missing}" ]; then
    warn "installing python packages: ${missing}"
    python3 -m pip install --quiet --disable-pip-version-check ${missing} \
      || warn "pip install failed; run: python3 -m pip install ${missing}"
  fi
fi

# --- reference library integrity -------------------------------------------
if [ -f reference/manifest.json ] && command -v python3 >/dev/null 2>&1; then
  if ! python3 scripts/reference-sync/build.py --verify >/tmp/reference-verify.log 2>&1; then
    warn "reference/ does not match reference/manifest.json (see /tmp/reference-verify.log); rebuild with build.py"
  else
    tail -n 1 /tmp/reference-verify.log | sed 's/^/setup: reference library ok: /'
  fi
fi

exit 0
