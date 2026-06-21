---
title: "PAC-learning in the Presence of Evasion Adversaries"
type: source
date_ingested: 2026-04-12
authors: [Daniel Cullina, Arjun Nitin Bhagoji, Prateek Mittal]
venue: "NeurIPS 2018 (arXiv:1806.01471)"
year: 2018
tags: [adversarial-ml, PAC-learning, sample-complexity, robustness, learning-theory, evasion-attacks]
---

## Summary

This paper is the first to formally extend the PAC learning framework to include a test-time (evasion) adversary and to introduce the **adversarial VC-dimension** (AVC) as the natural complexity measure for this setting. Given a nearness relation R ⊆ X × X, the authors define *corrupted hypotheses* κ_R(h) that output a special ⊥ ("always wrong") label whenever there exist two points in a test example's neighborhood receiving opposite labels from h. The VC-dimension of this corrupted class is the adversarial VC-dimension, which yields a Fundamental-Theorem-style sample complexity bound m_{H,R}(δ,ε) = O((AVC · log(AVC/ε) + log(1/δ))/ε²).

The key concrete result: for halfspace classifiers in R^d with any convex, origin-symmetric perturbation set (all ℓ_p, p ≥ 1, adversaries), AVC = VC = d+1. Thus sample complexity of PAC learning halfspaces does not increase in the presence of norm-bounded evasion adversaries — closing an open question from Schmidt et al. (2018).

The authors also show AVC can be *either larger or smaller* than the standard VC-dimension, depending on H and R, making it an interesting dimension in its own right.

Historical context: this paper set up a uniform-convergence-style theory that Montasser–Hanneke–Srebro (COLT 2019) subsequently showed was fundamentally inadequate for general H (finite VC classes may not admit *proper* robust learning; AVC can be infinite even when VC is finite).

## Key Contributions

- **Adversarial VC-dimension (Definition 5)**: AVC(H, R) = VC of the corrupted hypothesis class κ_R(H), where κ_R(h): X → {-1, +1, ⊥} outputs ⊥ when h disagrees inside the neighborhood N(x).
- **Theorem 1 (sample complexity upper bound)**: m_{H,R}(δ, ε) ≤ C · (d log(d/ε) + log(1/δ))/ε² where d = AVC(H, R). Follows from the Rademacher-complexity / Sauer-Shelah chain.
- **Theorem (halfspaces)**: For H = halfspaces over R^d and R derived from any nonempty closed convex origin-symmetric set B (so R = {(x,y) : y−x ∈ B}), AVC(H, R) = VC(H) = d+1. Closes an open question of Schmidt et al. 2018.
- **Examples**: Explicit constructions where AVC ≫ VC and where AVC ≪ VC — AVC is not monotone in either H or R relative to VC.
- **Corrupted hypothesis construction**: κ_R(h)(x) = −1 if h(y) = −1 ∀y ∈ N(x); +1 if h(y) = +1 ∀y ∈ N(x); ⊥ otherwise.

## Key Definitions / Theorems

**Adversarial expected risk (Def 1)**: L_P(h, R) = E_{(x,c)~P}[max_{y∈N(x)} ℓ(h(y), c)], where ℓ is 0-1 loss.

**Adversarial ERM (Def 2)**: AERM_{H,R}(x, c) = argmin_{h∈H} L_{(x,c)}(h, R).

**Corrupted hypothesis (Section 3.1)**: κ_R: (X → {±1}) → (X → {±1, ⊥}). Equivalence lemma: L_P(h, R) = L_P(κ_R(h), I_X). Learning with adversary R for H = learning without adversary for κ_R(H).

**Adversarial VC-dimension (Def 5)**: AVC(H, R) = sup { n : σ'(λ(κ_R(H)), n) = 2^n } where σ' is the shattering coefficient of the loss class.

**Halfspace AVC theorem**: Proved using signed-distance-to-boundary analysis — for halfspace h with weight vector w, the optimal evasion attack moves x by a ∥·∥_B-minimal amount, and the resulting corrupted hypothesis is itself a halfspace-like object with VC ≤ d+1.

## Connections

- [VC Classes are Adversarially Robustly Learnable](vc-classes-adversarially-robustly-learnable.md) — Montasser–Hanneke–Srebro 2019 show that AVC can be infinite when VC is finite, making AVC insufficient for characterizing learnability; uniform-convergence program this paper belongs to fails in general.
- [Robust PAC Learning Characterization](robust-pac-learning-characterization.md) — Montasser et al. 2022, the eventual characterization via global one-inclusion graph dimension.
- [Adversarial VC Dimension](../concepts/adversarial-vc-dimension.md)
- [Robust PAC Learning](../concepts/robust-pac-learning.md)
- [Evasion Attacks](../concepts/evasion-attacks.md)
- [Daniel Cullina](../entities/daniel-cullina.md), [Prateek Mittal](../entities/prateek-mittal.md)

## Open Questions / Limitations

- AVC does not characterize general robust learnability — the follow-up COLT 2019 paper showed finite VC classes can have infinite AVC yet still be (improperly) robustly learnable.
- Uniform convergence framework inherently justifies only proper learning (RERM); insufficient in the general case.
- Computing AVC for non-halfspace classes (neural networks, decision trees) is open in general.
- Extension to multi-class and regression settings.

## Quotes / Notable Passages

> "We extend the Probably Approximately Correct (PAC)-learning framework to account for the presence of an adversary... We derive the Vapnik-Chervonenkis (VC)-dimension for these, denoted as the adversarial VC-dimension."

> "The adversarial VC-dimension can be either larger or smaller than the standard VC-dimension depending on the hypothesis class and adversary."
