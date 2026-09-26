# english-grammar

A separate Anki deck: English grammar for Spanish speakers, B1 → C2, in 23
decks. **2544 cards, in Spanish** — it is the language-learning side of the
desk, whereas `algebra-lab/` is in English.

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python build.py                 # -> .apkg
.venv/bin/python lint.py                  # structural check
.venv/bin/python preview.py               # HTML preview
.venv/bin/python importar.py              # import into your collection
```

- `content/c01…c23_*.py` — one module per deck; the deck name, level and tags
  live at the top of each file.
- `content/_base.py` — the card helper and the shared tag scheme.
- `ankilib.py` — `.apkg` writing, deck lookup, the Spanish linter hooks.
- `build.py` — imports every content module and writes the `.apkg`.
- `spanish_check.py` — flags Spanish words left in English cards.
- `replace_deck.py` — swap a deck in place without duplicating notes.

`*.apkg` and `.venv/` are gitignored: both are build output.
