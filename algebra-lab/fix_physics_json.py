#!/usr/bin/env python3
"""One-off repair of cards_physics_*.json: escape a raw '<' inside math as
'&lt;', exactly as cards_lib.escape_lt does for the generated decks.

These two files predate cards_lib.py, so they have no builder. Run once; after
this they are consistent with the rest.
"""
import json
import pathlib
import re
import sys

LAB = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(LAB))
from cards_lib import escape_lt, norm  # noqa: E402

total = 0
for name in ('cards_physics_a.json', 'cards_physics_b.json'):
    p = LAB / name
    data = json.loads(p.read_text())
    n = 0
    for deck, cards in data['decks'].items():
        for c in cards:
            for k in ('f', 'b'):
                new = escape_lt(norm(c[k]))
                if new != c[k]:
                    c[k] = new
                    n += 1
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"{name}: {n} campo(s) corregidos")
    total += n
print("total:", total)
