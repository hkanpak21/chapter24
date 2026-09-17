# BCH22

Borja Balle and Giovanni Cherubin and Jamie Hayes. Reconstructing Training Data with Informed Adversaries. IEEE S\&P 2022.

The full reading note is the wiki source page, which holds the summary, the
claim boundary, the quotations and the classification evidence:

    wiki/sources/reconstructing-informed-adversaries.md

This file exists so a claim in `lib/claims.yml` that positions against BCH22
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
| antecedent | For the theory: the mechanism satisfies (alpha, epsilon)-Renyi DP (Theorem 2), epsilon-DP (Corollary 3) or rho-zCDP (Corollary 4); the adversary's side knowledge is exactly a prior pi over Z; the target is drawn Z ~ pi; and the bound is stated relative to a fixed error function l and threshold eta. For the converse (Theorem 5), the mechanism must be reconstruction robust simultaneously against every prior supported on a pair of points, under the 0/1 error. For the attacks: the adversary knows all training points but one, the model weights, and the training algorithm including hyper-parameters and, by default, the initialization. |

The row is in `lab/results/corpus-classification/classification.tsv`.
