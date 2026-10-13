# Acceptance gates: submission-ready for IEEE S&P SoK

Each gate states an observable outcome, the command that checks it, and what the
check must print. A gate is met only when its CHECK prints its EXPECT. Nothing is
reported as done while a gate is unmet, abandoned or deferred.

Run all: `make gates`, which is `bash lab/src/gates.sh` from the project root.

## G1. Every work in the corpus is classified
CHECK: `python3 lab/src/collect-cls.py`
EXPECT: classified count equals the number of wiki source pages, no remainder
STATUS: met, 200 of 200, 2026-09-17.

## G2. The baseline column is countable
The field was applied under two readings. Every row was re-read under the
narrower definition before the paper counted it.
CHECK: every `wiki/sources` row with `cls_baseline` other than `n/a` carries `cls_baseline_checked: yes`
EXPECT: 0 outstanding
STATUS: met, 2026-08-27.

## G3. The assessed column is countable
CHECK: rows with `cls_party != none` and empty `cls_assessed`
EXPECT: 0
STATUS: met, 2026-08-27.

## G4. No number in the paper is stale
`lib/numbers.csv` is the ledger of record and `paper/results.tex` is generated
from it. The checker recomputes every macro from the classification and compares
it against the ledger, never against the generated file.
CHECK: `python3 lab/src/check-numbers.py`
EXPECT: all 70 macros match the corpus
STATUS: met, 2026-09-17. `--write` updates the ledger and regenerates `results.tex`.

## G5. Both documents build clean
CHECK: tectonic on `paper/main.tex` and `paper/supplementary.tex`, then grep the output
EXPECT: 0 unresolved references, 0 `[?]` citations, both PDFs produced
STATUS: met, 2026-09-17.

## G6. Prose passes the linter
CHECK: `lint.py --paper paper/sections/*.tex`, with the venue and `CONTEXT.md` loaded
EXPECT: 0 errors
STATUS: met, 2026-09-17. 22 errors before the register pass, 0 after.

## G7. Figure fonts match the document
CHECK: `figfont.py check paper/figures/sankey-corpus.pdf --target 8`
EXPECT: 0 spans outside tolerance
STATUS: met. Recheck after regenerating the figure.

## G8. Bibliography is clean
CHECK: `lint.py --bib paper/refs.bib`, and a scan for wiki prose in booktitle fields
EXPECT: 0 errors, with the page rule waived for TMLR entries, which carry no pages
STATUS: met, 2026-09-03.

## G9. Format matches the call
EXPECT: IEEEtran with options `conference,compsoc`; text at most 13 pages;
references exempt for SoK; 18 pages in total
STATUS: met. Text is 11 pages and the document is 17, 2026-09-17.

## G10. An adversarial reviewer has read it and its findings are addressed
STATUS: unmet. Rounds one (2026-08-27) and two (2026-09-03) are addressed and
filed in `paper/reviews/sp27/`. Round three with three personas is owed after the
structural work. See `lib/issues/2026-09-17-halil-third-review-round-owed.md`.

## G11. No quotation is attributed to the wrong paper
CHECK: `python3 lab/src/check-quotes.py`, bound through `raw/SOURCES.md`
EXPECT: 0 belonging to another paper
STATUS: met, 2026-09-03, 155 verified in their own document, 5 unbound.

## G12. The submission build is anonymous and carries the ethics statement
CHECK: `check-blind.py` against `~/.config/research/blind-patterns`, and the
HotCRP ethics field
EXPECT: 0 identifying strings, ethics answered
STATUS: unmet. See `lib/issues/2026-09-17-halil-title-and-anonymity-fail-the-call.md`.
