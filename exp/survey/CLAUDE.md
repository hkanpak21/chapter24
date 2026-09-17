# CLAUDE.md — exp/survey

Project root for the SoK. The layout is the `research` skill's: `lab/`, `lib/`,
`paper/`, `sink/`, with `CONTEXT.md` at the root.

**Read `CONTEXT.md` first.** It carries the claim, the terminology ledger, the
symbols and the current state. Nothing here repeats it.

## Where things are

| Path | Holds |
| --- | --- |
| `paper/` | the draft. `main.tex`, `sections/`, generated `tables/` and `results.tex`, `figures/`, `contracts/`, `reviews/sp27/` |
| `lib/claims.yml` | every claim the paper asserts, with its evidence and status |
| `lib/numbers.csv` | every number that reaches the paper. `paper/results.tex` is generated from it |
| `lib/literature/codebook.md` | the thirteen fields, their values, and the rules that decide a row |
| `lib/profs/rulings.md` | the author's rulings, each one a codebook or scope decision |
| `lib/issues/` | open work, one file per issue |
| `lib/reports/archive/` | the record of earlier sessions, kept as history |
| `lab/results/corpus-classification/` | `classification.tsv`, the coded corpus every number comes from |
| `lab/src/` | the generators and checkers |

The literature knowledge base is outside this project, at the repo root `wiki/`,
governed by the repo root `CLAUDE.md`. That file holds the record of refuted
claims. Read it before asserting novelty about anything.

## Build

```bash
make            # both PDFs
make tables     # regenerate paper/tables/ from the classification
make figure     # regenerate paper/figures/sankey-corpus.pdf
make numbers    # regenerate paper/results.tex from lib/numbers.csv
make gates      # every acceptance gate, GATES.md
```

`paper/results.tex` and `paper/tables/*.tex` are generated. Editing either by
hand puts two answers in the repo.

## Rules that hold here

- A number enters the paper through `lib/numbers.csv` and a claim through
  `lib/claims.yml`. `python3 lab/src/check-numbers.py --write` recomputes the
  ledger from the corpus and regenerates `results.tex`.
- The paper proves nothing. Every result is a measurement of the coded corpus,
  and the prose never says otherwise.
- Prose register is `~/.claude/skills/research/references/writing.md`, and the
  venue profile is `references/venues/ieee-sp.md`. The linter runs at every
  commit: `python3 ~/.claude/skills/research/scripts/lint.py --paper paper/sections/*.tex`.
- A quotation enters the paper only after `lab/src/check-quotes.py` binds it to
  its own document. Always `grep -a` on extracted PDF text.
