"""Importa el mazo en tu perfil de Anki REAL.

USA ESTO solo con Anki CERRADO (cerrar ventana o salir del menú).
Uso:  .venv/bin/python importar.py
"""

import os
import shutil
import sys
import time

PROFILE = os.path.expanduser("~/.local/share/Anki2/User 1")
COLLECTION = os.path.join(PROFILE, "collection.anki2")
APKG = os.path.expanduser("~/Ingles-Grammar-B1C2.apkg")


def anki_corriendo():
    import subprocess
    r = subprocess.run(["pgrep", "-c", "anki"], capture_output=True, text=True)
    return int(r.stdout.strip() or 0) > 0


def main():
    if anki_corriendo():
        print("""
  Anki esta ABIERTO.  No puedo tocar la coleccion mientras este abierto
  (se corromperia).

  Opcion A (20 segundos, tu):
      1. Cierra Anki del todo.
      2. Ejecuta:   ~/Work/anki-english/.venv/bin/python ~/Work/anki-english/importar.py

  Opcion B (manual, sin cerrar):
      En Anki:  Archivo > Importar  (atajo Ctrl+Shift+I)
      Elige  ~/Desktop/Ingles-Grammar-B1C2.apkg
      Dale a "Importar".  Veras un aviso: 2475 notas, 3309 tarjetas.
""")
        return 1

    global APKG
    if not os.path.exists(APKG):
        APKG = os.path.expanduser("~/Desktop/Ingles-Grammar-B1C2.apkg")
    if not os.path.exists(APKG):
        print("  No encuentro el .apkg")
        return 1

    # red de seguridad: backup antes de tocar nada
    bak = COLLECTION + ".antes-de-importar.bak"
    if not os.path.exists(bak):
        shutil.copy2(COLLECTION, bak)
        print(f"  Backup creado: {bak}")

    from anki.collection import Collection, ImportAnkiPackageRequest

    col = Collection(COLLECTION)
    antes_n, antes_c = col.note_count(), col.card_count()
    col.import_anki_package(ImportAnkiPackageRequest(package_path=APKG))
    col.close()
    time.sleep(0.3)

    col = Collection(COLLECTION)
    print(f"""
  IMPORTACION CORRECTA
    notas    : {antes_n} -> {col.note_count()}  (+{col.note_count()-antes_n})
    tarjetas : {antes_c} -> {col.card_count()}  (+{col.card_count()-antes_c})
    mazos    : {len([x for x in col.decks.all_names_and_ids() if x.name != 'Default'])}
  Ya puedes abrir Anki.
""")
    col.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
