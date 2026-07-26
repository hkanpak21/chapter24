---
title: Revealing Information while Preserving Privacy
type: source
date_ingested: 2026-07-26
authors: [Irit Dinur, Kobbi Nissim]
venue: PODS (Principles of Database Systems)
year: 2003
tags: [cryptography, complexity theory, hardness-reductions, sample-complexity, reconstruction]
---

> **Provenance.** Ingested from a verified prior-art sweep (section headings and quoted passages
> extracted from the primary PDF), not from a full read. Marked passages are verbatim. A full read is
> still owed — this is the founding paper of the reconstruction literature and the programme now
> depends on knowing exactly what it proves.

## Summary

The founding result of the data-reconstruction literature, and — this is why it matters here — the
first paper to make the **statistical/computational separation** its main theorem rather than a remark.

A curator holds a database of `n` bits and answers subset-sum queries with perturbation. The question
is how much noise is needed to prevent an adversary from reconstructing the database. The answer
depends on the adversary's computational budget, and the paper is organized around that dependence:
**§3 treats the "Exponential Adversary"; §4 treats the "Polynomially Bounded Adversary."** Against an
unbounded adversary, `Ω(n)` perturbation is required. Against a time-`T` bounded adversary, `Õ(√T)`
suffices — for polynomial `T`, `Ω(√n)`.

The reconstruction task is explicitly framed as a search problem over a large solution set. The paper
notes the candidate list is *"exponential in size, so our goal is not to compute the entire list, but to
come up with one such"* — i.e. the set of consistent databases is huge, enumerating it is hopeless, and
**finding a single point in it is the attack.**

## Key Contributions

- The `Ω(√n)` perturbation threshold for polynomially-bounded adversaries, versus `Ω(n)` for unbounded
  ones — a genuine complexity separation in a privacy setting.
- The linear-programming reconstruction attack, which for least-squares-style mechanisms recovers the
  database from noisy aggregates.
- Framing reconstruction as *find one consistent database*, not *characterize all of them*.
- The intellectual ancestor of differential privacy (Dwork et al. 2006) — DP exists because this attack
  works.

## Key Definitions / Theorems

- **Abstract (verbatim):** for time-`T` bounded adversaries, privacy is preserved with perturbation
  `≈ Õ(√T)`; against unbounded adversaries linear `Ω(n)` noise is required.
- **§3 Exponential Adversary** — the information-theoretic bound.
- **§4 Polynomially Bounded Adversary — `Ω(√n)` Perturbation Needed for Privacy** — the computational
  bound. The gap between §3 and §4 is the result.

## Connections

- **Supersedes the central claim of [fibers-of-the-training-map](../../output/fibers-of-the-training-map.md).**
  The size-versus-navigability distinction developed there, and its ordinary-least-squares worked
  example, are this paper. See [native-asymmetry-in-learning](../analyses/native-asymmetry-in-learning.md).
- Restated for the modern setting by [Kaplan–Mansour–Nissim–Stemmer](kaplan-bayesian-memorization-reconstruction.md)
  as computational versus statistical memorization.
- Given a computational security definition by [Cohen et al. ITCS'25](cohen-data-reconstruction.md).
- [DP-SGD (ACG+16)](deep-learning-differential-privacy.md) — the descendant defence.
- Concept: [fiber-of-the-training-map](../concepts/fiber-of-the-training-map.md).

## Open Questions / Limitations

- The setting is a query-release mechanism over a bit database, **not** a training map. Whether the
  separation transfers to `D ↦ w` is the open question the programme inherits.
- The attack is linear-algebraic; it says nothing about mechanisms whose consistency conditions are
  higher-degree.

## Quotes / Notable Passages

> "exponential in size, so our goal is not to compute the entire list, but to come up with one such"
