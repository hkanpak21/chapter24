---
title: PAC Learning
type: concept
tags: [learning-theory, pac-learning, sample-complexity, computational-learning]
---

## Definition

**Probably Approximately Correct (PAC) learning** [Valiant 1984] is the foundational framework of computational learning theory. A concept class C over instance space X is PAC-learnable if there exists an algorithm A such that for any distribution D over X, any concept c ∈ C, and any ε, δ > 0, given m(ε, δ) = poly(1/ε, 1/δ) i.i.d. samples labeled by c, A outputs a hypothesis h with **Pr_{D}[h(x) ≠ c(x)] ≤ ε** with probability at least 1 − δ over the random samples.

**Key parameters**: sample complexity m(ε, δ), error parameter ε, confidence parameter δ.

**Efficient PAC learning** additionally requires the algorithm to run in poly(1/ε, 1/δ, n, size(c)) time.

## Intuition

PAC learning formalizes "with high probability, the learner outputs an approximately correct hypothesis." It is distribution-free over D but instance-specific to C. The framework decouples three questions: (1) *information-theoretic* learnability (sample complexity), (2) *computational* learnability (runtime), and (3) *representational* learnability (hypothesis class restrictions, proper vs. improper).

## Properties / Theorems

**VC-dimension characterization (Blumer-Ehrenfeucht-Haussler-Warmuth 1989)**: A concept class C is PAC-learnable iff VC(C) < ∞, with sample complexity Θ((VC(C) + log(1/δ))/ε).

**Fundamental Theorem of Statistical Learning**: For binary classification, ERM achieves PAC learning with sample complexity O(VC(C)/ε²) in the agnostic setting, O(VC(C)/ε) in the realizable setting.

**Proper vs. improper learning**: Some concept classes require improper learners (outputting h ∉ C) to achieve PAC-learnability with poly-time algorithms. The distinction is *qualitatively important* in adversarial settings ([Montasser-Hanneke-Srebro 2019](../sources/vc-classes-adversarially-robustly-learnable.md)).

**Agnostic PAC**: Extension where no c ∈ C is assumed to exactly label D; learner must output h with error close to inf_{c ∈ C} err_D(c).

**Adversarially robust PAC** ([Cullina-Bhagoji-Mittal 2018](../sources/pac-learning-evasion-adversaries.md), [Montasser-Hanneke-Srebro 2022](../sources/robust-pac-learning-characterization.md)): the learner must achieve low adversarial risk under a perturbation set. Characterized by the **global one-inclusion graph dimension**, not VC dimension.

## Where It Appears

- [PAC-Learning in the Presence of Evasion Adversaries](../sources/pac-learning-evasion-adversaries.md) — adversarial VC dimension.
- [VC Classes Are Adversarially Robustly Learnable](../sources/vc-classes-adversarially-robustly-learnable.md) — improper necessity.
- [Adversarially Robust Learning: A Generic Minimax Optimal Learner](../sources/robust-pac-learning-characterization.md) — full characterization.
- [Tolerant Robust PAC Learning](../sources/tolerant-robust-pac-learning.md) — tolerance relaxation.
- [Covert Learning](../sources/covert-learning.md) — PAC variant with crypto-style query privacy.
- [Lean Rademacher Formalization](../sources/lean-rademacher-formalization.md) — mechanized PAC-learning bounds.

## Related Concepts

- [Robust PAC Learning](robust-pac-learning.md) — adversarial extension.
- [Adversarial VC Dimension](adversarial-vc-dimension.md) — characterizing dimension for evasion-robust learning.
- [Statistical Query Model](statistical-query-model.md) — restricted PAC variant.
- [Covert Learning](covert-learning.md) — PAC with query privacy.

## Open Questions

- Tight sample complexity for adversarially robust PAC learning for specific classes (neural networks, decision trees).
- When does improper robust learning beat proper robust learning by more than a constant factor?
