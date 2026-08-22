---
title: "Multi-Level Certified Defense Against Poisoning Attacks in Offline Reinforcement Learning"
type: source
date_ingested: 2026-04-23
authors: [Shijie Liu, Andrew C. Cullen, Paul Montague, Sarah Erfani, Benjamin I. P. Rubinstein]
venue: "arXiv:2505.20621v1 (27 May 2025); ICLR 2025 (the PDF header reads 'Published as a conference paper at ICLR 2025')"
year: 2025
tags: [reinforcement-learning, certified-robustness, poisoning, differential-privacy, offline-rl]
claim_quantifier: conditional
antecedent: "The learning algorithm M is differentially private — the paper instantiates it with the Sampled Gaussian Mechanism — and the cumulative reward is bounded in a range [0, b]. The certified bound also needs a lower bound on the clean policy's return J(pi), which is estimated by sampling."
adversary_bound: "none — the adversary has full knowledge of the MDP and unbounded computation. It is bounded by r, the number of trajectories or transitions it may add, delete, or alter, which is a counting budget on the training data."
date_verified: 2026-08-20
---

## Summary

This paper (LCMEBR25) provides **certified bounds against training-data poisoning** simultaneously at the per-state action level and the cumulative-reward level for **offline reinforcement learning**, using **Differential Privacy composition** across continuous/discrete and stochastic/deterministic environments. Substantially tightens prior COPA-style guarantees (certified radius ~5× larger at 7% poisoning).

The multi-level structure:
1. **Per-state certification**: for each state, the policy's chosen action is robust to ε-poisoning.
2. **Cumulative-reward certification**: over a trajectory, the total discounted reward is robust to ε-poisoning.

The two levels are jointly certified via DP composition, allowing tighter bounds than separate analyses. The paper is the **RL-counterpart to certified classification** in the wiki — applying the DP-based framework of [PixelDP (LAGHJ19)](certified-robustness-differential-privacy.md) and [Cohen et al. (CRK19)](certified-robustness-randomized-smoothing.md) to the offline-RL setting.

## Claim Boundary

- **Quantified over:** all poisoned datasets D̃ within a distance r of the clean dataset D, under one of two distance notions the paper defines. Definition 3.1 counts modified *trajectories* and models an adversary corrupting collection, so a change propagates to later transitions. Definition 3.2 counts modified *transitions* and models an adversary editing after collection, so changes do not propagate. The two give different guarantees and should not be conflated.
- **Antecedent:** Theorem 4.2 requires the learning algorithm M to preserve an outcomes guarantee under approximate or Rényi differential privacy, which the paper obtains by training with the Sampled Gaussian Mechanism. It requires the cumulative reward to lie in a bounded range [0, b]. And its bound J(π̃) ≥ e^(−ε)(J(π) − bδ) is stated in terms of J(π), the clean policy's return, which is not known and must be lower-bounded by sampling. Strip any of the three and the certificate does not follow.
- **Which party is constrained:** the adversary, in the number of trajectories or transitions it may change. The paper grants it full knowledge of the MDP and does not limit its computation. The *defender* is constrained in a way worth noting, since it is unusual in this cluster: the learner must be differentially private, so the training algorithm pays for the guarantee in noise and utility.
- **Does not establish:** that the certified radius reflects what an attacker can do. The bound degrades with the privacy budget through e^(−ε), so a useful radius requires a small ε and therefore a noisy learner. It also does not establish anything for reward functions outside [0, b] without the Appendix A.4 extension to real-valued returns, which the paper gives separately as Theorem A.3.
- **Abstract vs theorem:** none found. The abstract's headline numbers — performance dropping no more than 50% at up to 7% poisoning, and radii five times larger than prior work — are reported as empirical evaluations, and the theorems are stated with their DP antecedent in place.

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

> _Not a quotation from the paper. This characterization was carried over from a secondary survey artifact during an earlier ingest and was wrongly presented in quotation marks. Retained unquoted, corrected 2026-08-20; verify against the primary source before citing._
>
> Certified bounds against training-data poisoning simultaneously at the per-state action level and the cumulative-reward level for offline RL, using Differential Privacy composition. Certified radius ~5× larger at 7% poisoning compared to prior COPA-style guarantees.

The abstract's own words on the same point, verbatim:

> "we extend certified defenses to provide larger guarantees against adversarial manipulation, ensuring robustness for both per-state actions, and the overall expected cumulative reward."

The threat model, verbatim, which is where the adversary's freedom is stated:

> "The adversary, with full knowledge of the MDP, can observe all the historical transitions and alter transitions"
