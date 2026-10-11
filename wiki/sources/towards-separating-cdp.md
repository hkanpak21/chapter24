---
title: Towards Separating Computational and Statistical Differential Privacy
type: source
date_ingested: 2026-08-20
authors: [Badih Ghazi, Rahul Ilango, Pritish Kamath, Ravi Kumar, Pasin Manurangsi]
venue: "FOCS 2023"
venue_evidence: "https://dblp.uni-trier.de/search?q=Towards%20Separating%20Computational%20and%20Statistical%20Differential%20Privacy; dblp: FOCS 2023, pp. 580-599, DOI 10.1109/FOCS57990.2023.00042 (confirms the venue-mining note's 3-vote FOCS lead)"
year: 2023
tags: [cryptography, indistinguishability-obfuscation, computational-indistinguishability, impossibility-frameworks, differential-privacy, low-degree-polynomial-framework]
claim_quantifier: conditional
antecedent: "Three simultaneous cryptographic assumptions: (i) NIWI — non-interactive witness indistinguishable proofs (Assumption 26); (ii) CRKHF — laconic collision-resistant keyless hash functions (Assumption 18); (iii) diO-for-pcS — differing-inputs obfuscation for public-coin samplers (Assumption 22)."
adversary_bound: PPT for the CDP mechanism; unbounded for the SDP lower bound; non-adaptive decision-tree (query) adversaries at the intermediate stage
cls_target: train data
cls_family: membership
cls_phase: post hoc
cls_access: white box
cls_write: read only
cls_frame: compute
cls_party: attacker
cls_unit: time
cls_tightness: poly
cls_baseline: stated
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: queries
cls_assessed: explicit
cls_evidence: "first we show that a mechanism is \"private\" against a certain class of decision tree adversaries, and then we use cryptographic constructions to \"lift\" this into privacy against computationally bounded adversaries"
cls_evidence_src: §I
cls_reason: "party=attacker for the CDP indistinguishability game (Def 9), not auditor, since the distinguisher's role is to break confidentiality of D vs D' rather than verify compliance. second_notion=queries for the intermediate non-adaptive decision-tree adversary class used in the two-stage lift (Rule 4b: one party, two incomparable notions, since the paper's own point is lifting query-bounded to PPT). target=train data and family=membership since CDP/SDP are neighbor-dataset (D vs D') indistinguishability games, the canonical membership-privacy shape. phase=post hoc since the adversary examines the mechanism's released output (a circuit plus NIWI proof) with no further training."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The strongest single-curator CDP-vs-SDP separation available, and the only one whose lower bound holds
against **computationally unbounded** mechanisms. Under three cryptographic assumptions, there is a task
with an `ε = O(1)` CDP mechanism achieving `1 − o(1)` utility, while no `(ε, δ)`-SDP mechanism — including
inefficient ones — achieves constant utility with constant `ε` and `δ = 1/n^{27}`. This answers Vadhan's
Open Problem 10.6 positively and Open Problem 10.8 (the multi-pair dense model extension of
[MPRV09](computational-differential-privacy.md)) negatively.

The task is engineered to walk through both barriers the paper identifies in the prior literature.
Barrier one is **high-dimensionality**: [GKY11](limits-cdp-client-server.md) rules out low-dimensional
real-valued outputs, so the task's output must be high-dimensional. Barrier two is **exotic
cryptography**: GKY11 also rules out black-box constructions from a list of primitives. The paper's
conceptual move is to make the output a **circuit**, which is high-dimensional and which "lends itself to
a powerful class of cryptographic objects: circuit obfuscators," noting explicitly that "obfuscation is
not in the list of primitives ruled out by the barrier in [GKY11]."

The base problem is `LDS_τ` — *low diameter set*: given a dataset `D ∈ {0,1}^n`, output a circuit `C`
that outputs 1 on `D` and 0 on every point at Hamming distance more than `τ` from `D`. No SDP mechanism
solves this for `τ ≤ n^{0.9}` (Lemma 3), by a straightforward blatant-non-privacy argument. Crucially the
SDP lower bound is **non-constructive**: "our lower bounds are non-constructive, and do not yield an
efficient adversary (which would imply a similar lower bound against CDP mechanisms)." That asymmetry is
the whole opening.

### The two-stage argument: restricted class, then lift by cryptography

This deserves its own note, because it is the structural template our programme keeps looking for.

The paper does not prove CDP directly. It proves privacy against a **restricted, combinatorially defined
adversary class first**, and then uses cryptography to lift that restricted-class guarantee into a
guarantee against arbitrary polynomial-time adversaries. In their words: "first we show that a mechanism
is 'private' against a certain class of decision tree adversaries, and then we use cryptographic
constructions to 'lift' this into privacy against computationally bounded adversaries. We believe this
approach could be useful to devise further tasks separating CDP from SDP."

The lift has two rungs, each with its own primitive:

1. **diO reduces computational adversaries to adaptive query adversaries.** Differing-inputs obfuscation
   guarantees that if an efficient adversary distinguishes obfuscations of `C₁` and `C₂`, an efficient
   adversary can *find* an input where they differ. So a white-box distinguisher is convertible into a
   black-box querier: privacy against decision trees suffices.
2. **Keyless collision-resistant hashing reduces adaptive query adversaries to non-adaptive ones.** The
   mechanism they can actually analyze — randomized response — is private only against **non-adaptive**
   decision trees, whose queries are fixed a priori, and "a polynomial-time algorithm with even black-box
   access to a function seems to be an inherently adaptive adversary." The fix is to restrict the task to
   datasets in a set `R` of strings hashing to a fixed value. Then the circuit reveals information only
   at points of `R`; laconic collision resistance means any efficient adversary can produce only
   polynomially many elements of `R` beyond its advice; so the set of *informative* queries the adversary
   can reach is effectively fixed in advance. "diO allows us to reduce computational adversaries to
   adaptive query adversaries and collision-resistant keyless hash functions allows us to reduce adaptive
   query adversaries to non-adaptive query adversaries." The paper notes this is, to its knowledge, the
   first joint use of keyless CRHFs and an obfuscation assumption.

A third primitive is needed for a separate reason. The utility function must be polynomial-time
computable — otherwise the notion of a "task" degenerates — but checking that a circuit outputs 0 on all
`τ`-far points takes `2^{n^{Ω(1)}}` time. The mechanism therefore also outputs a **witness** certifying
this, and to keep the witness from leaking, it outputs a **NIWI proof** of the witness's validity instead.
The final task is `VLDS_{τ,R,V}`, the verifiable low diameter set problem.

The authors devote §II-E to the plausibility of all three assumptions and are candid about the weakest
link: iO is now standard and gives NIWI; CRKHFs have candidates and hold in the ROM, and refuting them would give the first
non-contrived separation between the standard and Random Oracle models — GIKKM make this point by quoting
Bitansky, Kalai, and Paneth, that an attack on the multi-collision resistance of a keyless cryptographic
hash function "would constitute a strong and natural separation between the hash and random oracles"; but
diO "is controversial," with several papers casting doubt, though the specific assumption used is weaker
than public-coin diO and is needed only for one simple circuit family.

## Claim Boundary

- **Quantified over:** the SDP lower bound quantifies over **all** mechanisms, including
  computationally unbounded ones, at constant `ε_SDP, α > 0` and `δ_SDP = 1/n^{27}`. The CDP upper bound
  is a single existential construction, for any constant `ε_CDP > 0`.
- **Antecedent:** all three assumptions simultaneously — Assumption 26 (NIWI), Assumption 18 (laconic
  collision-resistant keyless hash functions, at a compression rate different from Bitansky–Kalai–Paneth's),
  and Assumption 22 (differing-inputs obfuscation for public-coin samplers, weaker than public-coin diO).
  The SDP lower bound additionally needs the set `R` to have density `≈ 1/n^{−o(log n)}` and `R_n` to be
  efficiently recognizable. `τ_n ≤ n^{0.9}`.
- **Excluded cases:** the CDP mechanism is **not** CDP against quasi-polynomial adversaries, and the
  authors say why: the hash length is only `o(log² λ)`, so guess-and-check breaks Assumption 18 in time
  `λ^{O(log λ)}`. The utility function is **non-uniform** (through the choice of `υ_n`). The task is
  admittedly contrived — the paper's own framing is "our task is specifically constructed for the purpose
  of separating CDP and SDP." SIM-CDP is out of scope by construction: "It should be noted that SIM-CDP
  cannot be used for the separation we are looking for," for exactly the utility-as-distinguisher reason
  given in [GKY11](limits-cdp-client-server.md) and [BCV16](separating-cdp-client-server.md).
- **Does not establish:** a separation for any natural task. It does not establish that CDP beats SDP on
  linear queries, counting queries, or any standard statistical problem; the paper's stated hope is that
  its existence "opens up a possibility that such a separation even holds for some 'natural' tasks," and
  it notes that packing lower bounds "do not necessarily rule out CDP mechanisms" and should be
  re-examined. It does not establish a separation against sub-exponential or quasi-polynomial adversaries.
  It does not establish anything from standard assumptions.
- **Abstract vs theorem:** none found. The abstract names all three assumptions, calls them "strong but
  plausible," and states the parameters exactly.

## Key Contributions

- The first task with a CDP mechanism and **no** SDP mechanism, resolving Vadhan Open Problem 10.6 under
  the stated assumptions.
- A negative answer to the multi-pair dense-model-theorem question (Vadhan Open Problem 10.8) left by
  [MPRV09](computational-differential-privacy.md).
- The **restricted-class-then-lift** proof technique: prove privacy against non-adaptive decision trees,
  lift to adaptive queries via keyless collision resistance, lift to polynomial time via diO. Offered
  explicitly as a reusable method.
- Naming the two barriers to a client/server separation — high-dimensionality and exotic cryptography —
  and the observation that circuit-valued outputs clear both.
- Identification of circuit-output tasks as a class that evades [GKY11](limits-cdp-client-server.md).

## Key Definitions / Theorems

- **Definition 7 (SDP).** `M(D) ≈_{ε,δ} M(D')` for every adjacent pair; extended to ensembles
  coordinatewise.
- **Definition 9 (CDP).** `{M_n(D_n)} ≈^c_{ε_n} {M_n(D'_n)}` for every sequence of adjacent pairs;
  this is IND-CDP, and the paper drops the qualifier because it is the only notion it uses. `δ` is
  always assumed negligible for CDP; `(ε, δ)` are both tracked for SDP, and the SDP lower bounds work for
  non-negligible `δ`, which strengthens the result.
- **Definition 10 (SIM-CDP [MPRV09]).** Reproduced and then set aside.
- **`LDS_τ`, `LDS_{τ,R}`, `NBP` (nearby point), `VLDS_{τ,R,V}` (Definition 14).** The problem family.
  `LDS_{τ,R}`'s utility "completely ignores all points outside of R."
- **Lemma 3.** For `0 < τ ≤ n^{0.9}`, constant `ε, α > 0`, `δ = 1/n^c` with `c > 1`, there is no
  `(ε, δ)`-SDP mechanism for `LDS_τ` that is `α`-useful. Follows from blatant non-privacy.
- **Theorem 5 (Main).** Under Assumptions 18, 22, 26: for any constant `ε_CDP > 0` there is an ensemble
  of polynomial-time computable utility functions with a `ε_CDP`-CDP mechanism that is `(1 − o_n(1))`-useful,
  while for any constants `ε_SDP, α > 0` and `δ_SDP = 1/n^{27}` no `(ε_SDP, δ_SDP)`-SDP mechanism is
  `α`-useful.
- **Fact 11.** Composition and post-processing for both `≈_{ε,δ}` and `≈^c_ε`; note that computational
  post-processing is closed only under **PPT** `A`, not all functions — the same structural caveat that
  [CIM19](capacity-bounded-dp.md) makes explicit for function classes.

## Connections

- Concept: [computational differential privacy](../concepts/computational-differential-privacy.md).
- Concept: [indistinguishability obfuscation](../concepts/indistinguishability-obfuscation.md).
- Builds on and inverts [GKY11](limits-cdp-client-server.md); the circuit-valued output is the first item
  on GKY11's own exclusion list.
- Strengthens [BCV16](separating-cdp-client-server.md) from infeasibility to genuine impossibility, at the
  cost of much stronger assumptions.
- The concluding section points at [HMST22](two-party-dp-complexity.md) as the model for the next
  question — what assumptions are *necessary* for a central-model separation — noting that key agreement
  is known to be necessary and sufficient in the two-party inner-product case.
- Concept: [statistical query model](../concepts/statistical-query-model.md) — the decision-tree
  intermediate class is a query-complexity restriction of the same family, though the paper does not use
  SQ language.
- Concept: [low-degree polynomial framework](../concepts/low-degree-polynomial-framework.md) — for the
  general pattern of proving a bound against a restricted class first.
- Entities: [Salil Vadhan](../entities/salil-vadhan.md) (whose survey supplies both open problems).

## Open Questions / Limitations

- Remove, relax, or replace the three assumptions; or, conversely, determine which cryptographic
  assumptions are **necessary** for a central-model CDP/SDP separation.
- Find a **natural** task. The authors call this "perhaps the most intriguing next direction."
- **Strengthen the adversary.** Their mechanism is not CDP against quasi-polynomial adversaries; they
  believe "there is no inherent barrier in proving a separation with CDP that holds even against, e.g.,
  sub-exponential time adversaries." This is a request for a finer-grained computational axis in privacy,
  from inside the CDP literature.
- Make the task uniform.
- Re-examine existing SDP lower bound techniques — especially packing bounds, which "when the packing
  lower bound requires the use of super-polynomially many datasets, the corresponding adversary does not
  necessarily run in polynomial time" — to see which of them also rule out CDP.

## Quotes / Notable Passages

> "first we show that a mechanism is "private" against a certain class of decision tree adversaries, and
> then we use cryptographic constructions to "lift" this into privacy against computationally bounded
> adversaries."

> "Crucially, our lower bounds are non-constructive, and do not yield an efficient adversary"

> "obfuscation is not in the list of primitives ruled out by the barrier in [GKY11]."

> "Indeed, our CDP mechanism does not remain CDP against quasi-polynomial adversary."

> "It should be noted that SIM-CDP cannot be used for the separation we are looking for."
