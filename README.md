# anki-lab

A study desk for math and science, built around **Anki**: 511 verified
flashcards across 41 hierarchical decks, an algebra drill lab with real CAS
backing, and an Omarchy menu so the whole thing is two keystrokes away.

Everything here is plain text you can read, edit and diff. The cards live in
JSON or in a Python generator, never in a binary blob.

```
511 cards   Physics 252 · QM 96 · CS 69 · QC 64 · Science 30
1101        formulas, every one rendered and counted by a headless browser
41          hierarchical decks, 0 duplicate fronts
```

---

## Contents

| path | what it is |
|---|---|
| `algebra-lab/` | the deck system, the algebra drill lab, the cheatsheet |
| `english-grammar/` | a separate 2544-card B1–C2 English grammar deck (Spanish-language cards) |
| `setup/` | Omarchy menu extension, launchers, Jupyter config |
| `install.sh` | one-shot, re-runnable installer |
| `.github/workflows/` | re-validates and re-renders on every push |

## Install

```bash
git clone https://github.com/sazardev/anki-lab.git
cd anki-lab

./install.sh --check     # dry run: prints what it would do
./install.sh             # menu + launchers + jupyter config
./install.sh --decks     # ...and import the 511 cards (asks first)
```

On Arch/Omarchy the Python side wants:

```bash
omarchy install app 'Math Lab' 'jupyter-notebook python-sympy python-numpy python-matplotlib'
sudo pacman -S anki
```

Then `omarchy menu summon math`.

Cloning somewhere else? `LAB_DIR=/path/to/anki-lab ./install.sh`, or set
`ALGEBRA_LAB_DIR` in your shell and the menu entries follow it.

---

## The decks

All content is **English**, LaTeX-rendered by Anki's built-in MathJax
(`Ctrl+M` in the editor). Cards are retrieval prompts — "compare X and Y",
"what breaks if…" — not definitions to reread.

Two tag axes, so you can slice either way:

- **type**: `q::what`, `q::do`, `q::how`, `q::pitfall`, `q::why`
- **topic**: `qm::schrodinger`, `qc::grover`, `cs::big-o`, `sci::statistics`…

| root | cards | decks |
|---|---|---|
| `Physics::*` | 252 | maths, mechanics (7), waves, thermal, EM, optics, relativity, atomic, quantum intro |
| `QM::*` | 96 | foundations, Hilbert-space formalism, Schrödinger, potentials, angular momentum, atoms, identical particles, approximations |
| `CS::*` | 69 | complexity, algorithms, data structures, languages, OS, concurrency, networking, databases, security, ML |
| `QC::*` | 64 | qubits, entanglement, circuits, algorithms, resources, error correction |
| `Science::*` | 30 | scientific method, measurement, statistics |

### The decks are generated

Four of the five are **generated**; the generator is the source of truth:

```bash
cd algebra-lab
python3 build_cards_qm.py                 # -> cards_qm.json
python3 build_cards_quantum_computing.py  # -> cards_quantum_computing.json
python3 build_cards_computing.py          # -> cards_computing.json
python3 build_cards_science.py            # -> cards_science.json
```

`cards_physics_a.json` and `cards_physics_b.json` were written by hand.

### Validate and load

```bash
cd algebra-lab
python3 anki_decks.py --check    # validate, writes nothing
python3 anki_decks.py --stats    # per-deck counts
python3 anki_decks.py --load     # idempotent: 0 new / 0 updated on a rerun
```

Close Anki before `--load`; if the collection is locked the script aborts
rather than corrupting it, and it takes a backup first.

---

## Why the validator is so picky

A malformed card does not fail loudly. It looks fine in the JSON, it looks
fine in Anki's editor, and it fails **only when MathJax renders it** — usually
as literal text with no error anywhere. So `anki_decks.py --check` rejects the
four failure modes that are actually silent, and `anki_preview.py` renders the
lot in headless Chromium to prove it:

| trap | symptom | rule |
|---|---|---|
| HTML inside `\(...\)` | the maths vanishes | tags go outside the delimiter |
| raw `<` | `0<x<L` is parsed as an HTML tag and destroys the formula | write `&lt;` |
| doubled backslash | `r"\\("` leaves two, and MathJax no longer sees a delimiter | one backslash; `cards_lib.norm()` collapses strays |
| matrix rows | need exactly `\\` (two) and `&`; four is always a bug | row environments are exempt from the `&` check |

Plus the boring ones: balanced `\(` `\)` `\[` `\]`, braces, `aligned`/`cases`/
`bmatrix`/`array`/`vmatrix`/`pmatrix`, stray `&`, and duplicate fronts.

```bash
python3 anki_preview.py            # writes anki_preview.html and checks it
python3 anki_preview.py --open     # and opens a browser
```

`anki_preview.py` counts `<mjx-container>` elements against the number of
delimiters in the source. A silent MathJax failure shows up as a missing
container, which no amount of JSON linting would catch. That check runs in CI
on every push, along with a check that the committed JSON still matches what
the builders produce.

---

## The algebra lab

`algebra-lab/` is also a standalone drill: 11 generators (factoring with 8
distinct methods, quadratics, systems, inequalities, sequences, vectors,
matrices, linear algebra) backed by SymPy, with every step shown.

```bash
cd algebra-lab
./run.sh              # interactive menu
./run.sh menu         # same, no browser
python3 algebra_lab.py --help
jupyter lab Algebra_Lab.ipynb
```

There is also `CHEATSHEET.md` — an expanded algebra reference that
`omarchy-launch-cheatsheet` renders with LaTeX instead of dumping raw markup
into a text editor.

---

## Adding your own cards

Drop a `cards_anything.json` next to the others and `--check`/`--load` pick it
up automatically:

```json
{
  "decks": {
    "MySubject::Basics": [
      {"f": "front, with \\( \\) inline maths",
       "b": "back, with \\[ \\] display maths",
       "t": "q::what my::topic"}
    ]
  }
}
```

Or add a `build_cards_mysubject.py` and use `cards_lib.write_json`, which
normalises the LaTeX as described above.

---

## Layout notes

- `cards_lib.py` is imported by the generators; it is what keeps `r"\\("` from
  ever reaching a JSON file.
- `fix_physics_json.py` is a one-off repair for the two hand-written physics
  files. Already applied; kept so the normalisation is reproducible.
- `mathjax/` is **not** in the repo (4 MB, third-party). `anki_preview.py`
  and `md2html.py` fall back to the jsDelivr CDN automatically. Drop a local
  copy in `algebra-lab/mathjax/` if you want to work offline.
- Anki's default is 20 new cards/day. Raise the per-deck preset or you will
  only see 20 of the 511.

## Licence

MIT — see [LICENSE](LICENSE).

Card content is factual material (physics, quantum mechanics, computer science,
statistics) and the English-grammar deck teaches a language; all of it is
covered by the MIT licence above. If you fork it, the licences of anything you
add are yours to choose.
