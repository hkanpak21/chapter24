---
title: Revealing Information while Preserving Privacy
type: source
date_ingested: 2026-07-26
date_verified: 2026-08-22
authors: [Irit Dinur, Kobbi Nissim]
venue: "venue unconfirmed from PDF"
year: 2003
claim_quantifier: universal
antecedent: "For the two impossibility theorems, none beyond the model: a binary database of n entries answering subset-sum queries within a stated perturbation magnitude. For the feasibility theorem, the database is drawn from the uniform distribution over {0,1}^n, which the authors state is the way they model an adversary with no prior knowledge."
adversary_bound: "Three separate bounds, one per theorem. Theorem 2 gives the adversary exponential time and all 2^n queries. Theorem 3 gives it polynomial time and n(log n)^2 uniformly random queries. Definition 4 and Theorem 5 give it a pair of Turing machines of time complexity T(n), which also caps the number of queries at T(n)."
tags: [cryptography, complexity theory, hardness-reductions, sample-complexity, reconstruction]
---

> **Verified against `raw/DN03_RevealingInformation.pdf` on 2026-08-22.** Section numbers, theorem
> statements, perturbation bounds and every quotation below were checked against the extracted text of
> that file. Still unverified: the venue. The PDF is a manuscript dated December 30, 2002 that names no
> conference, and PODS appears in it only inside a reference to Kleinberg, Papadimitriou and Raghavan.
> Other pages in this wiki cite the work as PODS 2003 on outside authority.

## Summary

The founding result of the data-reconstruction literature. A curator holds a database
`d = (d_1, ..., d_n) ∈ {0,1}^n`. A query is a subset `q ⊆ [n]`, whose exact answer is `a_q = Σ_{i∈q} d_i`,
and the curator answers within perturbation `E`, meaning `|a_q − A(q)| ≤ E` (Definitions 1 and 2). The
question is how large `E` must be to prevent an adversary from reconstructing almost all of `d`. The
answer depends on how much computation the adversary has, and the paper prices that dependence in
three places.

The authors state their own headline as the attack, not as the separation. The abstract reads
*"Our main result is a polynomial reconstruction algorithm of data from noisy (perturbed) subset
sums."* That algorithm is Theorem 3: it issues `t = n(log n)^2` uniformly random queries, solves a
linear program in the unknowns `c_1, ..., c_n` subject to `ã_{q_j} − E ≤ Σ_{i∈q_j} c_i ≤ ã_{q_j} + E` and
`0 ≤ c_i ≤ 1`, then rounds each coordinate at `1/2`. The proof is a union bound over a discretised
grid of candidate databases, using a lower-tail deviation argument (Lemma 4) rather than the usual
upper tail.

What makes the paper the reference point for pricing a privacy adversary in compute is that it names
the motivation explicitly. Rejecting variance-based privacy measures, the authors write that
*"this kind of definition does not allow us to capitalize on the limits of an adversary."* Section 4
then asks *"whether further restricting the adversary complexity enables achieving privacy using a
smaller perturbation"* and answers positively.

## Claim Boundary

**Quantified over.** Theorems 2 and 3 are universal over database algorithms `A`. Any `A` within the
stated perturbation is non-private, whatever its internal state or perturbation method, and the
adversary of Theorem 3 is *"oblivious both of the database distribution and the perturbation method"*
(footnote 4). Theorem 5 is existential over algorithms. It exhibits one perturbation algorithm and
shows it private.

**Antecedent.** Theorems 2 and 3 carry none beyond the model. Theorem 5 assumes `DB` is uniform over
`{0,1}^n` and `T(n) > polylog(n)`. The authors say the assumption is unavoidable, since for a database
known to be `1^n` or `0^n` a single query settles it unless `E ≥ n/2`.

**Which party is constrained and in what resource.** The adversary, in time and therefore in query
count. Theorem 2 allows exponential time and all `2^n` queries. Theorem 3 allows polynomial time and
`n(log n)^2` random queries. Theorem 5 allows time `T(n)`, with Definition 3 noting that a time bound
"implicitely bounds the number of queries the adversary issues". The curator is constrained only in
perturbation magnitude.

**The success criterion and its tolerance.** Non-privacy (Definition 3) is Hamming reconstruction.
For every constant `ε > 0` there is a machine outputting `c` with `dist(c, d) < εn` with probability at
least `2/3`. Privacy (Definition 4) is the complementary guessing game. Two machines `M_1^A, M_2` of
time `T(n)`, where `M_1` queries and commits to an index `i` and `M_2` receives the transcript **plus
every entry other than the i-th**, must fail to output `d_i` with probability `1/2 + δ`.

**The baseline.** For Definition 4 it is stated, and it is `1/2`, the coin flip on a uniform bit. For
Definition 3 there is no baseline term. The criterion is absolute Hamming distance.

**The bounds themselves.** Against an exponential adversary, `E = o(n)` is already fatal (Theorem 2),
so linear perturbation is needed. Against a polynomial adversary, `E = o(√n)` is fatal (Theorem 3), so
`Ω(√n)` is needed. Against a time-`T(n)` adversary, `Õ(√T(n))` perturbation suffices (Theorem 5).

**Does not establish.** It says nothing about a training map `D ↦ w`. The mechanism is a query-release
interface over a bit vector, and the attack is linear-algebraic, so it carries no information about
mechanisms whose consistency conditions are higher degree. The tightness construction of §3.3 is
private and useless at once, the authors noting that *"the above algorithm renders the database
effectively useless."* Appendix B recovers a little usability by releasing a randomised copy `d'` of
the database, which is a different mechanism from the one Theorem 3 attacks.

**Abstract versus theorem.** The abstract is accurate and, if anything, understates the §3.1 result.
It advertises the `Ω(√n)` bound and the `≈ √T` feasibility algorithm and does not advertise a
statistical-versus-computational separation as the contribution, which matches how §3.1 is presented
in the body as a warm-up on *"very small databases"*.

## Key Contributions

- A polynomial-time reconstruction algorithm from noisy subset sums, and with it the `Ω(√n)`
  perturbation threshold for polynomially bounded adversaries.
- The `Ω(n)` threshold against an adversary permitted all `2^n` queries, by exhaustive weeding.
- A feasibility result for time-`T(n)` bounded adversaries at perturbation `Õ(√T(n))`, proved by
  analysing the adversary's log-odds confidence as a random walk and applying Azuma's inequality.
- Framing reconstruction as finding one consistent database rather than characterising all of them.

## Key Definitions / Theorems

The section structure is the part the wiki has most often reported wrongly, so it is set down exactly.
Section 3 is titled **Impossibility results** and contains three subsections. Section 4 is titled
**Preserving Privacy in a Bounded Model - Feasibility Results**.

- **§3.1 Exponential Adversary.** Theorem 2. If `A` is within `o(n)` perturbation then `D` is
  `exp(n)`-non-private. The attack queries every `q ⊆ [n]` and outputs the first `c ∈ {0,1}^n`
  consistent with all answers, achieving `dist(d, c) ≤ 4E`.
- **§3.2 Polynomially Bounded Adversary – Ω(√n) Perturbation Needed for Privacy.** Theorem 3. If `A`
  is within `o(√n)` perturbation then `D` is `poly(n)`-non-private. This is the linear-programming
  attack.
- **§3.3 Tightness of the Impossibility Results.** A database algorithm within `Õ(√n)` perturbation
  that is private against polynomial adversaries, obtained by answering `|q|/2` unless the true count
  deviates by more than `E = √n·(log n)^{1+ε}`.
- **§4, Definition 4 (Privacy)** and **Theorem 5.** For `DB` uniform and `T(n) > polylog(n)`, there is
  an `Õ(√T(n))`-perturbation algorithm that is `(T(n), δ)`-private.

## Connections

- **Supersedes the central claim of [fibers-of-the-training-map](../../exp/docs/notes/fibers-of-the-training-map.md).**
  The size-versus-navigability distinction developed there is this paper's §3.1 against §3.2. The
  worked example there is ordinary least squares, which is **not** this paper's example. The attack
  here is a linear program over subset sums followed by rounding, and the words "least squares",
  "regression" and "OLS" do not occur in the PDF. See
  [native-asymmetry-in-learning](../analyses/native-asymmetry-in-learning.md).
- Restated for the modern setting by [Kaplan–Mansour–Nissim–Stemmer](kaplan-bayesian-memorization-reconstruction.md)
  as computational versus statistical memorization.
- Given a computational security definition by [Cohen et al.](cohen-data-reconstruction.md), which
  cites this paper as the origin of reconstruction attacks.
- Cited by [Haghifam–Smith–Ullman](haghifam-sample-complexity-mia.md) as the reconstruction-attack
  ancestor of the privacy-attack literature.
- [DP-SGD (ACG+16)](deep-learning-differential-privacy.md), the descendant defence.
- Concepts: [fiber-of-the-training-map](../concepts/fiber-of-the-training-map.md),
  [data-reconstruction-attack](../concepts/data-reconstruction-attack.md),
  [computational-differential-privacy](../concepts/computational-differential-privacy.md).

## Open Questions / Limitations

- The setting is a query-release mechanism over a bit database, not a training map. Whether the
  separation transfers to `D ↦ w` is the open question the programme inherits.
- Theorem 5 needs a prior on the database, and the case treated is the uniform one. The general
  distribution `DB` is set up in Definition 4 but the theorem is proved only for uniform.
- Section 3.3 shows the `Ω(√n)` bound is tight only via a mechanism the authors themselves call
  useless. Appendix B, "A Closer Look on the Threshold", gives a mechanism with some usability, but it
  works by releasing a noisy copy of the database rather than by perturbing answers, and it satisfies
  only the relaxed perturbation guarantee that holds for most queries.
- Appendix C shows query auditing leaks through its own refusals, and proposes self-auditing in
  response. The proposal is a suggestion, not a theorem.

## Quotes / Notable Passages

> "Applying this reconstruction algorithm to statistical databases we show that in order to achieve
> privacy one has to add perturbation of magnitude Ω(√n). That is, smaller perturbation always results
> in a strong violation of privacy."

> "For time-T bounded adversaries we demonstrate a privacy-preserving access algorithm whose
> perturbation magnitude is ≈ √T."

On why a computational definition was chosen over variance:

> "Secondly, this kind of definition does not allow us to capitalize on the limits of an adversary."

On the shape of the reconstruction task:

> "Note that in our case the list of feasible candidates is itself exponential in size, so our goal is
> not to compute the entire list, but to come up with one such candidate."

Opening §4:

> "A natural question is whether further restricting the adversary complexity enables achieving privacy
> using a smaller perturbation. In this section we answer this question positively."

On the price of the tight construction:

> "Note that, although guaranteeing perturbation magnitude of Õ(√n), the above algorithm renders the
> database effectively useless"
