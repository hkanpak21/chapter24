TECTONIC := ../../.tools/tectonic
MAIN     := main.tex
PDF      := main.pdf

.PHONY: all clean

all: $(PDF)

$(PDF): $(MAIN) results.tex refs.bib sections/*.tex
	$(TECTONIC) -X compile $(MAIN) --outdir .

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.fls *.fdb_latexmk *.synctex.gz
