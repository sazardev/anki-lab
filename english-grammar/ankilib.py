"""
Motor de construccion de mazos de Anki para Gramatica de Ingles B1-C2.

Tres tipos de nota:
  1. Reconocimiento  - enunciado con hueco -> respuesta + regla + excepciones
  2. Produccion      - se escribe la forma correcta (recuerdo activo)
  3. Cloze           - se enmascara algo dentro de su contexto real

Los mazos se organizan en sub-decks anidados ("Ingles::1 ...::Articulos").
"""

import hashlib
import re

import genanki
from genanki import Model, Note, Deck, Package, Card

# ---------------------------------------------------------------- identificadores
# IDs fijos => al regenerar, Anki actualiza el texto en vez de duplicar notas.

RID = 1760000001   # modelo Reconocimiento
PID = 1760000002   # modelo Produccion
CID = 1760000003   # modelo Cloze
DECK_ROOT = 1761000000

_DECKS = {}   # ruta -> Deck
_ALL_DECKS = []


def deck(name):
    """Devuelve (creando si hace falta) el mazo de esa ruta."""
    d = _DECKS.get(name)
    if d is None:
        d = Deck(DECK_ROOT + (len(_ALL_DECKS) + 1), name)
        _DECKS[name] = d
        _ALL_DECKS.append(d)
    return d


# --------------------------------------------------------------------- estilos

CSS = """
:root {
  --ink:#1b1b1f; --dim:#6b6b76; --line:#e3e3ea; --tint:#f4f6fb;
  --accent:#1f5fd0; --ok:#0f7b3e; --warn:#a35b00;
}
.card {
  font-family: -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 20px; line-height: 1.55; color: var(--ink);
  background: #ffffff; text-align: left; padding: 0 16px;
  max-width: 780px; margin: 0 auto;
}
.nightMode, .night_mode {
  --ink:#e6e6ea; --dim:#9b9baa; --line:#34343e; --tint:#22222a;
  --accent:#7aa7f7; --ok:#5fd08a; --warn:#e5a13a;
  background: #1e1e24; color: var(--ink);
}

.badge {
  display: inline-block; font-size: 11px; font-weight: 700; letter-spacing: .6px;
  text-transform: uppercase; padding: 2px 9px; border-radius: 999px;
  border: 1px solid var(--line); color: var(--dim);
  vertical-align: 3px; margin-left: 8px; white-space: nowrap;
}
.badge.b1 { border-color:#3aa76d; color:#0f7b3e; }
.badge.b2 { border-color:#1f5fd0; color:#1f5fd0; }
.badge.c1 { border-color:#a35b00; color:#a35b00; }
.badge.c2 { border-color:#8b3ab5; color:#8b3ab5; }
.nightMode .badge, .night_mode .badge { background: transparent !important; }

.q { font-size: 23px; margin: 2px 0 4px; }
.prompt { color: var(--dim); font-size: 15px; font-style: italic; margin-bottom: 10px; }
.t { color: var(--dim); font-size: 15px; }
.ex { font-size: 17px; margin: 4px 0; }
.ans { color: var(--ok); font-weight: 700; }
.full { font-size: 18px; margin: 4px 0 12px; }

.gap {
  display: inline-block; min-width: 96px; text-align: center;
  border-bottom: 2.5px solid var(--accent); font-weight: 700;
}
.gap.empty { color: transparent; }
.gap.b { color: var(--accent); }
.cue { color: var(--dim); font-size: 14px; font-style: italic; }

.box {
  border: 1px solid var(--line); border-radius: 10px; padding: 9px 13px;
  margin: 10px 0; background: var(--tint);
}
.lbl {
  font-size: 10.5px; font-weight: 700; text-transform: uppercase; letter-spacing: .8px;
  color: var(--dim); display: block; margin-bottom: 2px;
}
.rule { border-left: 4px solid var(--accent); }
.warn { border-left: 4px solid var(--warn); }
.note { border-left: 4px solid var(--ok); }
hr.sep { border: 0; border-top: 1px solid var(--line); margin: 14px 0; }

table { border-collapse: collapse; width: 100%; font-size: 16px; margin: 6px 0; }
th, td { border: 1px solid var(--line); padding: 5px 8px; text-align: left;
          vertical-align: top; }
th { background: var(--tint); font-size: 12.5px; text-transform: uppercase;
      letter-spacing: .5px; color: var(--dim); }
td.hi { background: var(--tint); font-weight: 700; }

ul.tight, ol.tight { margin: 4px 0; padding-left: 22px; }
li { margin: 3px 0; }
.small { font-size: 15px; }
.big { font-size: 27px; font-weight: 700; }
.mono { font-family: Menlo, Consolas, monospace; }
.k { color: var(--accent); font-weight: 600; }
.lin { font-family: Menlo, Consolas, monospace; background: var(--tint);
        border-radius: 4px; padding: 0 4px; }
.cloze { font-weight: 700; color: var(--accent); background: var(--tint);
          border-radius: 4px; padding: 0 3px; }
"""

# ---------------------------------------------------------------------- modelos

MODEL_RULE_DEF = Model(
    RID, "Ingles::Reconocimiento",
    fields=[{"name": "Front"}, {"name": "Back"}, {"name": "Regla"},
            {"name": "Ejemplos"}, {"name": "Notas"}],
    templates=[{
        "name": "Completar",
        "qfmt": "{{Front}}",
        "afmt": ("{{FrontSide}}<hr class=\"sep\">"
                 "<div class=\"full\">{{Back}}</div>"
                 "{{#Regla}}<div class=\"box rule\"><span class=\"lbl\">Regla</span>{{Regla}}</div>{{/Regla}}"
                 "{{#Ejemplos}}<div class=\"box\"><span class=\"lbl\">Ejemplos</span>{{Ejemplos}}</div>{{/Ejemplos}}"
                 "{{#Notas}}<div class=\"box warn\"><span class=\"lbl\">Ojo / excepciones</span>{{Notas}}</div>{{/Notas}}"),
    }],
    css=CSS,
)

MODEL_PROD_DEF = Model(
    PID, "Ingles::Produccion",
    fields=[{"name": "Prompt"}, {"name": "Respuesta"}, {"name": "Pista"},
            {"name": "Regla"}, {"name": "Ejemplos"}],
    templates=[{
        "name": "Escribir",
        "qfmt": "{{Prompt}}",
        "afmt": ("{{FrontSide}}<hr class=\"sep\">"
                 "<div class=\"ans big\">{{Respuesta}}</div>"
                 "{{#Pista}}<div class=\"box note\"><span class=\"lbl\">Pista</span>{{Pista}}</div>{{/Pista}}"
                 "{{#Regla}}<div class=\"box rule\"><span class=\"lbl\">Regla</span>{{Regla}}</div>{{/Regla}}"
                 "{{#Ejemplos}}<div class=\"box\"><span class=\"lbl\">Ejemplos</span>{{Ejemplos}}</div>{{/Ejemplos}}"),
    }],
    css=CSS,
)

MODEL_CLOZE_DEF = Model(
    CID, "Ingles::Cloze",
    fields=[{"name": "Texto"}, {"name": "Extra"}],
    templates=[{
        "name": "Cloze",
        "qfmt": "{{cloze:Texto}}<hr class=\"sep\">{{Extra}}",
        "afmt": "{{cloze:Texto}}<hr class=\"sep\">{{Extra}}",
    }],
    css=CSS,
    model_type=1,
)

MODELS = (MODEL_RULE_DEF, MODEL_PROD_DEF, MODEL_CLOZE_DEF)


# ------------------------------------------------------------------ utilidades

def badge(level):
    lv = level.strip().upper()
    return f'<span class="badge {lv.lower()}">{lv}</span>'


def ex(*pairs):
    """Solo ingles. Si la cadena trae '|| traduccion', la traduccion se
    descarta: el mazo es 100% inglés (inmersión total)."""
    out = []
    for p in pairs:
        en = p.split("||", 1)[0]
        out.append(f'<div class="ex">{en.strip()}</div>')
    return "".join(out)


def ul(*items):
    return "<ul class='tight'>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ol(*items):
    return "<ol class='tight'>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def table(headers, rows):
    th = "".join(f"<th>{h}</th>" for h in headers)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"<table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>"


def tl(*rows):
    """Tabla de 2 columnas; la primera celda de cada fila queda resaltada."""
    body = "".join("<tr>" + "".join(
        f"<td class='hi'>{c}</td>" if i == 0 else f"<td>{c}</td>"
        for i, c in enumerate(r)) + "</tr>" for r in rows)
    return f"<table><tbody>{body}</tbody></table>"


_TAGS = ("b", "i", "div", "span", "ul", "ol", "li", "td", "th", "tr",
         "table", "thead", "tbody", "p", "em", "strong", "sup", "sub")
_CLOSERS = {"li": "ul", "td": "table", "th": "table", "tr": "table"}


def sanitize(html):
    """Cierra (y descarta) las etiquetas HTML mal formadas de un campo.

    Se aplica AL GENERAR la tarjeta, nunca al codigo fuente, para que un
    '<b>' despistado no rompa ni el .py ni el renderizado.
    """
    if not html:
        return html
    tokens = list(re.finditer(r"<(/?)([a-zA-Z]+)[^>]*?(/?)>", html))
    if not tokens:
        return html
    stack, drop, pos = [], set(), 0
    for m in tokens:
        closing, name, selfc = m.group(1), m.group(2).lower(), m.group(3)
        if name in ("br", "hr", "img", "input", "meta", "link") or selfc:
            continue
        if closing:
            if stack and stack[-1] == name:
                stack.pop()
            else:
                drop.add(m.start())          # cierre huerfano: se descarta
        else:
            stack.append(name)
    if not drop and not stack:
        return html
    out, prev = [], 0
    for m in tokens:
        if m.start() in drop:
            out.append(html[prev:m.start()])
            prev = m.end()
    out.append(html[prev:])
    res = "".join(out)
    if stack:
        res += "".join("</%s>" % t for t in reversed(stack))
    return res


def _guid(model_id, deck_name, fields):
    """GUID estable y unico: si el mazo se regenera, Anki actualiza la
    nota en vez de duplicarla."""
    h = hashlib.sha256()
    h.update(("|".join([str(model_id), deck_name] + [str(f) for f in fields])
              ).encode("utf-8"))
    n = int.from_bytes(h.digest()[:8], "big")
    out = []
    while n > 0:
        out.append(_B91[n % len(_B91)])
        n //= len(_B91)
    return "".join(reversed(out)) or "0"


_B91 = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789!#$%&()*+,-./:;<=>?@[]\\^_`{|}~")


def _t(*tags):
    """Normaliza tags. Acepta tanto 'noun countability' como ('a','b').
    NUNCA desintegra una cadena en caracteres."""
    out = []
    for t in tags:
        if not t:
            continue
        if isinstance(t, (list, tuple, set)):
            out += _t(*t)
        else:
            out += [x for x in str(t).split() if x]
    return out


# ------------------------------------------------------------ API de contenido
# Todas las funciones registrar la nota en su mazo automaticamente.

def rule(deck_name, front, back, regla="", ejemplos="", notas="", tags=()):
    """RECONOCIMIENTO: enunciado -> respuesta + regla + excepciones."""
    f = [front, back, regla, ejemplos, notas]
    n = Note(model=MODEL_RULE_DEF, fields=f, tags=_t(tags),
             guid=_guid(RID, deck_name, f))
    deck(deck_name).add_note(n)
    return n


def prod(deck_name, prompt, respuesta, pista="", regla="", ejemplos="", tags=()):
    """PRODUCCION: se escribe la forma correcta (recuerdo activo)."""
    f = [prompt, respuesta, pista, regla, ejemplos]
    n = Note(model=MODEL_PROD_DEF, fields=f, tags=_t(tags),
             guid=_guid(PID, deck_name, f))
    deck(deck_name).add_note(n)
    return n


_CLOZE_RE = re.compile(r"{{c(\d+)::")


def cloze(deck_name, texto, extra="", tags=(), dry=False):
    """
    CLOZE: `texto` debe llevar marcadores {{c1::...}} / {{c2::...}}.
    genanki no crea las tarjetas cloze: las generamos nosotros, una por
    cada ordinal presente, que es lo que Anki espera.
    """
    n = Note(model=MODEL_CLOZE_DEF, fields=[texto, extra], tags=_t(tags))
    ords = sorted({int(m) for m in _CLOZE_RE.findall(texto)})
    if not ords:
        raise ValueError("cloze() sin marcadores {{cN::}}: %r" % texto[:70])
    n.cards = [Card(o) for o in ords]
    if not dry:
        deck(deck_name).add_note(n)
    return n


def cloze_n(texto):
    """Numero de tarjetas que producira un texto cloze."""
    return len({int(m) for m in _CLOZE_RE.findall(texto)})


def gap(deck_name, sentence, answer, nivel="B1", cue="", forma="", regla="",
        ejemplos="", notas="", tags=(), show_gap=False, produccion=True,
        pista="", hint=None, trad=None):
    """
    Atajo de alto nivel: una regla con hueco. Genera 2 tarjetas
    (reconocimiento + produccion) salvo que produccion=False.

    sentence  'How ___ sugar do you need?'
    answer    'much'
    forma     texto de apoyo en la tarjeta de produccion
    show_gap  si True el anverso ya muestra la palabra (solo repaso visual)
    """
    d = deck(deck_name)
    tags = _t(tags) + [nivel.lower(), "english"]
    hueco = ('<span class="gap b">%s</span>' % answer if show_gap
             else '<span class="gap empty">&#8203;</span>')
    _fr = ['<div class="q">%s</div>'
           '<div class="prompt">Completa: %s</div>'
           % (sentence.replace("___", hueco), cue or answer),
           '<span class="ans">%s</span>' % answer, regla, ejemplos, notas]
    out = [Note(model=MODEL_RULE_DEF, fields=_fr, tags=_t(tags),
                guid=_guid(RID, deck_name, _fr))]
    if produccion:
        # el hueco sigue visible: hay que saber DONDE escribir
        out.append(Note(model=MODEL_PROD_DEF,
                        fields=['<div class="q">%s</div>'
                                '<div class="prompt">Escribe: %s</div>'
                                % (sentence.replace("___", hueco), cue or answer),
                                '<span class="ans">%s</span>' % answer,
                                pista or '(%d car.) &nbsp;&middot;&nbsp; <i>%s</i>'
                                % (len(answer) if hint is None else hint,
                                   forma or answer),
                                regla, ejemplos],
                        tags=_t(tags) + ["production"]))
    if trad:
        pass          # english-only deck: no translation cards
    for n in out:
        d.add_note(n)
    return out


def tabla(deck_name, headers, rows, titulo="", nivel="B1", tags=(), nota=""):
    """Tarjeta de referencia: tabla completa en reverso, titular en anverso."""
    return rule(
        deck_name,
        front='<div class="q">%s</div>%s' % (titulo, badge(nivel)),
        back="",
        regla=table(headers, rows),
        notas=nota,
        tags=_t(tags) + [nivel.lower(), "reference"])


def serie(deck_name, items, nivel="B1", tags=(), regla_col=None, ej_col=None,
          nota_col=None, gap_idx=None):
    """
    Genera muchas tarjetas de una lista de datos, para contenido repetitivo
    (verbos + preposicion, colocaciones, verbos irregulares...).

    Cada item es una tupla o lista. Por defecto:
        [0] = anverso (pregunta)
        [1] = respuesta
        [2] = regla / explicacion
        [3] = ejemplos
        [4] = notas

    Con gap_idx=(i_frase, i_respuesta) genera en cambio tarjetas con hueco,
    donde i_frase es el indice de la frase con ___ y i_respuesta el de la
    forma que va en el hueco.
    """
    d = deck(deck_name)
    out = []
    for it in items:
        it = list(it) + [""] * (6 - len(it))
        tags_in = _t(tags)
        if gap_idx is not None:
            frase, resp = it[gap_idx[0]], it[gap_idx[1]]
            cue = it[2] if it[2] else resp
            out += gap(d.name, frase, resp, nivel=nivel, cue=cue,
                       regla=it[3] if len(it) > 3 else "",
                       ejemplos=it[4] if len(it) > 4 else "",
                       tags=tags_in,
                       trad=(it[5] if len(it) > 5 else None) or None)
        else:
            n = Note(model=MODEL_RULE_DEF,
                     fields=[it[0],
                             '<span class="ans">%s</span>' % it[1],
                             it[2] if regla_col is None else it[regla_col],
                             it[3] if ej_col is None else it[ej_col],
                             it[4] if nota_col is None else it[nota_col]],
                     tags=_t(tags) + [nivel.lower()])
            d.add_note(n)
            out.append(n)
    return out


def serie_gap(deck_name, items, nivel="B1", tags=()):
    """Atajo: items = [frase_con_hueco, respuesta, pista, regla, ejemplos]."""
    return serie(deck_name, items, nivel=nivel, tags=tags, gap_idx=(0, 1))


def serie_cloze(deck_name, items, nivel="B1", tags=()):
    """items = [texto_con_clozes, extra]"""
    d = deck(deck_name)
    for it in items:
        it = list(it) + ["", ""]
        cloze(deck_name, it[0], it[1], tags=_t(tags) + [nivel.lower()])
    return d


# ------------------------------------------------------------------- escritura

_BAD = re.compile(r"[\u0400-\u04FF\u4E00-\u9FFF\u3040-\u30FF\u0600-\u06FF]")

# atajos de teclado que colaron caracteres raros ("inglesAttribute")
_GLUED = re.compile(r"[A-Za-záéíóúñ]{2,}(?:[A-ZÁÉÍÓÚÑ][a-záéíóúñ]{2,})")


def validate(strict=True):
    """Revisa TODO el contenido antes de escribir el .apkg."""
    problems = []
    for d in _ALL_DECKS:
        for note in d.notes:
            for fld in note.fields:
                for m in _BAD.finditer(fld):
                    problems.append((d.name, m.group(0),
                                     fld[max(0, m.start() - 30):m.start() + 20]))
    if problems:
        for name, ch, ctx in problems[:40]:
            print(f"  [CORRUPTO] {name}: {ch!r} ... {ctx!r}")
        print(f"  {len(problems)} fragmentos corruptos. ABORTADO.")
        if strict:
            raise SystemExit(1)
    return len(problems)


def write(path, titulo="Ingles"):
    root = Deck(DECK_ROOT, titulo)
    pkg = Package([root] + _ALL_DECKS)
    for m in MODELS:
        root.add_model(m)
    for d in _ALL_DECKS:
        for note in d.notes:
            note.fields = [sanitize(f) for f in note.fields]
    pkg.write_to_file(path)
    n_notes = sum(len(d.notes) for d in _ALL_DECKS)
    return n_notes, n_notes, _ALL_DECKS
