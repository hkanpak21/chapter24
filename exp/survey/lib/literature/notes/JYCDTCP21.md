# JYCDTCP21

Hengrui Jia and Mohammad Yaghini and Christopher A. Choquette-Choo and Natalie Dullerud and Anvith Thudi and Varun Chandrasekaran and Nicolas Papernot. Proof-of-Learning: Definitions and Practice. IEEE S\&P 2021.

The full reading note is the wiki source page, which holds the summary, the
claim boundary, the quotations and the classification evidence:

    wiki/sources/proof-of-learning.md

This file exists so a claim in `lib/claims.yml` that positions against JYCDTCP21
can be traced from inside the project. It repeats nothing the wiki page holds.

## How the classification codes it

| Field | Value |
| --- | --- |
| party | attacker |
| unit | time |
| tightness | relative |
| baseline | absent |
| assessed | explicit |
| claim quantifier | conditional |
| antecedent | The compute-comparison claim rests on the paper's own Conjecture 1, which the authors state because they are \"not aware of a mechanism to prove this formally.\" The two actual theorems (entropy growth, reverse entropy growth) assume i.i.d. hardware/library noise `z` in the training process; the paper notes counter-based PRNGs can remove that noise, voiding the assumption. Nothing rests on a standard complexity assumption. |

The row is in `lab/results/corpus-classification/classification.tsv`.
