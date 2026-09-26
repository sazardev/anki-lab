#!/usr/bin/env python3
"""Study desk: one entry point for the whole session.

    python3 study.py status              # the dashboard: what is due, per deck
    python3 study.py algebra             # the 3-step algebra session, guided
    python3 study.py session physics     # same, for any deck root
    python3 study.py drill factoring -n 15   # straight to the generator
    python3 study.py menu                # interactive picker
    python3 study.py workspace           # open the tiled Hyprland workspace

The session follows the loop in STUDY-FLOW.md: review, drill, then anchor the
new cards to what you just did. Ordering is the whole point -- a new card is
worth much more after a problem you just solved.

Reading the collection needs Anki to be closed (it holds a lock). When it is
running, 'status' falls back to the last snapshot written by 'sync', and says so
rather than failing.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SNAPSHOT = HERE / ".study-snapshot.json"
SNAP_MAX_AGE = 6 * 3600

ROOTS = ("Algebra Lab", "Physics", "QM", "QC", "CS", "Science")

# tag filter to offer after each method, as (label, anki search)
METHOD_TAGS = {
    "gcf":            ("GCF",              "tag:factoring::gcf"),
    "diff-squares":   ("diferencia de cuadrados", "tag:factoring::squares"),
    "perfect-square": ("cuadrado perfecto", "tag:factoring::what"),
    "grouping":       ("agrupacion",       "tag:factoring::grouping"),
    "trinomial":      ("trinomio",         "tag:factoring::monic"),
    "systems":        ("sistemas",         "tag:systems"),
    "gauss":          ("gauss-jordan",     "tag:la::gauss"),
    "eigen":          ("autovalores",      "tag:la::eigen"),
    "det":            ("determinantes",    "tag:la::det"),
}


# ---------------------------------------------------------------- anki access

def collection_path() -> Path | None:
    env = os.environ.get("ANKI_COLLECTION")
    if env:
        p = Path(env).expanduser()
        return p if p.is_file() else None
    root = Path.home() / ".local/share/Anki2"
    found = sorted(root.glob("*/collection.anki2")) if root.is_dir() else []
    if not found:
        found = sorted((Path.home() / ".config/anki").glob("*/collection.anki2"))
    return found[0] if len(found) == 1 else None


def collect_stats() -> dict | None:
    """Live read of the collection, or None if Anki holds the lock."""
    path = collection_path()
    if not path:
        return None
    try:
        from anki.collection import Collection
    except ImportError:
        return None
    try:
        col = Collection(str(path))
    except Exception:
        return None
    try:
        decks: dict[str, dict] = {}
        root = col.sched.deck_due_tree()

        def walk(node, prefix: str) -> None:
            # deck_due_tree gives basenames, so rebuild the full path
            full = f"{prefix}{node.name}" if prefix else node.name
            if full:
                decks[full] = {
                    "new": node.new_count,
                    "rev": node.review_count,
                    "total": node.total_including_children,
                }
            for ch in node.children:
                walk(ch, f"{full}::" if full else "")
        walk(root, "")

        row = col.db.first(
            "SELECT COUNT(*), SUM(CASE WHEN ease > 2 THEN 1 ELSE 0 END) FROM revlog")
        total_answers, correct = (row or (0, 0))
        correct = correct or 0
        since = int(time.time()) - 86400
        today = col.db.scalar(
            "SELECT COUNT(*) FROM revlog WHERE id / 1000 >= ?", since) or 0
        streak = streak_days(col)
        return {
            "decks": decks,
            "answers": total_answers,
            "retention": (100.0 * correct / total_answers) if total_answers else None,
            "today": today,
            "streak": streak,
            "taken": time.time(),
        }
    finally:
        col.close()


def streak_days(col) -> int:
    """Consecutive days with at least one answer, counting back from today."""
    days = {int(r[0]) for r in col.db.all(
        "SELECT DISTINCT id / 1000 FROM revlog")}
    if not days:
        return 0
    now = int(time.time())
    day = now // 86400
    # today may not be studied yet; allow the streak to start yesterday
    if day not in days and (day - 1) in days:
        day -= 1
    n = 0
    while day in days:
        n += 1
        day -= 1
    return n


def load_stats() -> tuple[dict | None, str]:
    live = collect_stats()
    if live:
        return live, "live"
    if SNAPSHOT.is_file():
        try:
            data = json.loads(SNAPSHOT.read_text())
            age = time.time() - data.get("taken", 0)
            if age < SNAP_MAX_AGE:
                return data, f"snapshot, {int(age // 60)} min old"
        except Exception:
            pass
    return None, "unavailable"


def write_snapshot() -> None:
    data = collect_stats()
    if not data:
        print("could not read the collection; is Anki running?", file=sys.stderr)
        return
    SNAPSHOT.write_text(json.dumps(data, indent=2))
    print(f"wrote {SNAPSHOT.name} ({len(data['decks'])} decks)")


# ---------------------------------------------------------------- display

BOLD, DIM, OFF = "\033[1m", "\033[2m", "\033[0m"
GREEN, YELLOW, CYAN = "\033[32m", "\033[33m", "\033[36m"


def bar(frac: float, width: int = 24) -> str:
    n = max(0, min(width, round(frac * width)))
    return "#" * n + "." * (width - n)


def cmd_status(args) -> int:
    data, src = load_stats()
    if not data:
        print("No se puede leer la coleccion de Anki.", file=sys.stderr)
        print("  Cierra Anki y ejecuta:  python3 study.py sync", file=sys.stderr)
        return 1

    decks = data["decks"]
    print(f"\n{BOLD}MESA DE ESTUDIO{BOLD}   {DIM}({src}){OFF}\n")

    if data.get("streak"):
        print(f"  racha  {YELLOW}{data['streak']} dia(s){OFF}"
              f"  Hoy  {data['today']} respuesta(s)"
              f"   Repasos  {data['answers']}")
    else:
        print(f"  {DIM}Sin repasos aun. Hoy: {data['today']} respuestas.{OFF}")
    if data.get("retention") is not None:
        print(f"  retencion  {GREEN}{data['retention']:.1f}%{OFF}"
              f"   (acierto / total)")
    print()

    # only the decks this repo owns, parents first
    rows = []
    for name in ROOTS:
        d = decks.get(name)
        if not d:
            continue
        rows.append((name, d["new"], d["rev"], d["total"], 0))
        for sub, sd in sorted(decks.items()):
            if sub.startswith(name + "::"):
                rows.append((sub, sd["new"], sd["rev"], sd["total"],
                             sub.count("::")))
    if not rows:
        print("  (ningun mazo de este repo encontrado)", file=sys.stderr)
        return 1

    biggest = max((r[1] + r[2]) for r in rows) or 1
    width = max(len(r[0]) for r in rows) + 2
    print(f"  {'mazo':{width}} {'nuevas':>7} {'repaso':>7} {'total':>7}")
    for name, new, rev, total, depth in rows:
        if depth == 0 and total == 0:
            continue
        indent = "  " + "    " * depth
        col = BOLD if depth == 0 else DIM
        label = name.split("::")[-1] if depth else name
        cells = f"{new:>7} {rev:>7} {total:>7}"
        if depth == 0 and (new or rev):
            cells += "  " + CYAN + bar((new + rev) / biggest, 18) + OFF
        print(f"{indent}{col}{label:{width - 2}}{cells}{OFF}")

    due = sum(r[1] + r[2] for r in rows if r[4] == 0)
    tot = sum(r[3] for r in rows if r[4] == 0)
    print(f"\n  {BOLD}pendientes hoy: {due}{OFF} de {tot} tarjetas en tus mazos\n")
    if src != "live":
        print(f"  {DIM}Anki esta abierto: datos de un snapshot. "
              f"Para exactos: python3 study.py sync{OFF}\n")
    return 0


# ---------------------------------------------------------------- session

def cmd_session(args) -> int:
    root = args.deck
    print(f"\n{BOLD}SESION: {root}{OFF}   {DIM}revisar -> practicar -> anclar{OFF}\n")

    data, src = load_stats()
    if data:
        d = data["decks"].get(root, {})
        print(f"  paso 1  REPASAR   {d.get('new', 0)} nuevas, "
              f"{d.get('rev', 0)} repasos pendientes en {root}")
        print(f"          {DIM}Abre Anki en el mazo {root} y hazlos.{OFF}\n")
    else:
        print(f"  paso 1  REPASAR   {DIM}(no se pudo leer Anki){OFF}\n")

    if root == "Algebra Lab":
        print("  paso 2  PRACTICAR  un metodo, con --practice")
        print(f"          {DIM}metodos con tarjetas: ac-trick y gcf son los debiles{OFF}")
        print()
        for i, topic in enumerate(
                ("factoring", "systems", "gauss", "eigen", "det", "random"), 1):
            label = {"factoring": "factoreo (6 metodos)",
                     "systems": "sistemas 2x2 y 3x3",
                     "gauss": "reduccion por filas",
                     "eigen": "autovalores y vectores",
                     "det": "determinantes 3x3",
                     "random": "aleatorio"}[topic]
            print(f"            {i}  python3 algebra_lab.py {topic} "
                  f"-n 15 --practice   {DIM}{label}{OFF}")
        print(f"          {DIM}o el menu: ./run.sh menu{OFF}")
        print()
        print("  paso 3  ANCLAR    filtra en Anki por el metodo que pracastaste:")
        print()
        for key, (label, q) in METHOD_TAGS.items():
            print(f"            {label:26} {DIM}{q}{OFF}")
    else:
        print(f"  paso 2  PRACTICAR  lee 2-3 tarjetas de {root} y pon en practice")
        print(f"          {DIM}lo que seueba de memoria es lo que se queda{OFF}")
        print()
        print(f"  paso 3  ANCLAR    anade hasta 5 tarjetas nuevas de {root}")
    print(f"\n  {DIM}el orden importa: la tarjeta nueva va DESPUES del problema, "
          f"no antes.{OFF}")
    print(f"  {DIM}ver STUDY-FLOW.md para el por que.{OFF}\n")
    return 0


def cmd_drill(args) -> int:
    cmd = [sys.executable, str(HERE / "algebra_lab.py")] + args.rest
    if "--practice" not in cmd and not args.no_practice:
        cmd.append("--practice")
    return subprocess.call(cmd)


def cmd_workspace(args) -> int:
    launcher = HERE.parent / "setup" / "launchers" / "omarchy-launch-study"
    if not launcher.is_file():
        print(f"missing {launcher}", file=sys.stderr)
        return 1
    return subprocess.call([str(launcher)])


def cmd_sync(args) -> int:
    write_snapshot()
    return 0


# ---------------------------------------------------------------- menu

SUBJECTS = ["Algebra Lab", "Physics", "QM", "QC", "CS", "Science"]


def cmd_menu(args) -> int:
    while True:
        data, src = load_stats()
        print(f"\n{BOLD}Mesa de estudio{OFF} {DIM}({src}){OFF}")
        for i, s in enumerate(SUBJECTS, 1):
            n = (data or {}).get("decks", {}).get(s, {})
            print(f"  {i}  {s:14} {DIM}nuevas {n.get('new', 0):>3}"
                  f"  repasos {n.get('rev', 0):>3}{OFF}")
        print("  s  estado (dashboard)")
        print("  w  workspace de Hyprland")
        print("  q  salir")
        try:
            k = input("\n  ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if k == "q":
            return 0
        if k == "s":
            cmd_status(args)
        elif k == "w":
            cmd_workspace(args)
        elif k.isdigit() and 1 <= int(k) <= len(SUBJECTS):
            cmd_session(argparse.Namespace(deck=SUBJECTS[int(k) - 1]))
        else:
            print("  opcion no valida")


# ---------------------------------------------------------------- cli

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Study desk: dashboard, guided session, drills.")
    sub = ap.add_subparsers(dest="cmd")

    sub.add_parser("status", help="dashboard: what is due, per deck")
    sub.add_parser("sync", help="snapshot the collection (Anki must be closed)")

    p = sub.add_parser("session", help="guided 3-step session for a deck")
    p.add_argument("deck", nargs="?", default="Algebra Lab", choices=ROOTS)

    p = sub.add_parser("drill", help="run a generator with --practice")
    p.add_argument("rest", nargs=argparse.REMAINDER)
    p.add_argument("--no-practice", action="store_true")

    sub.add_parser("workspace", help="open the tiled Hyprland workspace")
    sub.add_parser("menu", help="interactive picker")

    args = ap.parse_args()
    cmd = args.cmd or "status"
    return {
        "status": cmd_status, "sync": cmd_sync, "session": cmd_session,
        "drill": cmd_drill, "workspace": cmd_workspace, "menu": cmd_menu,
    }[cmd](args)


if __name__ == "__main__":
    raise SystemExit(main())
