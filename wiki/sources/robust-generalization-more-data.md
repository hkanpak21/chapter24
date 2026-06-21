---
title: "Adversarially Robust Generalization Requires More Data"
type: source
date_ingested: 2026-04-23
authors: [Ludwig Schmidt, Shibani Santurkar, Dimitris Tsipras, Kunal Talwar, Aleksander Mądry]
venue: NeurIPS 2018 (arXiv:1804.11285)
year: 2018
tags: [adversarial-ml, sample-complexity, generalization, robust-pac-learning, information-theoretic]
---

## Summary

This paper (SSTTM18) establishes a **formal information-theoretic sample-complexity gap** between standard and adversarially-robust generalization. For a simple "Gaussian mixtures" binary classification problem (y ~ {±1}, x ~ N(yμ, σ²I) in d dimensions), the paper proves that standard classification is achievable with O(1) samples (independent of d), but adversarially robust classification under ℓ∞-bounded adversaries requires **Ω(√d)** samples. The gap is information-theoretic — it holds regardless of the learning algorithm or model family.

Experimentally, the paper demonstrates the same gap qualitatively on MNIST and CIFAR-10: adversarial generalization (adversarial test accuracy) lags standard generalization, and the lag is sample-complexity-shaped rather than algorithmic. This finding explains why adversarially-trained models on CIFAR-10 achieve substantially lower test accuracy than standard models even with state-of-the-art training procedures — the deficit is partly a data-efficiency issue, not just a training-procedure issue.

SSTTM18 is the natural complement to [Tsipras et al. 2019](robustness-at-odds-accuracy.md): where Tsipras et al. show that robust classifiers must learn *different features* (tradeoff persists at infinite data), SSTTM18 shows robust classifiers need *more data* to reach that feature-learning regime. Together, the two papers characterize two distinct costs of robustness — the sample-complexity premium and the accuracy premium.

## Key Contributions

- **Information-theoretic sample-complexity gap**: For the Gaussian-mixture binary task in d dimensions, standard generalization is achievable with O(1) samples, but ℓ∞-robust generalization requires Ω(√d) samples.
- **Lower bound holds for any algorithm**: the gap is not an artifact of specific training procedures — it is a property of the statistical problem.
- **Matching upper bound**: A simple estimator (thresholded mean) achieves O(√d) samples for robust classification, proving the gap is tight.
- **Empirical validation**: On MNIST and CIFAR-10, adversarial generalization gap is much larger than standard gap, and robust training accuracy improves substantially with more data (indicating the bottleneck is data, not algorithm).
- **Sample-complexity-shaped explanation** for why deep networks on CIFAR-10 fail to achieve high adversarial accuracy — dataset is too small for robust generalization.

## Key Definitions / Theorems

- **Gaussian-mixture problem**: y ~ Uniform{±1}, x | y ~ N(yμ, σ²I), d-dimensional.
- **Adversarial robustness at radius ε**: classifier f is ε-robust if P[∃ δ : ∥δ∥_∞ ≤ ε, f(x+δ) ≠ y] is small.
- **Theorem 1 (standard learnability)**: Standard accuracy within ε can be achieved with O(log(1/δ)/ε²) samples, independent of d.
- **Theorem 2 (robust lower bound)**: For robustness radius ≥ 1/4 (in the Gaussian-mixture setup), any learning algorithm requires Ω(√d) samples to achieve non-trivial ε-robust accuracy.
- **Theorem 3 (robust upper bound)**: A specific thresholded-mean classifier achieves ε-robust accuracy with O(√d / ε²) samples.

## Connections

- Source: [Robustness May Be at Odds with Accuracy (Tsipras et al. 2019)](robustness-at-odds-accuracy.md) — same MIT/Mądry group; SSTTM18 establishes the *sample-complexity* cost, TSETM19 establishes the *accuracy* cost.
- Source: [VC Classes Are Adversarially Robustly Learnable (Montasser-Hanneke-Srebro 2019)](vc-classes-adversarially-robustly-learnable.md) — the SSTTM18 sample-complexity gap motivated finer-grained characterization of robust PAC learnability.
- Source: [Robust PAC Learning Characterization (MHS 2022)](robust-pac-learning-characterization.md) — gives the tight characterizing dimension (global one-inclusion graph).
- Source: [Tolerant Robust PAC Learning (Ashtiani-Pathak-Urner 2025)](tolerant-robust-pac-learning.md) — achieves linear-in-VC sample complexity under tolerance relaxation.
- Source: [Empirically Measuring Concentration (MZME19)](empirically-measuring-concentration.md) — robustness gap may also be due to concentration; SSTTM18 adds the sample-complexity dimension.
- Concept: [Robust PAC Learning](../concepts/robust-pac-learning.md).
- Concept: [Sample Complexity](../concepts/) (implicit).
- Concept: [Evasion Attacks](../concepts/evasion-attacks.md).
- Authors: Aleksander Mądry (MIT), Dimitris Tsipras (MIT).

## Open Questions / Limitations

- **Specific to ℓ∞ perturbations on Gaussian-mixture distributions**; other perturbation models may have different sample-complexity scaling.
- **Gap is d^{1/2}**, not higher polynomial; whether natural distributions show larger gaps is open.
- **Sample-complexity gap conflated with computational cost** — the O(√d) upper bound requires a specific estimator; deep networks may not achieve it efficiently.
- **Semi-supervised / unlabeled-data augmentation** could partially close the gap; subsequent work (Carmon et al. 2019) explores this.

## Quotes / Notable Passages

> "The sample complexity of robust learning can be significantly larger than that of 'standard' learning, and this gap is information theoretic and holds irrespective of the training algorithm or the model family."

> "Our theoretical findings are complemented by experiments on popular image classification datasets and show that a similar gap exists in practice."
