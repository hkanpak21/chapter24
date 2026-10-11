# SSEP24

Avital Shafran and Ilia Shumailov and Murat A. Erdogdu and Nicolas Papernot. Beyond Labeling Oracles: What does it mean to steal ML models?. TMLR 2024.

The full reading note is the wiki source page, which holds the summary, the
claim boundary, the quotations and the classification evidence:

    wiki/sources/beyond-labeling-oracles.md

This file exists so a claim in `lib/claims.yml` that positions against SSEP24
can be traced from inside the project. It repeats nothing the wiki page holds.

## How the classification codes it

| Field | Value |
| --- | --- |
| party | none |
| unit | none |
| tightness | unstated |
| baseline | absent |
| assessed |  |
| claim quantifier | empirical |
| antecedent | For the negative cost conclusion: that the victim controls the informativeness of its OOD responses (the authors' own hybrid-model instrumentation V_h), and that commercial labeling prices are those quoted in §3.2. Neither is known to hold of deployed systems — the instrumentation is the authors' construction, not a shipped defence. |

The row is in `lab/results/corpus-classification/classification.tsv`.
