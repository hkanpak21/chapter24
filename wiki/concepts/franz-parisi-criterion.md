---
title: Franz–Parisi Criterion
type: concept
tags: [franz-parisi, statistical-physics, free-energy, low-degree-polynomials, statistical-computational-gaps]
---

## Definition

The **Franz–Parisi (FP) criterion** [Bandeira-El Alaoui-Hopkins-Schramm-Wein-Zadik 2022] is a computational hardness criterion for high-dimensional inference problems, derived by formalizing the physics-based **Franz–Parisi potential** from the statistical physics of spin glasses.

Given a high-dimensional hypothesis testing problem (null Q, planted P = E_{u~μ} P_u), define:

- **Low-overlap likelihood norm**: LO(δ) := E_{u,v ~ μ} [ 1_{|⟨u,v⟩|≤δ} · ⟨L_u, L_v⟩_Q ], where L_u = dP_u/dQ.
- **Overlap threshold**: δ(D) := sup{ε ≥ 0 : Pr_{u,v ~ μ}[|⟨u,v⟩| ≥ ε] ≥ e^{-D}}.
- **Franz–Parisi Criterion**: FP(D) := LO(δ(D)).

A problem is **FP-hard at D deviations** if FP(D) = O(1) as n → ∞. Heuristically, FP(D) bounded suggests computational hardness of weak detection at runtime exp(Θ(D)).

## Intuition

The Franz–Parisi potential in physics measures the free-energy landscape seen by a random signal u when a reference configuration u₀ is equilibrated nearby. A free-energy barrier at moderate overlap δ(D) signals metastability — local algorithms (MCMC, AMP, Langevin) get trapped.

The rigorous translation: FP captures the "correlations between two planted signals of small overlap." If these correlations sum to O(1), no polynomial-time test using the data's local geometry can distinguish P from Q — hardness for a broad class of algorithms.

FP and low-degree (LD) are closely related: both "restrict" the χ²-divergence ‖L‖²_Q. LD restricts to low-degree projections; FP restricts to low-overlap pairs. The two restrictions turn out to be nearly equivalent in many settings.

## Properties / Theorems

- **FP-LD equivalence for Gaussian additive models** [Theorems 2.4/2.5]: FP(D) and LD(D log n) are within constant factors.
- **FP-LD for planted sparse models** [Theorem 3.7]: FP-hard ⟹ LD-hard (one direction only).
- **FP ⟹ MCMC hardness** [Corollary 2.18]: For Gaussian additive models, FP-hard implies local MCMC fails.
- **Counterexamples** (Section 4): FP and LD disagree for some problems; equivalence is model-dependent.
- **Application — sparse linear regression**: New LD lower bounds derived via FP [Theorem 3.10] that were hard to obtain directly.

## Where It Appears

- [Bandeira Franz-Parisi Criterion](../sources/bandeira-franz-parisi-criterion.md) — introducing paper

## Related Concepts

- [Low-Degree Polynomial Framework](low-degree-polynomial-framework.md) — closely related
- [Overlap Gap Property](overlap-gap-property.md) — spin-glass analogue for optimization problems
- [Statistical-Computational Gaps](statistical-computational-gaps.md)

## Open Questions

- Which class of problems admits FP ↔ LD equivalence?
- Does the FP criterion extend to non-Gaussian, discrete, or compositional noise models?
- Relationship between annealed FP (used in the paper) and quenched FP — do they give different predictions?
- Connection to replica-symmetry-breaking in statistical physics.
