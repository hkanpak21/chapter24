# Acceptance gates: submission-ready for IEEE S&P SoK

Each gate states an observable outcome, the command that checks it, and what the
check must print. A gate is met only when its CHECK prints its EXPECT. Nothing is
reported as done while a gate is unmet, abandoned or deferred.

Run all: `bash tools/gates.sh`

## G1. Every work in the corpus is classified
CHECK: python3 tools/collect-cls.py
EXPECT: classified count equals the number of source pages, no remainder
STATUS: met, 200 of 200, 2026-09-03.

## G2. The baseline column is countable
The field was applied under two readings. Until re-passed, the paper discloses it
rather than counting it.
CHECK: grep -c "cls_baseline_checked: yes" over wiki/sources
EXPECT: every row with cls_baseline other than n/a carries the marker
STATUS: met, 2026-08-27.

## G3. The assessed column is countable
Blank on rows that do bound a party, contradicting its own rule.
CHECK: rows with cls_party != none and empty cls_assessed
EXPECT: 0
STATUS: met, 2026-08-27.

## G4. No number in the paper is stale
Every macro in results.tex is recomputed from the classification after any change.
CHECK: python3 tools/check-numbers.py
EXPECT: all macros match a recomputed value
STATUS: met. tools/check-numbers.py covers 70 macros and rewrites results.tex with --write, 2026-09-03.

## G5. Both documents build clean
CHECK: tectonic on main.tex and supplementary.tex, then grep the output
EXPECT: 0 unresolved references, 0 "[?]" citations, both PDFs produced
STATUS: met as of the last build. Recheck after every change.

## G6. Prose passes the linter
CHECK: lint.py --paper over the prose sections, excluding the generated table file
EXPECT: 0 errors
STATUS: met as of the last run. Recheck after every edit.

## G7. Figure fonts match the document
CHECK: figfont.py check figures/sankey-corpus.pdf --target 8
EXPECT: 0 spans outside tolerance
STATUS: met. Recheck after regenerating the figure.

## G8. Bibliography is clean
CHECK: lint.py --bib refs.bib, and a scan for wiki prose in booktitle fields
EXPECT: 0 errors, with the page rule waived for TMLR entries, which carry no pages
STATUS: met, 2026-09-03. Journal entries are @article with volume and pages where the journal assigns them.

## G9. Format matches the call
EXPECT: IEEEtran with options conference,compsoc; text at most 13 pages;
references exempt for SoK; appendix at most 5 pages
STATUS: met. Text is 12 pages, 2026-09-03.

## G10. An adversarial reviewer has read it and its findings are addressed
STATUS: round 1 (2026-08-27) and round 2 (2026-09-03) addressed; round 3 with three personas is owed after the structural work.

## G11. No quotation is attributed to the wrong paper
CHECK: python3 tools/check-quotes.py, bound through raw/SOURCES.md
EXPECT: 0 belonging to another paper
STATUS: met, 2026-09-03, 155 verified in their own document, 5 unbound.
