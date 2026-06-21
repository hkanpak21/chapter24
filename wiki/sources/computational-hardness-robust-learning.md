---
title: "Adversarially Robust Learning Could Leverage Computational Hardness"
type: source
date_ingested: 2026-04-12
authors: [Sanjam Garg, Somesh Jha, Saeed Mahloujifar, Mohammad Mahmoody]
venue: "ALT 2020 (arXiv:1905.11564)"
year: 2020
tags: [adversarial-ml, cryptography, one-way-functions, hardness-reductions, robustness, complexity-theory, evasion-attacks]
---

## Summary

This paper ([GJMM20]) provides the first formal evidence that computational hardness can be *positively leveraged* for adversarial robustness — in contrast to the prior complexity-theoretic literature (Bubeck et al. 2018; Degwekar–Nakkiran–Vaikuntanathan 2019) which used it to prove *negative* results about learnability. The central construction uses digital signatures and error-correcting codes to wrap any learning problem Q (with an information-theoretically vulnerable classifier) into a related problem P whose classifier is robust against polynomial-time adversaries but still vulnerable to unbounded ones.

This answers a question raised by Madry, Goldwasser, and others: can we build "cryptographic" robustness akin to stream-cipher encryption, where computational bounds on the attacker suffice for security? Prior to this work there was no provable evidence that crypto assumptions could help robust learning in any way. The converse is also proved: any non-negligible gap between the success of polynomial-time and unbounded adversaries implies average-case NP-hardness.

The authors give two constructions: (i) a "tamper-detection" variant where the classifier may output a special symbol ⋆ to flag suspected tampering, and (ii) a no-tamper-detection variant where the classifier must always produce a label. They also establish a learning problem where no polynomial-time learner can output any information-theoretically robust classifier, yet computationally robust classifiers exist — combining their construction with robust-hardness results of Degwekar–Vaikuntanathan.

## Key Contributions

- **Theorem 8 (main positive result)**: Given any learning problem Q with a classifier of risk α but adversarial risk β ≫ α under ℓ_0 (Hamming) perturbations, there exists a related problem P and classifier h_P such that: (i) computational (poly-time attacker) risk of h_P is at most α, while (ii) information-theoretic risk of h_P is ≈ β. Assumes one-way functions.
- **Game-based definition of computational robustness (Definition 1)**: Formal security game between challenger and attacker; attacker wins if it produces x' with HD(x, x') ≤ b, h(x') ≠ y, and h(x') ≠ ⋆.
- **Construction (Construction 7)**: Wrap (x, y) ~ D_Q by sampling a fresh signature keypair (vk_x, sk_x), attaching signed, error-correction-encoded (x, σ_x, [vk_x]). h_P verifies signature; outputs ⋆ on failure. Poly-time attacker cannot forge signatures; unbounded attacker can exhaustively search for a valid signature.
- **Theorem 14 (no tamper detection)**: Even without the ⋆ symbol, there is a binary-labeled classification problem with computational risk ≈ 0 but information-theoretic risk ≈ 1/2. Uses repeated signatures.
- **Corollary 9 (robustly-hard base problem)**: Combining with Degwekar–Vaikuntanathan 2019, one obtains a learning problem for which every poly-time learner outputs (w.h.p.) an IT-non-robust classifier, yet a computationally robust classifier exists.
- **Theorem 18 (reverse direction)**: If a learning task has an efficiently samplable distribution D and a classifier h with computational robustness α < information-theoretic robustness β (non-negligible gap), then there exists a samplable distribution over Boolean formulas φ that are satisfiable w.p. ≈ 1 yet no poly-time algorithm finds satisfying assignments with non-negligible probability. I.e., average-case NP-hardness is *necessary* for computational > IT robustness.

## Key Definitions / Theorems

**Security game (Def 1)**: Challenger samples S ~ D^m, trains h = L(S), samples test (x, y) ~ D, gives (x, y) and oracle access to h and D-sampler to adversary A; A outputs x'. A wins if (x = x' ∧ h(x) ≠ y) ∨ (x ≠ x' ∧ HD(x, x') ≤ b ∧ h(x') ≠ y ∧ h(x') ≠ ⋆).

**Computational risk**: Risk against all PPT (or poly-size) attackers.

**Information-theoretic risk**: Risk against computationally unbounded attackers.

**Construction 7 (signature-wrapped classifier)**:
- Sampler: draw (x, y) ~ D_Q; freshly generate signature keys (vk_x, sk_x); σ_x ← Sign(sk_x, x); output ((x, σ_x, [vk_x]), y) where [·] is an error-correcting encoding.
- Classifier h_P((x̃, σ̃, V)): decode V to vk; if Verify(vk, x̃, σ̃) = accept, output h_Q(x̃), else output ⋆.
- Hamming budget b ≪ |x|; error-correcting code requires Ω(|x|) bit changes to alter decoded vk.

**Theorem 18 technique**: A distinguisher between computational and IT adversaries yields an average-case NP-hard distribution via a standard "guess the attacker's witness" reduction.

## Connections

- [Win-Win Theorem for Robust Learning](win-win-robust-learning.md) — Degwekar–Nakkiran–Vaikuntanathan 2019, negative complementary result; [GJMM20] builds on the robust-hard problems they construct
- [Planting Undetectable Backdoors](planting-undetectable-backdoors.md) — Goldwasser et al. 2022; similarly uses digital signatures to separate poly-time from unbounded detection
- [Complexity Theoretic Adversarial ML](complexity-theoretic-adversarial-ml.md) — Mahloujifar thesis incorporates this work
- [Win-Win Theorem](../concepts/win-win-theorem.md) — contrasts with this paper's positive direction
- [One-Way Functions](../concepts/one-way-functions.md) (new)
- [Computational vs Information-Theoretic Robustness](../concepts/computational-vs-it-robustness.md) (new)
- [Evasion Attacks](../concepts/evasion-attacks.md)
- [Saeed Mahloujifar](../entities/saeed-mahloujifar.md), [Mohammad Mahmoody](../entities/mohammad-mahmoody.md), [Sanjam Garg](../entities/sanjam-garg.md), [Somesh Jha](../entities/somesh-jha.md)

## Open Questions / Limitations

- Applicability to natural learning tasks (image classification): the construction is artificial; do any practical problems exhibit a meaningful computational–IT robustness gap?
- Can the construction be generalized beyond Hamming distance to ℓ_p metrics?
- Weakening the crypto assumption: OWFs used here; can weaker assumptions (average-case hardness of single problems) suffice?
- Connection to randomized-smoothing-style certified defenses: can computational-robustness certificates be combined with them?

## Quotes / Notable Passages

> "Computational limitation of attackers can indeed be useful in robust learning by demonstrating the possibility of a classifier for some learning task for which computational and information theoretic adversaries of bounded perturbations have very different power."

> "Non-trivial computational robustness implies computationally hard problems in NP."
