---
title: Preventing False Discovery in Interactive Data Analysis is Hard
type: source
date_ingested: 2026-08-20
authors: [Moritz Hardt, Jonathan Ullman]
venue: venue unconfirmed from PDF (arXiv:1408.1655v1 [cs.LG], 6 Aug 2014; recorded elsewhere in this repo as FOCS'14)
year: 2014
tags: [statistical-query, hardness-reductions, one-way-functions, cryptography, adaptive-data-analysis, differential-privacy]
claim_quantifier: conditional
antecedent: "Theorem 1.1 and 1.3: one-way functions exist (exponentially hard OWFs for the sharpest dimension regime). Theorem 1.2 is unconditional but requires dimension d = n^{3+o(1)}. All results require d growing more than logarithmically in n, so that 2^d is superpolynomial. The analyst must be computationally efficient."
adversary_bound: query count (n^{3+o(1)} adaptive statistical queries); the adaptive analyst is required to be computationally EFFICIENT, and the oracle is the party assumed computationally bounded
cls_target: train data
cls_family: reconstruct
cls_phase: post hoc
cls_access: scores
cls_write: read only
cls_frame: compute
cls_party: attacker
cls_unit: queries
cls_tightness: exponent
cls_baseline: absent
cls_baseline_checked: yes
cls_second_party: samples
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "Assuming one-way functions exist, there is no computationally efficient oracle that given n samples is accurate on n3+o(1) adaptively chosen queries"
cls_evidence_src: "Thm 1.1"
cls_reason: "family=reconstruct classifies the attack mechanism that proves Theorem 1.1 (a fingerprinting-code tracing algorithm recovering elements of the oracle's sample S), per Rule 1's demand to classify the theorem; the paper's own framing ('do not file this as a privacy result') is about statistical validity versus confidentiality, not about whether the underlying technique is reconstruction, so family tracks the mechanism used, not the paper's chosen frame. party=attacker/unit=queries per Rule 3: n^{3+o(1)} is how many adaptive queries the analyst wields before the oracle is forced blatantly wrong; both oracle and analyst are 'computationally efficient' (both computational), so per Rule 4's tie-break the adversary's bound decides the row. second_party=samples records the oracle's own resource n, against which the exponent 3 in n^{3+o(1)} is stated, mirroring the haghifam-sample-complexity-mia precedent's second_party=samples structure for an analogous attacker-vs-honest-party exponent. tightness=exponent because the paper states the bound is tight 'up to a factor of n' against the known n^2 efficient upper bound, an explicit relation to the honest mechanism's own achievable performance, not a bare numeric budget. access=scores: a statistical query returns an approximate real-valued answer to α-tolerance, not a hard label or an access-unspecified black box."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The existence proof that **query count can be a rigorous security parameter with matching upper and lower
bounds**. Under a standard cryptographic assumption, no computationally efficient oracle given `n` samples
can give statistically valid answers to `n^{3+o(1)}` adaptively chosen statistical queries. Set against
Dwork–Feldman–Hardt–Pitassi–Reingold–Roth, who answer exponentially many adaptive queries inefficiently and
quadratically many efficiently, the bound is tight up to a factor of `n`.

**It is about statistical validity, not confidentiality.** The oracle's job is to answer `q(D) = E_{x∼D} p(x)`
to within a constant `α` — to *generalize* to the underlying distribution — and the failure mode is false
discovery, not disclosure. The paper is explicit about the difference from the privacy setting: "In the
privacy setting, accuracy is defined with respect to the oracle's sample. It is trivial to maintain accuracy
with respect to the sample by answering each query with the sample mean, which succeeds even when the oracle
is blatantly non-private. In the setting of false discovery, we define accuracy with respect to the
underlying distribution and show that achieving this notion of accuracy is hard for the oracle." Do not file
this as a privacy result.

The attack is a reconstruction attack driven by a **fingerprinting code**. The code's challenge queries,
answered accurately, let a tracing algorithm recover one element of the oracle's sample. Iterating over
`n − O(1)` rounds of roughly `n²` queries each shrinks the oracle's effective sample to constant size, after
which finding a blatantly wrong answer is easy. Two subtleties do the real work. First, nothing stops the
oracle from evaluating a challenge query *outside* its sample, which would leak distributional information
the oracle did not have; the fix is to **encrypt** the query definition off-sample, which is exactly where
the computational hypothesis enters and is why one-way functions suffice. For "natural" oracles that only
report empirical quantities, the problem does not arise and §3 gives an unconditional proof. Second, tracing
needs accuracy on the *sample* while the hypothesis gives accuracy on the *distribution*; the gap is closed
by a measure-concentration property of the chosen code, requiring the robust fingerprinting codes of
Bun–Ullman–Vadhan.

Theorem 1.2 removes the assumption at the price of dimension: with `d = n^{3+o(1)}`, no **computationally
unbounded** oracle is accurate on `n^{3+o(1)}` adaptive queries. And Theorem 1.3 restates the main result as
a privacy statement — any efficient oracle accurate on that many adaptive queries must be blatantly
non-private.

For this programme the value is the **shape**: a resource (adaptive query count), a matching upper bound, a
lower bound at a stated exponent, and a hardness assumption doing exactly one identifiable job. That is what
a computational security parameter looks like when it works. What is missing is any pricing of the analyst's
*compute* relative to the oracle's — both are "efficient," undifferentiated.

## Claim Boundary

- **Quantified over:** Theorem 1.1 over all computationally efficient oracles (running in time polynomial in
  `n` and `d` per query), for every distribution `D`; the analyst is a specific efficient adaptive algorithm,
  so the lower bound is constructive on the attack side. Theorem 1.2 over all oracles including unbounded
  ones.
- **Antecedent:** one-way functions exist, for Theorem 1.1 / 1.3; **exponentially hard** one-way functions
  for the strongest dimension regime (footnote 1). Dimension must satisfy `2^d` superpolynomial in `n` —
  necessary, since if `n ≫ 2^d` the empirical distribution is close in statistical distance and every query
  can be answered. Theorem 1.2 needs `d = n^{3+o(1)}`.
- **Excluded cases:** low-dimensional data is excluded and the paper explains why the exclusion is
  unavoidable. **Non-adaptive** queries are entirely outside the result — exponentially many
  (`k = 2^{o(n)}`) can be answered by Hoeffding plus a union bound, so the whole phenomenon is about
  adaptivity. The `n²`-to-`n³` gap is not closed.
- **Does not establish:** a confidentiality result. It establishes hardness of *statistical validity*.
  Theorem 1.3 does yield blatant non-privacy, but as a consequence of validity being maintained, not as a
  privacy lower bound in its own right. It does not establish that any particular deployed system is
  attackable. It does not price the analyst's compute against the oracle's.
- **Abstract vs theorem:** none found. The abstract states the hardness assumption, the exponent, and the
  tightness up to a linear factor.

## Key Contributions

- `n^{3+o(1)}` adaptive statistical queries is hard for efficient oracles under OWFs — the first
  **computational** barrier to preventing false discovery, and tight to within a factor `n` against known
  upper bounds.
- An unconditional version for unbounded oracles at dimension `n^{3+o(1)}`.
- An efficient reconstruction attack built from robust fingerprinting codes plus encryption, with the
  encryption isolating exactly the step where computational hardness is needed.
- The unconditional special case for "natural" oracles that answer using only sample statistics.
- The framing that statistical validity alone — with no privacy requirement at all — can be a source of
  computational intractability in adaptive settings.

## Key Definitions / Theorems

- **Setting.** SQ model of Kearns. `X = {0,1}^d`; a statistical query is a predicate `p : X → {0,1}`;
  `q(D) = E_{x∼D} p(x)`; an answer `a` is valid if `|a − q(D)| ≤ α` for a small constant `α`. An oracle is
  *accurate given `n` samples for `k` adaptively chosen queries* if for every `D` it answers any efficient
  adaptive analyst's `k` queries accurately.
- **Theorem 1.1.** Assuming one-way functions exist, there is no computationally efficient oracle that given
  `n` samples is accurate on `n^{3+o(1)}` adaptively chosen queries.
- **Theorem 1.2.** There is no computationally unbounded oracle that given `n` samples of dimension
  `d = n^{3+o(1)}` is accurate on `n^{3+o(1)}` adaptively chosen queries.
- **Theorem 1.3.** Under OWFs, any efficient oracle accurate on `n^{3+o(1)}` adaptive queries must be
  blatantly non-private.

## Connections

- Concept: [statistical query model](../concepts/statistical-query-model.md).
- Concept: [adaptive data analysis](../concepts/adaptive-data-analysis.md).
- Concept: [one-way functions](../concepts/one-way-functions.md).
- Concept: [data reconstruction attack](../concepts/data-reconstruction-attack.md).
- Uses the SQ model in the opposite role from [KLNRS08](what-can-we-learn-privately.md): there SQ restricts
  a private learner and the equivalence is with local DP; here the SQ oracle is the defender and the analyst
  is the attacker.
- [ML24](query-complexity-reconstruction.md) also makes query count the security parameter, but for
  reconstruction, and without any hardness assumption or computational restriction on the adversary. HU14 is
  the model of how to do it with one.
- Descendant of [Dinur–Nissim PODS'03](dinur-nissim-revealing-information.md) on the reconstruction side.
- [CIM19](capacity-bounded-dp.md) §6 arrives at a generalization guarantee from a restricted-adversary
  privacy notion — the positive direction of the same adaptive-data-analysis story.
- Entities: [Jonathan Ullman](../entities/jonathan-ullman.md), [Moritz Hardt](../entities/moritz-hardt.md).

## Open Questions / Limitations

- Close the gap between the `n²` efficient upper bound and the `n^{3+o(1)}` lower bound.
- The hardness applies to worst-case adaptive analysts; whether realistic analysts hit the barrier is not
  addressed.
- The two parties are both "efficient" with no relative budget; there is no exponent separating analyst from
  oracle.

## Quotes / Notable Passages

> "Conceptually, our result demonstrates that achieving statistical validity alone can be a source of
> computational intractability in adaptive settings."

> "In the setting of false discovery, we define accuracy with respect to the underlying distribution and show
> that achieving this notion of accuracy is hard for the oracle."

> "our result suggests that the perceived difficulty of preventing false discovery in today's collaborative
> research environment may be inherent."
