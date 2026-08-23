---
title: The Sample Complexity of Membership Inference and Privacy Auditing
type: source
date_ingested: 2026-07-26
date_verified: 2026-08-22
authors: [Mahdi Haghifam, Adam Smith, Jonathan Ullman]
venue: "venue unconfirmed from PDF"
year: 2025
claim_quantifier: universal
antecedent: "The dimension must exceed the threshold at which a fully informed attacker succeeds, d > c_1(n + n^2 ρ^2). The hard instances are Gaussian populations with spiked covariance Σ = I_d + σ^2 U U^T, σ^2 ≳ d, and the mean estimator is pinned to the noisy empirical mean. Under the complementary hypothesis, when the attacker already knows Σ, Theorem 1.2 gives m ≳ min{n, 1/ρ^2}, which never exceeds n."
adversary_bound: "Samples only. The attack is an arbitrary function ψ_m : (R^d)^m × R^d × R^d → {IN, OUT} of m auxiliary i.i.d. samples, the released mean and the target point. It is unbounded in computation, in space and in queries. It is also required to succeed for EVERY population in the family and every ρ-accurate symmetric algorithm, so the bound is minimax over the family rather than pointwise against one population."
tags: [sample-complexity, adversarial-ml, learning-theory, reconstruction]
cls_target: train data
cls_family: membership
cls_phase: post hoc
cls_access: weights
cls_write: read only
cls_frame: statistical
cls_party: attacker
cls_unit: samples
cls_tightness: exponent
cls_baseline: stated
cls_second_party: samples
cls_assessed: explicit
cls_evidence: "every sample-based MIA for the Gaussian mean estimation problem (Section 1.1) requires m ≳ n²ρ² + n samples"
cls_evidence_src: Thm 1.1
cls_reason: "access=weights because μ̂ is the whole released object with no further model structure to query; second=samples records the trainer's own n against which the attacker's m is measured; frame=compute stretches the codebook's compute/capability split to cover a sample bound, since capability is defined narrowly as perturbation or corruption and the paper itself calls the attacker computationally unbounded."
cls_prov: S
cls_date: 2026-08-22
---

> **Verified against `raw/HSU25_SampleComplexityMIA.pdf` on 2026-08-22.** The bound, the setting, the
> definition of a sample-based attack, the adversary's resource bound, the lower-bound technique and
> the quotations below were checked against the extracted text of that file. Two quotations carried by
> an earlier version of this page were faithful but truncated. The headline sentence ended at "than the
> [training algorithm]", with a square-bracket gloss standing in for the paper's own five closing words,
> and the Theorem 1.1 transcription dropped "(Section 1.1)". Both are restored below. Still unverified:
> the venue, and the proofs in Sections 3 and 4 and Appendices A through D, which were read for
> statement and method rather than line by line. The PDF is arXiv:2508.19458v1 dated August 26, 2025.

## Summary

The question is how much an attacker needs to know about the population, made precise as sample
complexity. The trainer sees `n` samples from `D = N(μ, Σ)` in `d` dimensions and releases `μ̂` with
`E[‖μ̂ − μ‖²_Σ] ≤ dρ² + d/n`. The attacker sees `μ̂`, a target point that is either a member of the
training set or an independent draw, and `m` further independent samples from `D`. It must achieve
false-positive rate at most `0.49` and true-positive rate at least `0.51` for every population in the
family and every `ρ`-accurate symmetric estimator.

Against that yardstick the answer is a quadratic separation. Theorem 1.1 gives `m ≳ n²ρ² + n`, so in
the regime `ρ = ω(n^{-1/2})` the attacker needs `ω(n)` samples, strictly more than the trainer used.
The abstract states the significance directly. *"Our result is the first to show that the attacker
sometimes needs many more samples than the training algorithm uses to train the model."*

Two facts govern how far the result travels. The first is that the driver is covariance estimation.
Theorem 1.2 shows that if the attacker knows `Σ` then `m ≳ min{n, 1/ρ²}` suffices and is optimal, which
is never more than `n`. The hard instances in Theorem 1.1 are spiked covariances
`Σ = I_d + σ²UU^T` with `σ² ≳ d`, and the intuition the authors give is that an attacker with fewer
than `k` auxiliary samples cannot find all `k` high-variance directions. The second is that the
adversary is computationally unbounded and constrained only in samples. The lower bound is a total
variation bound on a mixture over a uniformly random `k`-dimensional subspace, proved by a technique
the authors attribute to Ingster and Suslina.

## Claim Boundary

**Quantified over.** All `m`-sample-based attacks, which are arbitrary measurable functions with no
resource bound. It is a minimax statement. For every attack there **exists** a population in the family
on which it fails, so it does not say that a particular attacker facing a particular known population
needs `ω(n)` samples.

**Antecedent.** `d > c_1(n + n²ρ²)`, meaning the dimension is above the threshold `d★(n, ρ) ≜ n + n²ρ²`
at which a fully informed attacker succeeds at all. Below that threshold no attack works even with
infinite samples, so the question is empty. The hypothesis is a design choice about which regime to
study rather than an assumption about the world.

**Which party is constrained and in what resource.** The attacker, in auxiliary samples `m`. It has
unlimited computation. The trainer is constrained in accuracy through `ρ` and in symmetry, being
required to factor through the empirical mean, and the lower bound is witnessed by the specific
estimator `μ̂ = (1/n)Σᵢ Xᵢ + ρZ` with `Z ∼ N(0, Σ)`.

**The success criterion and its tolerance.** A distinguishing advantage of `0.02`, from
`FPR ≤ 0.49` and `TPR ≥ 0.51`. The authors observe that since these are lower bounds the weak
requirement only strengthens the result, and that the bound rules out any attack whose TPR minus FPR
exceeds a small constant, which covers the low-FPR regime empirical work cares about.

**The baseline.** A fully informed attacker with `m = ∞`, using the Neyman-Pearson test
`(X − μ)^T Σ^{-1}(μ̂ − μ) ≥ c·d/n`. The whole result is phrased as the gap between that attacker and a
sample-limited one.

**Does not establish.** No computational statement of any kind. There is no neural network, no
stochastic gradient descent and no non-Gaussian population. The characterisation is tight only when
`d ≍ d★(n, ρ)`. When `d` is much larger than `d★` the best known attack uses `Θ(d)` reference samples
and a gap remains. And the separation is specific to unknown covariance, which Theorem 1.2 makes
explicit.

**Abstract versus theorem.** The abstract matches the theorem. It says `Ω(n + n²ρ²)` samples *"can be
necessary"*, with "can be" carrying the existential over populations, and it names the competitor as
*"a fully informed attacker"*. The one place a reader may over-read is the practical implication in
§1.2.1, which is an argument about the restricted form of deployed attacks rather than a theorem.

## Key Contributions

- The first attacker-versus-trainer sample-complexity separation for membership inference, at
  `m ≳ n²ρ² + n` against a trainer using `n`.
- Identification of covariance estimation as the driver, by proving the matching `min{n, 1/ρ²}` bound
  for the known-covariance case, which shows the attack of Dwork et al. is sample-optimal there.
- A matching upper bound (Theorem 3.3) using `O(d★(n, ρ))` samples, so the characterisation is tight
  when `d ≍ d★(n, ρ)`.
- A reduction (Equation 5) from an `m`-sample attacker in `d` dimensions with `k` planted directions to
  a zero-auxiliary-sample attacker in `d − 2m` dimensions with `k − m` directions, plus a structural
  result identifying the sufficient statistics in the zero-sample case as `‖X̃‖`, `‖μ̃‖` and `⟨X̃, μ̃⟩`.
- A privacy-auditing consequence. Attacks used in practice have a restricted form, computing a
  distribution-independent statistic and using the reference data only to calibrate a threshold, and
  the authors show that for such attacks `Θ(n)` samples are as good as the distribution itself. Since
  `ω(n)` samples enable attacks that `O(n)` samples cannot, existing audits may understate risk.

## Key Definitions / Theorems

- **Theorem 1.1 (verbatim, informal version of Theorem 3.1):** *"Fix n, ρ, d, and assume d ≳ d★(n, ρ) ≜
  n + n²ρ², i.e., the dimension is large enough for a fully-informed attacker to succeed. Then, every
  sample-based MIA for the Gaussian mean estimation problem (Section 1.1) requires m ≳ n²ρ² + n samples.
  Moreover, the lower bound holds even when we restrict attention to the specific mean estimator
  μ̂ = (1/n)Σᵢ Xᵢ + ρZ where Z ∼ N(0, Σ)."* The mathematics is re-typeset from the PDF, and the earlier wiki
  rendering silently dropped "(Section 1.1)".
- **Theorem 3.1 (formal).** For universal constants `c_1, c_2`, if `d > c_1(n + n²ρ²)` and
  `m ≤ c_2(n + n²ρ²)` then there is no `(P_d, {A_{n,ρ}}, n, m)`-sample-based MIA, where `A_{n,ρ}` is the
  noisy empirical mean of Definition 2.4 and `P_d` is the family of Definition 2.3.
- **Theorem 1.2 (informal version of Theorem 4.1).** With known covariance, `m ≳ min{n, 1/ρ²}`, and more
  generally an `m`-sample-based MIA exists only if `d ≳ n + n²ρ² + n²/m`. The authors' gloss, verbatim,
  is that *"the driver of high sample complexity in MIA is estimating the covariance of the
  population."*
- **The success criterion (Section 1.1).** An `m`-sample-based MIA is a function
  `ψ_m : (R^d)^m × R^d × R^d → {IN, OUT}` such that for every normal distribution and every `ρ`-accurate
  symmetric algorithm, `Pr(ψ_m(Y^m, μ̂, X_0) = IN) ≤ 0.49` and `Pr(ψ_m(Y^m, μ̂, X_i) = IN) ≥ 0.51` for
  every `i ∈ [n]`.

## Connections

- **The programme's designated predecessor.** They prove the sample-complexity version with an
  unbounded attacker. The computational restatement in units native to the training algorithm is what
  remains. See [native-asymmetry-in-learning](../analyses/native-asymmetry-in-learning.md) §4.
- Contrast [Cohen et al.](cohen-data-reconstruction.md), whose Definition C.1 bounds the adversary's
  time rather than its samples, and [Kaplan et al.](kaplan-bayesian-memorization-reconstruction.md),
  which bounds neither.
- Cites [Dinur–Nissim](dinur-nissim-revealing-information.md) as the reconstruction-attack ancestor.
- The exponent instrument that would restate this is the information or generative exponent. See
  [native-computational-problems-survey](../../exp/literature/related-work.md) §5,
  [information-exponent](../concepts/information-exponent.md),
  [generative-exponent](../concepts/generative-exponent.md).
- Concepts: [membership-inference-game](../concepts/membership-inference-game.md),
  [computational-vs-statistical-memorization](../concepts/computational-vs-statistical-memorization.md),
  [low-fpr-evaluation-regime](../concepts/low-fpr-evaluation-regime.md).

## Open Questions / Limitations

- **The competitive hazard, now confirmed.** The lower-bound technique is the second-moment method,
  stated in the paper as *"a proof technique attributed to Ingster and Suslina"*, applied to the
  chi-squared divergence of a mixture over planted subspaces. That is one step from a low-degree
  restatement, and the step is available to anyone who reads the paper.
- Gaussian mean estimation only, with symmetric estimators. No neural network, no stochastic gradient
  descent.
- The attacker is sample-bounded and computationally unbounded, so the computational axis is untouched.
- The tight characterisation covers `d ≍ d★(n, ρ)`. For `d ≫ d★` the gap between the `Θ(d)` upper bound
  and Theorem 1.1 is open.
- The separation vanishes when the attacker knows the covariance, so it prices ignorance of `Σ` rather
  than the difficulty of membership inference as such.

## Quotes / Notable Passages

> "Our result is the first to show that the attacker sometimes needs many more samples than the
> training algorithm uses to train the model."

The abstract's own hedging of the bound:

> "Our result shows that for membership inference in this setting, Ω(n + n²ρ²) samples can be necessary
> to carry out any attack that competes with a fully informed attacker."

On why deployed attacks cannot see the gap:

> "all attacks used in practice have a restricted form that uses O(n) samples and cannot benefit from
> ω(n) samples"
