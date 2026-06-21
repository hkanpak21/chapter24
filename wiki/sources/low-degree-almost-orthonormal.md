---
title: "Low-Degree Lower Bounds via Almost Orthonormal Bases"
type: source
date_ingested: 2026-04-23
authors: [Alexandra Carpentier, Simone Maria Giancola, Christophe Giraud, Nicolas Verzelen]
venue: "arXiv:2509.09353 (Sep 2025; v2 Jan 2026)"
year: 2025
tags: [low-degree-polynomials, statistical-computational-gaps, proof-technique, planted-problems]
---

## Summary

This paper (CGGV25) introduces a **new general-purpose proof technique** for low-degree lower bounds when the planted distribution itself has structure that kills L²-orthogonality of the natural polynomial basis. The method constructs an **almost-orthonormal polynomial basis** precisely in the statistical-computational-gap regime, recovers known bounds (planted clique, hidden subcliques, stochastic block model, seriation), and produces new ones.

The technical contribution solves a long-standing practical issue: classical low-degree analysis via Hermite or Walsh polynomials requires orthogonality of the polynomial basis with respect to the null distribution. For many natural planted problems, the planted distribution itself perturbs the basis just enough to break strict orthogonality, blocking the analysis. CGGV25's almost-orthonormal construction replaces the strict-orthogonality requirement with a near-orthogonality bound that suffices for the LD lower-bound argument.

Directly relevant to extending [Ghosal-Hair-Jain-Sahai STOC 2025](pke-from-planted-clique.md)-style reductions to further ML problems, and to tightening existing low-degree bounds where orthogonality obstructions previously prevented a clean analysis.

## Key Contributions

- **Almost-orthonormal polynomial basis construction**: general proof technique for LD lower bounds under planted distributions that disrupt orthogonality.
- **Recovery of known bounds**: planted clique, hidden subcliques, stochastic block model, seriation.
- **New bounds**: derived for several previously-unanalyzed planted-structure problems.
- **Toolkit extension**: the method is general-purpose and can be applied to new planted problems emerging in the 2026 literature.

## Connections

- Source: [Low-Degree Polynomials Survey (Wein 2025)](low-degree-polynomials-survey.md) — canonical reference; CGGV25 extends the technical toolkit.
- Source: [SQ Algorithms and Low-Degree Tests (BBHLS21)](brennan-sq-lowdegree-equivalence.md) — SQ-LD equivalence; CGGV25 tightens the LD side.
- Source: [Low-Degree Estimation (SW22)](low-degree-estimation-schramm-wein.md) — LD for estimation; CGGV25 adds detection-side techniques.
- Source: [Counterexamples to LD Conjecture (HW21)](holmgren-counterexamples-low-degree.md) — shows LD framework has limits; CGGV25 expands its reach within those limits.
- Source: [SOS Lower Bound for PC (BHKKMP)](barak-sos-lower-bound-planted-clique.md) — SOS analog; CGGV25 is LD parallel.
- Source: [LB in Latent Models (Even-Giraud-Verzelen 2025)](lb-latent-models-clustering.md) — same Verzelen; applies CGGV25-style techniques to clustering.
- Concept: [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md).
- Concept: [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md).
- Concept: [Planted Clique](../concepts/planted-clique.md).

## Quotes / Notable Passages

> "Low-degree lower bounds via almost orthonormal bases... Constructs an almost-orthonormal polynomial basis precisely in the statistical-computational-gap regime, recovers known bounds (planted clique, hidden subcliques, SBM, seriation), and produces new ones."
