#!/usr/bin/env python3
"""Shared helpers for the build_cards_*.py generators.

Why this exists: in a Python raw string r"\\(" yields TWO backslashes, but
LaTeX needs one. Mixing r"..." and "..." fragments for the same card silently
produced doubled backslashes in the JSON, which MathJax does not recognise as
a delimiter -- the maths then renders as literal text with no error anywhere.

norm() collapses doubled backslashes, keeping the ones that are genuine row
separators inside matrix/aligned environments.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

# environments where "\\" is a row separator and must survive
ROW_ENVS = ("pmatrix", "bmatrix", "matrix", "smallmatrix", "psmallmatrix",
            "vmatrix", "Vmatrix", "Bmatrix", "array", "aligned", "alignedat",
            "cases", "split", "gathered")

ROW_ENV_SPAN = re.compile(
    r"\\begin\{(" + "|".join(ROW_ENVS) + r")\}.*?\\end\{\1\}", re.S)
INLINE_SPAN = re.compile(r"\\\((.*?)\\\)", re.S)
DISPLAY_SPAN = re.compile(r"\\\[(.*?)\\\]", re.S)
RAW_LT = re.compile(r"<(?![/!a-zA-Z])")
ANY_LT = re.compile(r"<")


def escape_lt(text: str) -> str:
    r"""Escape a raw '<' inside math as the HTML entity '&lt;'.

    Anki fields are HTML, so a bare '<' is seen by the HTML parser before
    MathJax ever runs. '< R' survives because a space cannot start a tag name,
    but '0<x<L' is parsed as a tag and silently destroys the formula. The
    entity is decoded to '<' in the text node, so MathJax still typesets an
    inequality correctly.
    """
    def fix(m: re.Match) -> str:
        body = m.group(1)
        if "<" not in body:
            return m.group(0)
        # inside math there are no HTML tags, so escape every '<' -- including
        # '0<x<L', where the letter after '<' is what makes it look like a tag
        return m.group(0).replace(body, ANY_LT.sub("&lt;", body))
    return DISPLAY_SPAN.sub(fix, INLINE_SPAN.sub(fix, text))


def norm(text: str) -> str:
    """Collapse doubled backslashes outside row-separator environments."""
    if "\\\\" not in text:
        return text

    # A doubled backslash in front of a control word is always a bug, and
    # would otherwise be protected by the row-separator span below.
    text = re.sub(r"\\\\(begin|end)\{", r"\\\1{", text)

    spans = [(m.start(), m.end()) for m in ROW_ENV_SPAN.finditer(text)]
    out = []
    i = 0
    while i < len(text):
        if text.startswith("\\\\", i):
            inside = any(s <= i < e for s, e in spans)
            out.append("\\\\" if inside else "\\")
            i += 2
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def write_json(stem: str, decks: dict[str, list[dict]]) -> Path:
    """Normalise every field, write <stem>.json, and print a summary."""
    here = Path(__file__).resolve().parent
    for cards in decks.values():
        for c in cards:
            c["f"] = escape_lt(norm(c["f"]))
            c["b"] = escape_lt(norm(c["b"]))
    out = here / f"{stem}.json"
    out.write_text(json.dumps({"decks": decks}, indent=2, ensure_ascii=False))
    total = sum(len(v) for v in decks.values())
    print(f"{out.name}: {len(decks)} decks, {total} cards")
    for k, v in decks.items():
        print(f"  {len(v):4}  {k}")
    return out
