---
title: Empirically Measuring Concentration — Fundamental Limits on Intrinsic Robustness
type: source
date_ingested: 2026-04-12
authors: [Saeed Mahloujifar, Xiao Zhang, Mohammad Mahmoody, David Evans]
venue: NeurIPS
year: 2019
tags: [adversarial-ml, concentration-of-measure, evasion-attacks, empirical, robustness]
---

## Summary

This paper (MZME19) tests empirically whether the concentration-of-measure upper bounds on intrinsic robustness [MDM19, Gilmer+, Fawzi+] actually explain the adversarial vulnerability observed on real datasets. The authors design algorithms for *empirically measuring* the concentration function of a distribution given only finite samples: given a dataset, they compute (lower bounds on) α(b) = 1 − inf{μ(S_b) : μ(S) ≥ 1/2} and compare it against the empirical adversarial risk of state-of-the-art classifiers.

The central finding: on benchmark datasets (MNIST, CIFAR-10) under commonly-used ℓ_∞ / ℓ₂ perturbation budgets, the concentration-of-measure upper bound on intrinsic robustness is *substantially above* what existing classifiers achieve — i.e., the gap between empirical adversarial error and the concentration bound is large. This implies that concentration alone does *not* explain the observed adversarial vulnerability: there is room for more robust classifiers than currently exist, and concentration-based impossibility results are not tight on natural data distributions under standard perturbation models.

The paper thus reframes the theoretical concentration narrative: while concentration is a fundamental obstacle in worst-case geometric spaces, real-world data may enjoy much weaker concentration, meaning a large fraction of the observed vulnerability is due to classifier design rather than inherent geometry.

## Key Contributions

- **Concentration function for a subset family (Def 3.1)**: h(μ, α, ε, G) = inf_{E ∈ G} {μ(E_ε) : μ(E) ≥ α}. Parameterizing by a family G (rather than all measurable sets) is the methodological move that makes empirical estimation feasible.
- **Complexity penalty (Def 3.2)**: φ(m, δ) is a complexity penalty for G if Pr_{S ← μᵐ}[∃E ∈ G with |μ(E) − μ̂_S(E)| ≥ δ] ≤ φ(m, δ). Instantiated via VC dimension or Rademacher complexity.
- **Generalization theorem (Thm 3.3)**: Empirical concentration w.r.t. G is close to true concentration w.r.t. G with probability ≥ 1 − 2(φ(m, δ) + φ_ε(m, δ)), where φ and φ_ε are penalties for G and G_ε.
- **Convergence theorem (Thm 3.5)**: Under (i) summability of complexity penalties for G(T) and G_ε(T), (ii) δ(T) → 0, and (iii) h(μ, α, ε, G(T)) → h(μ, α, ε) (universal-approximator condition on the family), the empirical concentration converges almost surely to the *true, unrestricted* concentration function as T, m → ∞.
- **ℓ∞ instantiation (Def 3.7, CR(T, n))**: Complement of union of T n-dimensional hyperrectangles. Authors provide a concrete algorithm and bound its convergence rate.
- **MNIST / CIFAR-10 case studies (Section 4)**: Measures concentration bounds for both ℓ_∞ and ℓ_2 and compares to adversarial accuracy of SOTA robust classifiers; code at github.com/xiaozhanguva/Measure-Concentration.
- **Gap discovery**: Empirical concentration-based upper bound on intrinsic robustness is substantially *higher* than current classifier robustness — concentration does not fully account for observed adversarial vulnerability.
- **Methodological point**: Distinguishes *intrinsic* (distribution-dependent) vulnerability from *classifier-induced* vulnerability.

## Key Definitions / Theorems

- **Def 2.1 — Adversarial risk**: AdvRisk_ε(f, f*) = Pr_x[∃ x' ∈ Ball(x, ε) with f(x') ≠ f*(x')].
- **Def 2.2 — Intrinsic robustness**: 1 − inf over classifiers in a family F of AdvRisk_ε. Authors take F = {classifiers with risk ≥ α}.
- **Theorem 2.4 (restated from MDM19)**: AdvRisk_ε(f, f*) ≥ h(μ, Risk(f, f*), ε). This is the concentration-based lower bound the paper wants to compute empirically.
- **Def 3.1 — Concentration function for a collection G**: h(μ, α, ε, G) = inf_{E ∈ G} {μ(E_ε) : μ(E) ≥ α}.
- **Def 3.2 — Complexity penalty**: Function φ(m, δ) bounding the probability that empirical measure deviates from true measure by δ uniformly over G.
- **Theorem 3.3 — Generalization of concentration**: Pr_{S ← μᵐ}[h(μ, α − δ, ε, G) − δ ≤ h(μ̂_S, α, ε, G) ≤ h(μ, α + δ, ε, G) + δ] ≥ 1 − 2(φ(m, δ) + φ_ε(m, δ)).
- **Theorem 3.5 — Convergence to true concentration**: under conditions (i)–(iv), lim_{T→∞} h(μ̂_{S_T}, α, ε, G(T)) = h(μ, α, ε) almost surely.
- **Def 3.7 — CR(T, n)**: Complement of union of T hyperrectangles family for ℓ∞.

## Connections

- Empirical companion to [The Curse of Concentration (MDM19)](curse-of-concentration.md) — tests whether its bound binds on natural data
- Supports positive-separation results like [GJMM20 / win-win theorems](win-win-robust-learning.md) that argue some robustness gaps are computational, not information-theoretic
- Related concepts: [Concentration of Measure](../concepts/concentration-of-measure.md), [Evasion Attacks](../concepts/evasion-attacks.md)
- Synthesized in [A Complexity Theoretic Approach to Adversarial ML](complexity-theoretic-adversarial-ml.md)

**Authors**: [Saeed Mahloujifar](../entities/saeed-mahloujifar.md), [Xiao Zhang](../entities/xiao-zhang.md), [Mohammad Mahmoody](../entities/mohammad-mahmoody.md), [David Evans](../entities/david-evans.md).

## Open Questions / Limitations

- Theorem 3.5's condition 4 (h(μ, α, ε, G(T)) → h(μ, α, ε)) is required but hard to verify for a given dataset: it asks the family G(T) to approximate arbitrary measurable sets in a measure-preserving, expansion-preserving way.
- Complexity penalty for G_ε is often much worse than for G alone — for example, the VC dimension of ε-expansions of halfspaces can be much larger than the VC dimension of halfspaces. The paper handles this for hyperrectangles but general families remain challenging. This difficulty is tied to generalization bounds in the adversarial setting ([Cullina-Bhagoji-Mittal 2018](pac-learning-evasion-adversaries.md), [Attias-Hanneke 2023](../concepts/robust-pac-learning.md)).
- ℓ₂ instantiation is less tight than ℓ∞ in the empirical results.
- Results are for ℓ_∞ / ℓ₂ on natural images; other modalities (audio, text, graph) unexplored.
- If concentration is *not* the binding constraint, what is? Candidates: manifold curvature, local Lipschitz structure of the ground-truth concept, computational hardness (see [Adversarial Examples from Computational Constraints](adversarial-examples-computational-constraints.md)).

## Quotes / Notable Passages

> "Our estimated intrinsic robustness shows that, for most settings, there exists a large gap between the robust error achieved by the best current models and the theoretical limits implied by concentration. This suggests the concentration of measure is not the only reason behind the vulnerability of existing classifiers to adversarial perturbations."

> "Either there is room for improving the robustness of image classifiers (even with non-zero classification error) or a need for deeper understanding of the reasons for the gap between intrinsic robustness and the actual robustness achieved by robust models."

> "Relating the complexity penalty for expansion of a collection to that of the original collection is tightly related to generalization bounds in the adversarial settings."
