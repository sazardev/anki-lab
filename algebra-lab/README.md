# Algebra Lab

Infinite practice for factoring, systems of equations, and linear algebra.
Problems are generated on the fly, graded automatically, and come with worked steps.

## Start here

| if you want | do this |
|---|---|
| the **rules**, rendered | menu -> Math -> *Algebra Rules Bible* |
| **practice**, graded | `./run.sh` then `practice('factoring')` |
| practice in the terminal | `./run.sh factoring --practice` |
| rules under time pressure | menu -> Math -> *Anki* |

```bash
./run.sh              # opens the notebook (Jupyter) in your browser
./run.sh test         # quick sanity check, prints 5 problems
```

## The cheatsheet

`CHEATSHEET.md` is the full reference. `md2html.py` renders it to
`cheatsheet.html` with **MathJax bundled locally** in `mathjax/`, so it works
with no internet and no app to learn. Regenerate after editing the Markdown:

```bash
/usr/bin/python3 md2html.py
```

Or from the terminal, graded drill:

```bash
./run.sh factoring --practice     # loops until you stop
./run.sh systems -n 5             # 5 problems with answers, no typing
./run.sh eigen --practice
./run.sh random -n 10 -s 42       # -s makes a repeatable set
```

## In the notebook

| call | what it does |
|---|---|
| `practice('factoring')` | graded drill, one problem at a time |
| `drill('systems', 5)` | print 5 problems + answers, no input |
| `selftest('random', 200)` | verify the generators still work |
| `menu()` | pick a topic interactively |
| `seed(42)` | fix the random seed |

Topics: `factoring`, `systems`, `gauss`, `eigen`, `det`, `random`.

## Typing answers

- `^` for powers: `x^2`
- `*` optional: `5x^2(6x+4)` and `(2x - 3)(5x - 3)` both work
- systems: `x=2, y=-1`
- eigenvalues: `lam=3, lam=-1, v=[1,2]`
- no/infinite solutions: type `no solution` or `infinitely many`
- while answering: `hint`, `skip`, `answer`, `q` to quit

## What gets generated

**Factoring** — greatest common factor, difference of squares, perfect square
trinomials, `x^2+bx+c`, `ax^2+bx+c` (split the middle term), grouping.

**Systems** — 2x2 and 3x3, including inconsistent (no solution) and dependent
(infinitely many) systems. Always clean integer answers.

**Gauss-Jordan** — row reduction with every operation recorded, then the
solution read off the RREF.

**Eigenvalues** — 2x2, always real integers (complex roots are filtered out),
plus eigenvectors from the null space.

**Determinants** — 3x3 by cofactor expansion along the first row.

## Design notes

- Factoring answers are graded by **polynomial equality**, not by matching the
  factorisation the generator happened to use. A different factorisation that
  expands to the same thing is accepted.
- Eigenvalue problems never have complex roots, and system solutions are always
  integers, so every answer is hand-checkable.
- `algebra_lab.py` is standalone — the notebook is a thin layer on top of it.

## Install

The bundled `.venv` already works. To install system-wide instead:

```bash
sudo pacman -S jupyter-notebook python-sympy python-numpy python-matplotlib maxima geogebra
sudo pacman -S anki     # spaced repetition for the rules
```

`geogebra` is the visual companion — build a matrix as a transformation and watch
it act on a vector. Java 17 is already required and already installed.

## Menu de Omarchy

Presiona la tecla del menú y entra en **Math**:

| entrada | qué hace |
|---|---|
| Algebra Lab (Jupyter) | servidor + navegador, apuntando al notebook |
| Terminal drill | los mismos generadores sin navegador |
| Rules reference | este README en tu editor |
| Anki | 511 de ciencia, más álgebra y los mazos de español || GeoGebra | visual: matrices como transformaciones |
| Maxima | CAS para contrastar SymPy |

## Anki

Mazo **`Algebra Lab`**: **269 tarjetas**, 100+ tags, LaTeX real (MathJax).

Cada tarjeta es de uno de tres tipos, filtrables:

| tag |Significado | nº |
|---|---|---|
| `q::what` | **qué es** esto | 43 |
| `q::do` | **qué hace** / cuándo usarlo | 95 |
| `q::how` | **cómo se resuelve** | 97 |
| `q::pitfall` | el error típico | 34 |

Topics: `arithmetic::*`, `algebra::fractions::*`, `algebra::exponents::*`,
`algebra::radicals::*`, `algebra::logs::*`, `factoring::*` (8 métodos),
`quadratics::*`, `systems::*`, `inequalities::*`, `functions::*`,
`geometry::*`, `sequences::*`, `vectors::*`, `matrices::*`, `la::*`,
`tricks::*`, `notation`.

**Empieza por** `tag:factoring::ac-trick tag:q::how` y
`tag:factoring::gcf tag:q::how` — es lo que dijiste que no dominabas.

Para regenerar tras editar `anki_cards.py`:

```bash
/usr/bin/python3 anki_cards.py     # idempotente: no duplica
```

## Mazos por materia

**511 tarjetas** en 41 mazos jerárquicos, en inglés, LaTeX real. Cada tarjeta
lleva un tag de tipo (`q::what`, `q::do`, `q::how`, `q::pitfall`, `q::why`) y
otro de tema (`qm::schrodinger`, `qc::grover`, `cs::big-o`, `sci::statistics`…),
así que se pueden filtrar por cualquiera de los dos ejes.

| raíz | tarjetas | contenido |
|---|---|---|
| `Physics::*` | 252 | 15 mazos: matemática, mecánica (7), ondas, térmica, EM, óptica, relatividad, atómica, intro cuántica |
| `QM::*` | 96 | 8 mazos: fundamentos, álgebra lineal, Schrödinger, potenciales, momento angular, átomos, partículas idénticas, aproximaciones |
| `CS::*` | 69 | 9 mazos: complejidad, algoritmos, estructuras, lenguajes, SO, concurrencia, redes, bases de datos, seguridad, ML |
| `QC::*` | 64 | 6 mazos: qubits, entanglement, circuitos, algoritmos, recursos, corrección de errores |
| `Science::*` | 30 | 3 mazos: método, medida, estadística |

Mazos de `Physics::` en detalle:

| mazo | nº | mazo | nº |
|---|---|---|---|
| `Physics::Math` | 17 | `Physics::Thermal` | 24 |
| `Physics::Mechanics::Kinematics` | 18 | `Physics::EM` | 29 |
| `Physics::Mechanics::Newton` | 20 | `Physics::Optics` | 16 |
| `Physics::Mechanics::Energy` | 15 | `Physics::Relativity` | 18 |
| `Physics::Mechanics::Momentum` | 14 | `Physics::Atomic` | 11 |
| `Physics::Mechanics::Rotation` | 16 | `Physics::Quantum-Intro` | 12 |
| `Physics::Mechanics::Gravitation` | 15 | `Physics::Waves` | 14 |
| `Physics::Mechanics::Oscillations` | 13 | | |

### Ficheros y generadores

`cards_physics_a.json` y `cards_physics_b.json` se escribieron a mano (física).
Los otros cuatro se **generan**, y el generador es la fuente de la verdad:

```bash
/usr/bin/python3 build_cards_qm.py                 # -> cards_qm.json
/usr/bin/python3 build_cards_quantum_computing.py  # -> cards_quantum_computing.json
/usr/bin/python3 build_cards_computing.py          # -> cards_computing.json
/usr/bin/python3 build_cards_science.py            # -> cards_science.json
```

`cards_lib.py`_normaliza el LaTeX al escribir (ver la sección de trampas).
Regenera siempre antes de `--load`.

### Regenerar y validar

```bash
/usr/bin/python3 anki_decks.py --check    # valida, no escribe nada
/usr/bin/python3 anki_decks.py --stats    # recuento por mazo
/usr/bin/python3 anki_decks.py --load     # idempotente: 0 new / 0 upd la 2ª vez
```

`--load` lee **todos** los `cards_*.json`. Cierra Anki antes: si la colección
está bloqueada el script aborta en vez de corromperla. Hace copia de seguridad
en `collection.anki2.antes-de-importar.bak`.

### Trampas que MathJax falla en silencio

`--check` rechaza las cuatro, porque ninguna produce error en ninguna
herramienta: se ven bien en el JSON y en Anki, y solo se rompen al renderizar.

- **HTML dentro de `\(...\)`**: `<b>` dentro de una fórmula no se renderiza.
  Las etiquetas van fuera del delimitador.
- **`<` crudo**: los campos de Anki son HTML, así que `0<x<L` se parsea como
  una etiqueta y destruye la fórmula. Dentro de math va `&lt;`.
- **Backslash doble**: `r"\\("` deja dos backslashes y MathJax ya no ve el
  delimitador. En raw strings escribe `\(`; `cards_lib.norm()` lo colapsa por
  si acaso, y el validador avisa.
- **Entornos**: `pmatrix` y compañía necesitan `\\` (exactamente dos) como
  separador de fila, y `&` como separador de columnas; por eso los entornos
  están en la lista de exenciones del chequeo de `&`.

Además balancea delimitadores `\(` `\)` `\[` `\]`, llaves, entornos `aligned`/
`cases`/`bmatrix`/`array`/`vmatrix`/`pmatrix`, `&` sueltos y fronts repetidos.

### Verificación usada

- **1101/1101** expresiones renderizadas en Chromium con MathJax, 0 `mjx-merror`.
- **64/64** afirmaciones numéricas de los mazos nuevos recalculadas.
- **67/67** de `cards_physics_b.json` y **24/24** de `cards_physics_a.json`.
- 0 fronts duplicados entre los 41 mazos.

`anki_preview.py` regenera el volcado visual y repite la comprobación de
renderizado, que es la única forma de detectar un fallo silencioso de MathJax:

```bash
/usr/bin/python3 anki_preview.py            # anki_preview.html + chequeo
/usr/bin/python3 anki_preview.py --open     # y abrirlo en el navegador
```

## Nota sobre Jupyter

`~/.jupyter/jupyter_server_config.py` deja el token vacío a propósito. El
servidor escucha **solo en 127.0.0.1**, así que no es accesible desde la red;
eso permite que el lanzador construya la URL del notebook sin leer el token del
log. Si alguna vez cambias `ServerApp.ip` a `0.0.0.0`, vuelve a poner un token.
