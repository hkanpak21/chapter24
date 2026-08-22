---
title: Limits of Computational Differential Privacy in the Client/Server Setting
type: source
date_ingested: 2026-08-20
authors: [Adam Groce, Jonathan Katz, Arkady Yerukhimovich]
venue: Theory of Cryptography Conference (TCC) 2011 — not stated in this PDF; attribution taken from the reference list of DP20_SoKDifferentialPrivacies ("Theory of Cryptography Conference, pages 417–431, Springer, 2011") and from the abstract of BCV16 ("Groce, Katz and Yerukhimovich (TCC 2011)")
year: 2011
tags: [cryptography, computational-indistinguishability, impossibility-frameworks, one-way-functions, differential-privacy]
claim_quantifier: conditional
antecedent: "Two separate and independent results. (1) The construction is fully black-box from a primitive instantiable by a random object. (2) The mechanism's output lies in R^n for CONSTANT n, and its average (p,v)-error is polynomially bounded."
adversary_bound: PPT (the CDP adversary); the constructed statistical mechanism is private against unbounded adversaries
---

## Summary

The paper usually cited for "computational differential privacy buys nothing from a single curator."
It does not say that. It proves **two separate conditional results**, each with a stated scope, and the
authors devote a titled subsection — *Limitations of our results*, at the end of §1.1 — to naming the
cases they do not cover. **A released machine-learning model is squarely inside the excluded set**, and
that is the single most consequential boundary fact in this corpus. Reproducing the folk version anywhere
in this wiki is a defect.

The two results are:

1. **Black-box constructions.** If an ε-IND-CDP mechanism is built as a fully black-box construction
   from a one-way function — or from any primitive "that can be instantiated with a random object,"
   which the paper says includes ideal ciphers, collision-resistant hash functions, and trapdoor
   permutations — then there is an `(ε, negl)`-DP mechanism that is roughly as efficient and matches it
   on **every** utility measure to within a negligible additive term (Theorem 1). The proof is the
   Impagliazzo–Rudich / Gennaro–Gertner–Katz–Trevisan move: a random oracle is one-way with
   overwhelming probability, so the mechanism that simulates `O` internally inherits the CDP guarantee,
   and because a relativizing construction's guarantee survives against unbounded adversaries that make
   only polynomially many oracle queries, the resulting object is statistically DP.
2. **Arbitrary mechanisms, restricted queries and utilities.** For a mechanism with output in `R^n` for
   **constant** `n`, whose average `(p,v)`-error (the `v`-th moment of the `L_p` error) is bounded by a
   polynomial `err(k)`, any efficient ε-SIM-CDP mechanism can be converted into an efficient
   `(ε, negl)`-DP one with error `< err(k) + negl(k)` (Theorem 2). The conversion is startlingly cheap:
   `f̂_k` runs `f_k` and adds discretized uniform noise of radius `c(k) = ⌈4n√(negl₁(k))⌉_k`. The
   argument splits `R^n` into a region `Close_k` near the true answer and its complement `Far_k`,
   bounds the discrepancy on the former by box-indistinguishability and the mass on the latter by the
   polynomial error bound. The IND-CDP case follows because MPRV09's SIM∀∃-CDP is equivalent to
   IND-CDP and the construction of `f̂_k` never refers to `F_k`.

There is a third, framing observation that matters more for our programme than either theorem, and the
paper states it in one sentence before proving anything: **achievability was never the live question.**
"it is not hard to see that the best achievable utility cannot be improved as long as the utility is an
efficiently computable function of the database and the output of the mechanism. (This is an immediate
consequence of the SIM-CDP and SIM∀∃-CDP definitions, since otherwise the utility function itself serves
as a distinguisher.)" So the only thing computational DP could ever have bought in the client/server
model is **efficiency** — a polynomial-factor saving — and these two theorems are attempts to close off
that possibility in particular regimes. The same argument reappears verbatim as
[BCV16](separating-cdp-client-server.md) Remark 12 and as
[GIKKM23](towards-separating-cdp.md)'s reason for abandoning SIM-CDP.

The impossibility conjecture was later **falsified**: [BCV16](separating-cdp-client-server.md) gave an
infeasibility separation, and [GIKKM23](towards-separating-cdp.md) gave a genuine one. Both did it by
walking through the exclusions listed below — non-real-valued output, non-black-box cryptography.

## Claim Boundary

- **Quantified over:** Theorem 1 ranges over all fully black-box constructions of `ε`-IND-CDP
  mechanisms from a primitive that can be instantiated with a random object, and over **all** utility
  measures `U` (the paper explicitly notes `U` need not be efficiently computable here). Theorem 2
  ranges over all efficient `ε`-SIM-CDP mechanisms `{f_k : D → R^n}` with `n` constant and average
  `(p,v)`-error polynomially bounded, for arbitrary fixed `p > 0`, `v ≥ 1`; extended to IND-CDP.
- **Antecedent:** For Theorem 1 — the construction is *fully* black-box and hence relativizing, and the
  underlying primitive is instantiable by a random object. For Theorem 2 — output space `R^n` with `n`
  independent of the security parameter `k`; error measured by an `L_p`-norm moment; **a polynomial
  bound `err(k)` on that error, uniform over all databases and all `k`**. No cryptographic assumption
  is used in either theorem; these are unconditional statements about restricted classes.
- **Excluded cases (mandatory; verbatim from the paper's own *Limitations of our results*):**

  > "There are several types of queries to which our results do not apply. The most important are
  > queries with outputs that cannot naturally be thought of as tuples of real numbers. This includes,
  > e.g., queries that return classifiers (as in [9]), graphs, or synthetic databases."

  > "Our results also do not apply, in general, to queries that return output in Rn for "large" n (i.e.,
  > n that grows with the security parameter k)."

  > "Our results also hold only for restricted classes of utility functions. For example, they do not
  > apply when there is no polynomial bound on the error."

  Two further exclusions in the same paragraph: multiple-query analysis is only covered for a
  **constant** number of queries, or for arbitrarily many queries answered **independently** by a
  stateless server; and where answering many queries jointly is known to beat independent answering,
  "in such cases our results do not apply."
- **Does not establish:** that CDP is useless in the client/server model. It does not rule out
  separations for tasks whose output is a classifier, a graph, or a synthetic database; nor for outputs
  in `R^n` with `n` growing in `k`; nor for utilities with unbounded error; nor for mechanisms using
  cryptography non-black-box. It does not rule out **utility** gains in general — that follows
  separately and trivially from the definitions whenever utility is efficiently computable, and is not
  a theorem of this paper. It says nothing about the two-party or local models, where CDP was already
  known to help. And the paper's own closing sentence asks for exactly what later work found: "We leave
  it as an open question to find utility measures or query classes with respect to which computational
  differential privacy can help in the client/server setting."
- **Abstract vs theorem:** none found. The abstract is scoped correctly — "We show, for queries with
  output in Rn (for constant n) and with respect to a large class of utilities, that any computationally
  private mechanism can be converted to a statistically private mechanism". The overstatement is
  entirely downstream, in citation practice.

## Key Contributions

- The black-box barrier: no relativizing construction of a CDP mechanism from OWFs, ideal ciphers,
  CRHFs, or trapdoor permutations can beat statistical DP on efficiency or on any utility measure.
- The constant-dimension barrier for arbitrary mechanisms with polynomially bounded `L_p`-moment error,
  proved by adding negligible uniform noise.
- The observation that **the utility function is itself the distinguisher**, so simulation-based CDP can
  never improve best-achievable utility when utility is efficiently computable. This localizes the whole
  CDP-vs-DP question onto efficiency.
- A road map, read in hindsight: the exclusions are the specification of a separation, and both
  subsequent separations satisfy it.

## Key Definitions / Theorems

- **Definition 5 (IND-CDP).** `{f_k}` is `ε`-IND-CDP if for every non-uniform polynomial-time `A` and
  every sequence of ordered pairs of polynomial-size adjacent databases,
  `Pr[A(f_k(D_k)) = 1] ≤ e^{ε(k)} · Pr[A(f_k(D'_k)) = 1] + negl(k)`.
- **Definition 6 (SIM-CDP).** `{f_k}` is `ε`-SIM-CDP if there is an `(ε, negl)`-DP family `{F_k}`
  computationally indistinguishable from it. The paper notes it *weakens* MPRV09 here — MPRV09 require
  `F_k` to be `ε`-DP, this paper only `(ε, negl)`-DP — "which makes our impossibility results stronger."
- **Definition 7 (SIM∀∃-CDP).** Quantifiers reversed: the statistical mechanism may depend on the pair
  of databases. "Crucially for our purposes, this definition is known to be equivalent to IND-CDP."
- **Definition 9 (Average `(p,v)`-error).** `σ_{p,v}(q, D, f_k) = E[‖f_k(D) − q(D)‖_p^v]`, for `p > 0`,
  `v ≥ 1`. Polynomially bounded if `σ_{p,v} ≤ err(k)` for all `D`, `k`.
- **Theorem 1.** Black-box result, stated above, with the utility guarantee
  `|E[U(D, f_k^O(D))] − E[U(D, f'_k(D))]| ≤ negl(k)` for all `D` and **all** `U`.
- **Theorem 2.** Constant-dimension result, stated above.
- **Lemma 1.** For any box sequence `{B_k}` and any `D`,
  `|Pr[f_k(D) ∈ B_k] − Pr[F_k(D) ∈ B_k]| ≤ negl₁(k)` — "an immediate consequence of the SIM-CDP
  definition (recall the definition requires indistinguishability against non-uniform adversaries)."
  Box membership is efficiently testable, so it is a legal distinguisher. This is the whole engine.

## Connections

- Concept: [computational differential privacy](../concepts/computational-differential-privacy.md) —
  this page is the negative half of that concept's history.
- Defines against [MPRV09](computational-differential-privacy.md), whose SIM∀∃-CDP ⟺ IND-CDP
  equivalence Theorem 2 relies on to cover IND-CDP.
- Circumvented by [BCV16](separating-cdp-client-server.md), which makes non-black-box use of one-way
  functions via zaps and uses a utility function "far from the form in which the second result of
  [GKY11] applies." BCV16 §4 also **strengthens** the second result: for any metric with doubling
  dimension `O(log k)` satisfying their Property L, CDP cannot improve utility by more than a constant
  factor, and for `L_p` error this covers `d = O(log k)` rather than only constant `d` — at the cost of
  a constant-factor error blowup instead of a negligible additive one. The two results are incomparable.
- Circumvented by [GIKKM23](towards-separating-cdp.md), which takes the first exclusion literally: its
  task outputs a **circuit**, and it notes "obfuscation is not in the list of primitives ruled out by
  the barrier in [GKY11]."
- [HMST22](two-party-dp-complexity.md) states the bounded version correctly: GKY11 "showed that a wide
  range of CDP mechanisms can be converted into an (information-theoretic) DP mechanism."
- [DP20](sok-differential-privacies.md) also states it correctly: "for a large class of queries, it
  cannot provide significant benefits over classical DP in the typical client-server setting."
- [Dinur–Nissim PODS'03](dinur-nissim-revealing-information.md) is the other direction: there, bounding
  the adversary's compute *does* change the answer, by a `√` in the required perturbation.
- Concept: [computational vs statistical memorization](../concepts/computational-vs-statistical-memorization.md).
- Entities: [Jonathan Katz](../entities/jonathan-katz.md).

## Open Questions / Limitations

- The paper's own open question — find a query class or utility measure where CDP helps in the
  client/server model — was answered twice, and both answers went through the exclusion list.
- Theorem 2 handles utilities beyond the `(p,v)`-error family "as long as they satisfy a technical
  requirement that follows from our proof. Since we do not currently have any clean way to state this
  requirement, we do not discuss it further." The true scope of Theorem 2 is therefore not fully
  characterized by the paper.
- **For this programme:** the excluded region is exactly where machine learning lives. A released model
  is a classifier; a DP-SGD run answers many queries jointly with state; the error of a learned model is
  not a polynomially bounded `L_p` moment of a fixed query. GKY11 does not price the adversary of a
  released model, and it does not claim to.

## Quotes / Notable Passages

> "it is not hard to see that the best achievable utility cannot be improved as long as the utility is an
> efficiently computable function of the database and the output of the mechanism."

> "The interesting question is therefore to look for improvements in the efficiency"

> "Although we show negative results, they may point toward specific situations where computational
> differential privacy gives some advantage."

> "Note that the above proof holds not just for constructions based on one-way functions, but for any
> black-box construction from a primitive P that can be instantiated with a random object."
