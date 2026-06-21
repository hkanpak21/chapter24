---
title: "Adversarially Robust Learning: A Generic Minimax Optimal Learner and Characterization"
type: source
date_ingested: 2026-04-12
authors: [Omar Montasser, Steve Hanneke, Nathan Srebro]
venue: "NeurIPS 2022 (arXiv:2209.07369)"
year: 2022
tags: [adversarial-ml, PAC-learning, sample-complexity, robustness, learning-theory]
---

## Summary

This paper resolves the sample complexity characterization of adversarially robust PAC learning. The central contribution is the **global one-inclusion graph** — a generalization of Haussler, Littlestone, and Warmuth's classical one-inclusion graph — from which the authors derive both a minimax-optimal learner and a dimension that exactly characterizes robust learnability: qualitatively (which hypothesis classes H can be robustly learned) and quantitatively (how many samples are needed).

Prior to this paper, the robust learnability question was open: VC-dimension does not characterize robust PAC learnability (Montasser et al. COLT 2019 showed finite VC-dim classes can be robustly learned by improper learners but some cannot by proper learners). This paper closes the gap.

## Key Contributions

- **Global one-inclusion graph dimension**: A dimension D based on the global one-inclusion graph (a generalization of the classical one-inclusion graph from standard PAC learning) that exactly characterizes robust PAC learnability.
- **Characterization theorem**: H is robustly learnable if and only if D(H, U) < ∞, where U is the perturbation set. Sample complexity is Θ(D(H, U) / ε²) in the agnostic case.
- **Generic minimax-optimal learner**: An explicit (improper) learner achieving the minimax optimal sample complexity for any H and perturbation type U.
- **Suboptimality of local learners**: Proves that existing local approaches (learners that reason about each test point's neighborhood independently) are suboptimal — a global perspective is necessary.
- **Resolves open problem from COLT 2019**: Closes the gap between upper and lower bounds left open by Montasser, Hanneke, Srebro (COLT 2019).

## Key Definitions / Theorems

**Global one-inclusion graph**: For hypothesis class H and perturbation type U, the global one-inclusion graph G(H, U) captures how hypotheses h, h' ∈ H interact across the entire distribution of perturbation neighborhoods — not just locally at a single test point.

**Characterization theorem**: The robust sample complexity m_R(ε, δ, H, U) satisfies:
`m_R(ε, δ, H, U) = Θ̃(D(H,U)/ε² + log(1/δ)/ε²)`
where D(H, U) is the global one-inclusion graph dimension.

**Qualitative characterization**: H is robustly PAC learnable under perturbation U iff D(H, U) < ∞.

**Suboptimality of proper learning** (from COLT 2019): There exist H, U where the optimal improper robust sample complexity is finite but no proper learner achieves finite sample complexity. Confirmed and strengthened here.

**Global perspective necessity**: Any learner that is "local" (makes decisions based only on the local neighborhood structure around each test point) is suboptimal by a polynomial factor in general.

## Connections

- [Evasion Attacks](../concepts/evasion-attacks.md) — this paper characterizes the sample complexity of defending against them
- [Tolerant Adversarially Robust PAC Learning](tolerant-robust-pac-learning.md) — Ashtiani et al. (2025) simplify learning under a tolerance relaxation, building on this work
- [Omar Montasser](../entities/omar-montasser.md)
- [Nathan Srebro](../entities/nathan-srebro.md)
- [Steve Hanneke](../entities/steve-hanneke.md)
- Precedes and motivates [win-win-robust-learning.md](win-win-robust-learning.md) — once we know the right dimension, we can ask: is it efficiently computable?

## Open Questions / Limitations

- Computing D(H, U) efficiently: the characterizing dimension is not known to be efficiently computable for general H and U, making the optimal learner computationally intractable.
- Does the global one-inclusion graph perspective yield efficient algorithms for specific practical hypothesis classes (halfspaces, neural networks)?
- Agnostic robust learnability beyond the realizable case — do the same dimensions characterize agnostic robust learning?
- Connection to VC dimension: when does D(H, U) = VC(H)? Known for halfspaces under ℓₚ perturbations; open in general.

## Quotes / Notable Passages

> "The global perspective is necessary — local learners are suboptimal. Sample complexity of robust PAC learning is characterized by the global one-inclusion graph dimension."
