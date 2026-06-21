---
title: "Provably Robust Adaptation for Language-Empowered Foundation Models (LeFCert, LeFCert-L, LeFCert-C)"
type: source
date_ingested: 2026-04-23
authors: [Yuni Lai, Xiaoyu Xue, Linghui Shen, Yulun Wu, Gaolei Li, Song Guo, Kai Zhou, Bin Xiao]
venue: "arXiv:2510.08659 (Oct 2025); Hong Kong Polytechnic University"
year: 2025
tags: [certified-robustness, foundation-models, few-shot, CLIP, randomized-smoothing, poisoning]
---

## Summary

This paper (LXS+25) introduces **LeFCert**, the first provably robust few-shot classifier tailored to **language-empowered foundation models (LEMs)** such as CLIP and GraphCLIP. The core construction is a **twofold trimmed-mean prototype** that blends textual and feature embeddings, with analytic upper/lower bounds on classification scores yielding certified accuracy under **worst-case support-set poisoning** (the attacker corrupts a bounded fraction of few-shot examples).

Two refinements extend the baseline:
- **LeFCert-L**: incorporates [randomized smoothing](certified-robustness-randomized-smoothing.md) to obtain **Lipschitz continuity** under dual feature+label budgets — the attacker can perturb both image features and text labels up to specified ℓ₂ radii.
- **LeFCert-C**: provides **collective certification** under a shared attack budget, tightening the guarantee when multiple attacks are correlated.

LeFCert extends Cohen-Rosenfeld-Kolter's randomized-smoothing framework from standard classification to the **few-shot foundation-model adaptation regime** — a significant deployment pattern for production AI systems (e.g., CLIP-based classifiers, zero-shot/few-shot LEM-based applications).

## Key Contributions

- **Twofold trimmed-mean prototype**: blends textual and image-feature embeddings with robust-statistics trimming.
- **Analytic score bounds**: upper/lower bounds on classification scores enable certified accuracy under support-set poisoning.
- **LeFCert-L**: combines trimmed-mean with randomized smoothing for dual feature+label-budget certification.
- **LeFCert-C**: collective certification under shared attack budget, sharper than per-attack analysis.
- **First certified defense for CLIP/GraphCLIP few-shot adaptation**: fills a deployment-relevant gap.
- **Extends CRK19 to few-shot foundation models**: structural adaptation of randomized smoothing to the LEM paradigm.

## Key Definitions / Theorems

- **Support-set poisoning model**: adversary corrupts up to k out of the few-shot support set; classifier must be robust to any such k-corruption.
- **Twofold trimmed-mean prototype**: for each class, remove top/bottom k/2 examples in each of the two embeddings (text, feature), then average the remainder.
- **Main theorem (LeFCert)**: certified robust accuracy bound as a function of poisoning budget, number of shots, and trimmed-mean threshold.
- **LeFCert-L theorem**: adds Lipschitz continuity via Gaussian smoothing, extending to continuous perturbation radii.
- **LeFCert-C theorem**: collective certification tighter by Ω(log n) under shared attack budget.

## Connections

- Source: [Certified Robustness via Randomized Smoothing (CRK19)](certified-robustness-randomized-smoothing.md) — foundational technique; LeFCert-L applies smoothing to LEMs.
- Source: [Certified Defenses for Data Poisoning (SKL17)](certified-defenses-data-poisoning.md) — predecessor certified poisoning framework.
- Source: [Robust Estimators in High Dimensions (DKKLMS16)](robust-estimators-high-dimensions.md) — trimmed-mean as robust statistic.
- Source: [Robustly-Reliable Learners (BBHS22)](robustly-reliable-learners-poison.md) — instance-level poisoning guarantees; complementary.
- Source: [SmoothAdv (SYL+19)](provably-robust-smoothadv.md) — randomized smoothing + adversarial training; LeFCert-L is the LEM analogue.
- Source: [RS-LLM-MAS (Hu et al. 2025)](rs-llm-multi-agent.md) — RS to multi-agent consensus; LeFCert is RS to few-shot LEMs.
- Concept: [Evasion Attacks](../concepts/evasion-attacks.md) — attack model includes feature-level attacks.
- Concept: [Poisoning Attacks](../concepts/poisoning-attacks.md) — support-set poisoning is the main threat.

## Open Questions / Limitations

- **Trimmed-mean threshold selection**: optimal k depends on attack budget; choosing without ground-truth is a hyperparameter-tuning challenge.
- **Other foundation-model architectures**: LeFCert is specific to CLIP / GraphCLIP; extension to GPT-4V, Gemini, or Llama-multimodal requires architecture-specific analysis.
- **Adversarial training integration**: can LeFCert combine with SmoothAdv-style training for tighter bounds?
- **Beyond few-shot**: in-context-learning and zero-shot settings have different threat surfaces; extensions open.

## Quotes / Notable Passages

> "The first provably robust few-shot classifier tailored to language-empowered foundation models (CLIP, GraphCLIP)."

> "A twofold trimmed-mean prototype that blends textual and feature embeddings, with analytic upper/lower bounds on classification scores yielding certified accuracy under worst-case support-set poisoning."
