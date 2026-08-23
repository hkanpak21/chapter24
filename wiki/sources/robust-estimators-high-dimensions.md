---
title: "Robust Estimators in High Dimensions without the Computational Intractability"
type: source
date_ingested: 2026-04-23
authors: [Ilias Diakonikolas, Gautam Kamath, Daniel M. Kane, Jerry Li, Ankur Moitra, Alistair Stewart]
venue: "FOCS 2016 (venue unconfirmed from PDF: raw/DKKLMS16_RobustEstimators.pdf is arXiv:1604.06443v2 [cs.DS] and names no venue; the attribution is carried over from the earlier ingest)"
year: 2016
tags: [robust-statistics, high-dimensional-statistics, algorithmic-statistics, poisoning-attacks, adversarial-ml]
claim_quantifier: existential
antecedent: "The distribution must lie in one of four named families — a single Gaussian, a product distribution on the hypercube, a mixture of two product distributions under a balancedness condition, or a mixture of spherical Gaussians — and the corrupted fraction ε must be bounded away from 1/2. Outside those families nothing is claimed."
date_verified: 2026-08-20
cls_target: train data
cls_family: poison
cls_phase: train time
cls_access: none
cls_write: corpus
cls_frame: compute
cls_party: learner
cls_unit: time
cls_tightness: poly
cls_baseline: n/a
cls_second: corruption
cls_assessed: explicit
cls_evidence: "In this work, we obtain the first computationally efficient algorithms with dimension-independent error guarantees for agnostically learning several fundamental classes of high-dimensional distributions"
cls_evidence_src: abstract
cls_reason: "Both parties are bounded, in different currencies, per the page's own Claim Boundary: the defender in polynomial time, the adversary only in the ε-fraction of samples it may replace (strong contamination model). By Rule 4 the computational bound decides the row: party=learner, unit=time, tightness=poly, and the corruption fraction goes in second, a clean fit for the corruption unit. access=none: the adversary sees and replaces raw samples directly before any model is queried, so none of the query-access categories describe it. write=corpus: 'an adversary is allowed to arbitrarily corrupt an ε-fraction of the samples' (abstract, verbatim) is a direct write into the training data."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper (DKKLMS16) launched the modern **algorithmic robust statistics** program. Before this work, robust high-dimensional estimation faced a sharp dichotomy: information-theoretic estimators like Tukey depth achieve dimension-independent error under adversarial corruption but require exponential time; computationally efficient estimators like coordinate-wise median or iterative SVD incur dimension-dependent error that grows like √d. The paper resolves this gap — providing the **first computationally efficient algorithms** achieving dimension-independent error for agnostically learning several fundamental high-dimensional distribution classes under arbitrary adversarial corruption of an ε-fraction of samples.

Concretely, the paper handles (1) a single Gaussian (mean + covariance), (2) product distributions on the Boolean hypercube, (3) mixtures of two balanced product distributions, and (4) mixtures of spherical Gaussians. For each, the estimator runs in polynomial time and achieves TV-distance error O(ε) (up to polylogarithmic factors) from the true distribution — independent of dimension d. This matches the information-theoretic optimum up to constants.

Two complementary technical approaches are developed:
- **Convex programming**: The set of possible empirical moments consistent with honest data forms a convex set; a separation oracle finds a point in this set whose distance from the mean reveals corruption. Used for Gaussians and mixtures of spherical Gaussians.
- **Filtering**: An iterative algorithm that detects and removes "outlier" samples whose empirical contribution to high-degree moments is anomalous. Used for Gaussians and product distributions.

Both approaches share a common structure: use *higher-order moments* (fourth-moment tensors, spectral properties) to detect corruption that would evade first-moment or covariance-based tests.

## Claim Boundary

- **Quantified over:** four specific distribution classes. Within each, the guarantee is universal over ε-corruptions and the algorithm is a single explicit procedure. The headline reading — that efficient robust estimation is now available in high dimensions — is an existential claim over distribution families, and the sparse case is a documented counterexample with a genuine statistical-computational gap.
- **Antecedent:** membership in one of the four families, and ε below the breakdown point. Both are stated in the abstract.
- **Which party is constrained:** both, in different currencies. The **adversary** is constrained only in the *fraction* ε of samples it may replace; within that it is computationally unbounded and sees the clean sample before choosing, which is the strong contamination model. The **defender** is constrained to polynomial time, and that constraint is the point of the paper — the contribution is removing an exponential-time requirement, not weakening the attacker. A survey of resource-bounded adversaries should file this as a bounded-defender result with an unbounded adversary on a counting budget.
- **Does not establish:** (i) anything for sparse robust mean estimation, where a k-to-k² gap is known; (ii) anything for heavy-tailed or general distributions; (iii) any hardness — the later evidence that these bounds are near-optimal comes from Hopkins and the small-set expansion hypothesis, not from this paper; (iv) a defence against poisoning of a *classifier*, since the object estimated is a distribution.
- **Abstract vs theorem:** none found. The abstract enumerates the four families explicitly and describes the general method as "a general recipe … that may be applicable to many other problems", which is a suggestion rather than a claim.

## Key Contributions

- **First dimension-independent poly-time robust estimation** for Gaussians, Boolean product distributions, and mixtures thereof.
- **Filtering framework**: iterative outlier removal guided by spectral analysis of higher-order moments; became the dominant paradigm for the field.
- **Convex programming framework**: alternative approach using separation oracles over moment constraints.
- **General recipe**: the "detect-and-correct" structure — use spectral anomalies as corruption signals — generalizes to many subsequent problems (list-decodable learning, sparse mean estimation, etc.).
- **Launched algorithmic robust statistics** as a field; dozens of follow-up papers (Charikar-Steinhardt-Valiant, Lai-Rao-Vempala, Klivans-Kothari-Meka, Bakshi-Prasad, etc.) extend these techniques.

## Key Definitions / Theorems

- **ε-corruption / strong contamination model**: adversary sees the clean sample and may arbitrarily replace an ε-fraction; most powerful model usually considered.
- **Theorem (Gaussian mean/covariance)**: For N(μ, Σ) with ε-corruption, there is a poly(d, 1/ε)-time algorithm outputting (μ̂, Σ̂) with total-variation distance O(ε log(1/ε)) from N(μ, Σ).
- **Theorem (Boolean products)**: For product distributions over {0,1}^d with ε-corruption, there is a poly(d, 1/ε)-time algorithm outputting p̂ with TV distance O(ε √log(1/ε)).
- **Filtering algorithm**: repeatedly (i) compute empirical mean and covariance, (ii) find direction v where projected variance exceeds threshold, (iii) remove samples with outlying projected values.
- **Separation oracle**: convex set of valid moment estimates; ellipsoid method or cutting-plane finds admissible point.

## Connections

- Source: [Curse of Concentration](curse-of-concentration.md) — the MDM19 offline poisoning theorem attacks deterministic learners with Õ(√m) substitutions; DKKLMS16 provides the complementary algorithmic defense achieving dimension-independent error.
- Source: [Robustly-Reliable Learners Under Poisoning](robustly-reliable-learners-poison.md) — Balcan-Blum-Hanneke-Sharma give instance-targeted certificates; DKKLMS16 gives distribution-level estimates.
- Source: [Certified Defenses for Data Poisoning (Steinhardt-Koh-Liang 2017)](certified-defenses-data-poisoning.md) — builds on DKKLMS16 ideas for classification poisoning.
- Source: [Reducibility and Statistical-Computational Gaps](reducibility-statistical-computational-gaps.md) — robust sparse mean estimation (Brennan-Bresler) has a k-to-k² computational gap; DKKLMS16 handles dense (non-sparse) mean.
- Concept: [Poisoning Attacks](../concepts/poisoning-attacks.md) — robust estimation is the algorithmic defense direction.
- Concept: [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md) — DKKLMS16 closes the statistical-computational gap for *dense* robust estimation; sparse versions retain a gap.
- Authors: [Jerry Li](../entities/jerry-li.md), [Ankur Moitra](../entities/ankur-moitra.md).

## Open Questions / Limitations

- **Sparse mean estimation**: the k-to-k² computational gap (Brennan-Bresler) shows that *sparse* robust mean estimation has a genuine statistical-computational gap beyond DKKLMS16's techniques.
- **Beyond Gaussian-like distributions**: robust learning of general distributions (heavy-tailed, non-spherical mixtures) remains partially open.
- **List-decodable regime (ε > 1/2)**: DKKLMS16 requires ε < 1/2; subsequent work (Charikar-Steinhardt-Valiant) handles ε up to 1 via list decoding.
- **Computational lower bounds**: Hopkins (COLT 2019) showed that surpassing DKKLMS16-style bounds refutes the small-set expansion hypothesis, giving worst-case hardness evidence.
- **Practical filtering thresholds**: the algorithm's constants are loose; practical robust estimation often uses heuristic thresholds (e.g., RANSAC).

## Quotes / Notable Passages

> "Is high-dimensional agnostic distribution learning even possible, algorithmically?"

> "We obtain the first computationally efficient algorithms with dimension-independent error guarantees for agnostically learning several fundamental classes of high-dimensional distributions."

> "We develop a general recipe for detecting and correcting corruptions in high-dimensions that may be applicable to many other problems."
