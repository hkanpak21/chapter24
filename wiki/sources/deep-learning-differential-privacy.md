---
title: Deep Learning with Differential Privacy
type: source
date_ingested: 2026-04-23
authors: [Martín Abadi, Andy Chu, Ian Goodfellow, H. Brendan McMahan, Ilya Mironov, Kunal Talwar, Li Zhang]
venue: CCS 2016
year: 2016
tags: [differential-privacy, deep-learning, privacy-preserving-ml, sgd, certification]
---

## Summary

This paper (ACG+16) introduces **DP-SGD** — the canonical mechanism for training deep neural networks under (ε, δ)-differential privacy — together with the **moments accountant**, a privacy-budget tracking technique that gives asymptotically and empirically tight bounds on composed privacy loss. The paper makes deep learning compatible with strong formal privacy guarantees for the first time at practical scales, and DP-SGD has since become the de facto privacy mechanism in production ML pipelines (Apple, Google, Meta, OpenAI).

The mechanism modifies standard SGD in four ways: (1) compute per-example gradients rather than batched gradients, (2) clip each per-example gradient's ℓ₂ norm to a threshold C, (3) add Gaussian noise calibrated to the clipping norm and a noise multiplier σ, (4) track cumulative privacy loss via the moments accountant. The per-example clipping bounds the sensitivity; Gaussian noise provides the DP guarantee; the moments accountant gives a tighter analysis than advanced composition because it tracks the *full distribution* of the privacy loss random variable rather than just its moments. Under Rényi-DP reformulation (later work), this is the source of near-optimal privacy-utility tradeoffs.

Experimental contributions include TensorFlow implementations, training deep networks on MNIST/CIFAR-10 with "single-digit" ε privacy budgets while preserving usable accuracy, and careful implementation strategies (lots, per-layer clipping, PCA projections for input-layer complexity reduction).

## Key Contributions

- **DP-SGD algorithm**: per-example clip + Gaussian noise + privacy accounting, implementable as a drop-in replacement for SGD.
- **Moments accountant**: tracks higher-order moments of privacy loss to give tight asymptotic and empirical bounds on composed (ε, δ)-DP.
- **Engineering techniques**: efficient per-example gradient computation, lots (sub-batches) to reduce memory, per-layer clipping and noise parameters, DP PCA projection for input layer.
- **Practical demonstration**: first DP-trained deep networks achieving useful accuracy on MNIST/CIFAR-10 under single-digit privacy budgets.
- **TensorFlow integration**: reference implementation enabling broad adoption.

## Key Definitions / Theorems

- **(ε, δ)-differential privacy** (Definition 1): Pr[M(d) ∈ S] ≤ e^ε · Pr[M(d') ∈ S] + δ for adjacent databases d, d'.
- **Gaussian mechanism**: M(d) = f(d) + N(0, S_f² σ²), satisfies (ε, δ)-DP if δ ≥ (4/5) exp(−(σε)²/2) and ε < 1.
- **DP-SGD (Algorithm 1)**: at each step, sample a lot with probability L/N, compute and clip per-example gradients to norm C, average, add N(0, σ²C²I) noise, take SGD step.
- **Moments accountant**: for each composition step, track log(E[exp(λ · PrivLoss)]) for multiple values of λ; yields the tightest (ε, δ) bound for the composed mechanism.

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

> "We demonstrate that, by tracking detailed information (higher moments) of the privacy loss, we can obtain much tighter estimates on the overall privacy loss, both asymptotically and empirically."

> "Proving the differential privacy guarantee of Algorithm 1 requires bounding the influence of each individual example on ˜g_t. Since there is no a priori bound on the size of the gradients, we clip each gradient in ℓ₂ norm."
