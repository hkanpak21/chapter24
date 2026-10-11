# DSMMSZTCEH24

Michael Duan and Anshuman Suri and Niloofar Mireshghallah and Sewon Min and Weijia Shi and Luke Zettlemoyer and Yulia Tsvetkov and Yejin Choi and David Evans and Hannaneh Hajishirzi. Do Membership Inference Attacks Work on Large Language Models?. COLM 2024.

The full reading note is the wiki source page, which holds the summary, the
claim boundary, the quotations and the classification evidence:

    wiki/sources/do-mias-work-on-llms.md

This file exists so a claim in `lib/claims.yml` that positions against DSMMSZTCEH24
can be traced from inside the project. It repeats nothing the wiki page holds.

## How the classification codes it

| Field | Value |
| --- | --- |
| party | none |
| unit | none |
| tightness | unstated |
| baseline | stated |
| assessed |  |
| claim quantifier | empirical |
| antecedent | Pretrained LLMs trained on web-scale corpora for approximately one epoch, with members and non-members drawn from the Pile's official train/test split. The near-random result is conditional on both properties; the paper varies each and shows attack performance rises when either is relaxed. |

The row is in `lab/results/corpus-classification/classification.tsv`.
