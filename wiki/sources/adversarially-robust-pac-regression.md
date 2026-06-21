---
title: "Adversarially Robust PAC Learnability of Real-Valued Functions"
type: source
date_ingested: 2026-04-23
authors: [Idan Attias, Steve Hanneke]
venue: ICML 2023 (arXiv:2206.12977)
year: 2023
tags: [adversarial-ml, PAC-learning, regression, fat-shattering, sample-complexity, sample-compression]
---

## Summary

This paper (AH23) extends the adversarial PAC-learnability characterization from classification to **regression** under ℓp losses with arbitrary perturbation sets. The main result: real-valued function classes with finite **γ-fat-shattering dimension** are robustly PAC learnable in both realizable and agnostic settings. For convex function classes, learning can even be *proper* (outputting a hypothesis from the class). In contrast, some non-convex function classes provably require improper learning, inheriting the Montasser-Hanneke-Srebro 2019 lower bound from the classification setting.

The main technical tool is an **adversarially robust sample compression scheme** of size determined by the fat-shattering dimension. Going beyond the binary-valued case requires (a) a robust boosting algorithm for real-valued functions (adapted from Kégl 2003 and Hanneke et al. 2019), (b) generalization from approximate interpolation via uniform convergence (Anthony-Bartlett), and (c) careful discretization via uniform supremum-metric covers (since the classification-era trick of inflating to a finite partition fails for ℓp losses).

A separate, novel agnostic sample compression scheme for real-valued functions is introduced along the way, which may be of independent interest for statistical learning theory.

## Key Contributions

- **Robustly learnable = finite fat-shattering dimension**: For real-valued function classes H, H is robustly PAC-learnable with ℓp loss iff fat(H, γ) < ∞ for all γ > 0 (realizable and agnostic).
- **Sample complexity bounds**: Õ(fat³(H, ε/p) fat*(H, ε/p) / ε⁵) for ℓp robust regression; improved to Õ(fat(H, ε/p) fat*(H, ε/p) / ε²).
- **(η, β)-robust regression** (cutoff loss): Õ(fat(H, β) fat*(H, β) / ε) realizable, Õ(fat(H, β) fat*(H, β) / ε²) agnostic.
- **Proper learning for convex classes**: Convex function classes are *properly* robustly learnable — circumventing the non-convex obstruction inherited from Montasser et al.
- **Robust sample compression scheme**: size determined by fat-shattering dimension; the technical heart of the proofs.
- **Agnostic sample compression for real-valued functions**: novel byproduct, useful beyond robust regression.

## Key Definitions / Theorems

- **γ-fat-shattering dimension fat(H, γ)**: largest n such that there exist x₁, ..., x_n and r₁, ..., r_n where for every subset S ⊆ [n], some h ∈ H satisfies h(x_i) ≥ r_i + γ for i ∈ S and h(x_i) ≤ r_i − γ for i ∉ S.
- **Dual fat-shattering dimension fat*(H, γ)**: fat-shattering of the dual class; finite whenever fat(H, γ) < ∞.
- **Robust Regression (ℓp)**: Err_ℓp(h; D) = E_{(x,y)} [sup_{z ∈ U(x)} |h(z) − y|^p].
- **(η, β)-Robust Regression (cutoff)**: Err_η(h; D) = Pr[sup_{z ∈ U(x)} |h(z) − y| ≥ η]; learner must achieve Err_{η+β}(ĥ) ≤ inf_h Err_η(h) + ε.
- **Main theorem**: finite fat-shattering dimension implies PAC learnability with sample complexity given above.
- **Proper-learning theorem**: For convex H, robust ERM on a discretized cover yields a proper learner; non-convex H may require improper learning.

## Connections

- Source: [VC Classes Are Adversarially Robustly Learnable (Montasser-Hanneke-Srebro 2019)](vc-classes-adversarially-robustly-learnable.md) — classification predecessor; improper-learning lower bound transfers to non-convex regression.
- Source: [Adversarially Robust Learning: Generic Minimax Optimal Learner (MHS 2022)](robust-pac-learning-characterization.md) — global one-inclusion-graph dimension characterization for classification; open question of analogous dimension for regression.
- Source: [Simplifying Adversarially Robust PAC Learning with Tolerance](tolerant-robust-pac-learning.md) — tolerance relaxation in the classification setting; complementary to this paper's cutoff-loss approach.
- Source: [PAC-Learning in the Presence of Evasion Adversaries](pac-learning-evasion-adversaries.md) — Cullina-Bhagoji-Mittal foundational framework.
- Concept: [PAC Learning](../concepts/pac-learning.md) — foundational framework.
- Concept: [Robust PAC Learning](../concepts/robust-pac-learning.md) — adversarial extension.
- Concept: [Adversarial VC Dimension](../concepts/adversarial-vc-dimension.md) — the dimension analogue for classification.
- Authors: [Steve Hanneke](../entities/steve-hanneke.md).

## Open Questions / Limitations

- Exact characterizing dimension for robust regression (analogous to MHS 2022's global one-inclusion-graph dimension for classification) remains open.
- Sample complexity gap between the two bounds (ε^{-2} vs. ε^{-5}) reflects the tension between proper-learner tractability and optimal rates.
- Computational efficiency of the robust sample compression scheme is not addressed; the algorithm is information-theoretic.
- Extension to stochastic loss functions beyond ℓp / cutoff not treated.

## Quotes / Notable Passages

> "Classes of finite fat-shattering dimension are learnable in both realizable and agnostic settings. Moreover, for convex function classes, they are even properly learnable. In contrast, some non-convex function classes provably require improper learning algorithms."

> "Our main technique is based on a construction of an adversarially robust sample compression scheme of a size determined by the fat-shattering dimension."
