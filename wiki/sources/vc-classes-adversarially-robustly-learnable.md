---
title: "VC Classes are Adversarially Robustly Learnable, but Only Improperly"
type: source
date_ingested: 2026-04-12
authors: [Omar Montasser, Steve Hanneke, Nathan Srebro]
venue: "COLT 2019 (arXiv:1902.04217)"
year: 2019
tags: [adversarial-ml, PAC-learning, sample-complexity, robustness, learning-theory]
---

## Summary

This is the foundational COLT 2019 paper (precursor to Montasser–Hanneke–Srebro 2022) establishing the first general separation between *proper* and *improper* adversarially robust PAC learning. The paper shows:

1. Finite VC dimension is **not sufficient** for proper robust PAC learning — there exist classes H with vc(H) = 1 and an adversary U such that no proper learning rule (including RERM) robustly learns H, even in the realizable case and with unbounded sample size.
2. Finite VC dimension **is sufficient** for improper robust PAC learning — for every H with finite VC and every perturbation map U, there is an improper learner achieving finite robust sample complexity (though possibly exponential in vc(H)).

The result overturns the pre-2019 consensus, based on uniform-convergence-style arguments (Cullina et al. 2018; Bubeck et al. 2018; Khim–Loh 2018; Yin et al. 2018), that RERM-style proper methods are adequate for adversarial robustness. It motivated the subsequent characterization program culminating in the global one-inclusion graph dimension of Montasser et al. 2022.

## Key Contributions

- **Theorem 1**: There exists H with vc(H) ≤ 1 and adversary U such that H is not properly robustly PAC learnable (even realizable).
- **Main positive result**: Every H with finite VC is improperly robustly PAC learnable under any perturbation U, via a sample compression scheme based on boosting over the dual class.
- **Gap between vc(H) and vc(L^U_H)**: For any m, there exists H with vc(H) ≤ 1 but the robust loss class has VC dimension ≥ m — so the naive "apply standard VC bounds to the robust loss class" argument is hopeless.
- **Uniform convergence is not necessary for robust learnability**: Places robust learning squarely in the "general learning" (Vapnik 1982) / Shalev-Shwartz et al. 2010 regime where ERM fails but the class is still learnable.
- **Sample complexity upper bound**: Realizable robust sample complexity m_R = Õ(vc(H) · vc*(H) / ε), where vc*(H) is the dual VC dimension, yielding at most exponential-in-vc(H) bounds.

## Key Definitions / Theorems

**Robust loss class**: L^U_H = { (x,y) ↦ sup_{z∈U(x)} 1[h(z) ≠ y] : h ∈ H }. RERM-based uniform convergence works iff vc(L^U_H) is finite.

**Theorem 1 (no proper learner)**: ∃ H with vc(H) ≤ 1 and U such that for every proper A: (X×Y)* → H, there exists a realizable distribution D and m ∈ N with Pr_{S~D^m}[R_U(A(S); D) > 1/8] ≥ 1/7.

**Construction** (Lemma 2): Place m points x_1,...,x_m with disjoint U-neighborhoods; for each bit string b ∈ {0,1}^m, define h_b labeling one fresh point in each U(x_i) where b_i = 1 as −1, everything else +1. Then vc(H) ≤ 1 but vc(L^U_H) ≥ m.

**Theorem (improper learnability)**: For every H with vc(H) < ∞ and every U, H is improperly robustly PAC learnable. The learner is constructed via α-boosting over the dual class plus sample compression (Moran–Yehudayoff style).

**Corollary**: Sample complexity is at most exponential in vc(H); tight bound left open (resolved by Montasser–Hanneke–Srebro 2022 via global one-inclusion graph dimension).

## Connections

- [Adversarially Robust PAC Learning Characterization](robust-pac-learning-characterization.md) — Montasser et al. 2022 resolves the quantitative gap left open here
- [Tolerant Robust PAC Learning](tolerant-robust-pac-learning.md) — Ashtiani–Pathak–Urner 2025 bypass the exponential blowup under a tolerance relaxation
- [PAC Learning with Evasion Adversaries](pac-learning-evasion-adversaries.md) — Cullina et al. 2018, the uniform-convergence predecessor this paper supersedes
- [Adversarial VC Dimension](../concepts/adversarial-vc-dimension.md)
- [Robust PAC Learning](../concepts/robust-pac-learning.md)
- [Evasion Attacks](../concepts/evasion-attacks.md)
- [Omar Montasser](../entities/omar-montasser.md), [Steve Hanneke](../entities/steve-hanneke.md), [Nathan Srebro](../entities/nathan-srebro.md)

## Open Questions / Limitations

- Quantitative sample complexity: is the exponential-in-vc(H) bound tight? (Resolved 2022 via global one-inclusion graph dimension — sometimes yes.)
- Proper-improper gap magnitude: how badly does proper fail quantitatively?
- Efficient algorithms for natural classes (halfspaces, neural nets).
- Agnostic case: the agnostic-to-realizable reduction (David–Moran–Yehudayoff 2016) is adapted here; full agnostic characterization open at time of writing.

## Quotes / Notable Passages

> "Any hypothesis class H with finite VC dimension is robustly PAC learnable with an improper learning rule. The requirement of being improper is necessary."

> "Previous approaches to adversarially robust generalization are not always sufficient, as all prior work we are aware of is based on uniform convergence of the robust risk."
