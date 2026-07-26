---
title: A Bayesian Perspective on Memorization and Reconstruction
type: source
date_ingested: 2026-07-26
authors: [Haim Kaplan, Yishay Mansour, Kobbi Nissim, Uri Stemmer]
venue: "arXiv:2505.23658 (May 2025); ITCS 2026"
year: 2026
tags: [reconstruction, computational-indistinguishability, learning-theory, cryptography]
---

> **Provenance.** Built from a verified sweep; the quoted passages are verbatim from the paper's
> introduction. Full read owed.

## Summary

Asks directly whether *computational* memorization and *statistical* memorization can come apart, and
answers yes. Statistical memorization is high mutual information between the released model and a
training example; computational memorization is extractability by an attack. The paper puts forward a
new security definition — **Bayesian Extraction-Safe** — under which mechanisms provably resist
extraction, and exhibits examples separating the two notions.

**The important qualifier for this programme:** the separating example is *information-theoretic*, not
complexity-theoretic. Example 1.3 releases a parity `H` of the training set `S` with
`I(S;H | Nature) = nd/2`, yet even an **unbounded** attacker cannot guess noticeably more than half the
coordinates of any single row. So their axis is mutual-information versus extractability-with-side-
information, and not mutual-information versus *polynomial-time* extractability.

That leaves a seam: the poly-time version of their question is adjacent to, and not identical with,
what they proved.

## Key Contributions

- The explicit framing of computational versus statistical memorization as a question, with a
  separation.
- **Bayesian Extraction-Safe** security definition.
- Example 1.3 — high mutual information with no extraction, even unbounded.

## Key Definitions / Theorems

- **The question (verbatim):** *"Is there a difference between computational memorization and
  statistical memorization? Could a model be considered 'memorizing' under one definition but not the
  other?"*
- **The programme statement (verbatim):** *"We put forward a new security definition, computational in
  nature, such that algorithms that satisfy it are guaranteed to resist extraction attacks… Therefore
  these examples separate statistical from computational memorization."*
- **The motivating rhetorical (verbatim):** *"if it is impossible for an attacker to extract information
  from the model, then had the model really memorized it?"*
- **Example 1.3:** `I(S;H|Nature) = nd/2`, yet *"even given H, no attacker (even unbounded) can guess
  noticeably more than half of the coordinates of any single row in S."*

## Connections

- Companion to [Cohen et al. ITCS'25](cohen-data-reconstruction.md) — same group, same programme; that
  paper carries the one-wayness equivalence, this one the memorization framing.
- Modern restatement of [Dinur–Nissim PODS'03](dinur-nissim-revealing-information.md).
- **Occupies the framing of** [fibers-of-the-training-map](../../output/fibers-of-the-training-map.md) §5
  — with the seam noted above.
- Adjacent information-theoretic accounts: Achille–Soatto arXiv:1905.12213 (`I(w;D)` as a weak form of
  DP); [Xiao–Devadas PAC Privacy](../analyses/native-asymmetry-in-learning.md) CRYPTO 2023
  (adversary explicitly *"possibly computationally-unbounded"*).
- Concept: [computational-vs-statistical-memorization](../concepts/computational-vs-statistical-memorization.md).

## Open Questions / Limitations

- **The seam.** Their "computational" means extraction-based in the proof-of-knowledge sense, not
  time-bounded. A genuinely poly-time-bounded version of the same separation is not what they proved.
- Their examples are constructed, not natural training procedures.

## Quotes / Notable Passages

> "Is there a difference between computational memorization and statistical memorization?"
