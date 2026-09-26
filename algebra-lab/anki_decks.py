#!/usr/bin/env python3
"""Load topic decks from JSON card files into Anki.

Cards live in JSON so there is no chance of a broken string concatenation
silently corrupting a formula -- the thing that bit us before.

File format:

    {
      "decks": {
        "Physics::Mechanics::Newton": [
          {"t": "q::what q::newton::laws", "f": "front", "b": "back"},
          ...
        ]
      }
    }

Deck names are Anki hierarchical decks, separated by "::".

Math uses Anki's built-in MathJax: \\( ... \\) inline, \\[ ... \\] display.
The editor shortcut is Ctrl+M.

Usage:
    anki_decks.py --load            # sync every cards_*.json
    anki_decks.py --check           # validate only, touch no collection
    anki_decks.py --stats           # per-deck card counts
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODEL = "Basic"


def find_collection() -> Path:
    """Locate this machine's Anki collection.

    Order: $ANKI_COLLECTION, then the only profile under
    ~/.local/share/Anki2/, then a lone 'User 1'. Never hardcodes a profile
    name, because the profile is called 'User 2' for anyone who made a second
    one and something else entirely on macOS and Windows.
    """
    env = os.environ.get("ANKI_COLLECTION")
    if env:
        return Path(env).expanduser()

    root = Path.home() / ".local/share/Anki2"
    found = sorted(root.glob("*/collection.anki2")) if root.is_dir() else []
    if not found:
        # Anki 25+ on some platforms keeps it elsewhere; look in the profile dir
        found = sorted((Path.home() / ".config/anki").glob("*/collection.anki2"))
    if len(found) == 1:
        return found[0]
    if not found:
        return root / "User 1" / "collection.anki2"   # for the error message
    names = "\n  ".join(str(p) for p in found)
    sys.exit(f"several Anki collections found; set ANKI_COLLECTION:\n  {names}")


COLLECTION = find_collection()

INLINE = re.compile(r"\\\((.*?)\\\)", re.S)
DISPLAY = re.compile(r"\\\[(.*?)\\\]", re.S)
ENV = ("\\begin{aligned}", "\\begin{cases}", "\\begin{bmatrix}",
       "\\begin{array}", "\\begin{vmatrix}", "\\begin{pmatrix}",
       "\\begin{matrix}", "\\begin{vmatrix}", "\\begin{Bmatrix}",
       "\\begin{smallmatrix}", "\\begin{psmallmatrix}", "\\text")
HTML_TAG = re.compile(r"<\s*/?\s*(?:b|i|em|strong|br|sup|sub|u|small|code|span|div|p)\b", re.I)
# a raw '<' that does not open a real tag/entity, e.g. "<(c)>"
BAD_LT = re.compile(r"<(?![/!a-zA-Z])")
# environments where a doubled backslash is a legitimate row separator
ROW_ENVS = ("pmatrix", "bmatrix", "matrix", "smallmatrix", "psmallmatrix",
            "vmatrix", "Vmatrix", "Bmatrix", "array", "aligned", "alignedat",
            "cases", "split", "gathered")
ROW_SPAN = re.compile(
    r"\\begin\{(" + "|".join(ROW_ENVS) + r")\}.*?\\end\{\1\}", re.S)


def stray_double_backslash(field: str) -> bool:
    """True if '\\\\' appears anywhere except as a matrix row separator.

    Doubled backslashes are the classic r"\\\\(" bug: MathJax then does not see
    the delimiter and renders the maths as literal text, with no error.
    A row separator needs exactly two; four is always a bug.
    """
    if "\\\\\\\\" in field:
        return True
    spans = [(m.start(), m.end()) for m in ROW_SPAN.finditer(field)]
    for m in re.finditer(r"\\\\", field):
        if not any(s <= m.start() < e for s, e in spans):
            return True
    return False


# ---------------------------------------------------------------- loading

def card_files() -> list[Path]:
    return sorted(HERE.glob("cards_*.json"))


def read_cards() -> dict[str, list[dict]]:
    decks: dict[str, list[dict]] = {}
    problems: list[str] = []

    for path in card_files():
        try:
            data = json.loads(path.read_text())
        except json.JSONDecodeError as exc:
            problems.append(f"{path.name}: invalid JSON -- {exc}")
            continue
        for deck, cards in data.get("decks", {}).items():
            bucket = decks.setdefault(deck, [])
            for i, c in enumerate(cards):
                for key in ("t", "f", "b"):
                    if key not in c or not str(c[key]).strip():
                        problems.append(f"{path.name} {deck}[{i}]: missing '{key}'")
                bucket.append(c)

    if problems:
        for p in problems:
            print("  ERROR", p, file=sys.stderr)
        raise SystemExit(1)
    return decks


# ---------------------------------------------------------------- checking

def check(decks: dict[str, list[dict]]) -> int:
    bad = 0
    total = 0
    seen: dict[str, str] = {}

    for deck, cards in sorted(decks.items()):
        if "::" not in deck:
            print(f"  WARN  deck {deck!r} is not hierarchical")
        for c in cards:
            total += 1
            f, b, t = c["f"], c["b"], c["t"]
            for field, name in ((f, "front"), (b, "back")):
                if field.count("\\(") != field.count("\\)"):
                    print(f"  BAD   {deck} / {name}: unbalanced ( ) -- {f[:50]!r}"); bad += 1
                if field.count("\\[") != field.count("\\]"):
                    print(f"  BAD   {deck} / {name}: unbalanced [ ] -- {f[:50]!r}"); bad += 1
                if field.count("{") != field.count("}"):
                    print(f"  BAD   {deck} / {name}: unbalanced braces -- {f[:50]!r}"); bad += 1
                if field.count("\\begin{aligned}") != field.count("\\end{aligned}"):
                    print(f"  BAD   {deck} / {name}: aligned -- {f[:50]!r}"); bad += 1
                for env in ("cases", "bmatrix", "array", "vmatrix"):
                    if field.count(f"\\begin{{{env}}}") != field.count(f"\\end{{{env}}}"):
                        print(f"  BAD   {deck} / {name}: {env} -- {f[:50]!r}"); bad += 1
                if "&" in field and not any(e in field for e in ENV):
                    # ignore HTML entities (&rarr; &mdash; &nbsp; ...)
                    stripped = re.sub(r"&(?:#\d+|#x[0-9a-fA-F]+|[a-zA-Z]+);", "", field)
                    if "&" in stripped:
                        print(f"  BAD   {deck} / {name}: bare & -- {f[:50]!r}"); bad += 1
                # HTML inside math silently fails to render in MathJax (and in
                # Anki's reviewer), so reject it: keep tags outside \( \).
                # A raw '<' that does not open a real tag. This includes math:
                # Anki fields are HTML, so '0<x<L' is parsed as a tag and the
                # formula is destroyed. Use &lt; inside math.
                if BAD_LT.search(field):
                    print(f"  BAD   {deck} / {name}: raw '<' (use &lt;) -- {f[:50]!r}"); bad += 1
                # Inside math any raw '<' is wrong: LaTeX has no HTML tags, and
                # '0<x<L' is parsed as a tag by the HTML parser before MathJax.
                for rx in (INLINE, DISPLAY):
                    if any("<" in m.group(1) for m in rx.finditer(field)):
                        print(f"  BAD   {deck} / {name}: raw '<' inside math (use &lt;) -- {f[:50]!r}")
                        bad += 1
                        break
                if stray_double_backslash(field):
                    print(f"  BAD   {deck} / {name}: doubled backslash -- {f[:50]!r}"); bad += 1
                for m in INLINE.finditer(field):
                    if HTML_TAG.search(m.group(1)):
                        print(f"  BAD   {deck} / {name}: HTML inside math -- {f[:50]!r}"); bad += 1
                for m in DISPLAY.finditer(field):
                    if HTML_TAG.search(m.group(1)):
                        print(f"  BAD   {deck} / {name}: HTML inside display math -- {f[:50]!r}"); bad += 1
            if f in seen:
                print(f"  DUP   front repeated in {deck} and {seen[f]} -- {f[:50]!r}"); bad += 1
            else:
                seen[f] = deck
            if len(t.split()) != len(set(t.split())):
                print(f"  BAD   {deck}: repeated tag -- {t!r}"); bad += 1

    print(f"\n  {len(decks)} decks, {total} cards, {bad} problems")
    return 0 if bad == 0 else 1


# ---------------------------------------------------------------- syncing

def sync(decks: dict[str, list[dict]]) -> int:
    # Anki's Collection() CREATES the file if it is missing, so a typo in
    # ANKI_COLLECTION would silently start a fresh empty collection instead of
    # reporting the problem. Refuse to touch anything that is not there already.
    if not COLLECTION.is_file():
        print(f"error: no Anki collection at {COLLECTION}", file=sys.stderr)
        print("  set ANKI_COLLECTION=/path/to/User\\ 1/collection.anki2",
              file=sys.stderr)
        return 1

    from anki.collection import Collection

    col = Collection(str(COLLECTION))
    try:
        model = col.models.by_name(MODEL)
        if model is None:
            print(f"error: no {MODEL!r} note type", file=sys.stderr)
            return 1

        grand_add = grand_upd = 0
        for deck, cards in sorted(decks.items()):
            did = col.decks.id(deck)
            existing: dict[str, int] = {}
            for nid in col.find_notes(f'"deck:{deck}"'):
                existing.setdefault(col.get_note(nid)["Front"], nid)

            added = updated = 0
            for c in cards:
                if c["f"] in existing:
                    old = col.get_note(existing[c["f"]])
                    if old["Back"] != c["b"] or set(old.tags) != set(c["t"].split()):
                        old["Back"] = c["b"]
                        old.tags = c["t"].split()
                        col.update_note(old)
                        updated += 1
                    continue
                note = col.new_note(model)
                note["Front"] = c["f"]
                note["Back"] = c["b"]
                note.tags = c["t"].split()
                col.add_note(note, did)
                existing[c["f"]] = 1
                added += 1

            total = col.decks.card_count(did, include_subdecks=True)
            print(f"  {added:4} new {updated:4} upd   {total:4} cards   {deck}")
            grand_add += added
            grand_upd += updated

        print(f"\n  total: {grand_add} new, {grand_upd} updated")
        return 0
    finally:
        col.close()


# ---------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--load", action="store_true", help="sync into Anki")
    ap.add_argument("--check", action="store_true", help="validate only")
    ap.add_argument("--stats", action="store_true", help="per-deck counts")
    args = ap.parse_args()

    decks = read_cards()
    if not decks:
        print("no cards_*.json found", file=sys.stderr)
        return 1

    if args.stats:
        for deck, cards in sorted(decks.items()):
            print(f"  {len(cards):4}  {deck}")
        print(f"  {sum(len(c) for c in decks.values()):4}  TOTAL")
        return 0

    rc = check(decks)
    if rc and not args.load:
        return rc
    if args.load:
        if rc:
            print("\nrefusing to load while there are problems", file=sys.stderr)
            return rc
        return sync(decks)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
