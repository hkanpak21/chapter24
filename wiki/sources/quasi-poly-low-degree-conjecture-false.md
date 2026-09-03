---
title: The Quasi-Polynomial Low-Degree Conjecture is False
type: source
date_ingested: 2026-08-21
authors: [Rares-Darius Buhai, Jun-Ting Hsieh, Aayush Jain, Pravesh K. Kothari]
venue: FOCS 2025 (the ingested PDF is arXiv:2505.17360v1, 23 May 2025, and does not itself state a venue)
year: 2025
tags: [complexity theory, low-degree-polynomials, statistical-computational-gaps, cryptography]
claim_quantifier: existential
antecedent: "none for the refutation itself. The constructions are unconditional. The first uses list decoding of Reed-Solomon codes in the high-error regime; the second is an explicit pair of rotation-invariant matrix distributions."
adversary_bound: "the object refuted is a bound on adversaries. The conjecture asserted that vanishing low-degree advantage rules out noise-tolerant distinguishers of a given running time, and the paper exhibits distinguishers that survive."
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: time
cls_tightness: quasi-poly
cls_baseline: n/a
cls_second_party: none
cls_assessed: explicit
cls_evidence: "the corresponding ε-noisy distinguishing problem can be solved in n^{O(log^{1/(k−1)}(n))} time"
cls_evidence_src: abstract
cls_reason: "Classified on the exhibited distinguisher of Thm 1.3, which the page's own Claim Boundary calls 'ordinary algorithms' not restricted to any class, so unit=time rather than algo class. No vocabulary value cleanly fits a quasi-polynomial runtime; budget was chosen as the closest (an explicit, stated runtime, no honest-party relation to compare it against) and is flagged as a vocabulary gap. second=none because the paper's substance is one distinguisher characterized under two resource axes, algorithm class and time, not two distinct bounded parties, which the second field does not capture. RECODE 2026-09-03 (R4, no adversary means no phase): phase train time -> n/a."
cls_second_notion: algo class
cls_prov: P
cls_date: 2026-08-22
---

## Summary

Hopkins' low-degree conjecture asserted that for a planted-versus-null distinguishing problem whose
null is a product distribution on `{0,1}^{binom(n,k)}` and whose planted distribution is invariant
under relabelling of `[n]`, a vanishing degree-`D` low-degree advantage rules out any noise-tolerant
distinguisher running in time `n^{D/polylog(n)}`. The two side conditions were the accumulated repairs
of a decade of near misses. Permutation invariance was added to block the error-correcting-code
counterexamples of [Holmgren and Wein](holmgren-counterexamples-low-degree.md), and noise tolerance to
block brittle algebraic algorithms such as Gaussian elimination and lattice basis reduction.

The paper disproves the conjecture in its own regime, satisfying both conditions. For every `ε > 0`
and integer `k ≥ 2` it constructs a permutation-invariant planted distribution whose degree-`n^{1−O(ε)}`
advantage against the uniform null is exactly zero, while the `ε`-noisy distinguishing problem is
solved with probability `1 − o(1)` in `n^{O(log^{1/(k−1)}(n))}` time. The construction is a
permutation-resilient, efficiently list-decodable code: sample a message, encode it so that the
codeword distribution is `D`-wise uniform, corrupt each entry independently, then apply a uniformly
random relabelling. Vanishing advantage follows from the dual code's distance, and the distinguisher
is high-error list decoding of Reed-Solomon codes.

A second, independent construction addresses a different piece of folklore. On `n × n` real matrices
the paper exhibits rotation-invariant `P_n` and `Q_n` whose degree-`Ω̃(n^{1/3})` advantage is `o(1)`,
while the largest eigenvalue distinguishes a noisy planted sample in polynomial time. The null here is
not a product distribution, so this does not refute the conjecture as stated, but it does contradict
the widely repeated intuition that simple spectral methods are captured by polylogarithmic-degree
polynomials. The mechanism is that the two ensembles have norms `1` and `1 + λ*` with
`λ* = 1/poly(n)`, so the trace of `A^{2k}` fails to separate them even at `k = n^c`.

## Claim Boundary

- **Quantified over:** the refutation is existential. It exhibits one family of distribution pairs per
  `(ε, k)`. It does not say that vanishing low-degree advantage generally fails to predict hardness,
  and the paper is careful that its own constructions are contrived rather than natural.
- **Antecedent:** none. Both constructions are unconditional, which is what makes this a refutation
  rather than a conditional separation.
- **Adversary class:** the low-degree class is the object under test. The distinguishers exhibited are
  ordinary algorithms, quasi-polynomial in the first construction and polynomial in the second and in
  the rectangular variant.
- **Does not establish:** that low-degree lower bounds are worthless. The paper says vanishing advantage
  may still be read as evidence of hardness. It also does not touch the `k = 1` Boolean vector case,
  where the concurrent [Hsieh, Kane, Kothari, Li, Mohanty and Tiegel](rigorous-implications-low-degree.md)
  proves the conjecture. The two together resolve the Boolean alphabet case in opposite directions at
  `k = 1` and `k ≥ 2`. The matrix construction does not refute the stated conjecture, because its null
  is not product.
- **Abstract vs theorem:** the title is stronger than the theorem in one respect worth keeping
  straight. What is refuted is the conjecture at quasi-polynomial time for `k ≥ 2`. The refutation with
  a *polynomial*-time distinguisher holds for the natural rectangular generalisation, where the
  symmetry group is the one appropriate to unequal-sized modes, not for the square `S_n`-symmetric
  statement. The paper marks the distinction itself, and lists improving the distinguisher to
  polynomial time in the square case as open.

## Key Contributions

- Theorem 1.3. For every `ε > 0` and `k ≥ 2` there is a `P_n` meeting every condition of the
  conjecture with degree-`n^{1−O(ε)}` advantage equal to `0`, distinguishable from the noisy null in
  `n^{O(log^{1/(k−1)}(n))}` time with probability `1 − o(1)`.
- Definition 1.4 and Observation 1.5. A permutation-resilient, efficiently list-decodable code whose
  codeword distribution is `D`-wise uniform and whose decoder tolerates a constant corruption rate and
  runs in `n^{o(D/polylog(n))}` time immediately falsifies the conjecture. This turns the refutation
  into a coding-theoretic construction problem, which is then solved with Reed-Solomon codes in the
  list-decoding regime.
- Theorem 2.4 with Remark 2.3. Under the natural symmetry for rectangular inputs, the same
  construction yields a polynomial-time distinguisher, refuting the heuristic that
  polylogarithmic-degree indistinguishability rules out polynomial-time noise-tolerant algorithms.
- Theorem 1.6. Rotation-invariant `P_n` and `Q_n` on `R^{n×n}` with degree-`Ω̃(n^{1/3})` advantage
  `o(1)` and a polynomial-time distinguisher given by the largest eigenvalue, together with Remark 1.7
  fixing a noise model, a scaled independent draw from the null, and a proof that the advantage stays
  vanishing for the noisy pair as well.
- The observation that the noisy polynomial interpolation problem underlying the first construction is
  the same shape as decoding randomly permuted noisy evaluations in McEliece-style cryptosystems.

## Key Definitions / Theorems

- **Definition 1.1, low-degree advantage.** `Adv^{≤D}(P, Q)` is the maximum over degree-`D` polynomials
  `f` of `(E_P f − E_Q f)/sqrt(Var_Q f)`. It is the degree-`D` truncation of the likelihood ratio and is
  usually easy to compute, which is the source of the heuristic's appeal.
- **Conjecture 1.2, the low-degree conjecture.** Fix `k`. Let `Q_n` be uniform on `{0,1}^{binom(n,k)}`
  and `P_n` be `S_n`-invariant on the same domain. If `Adv^{≤D}(P_n, Q_n) = O(1)` then for every fixed
  `ε > 0` there is no `n^{D/polylog(n)}`-time algorithm distinguishing `T_ε P_n` from `Q_n` with
  probability `1 − o(1)`, where `T_ε` replaces each coordinate with a uniform bit independently with
  probability `ε`.
- **Theorem 1.3, Theorem 2.4, Theorem 1.6** as summarised above.
- **Definition 1.4, permutation-resilient efficiently list-decodable code.** The decoder must recover a
  `poly(n, k)`-size list containing the message after independent bit flips at rate `ε` *and* a uniformly
  random relabelling of the tensor coordinates.

## Consequence for a restricted-class security claim

The line to carry forward is that "low-degree-bounded adversary" and "quasi-polynomial-time adversary"
are provably different objects. Before this result the two could be treated as interchangeable for
`S_n`-symmetric noisy problems, since the conjecture asserted that one implied the other. It does not.
Any security claim resting on a low-degree adversary must therefore say which of the two it means, and
must cite both this paper and its positive counterpart,
[Rigorous Implications of the Low-Degree Heuristic](rigorous-implications-low-degree.md), because that
paper's guarantees are the only ones now known to survive and they hold under strictly narrower
hypotheses.

The paper's own measured conclusion is that vanishing advantage remains usable as evidence of hardness
for well-studied problems where decades of algorithmic effort have failed, and that it should be
treated with caution for new and unexplored problems, naming cryptographic hardness assumptions as the
case where caution is most needed.

## Connections

- [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md) is the framework
  whose central conjecture this refutes.
- [Rigorous Implications of the Low-Degree Heuristic](rigorous-implications-low-degree.md) is the
  concurrent positive counterpart, and proves the `k = 1` case that this paper leaves untouched.
- [Counterexamples to the Low-Degree Conjecture](holmgren-counterexamples-low-degree.md) is the earlier
  refutation this one supersedes in scope, and the source of the code-based technique the construction
  extends to the permutation-invariant setting.
- [Computational Complexity of Statistics: New Insights from Low-Degree Polynomials](low-degree-polynomials-survey.md) is the survey through
  which the heuristic reached the applications now affected.
- [Statistical Query Algorithms and Low-Degree Tests Are Almost Equivalent](brennan-sq-lowdegree-equivalence.md)
  is the equivalence that transmits this caveat to the statistical query side.
- [Statistical Query Model](../concepts/statistical-query-model.md)
- [Cryptography from Planted Graphs: Security with Logarithmic-Size Messages](cryptography-from-planted-graphs.md) and
  [Public-Key Encryption from Planted Clique and Noisy k-LIN Over Expanders](pke-from-planted-clique.md) are constructions in the
  affected family, where security rests on planted-distribution hardness.
- [Low-Degree Security of the Planted Random Subgraph Problem](bogdanov-low-degree-planted-subgraph.md)
  is a security guarantee stated against a low-degree adversary, which this result recasts as a
  guarantee against that class and nothing wider.
- [Lattice-Based Methods Surpass Sum-of-Squares in Clustering](zadik-lattice-surpass-sos.md) is the brittle-algorithm
  family the noise condition was designed to exclude.
- [Pravesh K. Kothari](../entities/pravesh-kothari.md)

## Open Questions / Limitations

- Improving the square-case distinguisher from `n^{log^δ n}` to polynomial time, which the paper
  reduces to building an efficient permutation-invariant list-decodable code with large dual distance.
- Finding further algorithmic techniques that circumvent the conjecture, since each one marks a
  direction in which low-degree lower bounds can be surpassed for specific problems.
- Reformulating the conjecture under additional conditions that exclude these constructions while
  still covering well-studied average-case problems. No candidate reformulation is offered.
- Characterising rigorously which class of algorithms a vanishing advantage does rule out. The paper
  states that little work exists in this direction and points at its concurrent counterpart as the
  first progress.
- The matrix construction leaves the right noise model for non-product nulls unsettled, since no
  precise formulation exists in the literature for that case.

## Quotes / Notable Passages

> Our results suggest that while a vanishing LDA may still be interpreted as evidence of hardness,
> developing a theory of average-case complexity based on such heuristics requires a more careful
> approach.

> But how should we interpret vanishing LDA based hardness for a new and relatively unexplored problem
> [...] In such cases, our work suggests significant caution.

> This result goes against the conventional wisdom that spectral methods, at least of the simple kind
> that compute the largest eigenvalue, are "captured by polylog(n)-degree polynomials".
