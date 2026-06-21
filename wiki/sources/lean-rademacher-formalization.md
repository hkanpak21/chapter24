---
title: Lean Formalization of Generalization Error Bound by Rademacher Complexity and Dudley's Entropy Integral
type: source
date_ingested: 2026-04-12
authors: [Sho Sonoda, Kazumi Kasaura, Yuma Mizuno, Kei Tsukamoto, Naoto Onda]
venue: arXiv (AutoRes / RIKEN AIP)
year: 2026
tags: [learning-theory, formal-verification, lean, rademacher-complexity, certification]
---

## Summary
This paper presents a mechanically-checked Lean 4 formalization (repository: `auto-res/lean-rademacher`) of the classical Rademacher-complexity route to generalization bounds, built on Mathlib's measure-theoretic probability infrastructure. The pipeline covers: (i) empirical and expected Rademacher complexity definitions over product measures, (ii) a formal symmetrization argument yielding E[sup|empirical − population|] ≤ 2·ℜ_n, (iii) a bounded-differences (Lipschitz) property of the uniform-deviation functional, (iv) a fully-proved McDiarmid inequality giving high-probability tail bounds UD_n ≤ 2ℜ_n + b√(2 log(1/δ)/n), and (v) extension from countable to separable topological index sets via a countable-dense reduction.

Worked applications mechanize: empirical Rademacher bounds for ℓ₂-regularized linear predictors (O(XW/√n)) and ℓ₁-regularized linear predictors (O(X_∞ W √(log d / n)) via a Massart-type finite-class lemma), plus a formally-verified Dudley entropy integral bound ℜ̂_n^(no abs)(F;S) ≤ 4ε + (12/√n) ∫_ε^{c/2} √(log N(u)) du via covering numbers and a chaining construction.

The contribution is methodological: a reusable Lean formal infrastructure for modern learning theory at textbook fidelity (Mohri et al., Wainwright), going beyond prior VC-dimension/finite-class formalizations (Bagnall & Stewart 2019 in Coq; Tassarotti et al. 2021 for decision stumps in Lean 3). A key technical innovation is handling measurability of suprema over uncountable parameter spaces via reduction to a countable dense subset.

## Key Contributions
- First systematic Lean 4 formalization of Rademacher-complexity–based generalization analysis.
- Formal McDiarmid inequality in Lean 4 (independent of and complementing Isabelle/HOL AFP and Mathlib's existing Azuma–Hoeffding).
- Reusable lifting mechanism from countable to separable topological index sets for measurability of suprema.
- Mechanized worked examples: ℓ₂ and ℓ₁ linear-predictor Rademacher bounds, Dudley entropy integral.
- Discussion of Lean-specific design choices: product measures as primitive instead of i.i.d. sequences; avoidance of conditional expectations in McDiarmid proof via independence.

## Key Definitions / Theorems
- **Signs, empiricalRademacherComplexity, rademacherComplexity, uniformDeviation** (FoML/Defs.lean): finite uniform averaging over {±1}^n; expected complexity via product measure μ^n.
- **abs_symmetrization_equation** (FoML/Symmetrization.lean): formal symmetrization identity.
- **expectation_le_rademacher** (FoML/Rademacher.lean): μ^n[sup_i |Σ_k f_i(X(ω_k)) − n·μ[f_i ∘ X]|] ≤ 2n · ℜ_n(f; μ, X).
- **uniformDeviation_bounded_difference** (FoML/BoundedDifference.lean): bounded-differences constant ≤ 2b/n.
- **uniform_deviation_tail_bound_countable_of_pos** / **_separable_of_pos** (FoML/Main.lean): full McDiarmid tail bound μ^n(2ℜ_n + ε ≤ UD_n) ≤ exp(−ε² n / (2b²)).
- **linear_predictor_l2_bound**, **linear_predictor_l1_bound**: concrete Rademacher bounds.
- **dudley_entropy_integral_bound** (FoML/DudleyEntropy.lean): chaining-based entropy integral bound.

## Connections
- Formalizes classical results underlying [PAC-learning](../concepts/pac-learning.md) and statistical learning theory.
- Complements [universal-law-of-robustness](../concepts/universal-law-of-robustness.md) and concentration-based arguments used in adversarial-ML work.
- Concept: [Mechanized/Lean-Formalized Learning Theory](../concepts/lean-formalized-learning.md) — this paper is the primary instance of the lean-formalization direction.
- Related formalization efforts: Bagnall & Stewart (Coq, finite classes), Tassarotti et al. (Lean 3, decision stumps), Yuanhe et al. 2026 (Lean, Gaussian Lipschitz + Dudley independently).
- Authors: [Sho Sonoda](../entities/sho-sonoda.md); institutions RIKEN AIP, CyberAgent, OMRON SINIC X, UCC, Tokyo.

## Open Questions / Limitations
- Covers Rademacher route only; does not mechanize VC-dimension theory, PAC-Bayes, or stability-based bounds.
- Uncountable F requires separability + first-countability; arbitrary measurable classes not covered.
- Integrability obligations are handled manually; no automation for routine measurability goals.
- Does not formalize adversarially-robust generalization bounds.

## Quotes / Notable Passages
"Our contribution is, to our knowledge, the first systematic formalization of generalization analysis via Rademacher complexity."

"A major methodological contribution is the systematic treatment of measurability obstacles: results are first established for countable hypothesis classes … and then lifted to separable topological parameter spaces through a countable dense reduction."
