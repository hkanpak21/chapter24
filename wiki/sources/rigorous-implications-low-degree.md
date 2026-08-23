---
title: Rigorous Implications of the Low-Degree Heuristic
type: source
date_ingested: 2026-08-21
authors: [Jun-Ting Hsieh, Daniel M. Kane, Pravesh K. Kothari, Jerry Li, Sidhanth Mohanty, Stefan Tiegel]
venue: STOC 2026 (the ingested PDF is arXiv:2601.05850v1, 9 Jan 2026, and does not itself state a venue)
year: 2026
tags: [complexity theory, low-degree-polynomials, statistical-computational-gaps, computational-indistinguishability]
claim_quantifier: conditional
antecedent: "Every result assumes a vanishing degree-D truncated chi-squared divergence between the planted distribution P and the null N at a degree D above a stated threshold, and every result is stated about a NOISY version of P rather than P itself. Two of the three additionally require the planted distribution to be permutation invariant; the third, on symmetric polynomials, does not need that hypothesis because the test class is already symmetric."
adversary_bound: "restricted test classes. Result 1 bounds all distinguishers whatever their running time; result 2 bounds statistics of symmetric polynomials of degree at most O(log n / log log n); result 3 bounds statistics of a single constant-sized signed subgraph count."
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: auditor
cls_unit: algo class
cls_tightness: class
cls_baseline: n/a
cls_second: none
cls_assessed: explicit
cls_evidence: "no statistic based on symmetric polynomials of degree at most O(log n/ log log n) can distinguish between a noisy version of P from N (0, 1)n ."
cls_evidence_src: abstract, Result 2
cls_reason: "Classified on Result 2 (Gaussian vector, degree-restricted symmetric polynomials), the algorithm-class-restricted shape shared with Result 3, over Result 1. Result 1 (Boolean, full statistical indistinguishability against every distinguisher of any running time) is listed first in the abstract and is a strictly stronger, unconditional special case that the paper says is likely false in the matrix/tensor settings; a literal reading of rule 1 ('classify on what the abstract leads with') would instead give frame=none, party=none, unit=none, tightness=unstated for Result 1. Flagged for a second reader: this paper does not present one claim of a single shape."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The low-degree heuristic has been used for a decade to predict algorithmic thresholds, on the
hypothesis that a small low-degree likelihood ratio implies no efficient noise-tolerant algorithm
distinguishes planted from null. What a vanishing likelihood ratio actually implies had not been
established. The known formal consequence, from Kunisky, Wein and Bandeira, is that a vanishing
truncated divergence rules out low-degree polynomials that are concentrated under the null while
having large expectation under the planted distribution. That controls expectations, not
distinguishing, and matching expectations leaves open that some other statistic of a low-degree
polynomial separates the two.

The paper converts likelihood-ratio upper bounds into lower bounds against concrete algorithms, and
proves three such statements. In the Boolean vector setting it obtains the strongest form available,
total variation closeness of the null and the noisy planted distribution itself, which rules out every
distinguisher regardless of running time. In the Gaussian vector setting it rules out any statistic
built from symmetric polynomials of degree at most `O(log n / log log n)`. In the Gaussian matrix
setting it rules out any statistic built from a single signed subgraph count of a constant-sized
subgraph.

The technique is drawn from the bounded-independence-plus-noise line in pseudorandomness. A vanishing
truncated divergence plays the role of almost `D`-wise independence, low-frequency Fourier terms are
controlled by moment matching and high-frequency terms by the noise, and total variation closeness is
obtained through pointwise bounds on densities via characteristic functions. The difference from the
pseudorandomness literature is the target, since fooling a function class equalises expectations while
these results give closeness in total variation.

## Claim Boundary

- **Quantified over:** each theorem quantifies over a **test class**, and the three classes are
  different sizes. Theorem 1.1 quantifies over everything, because it bounds total variation between
  the distributions. Theorem 1.2 quantifies over statistics of the vector of symmetric polynomials of
  degree at most `k`, with `k` capped at `ε log n / (C log log n)`. Theorem 1.3 quantifies over
  statistics of one signed count of one constant-sized connected subgraph.
- **Antecedent:** a vanishing truncated divergence `χ²_D(P ‖ N) ≤ δ` at a stated `D`, and **noise**.
  The noise is not decoration. The paper states that all its total variation results need it, and gives
  the reason, that a discrete `P` can match every low-degree moment of a Gaussian null while any
  function of it stays far in total variation. Permutation invariance is assumed for Theorems 1.1 and
  1.3, and Theorem 1.1 depends on it structurally, since `S_n`-symmetry reduces the question to the
  Hamming weight and makes it one-dimensional. Theorem 1.2 does not need the assumption, and the paper
  says so, because restricting to symmetric polynomials already supplies the symmetry.
- **Adversary class:** as above. None of the three rules out all polynomial-time algorithms.
- **Does not establish:** the low-degree hypothesis. It does not show that vanishing divergence implies
  hardness against efficient algorithms in the Gaussian settings, and the paper marks the gap
  precisely: ruling out spectral methods or a largest-entry test would need the subgraph result at
  `O(log n)`-sized subgraphs rather than constant-sized, and technical barriers remain. The Gaussian
  symmetric-polynomial result faces its own ceiling, since degree `Ω(log n)` symmetric polynomials such
  as a power sum are not expected to satisfy local central limit theorems even under the null.
- **Abstract vs theorem:** the abstract is accurate and unusually careful. It states each result with
  its hypothesis, says "a noisy version of P" in all three, and confines itself to permutation-invariant
  `P`. The overreach risk is in citation rather than in the paper, since "low-degree indistinguishability
  implies hardness" is a fair summary of none of the three statements.

## The three results and their hypotheses

| Result | Setting | Hypothesis | What is ruled out |
|---|---|---|---|
| Theorem 1.1 | `P` over `{±1}^n`, `N = Ber(γ)^n`, `P` is `S_n`-symmetric | `χ²_D(P ‖ N) ≤ δ` for `D ≥ C_γ log(n)/ε` | everything. `d_TV(N, T_ε P) ≤ O_γ(δ/ε² + 1/(sqrt(n) ε²))`, so no algorithm of any running time distinguishes |
| Theorem 1.2 | `P` over `R^n`, `N = N(0, I_n)` | `χ²_D(P ‖ N) = δ` for `D ≥ C k² log(n)/ε²`, with `k ≤ ε log n / (C log log n)` | any statistic of the vector of symmetric polynomials of degree at most `k`. `d_TV(P(N), P(U_ε P)) ≤ δ^{Ω(1)} k^{k/2} + n^{-1/2}` |
| Theorem 1.3 | `P` over symmetric `R^{n×n}`, `N = N(0,1)^{n×n}`, `P` permutation invariant | `χ²_D(P ‖ N) ≤ δ` for `D ≥ log n · log log n` | any statistic of the signed count `χ_ϑ(M)` of one constant-sized connected `ϑ`. `d_TV(ν, π) ≤ O(δ^{αε²} + n^{−αε²})` |

In every row `P` is compared against a noisy planted distribution, `T_ε P` in the Boolean setting and
`U_ε P` in the Gaussian ones, defined by resampling each coordinate with probability `ε` and by
`sqrt(1−ε) x + sqrt(ε) g` respectively.

## Key Contributions

- The first translation of low-degree likelihood ratio upper bounds into lower bounds against concrete
  algorithm classes, answering a question posed as an open direction in the area.
- Full statistical indistinguishability in the Boolean vector case, which is the strongest form the
  heuristic could take, obtained by exploiting `S_n`-symmetry to reduce to a one-dimensional problem.
  The paper states it believes the analogous statement is likely false for matrix and tensor problems.
- A worked consequence for Wigner sparse PCA at `ℓ = n^{0.4}` and `λ = n^{0.3}`, a regime that is
  statistically distinguishable while all known efficient algorithms fail. Since the low-degree ratio
  there is known to be `o(1)` to degree `o(n)`, Theorem 1.3 gives that any test based on one
  constant-sized subgraph statistic has vanishing success probability.
- Two incidental results. In the case `P = N`, Theorem 1.3 gives a local central limit theorem for
  subgraph count polynomials in Gaussian matrices, connecting second-order Poincaré inequalities to
  operator norm bounds for graph matrices from the sum-of-squares literature.

## Key Definitions / Theorems

- **Definition 1.1, low-degree likelihood ratio and advantage.** `L^{≤D}` is the projection of the
  likelihood ratio onto degree at most `D`, and `χ²_D(P ‖ N) = Var_N[L^{≤D}]` is the square of the
  degree-`D` advantage. It is the degree-`D` truncation of the chi-squared divergence.
- **Conjecture 1.1, the low-degree hypothesis.** The statement the paper is measuring, in Hopkins'
  formulation. The paper notes both that permutation symmetry and that noise are necessary, citing the
  code counterexamples of [Holmgren and Wein](holmgren-counterexamples-low-degree.md) for the first and
  brittle algorithms for the second, and records that the quasi-polynomial regime has been disproved by
  [Buhai, Hsieh, Jain and Kothari](quasi-poly-low-degree-conjecture-false.md).
- **Definition 2.1, noise models.** The three operators used, one per setting, as described above.
- **Theorems 1.1, 1.2 and 1.3** as tabulated.

## Connections

- [The Quasi-Polynomial Low-Degree Conjecture is False](quasi-poly-low-degree-conjecture-false.md) is
  the concurrent negative counterpart. Together they resolve the Boolean alphabet case of the
  conjecture, this paper proving it for `k = 1` and that one refuting it for `k ≥ 2`. A security claim
  resting on a low-degree adversary must cite both.
- [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md)
- [Counterexamples to the Low-Degree Conjecture](holmgren-counterexamples-low-degree.md) supplies the
  reason permutation invariance is a hypothesis rather than a convenience.
- [Computational Complexity of Statistics: New Insights from Low-Degree Polynomials](low-degree-polynomials-survey.md)
  contains the Kunisky, Wein and Bandeira expectation bound that this paper strengthens.
- [Statistical Query Algorithms and Low-Degree Tests Are Almost Equivalent](brennan-sq-lowdegree-equivalence.md)
- [Statistical Query Model](../concepts/statistical-query-model.md)
- [Low-Degree Security of the Planted Random Subgraph Problem](bogdanov-low-degree-planted-subgraph.md)
  is a security statement made against a low-degree adversary, and this paper fixes what such a
  statement is worth on its own terms.
- [Cryptography from Planted Graphs: Security with Logarithmic-Size Messages](cryptography-from-planted-graphs.md)
- [Computational-Statistical Gaps in Gaussian Single-Index Models](generative-exponent-single-index.md)
  is the learning-theory use of the same class, where a low-degree lower bound sets an exponent.
- [Pravesh K. Kothari](../entities/pravesh-kothari.md), [Jerry Li](../entities/jerry-li.md)

## Open Questions / Limitations

- Extending Theorem 1.3 from constant-sized to `O(log n)`-sized subgraphs, which is what would be
  needed to preclude spectral methods and largest-entry tests. The paper calls its result a first step
  and states that technical barriers remain.
- Extending Theorem 1.2 past `k = Ω(log n)`, which the paper expects to be blocked, since high-degree
  symmetric polynomials are not expected to obey local central limit theorems even under the null.
- Whether full statistical indistinguishability holds for matrix and tensor valued problems. The paper
  believes it is likely false there, so the Boolean vector result does not generalise.
- The permutation-invariance and noise hypotheses are load-bearing and cannot be removed, which caps
  how far any of these guarantees can travel toward a security definition over deployed objects.

## Quotes / Notable Passages

> it remains unclear whether low-degree indistinguishability actually rules out any interesting class
> of algorithms.

> Both the S_n-symmetry assumption and adding noise to P are necessary.

> To preclude state-of-the-art algorithms such as spectral methods, or distinguishers based on the
> largest entry of a matrix, we would need a version of Theorem 1.3 that holds for O(log n)-sized
> subgraphs.
