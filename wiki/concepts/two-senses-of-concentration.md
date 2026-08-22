---
title: Two Senses of Concentration
type: concept
tags: [adversarial-ml, concentration-of-measure, evasion-attacks, robustness, terminology]
---

## Definition

The word **concentration** carries two distinct and nearly opposite meanings in the robustness literature. Both are about "measure sitting in a small place", but they measure *small* against different yardsticks, and they license opposite conclusions about whether robust classifiers can exist.

**Sense A — metric concentration (concentration of measure / Lévy).** A metric probability space (X, d, μ) is concentrated when every set of non-trivial measure has an ε-expansion covering almost all of X. Formally, via the concentration function α(ε) = 1 − inf{μ(S_ε) : μ(S) ≥ 1/2}, or the risk-indexed variant h(μ, α, ε) = inf{μ(E_ε) : μ(E) ≥ α}. *Small* here means: it takes only a short distance to grow any set into nearly everything.

- Direction of the conclusion: **concentration is bad for the defender.** If the space is concentrated, the error region of any classifier with non-trivial risk expands to nearly everything, so adversarial risk goes to ≈1. See [The Curse of Concentration](../sources/curse-of-concentration.md), [Fawzi–Fawzi–Fawzi](../sources/adversarial-vulnerability-any-classifier.md), Gilmer et al., Shafahi et al.
- Under this sense, the uniform measure on a high-dimensional sphere or cube is *highly* concentrated.

**Sense B — volume concentration (mass on a small-volume set).** A distribution q over X ⊆ R^n is (C,ε,δ)-concentrated when there is a set S with q(S) ≥ 1−δ but Vol(S) ≤ C·exp(−nε), where Vol is Lebesgue measure. *Small* here means: the mass lives on a set that is tiny relative to the ambient volume. This is concentration measured **relative to the uniform measure**, not intrinsically.

- Direction of the conclusion: **concentration is good for the defender.** Volume concentration is *necessary* for a robust classifier to exist, and a strengthened version of it is *sufficient*. See [Adversarial Examples Might be Avoidable](../sources/data-concentration-robustness-avoidable.md).
- Under this sense, the uniform measure is the *least* concentrated distribution possible — exactly inverting Sense A.

## Intuition

Sense A asks: *how fast does an ε-ball smear a set out over the space?* Sense B asks: *how much of the space does the data actually occupy?*

A uniform distribution on the sphere is maximally concentrated in Sense A (any half-sphere expands to swallow the rest) and minimally concentrated in Sense B (it occupies everything). A distribution living on a thin low-dimensional subspace is minimally concentrated in Sense A (its mass does not smear; it can be far from most of the space) and maximally concentrated in Sense B.

So the two senses are close to antonyms in practice, and the sentences "the data is concentrated, therefore no classifier can be robust" and "the data is concentrated, therefore a robust classifier exists" are both true statements about different properties.

## Properties / Theorems

- **Sense A, negative:** [MDM19 Thm 1.1](../sources/curse-of-concentration.md) — if (X,d,μ) is concentrated then any classifier with Ω(1) risk has adversarial risk ≈ 1 under ε-perturbations. Restated as AdvRisk_ε(f, f*) ≥ h(μ, Risk(f,f*), ε).
- **Sense A, measured:** [MZME19](../sources/empirically-measuring-concentration.md) estimates h for MNIST, CIFAR-10, Fashion-MNIST, SVHN with a provably convergent estimator and finds the bound does not bind: the concentration-implied floor on adversarial risk sits well below the adversarial risk of the best robust classifiers (e.g. CIFAR-10 ℓ∞ at 8/255: 29.21% estimated vs 52.96% attack success rate reported for Madry et al.). Conclusion: metric concentration "is not the sole reason behind vulnerability".
- **Sense B, necessary:** [PSV23 Thm 2.1](../sources/data-concentration-robustness-avoidable.md) — an (ε,δ)-robust classifier exists ⟹ some class conditional is (C,ε,δ)-concentrated. Proof by Brunn–Minkowski.
- **Sense B, insufficient alone:** PSV23 §3 — all classes could concentrate on the *same* small-volume set; then not even an accurate classifier exists.
- **Sense B, sufficient when strengthened:** PSV23 Thm 3.1 — (ε,δ,γ)-strong concentration (each class on its own small set, 2ε-expansions barely overlapping) ⟹ an (ε, δ+γ)-robust classifier exists. Existential, not constructive.

## Where It Appears

- [The Curse of Concentration (MDM19)](../sources/curse-of-concentration.md) — Sense A, negative direction.
- [Empirically Measuring Concentration (MZME19)](../sources/empirically-measuring-concentration.md) — Sense A, measured and found not to bind on image benchmarks.
- [Adversarial Examples Might be Avoidable (PSV23)](../sources/data-concentration-robustness-avoidable.md) — Sense B, positive direction; §6 names the distinction explicitly.
- [Adversarial Vulnerability for Any Classifier (FFF18)](../sources/adversarial-vulnerability-any-classifier.md) — Sense A, via smooth generative models.
- [Adversarial Spheres](../sources/adversarial-spheres.md) — the sphere instance that seeded Sense A.
- [Computational Concentration of Measure (EMM20)](../sources/computational-concentration-of-measure-etesami.md) — a poly-time-attacker version of Sense A.

## Related Concepts

- [Concentration of Measure](concentration-of-measure.md) — Sense A proper.
- [Lévy Family](levy-family.md) — the canonical Sense-A-concentrated spaces.
- [Intrinsic Robustness](intrinsic-robustness.md) — the quantity Sense A upper-bounds and Sense B lower-bounds.
- [Isoperimetry and Robustness](isoperimetry-and-robustness.md).

## Open Questions

- Is there a single parameterized definition with both senses as limits? The natural candidate is a two-measure concentration function h(q, μ_ref, α, ε) that reduces to Sense A when q = μ_ref and to Sense B when μ_ref is uniform. Nobody in this wiki's sources writes it that way.
- Sense B has never been *measured* on a real dataset the way MZME19 measured Sense A. PSV23 infers weak Sense-B concentration from the observed existence of robust classifiers rather than estimating it. An estimator for strong concentration (Def 3.1) is open.
- Both senses are information-theoretic. Neither prices the adversary's compute. The Sense-A line has a computational analogue ([EMM20](../sources/computational-concentration-of-measure-etesami.md)); Sense B has none.
- A source page whose framing quantifies over "any concentrated space" must say *which* sense, or it inverts. This page exists because that failure was found and corrected on [curse-of-concentration](../sources/curse-of-concentration.md).
