# LLW19

Rio LaVigne and Andrea Lincoln and Virginia Vassilevska Williams. Public-Key Cryptography in the Fine-Grained Setting. CRYPTO 2019.

The full reading note is the wiki source page, which holds the summary, the
claim boundary, the quotations and the classification evidence:

    wiki/sources/pkc-fine-grained-setting.md

This file exists so a claim in `lib/claims.yml` that positions against LLW19
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
| antecedent | The strong Zero-k-Clique-R hypothesis (an average-case search hypothesis stated in this paper), or the Random Edge Zero-k-Clique hypothesis which implies it. Non-standard: these are average-case fine-grained hypotheses, not standard cryptographic assumptions. |

The row is in `lab/results/corpus-classification/classification.tsv`.
