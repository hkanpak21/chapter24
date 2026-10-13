# The project's build. Run `make` here, or `make -C paper` from the project root.
# Tool targets run from the project root, where the scripts expect to start.
ROOT     := ..
TECTONIC := $(abspath $(CURDIR)/../../../.tools/tectonic)

.PHONY: all paper supplement tables figure numbers gates ontology clean

all: paper supplement

paper: main.pdf
supplement: supplementary.pdf

main.pdf: main.tex results.tex refs.bib sections/*.tex tables/*.tex
	$(TECTONIC) -X compile main.tex --outdir .

supplementary.pdf: supplementary.tex tables/04-tables.tex refs.bib
	$(TECTONIC) -X compile supplementary.tex --outdir .

# Regenerate everything the classification feeds.
tables:
	cd $(ROOT) && python3 lab/src/gen-tables.py && python3 lab/src/gen-rowtables.py

figure:
	cd $(ROOT) && python3 paper/figures/src/sankey.py

# results.tex is generated from lib/numbers.csv and never edited by hand.
numbers:
	cd $(ROOT) && python3 ~/.claude/skills/research/scripts/numbers-to-tex.py lib/numbers.csv -o paper/results.tex

gates:
	cd $(ROOT) && bash lab/src/gates.sh

# lib/literature/ontology/onto.tsv and views.md from the coded facts.
ontology:
	cd $(ROOT) && python3 lab/src/merge-onto.py --write

clean:
	rm -f *.aux *.bbl *.blg *.log *.out
