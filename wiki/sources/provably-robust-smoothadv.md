---
title: "Provably Robust Deep Learning via Adversarially Trained Smoothed Classifiers (SmoothAdv)"
type: source
date_ingested: 2026-04-23
authors: [Hadi Salman, Greg Yang, Jerry Li, Pengchuan Zhang, Huan Zhang, Ilya Razenshteyn, Sébastien Bubeck]
venue: "NeurIPS 2019, stated in the PDF's own footer as 33rd Conference on Neural Information Processing Systems, Vancouver (arXiv:1906.04584v5, 10 Jan 2020)"
year: 2019
tags: [adversarial-ml, certified-robustness, randomized-smoothing, adversarial-training, evasion-attacks]
claim_quantifier: empirical
antecedent: "none. The certification machinery is Cohen et al.'s and rests on the Neyman-Pearson lemma; the contribution is a training method whose benefit is measured, not proved."
adversary_bound: "none. The attacker is an ℓ₂ ball of radius R. The training-time attack is a bounded-norm optimisation, not a computationally bounded adversary."
date_verified: 2026-08-20
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: white box
cls_write: read only
cls_frame: capability
cls_party: attacker
cls_unit: perturbation
cls_tightness: budget
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "ε = maximum allowed ℓ2 perturbation of the input"
cls_evidence_src: "§4 (experimental hyperparameters)"
cls_reason: "Rule 5, same shape as Cohen et al. (whose certification machinery this paper inherits unchanged, per the Claim Boundary: 'the certificate is Cohen et al.'s and is unconditional'): the only restriction on the evasion adversary is the l2 perturbation radius epsilon, so party=attacker, unit=perturbation, tightness=budget, frame=capability, access=white box, write=none. The paper's own 'SmoothAdv attack' objective is a training-time proxy the defender solves to generate adversarial examples for adversarial training, not a bound on the threat-model attacker, so it does not change this row. second_party=none: the reported Monte Carlo/training-time cost (8-16x) appears only in the wiki's Open Questions/Limitations discussion, not as a formal theorem parameter (rule 8), so it is not elevated to a second party bound."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper (SYLZZ+19, "SmoothAdv") improves [Cohen-Rosenfeld-Kolter 2019](certified-robustness-randomized-smoothing.md)'s randomized smoothing via **adversarial training tailored to the smoothed classifier**. The key insight: when the base classifier f is adversarially trained not on f itself but on the smoothed soft-classifier G (computed over Gaussian noise), the resulting smoothed classifier g has substantially better certified robustness. At ImageNet ℓ₂ radius 0.5, SmoothAdv achieves 56% certified top-1 accuracy versus Cohen et al.'s 49%; on CIFAR-10 the gain is ~16% absolute across all radii, rising to ~22% when combined with pre-training and semi-supervised learning.

The core technical contribution is the **SmoothAdv attack objective** (S): maximize ℓ_CE(G(x'), y) over ∥x' − x∥₂ ≤ ε, where G is the smoothed soft-classifier. This differs from a naive "attack G via attacking f" because the argmax in G's definition is replaced by a soft version, making gradient-based optimization feasible. The paper provides several gradient estimators for (S) and shows that adversarial training with this objective improves the certified accuracy of the resulting smoothed classifier — not merely its empirical robustness.

Along the way, the paper also offers an alternative, more concise proof of Cohen et al.'s tight robustness guarantee by casting it as a nonlinear Lipschitz property of the smoothed classifier (Appendix A).

## Claim Boundary

- **Quantified over:** two datasets, ImageNet and CIFAR-10, and the architectures trained on them. The headline numbers are measurements: 56% provable top-1 on ImageNet at ℓ₂ radius `127/255`, against 49% for Cohen et al.; up to 16% improvement on CIFAR-10, rising to 22% with pre-training and semi-supervised learning. Nothing here is proved to hold for other datasets or architectures.
- **Antecedent:** none. The certificate is Cohen et al.'s and is unconditional; this paper changes the base classifier, not the certification.
- **Which party is constrained:** **neither party is bounded in computation.** The evasion adversary is an ℓ₂ ball. The "attack" this paper introduces is a training-time optimisation problem solved by the *defender*, not an adversary with a budget. The one genuine resource cost is the defender's: Monte Carlo samples per training step, and the certification passes per test point.
- **Does not establish:** any new certification bound. The paper says so — it uses "the certification method of Cohen et al." — so the improvement is entirely in the base classifier. It also does not establish that the best gradient estimator for the SmoothAdv objective is the right one in general; the choice is empirical.
- **Abstract vs theorem:** the abstract's "consistently outperforms all existing provably ℓ₂-robust classifiers" is a claim about the classifiers existing in 2019 and is supported by the tables, not by a theorem.

## Key Contributions

- **SmoothAdv attack**: adversarial attack specifically designed for smoothed classifiers, via gradient optimization on the smoothed soft-classifier's cross-entropy loss.
- **State-of-the-art certified ℓ₂ robustness**: 56% certified top-1 on ImageNet at radius 0.5 (7% improvement over Cohen et al.); up to 22% improvement on CIFAR-10 when combined with pre-training.
- **Adversarial training boosts certified (not just empirical) robustness**: when base classifier f is adversarially trained against SmoothAdv, the certified radius of the resulting smoothed g increases.
- **Pre-training + semi-supervised learning compound the gains**: combined approach gives best-in-class results on CIFAR-10.
- **Alternative Neyman-Pearson proof** via Lipschitz property of the smoothed classifier — a cleaner derivation of the Cohen et al. tight bound.

## Key Definitions / Theorems

- **Smoothed soft classifier G(x) = E_{δ~N(0,σ²I)}[F(x+δ)]** where F: ℝ^d → P(Y) is a soft classifier.
- **SmoothAdv objective (S)**: x̂ = argmax_{∥x'−x∥₂ ≤ ε} −log E_δ [(F(x' + δ))_y] — attacks G's soft-classification probability of the true class y.
- **Distinction from naive objective (4)**: solving (4) corresponds to finding an adversarial example of `F` that is robust to Gaussian noise; (S) directly attacks the smoothed model. The paper reports that the distinction is decisive in practice, since Cohen et al. found attacks based on (4) ineffective.
- **Gradient estimators**: several Monte-Carlo gradient estimators for (S) under the non-convexity of the log-expectation; choice of estimator matters substantially.
- **Lipschitz proof of smoothed-classifier robustness (Appendix A)**: G has a specific nonlinear Lipschitz property that directly yields the Cohen et al. tight robustness radius.

## Connections

- Source: [Certified Robustness via Randomized Smoothing (Cohen-Rosenfeld-Kolter 2019)](certified-robustness-randomized-smoothing.md) — the baseline this paper improves.
- Source: [Certified Robustness via Differential Privacy (Lecuyer et al. 2019)](certified-robustness-differential-privacy.md) — earlier randomized-smoothing approach via DP.
- Source: [Universal Law of Robustness (Bubeck-Sellke 2021)](universal-law-of-robustness.md) — same Bubeck group; provides the overparameterization-necessary underpinning that smoothing partially sidesteps via noise-averaging.
- Source: [Provable Defenses via Convex Polytope (Wong-Kolter 2018)](provable-defenses-convex-polytope.md) — alternative certified defense for ℓ∞.
- Concept: [Evasion Attacks](../concepts/evasion-attacks.md) — the attack surface defended against.
- Concept: [Certified Robustness](../concepts/) — the goal.
- Author: [Sébastien Bubeck](../entities/sebastien-bubeck.md), [Ilya Razenshteyn](../entities/ilya-razenshteyn.md), [Jerry Li](../entities/jerry-li.md).

## Open Questions / Limitations

- **Subtle non-convexity of the SmoothAdv objective**: different gradient estimators can lead to training instability; "best" estimator is empirically found, not formally derived.
- **ℓ∞ extension** via non-Gaussian noise distributions remains looser than Gaussian-ℓ₂.
- **Computational cost**: adversarial training for smoothed classifiers requires many Monte Carlo samples per step, multiplying training time by ~8-16×.
- **Does not provide new certification methodology** — uses Cohen et al.'s CERTIFY, so improvements come from better base classifiers not better bounds.
- **Pre-training + semi-supervised gains may not generalize to ImageNet** — the compounding is most pronounced on CIFAR-10.

## Quotes / Notable Passages

Verified against `raw/SYL+19_SmoothAdv.pdf` on 2026-08-20 unless marked otherwise.

> "We demonstrate through extensive experimentation that our method consistently outperforms all existing provably ℓ₂-robust classifiers by a significant margin on ImageNet and CIFAR-10, establishing the state-of-the-art for provable ℓ₂-defenses."

— abstract. Matched digit-insensitively; the subscript-2 glyph does not survive text extraction from the PDF.

> "Directly finding adversarial examples for the smoothed hard classifier g is a somewhat ill-behaved problem because of the argmax, so we instead propose to find adversarial examples for the smoothed soft classifier G."

— §2.2.

> _Not verbatim. Checked against `raw/SYL+19_SmoothAdv.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> Conceptually, solving (4) corresponds to finding an adversarial example of F that is robust to Gaussian noise. In contrast, (S) corresponds to finding an adversarial example of the smoothed classifier G itself.

The first sentence is the paper's; the second was rewritten. The full passage reads:

> "Conceptually, solving (4) corresponds to finding an adversarial example of F that is robust to Gaussian noise. In contrast, (S) is directly attacking the smoothed model i.e. trying to find adversarial examples that decrease the probability of correct classification of the smoothed soft classifier G."

— §2.2, followed by the remark that Cohen et al. found attacks based on (4) not to be effective.
