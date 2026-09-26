#!/usr/bin/env python3
"""Set the new-cards-per-day limit on the Anki decks in this repo.

Anki ships with 20 new cards/day. These decks are factual recall (definitions,
identities, comparisons), which tolerates a much higher rate than prose, but
the default means only 20 of the 511 cards ever show up.

    python3 set_anki_limits.py                # 60 new/day on every deck here
    python3 set_anki_limits.py --new 40
    python3 set_anki_limits.py --new 20       # back to Anki's default
    python3 set_anki_limits.py --show         # report, change nothing

The limit lives in a *deck config group* ('new.perDay'), not on the deck, and
every deck in a collection shares one by default. Editing that shared group
would also change the Spanish decks, so this creates a dedicated group and
points only the decks owned by this repo at it. Existing groups are left
alone; --show tells you which group each deck is on.

Per-deck-group, not global: each deck root keeps its own allowance, so studying
one subject does not spend the others' budget. Anki must be closed.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OWNED = ("Physics", "QM", "QC", "CS", "Science", "Algebra Lab")
GROUP_NAME = "Anki Lab"


def collection() -> Path:
    env = os.environ.get("ANKI_COLLECTION")
    if env:
        return Path(env).expanduser()
    root = Path.home() / ".local/share/Anki2"
    found = sorted(root.glob("*/collection.anki2")) if root.is_dir() else []
    if not found:
        found = sorted((Path.home() / ".config/anki").glob("*/collection.anki2"))
    if len(found) == 1:
        return found[0]
    if not found:
        sys.exit("no Anki collection found; set ANKI_COLLECTION")
    sys.exit("several collections found; set ANKI_COLLECTION:\n  "
             + "\n  ".join(str(p) for p in found))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--new", type=int, default=60,
                    help="new cards per day for these decks (default 60)")
    ap.add_argument("--decks", nargs="*", default=list(OWNED),
                    help=f"deck roots to touch (default: {' '.join(OWNED)})")
    ap.add_argument("--show", action="store_true",
                    help="report which group each deck uses, change nothing")
    args = ap.parse_args()

    from anki.collection import Collection

    path = collection()
    if not path.is_file():
        print(f"error: no Anki collection at {path}", file=sys.stderr)
        return 1

    col = Collection(str(path))
    try:
        d = col.decks
        targets = [x.name for x in d.all_names_and_ids()
                   if x.name.split("::")[0] in args.decks]
        if not targets:
            print("no matching decks. Available roots:", file=sys.stderr)
            for r in sorted({x.name.split("::")[0] for x in d.all_names_and_ids()}):
                print(f"  {r}", file=sys.stderr)
            return 1

        if args.show:
            print(f"{'deck':50} {'cards':>6} {'group':>12} {'new/day':>8}")
            for name in sorted(targets):
                did = d.id(name)
                n = col.db.scalar(
                    "SELECT COUNT(DISTINCT nid) FROM cards WHERE did = ?", did) or 0
                conf = d.get(did).get("conf") or 1
                cfg = d.get_config(conf) or {}
                gname = cfg.get("name", f"id {conf}")
                per = (cfg.get("new") or {}).get("perDay", "?")
                print(f"{name:50} {n:6} {gname:>12} {str(per):>8}")
            return 0

        # --- find or create the dedicated config group
        cid = None
        for cfg in d.all_config():
            if cfg.get("name") == GROUP_NAME:
                cid = cfg["id"]
                base = cfg
                break
        if cid is None:
            base = dict(d.get_config(1))          # clone the Default group
            base["name"] = GROUP_NAME
            cid = d.add_config_returning_id(GROUP_NAME, base)
            print(f"created config group {GROUP_NAME!r} (id {cid}) "
                  f"cloned from Default")
        created_group = cid

        base = dict(d.get_config(cid))
        base["new"] = dict(base.get("new") or {})
        base["new"]["perDay"] = args.new
        base["rev"] = dict(base.get("rev") or {})
        base["rev"].setdefault("perDay", 200)
        d.update_config(base, preserve_usn=False)

        # --- point our decks at it
        moved = 0
        for name in sorted(targets):
            did = d.id(name)
            deck = d.get(did)
            if deck.get("conf") == cid:
                continue
            d.set_config_id_for_deck_dict(deck, cid)
            d.update_dict(deck)
            moved += 1

        # --- verify by reading back
        bad = []
        for name in sorted(targets):
            did = d.id(name)
            conf = d.get(did).get("conf")
            per = ((d.get_config(conf) or {}).get("new") or {}).get("perDay")
            if per != args.new:
                bad.append(f"{name}: group={conf} perDay={per}")
        print(f"group {GROUP_NAME!r} (id {created_group}) perDay={args.new}; "
              f"{moved} deck(s) moved onto it, {len(targets)} total")
        if bad:
            print("FAILED to set:", *bad, sep="\n  ", file=sys.stderr)
            return 1
        print(f"verified {len(targets)}/{len(targets)} decks at "
              f"{args.new} new/day")
        others = sorted({x.name for x in d.all_names_and_ids()
                         if x.name.split("::")[0] not in args.decks})
        if others:
            print(f"untouched: {len(others)} deck(s) outside "
                  f"{' '.join(args.decks)}")
        return 0
    finally:
        col.close()


if __name__ == "__main__":
    raise SystemExit(main())
