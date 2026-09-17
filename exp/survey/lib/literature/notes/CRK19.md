# CRK19

Jeremy Cohen and Elan Rosenfeld and J. Zico Kolter. Certified Adversarial Robustness via Randomized Smoothing. ICML 2019.

The full reading note is the wiki source page, which holds the summary, the
claim boundary, the quotations and the classification evidence:

    wiki/sources/certified-robustness-randomized-smoothing.md

This file exists so a claim in `lib/claims.yml` that positions against CRK19
can be traced from inside the project. It repeats nothing the wiki page holds.

## How the classification codes it

| Field | Value |
| --- | --- |
| party | attacker |
| unit | perturbation |
| tightness | budget |
| baseline | n/a |
| assessed | explicit |
| claim quantifier | universal |
| antecedent | none. The robustness guarantee is a geometric consequence of Gaussian smoothing via the Neyman-Pearson lemma. No hardness assumption is used. |

The row is in `lab/results/corpus-classification/classification.tsv`.
