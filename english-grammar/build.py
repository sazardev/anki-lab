"""Punto de entrada: importa todos los modulos de contenido y escribe el .apkg.

Uso:  .venv/bin/python build.py [ruta_salida.apkg]
"""

import importlib
import json
import warnings
import os
import sys
import sqlite3
import zipfile
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import ankilib as AL

MODULES = [
    "c01_fundamentos",
    "c02_verbos_presentes",
    "c03_pasado_perfecto",
    "c04_futuro",
    "c05_modales",
    "c06_condicionales",
    "c07_pasiva_causativa",
    "c08_patrones_verbales",
    "c09_frases_relativas",
    "c10_clausulas",
    "c11_preposiciones",
    "c12_phrasal_verbs",
    "c13_colocaciones",
    "c14_registro_c1c2",
    "c15_errores",
    "c16_irregulares",
    "c17_lexico_c1c2",
    "c18_cohesion",
    "c19_word_formation",
    "c20_oraciones_c2",
    "c21_conjugacion",
    "c22_reported_speech",
    "c23_trampas",
]


def main(out=None):
    # Anki SÍ admite <s> y <u>; el aviso de genanki es conservador.
    warnings.filterwarnings("ignore", message=".*invalid HTML tags.*")
    for m in MODULES:
        name = f"content.{m}"
        try:
            importlib.import_module(name)
        except ModuleNotFoundError as e:
            if e.name == name:
                print(f"  [skip] {m} (todavia no existe)")
            else:
                raise
        else:
            print(f"  [ok]   {m}")

    bad = AL.validate()
    if bad:
        raise SystemExit(1)

    out = out or "/tmp/opencode/Ingles-Grammar-B1C2.apkg"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    n_notes, _, decks = AL.write(out)

    # ---- estadisticas reales leidas del .apkg generado
    with zipfile.ZipFile(out) as z:
        dbn = [n for n in z.namelist() if n.endswith(".anki2")][0]
        tmp = tempfile.NamedTemporaryFile(suffix=".anki2", delete=False)
        tmp.write(z.read(dbn))
        tmp.close()
    con = sqlite3.connect(tmp.name)
    os.unlink(tmp.name)
    n_cards = con.execute("select count(*) from cards").fetchone()[0]
    n_decks = len(json.loads(con.execute("select decks from col").fetchone()[0]))

    print("\n" + "=" * 58)
    print(f"  Notas generadas : {n_notes}")
    print(f"  Tarjetas       : {n_cards}")
    print(f"  Mazos          : {n_decks}")
    print(f"  Archivo        : {out}")
    print("=" * 58)
    print("\n  Desglose por sub-mazo:")
    for d in sorted(decks, key=lambda x: x.name):
        if d.notes:
            print(f"    {len(d.notes):>4}  {d.name}")
    return out


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
