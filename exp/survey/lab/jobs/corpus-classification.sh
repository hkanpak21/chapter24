#!/bin/bash
# Rebuild the coded corpus from the wiki front matter, then everything it feeds.
# The wiki page is the authority. classification.tsv is a projection of it.
set -e
cd "$(dirname "$0")/../.."
python3 lab/src/collect-cls.py
python3 lab/src/gen-tables.py
python3 lab/src/gen-rowtables.py
python3 paper/figures/src/sankey.py
python3 lab/src/check-numbers.py --write
