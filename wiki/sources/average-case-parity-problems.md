---
title: "Average-Case Hardness of Parity Problems: Orthogonal Vectors, k-SUM and More"
type: source
date_ingested: 2026-08-20
authors: [Mina Dalirrooyfard, Andrea Lincoln, Barna Saha, Virginia Vassilevska Williams]
venue: "venue unconfirmed from PDF (the PDF is arXiv:2503.21951v1, 27 Mar 2025; raw/SOURCES.md records SODA 2025)"
year: 2025
claim_quantifier: conditional
antecedent: "At least one of: the randomized Exponential Time Hypothesis (rETH), the k-OV hypothesis, the k-SUM hypothesis, the k-XOR hypothesis, or the k-clique hypothesis. All are worst-case fine-grained hypotheses; the disjunctive form makes the antecedent unusually weak."
tags: [complexity-theory, average-case-reductions, hardness-reductions, fine-grained-cryptography, statistical-computational-gaps]
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: time
cls_tightness: exponent
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed:
cls_evidence: "Assuming that at least one of the worst-case k-OV, k-SUM, or k-XOR hypotheses holds, all of parity-k-OV, parity-k-SUM and parity-k-XOR are n^{Ω(√k)}-hard on average for a natural distribution."
cls_evidence_src: Thm 1.1
cls_reason: "party=learner, not attacker: the Claim Boundary states the paper 'does not discuss cryptography at all' and there is no attacker/defender security game, only an algorithm attempting to solve a computational problem on average -- matching the convention used elsewhere in this corpus for non-adversarial hardness-of-computation papers (e.g. bandeira-franz-parisi-criterion, detection-recovery-refutation-gaps) rather than the attacker convention used for security definitions (e.g. authentication-bounded-storage). phase=n/a rather than train time because this is a combinatorial decision/counting problem (k-OV/k-SUM/k-XOR), not a statistical learning task -- the 'train time' convention in this corpus is reserved for SQ/low-degree hardness of learning specifically. tightness=exponent: the paper's own framing is 'a quadratically or cubically degraded exponent, not the worst-case one' (Summary), i.e. an explicit stated relation between the average-case lower bound (sqrt(K) or K^{1/3}) and the worst-case exponent K that functions as the honest/reference bound. family=none/target=none because no ML asset or attack family applies. Flagged gap: the theorems additionally require near-perfect success probability (1-Theta(1/2^K)), a second bound on the same party (the solving algorithm) with no matching unit in the vocabulary (not queries/samples/memory/algo class/perturbation/corruption/rounds/privacy budget) -- left out of second_notion rather than guessed; the Claim Boundary itself flags this as the paper's most important limitation for any cryptographic reading."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

Supplies what average-case fine-grained complexity has been missing for its three core problems: an
explicit, easy-to-sample distribution on which a version of `k`-OV, `k`-SUM and `k`-XOR is provably
hard, conditioned on worst-case hypotheses. The version is the **parity of the count** — return one
bit, the parity of the number of `k`-tuples that are orthogonal / sum to zero / XOR to zero.

The route is to improve the Dalirrooyfard-Lincoln-Vassilevska Williams *factored problem* framework
and then reduce factored problems back to their un-factored counterparts, which is the step nobody had.
Two relaxations do the work: polynomials over the integers rather than modulo a prime, and *`d`-partite*
rather than *strongly `d`-partite* polynomials — each monomial takes **at most** one variable per
section instead of exactly one. The authors call these *fine `d`-degree polynomials*.

The headline exponents are the boundary. Worst-case, all three problems take `dn^{Θ(k)}`. The
average-case lower bounds obtained here are `N^{Ω(√K)}` under rETH and `N^{K^{1/3}/4−o(1)}` under the
`K`-XOR or `K^{1/3}`-SUM hypotheses — **a quadratically or cubically degraded exponent**, not the
worst-case one. Under the disjunction of all the standard hypotheses, `N^{Ω(K^{1/3})}`.

## Claim Boundary

- **Quantified over:** Algorithms with a **very high success-probability requirement**. Theorems 1.3
  and 1.4 bound *"any algorithm that solves P of size N with vectors of dimension Θ(K lg N) with
  probability 1 − Θ(1/2^K)"*. Nothing at all is claimed about an algorithm that succeeds with, say,
  probability `0.99`, or `1/2 + ε`. The general framework (Theorem 1.6) needs success probability
  `≥ 1 − 1/(2^{d+2}(d + log_2 M)^d)`. This is the single most important limitation for anyone
  contemplating a cryptographic application: security definitions need hardness against **low**-advantage
  adversaries, and these theorems give hardness only against **near-perfect** ones. Machine model is
  ordinary uniform algorithms; no circuit or non-uniform statement is made.
- **Antecedent:** Worst-case fine-grained hypotheses, in a disjunction. The distributions
  `D^P_1, D^P_2, D^P_3` are *constructed* by the reductions — one distribution per hypothesis — not
  the natural uniform distribution over instances.
- **Does not establish:** Average-case hardness of the **search** or **decision** versions of `k`-OV,
  `k`-SUM or `k`-XOR. The paper is explicit that the parity results are *"an intermediate step towards
  the ultimate goal of resolving the average case complexity of the detection problems."* It also does
  not establish hardness at the worst-case exponent: `√K` and `K^{1/3}` are not `K`.
- **Abstract vs theorem:** None found. The abstract states the `n^{Ω(√k)}` and `n^{Ω(k^{1/3})}`
  exponents and says "for specific distributions" throughout.

**On cryptographic applications.** `raw/SOURCES.md` records that this paper "claims no crypto
applications". The accurate statement is weaker and cleaner: **the paper does not discuss
cryptography at all.** The string "Cryptography" occurs exactly once in the extracted text, inside a
bibliography entry for a DIMACS workshop volume. There is no claim either way.

## Key Contributions

- **Theorem 1.6**: the simplified worst-case-to-average-case framework — a problem representable by a
  *fine `d`-degree polynomial* over the integers admits a random self-reduction with overhead
  `O((2d + 2 log_2 M)^d (n + T(n)))`. The relaxation from strongly-`d`-partite to `d`-partite is what
  admits parity and higher-degree functions.
- **Theorem 1.3**: average-case lower bounds for parity-`K`-OV and parity-`K`-XOR under rETH, the
  `K`-XOR hypothesis, and the `K^{1/3}`-SUM hypothesis, on three explicit distributions.
- **Theorem 1.4**: the corresponding bounds for parity-`K`-SUM, including `N^{Ω(√(K/lg K))}` under rETH.
- **Theorem 1.5**: hardness for all three from the `k`-clique hypothesis at `N^{(√(2K)+1)ω/6−o(1)}`,
  where `ω` is the matrix-multiplication exponent.
- **Theorem 5.3 / §6**: reductions from factored problems to un-factored ones, and average-case
  parity-subgraph-counting for any `k`-node pattern `H`, extending Boix-Adserà-Brennan-Bresler.
- Resolves a question of Jafargholi and Viola about carrying a 4-clique-to-6-SUM reduction over `Z_2^t`.

## Key Definitions / Theorems

- **Theorem 1.1 (informal), verbatim:** *"Assuming that at least one of the worst-case k-OV, k-SUM, or
  k-XOR hypotheses holds, all of parity-k-OV, parity-k-SUM and parity-k-XOR are n^{Ω(√k)}-hard on
  average for a natural distribution."*
- **Theorem 1.3.** For `P ∈ {parity-K-OV, parity-K-XOR}` and `K` constant, there are easy-to-sample
  `D^P_1, D^P_2, D^P_3` such that any algorithm solving `P` of size `N` in dimension `Θ(K lg N)` with
  probability `1 − Θ(1/2^K)` requires `N^{Ω(√K)}` (rETH), `N^{K^{1/3}/4−o(1)}` (`K`-XOR), or
  `N^{K^{1/3}/4−o(1)}` (`K^{1/3}`-SUM) time respectively.
- **Theorem 1.6.** If a fine `d`-degree polynomial `f` agrees with `P` on `{0,1}^n`, and an
  average-case algorithm `A` succeeds on uniform `Z_2^n` with probability
  `≥ 1 − 1/(2^{d+2}(d + log_2 M)^d)`, then there is a randomized worst-case algorithm `B` running in
  `O((2d + 2 log_2 M)^d (n + T(n)))`.

## Connections

- **The distribution problem this corpus keeps hitting.**
  [The Planted Orthogonal Vectors Problem](planted-orthogonal-vectors.md) attacks the same gap for
  `k`-OV by *conjecturing* hardness of a planted distribution; this paper *proves* hardness, but for
  the parity variant and at a degraded exponent. Neither yields what a fine-grained key exchange
  needs. Reading them together is the clearest statement of where average-case fine-grained
  complexity actually is.
- [Public-Key Cryptography in the Fine-Grained Setting](pkc-fine-grained-setting.md) is the paper that
  needs an average-case hypothesis of exactly this kind and, lacking one, assumes it outright.
- [Towards Permissionless Consensus](permissionless-consensus-fine-grained.md) uses the arithmetized
  `k`-OV polynomial `fOV_k` and its own robust direct sum theorem — the same low-degree-polynomial
  self-reduction machinery this paper generalizes.
- Concepts: [Orthogonal Vectors Conjecture](../concepts/orthogonal-vectors-conjecture.md),
  [Average-Case Reductions](../concepts/average-case-reductions.md),
  [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md).
- **Not** the low-degree framework this wiki already catalogues. The "low-degree polynomial" here is a
  *polynomial representation* of the problem used to build a random self-reduction; the wiki's
  [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md) is the low-degree
  *likelihood ratio* heuristic for statistical-computational gaps. Same phrase, unrelated objects.
- Compare the planted-clique lineage in this wiki:
  [Planted Clique Conjectures are Equivalent](hirahara-planted-clique-conjectures-equivalent.md),
  [Cryptography from Planted Graphs](cryptography-from-planted-graphs.md),
  [PKE from Planted Clique](pke-from-planted-clique.md) — the same worst-case-to-average-case-then-
  build-crypto pattern, on a different problem family and further along.

## Open Questions / Limitations

- The detection (decision) and search versions remain open on average; the authors present parity as
  an intermediate step toward them.
- The success-probability requirement `1 − Θ(1/2^K)` is far from what cryptography needs and the paper
  does not address amplification.
- The exponents `√K` and `K^{1/3}` fall well short of the worst-case `K`.
- The distributions are constructed to fit the reduction; nothing is proved about uniform instances.

## Quotes / Notable Passages

> "However, no average-case hardness has been proven so far for the core problems of fine-grained
> complexity like k-SUM, k-OV, and k-XOR, even for their counting versions."

> "The hardness of the parity versions can naturally be seen as an intermediate step towards the
> ultimate goal of resolving the average case complexity of the detection problems."
