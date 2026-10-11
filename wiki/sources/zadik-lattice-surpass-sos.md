---
title: Lattice-Based Methods Surpass Sum-of-Squares in Clustering
type: source
date_ingested: 2026-04-12
authors: [Ilias Zadik, Min Jae Song, Alexander S. Wein, Joan Bruna]
venue: COLT 2022 (the ingested PDF is arXiv:2112.03898v2, 7 Jan 2022, and does not itself state a venue)
year: 2022
tags: [lattice-methods, LLL, sum-of-squares, low-degree-polynomials, clustering, counterexamples, statistical-computational-gaps]
claim_quantifier: existential
antecedent: "exact noiselessness. The authors state that inverse-polynomial noise breaks the method."
algorithm_class: "none. This is an upper bound, and its bearing on the cluster is that it limits what low-degree and sum-of-squares lower bounds can be read to mean."
date_verified: 2026-08-20
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: time
cls_tightness: poly
cls_baseline: n/a
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: samples
cls_assessed: explicit
cls_evidence: "if n = d+1 then there is an LLL-based algorithm (Algorithm 1) which terminates in polynomial time and outputs exactly, up to a global sign flip, both the correct labels xi and the correct hidden direction u"
cls_evidence_src: Thm 1.1
cls_reason: "target/family/phase/access/write are all none: this is a planted-Gaussian-clustering/lattice-algorithm paper with no ML pipeline, no train data, model or output being attacked, per rule 8 (classify what the work claims). party=learner not attacker: the LLL algorithm plays a recovery/estimator role against a randomized planted model, not an adversarial-ML security game; front matter's own 'algorithm_class: none' rules out tightness=class, so the bound is recorded as ordinary poly-time instead. second_notion=samples: Thm 1.1 bounds the same party (the LLL algorithm) under two incomparable notions, time (poly) and samples (n=d+1), per rule 4b. baseline=stated: Thm 1.2's information-theoretic lower bound (n>=d-1 needed by any estimator) is the optimal baseline the poly-time algorithm's n=d+1 sample count is shown to match."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper shows that for certain noiseless/degenerate Gaussian clustering problems, LLL-based (Lenstra-Lenstra-Lovász) lattice reduction algorithms achieve the statistically optimal sample complexity (n = d+1 samples), provably surpassing both low-degree polynomial methods and the sum-of-squares hierarchy, which had been shown to fail up to n = Õ(d²). This is the first example where SoS and LD lower bounds are both active and both *broken* by a poly-time algorithm — a striking counterexample to the low-degree conjecture in structured settings.

The concrete problem is clustering Gaussian mixtures with degenerate covariance Σ = I - uu^T (equivalently: find a planted ±1 hypercube vector in a subspace, or noiseless non-Gaussian component analysis). The LLL-based algorithm recovers both the hidden direction u and the labels x_i from n = d+1 samples, which is information-theoretically optimal. Previous best poly-time bound was n ≫ d². Analogous successes apply to Planted Sparse Vector, hCLWE (noiseless Continuous LWE), and similar "noiseless" statistical problems.

The authors emphasize that LLL's success is brittle: adding inverse-polynomial noise breaks it (consistent with hCLWE being hard under lattice assumptions [Bruna-Regev-Song-Tang 2021]). This highlights noise as the crucial parameter separating LD/SoS-predicted hardness from actual hardness.

## Claim Boundary

- **Quantified over:** one family of noiseless problems. The result is an algorithm, so the claim is existential. It exhibits a regime where a polynomial-time method succeeds although low-degree and sum-of-squares lower bounds are both active.
- **Antecedent:** exact noiselessness. The authors state that the method is brittle and that adding inverse-polynomial noise breaks it, which is consistent with the hardness of noisy continuous learning with errors.
- **Algorithm class:** none. This is an upper bound. Its bearing on the rest of this cluster is that it limits what a low-degree or a sum-of-squares lower bound can be read to mean.
- **Does not establish:** that low-degree or sum-of-squares lower bounds are wrong in general, or that any noisy problem becomes easy. It establishes that in the noiseless regime neither lower bound predicts the polynomial-time threshold.
- **Abstract vs theorem:** none found.

## Key Contributions

- LLL-based poly-time algorithm achieving optimal n = d+1 sample complexity for:
  - Planted Hypercube Vector in a Subspace
  - Gaussian Clustering (SNR = ∞)
  - Homogeneous Continuous LWE (hCLWE) with zero noise
- Refutes SoS/LD conjectured hardness (which predicted n = Ω̃(d²) for all three).
- Information-theoretic lower bound of n = d samples (matching up to +1) via separate analysis.
- Conceptual argument: "noiseless" inference problems may systematically escape SoS/LD lower bounds through algebraic lattice structure.

## Key Definitions / Theorems

- **Model (eq 1)**: z_i ~ N(x_i u, I - uu^T), x_i ~ Rademacher, i.i.d.
- **Theorem 1.1**: If n ≥ d+1, an LLL-based poly-time algorithm outputs exactly correct (x_i, u) w.p. 1 - exp(-Ω(d)).
- **Theorem 1.2**: No estimator can recover u from n ≤ d-1 samples (info-theoretic).
- **Theorem 1.3**: n = d+1 is optimal for label recovery up to 1+o(1).
- Brittleness: algorithm fails under inverse-poly noise perturbation (hCLWE hardness kicks in).

## Connections

- [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md) — counterexample
- [Sum-of-Squares Hierarchy](../concepts/sum-of-squares-hierarchy.md) — counterexample
- [LLL Algorithm](../concepts/lll-algorithm.md) — algorithmic tool
- [Continuous LWE](../concepts/continuous-lwe.md) — noisy version is hard
- [Bruna Continuous LWE](bruna-continuous-lwe.md) — hardness of noisy hCLWE
- [Alexander Wein](../entities/alexander-wein.md), [Ilias Zadik](../entities/ilias-zadik.md), [Joan Bruna](../entities/joan-bruna.md)

## Open Questions / Limitations

- LLL approach is brittle to noise: does not "close" statistical-computational gaps in noisy regimes.
- Does LLL break any other conjectured SoS-hard problem in the "noiseless" regime?
- How to formally define "noiseless" problems — the class where LLL might apply.
- Implications for planted clique: PC is not "noiseless" in the relevant sense, so PC hardness likely unaffected.

## Quotes / Notable Passages

> _Opening paraphrased. Checked against `raw/ZSWB22_LatticeSurpassSOS.pdf` on 2026-08-20. From "the success of an LLL-based method" onward the wording is the paper's; the opening clause is not. The paper's own sentence follows._
>
> Our result shows the success of an LLL-based method in a regime where low-degree and SoS lower bounds both suggest computational intractability.

> "Yet, to the best of our knowledge, this work is the first to establish the success of an LLL-based method in a regime where low-degree and SoS lower bounds both suggest computational intractability."

> "All existing algorithms for statistical problems based on LLL suffer from the same lack of robustness. In this sense, there is a strong analogy between LLL and the other known successful polynomial-time method for noiseless inference, namely the Gaussian elimination approach to learning parity."
