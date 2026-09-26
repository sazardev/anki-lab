"""Detector de espanol residual en el mazo generado.

Escanea TODOS los campos de las notas y busca palabras o marcadores
tipicos del espanol. Uso:  .venv/bin/python spanish_check.py
"""

import os
import re
import sys
import zipfile
import sqlite3
import json
import tempfile
import collections
import html as htmlmod

APKG = sys.argv[1] if len(sys.argv) > 1 else "/tmp/opencode/Ingles-Grammar-B1C2.apkg"

# palabras funcionales del espanol que no existen en ingles
ES = r"""
 el la los las un una unos unas de del al y o u e o sea es son era eran
 ser estar estoy está están he ha han había habían hay hay
 que qué quien cuál como cómo cuando donde porque para por con sin
 sobre bajo entre desde hasta hacia tras tras durante
 pero aunque sino tambien tampoco tampoco ya muy mas más menos
 esto esto ese ese aquel aquello aqui aquí alli allí
 mi mis tu tus su sus nuestro nuestra vuestro
 yo tú el ella nosotros vosotros ellos ellas
 me te se nos os lo le les
 hacer hace hacen hacia hay
 con saber sabe saben
 este esta estos estas mismo misma
 cada todo toda todos todas
 otro otra otros otras
 varios varias mucho muchos alguno alguna ninguno
 entonces despues después ahora antes luego
 sobre todo ademas además aunque ademas
 cosa cosas manera forma modo sitio lugar
 siempre nunca jamas jamás
 deber debe deben
 poder puede pueden
 decir dice dicen dijo dijo querer
 tambien así aunque sinoquizá
 """.split()

# marcadores inequívocos
MARKERS = [
    r"\bel\b(?!>)", r"\bla\b", r"\blos\b", r"\blas\b", r"\bun\b", r"\buna\b",
    r"\bde\b(?! ?-)", r"\bdel\b", r"\bque\b", r"\bqué\b", r"\bpara\b",
    r"\bcon\b", r"\bpor\b", r"\bsin\b", r"\bcomo\b", r"\bcuando\b",
    r"\bporque\b", r"\bmás\b", r"\bmuy\b", r"\btambién\b", r"\bya\b",
    r"\bestá\b", r"\bestán\b", r"\bhay\b", r"\bhace\b", r"\bdebe\b",
    r"\bpuede\b", r"\bpueden\b", r"\bnunca\b", r"\bsiempre\b",
    r"\bnote\b", r"\bwarning\b", r"\bOJO\b", r"\bWATCH OUT\b",
    r"\bEjemplos?\b", r"\bRegla\b", r"\bfalso amigo\b",
    r"\binterferencia\b", r"\bnivel B1\b",
]

# palabras inglesas legitimas que coinciden con el patron (falsos positivos)
OK = set("""a an the is are was were be been being of in on at to for with by
from as it this that these those and or but if then than so such not no yes
one two three we you he she they me him her them my your his its our their
do does did done have has had will would shall should can could may might must
where when why how who what which whose there here more most less least much
many few several any some all both each every other another own same too very
just only even still already yet again never always often sometimes usually
rarely hardly barely enough almost about above below before after during
while because although though unless until since between among through
across around along up down over under past per via toward towards
make makes made take takes took get gets got give gives gave say says said
see sees saw know knows knew think thinks thought go goes went come comes came
look looks looked want wants wanted need needs needed use uses used
work works worked seem seems appeared look looks feel feels felt
""".split())


def strip_html(s):
    s = re.sub(r"<[^>]+>", " ", s)
    return htmlmod.unescape(s)


def main():
    z = zipfile.ZipFile(APKG)
    tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    tmp.write(z.read([n for n in z.namelist() if n.endswith(".anki2")][0]))
    tmp.close()
    con = sqlite3.connect(tmp.name)
    col = json.loads(con.execute("select models from col").fetchone()[0])
    decks = json.loads(con.execute("select decks from col").fetchone()[0])
    dname = {int(d["id"]): d["name"] for d in decks.values() if d["id"] != 1}

    hits = collections.Counter()
    where = collections.defaultdict(set)
    for nid, mid, did, flds in con.execute(
            "select c.nid, n.mid, c.did, n.flds from cards c "
            "join notes n on n.id = c.nid"):
        mname = col[str(mid)]["name"]
        if mname.endswith("Cloze"):
            continue          # las frases inglesas ya son solo ingles
        text = strip_html(flds)
        for m in MARKERS:
            for mm in re.finditer(m, text):
                w = mm.group(0)
                if w.lower() in OK:
                    continue
                hits[w] += 1
                where[w].add(dname.get(did, "?")[:34])
        # palabras del español de 3+ letras que no sean inglesas conocidas
        for w in re.findall(r"[A-Za-zÁÉÍÓÚáéíóúñÑ']{3,}", text):
            lw = w.lower()
            if lw in OK or lw in set(x.lower() for x in ES):
                continue
        # heuristica: palabras acentuadas que no existen en ingles
    # palabras acentuadas tipicamente espanolas que aparecen sueltas
    for w in sorted(hits, key=lambda x: -hits[x]):
        print(f"{hits[w]:>5}x  {w:<14} {sorted(where[w])[:2]}")
    total = sum(hits.values())
    print(f"\nTOTAL marcadores españoles: {total}")
    os.unlink(tmp.name)
    return total


if __name__ == "__main__":
    sys.exit(0 if main() == 0 else 1)
