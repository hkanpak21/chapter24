---
title: "Computational Lower Bounds in Latent Models: Clustering, Sparse-Clustering, Biclustering"
type: source
date_ingested: 2026-04-23
authors: [Bertrand Even, Christophe Giraud, Nicolas Verzelen]
venue: "Preprint. The ingested PDF is arXiv:2506.13647v1, 16 Jun 2025, and does not state a venue."
year: 2025
tags: [statistical-computational-gaps, low-degree-polynomials, clustering, biclustering, latent-models]
claim_quantifier: universal
antecedent: "none for the lower bounds themselves. Reading them as computational thresholds rests on the low-degree conjecture."
algorithm_class: "low-degree"
date_verified: 2026-08-20
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: algo class
cls_tightness: class
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "We build on the seminal paper of [66] and propose a new scheme to derive lower bounds on the performance of low-degree polynomials in some latent space models."
cls_evidence_src: abstract
cls_reason: "Paper prices a learner restricted to low-degree polynomials solving clustering/sparse-clustering/biclustering, not an ML-security attacker; party=learner and unit=algo class follow rule 3. No attack scenario is present, so target/family/phase/access/write are none/n/a."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper (EGV25) uses **conditioned low-degree techniques** to produce **tight LD lower bounds** for three canonical ML problems:
1. **Gaussian-mixture clustering**
2. **Sparse clustering** (clustering with sparse-mean separation)
3. **Biclustering** (row-column simultaneous clustering in data matrices)

Each bound has a **matching upper bound** via an efficient algorithm, yielding sharp statistical-computational gap characterizations. This is a concrete post-2024 extension of the [Schramm-Wein 2022](low-degree-estimation-schramm-wein.md) low-degree-for-estimation program into canonical ML tasks, complementing [Ding-Hua-Slot-Steurer 2025](ding-low-degree-community-detection.md)'s community-detection analysis.

EGV25 is representative of the 2025-2026 trajectory where the low-degree framework is being systematically applied to practical ML problems: clustering, biclustering, community detection, sparse PCA — giving the field a unified "computational-threshold landscape" for unsupervised learning.

## Claim Boundary

- **Quantified over:** low-degree polynomials for clustering, sparse clustering and biclustering in the latent space models the paper defines.
- **Antecedent:** none for the lower bounds themselves. Reading them as computational thresholds rests on the low-degree conjecture.
- **Algorithm class:** low-degree. The matching upper bounds are explicit polynomial-time algorithms, so the two sides meet inside the low-degree picture rather than proving hardness.
- **Does not establish:** that clustering, sparse clustering or biclustering below the stated thresholds is hard for polynomial time.
- **Abstract vs theorem:** none found. The abstract describes the framework as a way to assess the best performance achievable in polynomial time, which is a prediction rather than a proof.

## Key Contributions

- **Tight LD lower bounds for Gaussian-mixture clustering, sparse clustering, biclustering**.
- **Matching algorithmic upper bounds**: each lower bound paired with a poly-time algorithm achieving it — sharp stat-comp gap characterization.
- **Conditioned LD technique**: conditioning on auxiliary random variables sharpens the LD analysis for latent-model problems.
- **Unified treatment**: three problems analyzed with the same conditioned-LD machinery.

## Connections

- Source: [Low-Degree Polynomials Survey (Wein 2025)](low-degree-polynomials-survey.md).
- Source: [Low-Degree Estimation (SW22)](low-degree-estimation-schramm-wein.md) — foundational estimation LD framework.
- Source: [Ding-Hua-Slot-Steurer 2025 (SBM thresholds)](ding-low-degree-community-detection.md) — companion community-detection analysis.
- Source: [Low-Degree Almost Orthonormal (CGGV25)](low-degree-almost-orthonormal.md) — same Verzelen; complementary technique.
- Source: [Lattice-Based Methods Surpass SOS (ZSWB22)](zadik-lattice-surpass-sos.md) — cautionary counterexample; ZSWB shows some clustering problems escape LD.
- Concept: [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md).
- Concept: [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md).

## Quotes / Notable Passages

> _Not a quotation from the paper. This characterization was carried over from a secondary survey artifact during an earlier ingest and was wrongly presented in quotation marks. Retained unquoted, corrected 2026-08-20; verify against the primary source before citing._
>
> Tight LD lower bounds for Gaussian-mixture clustering, sparse clustering, and biclustering, with matching upper bounds.

_The two passages below are verbatim, verified against `raw/LM25_LBLatentModels.pdf` on 2026-08-20._

> "We build on the seminal paper of [66] and propose a new scheme to derive lower bounds on the performance of low-degree polynomials in some latent space models."

> "We also prove matching upper-bounds and some additional statistical results, in order to provide a comprehensive description of the statistical-computational gaps occurring in these three problems."
