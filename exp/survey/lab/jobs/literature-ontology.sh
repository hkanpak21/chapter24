#!/bin/bash
# The ontology coding run of 2026-10-13. Five agents coded the 200 corpus works
# and the sweep-only works against lib/literature/ontology/schema.tsv, following
# lab/src/briefs/ontology-brief.md, one input list each (input-N.txt), and wrote
# coded-N.tsv into lab/results/literature-ontology/. The agents are not rerun
# by this script. It rebuilds what the coded facts feed.
set -e
cd "$(dirname "$0")/../.."
python3 lab/src/merge-onto.py --write
