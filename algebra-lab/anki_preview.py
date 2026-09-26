#!/usr/bin/env python3
"""Render every cards_*.json deck to HTML so MathJax output can be checked in a
real browser, and report whether all the maths actually got typeset.

    /usr/bin/python3 anki_preview.py             -> anki_preview.html
    /usr/bin/python3 anki_preview.py --open      -> also launch a browser

Chromium is used headless to dump the DOM, so the script can compare the
number of <mjx-container> elements against the number of delimiters in the
source. A silent MathJax failure (e.g. HTML inside \\( ... \\)) shows up here as
a missing container, which --check alone cannot see.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
MATHJAX_LOCAL = HERE / "mathjax" / "tex-chtml-full.js"
MATHJAX_CDN = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml-full.js"

INLINE = re.compile(r"\\\((.*?)\\\)", re.S)
DISPLAY = re.compile(r"\\\[(.*?)\\\]", re.S)
CHROME = shutil.which("chromium") or shutil.which("chromium-browser") \
    or shutil.which("google-chrome")


def mathjax_src() -> str:
    """Prefer the vendored copy (works offline), fall back to the CDN."""
    if MATHJAX_LOCAL.exists():
        return MATHJAX_LOCAL.as_uri()
    return MATHJAX_CDN


def page(decks: dict[str, list[dict]], title: str) -> str:
    src = mathjax_src()
    out = [
        "<!doctype html><meta charset='utf-8'>",
        f"<title>{html.escape(title)}</title>",
        f"<script src='{src}' id='MathJax-script'></script>",
        "<style>body{font-family:system-ui,sans-serif;max-width:820px;"
        "margin:2rem auto;line-height:1.5}"
        "h2{background:#eee;padding:.3rem .6rem;border-radius:4px}"
        ".c{border-bottom:1px solid #ddd;padding:.5rem 0}"
        ".q{font-weight:600}.a{margin-left:1.2rem}</style><body>",
        f"<h1>{html.escape(title)}</h1>",
    ]
    for deck, cards in decks.items():
        out.append(f"<h2>{html.escape(deck)}</h2>")
        for i, c in enumerate(cards, 1):
            out.append(
                f"<div class='c'><div class='q'>{i}. {c['f']}</div>"
                f"<div class='a'>{c['b']}</div></div>")
    out.append("</body>")
    return "\n".join(out)


def count_math(text: str) -> int:
    return len(INLINE.findall(text)) + len(DISPLAY.findall(text))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(HERE / "anki_preview.html"))
    ap.add_argument("--open", action="store_true")
    args = ap.parse_args()

    files = sorted(HERE.glob("cards_*.json"))
    if not files:
        print("no cards_*.json found", file=sys.stderr)
        return 1

    decks: dict[str, list[dict]] = {}
    for p in files:
        for deck, cards in json.loads(p.read_text()).get("decks", {}).items():
            decks.setdefault(deck, []).extend(cards)

    total = sum(len(c) for c in decks.values())
    expected = sum(count_math(c[k]) for cs in decks.values() for c in cs
                   for k in ("f", "b"))

    out = Path(args.out)
    out.write_text(page(decks, f"Anki decks: {total} cards"))
    local = "local" if MATHJAX_LOCAL.exists() else "CDN"
    print(f"{total} cards, {expected} maths expressions -> {out}  (MathJax: {local})")

    if not CHROME:
        print("chromium not found; skipped the render check")
        return 0

    with tempfile.TemporaryDirectory() as td:
        dom = subprocess.run(
            [CHROME, "--headless", "--no-sandbox", "--disable-gpu",
             "--virtual-time-budget=30000", "--dump-dom", out.as_uri()],
            capture_output=True, text=True, timeout=180).stdout

    got = dom.count("<mjx-container")
    errors = dom.count("<mjx-merror")
    print(f"rendered {got}/{expected} maths expressions, {errors} errors")
    if got < expected or errors:
        print("RENDER CHECK FAILED", file=sys.stderr)
        return 1
    print("render check OK")

    if args.open:
        subprocess.Popen([CHROME, out.as_uri()])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
