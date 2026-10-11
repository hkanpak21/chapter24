---
title: Kamalika Chaudhuri
type: entity
entity_type: author
tags: [differential-privacy, adversarial-ml, learning-theory, low-degree-polynomial-framework]
---

## About

UC San Diego. In this wiki she is the author of the closest thing the privacy literature has to a
**function-class-bounded adversary** — the adversary is restricted not in runtime but in the class its attack
algorithm is drawn from.

## Contributions / Works

- [Capacity Bounded Differential Privacy](../sources/capacity-bounded-dp.md) (CIM19) — `(H, Γ)`-capacity
  bounded privacy via restricted `f`- and Rényi divergences; conditional post-processing, convexity, parallel
  and non-adaptive sequential composition; Laplace, Gaussian, and Matrix Mechanism parameters for the linear
  class; a Pinsker-like inequality for restricted KL divergences; and an algorithmic generalization bound.
  The degree-indexed `(poly, Renyi)` family is the one place in the privacy literature where an adversary's
  strength is a graded quantity rather than a binary one.

## Connections

- Directly extended by [DM22](../sources/kernel-quantum-renyi-audit.md), which makes the same
  restrict-the-witness-class move with RKHS classes and names "the link of the learned kernel with adversaries
  with limited capacity" as unfinished work.
- Orthogonal to the runtime axis of [MPRV09](../sources/computational-differential-privacy.md); the relation
  between the two axes has never been established.
- Concepts: [capacity-bounded privacy](../concepts/capacity-bounded-privacy.md),
  [low-degree polynomial framework](../concepts/low-degree-polynomial-framework.md),
  [computational differential privacy](../concepts/computational-differential-privacy.md).
