---
title: Adversarial VC Dimension
type: concept
tags: [adversarial-ml, PAC-learning, sample-complexity, learning-theory, robustness]
---

## Definition

Given a hypothesis class H ⊆ {±1}^X and a nearness relation R ⊆ X × X defining adversarial neighborhoods N(x) = {y : (x, y) ∈ R}, the **adversarial VC-dimension** AVC(H, R) is defined as the VC-dimension of the *corrupted hypothesis class* κ_R(H), where

κ_R(h)(x) = −1 if ∀y ∈ N(x): h(y) = −1
          = +1 if ∀y ∈ N(x): h(y) = +1
          = ⊥  otherwise (adversary wins)

Equivalently, AVC(H, R) = VC of the robust loss class L^R_H = {(x, y) ↦ sup_{z ∈ N(x)} 1[h(z) ≠ y] : h ∈ H}.

Introduced by Cullina, Bhagoji, Mittal (NeurIPS 2018).

## Intuition

AVC measures the complexity of the "robust version" of H — how many points the adversary cannot shatter in the presence of perturbations. When AVC is finite, RERM-style proper learning yields uniform convergence with sample complexity O((AVC · log(AVC/ε) + log(1/δ))/ε²).

## Properties / Theorems

- **AVC ≤ VC**? **False.** Cullina et al. 2018 give explicit constructions where AVC ≫ VC or AVC ≪ VC. AVC can be infinite even when VC is finite.
- **Halfspaces (Cullina et al. 2018)**: For H = halfspaces in R^d and any convex origin-symmetric perturbation set B, AVC(H, R_B) = VC(H) = d+1. So norm-bounded evasion doesn't increase sample complexity for halfspaces.
- **Not sufficient for robust learnability characterization (Montasser–Hanneke–Srebro 2019)**: There exist H with VC(H) = 1 but AVC(H, U) = ∞; H is nevertheless *improperly* robustly learnable. So AVC characterizes proper robust learnability (under uniform convergence) but not robust learnability in general.
- **Superseded by global one-inclusion graph dimension (Montasser–Hanneke–Srebro 2022)** as the characterizing dimension for robust PAC learnability.

## Where It Appears

- [PAC Learning in the Presence of Evasion Adversaries](../sources/pac-learning-evasion-adversaries.md) — introduces AVC
- [VC Classes are Adversarially Robustly Learnable](../sources/vc-classes-adversarially-robustly-learnable.md) — shows AVC insufficient
- [Robust PAC Learning Characterization](../sources/robust-pac-learning-characterization.md) — supersedes via global one-inclusion graph dimension
- [Tolerant Robust PAC Learning](../sources/tolerant-robust-pac-learning.md) — uses VC_U-dimension, a tolerant variant

## Related Concepts

- [Robust PAC Learning](robust-pac-learning.md)
- [Evasion Attacks](evasion-attacks.md)
- Global one-inclusion graph dimension (see robust-pac-learning-characterization source page)

## Open Questions

- Tight characterization of when AVC = VC (known for halfspaces under convex perturbations; open for neural nets, decision trees).
- Efficient computation of AVC for structured H.
- Multiclass / regression analogues.
