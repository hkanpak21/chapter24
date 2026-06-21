---
title: Reliable Learning (Robustly-Reliable Learners)
type: concept
tags: [adversarial-ml, PAC-learning, poisoning-attacks, certification, learning-theory]
---

## Definition

A **robustly-reliable learner** L, given a (possibly adversarially corrupted) sample S', outputs a function L_{S'}: X → Y × R such that for every test x with L_{S'}(x) = (y, η), the following guarantee holds: if there exists an uncorrupted sample S labeled by some h* ∈ H with d(S, S') ≤ η (normalized Hamming), then y = h*(x).

In other words, the output is a **(label, correctness-confidence)** pair: the label is *guaranteed correct* as long as (a) the target concept is in H and (b) the adversary has corrupted at most an η fraction of the training data. Introduced by Balcan, Blum, Hanneke, Sharma (COLT 2022).

Generalizes: the reliable-useful learning model of Rivest–Sloan (1988) and the perfect selective classification model of El-Yaniv–Wiener (2012), both originally for noise-free data.

## Intuition

Stability certificates say "the learner's prediction doesn't change under bounded poisoning." Correctness certificates (this concept) say "the learner's prediction is *right* under bounded poisoning." The latter is qualitatively stronger: a trivial all-negative classifier trivially satisfies stability but not correctness.

The optimal reliable learner outputs the label everyone in H_η(S') = {h ∈ H : err_{S'}(h) ≤ η} agrees on, for the largest η achievable — i.e., uses the **agreement region of the η-version-space**.

## Properties / Theorems

- **Optimal learner** (Balcan et al. 2022, Theorem 3.1): L_{S'}(x) = (y, η) with η largest such that x ∈ Agree(H_η(S')). Pointwise optimal among all strongly robustly-reliable learners (Theorem 3.5).
- **Efficient via ERM oracle** (Theorem 3.2): O(|Y|) oracle calls suffice, forcing each candidate label at the test point.
- **Region size bound** (Theorem 3.3): RR^L(S, h*, η) ⊇ Agree(B^H_D(h*, 2η + ε)); controlled by the disagreement coefficient.
- **Efficient for linear separators under log-concave marginals** (Theorem 4.1).
- **Extends to active learning** against adaptive adversaries and to the agnostic setting.
- **Instance-targeting**: certificate holds even if the adversary knows x before committing corruptions.

## Where It Appears

- [Robustly-Reliable Learners Under Poisoning](../sources/robustly-reliable-learners-poison.md) — main source

## Related Concepts

- [Poisoning Attacks](poisoning-attacks.md)
- [Robust PAC Learning](robust-pac-learning.md)
- [Undetectable Backdoors](undetectable-backdoors.md) — complementary: some poisoning is cryptographically undetectable

## Open Questions

- Efficient (non-oracle) algorithms beyond linear separators under log-concave marginals.
- Combining with test-time robustness for simultaneous training/test-time certificates.
- Tight agnostic bounds for the η-robustly-reliable region.
