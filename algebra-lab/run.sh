#!/usr/bin/env bash
# Launcher for the algebra lab. Prefers the local venv (works with no install),
# falls back to the system python (needs the pacman packages).
set -euo pipefail
cd "$(dirname "$0")"

# Prefer the system python (installed via pacman/omarchy); fall back to the
# bundled venv, which works on its own without any install.
pick_python() {
  for cand in "$(command -v python3)" .venv/bin/python; do
    [[ -x $cand ]] || continue
    if "$cand" -c 'import sympy' 2>/dev/null; then
      printf '%s' "$cand"
      return 0
    fi
  done
  return 1
}

if ! PY=$(pick_python); then
  cat >&2 <<'EOF'
error: sympy not found in any python.

install it with:
  omarchy install app 'Math Lab' 'jupyter-notebook python-sympy python-numpy python-matplotlib maxima geogebra anki'
EOF
  exit 1
fi

case "${1:-notebook}" in
  notebook|nb)
    exec "$PY" -m jupyter lab --notebook-dir=. "$@"
    ;;
  test)
    shift
    exec "$PY" algebra_lab.py random -n 5 "$@"
    ;;
  *)
    exec "$PY" algebra_lab.py "$@"
    ;;
esac
