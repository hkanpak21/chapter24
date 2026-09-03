---
title: "Chinchilla Scaling: A Replication Attempt"
type: source
date_ingested: 2026-08-22
authors: [Tamay Besiroglu, Ege Erdil, Matthew Barnett, Josh You]
venue: "arXiv:2404.10102"
venue_evidence: "https://arxiv.org/abs/2404.10102; Epoch AI blog post, no refereed venue found by web search as of 2026-09-03"
year: 2024
tags: [learning-theory, evaluation-methodology, sample-complexity]
claim_quantifier: empirical
antecedent: "The data are reconstructed from the published figure of Hoffmann et al. rather than obtained from the authors, so every conclusion is conditional on the fidelity of that reconstruction, which the paper describes and defends."
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: none
cls_party: none
cls_unit: none
cls_tightness: unstated
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed:
cls_evidence: absent
cls_evidence_src: "a refit of another paper's parametric loss model; no party's resources are bounded anywhere in it"
cls_reason: "An empirical replication of the Chinchilla estimate. It bounds nobody, and its subject is whether a published fit describes its own data."
cls_prov: S
cls_date: 2026-08-27
---

## Summary

The paper reconstructs the dataset behind the third estimation approach of
[Chinchilla](chinchilla-compute-optimal.md) from its published figure and refits the
parametric loss model. The refitted model differs substantially from the printed
one, the printed fit fails to describe the reconstructed data, and the paper
argues the printed confidence intervals could not have come from a proper
statistical procedure at that sample size. The equal-scaling conclusion of
Hoffmann et al.\ survives; the specific fitted constants of the third approach do
not.

## Claim Boundary

- **Quantified over:** one estimation approach (Approach 3) of one paper, refit on
  reconstructed data.
- **Antecedent:** fidelity of the data reconstruction from the published figure.
- **Does not establish:** that compute-optimal equal scaling of parameters and
  data is wrong. The paper is explicit that its own refit is consistent with the
  20-tokens-per-parameter rule and with the other two approaches.
- **Abstract vs theorem:** none found; the abstract states the finding at the
  strength the body supports.

## Key Contributions

- A refit of the Approach 3 parametric loss model on data reconstructed from the
  published figure, differing substantially from the printed fit.
- The statistical argument that the printed confidence intervals are, verbatim,
  "implausibly tight and unlikely to be obtained from proper statistical
  procedures given the size of their dataset."
- The observation that the printed fit "implies a scaling policy that is
  inconsistent with their other approaches and their 20 tokens-per-parameter
  rule-of-thumb."

## Connections

- [Chinchilla](chinchilla-compute-optimal.md), whose Limits section records this
  dispute together with the reconciliation analysis of Porian et al.

## Open Questions / Limitations

- The reconstruction, not the original data, carries the refit.
- The dispute concerns constants, not the form of the law.

## Quotes / Notable Passages

Verified against `raw/Bes24_ChinchillaReplication.pdf` on 2026-08-22.

> "the confidence intervals reported by Hoffmann et al. are implausibly tight and unlikely to be obtained from proper statistical procedures given the size of their dataset"

> "inconsistent with their other approaches and their 20 tokens-per-parameter rule-of-thumb"
