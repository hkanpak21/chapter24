#!/bin/bash
# Hidden sparse parity, step count against input dimension. Parked: no section
# of the paper uses the result. Seeds are fixed inside sparse_parity.py.
set -e
cd "$(dirname "$0")/../.."
python3 lab/src/sparse_parity.py --k 3 --dims 20,30,40,50,60 --seeds 8 \
        --batch 128 --lr 0.01 --width 100 --threshold 0.90 \
        --out lab/results/sparse-parity/canonical_b128.json
python3 lab/src/plot_parity.py lab/results/sparse-parity/canonical_b128.json \
        --out paper/figures/parity-scaling.pdf
