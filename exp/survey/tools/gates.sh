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

if python3 tools/check-numbers.py >/dev/null 2>&1; then pass "G4 no stale numbers"; else fail "G4 no stale numbers" "$(python3 tools/check-numbers.py 2>&1 | head -1)"; fi

$T -X compile main.tex --outdir . >/dev/null 2>&1
$T -X compile supplementary.tex --outdir . >/dev/null 2>&1
u=$(pdftotext main.pdf - | grep -c "??"); q=$(pdftotext supplementary.pdf - | grep -c "\[?\]")
[ "$u" = "0" ] && [ "$q" = "0" ] && pass "G5 both documents build clean" || fail "G5 build" "$u unresolved, $q bad citations"

e=$(python3 ~/.claude/skills/research/scripts/lint.py --paper sections/00-abstract.tex sections/01-introduction.tex sections/02-problem.tex sections/03-preliminaries.tex sections/04-methodology.tex sections/05-reading.tex sections/06-literature.tex sections/07-findings.tex sections/08-related.tex sections/09-conclusion.tex 2>&1 | grep -oE "^[0-9]+ error" | grep -oE "^[0-9]+")
[ "$e" = "0" ] && pass "G6 prose lint" || fail "G6 prose lint" "$e errors"

f=$(python3 ~/.claude/skills/research/scripts/figfont.py check figures/sankey-corpus.pdf --target 8 2>&1 | grep -oE "^[0-9]+ of" | grep -oE "^[0-9]+")
[ "$f" = "0" ] && pass "G7 figure fonts" || fail "G7 figure fonts" "$f spans off"

q=$(QUOTE_TXT_DIR=${QUOTE_TXT_DIR:-/tmp/quote-txt} python3 tools/check-quotes.py 2>&1 | grep -oE "belonging to another paper  : [0-9]+" | grep -oE "[0-9]+$")
[ "$q" = "0" ] && pass "G11 no quote attributed to the wrong paper" || fail "G11 quote attribution" "$q transposed"

bl=$(python3 -c "
import glob,re
u=0
for f in glob.glob('../../wiki/sources/*.md'):
    s=open(f,encoding='utf-8').read()
    m=re.search(r'^cls_baseline:[ \t]*(.*)\$',s,re.M)
    if m and m.group(1).strip()!='n/a' and not re.search(r'^cls_baseline_checked:[ \t]*yes',s,re.M): u+=1
print(u)")
[ "$bl" = "0" ] && pass "G2 baseline re-checked" || fail "G2 baseline re-checked" "$bl rows outstanding"

# TMLR assigns no page numbers, so the checker's page rule is waived for its entries only.
tmlr=$(grep -B6 "journal *= *{TMLR}" refs.bib | grep -oE "@article\{[A-Za-z0-9]+" | sed 's/@article{//' | paste -sd'|' -)
b=$(python3 ~/.claude/skills/research/scripts/lint.py --bib refs.bib 2>&1 | grep ERROR | grep -vE "(${tmlr:-NONE}): a journal entry needs pages" | wc -l | tr -d ' ')
[ "$b" = "0" ] && pass "G8 bibliography" || fail "G8 bibliography" "$b errors"

tp=$(python3 -c "
import subprocess,re
t=subprocess.run(['pdftotext','main.pdf','-'],capture_output=True,text=True).stdout
p=t.split(chr(12))
for i,x in enumerate(p,1):
    if re.search(r'^\[1\]',x,re.M): print(i-1); break
else: print(len(p))")
[ "$tp" -le 13 ] && pass "G9 text within 13 pages ($tp)" || fail "G9 text length" "$tp pages"
