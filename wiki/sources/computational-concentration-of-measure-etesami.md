---
title: Computational Concentration of Measure — Optimal Bounds, Reductions, and More
type: source
date_ingested: 2026-04-12
authors: [Omid Etesami, Saeed Mahloujifar, Mohammad Mahmoody]
venue: SODA
year: 2020
tags: [concentration-of-measure, computational-complexity, adversarial-ml, evasion-attacks, poisoning-attacks, complexity-theory]
---

## Summary

This paper (EMM20) closes the gap between information-theoretic and computational concentration of measure on product distributions under Hamming distance. The information-theoretic (Talagrand) bound says: for any set S of measure ≥ ε in [μ₁ × ... × μ_n], a (1 − δ)-fraction of points have a neighbor in S at Hamming distance O(√(n · ln(1/εδ))). Prior work [MM19] gave a polynomial-time algorithm matching this bound only for sets of measure Pr[S] ≥ ω(1/√n); this paper resolves the open question, providing a poly(n, 1/ε, 1/δ)-time algorithm (MUCIO: MUltiplicative Conditional Influence Optimizer) that matches the information-theoretic bound for all non-negligible ε.

The algorithm is *online*: it fixes coordinates one at a time, using the change it makes only based on already-set coordinates, via a multiplicative update on the partial expectation oracle. The authors then develop a general framework of *algorithmic reductions* between concentration results in different metric probability spaces (requiring both an algorithmic Lipschitz mapping and an algorithmic coupling), and use it to lift computational concentration to high-dimensional Gaussian distributions under ℓ₁ by revisiting the proof of [B+97]. They also prove a computational McDiarmid inequality (concentration around the mean, not just around sets), which generalizes Theorem 3.2 to random processes and yields new polynomial-time biasing attacks against collective coin-tossing protocols.

Finally, they prove exponential *lower bounds* on the query complexity of nonadaptive algorithms and algorithms that only query membership at points close to the input, illustrating why MUCIO's adaptive, multiplicative design is necessary.

## Key Contributions

- **Optimal computational concentration (Theorem 1.1/3.2)**: For any non-negligibly measured set S in a product space, a poly(n, 1/ε, 1/δ)-time online algorithm MUCIO finds Hamming-neighbors in S at distance O(√(n ln(1/εδ))) from a typical sample.
- **MUCIO algorithm**: Multiplicative update on partial expectation oracles; tampers (or aborts) on coordinate i based on whether the "multiplicative influence" of changing w_i exceeds a threshold.
- **Algorithmic reductions framework**: A definition of computational concentration reduction across metric probability spaces using pairs of inverse Lipschitz / coupling mappings.
- **Gaussian ℓ₁ application**: Algorithmic version of [B+97] yielding computational concentration for Gaussians under ℓ₁.
- **Computational McDiarmid (Theorem 5.1)**: Polynomial-time algorithm that modifies √n coordinates to push any Lipschitz function to near its mean.
- **Application to coin-tossing**: For any n-round coin-tossing protocol, a poly-time tamperer who corrupts Õ(√n) messages can bias the output bit to ≈ 1.
- **Nonadaptive lower bounds (Theorem 6)**: Exponential query complexity for nonadaptive methods, and for methods that only query near the input.
- **Polynomial-time poisoning and evasion**: For robust learning problems with ε ≥ 1/poly(n), MUCIO gives polynomial-time evasion attacks matching the information-theoretic optimum (closing the regime ε < ω(1/√n) left open by MM19).

## Key Definitions / Theorems

- **MUCIO (Construction 1.2 / Section 3)**: adaptive, online coordinate-choosing algorithm using multiplicative conditional influence updates, parameter λ ≈ 1/√n.
- **Algorithmic reduction**: (Lipschitz_mapping, Coupling_mapping) pair — both polynomial-time — reducing computational concentration from one (X,d,μ) to another.
- **Theorem 3.2 (master theorem)**: Stated for general discrete random processes; implies product-space version and the random-process / coin-tossing version.
- **Corollary (polynomial-time attacks)**: Any non-negligible bad-event probability in robust PAC learning over product distributions + Hamming can be amplified to ≈ 1 by a polynomial-time attacker changing Õ(√n) coordinates.

## Connections

- Direct algorithmic strengthening of [The Curse of Concentration (MDM19)](curse-of-concentration.md)
- Resolves the open question of [MM19] on computational concentration for all non-negligible set sizes
- Extends [p-Tampering Model](../concepts/p-tampering-model.md): p-tampering gives O(p) bias; MUCIO's "choose-locations" model gives ≈ 1 bias with Õ(√n) tamperings — exponentially stronger
- Builds on [KKR18] / Komargodski-Raz-Kalai alternative proof of [LLS89]
- Synthesized in [A Complexity Theoretic Approach to Adversarial ML](complexity-theoretic-adversarial-ml.md)
- Related: [Computational Concentration of Measure](../concepts/computational-concentration-of-measure.md), [Evasion Attacks](../concepts/evasion-attacks.md), [Poisoning Attacks](../concepts/poisoning-attacks.md)

**Authors**: [Omid Etesami](../entities/omid-etesami.md), [Saeed Mahloujifar](../entities/saeed-mahloujifar.md), [Mohammad Mahmoody](../entities/mohammad-mahmoody.md).

## Open Questions / Limitations

- Algorithmic Talagrand inequality with *coordinate-dependent* costs α_i remains open.
- Computational concentration on non-product distributions (e.g., natural image distributions) remains open.
- Characterizing metric probability spaces where *no* polynomial-time attack exists (despite IT concentration) — the [GJMM20] positive separation shows this can happen with crypto assumptions on engineered problems.

## Quotes / Notable Passages

> "We resolve the open question about the computational concentration of measure in product spaces under Hamming distance with a (tight up to constant) computational concentration for all range of initial probabilities Pr[S] for the target set."

> "Our attackers *can choose* which blocks are the target of their tampering substitutions, but then achieve much stronger bias and almost fixing the output with much smaller o(n) number of tamperings."
