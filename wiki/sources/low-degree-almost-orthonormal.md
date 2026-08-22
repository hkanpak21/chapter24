---
title: "Low-Degree Lower Bounds via Almost Orthonormal Bases"
type: source
date_ingested: 2026-04-23
authors: [Alexandra Carpentier, Simone Maria Giancola, Christophe Giraud, Nicolas Verzelen]
venue: "Preprint. The ingested PDF is arXiv:2509.09353v2, 5 Jan 2026, and does not state a venue."
year: 2025
tags: [low-degree-polynomials, statistical-computational-gaps, proof-technique, planted-problems]
claim_quantifier: universal
antecedent: "none beyond the random graph models treated. The almost-orthonormality is proved in precisely the gap regimes, not assumed."
algorithm_class: "low-degree"
date_verified: 2026-08-20
---

## Summary

This paper (CGGV25) introduces a **new general-purpose proof technique** for low-degree lower bounds when the planted distribution itself has structure that kills L²-orthogonality of the natural polynomial basis. The method constructs an **almost-orthonormal polynomial basis** precisely in the statistical-computational-gap regime, recovers known bounds (planted clique, hidden subcliques, stochastic block model, seriation), and produces new ones.

The technical contribution solves a long-standing practical issue: classical low-degree analysis via Hermite or Walsh polynomials requires orthogonality of the polynomial basis with respect to the null distribution. For many natural planted problems, the planted distribution itself perturbs the basis just enough to break strict orthogonality, blocking the analysis. CGGV25's almost-orthonormal construction replaces the strict-orthogonality requirement with a near-orthogonality bound that suffices for the LD lower-bound argument.

Directly relevant to extending [Ghosal-Hair-Jain-Sahai STOC 2025](pke-from-planted-clique.md)-style reductions to further ML problems, and to tightening existing low-degree bounds where orthogonality obstructions previously prevented a clean analysis.

## Claim Boundary

- **Quantified over:** polynomials of bounded degree, for the random graph models treated, in the regimes where a statistical-computational gap arises.
- **Antecedent:** none beyond those model assumptions. The almost-orthonormality of the constructed basis is proved in precisely the gap regimes rather than assumed.
- **Algorithm class:** low-degree. The paper is a proof technique for low-degree lower bounds and introduces no other class.
- **Does not establish:** hardness against polynomial time for hidden subcliques, stochastic block models or seriation. It establishes low-degree lower bounds for them, and it identifies which polynomials optimize the low-degree criterion.
- **Abstract vs theorem:** none found.

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

> _Not a quotation from the paper. Checked against `raw/CV+25_AlmostOrthonormal.pdf` on 2026-08-20 and not found; this is the page title followed by a summary that an earlier ingest presented as quotation. Retained unquoted as a summary._
>
> Constructs an almost-orthonormal polynomial basis precisely in the statistical-computational-gap regime, recovers known bounds (planted clique, hidden subcliques, SBM, seriation), and produces new ones.

> "Focusing on random graph models, we construct a basis of polynomials that is almost orthonormal under P, in precisely those regimes where statistical-computational gaps arise."

> "We illustrate the effectiveness of our approach by recovering known low-degree lower bounds, and establishing new ones for problems such as hidden subcliques, stochastic block models, and seriation models."
