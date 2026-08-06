# Case study: feature inference against a sparse regression model

*End-to-end exposition. Companion to [[2026-08-05-unfiled-natural-source-r-selects-the-problem]].
Written 2026-08-05.*

> **Provenance.** The construction and the argument are this programme's. The cited results are drawn
> from a literature sweep and from standard references; **they have not all been read in full here**, and
> every numbered threshold below should be checked against its source before it is presented as exact.
> Statements marked **[verify]** are the ones where a wrong constant would change the story.

---

## 0. What this case study is for

It demonstrates one claim and nothing else:

> **Over a single fixed, entirely natural learning setting, the choice of success criterion `R` decides
> which computational problem the adversary faces, and therefore which threshold governs security. `R`
> is the instrument. It is not a reader of hardness placed somewhere else.**

An earlier attempt used a cryptographically planted source (Gaussian pancakes). That attempt failed for
a specific reason worth stating: the hardness was present in the data distribution before `R` was
introduced, so `R` performed no work and the reduction said nothing about learning. This case study
holds the source ordinary throughout.

---

## Part I — The setting

### 1. The source

Fix a dimension `d`, a sparsity level `k` with `k ≪ d`, and a sample size `n`.

**Design.** Draw `n` covariate vectors independently,

```
x_1, …, x_n  ~  N(0, I_d)   i.i.d.
```

and stack them as the rows of `X ∈ ℝ^{n×d}`. This is the *isotropic Gaussian design*. It is the
standard assumption in high-dimensional statistics, and it contains no hidden structure of any kind.

**Signal.** Fix `β* ∈ ℝ^d` with exactly `k` non-zero entries. Write

```
S* = supp(β*) = { j : β*_j ≠ 0 },   |S*| = k
```

for its **support** — the set of features the signal actually uses.

**Responses.** With noise level `σ > 0`,

```
y = X β* + w,    w ~ N(0, σ² I_n)
```

**Two quantities that govern everything below.**

- `β_min := min_{j ∈ S*} |β*_j|`, the smallest non-zero coefficient. Support recovery is impossible if
  the smallest coefficient is buried in the noise, so `β_min` appears in every recovery threshold.
- The signal-to-noise ratio, conventionally `‖β*‖²_2 / σ²` or `k β_min² / σ²` depending on the source.

**Nothing here is planted.** The support `S*` is a secret only in the sense that the adversary does not
know it. It is not a cryptographic key, it carries no trapdoor, and the distribution of `x` is exactly
what a textbook would write down.

### 2. The defender and the learning algorithm

The defender's job is **prediction**: given a fresh `x`, output an estimate of `y`. This is an ordinary,
useful task, and the defender genuinely succeeds at it.

**The algorithm.** The canonical estimator is the LASSO (Tibshirani 1996):

```
β̂ = argmin_β   (1/2n)·‖y − Xβ‖²_2  +  λ·‖β‖_1
```

The `ℓ1` penalty is a convex surrogate for the `ℓ0` sparsity constraint; the problem is convex and
solvable in polynomial time by coordinate descent or proximal gradient methods.

**What the defender obtains.** With `λ ≍ σ·√(log d / n)`:

| Guarantee | Statement | Regime | Source |
| --- | --- | --- | --- |
| Prediction error | `(1/n)‖X(β̂ − β*)‖²_2 ≲ σ²·k·log d / n` | `n ≳ k log d` | Bickel–Ritov–Tsybakov 2009 **[verify]** |
| Estimation error | `‖β̂ − β*‖_2 ≲ σ·√(k log d / n)` | same, under a restricted eigenvalue condition | Bickel–Ritov–Tsybakov 2009 **[verify]** |
| Support recovery | `supp(β̂) = S*` with high probability | `n ≳ 2k·log(d−k)` **and** `β_min` above a noise-dependent floor | Wainwright 2009 **[verify]** |

The regularity conditions (restricted eigenvalue, irrepresentability) hold with high probability for
the isotropic Gaussian design, so they are not obstacles here. They matter for correlated designs and
should be stated when the setting is generalized.

**The operating point that makes this a security question.** Take `n` large enough for good prediction
and *not* large enough for reliable support recovery, or take `β_min` below the recovery floor. The
defender then has a genuinely useful model and the support is not simply readable from it. That regime
is where the whole case study lives.

### 3. What is released

This is the decision that creates or destroys the security question, and it must be stated explicitly.

| Release | Can the support be recovered | Adversary's problem |
| --- | --- | --- |
| the fitted vector `β̂` | by inspection: read off `supp(β̂)` | none — the question is void |
| query access, `d` or more queries permitted | probe the basis vectors `e_1 … e_d` and read each coefficient | trivial, `d` queries |
| query access, `q < d` queries | `q` linear measurements of a `k`-sparse vector | compressed sensing; recoverable at `q ≍ k·log(d/k)`, polynomial time |
| **a trained network computing the same function** | **unknown** | **the open case, and the one that occurs in deployment** |

**The release assumed throughout the rest of this document is the last row**: a model that predicts well
and whose parameterization does not expose the support. A network trained on the same data is the
concrete instance. The adversary must infer the support from behaviour.

This is also where the phrase "leaving space for the adversary" becomes precise. The adversary is not
blocked; it can obtain *partial* support information, and the criterion below measures how much.

---

## Part II — The security question

### 4. The harm, stated before any difficulty is examined

The programme's standing guardrail is that `R` must be pinned to a harm *before* anyone looks at whether
achieving it is hard. Otherwise one proves a fact about `R` and not about the system.

The harm here is **feature inference**, also called attribute or property inference: an adversary
learns *which features the model uses*. Real instances:

- **Genomics.** A polygenic risk score uses a panel of variants. The panel is commercially valuable, and
  its membership discloses which variants a cohort was screened on.
- **Credit and insurance.** Whether a scoring model uses a particular attribute, or a proxy for a
  protected one, is a regulatory question with legal consequences.
- **Clinical models.** Which biomarkers enter a diagnostic model reveals both proprietary methodology
  and, in aggregate, something about the study population.

None of these requires reconstructing a training record. The support alone is the asset.

### 5. The adversary

| Component | Value |
| --- | --- |
| Knows | the setting: `d`, `k`, `σ`, the fact that the source is a sparse Gaussian linear model |
| Does not know | `S*`, `β*`, the training sample |
| Access | the released model, white-box or by query, at a stated budget |
| Budget | `q` queries and time `T`; alternatively `m` auxiliary samples from the same source |
| Output | a candidate set `Ŝ ⊆ [d]`, with `|Ŝ| = k` |

The adversary is *not* assumed computationally unbounded, and the budget is part of the specification
rather than an afterthought. This is the point at which the programme departs from the differential
privacy tradition, in which the adversary has unlimited time.

---

## Part III — The criterion `R`

### 6. What `R` is

`R` is the **quantizer between two layers that speak different languages.**

- The learning layer is approximate everywhere. Risks, tolerances, convergence, regularity conditions,
  and outcomes that differ between random seeds.
- The cryptographic layer is exact. An adversary either produced a valid object or it did not; a
  reduction consumes a bit.
- A reduction cannot consume an approximate outcome.

`R` is the map between them. Its type is

```
R : (world) × (adversary output) → {0, 1}
```

so it is exact by construction, and **its parameters are placed exactly where the approximation gets
quantized**. This is why the empirical variance that makes security results disagree between papers,
settings and seeds does not enter a reduction built on `R`: the reduction consumes the bit and nothing
upstream of it.

`R` does four things.

| Function | Statement |
| --- | --- |
| Quantizes | converts an approximate learning outcome into the single bit a reduction can consume |
| Carries the parameters | `R`'s tolerance *is* the reference problem's precision, as one symbol used once and never as a correspondence |
| Fixes the baseline | names what public knowledge alone achieves, which is what makes "advantage" defined at all |
| **Selects the problem** | fixing `R` fixes the search or decision problem the adversary solves; the problem is read off, not constructed |

The fourth is the one this case study demonstrates.

### 7. The criterion for this case study

```
R_η(S*, Ŝ) = 1   exactly when   |Ŝ ∩ S*| ≥ (1 − η)·k
```

with `|Ŝ| = k`. At `η = 0` this is exact support recovery. At `η > 0` the adversary is credited for
recovering a `(1−η)` fraction of the support.

**Free parameters.**

| Parameter | Meaning in `R` | Meaning in the reference problem |
| --- | --- | --- |
| `η` | recovery tolerance | the partial-recovery precision |
| `k` | support size | the sparsity level |
| `d` | ambient dimension | the ambient dimension |
| `q`, `T`, or `m` | the adversary's budget | the algorithm's budget |

**No symbol is translated.** One writes `η` once and it appears in both layers. This is the whole
content of the phrase "no translation occurs": there is nothing to say "corresponds to," because the
tolerance and the precision are the same number in the same inequality.

### 8. The baseline, and why it is not degenerate

A party with only public knowledge — it knows `d` and `k` but nothing about `S*` — guesses a uniformly
random `k`-subset. Its success probability on `R_η` is

```
Pr[ |Ŝ ∩ S*| ≥ (1−η)k ]  =  Σ_{i ≥ (1−η)k}  C(k,i)·C(d−k, k−i) / C(d,k)
```

For `η` bounded away from `1` and `k ≪ d` this is exponentially small in `k`. So:

- the baseline is **non-degenerate**, unlike the membership-inference baseline which sits at one half by
  construction;
- baseline-subtracted advantage is therefore meaningful here, and the failure mode recorded against
  `COMP-MEM` does not arise.

At `η → 1` the criterion degenerates (any `k`-set wins) and at `η = 0` the baseline is
`1 / C(d,k)`. The usable range is between.

### 9. Where the `R` idea comes from

The criterion-as-free-parameter is not this programme's invention. The lineage, in order:

| Work | Contribution | Form of the criterion |
| --- | --- | --- |
| Bhowmick, Duchi, Freudiger, Kapoor, Rogers, arXiv:1812.00984 (2018), Def. 2.3 | earliest fully parameterized reconstruction definition found | free loss `L_rec` **and** free target function `f`; `sup` over observations |
| Balle, Cherubin, Hayes, IEEE S&P 2022, arXiv:2201.04845, Def. 2 | reconstruction robustness (ReRo); the **informed adversary** | free `(ℓ, η)` — distance and tolerance |
| Hayes, Mahloujifar, Balle, NeurIPS 2023, arXiv:2302.07225, Def. 1 | ReRo bounds for DP-SGD | free `(ρ, η)` |
| Xiao, Devadas, CRYPTO 2023, arXiv:2210.03458, Def. 1 | PAC Privacy | free predicate `ρ` for "an arbitrary inference task of interest" |
| Cummings, Hod, Sarathy, Swanberg, arXiv:2405.01716, Defs 4.4 / 4.8 | Attaxonomy; distributionally informed adversary | free `(ℓ, η)`, three aggregation shapes |
| **Cohen, Kaplan, Mansour, Moran, Nissim, Stemmer, Tsfadia, ITCS 2025, arXiv:2405.15753** | **`R : X* × {0,1}* → {0,1}` as the explicit object; Defs 1.4, 1.5, 1.6 (Narcissus), C.1 (computational)** | **free relation `R`** |
| Kaplan, Mansour, Nissim, Stemmer, arXiv:2505.23658 (ITCS 2026), Defs 3.6, 4.4 | two relations `(R, R̂)`; a surprisal-conditioned variant | free relation, twice |
| Swanberg, Annamalai, Balle, Hayes, Smith, arXiv:2507.08158 (2026) | unifies MI, attribute inference and reconstruction | free decomposable metric `L = Σ ℓ_i` |
| Salem, Cherubin, Evans, Köpf, Paverd, Suri, Tople, Zanella-Béguelin, IEEE S&P 2023, arXiv:2212.10986 | the privacy-games SoK; 17 games over 5 adversary goals | criterion free for reconstruction, hard-coded elsewhere |

**The specific debt.** The notation `R`, its type as a relation into `{0,1}`, and the treatment of the
criterion as the object of study rather than as a modelling detail are Cohen et al.'s. Their Definition
1.4 is attributed by them to Balle–Cherubin–Hayes and to Attaxonomy.

**What is not borrowed.** Every definition in the table above quantifies over a **computationally
unbounded** adversary, with one exception: Cohen et al.'s Definition C.1, which is polynomial-time
bounded and is proved equivalent to one-wayness. No definition in the lineage bounds the adversary by an
*amount* of computation, and none uses `R` to *select* a reference problem. Salem et al. §II-C names the
compute-parameterization move explicitly and then declines it, which makes it the clean citation for the
move being recognized and unbuilt.

**Adjacent, for property inference specifically.** Ateniese, Mancini, Spognardi, Villani, Vitali,
Felici, IJSN 2015 (origin); Yeom, Giacomelli, Fredrikson, Jha, CSF 2018 (attribute advantage
parameterized by an attribute function `φ`); Suri, Evans, PoPETs 2022(4), arXiv:2109.06024
(distribution inference as a cryptographic game, parameterized by two distribution transformers).

---

## Part IV — The demonstration

### 10. `R` selects the problem

Source fixed. Defender fixed. Release fixed. **Only `R` changes.**

| `R` | The adversary's problem | Governing threshold | Regime |
| --- | --- | --- | --- |
| predict `y` to squared error `ε` | the defender's own task | `n ≳ k log d` | polynomial (LASSO) |
| recover `β*` to `‖·‖_2` tolerance `η` | sparse estimation | `n ≳ k log d` | polynomial |
| `R_0`: recover `S*` exactly | exact support recovery | `n ≳ 2k log(d−k)` **and** `β_min` above the noise floor | polynomial when both hold |
| `R_0` with `β_min` **below** that floor | support recovery in the hard regime | information-theoretically possible above `n_IT`; no polynomial algorithm known | **the gap** |
| `R_η` for `η` close to 1 | naming one support member | far weaker than recovery | easy |

Five problems. Five thresholds. One unchanged natural source, one unchanged learning algorithm, one
unchanged release. The only thing that moved was the criterion.

That is the demonstration, and it is what the pancake construction could not show, because there the
hardness was already in the source before any criterion was chosen.

---

## Part V — The hard problem

### 11. Sparse regression in the hard regime

The fourth row above is the one that reaches a computational problem.

**The information-theoretic threshold.** Exact support recovery is possible for an unbounded algorithm —
exhaustive search over all `C(d,k)` supports, selecting the one minimizing residual error — once

```
n  ≳  n_IT  ≈  2k·log d / log(1 + 2k/σ²)          [verify]
```

Gamarnik and Zadik establish this threshold and the sharp phase transition around it (*Sparse
High-Dimensional Linear Regression: Estimating Squared Error and a Phase Transition*, Annals of
Statistics 2022; earlier as arXiv:1701.04455). The "all-or-nothing" character — the estimation error
drops discontinuously at the threshold — is theirs. **[verify]**

**The polynomial-time threshold.** Every known polynomial algorithm — LASSO, orthogonal matching
pursuit, the Dantzig selector — requires substantially more samples than `n_IT`, and additionally a
`β_min` condition that exhaustive search does not need.

**The gap.** Between `n_IT` and the sample size at which polynomial methods succeed lies a regime where
recovery is information-theoretically possible and computationally out of reach. That regime is the
reference problem.

### 12. The evidence for hardness in the gap

No unconditional lower bound against all polynomial algorithms exists, and none can be expected, since
that would separate complexity classes. What exists is three independent bodies of evidence.

| Evidence | Statement | Source |
| --- | --- | --- |
| **Overlap gap property** | The solution space in the hard regime is shattered: near-optimal supports come in clusters that are either very close or very far, with nothing between. This provably blocks *stable* algorithms — low-degree polynomials, bounded-time Langevin dynamics, and polynomial-size circuits below depth `log n / (2 log log n)` | Gamarnik–Zadik; Gamarnik–Jagannath–Wein **[verify]** |
| **Low-degree lower bounds** | No low-degree polynomial distinguishes the planted from the null model in the gap regime | Bandeira, El Alaoui, Hopkins, Schramm, Wein, Zadik, *The Franz-Parisi Criterion and Computational Trade-offs in High Dimensional Statistics*, NeurIPS 2022 **[verify]** |
| **Average-case reductions** | Sparse regression variants sit in the reduction web rooted at planted clique, so hardness transfers from a thirty-year-old conjecture | Brennan–Bresler, *Reducibility and Statistical-Computational Gaps from Secret Leakage*, 2020; see [[reducibility-statistical-computational-gaps]] |

The three agree in this regime, which is the situation in which confidence is highest. Where physics
criteria and TCS criteria diverge, neither is authoritative — a caution recorded in [[related-work]] §7.

**Why this reference problem and not a lattice problem.** The programme's method is to reduce one
learning problem to another, because attacks in this field are themselves learning algorithms. Sparse
regression is a learning problem with calibrated thresholds on both sides of the gap. A lattice problem
would give stronger hardness and a worse fit, and it would reintroduce exactly the objection that killed
the pancake construction.

### 13. The mapping, step by step

| Step | Statement |
| --- | --- |
| 1 | The defender releases a model `M` that predicts `y` well and does not expose `supp(β*)` |
| 2 | The adversary, at budget `b`, outputs `Ŝ` and achieves `R_η(S*, Ŝ) = 1` with probability `p(b)` |
| 3 | The baseline `p_0` is the random-subset probability from §8, exponentially small |
| 4 | An adversary with `p(b) ≫ p_0` has extracted support information from `M` |
| 5 | **[open]** Such an adversary yields an algorithm for `(1−η)`-partial support recovery on the sparse regression instance, at budget `b` plus the cost of simulating `M` |
| 6 | In the gap regime, that contradicts the low-degree and overlap-gap evidence of §12 |

**Step 5 is the unproved step, and it is the whole technical content.** It requires showing that the
adversary's access to a *trained network* can be converted into access to the *samples*, or that the
network's behaviour is itself a low-degree function of the samples so that the low-degree bound applies
directly. Neither is established here.

### 14. The alignment check

The programme's test for whether a mapping is a measurement rather than an analogy: three quantities
must be the same symbols, not correspondences.

| | In `R` | In the reference problem | Aligned |
| --- | --- | --- | --- |
| tolerance | `η`, the partial-recovery fraction | the partial-recovery precision | yes |
| structure parameter | `k`, the support size | the sparsity level | yes |
| budget unit | samples `m`, or queries `q` | samples in the threshold `n_IT` | **only if the adversary's budget is stated in samples** |

The third row passes when the adversary is given auxiliary samples from the same source and fails when
it is given only query access to `M`, because query count and sample count are not the same resource.
**This is a modelling decision that must be made explicitly**, and stating the adversary's budget in
samples is what makes the mapping a measurement.

---

## Part VI — Status

### 15. What is established, assumed and open

| Claim | Status |
| --- | --- |
| The setting is natural and the defender's task succeeds | **established**, standard statistics |
| Changing `R` alone reaches five distinct problems with distinct thresholds | **established** by §10 |
| The baseline is non-degenerate, so advantage is well defined | **established** by §8 |
| A stat-comp gap exists for sparse regression support recovery | **assumed**, on three independent bodies of evidence, none unconditional |
| The adversary's budget is stated in samples so the alignment test passes | **a modelling decision**, made explicitly in §14 |
| Support recovery from a trained network reduces to support recovery from samples | **open — step 5, the technical content** |
| The construction is novel | **unchecked.** Four novelty claims failed in the session that produced this document. Do not assert it |

### 16. The first thing to do next

Settle step 5 on the easiest instance. Take the release to be a *linear* model that is not the LASSO
solution — a ridge-regularized fit, which predicts well and is dense, so the support is not readable —
and ask whether an adversary with `m` auxiliary samples and query access recovers `S*` at a rate
governed by `n_IT`. If it does, the mapping is real on a case where everything is computable in closed
form. If it does not, the obstruction will be visible, and it will be visible in weeks.

---

## References

**The criterion `R`.** Cohen, Kaplan, Mansour, Moran, Nissim, Stemmer, Tsfadia, *Data Reconstruction:
When You See It and When You Don't*, ITCS 2025, arXiv:2405.15753 · Balle, Cherubin, Hayes, *Reconstructing
Training Data with Informed Adversaries*, IEEE S&P 2022, arXiv:2201.04845 · Hayes, Mahloujifar, Balle,
NeurIPS 2023, arXiv:2302.07225 · Bhowmick, Duchi, Freudiger, Kapoor, Rogers, arXiv:1812.00984 · Xiao,
Devadas, *PAC Privacy*, CRYPTO 2023, arXiv:2210.03458 · Cummings, Hod, Sarathy, Swanberg, *Attaxonomy*,
arXiv:2405.01716 · Kaplan, Mansour, Nissim, Stemmer, arXiv:2505.23658 · Swanberg, Annamalai, Balle,
Hayes, Smith, arXiv:2507.08158 · Salem et al., *SoK: Let the Privacy Games Begin!*, IEEE S&P 2023,
arXiv:2212.10986.

**Sparse regression.** Tibshirani, *Regression shrinkage and selection via the lasso*, JRSS-B 1996 ·
Wainwright, *Sharp thresholds for high-dimensional and noisy sparsity recovery using ℓ1-constrained
quadratic programming (Lasso)*, IEEE Trans. Inf. Theory 55(5), 2009 · Bickel, Ritov, Tsybakov,
*Simultaneous analysis of Lasso and Dantzig selector*, Annals of Statistics 37(4), 2009 · Zhao, Yu, *On
model selection consistency of Lasso*, JMLR 7, 2006 · Candès, Tao, *The Dantzig selector*, Annals of
Statistics 35(6), 2007.

**The gap and its evidence.** Gamarnik, Zadik, *Sparse High-Dimensional Linear Regression: Estimating
Squared Error and a Phase Transition*, Annals of Statistics 2022, arXiv:1701.04455 · Bandeira, El Alaoui,
Hopkins, Schramm, Wein, Zadik, *The Franz-Parisi Criterion and Computational Trade-offs in High
Dimensional Statistics*, NeurIPS 2022 · Brennan, Bresler, *Reducibility and Statistical-Computational Gaps
from Secret Leakage*, 2020 · Zhang, Wainwright, Jordan, *Lower bounds on the performance of
polynomial-time algorithms for sparse linear regression*, COLT 2014.

**Property and attribute inference.** Ateniese, Mancini, Spognardi, Villani, Vitali, Felici, IJSN 10(3),
2015 · Yeom, Giacomelli, Fredrikson, Jha, CSF 2018 · Suri, Evans, *Formalizing and Estimating Distribution
Inference Risks*, PoPETs 2022(4), arXiv:2109.06024.

**Programme documents.** [[CONTEXT]] · [[2026-08-05-unfiled-natural-source-r-selects-the-problem]] ·
[[2026-08-05-unfiled-r-as-quantizer-and-one-reduction]] · [[2026-08-05-unfiled-concrete-r-criteria]] ·
[[related-work]] · [[cohen-data-reconstruction]] · [[reducibility-statistical-computational-gaps]].
