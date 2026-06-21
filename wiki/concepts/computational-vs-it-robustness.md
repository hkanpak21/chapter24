---
title: Computational vs Information-Theoretic Robustness
type: concept
tags: [adversarial-ml, cryptography, one-way-functions, hardness-reductions, robustness, complexity-theory]
---

## Definition

A classifier h for a classification task (X, Y, D) is:
- **Information-theoretically robust** under perturbation budget b if no (computationally unbounded) adversary can, given x ~ D and oracle access to h, produce x' with d(x, x') ≤ b and h(x') ≠ label(x) with probability > α.
- **Computationally robust** under budget b if no PPT / poly-size adversary can do so.

The **computational–IT gap** is the difference between these two notions. A task exhibits a meaningful gap if computational robustness is strictly stronger (in achievability) than IT robustness.

Formalized via game-based definitions (Garg–Jha–Mahloujifar–Mahmoody 2020, Definition 1) following the cryptographic tradition.

## Intuition

Analogous to the distinction in cryptography between one-time-pad (IT security) and stream ciphers / public-key crypto (computational security). IT security rules out *existence* of an attack; computational security rules out *efficient* finding of one. The latter is strictly weaker but sufficient in practice and enables fundamentally impossible tasks (e.g., encrypting long messages with short keys).

## Properties / Theorems

- **Positive: signatures + error-correction construction** (GJMM20, Theorem 8): for any IT-vulnerable classifier h_Q, can construct a wrapper h_P with computational robustness ≈ h_Q's clean risk but IT robustness as bad as h_Q's adversarial risk. Assumes OWFs.
- **Positive with tamper detection removed** (GJMM20, Theorem 14): even when the classifier must always output a label (no ⋆), a learning task exists with computational risk ≈ 0 but IT risk ≈ 1/2.
- **Negative/reverse (GJMM20, Theorem 18)**: a meaningful gap implies average-case NP-hardness (samplable satisfiable CNFs that cannot be solved with non-negligible probability).
- **Win-win hardness** (Degwekar–Nakkiran–Vaikuntanathan 2019): hardness of learning an IT-robust classifier implies OWFs.
- **Complementary to geometric/IT barriers**: concentration of measure (Mahloujifar et al.) and Universal Law of Robustness (Bubeck–Sellke) prove IT lower bounds; computational robustness can potentially beat these.

## Where It Appears

- [Computational Hardness for Robust Learning](../sources/computational-hardness-robust-learning.md) — main source (GJMM20)
- [Win-Win Robust Learning](../sources/win-win-robust-learning.md) — complementary hardness direction
- [Planting Undetectable Backdoors](../sources/planting-undetectable-backdoors.md) — same signature-based technique for backdoor undetectability
- [Complexity Theoretic Adversarial ML](../sources/complexity-theoretic-adversarial-ml.md)

## Related Concepts

- [One-Way Functions](one-way-functions.md)
- [Win-Win Theorem](win-win-theorem.md)
- [Computational Concentration of Measure](computational-concentration-of-measure.md)
- [Evasion Attacks](evasion-attacks.md)

## Open Questions

- Does the gap exist for *natural* tasks (image classification)?
- Beyond Hamming distance: ℓ_p and other metric spaces.
- Weaker crypto assumptions sufficient for constructions?
- Combining computational robustness with certified (smoothing-based) robustness.
