---
title: Kesten-Stigum Threshold
type: concept
tags: [kesten-stigum, stochastic-block-model, community-detection, statistical-computational-gaps, statistical-physics]
---

## Definition

The **Kesten-Stigum (KS) threshold** for the symmetric k-stochastic block model is the parameter regime ε²d = k² (where d is average degree, ε is bias, k is community count). It marks a sharp transition in the computational difficulty of weak recovery:

- **Above KS** (ε²d > k²): poly-time algorithms (spectral, message passing) achieve constant correlation with true community labels.
- **Below KS** (ε²d < k² with k ≥ 5): conjecturally no poly-time algorithm succeeds, while exponential-time algorithms can still achieve information-theoretic recovery in a subregion.

The name comes from the classical Kesten-Stigum theorem (1966) on Galton-Watson branching processes: the same threshold governs reconstruction of ancestral information in trees, and the SBM weak-recovery threshold is heuristically its graph analogue.

## Intuition

KS corresponds to the point where the "signal" decays too fast along typical paths of length log n (the graph diameter) for local message-passing to accumulate coherent information. Physically, it marks a dynamical/spin-glass transition from a "liquid" posterior to a "glassy" one.

## Properties / Theorems

- **Massoulié 2014 / Abbe-Sandon 2015**: Above KS, poly-time weak recovery.
- **Banks-Moore-Neeman-Netrapalli 2016**: For k ≥ 5, info-theoretic weak recovery is possible strictly below KS.
- **Hopkins 2018, BBK+21a**: LD-detection lower bounds at KS.
- **Ding-Hua-Slot-Steurer 2025**: LD-recovery lower bounds at KS under extended LD conjecture.
- **Tree reconstruction connection**: KS originates from tree Ising model reconstruction thresholds.

## Where It Appears

- [Stochastic Block Model](stochastic-block-model.md)
- [Ding Low-Degree Community Detection](../sources/ding-low-degree-community-detection.md)

## Related Concepts

- [Stochastic Block Model](stochastic-block-model.md)
- [Statistical-Computational Gaps](statistical-computational-gaps.md)
- [Low-Degree Polynomial Framework](low-degree-polynomial-framework.md)

## Open Questions

- Unconditional poly-time lower bound at KS.
- Sharp KS threshold for asymmetric / labeled / degree-heterogeneous SBMs.
- Universality: does KS govern recovery thresholds in non-Bernoulli edge models?
