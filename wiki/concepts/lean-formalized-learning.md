---
title: Lean-Formalized Learning Theory
type: concept
tags: [formal-verification, lean, learning-theory, rademacher-complexity, certification]
---

## Definition
The project of expressing and mechanically verifying statistical learning theory theorems — PAC generalization bounds, VC-dimension results, Rademacher-complexity bounds, concentration inequalities — in a dependently-typed proof assistant (Lean, Coq/Rocq, Isabelle/HOL) on top of a formal measure-theoretic probability library (Mathlib, MathComp-Analysis, HOL-Probability).

## Intuition
Textbook learning-theory proofs often gloss over measurability of suprema, integrability conditions, and switching of expectations. Mechanization forces these obligations to be discharged explicitly, producing generalization bounds that are trustworthy building blocks for certified ML pipelines and for formal assurance of regulatory claims.

## Properties / Theorems
Known formalization milestones:
- **Bagnall & Stewart (2019, Coq)**: PAC bound for finite hypothesis classes via Hoeffding.
- **Tassarotti, Vajjha, Banerjee, Tristan (2021, Lean 3)**: PAC learnability of decision stumps (VC = 1).
- **Bentkamp et al. (2016–2019, Isabelle/HOL)**: expressive-power separation of deep vs. shallow networks.
- **Vajjha et al. (CertRL, 2021; Stochastic Approximation, 2022, Coq)**: convergence of value/policy iteration and stochastic approximation.
- **Hirata (2025, Isabelle/HOL)**: no-free-lunch theorem.
- **Sonoda et al. (2026, Lean 4)**: Rademacher complexity, symmetrization, McDiarmid inequality, Dudley entropy integral; ℓ₂/ℓ₁ linear-predictor bounds.
- **Yuanhe et al. (2026, Lean 4)**: statistical learning theory with Gaussian Lipschitz concentration and Dudley.
- **Karayel & Tan (2023, Isabelle/HOL AFP)**: Concentration Inequalities (Bennett, Bernstein, Efron–Stein, McDiarmid, Paley–Zygmund).

## Where It Appears
- [lean-rademacher-formalization](../sources/lean-rademacher-formalization.md) — Sonoda et al., primary source.

## Related Concepts
- [pac-learning](pac-learning.md) (parent).
- [universal-law-of-robustness](universal-law-of-robustness.md) — a natural next target for mechanization.
- [zk-ml-verification](zk-ml-verification.md) — certified bounds complement ZK proofs of training/inference.

## Open Questions
- Mechanization of adversarially-robust PAC learning (Montasser et al.).
- Automation for measurability/integrability obligations.
- Formalization of PAC-Bayes and stability-based bounds.
- Integration with certified differentially-private training proofs.
