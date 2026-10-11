# YGFJ18

Samuel Yeom and Irene Giacomelli and Matt Fredrikson and Somesh Jha. Privacy Risk in Machine Learning: Analyzing the Connection to Overfitting. CSF 2018.

The full reading note is the wiki source page, which holds the summary, the
claim boundary, the quotations and the classification evidence:

    wiki/sources/privacy-risk-overfitting.md

This file exists so a claim in `lib/claims.yml` that positions against YGFJ18
can be traced from inside the project. It repeats nothing the wiki page holds.

## How the classification codes it

| Field | Value |
| --- | --- |
| party | none |
| unit | none |
| tightness | unstated |
| baseline | stated |
| assessed |  |
| claim quantifier | conditional |
| antecedent | Each theorem carries its own hypothesis, named separately: Theorem 1 assumes the learning algorithm is epsilon-differentially private; Theorem 2 assumes the loss is bounded by B; Theorem 3 assumes the residual is Gaussian with known variances under both worlds; Theorem 4 assumes an ARO-stable learning rule, a bounded loss, a finite domain, keyed pseudorandom functions, and that x uniquely determines (x,y); Theorem 5 assumes a uniform binary sensitive attribute and Gaussian residuals. |

The row is in `lab/results/corpus-classification/classification.tsv`.
