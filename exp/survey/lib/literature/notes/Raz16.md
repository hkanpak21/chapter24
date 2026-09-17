# Raz16

Ran Raz. Fast Learning Requires Good Memory: A Time-Space Lower Bound for Parity Learning. FOCS 2016.

The full reading note is the wiki source page, which holds the summary, the
claim boundary, the quotations and the classification evidence:

    wiki/sources/raz-parity-time-space.md

This file exists so a claim in `lib/claims.yml` that positions against Raz16
can be traced from inside the project. It repeats nothing the wiki page holds.

## How the classification codes it

| Field | Value |
| --- | --- |
| party | learner |
| unit | memory |
| tightness | exponent |
| baseline | n/a |
| assessed | explicit |
| claim quantifier | universal |
| antecedent | none. The bound is unconditional. The only structural hypotheses are that the target is drawn uniformly from {0,1}^n, that samples arrive as a stream and cannot be revisited unless stored, and that the algorithm is modelled as a branching program. |

The row is in `lab/results/corpus-classification/classification.tsv`.
