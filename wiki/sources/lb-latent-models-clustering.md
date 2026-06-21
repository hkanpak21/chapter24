---
title: "Computational Lower Bounds in Latent Models: Clustering, Sparse-Clustering, Biclustering"
type: source
date_ingested: 2026-04-23
authors: [Bertrand Even, Christophe Giraud, Nicolas Verzelen]
venue: "arXiv:2506.13647 (Jun 2025)"
year: 2025
tags: [statistical-computational-gaps, low-degree-polynomials, clustering, biclustering, latent-models]
---

## Summary

This paper (EGV25) uses **conditioned low-degree techniques** to produce **tight LD lower bounds** for three canonical ML problems:
1. **Gaussian-mixture clustering**
2. **Sparse clustering** (clustering with sparse-mean separation)
3. **Biclustering** (row-column simultaneous clustering in data matrices)

Each bound has a **matching upper bound** via an efficient algorithm, yielding sharp statistical-computational gap characterizations. This is a concrete post-2024 extension of the [Schramm-Wein 2022](low-degree-estimation-schramm-wein.md) low-degree-for-estimation program into canonical ML tasks, complementing [Ding-Hua-Slot-Steurer 2025](ding-low-degree-community-detection.md)'s community-detection analysis.

EGV25 is representative of the 2025-2026 trajectory where the low-degree framework is being systematically applied to practical ML problems: clustering, biclustering, community detection, sparse PCA — giving the field a unified "computational-threshold landscape" for unsupervised learning.

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

> "Tight LD lower bounds for Gaussian-mixture clustering, sparse clustering, and biclustering, with matching upper bounds."
