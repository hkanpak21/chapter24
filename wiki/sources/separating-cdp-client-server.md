---
title: Separating Computational and Statistical Differential Privacy in the Client-Server Model
type: source
date_ingested: 2026-08-20
authors: [Mark Bun, Yi-Hsiu Chen, Salil Vadhan]
venue: venue unconfirmed from PDF (dated August 26, 2016; cited elsewhere in this corpus as TCC 2016-B)
year: 2016
tags: [cryptography, one-way-functions, computational-indistinguishability, impossibility-frameworks, differential-privacy]
claim_quantifier: conditional
antecedent: "Sub-exponentially secure one-way functions, and 'exponentially extractable' 2-message witness indistinguishable proofs (zaps) for NP. Complexity leveraging requires a gap: sub-exponential time must break the zap but not forge a signature."
adversary_bound: PPT for the CDP mechanism; sub-exponential time for the extractor in the lower-bound reduction; unbounded for the inefficient DP mechanism that also solves the task
---

## Summary

The first single-curator separation, and it is an **infeasibility** result rather than an impossibility
one. The task admits an efficient CDP mechanism, admits an inefficient statistically DP mechanism with
matching parameters, and admits no efficient statistically DP mechanism. The gap is in computation, not
in achievability.

That structure is forced, and the paper says so twice. The CDP mechanism satisfies the
simulation-based notion (they call it PURE-SIM-CDP), and by definition a SIM-CDP mechanism comes with a
possibly-inefficient DP mechanism indistinguishable from it; since the utility function is efficiently
computable by requirement, that DP mechanism inherits the utility. Otherwise "the utility function
`u_k(D_k, ·)` would itself serve as a distinguisher" (Remark 12) — the same observation
[GKY11](limits-cdp-client-server.md) makes in §1.1 and [GIKKM23](towards-separating-cdp.md) repeats as its
reason for using IND-CDP only. Getting genuine impossibility therefore requires a task achievable under
IND-CDP but not SIM-CDP, which would also separate those two notions — an open problem inherited from
[MPRV09](computational-differential-privacy.md).

The construction. Take an existentially unforgeable digital signature scheme and a zap (2-message witness
indistinguishable proof) for NP. A dataset is `n` message-signature pairs. A mechanism is useful if it
outputs a zap proof of the statement *there exists a message-signature pair `(m, σ)` with
`Ver(m, σ) = 1`*.

- The **inefficient DP mechanism** `M^unb` checks privately that the dataset contains many valid pairs,
  then uses unbounded computation to forge a *canonical* pair and proves using that. Because the
  canonical witness does not depend on the data at all, the whole thing is DP.
- The **CDP mechanism** `M^CDP` does the same check but proves using an arbitrary pair `(m_i, σ_i)` drawn
  from the dataset. Witness indistinguishability means a bounded observer cannot tell that proof from the
  canonical one. So `M^CDP` is SIM-CDP, with `M^unb` as its simulator.
- The **lower bound.** Suppose an efficient DP mechanism `M` solved the task. A sub-exponential-time
  adversary `A` breaks the zap and extracts a witness `(m, σ)` from the proof. Since `M` is DP, the
  extracted pair cannot be a row of `D` — so `A ∘ M` is a forger, contradicting sub-exponential
  unforgeability. Complexity leveraging is what makes this work, and it is why a *gap* between the two
  primitives is assumed rather than plain security.

**The authors' own assessment of their task is worth recording, because it is the honest limitation and it
was quoted back at them by later work:** "our utility function is cryptographic and unnatural from a data
analysis point view." They ask directly "whether a separation can be obtained from a more natural task
(such as answering a polynomial number of counting queries with differential privacy)."

Two circumventions of [GKY11](limits-cdp-client-server.md) are named: non-black-box use of one-way
functions through zap machinery, and a utility function far outside the `L_p`-moment form. §4 then goes
back and **strengthens** GKY11's second result in a different direction — see below.

## Claim Boundary

- **Quantified over:** part 3 of the main theorem quantifies over **every efficient** `(ε_k, δ = 1/n²)`-DP
  mechanism, for `ε_k ≤ O(log k)`, `α_k = 1/poly(k)`, `n = poly(k)`, and asserts the existence of a bad
  dataset for each. Parts 1 and 2 are existential constructions.
- **Antecedent:** sub-exponentially secure one-way functions (which, by their Theorem 10, yield a
  `c`-strongly unforgeable signature scheme for some constant `c ∈ (0,1)`) **and** extractable zaps for NP.
  The complexity-leveraging gap is part of the assumption, not a consequence.
- **Excluded cases:** the separation says nothing about tasks whose utility is not of this cryptographic
  form. It is limited to the SIM-CDP notion on the positive side, and therefore structurally cannot yield
  impossibility. It does not cover `δ` outside the stated regime, nor `ε_k` growing faster than `O(log k)`.
- **Does not establish:** that CDP is impossible to match with SDP. The task **is** solvable with
  statistical DP, inefficiently and with matching parameters — this is part 2 of the theorem, stated
  deliberately. A reader who takes this paper as showing SDP cannot do the task has inverted it. It also
  does not separate IND-CDP from SIM-CDP, which the authors flag as the open problem a genuine
  impossibility would require.
- **Abstract vs theorem:** none found. The abstract says "can be efficiently performed with CDP, but is
  infeasible to perform with information-theoretic differential privacy" — *infeasible*, chosen
  carefully.

## Key Contributions

- The first client/server task efficiently solvable with CDP and infeasible with statistical DP, under
  sub-exponential OWFs plus extractable zaps.
- The explanation of **why infeasibility is inherent for any SIM-CDP-based separation**: the utility
  function is a distinguisher (Remark 12).
- Two named routes past [GKY11](limits-cdp-client-server.md): non-black-box cryptography, and a utility
  function outside the `L_p`-error family.
- §4 strengthens GKY11's dimension barrier along a different axis. For any discrete metric space
  `(R_k, g)` satisfying **Property L** — doubling dimension `O(log k)`, uniformity, efficiently checkable
  ball membership, efficiently samplable balls — an efficient `ε_k`-IND-CDP mechanism that is
  `α_k`-accurate can be converted into an efficient `(ε, negl(k))`-DP mechanism that is `O(α_k)`-accurate
  (Theorem 27, Corollary 28 for `L_p` on `R^d` with `d = O(log k)`).
- The paper is explicit that this is **incomparable** to GKY11, not stronger: "We incur a constant-factor
  blowup in error, rather than a negligible additive increase as in [GKY11]. However, in the case that
  utility is measured by an `L_p` norm, our result applies to output spaces of dimension that grow
  logarithmically in the security parameter `k`, whereas the result of [GKY11] only applies to outputs of
  constant dimension." It also handles IND-CDP directly rather than via the MPRV09 reduction.

## Key Definitions / Theorems

- **Theorem 10.** Sub-exponentially secure OWFs ⟹ a `c`-strongly unforgeable signature scheme for some
  constant `c ∈ (0,1)`.
- **Theorem 11 (Main).** Under sub-exponential OWFs and extractable zaps for NP, there is an efficiently
  computable `u_k` with: (1) for any `ε_k, β_k > 0`, a polynomial-time `ε_k`-PURE-SIM-CDP mechanism and an
  inefficient `ε_k`-PURE-DP mechanism both achieving utility `≥ 1 − β_k` for `n ≥ p(k, 1/ε_k, log(1/β_k))`;
  (2) for `ε_k ≤ O(log k)`, `α_k = 1/poly(k)`, `n = poly(k)`, every efficient `(ε_k, 1/n²)`-DP mechanism
  has a dataset on which its utility is `≤ α_k`.
- **Remark 12.** The inherence of infeasibility, quoted above.
- **Definition 25 (Property L).** Doubling dimension `O(log k)`; uniform ball sizes; `poly(k)`-time ball
  membership; `poly(k)`-time uniform sampling from balls.
- **Definition 26 (`α`-accuracy).** `Pr[g(q_k(D), M_k(D)) ≤ α_k] ≥ 1 − negl(k)`.
- **Corollary 28.** `L_p` case: `d = O(log k)` suffices, using that `R^d` under `L_p` has doubling
  dimension `O(d)`, plus a projection step to handle the non-uniformity at the boundary of the discretized
  range.

## Connections

- Concept: [computational differential privacy](../concepts/computational-differential-privacy.md).
- Concept: [one-way functions](../concepts/one-way-functions.md).
- Extends and partially strengthens [GKY11](limits-cdp-client-server.md); see §4. Note carefully: this
  paper *widens* the GKY11 barrier from constant to logarithmic dimension for `L_p` error, so the excluded
  region named on the GKY11 page shrinks slightly — but the categorical exclusions (classifiers, graphs,
  synthetic databases, unbounded error) are untouched by it.
- Superseded on the impossibility question by [GIKKM23](towards-separating-cdp.md), which achieves a
  lower bound against unbounded mechanisms by abandoning SIM-CDP for IND-CDP and paying with three much
  stronger assumptions.
- Uses the notions of [MPRV09](computational-differential-privacy.md).
- [HMST22](two-party-dp-complexity.md) describes this result accurately as holding "under (unnatural)
  cryptographic assumptions" and yielding infeasibility "(not impossibility)."
- Entities: [Salil Vadhan](../entities/salil-vadhan.md).

## Open Questions / Limitations

- **A natural task.** The authors ask for one explicitly, naming "answering a polynomial number of
  counting queries with differential privacy" as the target.
- **Separate IND-CDP from SIM-CDP.** Needed for any true impossibility separation, and interesting on its
  own.
- Reduce the assumptions; extractable zaps and complexity leveraging are heavy.

## Quotes / Notable Passages

> "Indeed, our utility function is cryptographic and unnatural from a data analysis point view."

> "Note that the theorem provides a task where achieving differential privacy is infeasible – not
> impossible."

> "It remains an intriguing open problem to exhibit a task that can be achieved with a weaker
> indistinguishably-based notion of CDP ("IND-CDP") but is impossible to achieve (even inefficiently) with
> differential privacy."

> "all known lower bounds against computationally efficient differentially private algorithms [...] in the
> client-server model are proved by exhibiting computationally efficient adversaries. Thus, these lower
> bounds rule out the existence of CDP mechanisms just as well as they rule out differentially private
> ones."
