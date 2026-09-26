#!/usr/bin/env bash
#
# One-shot installer. Safe to re-run: it merges rather than overwrites the
# Omarchy menu, and every step is guarded.
#
#   ./install.sh              install menu + launchers
#   ./install.sh --decks      also import the 511 Anki cards (asks first)
#   ./install.sh --check      print what would happen, change nothing
#
# Override the target with LAB_DIR=/path/to/anki-lab ./install.sh

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LAB_DIR="${LAB_DIR:-$REPO}"
BIN="${BIN:-$HOME/.local/bin}"
MENU_SRC="$REPO/setup/omarchy-menu.jsonc"
MENU_DST="$HOME/.config/omarchy/extensions/omarchy-menu.jsonc"
JUP_SRC="$REPO/setup/jupyter_server_config.py"
JUP_DST="$HOME/.jupyter/jupyter_server_config.py"

DRY=0
IMPORT=0
for arg in "$@"; do
  case "$arg" in
    --check) DRY=1 ;;
    --decks) IMPORT=1 ;;
    -h|--help) sed -n '3,10p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown option: $arg" >&2; exit 2 ;;
  esac
done

say()  { printf '  %s\n' "$*"; }
head() { printf '\n%s\n' "$*"; }
run()  { if (( DRY )); then say "would run: $*"; else "$@"; fi; }

printf 'repo   : %s\n' "$REPO"
printf 'lab    : %s/algebra-lab\n' "$LAB_DIR"
printf 'mode   : %s\n' "$( ((DRY)) && echo 'dry run (--check)' || echo 'install' )"

# ---------------------------------------------------------------- dependencies
head "1/5  dependencies"
if (( DRY )); then
  say "would check: python3, anki, omarchy-launch-*"
else
  command -v python3 >/dev/null || { echo "python3 not found" >&2; exit 1; }
  say "python3: $(python3 --version 2>&1)"
  for pkg in sympy jupyterlab; do
    python3 -c "import $pkg" 2>/dev/null && say "$pkg: ok" \
      || say "$pkg: MISSING -- omarchy install app 'Math Lab' 'jupyter-notebook python-sympy python-numpy python-matplotlib'"
  done
  command -v anki >/dev/null && say "anki: ok" || say "anki: MISSING -- pacman -S anki"
  command -v omarchy >/dev/null && say "omarchy: ok" || say "omarchy: not installed (menu step will be skipped)"
fi

# ---------------------------------------------------------------- launchers
head "2/5  launchers -> $BIN"
if (( DRY )); then
  ls "$REPO/setup/launchers" | sed 's/^/  would install: /'
else
  mkdir -p "$BIN"
  for f in "$REPO"/setup/launchers/*; do
    install -m 0755 "$f" "$BIN/$(basename "$f")"
    say "installed $(basename "$f")"
  done
fi

# ---------------------------------------------------------------- omarchy menu
head "3/5  omarchy menu -> $MENU_DST"
if (( DRY )); then
  say "would merge the \"math\" subtree from setup/omarchy-menu.jsonc"
elif ! command -v omarchy >/dev/null; then
  say "skipped: omarchy not on PATH"
elif [[ -f $MENU_DST ]] && grep -q '"math"' "$MENU_DST"; then
  say "menu already has a \"math\" key -- leaving it alone."
  say "to update manually, merge the block from setup/omarchy-menu.jsonc"
  say "backup of the current file: ${MENU_DST}.bak.$(date +%s)"
  cp "$MENU_DST" "${MENU_DST}.bak.$(date +%s)"
else
  mkdir -p "$(dirname "$MENU_DST")"
  # Strip the comment header: a fresh file has no surrounding braces to merge into.
  sed -e '1,/^$/d' "$MENU_SRC" > "$MENU_DST"
  say "wrote a fresh $MENU_DST (none existed)"
  say "if you already have an omarchy-menu.jsonc, merge the block by hand"
fi

# ---------------------------------------------------------------- jupyter
head "4/5  jupyter config -> $JUP_DST"
if (( DRY )); then
  say "would write $JUP_DST pointing at $LAB_DIR/algebra-lab"
else
  mkdir -p "$(dirname "$JUP_DST")"
  if [[ -f $JUP_DST ]]; then
    cp "$JUP_DST" "$JUP_DST.bak.$(date +%s)"
    say "back up the existing config"
  fi
  sed "s|~/Work/anki-lab|$LAB_DIR|g" "$JUP_SRC" > "$JUP_DST"
  say "wrote $JUP_DST (root_dir = $LAB_DIR/algebra-lab)"
  say "token left empty on purpose: the server only listens on 127.0.0.1"
fi

# ---------------------------------------------------------------- decks
head "5/5  anki decks"
if (( ! IMPORT )); then
  say "skipped (pass --decks to import)"
elif (( DRY )); then
  say "would run: $LAB_DIR/algebra-lab/anki_decks.py --check"
else
  say "validating first..."
  ( cd "$LAB_DIR/algebra-lab" && python3 anki_decks.py --check ) || {
    echo "validation failed -- not importing" >&2; exit 1; }
  if pgrep -x anki >/dev/null 2>&1; then
    echo "Anki is running and holds the collection lock." >&2
    echo "Quit Anki, then re-run: $0 --decks" >&2
    exit 1
  fi
  read -r -p "Import the 511 cards into your Anki collection? [y/N] " a
  case "$a" in
    [yY]*) ( cd "$LAB_DIR/algebra-lab" && python3 anki_decks.py --load ) ;;
    *) say "cancelled" ;;
  esac
fi

head "done"
say "open the menu with: omarchy menu summon math"
say "or run the drills directly: $LAB_DIR/algebra-lab/run.sh"
