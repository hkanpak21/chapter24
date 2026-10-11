# BGGKRR26

Sarah Ball and Greg Gluch and Shafi Goldwasser and Frauke Kreuter and Omer Reingold and Guy N. Rothblum. On the Impossibility of Separating Intelligence from Judgment: The Computational Intractability of Filtering for AI Alignment. ICLR 2026.

The full reading note is the wiki source page, which holds the summary, the
claim boundary, the quotations and the classification evidence:

    wiki/sources/filter-impossibility-ai-alignment.md

This file exists so a claim in `lib/claims.yml` that positions against BGGKRR26
can be traced from inside the project. It repeats nothing the wiki page holds.

## How the classification codes it

| Field | Value |
| --- | --- |
| party | auditor |
| unit | time |
| tightness | relative |
| baseline | stated |
| assessed | implicit |
| claim quantifier | existential |
| antecedent | cryptographic hardness (TLPs for Thm 1; OWFs plus an LLM-attacker shared secret for Thm 2; PKE for Thm 3); the LLM is constructed by the proof, not given |

The row is in `lab/results/corpus-classification/classification.tsv`.
