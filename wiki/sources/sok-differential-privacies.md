---
title: "SoK: Differential privacies"
type: source
date_ingested: 2026-08-20
authors: [Damien Desfontaines, Balázs Pejó]
venue: Proceedings on Privacy Enhancing Technologies (PoPETs) 2020(2):288–313
year: 2020
tags: [differential-privacy, adversary-knowledge-taxonomy, attack-taxonomy-llms, impossibility-frameworks]
claim_quantifier: universal
antecedent: none (a survey; individual catalogued results carry their own antecedents)
adversary_bound: varies by dimension — the survey's dimension C is the runtime axis, occupied by PPT only
---

## Summary

The systematization that **names the computational axis** and shows how thin it is. Roughly 200
differential-privacy variants are partitioned into seven dimensions, chosen to satisfy mutual
compatibility (variants from different dimensions combine) and inner exclusivity (variants within a
dimension do not). The dimensions are derived by reformulating the DP guarantee and highlighting each
modifiable aspect:

> "An attacker with perfect background knowledge (B) and unbounded computation power (C) is unable (R) to
> distinguish (F) anything about an individual (N), uniformly across users (V) even in the worst-case
> scenario (Q)."

Dimension **C — Computational power** answers "How much computational power can the attacker use?" with
usual motivation "Combining cryptography techniques with DP." §9 catalogues its occupants and there are
essentially two: `ε_κ`-IndCDP and `ε_κ`-SimCDP, both from
[MPRV09](computational-differential-privacy.md), plus output-constrained DP as a two-party instantiation
and computational zero-knowledge privacy as a simulator-bounded variant. The relation table records
`ε_κ`-IndCDP ≺ `ε_κ`-SimCDP and `ε_κ`-SimCDP ≺ `ε`-DP.

The axis therefore has **one bit of resolution**: unbounded, or polynomial-time. Nothing between, nothing
graded, no exponent. And the survey's assessment of its practical use is blunt: "Limiting the computational
power of the attacker is a reasonable assumption, but for a large class of queries, it cannot provide
significant benefits over classical DP in the typical client-server setting [79]. Thus, existing work using
it focuses on multi-party settings [13]." Reference [79] is [GKY11](limits-cdp-client-server.md), and note
that the survey states it in the correctly bounded form — "for a large class of queries" — not the folk
universal.

The counting argument in the conclusion is the useful headline number: with only three options per
dimension there would be `3⁷ = 2187` possible definitions, so "the ≈ 200 existing definitions shown in
Figure 1 are only scratching the surface of the space of possible notions." The corollary for our purposes
is that the axis the programme cares about is the one nobody populated.

## Claim Boundary

- **Quantified over:** all data privacy definitions based on DP that the authors could find and that meet
  their inclusion criterion (the attacker's capabilities must be clearly defined and the definition must
  prevent that attacker from learning something).
- **Antecedent:** none for the taxonomy itself. The dimension framework rests on the authors' two stated
  properties (mutual compatibility, inner exclusivity) and on a design choice about DP's interpretation:
  the reformulation above adopts the **strong adversary assumption** (the adversary knows all data points
  except one) rather than the independence assumption, because the associative view of DP requires one or
  the other. Under the causal view no such assumption is needed.
- **Excluded cases:** §10.2 lists definitions excluded by the inclusion criterion. `k`-anonymity and its
  descendants are out of scope, being dataset properties rather than process properties.
- **Does not establish:** any new impossibility or separation. It is a catalogue with a partial order and
  a properties table; where it asserts relations it either collects existing proofs or supplies new ones,
  and it does not claim exhaustiveness.
- **Abstract vs theorem:** none found.

## Key Contributions

- Seven dimensions: **Q** quantification of privacy loss, **N** neighborhood definition, **V** variation of
  privacy loss, **B** background knowledge, **F** formalism change, **R** relativization of knowledge gain,
  **C** computational power.
- Explicit recognition of computational power as a first-class axis of the definition space, and the
  demonstration that it has one occupant family.
- A partial order of relative strength across ~200 notions, plus a table of which satisfy the privacy
  axioms, composition, post-processing, convexity.
- The `3⁷` counting observation: the definition space is barely explored.

## Key Definitions / Theorems

- **Definition 21 (`ε_κ`-IndCDP [MPRV09]).** Distinguisher modelled explicitly as a non-uniform ppt Turing
  machine; `P[Ω(M(D₁)) = 1] ≤ e^{ε_κ} · P[Ω(M(D₂)) = 1] + neg(κ)`.
- **Definition 22 (`ε_κ`-SimCDP [MPRV09]).** Existence of an `ε_κ`-DP family `M'_κ` with
  `|P[Ω(M(D)) = 1] − P[Ω(M'(D)) = 1]| ≤ neg(κ)`.
- Recorded relations: `ε_κ`-SimCDP ⟹ `ε_κ`-IndCDP; `ε_κ`-SimCDP ≺ `ε`-DP.

## Connections

- Concept: [computational differential privacy](../concepts/computational-differential-privacy.md) — this
  survey is the census of that concept's population.
- Concept: [adversary knowledge taxonomy](../concepts/adversary-knowledge-taxonomy.md) — dimension **B** is
  that axis.
- Reproduces the definitions of [MPRV09](computational-differential-privacy.md).
- Cites [GKY11](limits-cdp-client-server.md) in bounded form, as noted above.
- Its dimension list has **no function-class axis**, so [CIM19](capacity-bounded-dp.md) and
  [DM22](kernel-quantum-renyi-audit.md) do not fit any of the seven cleanly; they are neither B nor C.
  Worth flagging as a gap in the taxonomy rather than in the papers.
- [CHSS24](attaxonomy.md) and [SAH+25](adversary-aware-dp-bounds.md) taxonomize **attacks** rather than
  definitions, and neither has a computational axis either.
- Concept: [attack taxonomy for LLMs](../concepts/attack-taxonomy-llms.md).

## Open Questions / Limitations

- The `3⁷` gap: most of the definition space is unpopulated, and dimension **C** in particular is
  populated only at its two extremes.
- The survey does not resolve the associative-versus-causal interpretation debate; it records that the
  choice changes which variants are meaningful.

## Quotes / Notable Passages

> "How much computational power can the attacker use?"

> "Limiting the computational power of the attacker is a reasonable assumption, but for a large class of
> queries, it cannot provide significant benefits over classical DP in the typical client-server setting"

> "the ≈ 200 existing definitions shown in Figure 1 are only scratching the surface of the space of possible
> notions."
