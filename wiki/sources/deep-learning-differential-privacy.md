---
title: Deep Learning with Differential Privacy
type: source
date_ingested: 2026-04-23
authors: [Martín Abadi, Andy Chu, Ian Goodfellow, H. Brendan McMahan, Ilya Mironov, Kunal Talwar, Li Zhang]
venue: "CCS 2016 (23rd ACM Conference on Computer and Communications Security), stated on the first page of the PDF; the file is the full version"
year: 2016
tags: [differential-privacy, deep-learning, privacy-preserving-ml, sgd, certification]
claim_quantifier: empirical
antecedent: "none. Differential privacy is an information-theoretic guarantee and no computational assumption is used."
adversary_bound: "none. The paper states that its approach protects against an adversary with full knowledge of the training mechanism and access to the model's parameters, and that this adversary may control some or all of the remaining training data. No bound on its computation is imposed anywhere."
date_verified: 2026-08-20
cls_target: train data
cls_family: none
cls_phase: train time
cls_access: none
cls_write: none
cls_frame: capability
cls_party: mechanism
cls_unit: privacy budget
cls_tightness: budget
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed:
cls_evidence: "satisfies (ε, δ)-differential privacy if for any two adjacent inputs d, d0 ∈ D and for any subset of outputs S ⊆ R it holds that Pr[M(d) ∈ S] ≤ eε Pr[M(d0) ∈ S] + δ"
cls_evidence_src: Def 1
cls_reason: "Adversary is explicitly unbounded (\"full knowledge of the training mechanism and access to the model's parameters\", §1); the only bound in the paper falls on the mechanism, via the privacy budget ε, hence party=mechanism/unit=privacy budget/frame=capability rather than an attacker-side reading; family=none because this is a defence with no attack instantiated."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper introduces **DP-SGD** — the canonical mechanism for training deep neural networks under (ε, δ)-differential privacy — together with the **moments accountant**, a privacy-budget tracking technique that gives asymptotically and empirically tighter bounds on composed privacy loss than the strong composition theorem.

The mechanism modifies standard SGD in four ways: (1) compute per-example gradients rather than batched gradients, (2) clip each per-example gradient's ℓ₂ norm to a threshold C, (3) add Gaussian noise calibrated to the clipping norm and a noise multiplier σ, (4) track cumulative privacy loss via the moments accountant. The per-example clipping bounds the sensitivity and the Gaussian noise supplies the guarantee.

The moments accountant bounds the **log moment generating function** of the privacy loss random variable at several values of `λ`, then converts to `(ε, δ)`. Theorem 1 gives the payoff: for sampling probability `q = L/N` and `T` steps, Algorithm 1 is `(ε, δ)`-differentially private for any `δ > 0` and `ε < c₁q²T` provided `σ ≥ c₂ q√(T log(1/δ)) / ε`. Against the strong composition theorem this saves a `√(log(1/δ))` factor in `ε` and a `Tq` factor in `δ`; the paper's worked example gives `ε ≈ 1.26` where strong composition gives `ε ≈ 9.34`.

**Correction, 2026-08-20.** The description previously given here, that the accountant "tracks the *full distribution* of the privacy loss random variable rather than just its moments", contradicts both its name and its content. It tracks bounded log moments. The claim that DP-SGD "has since become the de facto privacy mechanism in production ML pipelines (Apple, Google, Meta, OpenAI)" is about the world in 2026, not about this 2016 paper, and no source is attached to it here.

## Claim Boundary

- **Quantified over:** the mechanism, universally. `(ε, δ)`-differential privacy is a worst-case guarantee over all pairs of adjacent datasets and all measurable output sets. The *utility* claims are empirical and cover exactly two tasks, MNIST and CIFAR-10.
- **Antecedent:** none of a cryptographic or complexity kind. The privacy analysis does assume the sampling model it states — lots drawn with probability `q = L/N`, and Theorem 1's regime `ε < c₁q²T`.
- **Which party is constrained:** the **mechanism**, in the noise it must add and the sensitivity it must bound. The adversary is **not** constrained at all: the paper says its protection holds against an adversary with full knowledge of the training mechanism and access to the model's parameters, which may additionally control some or all of the rest of the training data. This is the opposite of the compute-bounded-adversary setting; nothing here prices an attacker.
- **Does not establish:** that a given `ε` is enough for any particular application; that the guarantee survives when real training deviates from the assumed Poisson-style sampling; or that hyperparameter search is covered, which it is not without an outer accounting.
- **Abstract vs theorem:** none found. The abstract claims only "a modest privacy budget" and "a manageable cost", and the body qualifies "single-digit" explicitly.

Experimental contributions include TensorFlow implementations, training deep networks on MNIST/CIFAR-10 with "single-digit" ε privacy budgets while preserving usable accuracy, and careful implementation strategies (lots, per-layer clipping, PCA projections for input-layer complexity reduction).

## Key Contributions

- **DP-SGD algorithm**: per-example clip + Gaussian noise + privacy accounting, implementable as a drop-in replacement for SGD.
- **Moments accountant**: tracks higher-order moments of privacy loss to give tight asymptotic and empirical bounds on composed (ε, δ)-DP.
- **Engineering techniques**: efficient per-example gradient computation, lots (sub-batches) to reduce memory, per-layer clipping and noise parameters, DP PCA projection for input layer.
- **Practical demonstration**: DP-trained deep networks on MNIST and CIFAR-10 under a single-digit privacy budget, on non-convex objectives with tens of thousands to millions of parameters. The paper contrasts this with prior work obtaining strong results on convex models with fewer parameters, or on complex networks with large privacy loss. **Correction, 2026-08-20:** the word "first" was removed; the paper claims a contrast with prior work, not priority.
- **TensorFlow implementation**: the paper builds on TensorFlow for training with differential privacy.

## Key Definitions / Theorems

- **(ε, δ)-differential privacy** (Definition 1): Pr[M(d) ∈ S] ≤ e^ε · Pr[M(d') ∈ S] + δ for adjacent databases d, d'.
- **Gaussian mechanism**: M(d) = f(d) + N(0, S_f² σ²), satisfies (ε, δ)-DP if δ ≥ (4/5) exp(−(σε)²/2) and ε < 1.
- **DP-SGD (Algorithm 1)**: at each step, sample a lot with probability L/N, compute and clip per-example gradients to norm C, average, add N(0, σ²C²I) noise, take SGD step.
- **Moments accountant**: for each composition step, bound `α(λ) = log E[exp(λ · PrivLoss)]` for several values of λ, then convert to `(ε, δ)`. **Correction, 2026-08-20:** "yields the tightest (ε, δ) bound for the composed mechanism" is not claimed by the paper; what it claims is that the bound is tighter than the strong composition theorem, saving `√(log(1/δ))` in `ε` and `Tq` in `δ`.
- **Theorem 1**: there exist constants `c₁, c₂` such that, given `q = L/N` and `T` steps, for any `ε < c₁q²T`, Algorithm 1 is `(ε, δ)`-differentially private for any `δ > 0` if `σ ≥ c₂ q√(T log(1/δ)) / ε`.
- **Threat model, stated in §1**: an adversary with full knowledge of the training mechanism and access to the model's parameters, possibly controlling some or all of the remaining training data.

## Connections

- Concept: [Differential Privacy](../concepts/) (concept page to be created in follow-up lint — currently canonical definition appears in multiple concept pages).
- Source: [Certified Robustness via Differential Privacy (PixelDP)](certified-robustness-differential-privacy.md) — applies DP machinery at inference time for adversarial robustness, building on DP-SGD's training-time foundation.
- Source: [Universal Jailbreak Backdoors from Poisoned RLHF](universal-jailbreak-rlhf-backdoors.md) — DP-SGD is one mitigation discussed against RLHF poisoning.
- Source: [Covert Learning](covert-learning.md) — related cryptographic privacy framework for learning.
- Concept: [Computational Indistinguishability](../concepts/computational-indistinguishability.md) — DP is a statistical analogue; pure-DP (δ=0) is a statistical-distance guarantee, approximate-DP (δ>0) is close to but not identical to computational indistinguishability.
- Concept: [Poisoning Attacks](../concepts/poisoning-attacks.md) — DP training incidentally provides certified poisoning robustness.
- Authors: Abadi, Chu, McMahan, Mironov, Talwar, Zhang (Google); Goodfellow (OpenAI, at Google during work).

## Open Questions / Limitations

- Utility gap: DP-SGD incurs 10–30% accuracy loss at useful privacy levels on challenging datasets.
- Hyperparameter sensitivity: clipping threshold C and noise multiplier σ are task-dependent; recent work (DP-FTRL, etc.) reduces this.
- Amplification by sampling + moments accountant gives the best bound, but the analysis assumes Poisson sampling which real training rarely matches.
- Private hyperparameter tuning: choosing (C, σ, η) privately is expensive; usually accounted for by outer DP composition.

## Quotes / Notable Passages

Verified against `raw/ACG+16_DeepLearningDP.pdf` on 2026-08-20.

> "We demonstrate that, by tracking detailed information (higher moments) of the privacy loss, we can obtain much tighter estimates on the overall privacy loss, both asymptotically and empirically."

— §1, contribution 1.

> "Proving the differential privacy guarantee of Algorithm 1 requires bounding the influence of each individual example on ˜g_t. Since there is no a priori bound on the size of the gradients, we clip each gradient in ℓ₂ norm."

— §3.1. Matched digit-insensitively; the subscript-2 glyph on the norm does not survive text extraction.

> "Our approach offers protection against a strong adversary with full knowledge of the training mechanism and access to the model's parameters."

— §1, on the threat model. No computational bound accompanies it anywhere in the paper.
