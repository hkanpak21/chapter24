---
title: Data Reconstruction Attack
type: concept
tags: [adversarial-ml, reconstruction, one-way-functions, computational-indistinguishability]
---

## Definition

A **data reconstruction attack** recovers training data from a trained model. Per
[Wen, Liu, Backes and Zhang](../sources/sok-data-reconstruction-attacks.md), the object is a map

```
A : M × K → D ,     D_rec = A^k(m) ,     |D_rec| = |D_tar|
```

from a target model `m` and *extra knowledge* `k` to a reconstructed dataset of the **same
cardinality** as the target — the cardinality constraint exists to block the degenerate adversary
that enumerates every pixel combination and thereby "contains" the training set.

Extra knowledge `K` factors on three axes: training type (static / dynamic), model access (black-box /
white-box), dataset access (none / similar distribution / same distribution).

Success is parameterized by a distance measure `µ`:

- **`µ`-exact reconstruction**: `µ(A^k(m), D_tar) = 0`.
- **`(ε, µ)`-approximate reconstruction**: `µ(A^k(m), D_tar) ≤ ε`.

## Intuition

Reconstruction is the dataset-level, search-flavoured cousin of membership inference, which is
sample-level and decision-flavoured. It is the strongest privacy failure: not "was this record used"
but "here are the records".

## The two things `ε` is not

`ε` above is a **reconstruction-quality tolerance**. It is not a security parameter and it does not
mention the adversary's resources. That matters because the same subfield has, elsewhere, a
computational notion:

- [Cohen, Kaplan, Mansour, Moran, Nissim, Stemmer and Tsfadia](../sources/cohen-data-reconstruction.md)
  define computational Narcissus resiliency (Def. C.1) over poly-time adversaries, and prove it
  **equivalent to one-wayness**.
- [Dinur and Nissim](../sources/dinur-nissim-revealing-information.md) separate an exponential
  adversary from a polynomially bounded one for reconstruction — the separation is the main theorem.
- [Kaplan, Mansour, Nissim and Stemmer](../sources/kaplan-bayesian-memorization-reconstruction.md)
  restate the split as
  [computational vs statistical memorization](computational-vs-statistical-memorization.md).

So there are two parallel literatures: one measuring *how good* a reconstruction is, one measuring
*how hard* reconstruction is. The 2025 SoK belongs to the first and does not cite the second.

## Properties / Theorems

- No evaluated attack achieves exact reconstruction on standard vision benchmarks (SoK §5.1).
- Reconstruction quality correlates with per-sample memorization; larger training sets lower both.
  Replicated on Swin and MAE, and in text (Vec2Text, prompt recovery). Correlational, not causal.
- Sample-level metrics (MSE, PSNR, SSIM, feature distance) miss coverage; train-a-model accuracy
  misses precision. Hence the SoK's `(S-Dis, α)` pair, where `α = |f(A^k(m))| / |D_tar|` is coverage.
- `µ`-exact reconstruction is "a necessary and insufficient condition for the perfect reconstruction,
  depending on the choice of measure µ" — the definition is a schema, not a closed predicate.

## Where It Appears

- [SoK: Data Reconstruction Attacks Against Machine Learning Models](../sources/sok-data-reconstruction-attacks.md)
- [Data Reconstruction: When You See It and When You Don't](../sources/cohen-data-reconstruction.md)
- [Dinur–Nissim, Revealing Information While Preserving Privacy](../sources/dinur-nissim-revealing-information.md)
- [Kaplan et al., Bayesian memorization and reconstruction](../sources/kaplan-bayesian-memorization-reconstruction.md)
- [Suliman et al., Data Forging Attacks in Practice](../sources/suliman-data-forging-attacks.md) — the
  constrained-navigation half.

## Related Concepts

- [Fiber of the Training Map](fiber-of-the-training-map.md) — reconstruction is a search in the fibre;
  the cardinality constraint is a constraint on which fibre elements count as an answer.
- [Computational vs Statistical Memorization](computational-vs-statistical-memorization.md)
- [One-Way Functions](one-way-functions.md)
- [Model Extraction](model-extraction.md), [Machine Unlearning](machine-unlearning.md) — the two
  neighbouring subfields with the same missing-predicate defect.

## Open Questions

- Reconciling the quality-metric literature with the computational-hardness literature. They use
  incompatible units and do not cite each other.
- Any adversary-resource term in a reconstruction success definition outside the crypto line. The SoK
  characterizes the adversary purely by *knowledge*; compute never appears.
- Whether the memorization–vulnerability correlation has a mechanism or a bound behind it.
