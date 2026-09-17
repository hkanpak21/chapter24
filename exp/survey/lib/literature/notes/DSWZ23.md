# DSWZ23

Itai Dinur and Uri Stemmer and David P. Woodruff and Samson Zhou. On Differential Privacy and Adaptive Data Analysis with Bounded Space. EUROCRYPT 2023.

The full reading note is the wiki source page, which holds the summary, the
claim boundary, the quotations and the classification evidence:

    wiki/sources/dp-adaptive-analysis-bounded-space.md

This file exists so a claim in `lib/claims.yml` that positions against DSWZ23
can be traced from inside the project. It repeats nothing the wiki page holds.

## How the classification codes it

| Field | Value |
| --- | --- |
| party | mechanism |
| unit | memory |
| tightness | conditional |
| baseline | n/a |
| assessed | explicit |
| claim quantifier | conditional |
| antecedent | Existence of a Gamma(lambda)-secure symmetric-key encryption scheme against non-uniform adversaries, with Omega(lambda) <= Gamma(lambda) <= 2^{o(lambda)}, for the differential privacy separation (Corollary 3.13). Existence of one-way functions for the adaptive data analysis space lower bound (Theorem 4.1, via the same encryption primitive). |

The row is in `lab/results/corpus-classification/classification.tsv`.
