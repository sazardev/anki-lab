"""Reemplaza el mazo de Ingles en tu perfil de Anki por la version 100% ingles.

 borra los mazos antiguos (los que empiezan por 01..23 o 'Ingles') y
importa el .apkg nuevo.  Deja intacto el resto (p.ej. 'Algebra Lab').

USA ESTO solo con Anki CERRADO.
Uso:  .venv/bin/python replace_deck.py
"""

import os
import shutil
import subprocess
import sys
import time

PROFILE = os.path.expanduser("~/.local/share/Anki2/User 1")
COLLECTION = os.path.join(PROFILE, "collection.anki2")
APKG = os.path.expanduser("~/Work/anki-english/Ingles-Grammar-B1C2-EN.apkg")

# prefijos de los mazos antiguos (en espanol) que hay que eliminar
OLD_PREFIXES = tuple(f"{i:02d} " for i in range(1, 24)) + ("Ingles",)


def anki_running():
    r = subprocess.run(["pgrep", "-c", "anki"], capture_output=True, text=True)
    return int(r.stdout.strip() or 0) > 0


def main():
    if anki_running():
        print("""
  Anki esta ABIERTO.  Cierra Anki del todo y vuelve a ejecutar:

      ~/Work/anki-english/.venv/bin/python ~/Work/anki-english/replace_deck.py
""")
        return 1

    if not os.path.exists(APKG):
        print("  No encuentro el .apkg:", APKG)
        return 1

    bak = COLLECTION + ".bak-antes-de-reemplazar"
    if not os.path.exists(bak):
        shutil.copy2(COLLECTION, bak)
        print("  Backup creado:", os.path.basename(bak))

    from anki.collection import Collection, ImportAnkiPackageRequest

    col = Collection(COLLECTION)
    before_n, before_c = col.note_count(), col.card_count()

    # --- borrar las notas de los mazos antiguos
    victims = [d for d in col.decks.all_names_and_ids()
               if d.name.startswith(OLD_PREFIXES)]
    if victims:
        cids = []
        for d in victims:
            cids += col.decks.cids(d.id)
        if cids:
            col.remove_cards_and_orphaned_notes(cids)
        # limpiar mazos vacios huerfanos
        for d in victims:
            try:
                col.decks.remove([d.id])
            except Exception:
                pass
        print(f"  Borrados {len(victims)} mazos antiguos "
              f"({len(cids)} tarjetas)")

    # --- importar el nuevo
    col.import_anki_package(ImportAnkiPackageRequest(package_path=APKG))
    col.close()
    time.sleep(0.3)

    col = Collection(COLLECTION)
    kept = sorted(d.name for d in col.decks.all_names_and_ids()
                  if d.name == "Default" or d.name == "Algebra Lab")
    print(f"""
  LISTO
    notas    : {before_n} -> {col.note_count()}
    tarjetas : {before_c} -> {col.card_count()}
    mazos de ingles: {len([d for d in col.decks.all_names_and_ids() if d.name[:2].isdigit() or d.name == 'Ingles'])}
    otros mazos conservados: {', '.join(n for n in kept if n != 'Default') or '(ninguno)'}
  Ya puedes abrir Anki.
""")
    col.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
