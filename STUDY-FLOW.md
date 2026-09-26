# Study flow

The loop, and why it is in that order. This is the one thing worth memorising;
everything else in this repo is a tool for one of the three steps.

**The idea:** you do not learn algebra by reading, you learn it by producing the
answer. Anki keeps the rule; the drill teaches the execution. Skipping the drill
is what makes algebra feel learned when it is not.

## The loop

```
1. REVIEW   ->  Anki, only what is due.         ~5 min
2. DRILL    ->  one method, with --practice.    ~15 min
3. ANCHOR   ->  5 new cards from THAT method.   ~5 min
```

Step 3 is last on purpose. A new card is worth much more right after you solved
a problem of that type — it gets anchored to something concrete. Introduced
first, it stays a loose definition.

Step 1 is maintenance, not learning. Do it quickly and get to step 2.

```bash
cd algebra-lab

# 2. the part that actually teaches: one method, graded
python3 algebra_lab.py factoring -n 15 --practice
./run.sh menu                    # interactive: 1-5, or "r" for random

# 3. then, in Anki, filter to the method you just drilled
#    tag:factoring::gcf  tag:q::pitfall
```

`--practice` is what makes it work. Without it the generator prints the answer
and the steps straight away.

## The gate between methods

**Do not move on until you are around 90% on a method with no hints.** Each
method is a prerequisite for the next, and skipping the GCF shows up later as
the classic "you divided some terms but not others".

Difficulty order, not deck order:

```
GCF -> squares -> perfect square -> grouping
    -> trinomial (monic, then with a) -> ac-trick -> cubes, substitution
```

## The traps

1. **Feeling that you know because you answered cards.** You can answer "when do
   I use the ac-trick?" perfectly and still freeze on a random trinomial.
   Recognising a rule is not executing it. This is why step 2 teaches and step 1
   only maintains.
2. **Reading the cheatsheet.** It is there to unblock you. Section 2 is the
   decision tree ("which method?"), and method selection is the real skill.
3. **Reading the whole solution when stuck.** Look at *one* step of `STEPS`, try
   again, then look at the next.
4. **Doing only Anki.** Without step 2 you will feel fluent and be wrong.

## Linear algebra is a different animal

Order is `gauss -> eigen -> det`, and the **visual** matters more than the
cards: launch GeoGebra from the Math menu and watch a row reduction as a linear
transformation. The `la::*` cards and the `gauss`/`eigen`/`det` generators are
support, not the centre.

## For the other subjects

Physics, QM, QC, CS and Science are card-only, so the loop collapses:

1. Review what is due.
2. Read 2–3 cards *from memory* before revealing — that is what sticks.
3. Add up to 5 new cards.

```bash
python3 study.py status            # what is due, per deck, with a streak
python3 study.py session physics   # the loop, spelled out for that deck
python3 study.py menu              # interactive picker
python3 study.py workspace         # the tiled Hyprland workspace
```

`study.py status` needs Anki closed (it holds the collection lock). When Anki is
running it falls back to the last snapshot from `study.py sync` and says so.

## Deck limits

`python3 set_anki_limits.py` puts these decks on a dedicated config group at 60
new/day, leaving every other deck in the collection alone. Anki's default of 20
would mean 20 of the 511 cards ever appearing.
