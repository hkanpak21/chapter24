#!/bin/bash
# Runs every mechanical gate and prints a pass or fail line for each.
cd "$(dirname "$0")/.." || exit 1
T=../../.tools/tectonic
pass(){ printf "  PASS  %s\n" "$1"; }
fail(){ printf "  FAIL  %s  (%s)\n" "$1" "$2"; }

n=$(python3 tools/collect-cls.py 2>&1 | grep -oE "classified: [0-9]+" | grep -oE "[0-9]+")
tot=$(ls ../../wiki/sources/*.md 2>/dev/null | wc -l | tr -d ' ')
[ "$n" = "$tot" ] && pass "G1 every work classified ($n/$tot)" || fail "G1 every work classified" "$n of $tot"

blank=$(python3 -c "
import csv;R=list(csv.DictReader(open('notes/classification.tsv',encoding='utf-8'),delimiter='\t'))
print(sum(1 for r in R if r['party']!='none' and not r['assessed']))")
[ "$blank" = "0" ] && pass "G3 assessed complete" || fail "G3 assessed complete" "$blank blank rows"

$T -X compile main.tex --outdir . >/dev/null 2>&1
$T -X compile supplementary.tex --outdir . >/dev/null 2>&1
u=$(pdftotext main.pdf - | grep -c "??"); q=$(pdftotext supplementary.pdf - | grep -c "\[?\]")
[ "$u" = "0" ] && [ "$q" = "0" ] && pass "G5 both documents build clean" || fail "G5 build" "$u unresolved, $q bad citations"

e=$(python3 ~/.claude/skills/research/scripts/lint.py --paper sections/00-abstract.tex sections/01-introduction.tex sections/02-problem.tex sections/03-preliminaries.tex sections/04-methodology.tex sections/05-reading.tex sections/06-literature.tex sections/07-findings.tex sections/08-related.tex sections/09-conclusion.tex 2>&1 | grep -oE "^[0-9]+ error" | grep -oE "^[0-9]+")
[ "$e" = "0" ] && pass "G6 prose lint" || fail "G6 prose lint" "$e errors"

f=$(python3 ~/.claude/skills/research/scripts/figfont.py check figures/sankey-corpus.pdf --target 8 2>&1 | grep -oE "^[0-9]+ of" | grep -oE "^[0-9]+")
[ "$f" = "0" ] && pass "G7 figure fonts" || fail "G7 figure fonts" "$f spans off"

b=$(python3 ~/.claude/skills/research/scripts/lint.py --bib refs.bib 2>&1 | grep -oE "^[0-9]+ error" | grep -oE "^[0-9]+")
[ "$b" = "0" ] && pass "G8 bibliography" || fail "G8 bibliography" "$b errors"

tp=$(python3 -c "
import subprocess,re
t=subprocess.run(['pdftotext','main.pdf','-'],capture_output=True,text=True).stdout
p=t.split(chr(12))
for i,x in enumerate(p,1):
    if re.search(r'^\[1\]',x,re.M): print(i-1); break
else: print(len(p))")
[ "$tp" -le 13 ] && pass "G9 text within 13 pages ($tp)" || fail "G9 text length" "$tp pages"
