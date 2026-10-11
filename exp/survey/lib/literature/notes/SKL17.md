# SKL17

Jacob Steinhardt and Pang Wei Koh and Percy Liang. Certified Defenses for Data Poisoning Attacks. NeurIPS 2017.

The full reading note is the wiki source page, which holds the summary, the
claim boundary, the quotations and the classification evidence:

    wiki/sources/certified-defenses-data-poisoning.md

This file exists so a claim in `lib/claims.yml` that positions against SKL17
can be traced from inside the project. It repeats nothing the wiki page holds.

## How the classification codes it

| Field | Value |
| --- | --- |
| party | attacker |
| unit | corruption |
| tightness | budget |
| baseline | absent |
| assessed | explicit |
| claim quantifier | conditional |
| antecedent | Two assumptions the paper states and does not verify: that the dataset is large enough for statistical concentration between train and test error to hold, and that outliers within the clean data do not have a strong effect on the model. The defender is further restricted to outlier removal followed by minimisation of a margin-based loss. The bound is described by the authors as approximate, not exact. |

The row is in `lab/results/corpus-classification/classification.tsv`.
