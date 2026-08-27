---
title: "Data Reconstruction: When You See It and When You Don't"
type: source
date_ingested: 2026-07-26
date_verified: 2026-08-22
authors: [Edith Cohen, Haim Kaplan, Yishay Mansour, Shay Moran, Kobbi Nissim, Uri Stemmer, Eliad Tsfadia]
venue: "venue unconfirmed from PDF"
year: 2024
claim_quantifier: conditional
antecedent: "The one-wayness equivalence (Theorem C.5) holds for functions f that are efficiently computable AND well-spread, meaning Pr_{x~U_λ}[f(x) = y] ≤ ν(λ) for negligible ν and every y. Every injective function is well-spread. A function with a heavy output fibre is not, and the theorem says nothing about it."
adversary_bound: "Two, in the same paper. The main-body notion (Definition 1.6, Narcissus resiliency) quantifies over ALL attackers, with no resource bound. The appendix notion (Definition C.1, computational Narcissus resiliency) quantifies over all non-uniform attackers running in poly(λ) time. The one-wayness and encryption results all live under the second."
tags: [cryptography, one-way-functions, computational-indistinguishability, reconstruction, hardness-reductions]
cls_target: train data
cls_family: reconstruct
cls_phase: post hoc
cls_access: none
cls_write: read only
cls_frame: compute
cls_party: attacker
cls_unit: time
cls_tightness: poly
cls_baseline: stated
cls_baseline_checked: yes
cls_second_party: time
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "Algorithm M is (ε, δ, F)-R-computational-Narcissus-resilient if for all D ∈ F and for all (non-uniform) attackers A running in poly(λ) time it holds that"
cls_evidence_src: "Def C.1"
cls_reason: "Judgment call, flagged for a second reader: classified on the computational Narcissus resiliency of Appendix C (Def C.1 / Thm C.5), not the uncomputational main-body Def 1.6 the abstract leads with. Def 1.6 alone quantifies over all attackers with no resource bound and would give party=none, unit=none, tightness=unstated, frame=none for the whole row. Def C.1 is the instance the one-wayness equivalence (Thm C.5) and this programme's own citation of the paper rest on, and it is the only part of the paper that speaks to computational security. second_party=time: Remark C.2 additionally restricts the mechanism M (and relation R) to be efficient and every distribution in F to be poly(λ)-samplable, a second, explicitly-named party bound in the same unit (time). baseline=stated: Narcissus resiliency's defining move is scoring the attacker against its own success on a fresh independent draw T from the same distribution, an explicit self-referential baseline. Per Theorem C.5's antecedent (already in the front matter above), the one-wayness equivalence itself only holds for f efficiently computable and well-spread; that antecedent is not re-encoded in these fields, which describe the adversary's resource bound rather than the antecedent on f."
cls_prov: P
cls_date: 2026-08-22
---

> **Verified against `raw/C+25_DataReconstructionSeeIt.pdf` on 2026-08-22.** The definition numbers,
> the theorem number carrying the one-wayness equivalence, its hypotheses, and every quotation below
> were checked against the extracted text of that file. Still unverified: the venue. The PDF is
> arXiv:2405.15753v2 dated December 10, 2024 and contains no occurrence of "ITCS", so the year above is
> the PDF's and the ITCS 2025 attribution carried elsewhere in this wiki rests on outside authority.
> Also unverified: the appendices other than C, D and E, which were read only in the parts bearing on
> the claims here.

## Summary

The paper's stated aim is definitional. It argues that no single definition of reconstruction is
likely to work, and instead sandwiches the concept between a sufficient condition for safety and a
criterion for when an exhibited attack is convincing. From the abstract, *"our exploration reveals
that a precise definition is much more nuanced than it appears, to the extent that a single
all-encompassing definition may not exist."*

The safety side is **Narcissus resiliency** (Definition 1.6). The attacker is made its own baseline.
`M` is `(ε, δ, F)`-`R`-Narcissus-resilient if for every `D ∈ F` and every attacker `A`, the probability
that `A` reconstructs the real dataset `S` is at most `e^ε` times the probability that the same output
`z` happens to be a valid reconstruction of an independent fresh dataset `T ← D`, plus `δ`. The point
is that the attacker cannot be rewarded for outputting something generic, because a generic output
scores on `T` as well as on `S`, and it cannot tell which experiment it is in.

The attack side is a Kolmogorov-complexity criterion (Definitions 1.12, 1.13 and 3.1). An attack on
`x` counts as extraction when the adversary produces a short program `A` with `R(x, A(y)) = 1` and
`K_L({z : R(x, z) = 1}) ≫ |A|`, so the program is much shorter than the set of valid reconstructions is
complex. Appendix E.4.1 shows that deciding this is itself hard assuming pseudorandom generators
exist.

Appendix C is the part this wiki depends on. It introduces the computational form of the definition
and shows the paradigm subsumes one-wayness and both flavours of ciphertext indistinguishability.

## Claim Boundary

**Quantified over.** Definition 1.6 quantifies over all distributions in the family `F` and all
attackers, unrestricted. Definition C.1 quantifies over all `D ∈ F` and all non-uniform attackers
running in `poly(λ)` time. Theorem C.5 is a biconditional about a single function `f` satisfying its
hypotheses, not a statement about mechanisms in general.

**Antecedent.** Theorem C.5 requires `f` to be efficiently computable and well-spread (Definition
C.4). The authors flag the restriction themselves. *"For technical reasons, we will only show this for
functions f which are well spread, which intuitively means that the outcome distribution of f (x) on a
random x is 'close to uniform'."* Well-spreadness is what makes the right-hand side of the Narcissus
inequality negligible, so it is load-bearing rather than cosmetic. Remark C.2 adds a working
restriction, making the definition of interest only when `M` and `R` are efficient and every distribution
in `F` is samplable in `poly(λ)` time.

**Which party is constrained and in what resource.** The attacker, in running time, and only in
Appendix C. In the main body no party is resource-bounded.

**The success criterion and its tolerance.** A binary relation `R(S, z)`, supplied per setting rather
than fixed. Tolerance is the pair `(ε, δ)`, plus an extra additive `neg(λ)` in Definition C.1. For the
one-wayness instance the parameters are `ε = 0`, `δ = neg(λ)`, `F = {(U_λ, U_λ)}` and
`R(x, x') = 1 iff f(x) = f(x')`.

**The baseline.** The attacker's own success against a fresh independent draw from the same
distribution. This is the paper's central move and the reason the definition avoids a hand-set
threshold.

**Does not establish.** The equivalence is between one-wayness of `f` and Narcissus resiliency of the
mechanism `M_f` that simply outputs `f(x)`. It is not a statement about a training map with the
structure of stochastic gradient descent, and `M_f` has no dataset, no distribution over examples and
no learning objective. The paper also does not claim that Narcissus resiliency composes. Appendix D
gives an explicit counterexample where two individually resilient releases compose into a total break,
and recovers composition only for `ε = 0` under the restricted family of Definition B.2 (Theorem D.2).
The relationship between computational differential privacy and reconstruction is discussed in §1.3
and not developed.

**Abstract versus theorem.** The abstract claims Narcissus resiliency *"captures as special cases
multiple well-studied concepts including differential privacy and other security notions of one-way
functions and encryption schemes."* The body supports this, but the one-wayness case carries the
well-spreadness hypothesis that the abstract does not mention.

## Key Contributions

- **Definition 1.6, Narcissus resiliency.** The self-referential baseline, in the information-theoretic
  form that quantifies over all attackers.
- **Definition C.1, computational Narcissus resiliency.** The same inequality with the attacker
  restricted to non-uniform `poly(λ)` time and an extra `neg(λ)` slack.
- **Theorem C.5.** The one-wayness equivalence, **proved in both directions**, for efficiently
  computable well-spread `f`.
- **Theorems C.8 and C.12.** Private-key EAV-security (Definition C.7) and public-key indistinguishable
  encryptions (Definition C.10) recast as computational Narcissus resiliency, the latter through
  Definition C.11 for protocols.
- **Theorem 2.3 and Definition 2.5.** Resilience to membership inference, and singling out, as
  Narcissus resiliency instances.
- **Definitions 1.12, 1.13 and 3.1 with Lemma 3.2.** The Kolmogorov criterion for a convincing attack,
  and the result that Narcissus resiliency prevents non-trivial extraction.

## Key Definitions / Theorems

- **Theorem C.5 (verbatim):** *"Let f : {0, 1}\* → {0, 1}\* be an efficiently computable well-spread
  function. Let M_f be the algorithm that takes an input x and returns f(x). Let R : {0, 1}\* × {0, 1}\*
  → {0, 1} be s.t. R(x, x′) = 1 iff f(x) = f(x′). Let λ ∈ N be a parameter and let U_λ be the uniform
  distribution over {0, 1}^λ. Then, f is a one-way function if and only if M_f is (0, neg(λ), {(U_λ,
  U_λ)})-R-computationally-Narcissus-resilient."*
- **Definition C.1, the adversary clause (verbatim):** *"Algorithm M is (ε, δ, F)-R-computational-
  Narcissus-resilient if for all D ∈ F and for all (non-uniform) attackers A running in poly(λ) time
  it holds that"* the Narcissus inequality with an additional `+ neg(λ)`.
- **On computational DP (verbatim):** *"We note that an efficient privacy attack (e.g., membership
  inference or reconstruction) implies that the algorithm is not computationally differentially
  private. But in the opposite direction, if an algorithm is not computationally differentially
  private, the privacy attack, while being efficient, could be very negligible (e.g., the attack might
  reveal only a single, insignificant, bit of information about a training example, and still violating
  computational differential privacy)."*
- **On size versus extractability (verbatim, with the exception clause restored):** *"While large
  memorization (i.e., mutual information) implies that the algorithm is not differentially private, it
  does not imply the existence of an efficient attack. Indeed, except for [BZ16; ADH+24], these works
  are typically not constructive (i.e., they do not provide an efficient way to translate the
  memorization into an efficient privacy attack)."* The earlier wiki rendering elided
  "except for [BZ16; ADH+24]", which is the clause naming the two constructive exceptions.

## Connections

- **Occupies "is the training map a one-way function", for the mechanism `M_f`.** Any programme
  statement of that form must position against Definition C.1 and Theorem C.5, and must say whether its
  map is well-spread.
- Successor to [Dinur–Nissim](dinur-nissim-revealing-information.md), which this paper cites as the
  origin of reconstruction attacks.
- Companion to [Kaplan–Mansour–Nissim–Stemmer](kaplan-bayesian-memorization-reconstruction.md), which
  builds its Bayesian extraction-safety definition directly on Definition 1.6.
- **The ML side of the same question, in incompatible units.**
  [Wen–Liu–Backes–Zhang, SoK: Data Reconstruction Attacks](sok-data-reconstruction-attacks.md)
  declares that reconstruction has no consensus formal definition and supplies `(ε, µ)`-approximate
  reconstruction, in which `ε` is a quality tolerance and the adversary is characterised only by its
  knowledge, never by its resources. It does not cite this paper.
- Definitions 1.4 and 1.5 are the reconstruction-robustness notions of Balle–Cherubin–Hayes and
  Cummings et al., which this paper reproduces in order to argue that a fixed baseline fails.
- Concepts: [one-way-functions](../concepts/one-way-functions.md),
  [fiber-of-the-training-map](../concepts/fiber-of-the-training-map.md),
  [computational-vs-statistical-memorization](../concepts/computational-vs-statistical-memorization.md),
  [data-reconstruction-attack](../concepts/data-reconstruction-attack.md),
  [computational-differential-privacy](../concepts/computational-differential-privacy.md).

## Open Questions / Limitations

- Question 1.1, "What is reconstruction?", is left open by the authors on purpose.
- `M_f` is a general mechanism, not a training map on a data distribution. Whether the equivalence is
  informative for the training map, or merely applicable to it, is the gap worth measuring.
- Narcissus resiliency does not compose in general. A programme that wants to release several statistics
  cannot inherit composition from this definition.
- The relationship between computational differential privacy and reconstruction is raised in §1.3 and
  not built out. That branch was verified open across the computational-DP line.
- The well-spreadness hypothesis in Theorem C.5 has no counterpart on the mechanism side of the
  reconstruction setting, so it is not obvious what it corresponds to for a learning algorithm.

## Quotes / Notable Passages

See Key Definitions. The four verbatim passages there are the load-bearing ones. One more, on the
definitional stance of the whole paper:

> "our exploration reveals that a precise definition is much more nuanced than it appears, to the
> extent that a single all-encompassing definition may not exist"
