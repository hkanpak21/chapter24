---
title: Robust PAC Learning
type: concept
tags: [adversarial-ml, PAC-learning, sample-complexity, robustness, learning-theory]
---

## Definition

Given hypothesis class H ⊆ Y^X and perturbation map U: X → 2^X (with U(x) ≠ ∅), the **robust risk** of h under distribution D is
`R_U(h; D) = E_{(x,y) ~ D} [sup_{z ∈ U(x)} 1[h(z) ≠ y]]`.

H is **agnostic robustly PAC learnable** w.r.t. U if there is a learning rule A and function m(ε, δ) such that for every distribution D, with probability ≥ 1−δ over S ~ D^m, R_U(A(S); D) ≤ inf_{h ∈ H} R_U(h; D) + ε.

**Realizable robust PAC learnable**: same but quantified over D with inf = 0.

**Proper** = A outputs in H; **Improper** = A may output in Y^X.

## Intuition

An extension of PAC learning where, at test time, an adversary is permitted to perturb each input within its U-neighborhood before it is fed to the classifier. The learner still sees clean i.i.d. training data; only the evaluation is adversarial.

## Properties / Theorems

- **Finite VC does not imply proper robust learnability** (Montasser–Hanneke–Srebro 2019): ∃ H with vc(H) ≤ 1, U such that no proper rule robustly learns H.
- **Finite VC implies improper robust learnability** (Montasser–Hanneke–Srebro 2019): For every H with vc(H) < ∞ and every U, an improper robust PAC learner exists (sample complexity possibly exponential in vc(H)).
- **Global one-inclusion graph dimension characterizes robust PAC learnability** (Montasser–Hanneke–Srebro 2022): H is robustly PAC learnable iff D(H, U) < ∞, with sample complexity Θ̃(D(H, U)/ε²).
- **Tolerant robust learning is linear in VC** (Ashtiani–Pathak–Urner 2025): if learner is measured against a strictly larger perturbation set V ⊃ U, sample complexity Õ(vc(H) · log(...) / ε) is achievable by simple RERM-and-smooth / RERM-and-discretize.
- **Computational robustness is strictly stronger than IT robustness under crypto** (Garg–Jha–Mahloujifar–Mahmoody 2020): there exist learning tasks where poly-time adversaries cannot win but unbounded adversaries can.
- **Win-win hardness** (Degwekar–Nakkiran–Vaikuntanathan 2019): hardness of robust learning implies OWFs.

## Where It Appears

- [PAC Learning with Evasion Adversaries](../sources/pac-learning-evasion-adversaries.md) — first formal definition
- [VC Classes are Adversarially Robustly Learnable](../sources/vc-classes-adversarially-robustly-learnable.md) — proper vs improper separation
- [Robust PAC Learning Characterization](../sources/robust-pac-learning-characterization.md) — characterization via global one-inclusion graph dimension
- [Tolerant Robust PAC Learning](../sources/tolerant-robust-pac-learning.md) — tolerance relaxation
- [Computational Hardness for Robust Learning](../sources/computational-hardness-robust-learning.md) — computational variant
- [Win-Win Robust Learning](../sources/win-win-robust-learning.md) — crypto hardness

## Related Concepts

- [Adversarial VC Dimension](adversarial-vc-dimension.md)
- [Evasion Attacks](evasion-attacks.md)
- [Win-Win Theorem](win-win-theorem.md)
- [Reliable Learning](reliable-learning.md)
- [Computational Concentration of Measure](computational-concentration-of-measure.md)

## Open Questions

- Efficiently computable characterizing dimension for natural H.
- Agnostic characterization beyond the realizable case.
- Practical algorithms for neural networks with provable robust PAC guarantees.
