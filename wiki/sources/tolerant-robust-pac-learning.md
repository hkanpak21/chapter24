---
title: "Simplifying Adversarially Robust PAC Learning with Tolerance"
type: source
date_ingested: 2026-04-12
authors: [Hassan Ashtiani, Vinayak Pathak, Ruth Urner]
venue: "arXiv:2502.07232 (February 2025)"
year: 2025
tags: [adversarial-ml, PAC-learning, sample-complexity, robustness, learning-theory]
---

## Summary

This paper presents the first simple learner achieving **sample complexity linear in VC-dimension** for adversarially robust PAC learning, under a *tolerance* relaxation. The tolerance framework allows the learner to be evaluated against a slightly larger perturbation set than the adversary uses — the learner uses perturbation set U, but is compared against the optimal classifier for the expanded set V ⊃ U. Under this relaxation, linear-in-VC-dim sample complexity is achievable without relying on complex subroutines (one-inclusion graphs, compression schemes) from prior work.

Key result: the learner is improper but "almost proper" — it outputs a smooth (majority-vote) version of an ERM classifier or a discretized version thereof. Improper learning is necessary (proved for VC(H) = 1 classes).

## Key Contributions

- **Theorem 9 (RERM-and-Smooth)**: Sample complexity `Õ(VC(H) · log(VC(H)/η) / ε)` for realizable tolerant robust learning, using Robust ERM followed by majority-vote smoothing. For Euclidean balls: `Õ(VC(H)(log(VC(H)) + d·log(1+1/γ)) / ε)`.
- **Theorem 12 (RERM-and-Discretize)**: Sample complexity `Õ(VC(H)·log(k) / ε)` realizable, `Õ(VC(H)·log(k) / ε²)` agnostic, via discretization of the perturbation set. k = |C(x)| ≤ Θ((1+1/γ)^d · d^{d/2}) for ℓₚ norms.
- **Theorem 7 (Necessity of improper learning)**: For any r, d, γ > 0, there exists H with VC(H) = 1 that is NOT properly tolerantly robustly PAC learnable. Improper learning is necessary even for unit-VC-dimension classes.
- **Semi-supervised extension**: Comparable bounds in the semi-supervised setting, avoiding complex subroutines from prior work.
- **Simplification**: Avoids one-inclusion graph and compression-based subroutines of Montasser et al. 2022 — yields cleaner, deployable algorithms.

## Key Definitions / Theorems

**Tolerant adversarial PAC learning (Definition 3)**: Learner A is (U, V)-tolerantly robust PAC if given m samples, with probability ≥ 1−δ:
`ℒ_P^U(A(S)) ≤ ℒ_P^V(H) + ε`
where U ≺ V (U is a smaller perturbation set than V), and ℒ^U_P(h) = Pr_{(x,y)~P}[max_{z∈U(x)} ℓ(h,z,y) = 1].

**Adversarial loss (Definition 1)**: `ℓ^U(h,x,y) = max_{z∈U(x)} ℓ^{0/1}(h,z,y)`.

**VC_U-dimension (Definition 4)**: The maximum number of points that H can U-shatter — i.e., for which H can achieve all 2^m robustly distinct labelings under U perturbations.

**RERM-and-Smooth (Algorithm 1)**: (1) Compute robust ERM ĥ; (2) output majority vote of ĥ over a smoothing neighborhood W(x) at test point x.

**RERM-and-Discretize (Algorithm 2)**: (1) Discretize perturbation set via global grid C; (2) compute RERM on discretized perturbation type; (3) output nearest-neighbor discretized hypothesis.

## Connections

- [Robust PAC Learning Characterization](robust-pac-learning-characterization.md) — Montasser et al. 2022 characterized robust learnability via global one-inclusion graph; this paper gives simpler algorithms under tolerance
- [Evasion Attacks](../concepts/evasion-attacks.md) — tolerant robust learning provides a practical defense
- [Hassan Ashtiani](../entities/hassan-ashtiani.md)
- [Ruth Urner](../entities/ruth-urner.md)

## Open Questions / Limitations

- The tolerance gap between U and V is necessary for the linear-VC-dim bound — can it be removed while maintaining linear sample complexity?
- Are the RERM-and-Smooth / RERM-and-Discretize algorithms efficient for practical hypothesis classes (halfspaces, neural networks)?
- What is the tight dependence on the tolerance parameter γ in the sample complexity?
- Extension to infinite perturbation sets beyond ℓₚ balls?
