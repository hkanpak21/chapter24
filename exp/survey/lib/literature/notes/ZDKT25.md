# ZDKT25

Jie Zhang and Debeshee Das and Gautam Kamath and Florian Tram{\`e}r. Position: Membership Inference Attacks Cannot Prove that a Model Was Trained On Your Data. IEEE SaTML 2025.

The full reading note is the wiki source page, which holds the summary, the
claim boundary, the quotations and the classification evidence:

    wiki/sources/mia-cannot-prove-training.md

This file exists so a claim in `lib/claims.yml` that positions against ZDKT25
can be traced from inside the project. It repeats nothing the wiki page holds.

## How the classification codes it

| Field | Value |
| --- | --- |
| party | auditor |
| unit | time |
| tightness | unstated |
| baseline | absent |
| assessed | implicit |
| claim quantifier | conditional |
| antecedent | The model developer's training set D and training procedure Train are unknown, AND the verifier cannot efficiently retrain the model. Asserted as a fact about production foundation models; not measured, not proved. |

The row is in `lab/results/corpus-classification/classification.tsv`.
