# CCNSTT22

Nicholas Carlini and Steve Chien and Milad Nasr and Shuang Song and Andreas Terzis and Florian Tram{\`e}r. Membership Inference Attacks From First Principles. IEEE S\&P 2022.

The full reading note is the wiki source page, which holds the summary, the
claim boundary, the quotations and the classification evidence:

    wiki/sources/mia-from-first-principles.md

This file exists so a claim in `lib/claims.yml` that positions against CCNSTT22
can be traced from inside the project. It repeats nothing the wiki page holds.

## How the classification codes it

| Field | Value |
| --- | --- |
| party | attacker |
| unit | time |
| tightness | measured |
| baseline | stated |
| assessed | implicit |
| claim quantifier | empirical |
| antecedent | The adversary can train N shadow models on data from the target's distribution, and the per-example loss distributions (in logit scale) under the IN and OUT worlds are approximately Gaussian. Both are constructions of the paper, not properties of the target. |

The row is in `lab/results/corpus-classification/classification.tsv`.
