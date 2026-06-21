---
title: (k, p)-Poisoning Model
type: concept
tags: [poisoning-attacks, byzantine, adversarial-ml, cryptography, federated-learning, complexity-theory]
---

## Definition

The **(k, p)-poisoning model** [Mahloujifar-Mahmoody-Mohammed, ICML 2019] is a corruption model for m-party collaborative protocols (coin tossing, federated / collaborative learning) that interpolates between static Byzantine corruption and p-tampering:

1. The adversary statically chooses k ≤ m parties to corrupt.
2. For each corrupted party P_i, the adversary may, for each of P_i's messages, sample from any distribution that is p-close in **total variation distance** to the honest distribution of that message.

Honest parties behave normally. The (k, p) corruption is **online** — the adversary does not need to know future messages.

## Intuition

Real multi-party systems face "partial partial" corruption: some parties are fully adversarial (Byzantine), but even compromised parties often leak only occasionally, and fully-trusted parties can suffer transient network-level corruption. The (k, p) model captures this spectrum: k measures how many parties are broken; p measures how deeply each is controlled. The result is that **bias / bad-event probability scales as Ω(k · p / m)** — both dimensions multiply in a unit-less, universal bound.

## Properties / Theorems

**Universal amplification theorem** [MMM19]: For any m-party protocol (coin-tossing or learning), any (k, p)-adversary can increase the probability of any "bad" Boolean property from μ to **μ^{1 − pk/m}**. Attack is polynomial-time, online, and uses only valid/correctly-labeled messages.

For small μ, the multiplicative bound expands as μ^{1 − pk/m} ≈ μ + Ω(pk/m · μ log(1/μ)), which explains the often-quoted "additive" rate Ω(pk/m) for Ω(1) initial error.

**Interpolation**:
- k = m: recovers p-tampering amplification μ → μ^{1−p}.
- p = 1: subsumes static k-corruption from secure multi-party computation with μ → μ^{1 − k/m}.

**ML application**: In m-party federated learning, (k, p)-adversary drives any bad property of the learned model from μ to μ^{1 − pk/m}, even against DP-SGD or secure aggregation (attack uses only public updates).

**Coin tossing**: Output bit biased from μ to μ^{1 − pk/m} from a single-round m-party coin-tossing protocol.

**Enabling technical result — generalized p-tampering**: For any discrete random process x = (x₁, ..., xₙ) with efficient conditional sampling and any bounded f: Supp(x) → [0,1], and any set distribution S over [n] with Pr[i ∈ S] = p (possibly correlated), there is a poly-time generalized-p-tampering attack raising E[f(x)] from μ to arbitrarily close to μ − p·E[f(x)^{1+p}]. For Boolean f, this becomes μ^{1 − p}. This allows correlated tamperable-coordinates, which prior p-tampering proofs [MM17, MDM18] could not handle and which is essential when k parties are corrupted.

## Where It Appears

- [Universal Multi-Party Poisoning Attacks](../sources/multi-party-poisoning.md) — introduced here
- [A Complexity Theoretic Approach to Adversarial ML](../sources/complexity-theoretic-adversarial-ml.md) — covered in synthesis

## Related Concepts

- [p-Tampering Model](p-tampering-model.md) — special case k = m
- [Poisoning Attacks](poisoning-attacks.md) — broader framework
- [Concentration of Measure](concentration-of-measure.md) — proof technique

## Open Questions

- Can cryptographic trusted setup or robust aggregation generically beat the Ω(kp/m) bound?
- Adaptive corruption: adversary chooses which k parties to corrupt based on transcript prefix — tight bounds open.
- Extension to non-Boolean output properties (e.g., approximate statistical properties of the trained model).
