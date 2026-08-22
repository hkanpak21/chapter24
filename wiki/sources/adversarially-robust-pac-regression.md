---
title: "Adversarially Robust PAC Learnability of Real-Valued Functions"
type: source
date_ingested: 2026-04-23
authors: [Idan Attias, Steve Hanneke]
venue: "ICML 2023 (venue unconfirmed from PDF: raw/AH23_RobustPACRegression.pdf is arXiv:2206.12977v3 [cs.LG] and names no venue; the attribution is carried over from the earlier ingest)"
year: 2023
tags: [adversarial-ml, PAC-learning, regression, fat-shattering, sample-complexity, sample-compression]
claim_quantifier: universal
antecedent: "Finite γ-fat-shattering dimension of the real-valued function class, an ℓp loss, and an arbitrary perturbation set. For the proper-learning half, convexity of the function class. The training sample is i.i.d. and non-adversarial; the adversary acts at test time only."
date_verified: 2026-08-20
---

## Summary

This paper (AH23) extends the adversarial PAC-learnability characterization from classification to **regression** under ℓp losses with arbitrary perturbation sets. The main result: real-valued function classes with finite **γ-fat-shattering dimension** are robustly PAC learnable in both realizable and agnostic settings. For convex function classes, learning can even be *proper* (outputting a hypothesis from the class). In contrast, some non-convex function classes provably require improper learning, inheriting the Montasser-Hanneke-Srebro 2019 lower bound from the classification setting.

The main technical tool is an **adversarially robust sample compression scheme** of size determined by the fat-shattering dimension. Going beyond the binary-valued case requires (a) a robust boosting algorithm for real-valued functions (adapted from Kégl 2003 and Hanneke et al. 2019), (b) generalization from approximate interpolation via uniform convergence (Anthony-Bartlett), and (c) careful discretization via uniform supremum-metric covers (since the classification-era trick of inflating to a finite partition fails for ℓp losses).

A separate, novel agnostic sample compression scheme for real-valued functions is introduced along the way, which may be of independent interest for statistical learning theory.

## Claim Boundary

- **Quantified over:** all real-valued function classes of finite fat-shattering dimension, all perturbation sets, ℓp losses, realizable and agnostic. The proper-learning result is quantified over convex classes; the improper-learning necessity is existential, inherited as a construction from the classification setting.
- **Antecedent:** finite fat-shattering dimension at the relevant scale, and for the proper half, convexity. Both are properties of the hypothesis class, checkable in principle for a given class.
- **Which party is constrained:** the **learner**, in sample complexity. The perturbation set is arbitrary and the adversary realising it has no resource bound of any kind. Nothing is computational — the page's own limitations section records that the compression scheme's efficiency is not addressed. The one bounded quantity, the compression size, is a property of the learner.
- **Does not establish:** (i) the converse — the abstract claims only that finite fat-shattering implies learnability, so the "iff" stated earlier on this page under Key Contributions is stronger than what is verified from the abstract and should be checked against the theorem statements before being cited; (ii) any efficient algorithm; (iii) the exact characterizing dimension for robust regression, which the paper leaves open.
- **Abstract vs theorem:** none found in the paper. The overstatement is on this page, in the "iff" noted above.

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

> "We show that classes of finite fat-shattering dimension are learnable in both realizable and agnostic settings. Moreover, for convex function classes, they are even properly learnable. In contrast, some non-convex function classes provably require improper learning algorithms."
>
> _Corrected 2026-08-20 against `raw/AH23_RobustPACRegression.pdf`: the passage previously began "Classes of finite…", dropping the abstract's "We show that". Restored so that the sentence reads as the paper states it — an implication in one direction, not an equivalence._

> "Our main technique is based on a construction of an adversarially robust sample compression scheme of a size determined by the fat-shattering dimension."
