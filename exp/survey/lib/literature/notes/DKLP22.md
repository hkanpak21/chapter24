# DKLP22

Adam Dziedzic and Muhammad Ahmad Kaleem and Yu Shen Lu and Nicolas Papernot. Increasing the Cost of Model Extraction with Calibrated Proof of Work. ICLR 2022.

The full reading note is the wiki source page, which holds the summary, the
claim boundary, the quotations and the classification evidence:

    wiki/sources/calibrated-proof-of-work-extraction.md

This file exists so a claim in `lib/claims.yml` that positions against DKLP22
can be traced from inside the project. It repeats nothing the wiki page holds.

## How the classification codes it

| Field | Value |
| --- | --- |
| party | attacker |
| unit | time |
| tightness | measured |
| baseline | absent |
| assessed | explicit |
| claim quantifier | empirical |
| antecedent | Users are identifiable and the server keeps per-user state; the defender holds enough training data to build a PATE teacher ensemble whose vote consensus is a usable leakage signal; a reference population of legitimate users exists from which the expected cost curve is fitted; legitimate queries are drawn at random from an in-distribution set unseen by the victim. |

The row is in `lab/results/corpus-classification/classification.tsv`.
