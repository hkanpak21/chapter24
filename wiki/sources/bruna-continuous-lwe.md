---
title: Continuous LWE
type: source
date_ingested: 2026-04-12
authors: [Joan Bruna, Oded Regev, Min Jae Song, Yi Tang]
venue: STOC 2021 (the ingested PDF is arXiv:2005.09595v2, 24 Oct 2020, and does not itself state a venue)
year: 2021
tags: [lattice-cryptography, continuous-lwe, gaussian-mixtures, statistical-query, hardness-reductions, cryptography]
claim_quantifier: conditional
antecedent: "worst-case hardness of GapSVP and SIVP against quantum polynomial-time algorithms, for gamma at least 2 sqrt(n) with beta polynomially bounded. A standard lattice assumption."
algorithm_class: "all poly-time for the reduction-based hardness, SQ for the separate hCLWE lower bound"
adversary_bound: "quantum poly-time via the reduction"
date_verified: 2026-08-20
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: time
cls_tightness: conditional
cls_baseline: n/a
cls_second_party: none
cls_second_notion: algo class
cls_assessed: explicit
cls_evidence: "We give a polynomial-time quantum reduction from worst-case lattice problems to CLWE, showing that CLWE enjoys similar hardness guarantees to those of LWE."
cls_evidence_src: abstract
cls_reason: "party=learner: the bound binds whoever attempts to solve CLWE / learn the Gaussian mixture / build the Bubeck et al. robust classifier, not an MIA/extraction-style attacker. tightness=conditional since Thm 1.1's hardness rests entirely on the GapSVP/SIVP antecedent (front matter claim_quantifier=conditional). second_notion=algo class records the separate SQ lower bound for hCLWE (Claim Boundary: 'two different statements about two different classes'), same conceptual learner party under a second notion per rule 4b."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper introduces **Continuous LWE (CLWE)**, a continuous analogue of the Learning With Errors problem, and establishes it as computationally hard under standard worst-case lattice assumptions (via a polynomial-time quantum reduction from GapSVP/SIVP). In CLWE, equations in Z_q^n are replaced with inner products in R^n: given samples (y_i, z_i) with z_i ≈ γ⟨y_i, w⟩ mod 1 for random Gaussian y_i and secret unit vector w, recover w.

The main consequences:
1. **Resolves computational hardness of learning Gaussian mixtures** without separation (open since Diakonikolas 2016 / Moitra 2018): learning mixtures of Gaussians with non-overlapping components is computationally hard under lattice assumptions, even for mere density estimation.
2. **Addresses Bubeck et al. 2019** open question on the complexity of robust-ML-style Gaussian-pancake problems: CLWE's homogeneous variant (hCLWE) is hard, matching the SQ lower bounds of Diakonikolas-Kane-Stewart 2017.
3. **Opens new avenues for quantum attacks on lattice problems** — a CLWE algorithm implies a quantum lattice algorithm.

The noiseless variant of hCLWE is later shown by [Zadik-Song-Wein-Bruna 2022] to be *not* hard (LLL solves it), emphasizing that noise is essential to CLWE's hardness.

## Claim Boundary

- **Quantified over:** algorithms for CLWE, through a polynomial-time quantum reduction from worst-case lattice problems. The separate lower bound on homogeneous CLWE quantifies over statistical query algorithms.
- **Antecedent:** worst-case hardness of GapSVP and SIVP against quantum polynomial-time algorithms, in the parameter regime where gamma is at least 2 times the square root of n and beta is polynomially bounded. This is a standard lattice assumption.
- **Algorithm class:** all polynomial time for the reduction-based hardness, and SQ for the exponential lower bound on homogeneous CLWE. These are two different statements about two different classes and should not be merged into one.
- **Does not establish:** classical hardness. The reduction is quantum, as it is for LWE. It also says nothing about the noiseless case, where an LLL-based algorithm succeeds.
- **Abstract vs theorem:** none found. The abstract states that the reduction is quantum, and offers the reverse reading itself, that the result opens new avenues of quantum attacks on lattice problems.

## Key Contributions

- Definition of CLWE (search and decision) and homogeneous CLWE (hCLWE), the latter being a mixture of Gaussian "pancakes" along a hidden direction.
- **Main Theorem 1.1**: quantum poly-time reduction from worst-case GapSVP/SIVP to CLWE_{β,γ} for γ ≥ 2√n, β polynomially bounded.
- Hardness of density-estimation-style learning Gaussian mixtures without separation.
- Hardness of Bubeck et al.'s robust binary classification task.
- Exponential SQ lower bounds for hCLWE in the super-polynomial precision regime.

## Key Definitions / Theorems

- **CLWE_{β,γ}**: samples (y_i, z_i) with y_i ~ N(0, I_n), z_i = γ⟨y_i, w⟩ + ν_i mod 1, ν_i ~ N(0, β²); recover w.
- **hCLWE**: CLWE conditioned on z_i ≈ 0; mixture of Gaussian layers of spacing ≈ 1/γ, width ≈ β/γ along w.
- **Theorem 1.1 (informal)**: CLWE hardness ≡ worst-case lattice hardness (under quantum reductions).
- **SQ lower bound**: hCLWE is SQ-hard with super-polynomial precision (matching lattice hardness).
- **Analogy to LWE**: γ ↔ 1/noise in LWE; β ↔ relative noise α. Larger γ/β separation ↔ stronger LWE variant.

## Connections

- [Continuous LWE](../concepts/continuous-lwe.md) — concept page
- [Learning With Errors](../concepts/learning-with-errors.md)
- [Statistical Query Model](../concepts/statistical-query-model.md) — hCLWE matches SQ lower bound
- [Zadik Lattice Surpass SoS](zadik-lattice-surpass-sos.md) — noiseless hCLWE is poly-time solvable via LLL (not a contradiction; noise is essential)
- [Joan Bruna](../entities/joan-bruna.md), [Oded Regev](../entities/oded-regev.md)

## Open Questions / Limitations

- Reduction is quantum; classical reduction open (like LWE).
- Cryptographic applications mentioned but not explored; discretization needed.
- Noiseless variant easy via LLL — noise is essential.
- Can CLWE be used as foundation for cryptographic primitives distinct from LWE?

## Quotes / Notable Passages

> "Our work resolves an open problem regarding the computational complexity of learning mixtures of Gaussians without separability assumptions."

> "We interpret this as an encouraging sign that CLWE might be a better algorithmic target than LWE."

_Verified verbatim against `raw/BRST21_ContinuousLWE.pdf` on 2026-08-20. A note added earlier that day marked this passage as not found; that verdict was too broad. It failed only because an editorial gloss had been appended inside the quotation marks. The sentence itself is in Section 1 of the paper. The gloss, retained unquoted, read: suggests CLWE's continuous geometry may enable new lattice algorithm design. The claim the paper attaches to the sentence is narrower, namely that a simple moment-based algorithm solves CLWE in time exp(γ²) where the comparable lattice result needs a more involved argument._
