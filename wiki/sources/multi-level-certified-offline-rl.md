---
title: "Multi-Level Certified Defense Against Poisoning Attacks in Offline Reinforcement Learning"
type: source
date_ingested: 2026-04-23
authors: [Shijie Liu, Andrew C. Cullen, Paul Montague, Sarah Erfani, Benjamin I. P. Rubinstein]
venue: "arXiv:2505.20621 (May 2025); ICLR 2025"
year: 2025
tags: [reinforcement-learning, certified-robustness, poisoning, differential-privacy, offline-rl]
---

## Summary

This paper (LCMEBR25) provides **certified bounds against training-data poisoning** simultaneously at the per-state action level and the cumulative-reward level for **offline reinforcement learning**, using **Differential Privacy composition** across continuous/discrete and stochastic/deterministic environments. Substantially tightens prior COPA-style guarantees (certified radius ~5× larger at 7% poisoning).

The multi-level structure:
1. **Per-state certification**: for each state, the policy's chosen action is robust to ε-poisoning.
2. **Cumulative-reward certification**: over a trajectory, the total discounted reward is robust to ε-poisoning.

The two levels are jointly certified via DP composition, allowing tighter bounds than separate analyses. The paper is the **RL-counterpart to certified classification** in the wiki — applying the DP-based framework of [PixelDP (LAGHJ19)](certified-robustness-differential-privacy.md) and [Cohen et al. (CRK19)](certified-robustness-randomized-smoothing.md) to the offline-RL setting.

## Key Contributions

- **Multi-level certification**: per-state + cumulative-reward simultaneously.
- **DP composition across environment types**: continuous/discrete, stochastic/deterministic.
- **5× tighter certified radius** vs. prior COPA framework at 7% poisoning.
- **RL-counterpart to certified classification**: fills a deployment-relevant gap.

## Connections

- Source: [Deep Learning with DP (ACG+16)](deep-learning-differential-privacy.md) — DP framework.
- Source: [Certified Robustness via Randomized Smoothing (CRK19)](certified-robustness-randomized-smoothing.md) — smoothing foundation.
- Source: [PixelDP (LAGHJ19)](certified-robustness-differential-privacy.md) — DP-based certified robustness.
- Source: [Certified Defenses for Data Poisoning (SKL17)](certified-defenses-data-poisoning.md) — predecessor framework for classification poisoning.
- Source: [Robustly-Reliable Learners (BBHS22)](robustly-reliable-learners-poison.md) — instance-targeted certificates.
- Concept: [Poisoning Attacks](../concepts/poisoning-attacks.md).
- Concept: [Certified Robustness](../concepts/).

## Quotes / Notable Passages

> "Certified bounds against training-data poisoning simultaneously at the per-state action level and the cumulative-reward level for offline RL, using Differential Privacy composition. Certified radius ~5× larger at 7% poisoning compared to prior COPA-style guarantees."
