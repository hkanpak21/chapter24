# The project root is exp/survey. The paper builds inside paper/.
TECTONIC := $(CURDIR)/../../.tools/tectonic
PAPER    := paper

.PHONY: all paper supplement tables figure numbers gates clean

all: paper supplement

paper: $(PAPER)/main.pdf
supplement: $(PAPER)/supplementary.pdf

$(PAPER)/main.pdf: $(PAPER)/main.tex $(PAPER)/results.tex $(PAPER)/refs.bib $(PAPER)/sections/*.tex $(PAPER)/tables/*.tex
	cd $(PAPER) && $(TECTONIC) -X compile main.tex --outdir .

$(PAPER)/supplementary.pdf: $(PAPER)/supplementary.tex $(PAPER)/tables/04-tables.tex $(PAPER)/refs.bib
	cd $(PAPER) && $(TECTONIC) -X compile supplementary.tex --outdir .

# Regenerate everything the classification feeds.
tables:
	python3 lab/src/gen-tables.py && python3 lab/src/gen-rowtables.py

figure:
	python3 $(PAPER)/figures/src/sankey.py

# results.tex is generated from lib/numbers.csv and never edited by hand.
numbers:
	python3 ~/.claude/skills/research/scripts/numbers-to-tex.py lib/numbers.csv -o $(PAPER)/results.tex

gates:
	bash lab/src/gates.sh

clean:
	rm -f $(PAPER)/*.aux $(PAPER)/*.bbl $(PAPER)/*.blg $(PAPER)/*.log $(PAPER)/*.out
