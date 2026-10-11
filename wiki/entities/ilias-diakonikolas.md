---
title: Ilias Diakonikolas
type: entity
entity_type: author
tags: [robust-statistics, statistical-query, learning-theory, agnostic-learning, multi-index-model]
---

## About

UW Madison (affiliation as stated in the ingested PDFs). Works on robust high-dimensional statistics, SQ lower bounds, and the computational complexity of learning under noise.

## Contributions / Works

- **[Algorithms and SQ Lower Bounds for Robustly Learning Real-valued Multi-index Models](../sources/robust-multi-index-sq-bounds.md)** (Diakonikolas, Iakovidis, Kane, Ren; 2025) — an agnostic PAC learner for well-behaved MIMs with `d^{O(m)}` dimension dependence and a nearly matching `d^{Omega(m)}` SQ lower bound; the first size-independent learner for homogeneous Lipschitz ReLU networks.
- **[Sample and Computationally Efficient Robust Learning of Gaussian Single-Index Models](../sources/robust-single-index-efficient.md)** (Wang, Zarifis, Diakonikolas, Diakonikolas; 2024) — a constant-factor agnostic proper learner at `Theta~(d^{ceil(k*/2)} + d/eps)`, matching CSQ lower bounds.
- Cited throughout this corpus for the Non-Gaussian Component Analysis SQ framework (Diakonikolas–Kane–Stewart) that both papers' lower bounds build on.

## Connections

- Both papers place the adversary in the *agnostic* (adversarial-label-noise) model: the corruption is unbounded and uncosted, and only the learner is priced. See [Robust Estimators in High Dimensions](../sources/robust-estimators-high-dimensions.md) for the broader programme.
