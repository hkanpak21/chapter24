---
title: "Average-Case Fine-Grained Hardness"
type: source
date_ingested: 2026-08-22
authors: [Marshall Ball, Alon Rosen, Manuel Sabin, Prashant Nalini Vasudevan]
venue: "venue unconfirmed from PDF (no venue line; the document is dated February 27, 2017 and refers to a companion paper as [BRSV17])"
year: 2017
tags: [complexity-theory, cryptography, hardness-reductions, one-way-functions, fine-grained-cryptography, average-case-reductions]
claim_quantifier: conditional
antecedent: "Worst-case conjectures, each stated for randomized two-sided-error algorithms: the OV conjecture (n^{2-o(1)} for OV_d with d = ω(log n)), the 3SUM conjecture (n^{2-o(1)}), the APSP conjecture (n^{3-o(1)}), the Triangle-Collection conjecture, and SETH. Definition 2, the fine-grained one-way function, has no antecedent because it has no instantiation here: the paper defines it and then shows a barrier (NSETH) to the one construction route it proposes."
adversary_bound: "Uniform randomized algorithms in the Word RAM model with O(log n)-bit words, bounded by running time. Definition 2 quantifies over every algorithm running in O(t(n)^{1−δ'}) time, for every δ' > 0. Not circuits, not non-uniform, not queries."
date_verified: 2026-08-22
---

## Summary

The origin of average-case fine-grained hardness. The paper takes the three anchor problems of
fine-grained complexity — Orthogonal Vectors, 3SUM, and All-Pairs Shortest Paths — and produces for
each a family of low-degree polynomials over a finite field whose *average-case* evaluation cost is
pinned to the anchor problem's conjectured *worst-case* cost. The polynomials are `FOV`, `F3SUM`,
`FZWT` (Zero-Weight Triangle, a proxy that both 3SUM and APSP reduce to), and `FTC`
(Triangle-Collection, reduced to from k-SAT as well as 3SUM and APSP).

The mechanism is the classical random self-reducibility of low-degree polynomials — local
correctability of Reed-Muller codes — applied with the running-time bookkeeping made explicit, which
is what makes it fine-grained rather than merely polynomial. Lemma 1 converts an average-case solver
running in time `t` for a degree-`D` polynomial in `N` variables over `F_p` into a worst-case solver
running in `O(N D² log² p + D³ + tD)`. Because the constructed polynomials have degree `polylog(n)`,
the `tD` overhead is subpolynomial and the reduction preserves the exponent. The results are
therefore *tight in both directions*: `FOV` is evaluable in `Õ(n²)` and, under the OV conjecture,
requires `n^{2−o(1)}` even on uniformly random inputs; `FZWT` and `FTC` are cubic-computable and
sub-cubic-hard. Generalising OV to k-OV yields a conditional average-case time hierarchy, one problem
per integer `k`, all of it implied by SETH alone.

Section 5 is the part the survey needs. It states the case for fine-grained cryptography — *"We
hence consider fine-grained cryptography, where we only ask for security against adversaries that run
in some fixed polynomial time."* — and gives **Definition 2**, the fine-grained one-way function, in the
running-time convention. It then does not build one. The natural route, an input-output sampler `S`
for `FOV` running in sub-quadratic time, is shown to be blocked: the sampler's randomness `r` would be
a sub-quadratically verifiable certificate for NO instances of OV, hence for CNF-UNSAT, contradicting
NSETH. The paper's own suggestion for getting around this is an *erring* sampler, which would still
imply a single-round coAM protocol for OV with a sub-quadratic verifier, and it leaves that as an open
problem. So Definition 2 enters the literature as a definition with a barrier attached, not as a
realised object.

Two applications follow from the average-case hardness. A Proof of Work scheme, built from the
`FOV` polynomial and Williams's MA protocol, in which the challenger works about the square root of
the prover's cost. And *heuristic falsifiability*: because the hard instances are uniformly random and
the exponent is small, an empirically fast solver for `FOV` is real evidence against the OV
conjecture and hence against SETH — a falsification route that neither average-case analysis nor
fine-grained analysis supplies alone.

## Claim Boundary

- **Quantified over:** the four named polynomial families and their k-OV generalisation, and, in the
  average-case statements, the uniform distribution over the polynomial's own domain `F_p^N` — not
  over instances of OV, 3SUM, or APSP. Definition 1 fixes the success threshold at probability `3/4`.
  Appendix D amplifies this to a `1/polylog(n)` fraction of inputs by local list decoding, with a
  smooth running-time/success trade-off.
- **Antecedent:** the OV, 3SUM, APSP, and Triangle-Collection conjectures, and SETH. All are stated
  in the paper for randomized two-sided-error algorithms, which the authors defend as the right
  reading: *"we see these as structural beliefs about the problems – that brute force is essentially
  necessary."* None is standard in the sense that a lattice assumption is standard; they are
  conjectures with no reduction to anything weaker. SETH implies the OV conjecture, so `FOV` and `FTC`
  rest on the weakest antecedents in the paper.
- **Adversary class and machine model:** uniform randomized algorithms in the **Word RAM model with
  `O(log n)`-bit words**, measured by running **time**. Definition 2 quantifies over *all* algorithms
  running in `O(t(n)^{1−δ'})` time, for *every* `δ' > 0`. This is a uniform time bound, not a circuit
  size bound and not an oracle query bound, and it is not comparable to either without further
  argument. The paper notes the specifications could be restated for space or circuit size *"when
  working in other models"*, but does not do so.
- **Does not establish:** that a fine-grained one-way function exists. Definition 2 is stated and left
  uninstantiated; the only construction route offered is shown to break NSETH. It also does not
  establish average-case hardness *of OV, 3SUM, or APSP themselves* under any natural distribution —
  the hardness transfers to the polynomials, and the paper lists reducing the polynomials back to
  their source problems as open problem 2. The Proof of Work scheme is a construction from the
  average-case conjectures, not from any standard cryptographic assumption.
- **Abstract vs theorem:** none found. The abstract says the results assume *"widely-conjectured
  worst-case hardness"* and describes the cryptographic material as *"outline the construction of a
  Proof of Work scheme and discuss possible approaches to constructing fine-grained One-Way
  Functions"* — accurately weaker than the body would allow a careless reader to assume.

## Key Contributions

- Worst-case-to-average-case fine-grained reductions from OV, 3SUM, APSP (via Zero-Weight Triangle),
  and Triangle-Collection to the evaluation of explicit low-degree polynomials, with matching upper
  bounds so the exponent is tight on both sides.
- A conditional average-case time hierarchy: for every integer `k ≥ 2`, a problem computable in
  `Õ(n^k)` and requiring `n^{k−o(1)}` on average, the whole hierarchy implied by SETH.
- **Definition 2**, the running-time convention for a fine-grained one-way function.
- The NSETH barrier to building one from `FOV` by a perfect sampler, and the coAM barrier to building
  one from an erring sampler.
- A Proof of Work scheme with a square-root verification gap, based on a worst-case conjecture.
- Heuristic falsifiability: a route by which empirical measurement bears on a worst-case complexity
  conjecture.

## Key Definitions / Theorems

**Definition 1 (average-case computability), verbatim:**

> "A family of functions F = {fn } is computable in time t on average if there is an algorithm that
> runs in t(n) time on the domain of fn and, for all large enough n, computes fn correctly with
> probability at least 3/4 over the uniform distribution of inputs in its domain."

**Definition 2 (fine-grained one-way function), verbatim, in pieces as extracted:**

> "We say a function f : {0, 1}∗ → {0, 1}∗ is (t, )-one-way if it can be computed in"
> ... "time for some δ > 0, but for any δ" ... "-time algorithm A, and all sufficiently large n,"

with the displayed inequality `Pr_{x←{0,1}^n}[A(f(x)) ∈ f^{-1}(f(x))] ≤ ε(n, δ')`.

> **Transcription note.** `pdftotext` drops the `ε` from `(t, ε)-one-way` (it survives as a control
> byte), flattens both exponents, and strands the prime of `δ'` on a line of its own. Read in the PDF,
> the definition is: `f` is `(t, ε)`-one-way if it can be computed in `O(t(n)^{1−δ})` time for some
> `δ > 0`, but for any `δ' > 0`, any `O(t(n)^{1−δ'})`-time algorithm `A`, and all sufficiently large
> `n`, the displayed inversion probability is at most `ε(n, δ')`. The quoted fragments above are the
> extraction verbatim; the restored form is stated separately here rather than inside quotation marks.

**BRSV17's own convention, and why it is not interchangeable with the others.** See
[security gap exponent](../concepts/security-gap-exponent.md), which records two incompatible `δ`
conventions in this corpus. Definition 2 is the ancestor of the second of them, and matches neither
exactly:

| | BRSV17 Definition 2 |
|---|---|
| resource | running **time**, Word RAM, `O(log n)`-bit words |
| adversary | **uniform** randomized algorithm |
| baseline | an **external** threshold `t(n)`; the honest party must beat it, computing in `O(t(n)^{1−δ})` for **some** `δ > 0` |
| security quantifier | over **every** `δ' > 0`, i.e. against everything polynomially below `t(n)` |
| success bound | `ε(n, δ')` — a function of the security parameter **and of the adversary's own discount** |
| name for the gap | none. `δ` and `δ'` are separate local variables and neither is christened |

Two consequences matter for citation. First, this is the `T^{1−δ}`-versus-`T` shape of
[LLV19 Definition 5](pkc-fine-grained-setting.md), not the `honest^{1+δ}` circuit-size shape of
[BC22 Definition 6](fine-grained-one-way-functions.md); a `δ` carried between them without conversion
is wrong, and the conversion is `δ_A = δ_B/(1 − δ_B)`. Second, BRSV17's `ε` is indexed by the
adversary's discount `δ'` as well as by `n`, which neither of the later definitions does — the
achievable success probability is allowed to degrade as the adversary is given more budget. Anyone
quoting "BRSV17 Definition 2" as a single number is quoting something the paper does not define.

**Lemma 1 (fine-grained random self-reduction).** For a degree-`D` polynomial `f : F_p^N → F_p` with
`D > 9`, `p` prime, `p > 12D`, an average-case solver correct with probability `≥ 1 − ε` running in
time `t` yields a worst-case solver running in time `O(N D² log² p + D³ + tD)`.

**Theorem 1 / Corollary 1 (OV).** If `FOV` is computable in `O(n^{1+α})` time on average for some
`α > 0`, then OV is decidable in `Õ(n^{1+α})` in the worst case. Hence, verbatim:

> "if OV requires n2−o(1) time to decide, FOV requires n2−o(1) time to compute on average."

> **Transcription note.** `n2−o(1)` above is the extraction of `n^{2−o(1)}`.

**Theorem 2 / Corollary 3 (ZWT).** If either 3SUM requires `n^{2−o(1)}` or APSP requires `n^{3−o(1)}`,
then `FZWT` requires `n^{3−o(1)}` on average.

**Theorem 3 / Corollary 5 (Triangle-Collection).** If SETH holds, or 3SUM takes `n^{2−o(1)}`, or APSP
takes `n^{3−o(1)}`, then `FTC` requires `n^{3−o(1)}` on average.

**Theorem 4 / Corollary 6 (hierarchy).** For every `k ≥ 2`, if k-OV requires `n^{k−o(1)}`, then
`FOV_k` requires `n^{k−o(1)}` on average while being computable in `Õ(n^k)`.

**Definition 3 (Proof of Work).** `Challenge` and `Verify` computable in time `s(n)`, `Solve` in time
`t(n) > s(n)`, and any `A` that satisfies `Verify` with probability `≥ ε` must take time at least
`t'(n)` on an `ε'` fraction of challenges. Instantiated with `FOV`: `Challenge` and `Verify` in
`Õ(n)`, `Solve` in `Õ(n²)`.

**The barrier.** A perfect sub-quadratic input-output sampler for `FOV` would yield sub-quadratically
verifiable certificates for NO instances of OV and hence for k-SAT — verbatim, *"the impossibility of
this was recently conjectured and formalized as NSETH"*. An erring sampler escapes NSETH but yields a
single-round coAM protocol for OV with a sub-quadratic verifier, which the paper suggests conjecturing
as an `AM[2]SETH`.

## Connections

- [Security gap exponent](../concepts/security-gap-exponent.md) — the concept page holding the two
  incompatible `δ` conventions. Definition 2 above is the ancestor of Convention B and adds a third
  wrinkle (`ε` indexed by `δ'`).
- [Fine-grained cryptography](../concepts/fine-grained-cryptography.md) — the genre this paper names
  and motivates, verbatim: *"a form of cryptography might be realizable even in Impagliazzo's
  Pessiland"*.
- [On Building Fine-Grained One-Way Functions](fine-grained-one-way-functions.md) — Brzuska–Couteau's
  circuit-size convention, and the later attempt on the same target.
- [Public-Key Cryptography in the Fine-Grained Setting](pkc-fine-grained-setting.md) — the
  running-time convention in its named form, where "the gap" becomes an object.
- [Fine-Grained Cryptography](fine-grained-cryptography.md) (Degwekar–Vaikuntanathan–Vasudevan), cited
  here as prior work in the genre.
- [Fine-Grained Complexity of Empirical Risk Minimization](fine-grained-erm.md) and
  [fine-grained gradient computation for LLMs](fine-grained-gradient-llm.md) — the same OV/SETH
  machinery pointed at learning rather than at cryptography.
- [Orthogonal vectors conjecture](../concepts/orthogonal-vectors-conjecture.md).
- [One-way functions](../concepts/one-way-functions.md).
- [Calibrated proofs of work](calibrated-proof-of-work-extraction.md) and
  [Proof-of-Learning](proof-of-learning.md) — the same "prover must pay more than verifier" shape,
  priced in different units.
- [Permissionless consensus in the fine-grained setting](permissionless-consensus-fine-grained.md).

## Limits

- [A Fine-Grained World Without Cryptography](fine-grained-world-without-crypto.md)
  (Alman–Huang–Yeo) constrains how far the fine-grained programme can be pushed in a world with no
  one-way functions, and bounds the gap achievable by the LLV19 construction below quadratic.
- The NSETH barrier is internal to this paper and is stated by the authors, not by a later source:
  the route from `FOV` to a fine-grained one-way function is blocked unless NSETH is false.

## Open Questions / Limitations

- Open problem 6, in the paper's own numbering: *can a fine-grained OWF be constructed from
  worst-case hardness assumptions?* Definition 2 is not instantiated here.
- Open problem 2: reduce the polynomial families back to the problems they came from, which would
  give an average-case hard *distribution over OV/3SUM/APSP instances* rather than over polynomial
  inputs.
- Open problem 5: a single-round coAM protocol for OV with a sub-quadratic verifier — resolving this
  either way settles the erring-sampler route.
- No family of polynomials for k-CLIQUE is known that is both `n^{ωk/3}`-computable and of degree
  `n^{o(1)}`, so the fourth emerging island of fine-grained complexity is not covered.
- The two `k`-SUM-based hierarchies are loose: `n^{⌈k/2⌉−o(1)}` hardness against an `Õ(n^{k−1})`
  upper bound.

## Quotes / Notable Passages

> "All our discussion will be in the Word RAM model of computation with O(log(n))-bit words."

> "We hence consider fine-grained cryptography, where we only ask for security against adversaries that run in some fixed polynomial time."

> "a form of cryptography might be realizable even in Impagliazzo's Pessiland"

> "the impossibility of this was recently conjectured and formalized as NSETH"
