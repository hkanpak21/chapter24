# BRSV17

Marshall Ball and Alon Rosen and Manuel Sabin and Prashant Nalini Vasudevan. Average-Case Fine-Grained Hardness. STOC 2017.

The full reading note is the wiki source page, which holds the summary, the
claim boundary, the quotations and the classification evidence:

    wiki/sources/average-case-fine-grained-hardness.md

This file exists so a claim in `lib/claims.yml` that positions against BRSV17
can be traced from inside the project. It repeats nothing the wiki page holds.

## How the classification codes it

| Field | Value |
| --- | --- |
| party | attacker |
| unit | time |
| tightness | relative |
| baseline | n/a |
| assessed | explicit |
| claim quantifier | conditional |
| antecedent | Worst-case conjectures, each stated for randomized two-sided-error algorithms: the OV conjecture (n^{2-o(1)} for OV_d with d = ω(log n)), the 3SUM conjecture (n^{2-o(1)}), the APSP conjecture (n^{3-o(1)}), the Triangle-Collection conjecture, and SETH. Definition 2, the fine-grained one-way function, has no antecedent because it has no instantiation here: the paper defines it and then shows a barrier (NSETH) to the one construction route it proposes. |

The row is in `lab/results/corpus-classification/classification.tsv`.
