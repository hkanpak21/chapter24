---
title: Computationally Differentially Private Inner-Product Protocols Imply Oblivious Transfer
type: source
date_ingested: 2026-08-20
authors: [Iftach Haitner, Noam Mazor, Jad Silbak, Eliad Tsfadia, Chao Yan]
venue: venue unconfirmed from PDF (arXiv:2502.15629v2 [cs.CR], 7 Jul 2025)
year: 2025
tags: [cryptography, computational-indistinguishability, hardness-reductions, differential-privacy, one-way-functions]
claim_quantifier: conditional
antecedent: "Existence of an (ε, 1/3n)-CDP two-party protocol estimating the inner product over {−1,1}^n × {−1,1}^n up to additive error n^{1/6}/(c·e^{cε}) with probability 0.999, for a universal constant c > 0."
adversary_bound: PPT (the CDP distinguisher); the reduction is uniform and black-box, so it also covers uniform distinguishers
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: attacker
cls_unit: time
cls_tightness: poly
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "Equation (1) only holds for computationally efficient (ppt) algorithms D, and not necessarily for any algorithm D."
cls_evidence_src: "§1 (Introduction, discussing Def 1.1)"
cls_reason: "Not an ML-attack-scenario paper (target/family/phase/access/write = none/n/a): a two-party CDP protocol result. party/unit/tightness from the CDP distinguisher D, restricted to ppt in Def 1.1's relaxation. baseline = n/a, no advantage-over-baseline game. second_party = none: no other party is bounded computationally in the headline theorem."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

Prices a two-party CDP protocol in cryptographic strength: at accuracy `O(n^{1/6})` for the inner product,
computational differential privacy is **equivalent to oblivious transfer**. The reduction is uniform and
fully black-box, and the paper notes this means the conclusion also holds for CDP defined against uniform
distinguishers.

The setting is the standard gap. Two parties hold `x, y ∈ {−1,1}^n` and want `⟨x, y⟩`. Randomized response
gives `ε`-DP with additive error `O_ε(√n)`, and that is essentially optimal — McGregor et al. FOCS'10 and
[HMST22](two-party-dp-complexity.md) show any `ε`-DP protocol needs `Ω_ε(√n)` even allowing
`δ ∈ o(1/n)`. In the centralized model the Laplace mechanism gets `O_ε(1)`. Given oblivious transfer the
parties can emulate the central mechanism by secure computation and recover `O_ε(1)`. The question is
whether anything weaker than OT suffices.

Answer: not at `O(n^{1/6})`. Theorem 1.3 turns such a protocol into an OT protocol, and Corollary 1.4 then
turns it into an `(ε, neg(n))`-CDP protocol with error `20/ε` — so "a protocol with a small polynomial
additive error is equivalent to a protocol with a constant error." This improves on the predecessor
[HMST22](two-party-dp-complexity.md), which got only key agreement, a primitive believed weaker and
insufficient for secure MPC.

**The accuracy threshold `O(n^{1/6})` is the exact logical boundary and nothing is claimed above it.** The
paper is careful that its result is *not* strictly stronger than HMST22: HMST22 covers the whole non-trivial
regime up to `O_ε(√n)` and holds in low-confidence regimes, while this result needs confidence 0.999 and
stops at `n^{1/6}`. The compensating advantages in the high-accuracy high-confidence regime are that the
reduction needs only **one** party to see the estimate, whereas HMST22 required the estimate to appear in
the transcript, and that the proof is conceptually simpler despite building a stronger primitive.

This is the closest the privacy literature comes to a graded computational price — but the grading is in
the *primitive* (key agreement versus OT), not in a resource budget, and the adversary remains PPT.

## Claim Boundary

- **Quantified over:** all `(ε, 1/3n)`-CDP two-party protocols meeting the stated accuracy and confidence;
  the conclusion is the existence of an OT protocol.
- **Antecedent:** as in the front matter. The reduction is uniform and black-box (footnote 1).
- **Excluded cases:** additive errors between `n^{1/6}` and `√n` are **open** — "we still do not know what
  is the right answer for additive errors in the range between n^{1/6} and √n." Low-confidence regimes
  are not covered. Functionalities other than inner product and Hamming distance (which reduces to it) are
  not covered.
- **Does not establish:** that CDP requires OT in general, in the central model, or for any other
  functionality. It does not establish anything about the client/server setting. It does not lower-bound a
  *resource* — it identifies a *primitive*.
- **Abstract vs theorem:** none found. The abstract states the `O(n^{1/6})` threshold and the improvement
  over HMST22 precisely.

## Key Contributions

- First equivalence between OT and a CDP protocol for a natural **non-Boolean** functionality. Prior
  OT-equivalences were for XOR, which the paper notes is "a less interesting functionality in the context of
  DP, as even in the centralized model, any DP algorithm for estimating XOR must incur an error close to
  one-half."
- Corollary: mild-polynomial accuracy and constant accuracy are equivalent for CDP inner product.
- A reduction requiring only that one party see the estimate.
- Machinery: the weak/approximate erasure channel (WEC/AWEC) route from a DP inner-product protocol to OT.

## Key Definitions / Theorems

- **Definition 1.1 (DP).** Standard; CDP is the relaxation where the distinguisher `D` is restricted to ppt.
- **Theorem 1.3 (Main, informal).** An `(ε, 1/3n)`-CDP protocol estimating the inner product over
  `{−1,1}^n × {−1,1}^n` up to additive error `n^{1/6}/(c·e^{cε})` with probability 0.999 can be used to
  construct an OT protocol.
- **Corollary 1.4.** Under the same hypothesis, there is an `(ε, neg(n))`-CDP protocol with additive error
  `20/ε` at probability 0.999.

## Connections

- Concept: [computational differential privacy](../concepts/computational-differential-privacy.md).
- Concept: [one-way functions](../concepts/one-way-functions.md) — for the hardness hierarchy this result
  places CDP inside.
- Direct predecessor: [HMST22](two-party-dp-complexity.md), whose key-agreement bound this improves in the
  high-accuracy regime. Appendix A shows HMST22's own protocol cannot imply OT, so a new construction was
  needed.
- The candidate separation whose complexity is being priced originates in
  [MPRV09](computational-differential-privacy.md) §5 (Hamming distance).
- Contrast with [GKY11](limits-cdp-client-server.md): CDP is powerful in the two-party model and the
  question there is *how expensive*; the client/server model is a different setting entirely.
- [GIKKM23](towards-separating-cdp.md)'s conclusion points at this line of work as the model for asking
  which assumptions are necessary for a central-model separation.
- Entities: [Salil Vadhan](../entities/salil-vadhan.md) (via the McGregor et al. bound this line answers).

## Open Questions / Limitations

- Close the accuracy gap between `n^{1/6}` and `√n`.
- Characterize CDP for functionalities beyond inner product and Hamming distance — "finding a more general
  characterization that captures more (or even all) functionalities, remains open."

## Quotes / Notable Passages

> "In particular, for the inner-product functionality, it was previously unknown whether oblivious transfer
> is necessary even for the best possible constant additive error."

> "It follows that a protocol with a small polynomial additive error is equivalent to a protocol with a
> constant error."

> "We remark that our result is not strictly stronger than [Hai+22]."
