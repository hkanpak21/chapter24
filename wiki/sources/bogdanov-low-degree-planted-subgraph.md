---
title: Low-Degree Security of the Planted Random Subgraph Problem
type: source
date_ingested: 2026-07-26
authors: [Andrej Bogdanov, Chris Jones, Alon Rosen, Ilias Zadik]
venue: TCC 2024
year: 2024
tags: [cryptography, planted-clique, statistical-query, computational-indistinguishability, hardness-reductions]
---

> **Provenance.** Verified sweep, not a full read. **This paper is the reason a claim written into
> `CLAUDE.md` on 2026-07-25 had to be retracted.**

## Summary

Proves low-degree hardness for detecting a planted random subgraph, and cashes it into cryptography:
communication-optimal multiparty private simultaneous messages (PSM) protocols and bit secret sharing
with share size `(1+ε)log n`.

The significance for this programme is definitional rather than technical. **Security here is
quantified over low-degree distinguishers** — an adversary class restricted by *algebraic shape*, not by
running time. That is precisely the move the programme had recorded as unclaimed. It is claimed, it
works, and it carries real cryptographic functionality.

The bound is stated as tight in three parameters simultaneously: the distinguisher's degree, its
advantage, and the number of leaked vertices.

## Key Contributions

- Low-degree hardness of planted-subgraph detection up to `k ≤ n^{1−Ω(1)}`, tight in degree, advantage,
  and leakage.
- Communication-optimal PSM protocols from that hardness.
- Bit secret sharing with share size `(1+ε)log n`.
- A working demonstration that **restricted-class adversaries can underwrite cryptographic
  constructions**, not merely hardness evidence.

## Key Definitions / Theorems

- Low-degree indistinguishability of the planted random subgraph distribution from the null, with
  matching tightness in the three parameters above.

## Connections

- **Retracts** the negative result recorded in [CLAUDE.md](../../CLAUDE.md) and in
  [native-asymmetry-in-learning](../analyses/native-asymmetry-in-learning.md) §3.1 — low-degree-bounded
  adversaries *do* appear in security definitions.
- Builds on / secures [ABIKN23 Cryptography from Planted Graphs](cryptography-from-planted-graphs.md).
- [PKE from Planted Clique (GHJS25)](pke-from-planted-clique.md) — the same programme of crypto from
  planted problems.
- [BBHLS21 SQ ≈ low-degree](brennan-sq-lowdegree-equivalence.md),
  [low-degree survey](low-degree-polynomials-survey.md).
- Concept: [statistical-query-model](../concepts/statistical-query-model.md).

## Open Questions / Limitations

- The restricted class is **low-degree**, over a *planted graph* instance. The programme's target class
  is SQ or exponent-bounded, over a *continuous learning* instance — related, not the same. What remains
  unclaimed after this paper is the **exponent** units, verified by citation-graph sweep.
- Methodological lesson recorded: this was missed by two sweeps because both searched the ML-security
  literature while the result lives in the crypto literature. **A novelty check must sweep the venue
  where the technique lives, not where the application lives.**

## Quotes / Notable Passages

*(Full read owed.)*
