"""Linter del contenido: detecta caracteres corruptos, typos y datos dudosos
en los modulos de content/ antes de generar el .apkg.

Uso: .venv/bin/python lint.py
"""
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, "content")

# caracteres no latinos que casi siempre son basura (CJK, cirilico, etc.)
SUSPECT = re.compile(r"[\u0400-\u04FF\u4E00-\u9FFF\u3040-\u30FF\u0600-\u06FF]")

# token latino/ingles pegado a otro (bug de tecleo al escribir deprisa)
GLUED = re.compile(r"\b(?:[A-Za-z]*(?:se|to|in|at|de|el|la|los|las|un|una)[A-Z][A-Za-z]{2,})\b")

# palabras que en este proyecto siempre están mal escritas
TYPOS = [
    (r"\bsilaba\b", "sílaba"),
    (r"\bsilabas\b", "sílabas"),
    (r"\bingles\b", "inglés"),
    (r"\bIngles\b(?!::)", "Inglés"),
    (r"\bmas\b(?!\s+(?:de|o|a|que)\b)", "más"),
    (r"\bnumero\b", "número"),
    (r"\bdespues\b", "después"),
    (r"\bsegun\b", "según"),
    (r"\btambien\b", "también"),
    (r"\bdemas\b", "demás"),
    (r"\btambien\b", "también"),
    (r"\bhabia\b", "había"),
    (r"\bseria\b", "sería"),
    (r"\bahi\b", "ahí"),
    (r"\basi\b", "así"),
    (r"\bsolo\b(?!)", "solo"),  # aviso, no error
]

ALLOWED_NON_ASCII = set("áéíóúüñÁÉÍÓÚÜÑ¿¡ºª…“”‘’–—→↳·«»✓✔°≠ː±ˈθðŋʃʒɒəʊɑːiːɜːæʌʌtʃdʒ↔")


def check(path):
    src = open(path, encoding="utf-8").read()
    problems = []

    for i, line in enumerate(src.splitlines(), 1):
        m = SUSPECT.search(line)
        if m:
            problems.append((i, "caracter no latino: %r" % m.group(0)))
        for ch in line:
            if ord(ch) > 127 and ch not in ALLOWED_NON_ASCII:
                if not ch.isprintable():
                    continue
                nm = unicodedata.name(ch, "?")
                if "LATIN" not in nm and "SPACE" not in nm:
                    problems.append((i, "unicode raro: %r (%s)" % (ch, nm)))
        for g in GLUED.finditer(line):
            problems.append((i, "posible palabra pegada: %r" % g.group(0)))
        for pat, good in TYPOS:
            if pat.endswith("(?!)"):
                continue
            if re.search(pat, line):
                problems.append((i, "typo: %s  ->  %s" % (pat, good)))
    return problems


def main():
    total = 0
    for f in sorted(os.listdir(CONTENT)):
        if not f.endswith(".py") or f == "__init__.py":
            continue
        p = os.path.join(CONTENT, f)
        probs = check(p)
        print(f"\n{f}  ({len(probs)} avisos)")
        for ln, msg in probs:
            print(f"   L{ln}: {msg}")
        total += len(probs)
    print(f"\n{'='*50}\nTOTAL: {total} avisos")
    return total


if __name__ == "__main__":
    sys.exit(0 if main() == 0 else 1)
