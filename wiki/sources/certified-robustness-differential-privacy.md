---
title: "Certified Robustness to Adversarial Examples with Differential Privacy (PixelDP)"
type: source
date_ingested: 2026-04-23
authors: [Mathias Lecuyer, Vaggelis Atlidakis, Roxana Geambasu, Daniel Hsu, Suman Jana]
venue: "IEEE S&P 2019"
venue_evidence: "https://ieeexplore.ieee.org/document/8835364/; 2019 IEEE Symposium on Security and Privacy"
year: 2019
tags: [adversarial-ml, certified-robustness, differential-privacy, randomized-smoothing, evasion-attacks]
claim_quantifier: universal
antecedent: "none. The certificate follows from the differential privacy of the scoring function, which is a property of the injected noise, not a computational assumption."
adversary_bound: "none. Neither party is bounded in computation. The attacker is constrained only geometrically, by a p-norm ball of radius 1 on the input features, and the certificate is a statement about that ball."
date_verified: 2026-08-20
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: none
cls_write: read only
cls_frame: capability
cls_party: attacker
cls_unit: perturbation
cls_tightness: budget
cls_baseline: n/a
cls_second_party: none
cls_assessed: explicit
cls_evidence: "It is natural to constrain the amount of change an attacker is allowed to make to the input, and often this is measured by the p-norm of the change"
cls_evidence_src: "§II, framing before Def. of B_p(r)"
cls_reason: "Textbook fit for Rule 5: front matter already states neither party is bounded computationally, only the attacker's p-norm ball of radius 1 (verified verbatim against raw/LAGHJ19_PixelDP.pdf), giving party=attacker, unit=perturbation, tightness=budget, frame=capability directly. access=none since the certificate is a worst-case-over-the-ball statement; the paper never uses 'white-box' or 'black-box' language (grepped, zero hits) and specifies no query model. second=none: the front matter is explicit that the defender's Monte Carlo sampling budget affects only the confidence interval of the estimate, not a formal bound entering the theorem, so it is not a second party's resource."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper (LAGHJ19) introduces **PixelDP**, the first certified adversarial defense that scales to ImageNet-size networks, via a novel connection between **differential privacy** (DP) and **adversarial robustness**. The key conceptual insight is that DP, though traditionally used to hide information about individual records in training data, can be equivalently applied at inference time *over input features* (e.g., pixels): if a classifier is (ε, δ)-DP with respect to a norm-bounded change in input pixels, then its expected scores are stable under such perturbations, yielding a certified robustness radius.

Concretely, PixelDP inserts a Gaussian or Laplace noise layer inside the classifier and leverages two properties of DP: (1) **post-processing** — any computation applied to the output of an `(ε, δ)`-DP algorithm remains `(ε, δ)`-DP, so noise can be injected anywhere in the pipeline; (2) the **expected output stability** property, which the paper calls "a rather obvious but not previously enunciated property" and proves as Lemma 1: for an `(ε, δ)`-DP function with output bounded in `[0, b]`, `E[A(x)] ≤ e^ε E[A(x+α)] + bδ` for every `α` in the unit `p`-norm ball. Combining with a most-likely-class decision rule yields a certified robustness condition.

**Correction, 2026-08-20.** The bound was previously written here as `|E[A(x)] − E[A(x + α)]| ≤ (e^ε − 1) · E[A(x+α)] + bδ`. The paper states a one-sided inequality without absolute values; the two-sided form does not follow from Lemma 1 as stated and is not in the paper.

PixelDP is the predecessor of [Cohen-Rosenfeld-Kolter 2019 (Randomized Smoothing)](certified-robustness-randomized-smoothing.md); Cohen et al. showed that Gaussian smoothing admits a tighter robustness radius via the Neyman-Pearson lemma directly, though both approaches have the same certified-defense structure.

## Claim Boundary

- **Quantified over:** all inputs and all perturbations inside the stated norm ball, for a given trained network with a given noise layer. The certificate is per-input: it either holds for a particular `x` or does not, and the paper reports the fraction of test points on which it holds.
- **Antecedent:** none. Differential privacy of the scoring function is arranged by construction through the noise layer and the sensitivity of the computation preceding it. No hardness assumption enters.
- **Which party is constrained:** **neither party is bounded in computation.** The attacker is constrained purely geometrically, by a norm ball on the input features, and the certificate is a statement about that ball. It is worth stating plainly, because the DP framing invites the reading that some resource bound is in play; there is none. The one resource that matters is the defender's Monte Carlo budget, which enters as the confidence interval on the estimated expected scores, not as a bound on the attacker.
- **Does not establish:** privacy of the training data. The paper is explicit that its use of DP is orthogonal to that goal. It also does not establish robustness outside the certified radius, and the certificate degrades when the estimated expectations are loose.
- **Abstract vs theorem:** none found. The intro's "the first certified defense we are aware of that both scales to large networks and datasets" is hedged as written.

## Key Contributions

- **DP-robustness connection**: First formal reduction linking DP at inference time (over input features) to certified adversarial robustness.
- **First certified ImageNet defense**: PixelDP on the Inception network for ImageNet — scalable in a way no prior certified defense was.
- **Architecture-agnostic**: unlike convex-polytope bounds (Wong-Kolter) which assume ReLU structure, PixelDP works for arbitrary architectures.
- **Expected Output Stability Bound (Lemma 1)**: a general property of DP mechanisms that the paper uses to derive robustness certificates; useful beyond adversarial robustness.
- **Experimental validation**: matches empirical best-effort defenses (Madry adversarial training) on MNIST/CIFAR-10/SVHN while providing formal guarantees.
- **Flexible ℓp support**: PixelDP certificates extend from standard ℓ₂ (Gaussian mechanism) to ℓ₁ (Laplace mechanism) and ℓ∞.

## Key Definitions / Theorems

- **(ε, δ)-PixelDP classifier**: scoring function A satisfies (ε, δ)-DP w.r.t. ℓp norm on input features — i.e., for any x, x' with ∥x − x'∥_p ≤ 1 and any output set S, Pr[A(x) ∈ S] ≤ e^ε Pr[A(x') ∈ S] + δ.
- **Lemma 1 (Expected Output Stability)**: for an (ε, δ)-DP function A with output bounded in [0, b], for any α ∈ B_p(1): `E[A(x)] ≤ e^ε E[A(x+α)] + bδ`. Applied with `b = 1` to each class score this gives Equation (3), `∀k, ∀α ∈ B_p(1) : E(y_k(x)) ≤ e^ε E(y_k(x+α)) + δ`. The paper describes the property as "rather obvious but not previously enunciated".
- **Robustness certification condition**: A prediction f(x) = argmax_c y_c(x) is certifiably robust to L-norm-bounded perturbations if the top-class expected score exceeds the second-class expected score after applying the DP-induced scaling by e^{εL}.
- **DP noise layer**: insert Gaussian/Laplace noise at a chosen layer; sensitivity depends on the intermediate computation up to that layer.

## Connections

- Source: [Certified Robustness via Randomized Smoothing (Cohen-Rosenfeld-Kolter 2019)](certified-robustness-randomized-smoothing.md) — the tighter Neyman-Pearson-based version of this paper's idea; supersedes PixelDP's guarantees in the Gaussian-ℓ₂ case.
- Source: [Deep Learning with Differential Privacy (Abadi et al. 2016)](deep-learning-differential-privacy.md) — DP-SGD provides the privacy-at-training-time mechanism; PixelDP is privacy-at-inference-time.
- Source: [Provably Robust SmoothAdv (Salman et al. 2019)](provably-robust-smoothadv.md) — adversarial-training boost to randomized smoothing.
- Source: [Provable Defenses via Convex Polytope (Wong-Kolter 2018)](provable-defenses-convex-polytope.md) — alternative certified defense that does *not* scale to ImageNet.
- Concept: [Evasion Attacks](../concepts/evasion-attacks.md) — the attack surface this paper defends against.
- Concept: [Differential Privacy](../concepts/) — the mechanism.
- Concept: [Certified Robustness](../concepts/) — the goal.

## Open Questions / Limitations

- **Looseness**: The PixelDP bound is loose by a factor determined by the DP composition analysis; Cohen et al. tightened this using Neyman-Pearson directly.
- **Monte Carlo sampling overhead**: certification requires many forward passes to estimate expected scores.
- **ℓ∞ certification is weaker** than ℓ₂ — the Laplace-noise pathway for ℓ∞ does not give as tight a bound as Gaussian-noise for ℓ₂.
- **Certification is for a specific network architecture with specific noise injection**; adapting to new architectures requires re-analysis of sensitivity.
- **Does not compose well** with other defense mechanisms (e.g., adversarial training at inference time).

## Quotes / Notable Passages

Verified against `raw/LAGHJ19_PixelDP.pdf` on 2026-08-20 unless marked otherwise.

> "Our defense, called PixelDP, is based on a novel connection between robustness against adversarial examples and differential privacy, a cryptographically-inspired privacy formalism, that provides a rigorous, generic, and flexible foundation for defense."

> "DP on a small number of pixels in an image guarantees robustness of predictions against adversarial examples that can change up to that number of pixels."

> _Not verbatim. Checked against `raw/LAGHJ19_PixelDP.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> Incorporating DP into the learning procedure to increase robustness to adversarial examples is completely different and orthogonal to using DP to preserve the privacy of the training set.

The paper's own sentence carries an extra word and a clause the paraphrase dropped:

> "Incorporating DP into the learning procedure to increase robustness to adversarial examples requires is completely different and orthogonal to using DP to preserve the privacy of the training set, the focus of prior DP ML literature [40], [1], [9] (as § VI explains)."

— §I. The stray "requires" is the paper's, not a transcription error.

> "PixelDP is orthogonal to these works, differing in goals, semantic, and algorithms. The only thing we share with DP ML (and most other applied DP literature) are DP theory and mechanisms."

— §VI, the same point stated without the typo.
