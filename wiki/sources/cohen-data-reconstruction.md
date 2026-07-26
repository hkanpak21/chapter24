---
title: "Data Reconstruction: When You See It and When You Don't"
type: source
date_ingested: 2026-07-26
authors: [Edith Cohen, Haim Kaplan, Yishay Mansour, Shay Moran, Kobbi Nissim, Uri Stemmer, Eliad Tsfadia]
venue: ITCS 2025
year: 2025
tags: [cryptography, one-way-functions, computational-indistinguishability, reconstruction, hardness-reductions]
---

> **Provenance.** Built from a verified sweep (definitions and quoted passages extracted from the
> primary PDF), not a full read. **This paper is the single most important obstacle to the programme's
> reconstruction corner and must be read in full before anything is written.**

## Summary

Introduces **Narcissus resiliency** as a security notion for data reconstruction, and — the part that
matters — gives it a **computational** form that is *equivalent to one-wayness*.

The central move is to define what it means for a mechanism to resist reconstruction in a way that
quantifies over efficient adversaries rather than all adversaries. Appendix C then shows this notion is
not merely analogous to cryptography but is cryptography: a function `f` is one-way **if and only if**
its associated mechanism is computationally Narcissus-resilient; and CPA-security of an encryption
scheme is likewise a Narcissus-resiliency statement.

The paper also states, plainly, the observation the programme had been treating as its own: large
mutual information between model and data does not imply an efficient attack exists.

## Key Contributions

- **Definition C.1 — computational Narcissus resiliency.** A poly-time-bounded security notion for
  reconstruction.
- **§C.1 "One-wayness as computational Narcissus resiliency"** — the equivalence, both directions.
- **§C.2 / §C.4** — private-key and public-key ciphertext indistinguishability recast as Narcissus
  resiliency; CPA-secure iff computationally Narcissus-resilient.
- Explicit treatment of the relationship between computational DP and reconstruction attacks.
- A Kolmogorov-complexity formulation of reconstruction success, with the note that verifying a valid
  attack is itself computationally hard assuming cryptography exists.

## Key Definitions / Theorems

- **Theorem (verbatim):** *"f is a one-way function if and only if `M_f` is
  `(0, neg(λ), {(U_λ, U_λ)})`-R-computationally-Narcissus-resilient."*
- **On computational DP (verbatim):** *"an efficient privacy attack (e.g., membership inference or
  reconstruction) implies that the algorithm is not computationally differentially private. But in the
  opposite direction, if an algorithm is not computationally differentially private, the privacy attack,
  while being efficient, could be very negligible."*
- **On size versus extractability (verbatim):** *"While large memorization (i.e., mutual information)
  implies that the algorithm is not differentially private, it does not imply the existence of an
  efficient attack. Indeed… these works are typically not constructive (i.e., they do not provide an
  efficient way to translate the memorization into an efficient privacy attack)."*

## Connections

- **Occupies "is the training map a one-way function."** The equivalence is already proved for the
  reconstruction setting; any programme statement of that form must position against Def C.1.
- Successor to [Dinur–Nissim PODS'03](dinur-nissim-revealing-information.md).
- Companion to [Kaplan et al. arXiv:2505.23658](kaplan-bayesian-memorization-reconstruction.md), same group.
- Concept: [one-way-functions](../concepts/one-way-functions.md),
  [fiber-of-the-training-map](../concepts/fiber-of-the-training-map.md),
  [computational-vs-statistical-memorization](../concepts/computational-vs-statistical-memorization.md).

## Open Questions / Limitations

- The mechanism `M_f` is a general mechanism, not specifically a *training* map with the structure of
  SGD on a data distribution. Whether the equivalence is informative for the training map, or merely
  applicable to it, is the gap worth measuring.
- They *discuss* the CDP/reconstruction relationship; they do not build the theory. That branch was
  verified open across the whole computational-DP line.

## Quotes / Notable Passages

See Key Definitions — the three verbatim passages above are the load-bearing ones for this programme.
