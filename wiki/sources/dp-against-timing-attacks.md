---
title: A Framework for Differential Privacy Against Timing Attacks
type: source
date_ingested: 2026-08-20
authors: [Zachary Ratliff, Salil Vadhan]
venue: venue unconfirmed from PDF (arXiv:2409.05623v2 [cs.CR], 24 Nov 2024)
year: 2024
tags: [differential-privacy, verifiable-computation, impossibility-frameworks]
claim_quantifier: universal
antecedent: "An idealized cost model — RAM or Word RAM, every instruction one time step. Timing-stable programs must have O(n) runtime (Lemma 30). The delay-based constructions yield approximate rather than pure DP."
adversary_bound: unbounded (the adversary observes runtime in addition to output and is otherwise unrestricted); the compute being modelled is the MECHANISM's
---

## Summary

Formalizes **runtime as a leakage channel** and gives a compositional framework for closing it. This is the
one paper in the batch where computation is a first-class object in the definition — and the computation
being priced belongs to the **mechanism**, not to the adversary. **The adversary's own compute stays
unbounded throughout.** That contrast is the reason this page exists in a batch about the computational
axis: a paper can be entirely about compute and still leave the adversary's budget uncosted.

The problem is real. Implementations leak through runtime — Haeberlen–Pierce–Narayan showed user-defined
queries leaking record presence, and Jin–McMurtry–Rubinstein–Ohrimenko showed the runtime of discrete
Laplace and discrete Gaussian samplers revealing the magnitude of the sampled noise, which can be subtracted
back out. Prior mitigations were ad hoc or reached for constant-time execution, and the paper argues
constant-time is both costly and "overkill. It prevents all information leakage from the runtime, whereas
differential privacy only requires that executions over neighboring inputs are indistinguishable."

The definitional move is to reason about **programs** `P : X × E → Y × E` rather than functions, where `E`
is the set of execution environments, and to make the runtime differentially private **conditioned on the
output**. Definition 3 (`ε`-OC-timing privacy) asks that for adjacent `x, x'`, input-compatible
environments, and each shared output value `y`,
`Pr[T_P(x, env) ∈ S | out = y] ≤ e^ε · Pr[T_P(x', env') ∈ S | out = y]`. Conditioning on the output buys a
genuine design freedom: timing privacy and output privacy can be measured by **different** privacy measures.
"one generally compromises on utility to achieve output privacy, while one can instead compromise on
efficiency (longer runtimes) to achieve timing privacy."

The alternative, from Ben Dov–David–Naor–Tzalik, is joint output/timing privacy — plain DP applied to the
pair `(output, runtime)`. The paper renames it and relates the two: for pure DP the two formulations are
equivalent up to a constant factor in `ε`; more generally OC-timing privacy plus output privacy implies joint
privacy when both use the same measure (Lemma 36).

The framework then composes: chain **timing-stable** programs (close inputs give close runtime
distributions), append a single **timing-private delay program**, and the whole chain is timing-private.
Instantiations are given in the RAM and Word RAM models for randomized response, private sums, and private
means, including unbounded-DP versions whose accuracy matches their non-timing-private counterparts. A
proof-of-concept lives in OpenDP — and the paper is careful that this "is only meant to show how our
framework can be easily implemented on top of existing frameworks, not to provide actual guarantees of
privacy against an adversary who can measure physical time, which we leave as an important direction for
future work."

## Claim Boundary

- **Quantified over:** all adjacent dataset pairs, all pairs of input-compatible execution environments,
  all outputs in the common support, all measurable timing sets. The adversary is any observer of
  `(output, runtime)`.
- **Antecedent:** an idealized computational model in which each RAM instruction costs one time step.
  "On physical CPUs, this assumption does not hold and the varying time for different operations has been
  used as the basis for past timing attacks."
- **Excluded cases:** physical-time adversaries are explicitly out of scope for the implementation.
  Superlinear-time DP algorithms are out — Lemma 30 forces timing-stable programs to run in `O(n)`, so
  sorting-based mechanisms (approximate medians via the exponential mechanism) and pairwise-comparison
  mechanisms (DP Theil–Sen) are not covered. **Pure** timing privacy is largely out: the delay constructions
  "seem[] to inherently yield approximate DP (i.e. δ > 0)."
- **Does not establish:** any bound on the adversary's computational resources. The framework does not price
  what an attacker can compute from the timing channel; it bounds what the channel reveals, against any
  observer. It also does not establish guarantees on real hardware.
- **Abstract vs theorem:** none found. The abstract scopes the instantiations to "the RAM and Word RAM
  models of computation."

## Key Contributions

- `(ε, δ)`-differentially private **programs** (Definition 2): DP quantified over execution environments as
  well as datasets.
- `ε`-OC-timing privacy (Definition 3): runtime DP **conditioned on the output**, permitting different
  privacy measures for the two channels.
- The relation to joint output/timing privacy (Ben Dov et al., renamed): equivalence up to constants for
  pure DP; Lemma 36 in general.
- Timing stability, output-conditional timing stability, joint output/timing stability, and a chaining and
  composition calculus over them.
- Timing-private delay programs, and concrete RAM / Word RAM mechanisms — randomized response, unbounded
  noisy sum, unbounded mean — "often much more efficient than constant-time constructions."
- An OpenDP proof-of-concept tracking timing stability across transformations.

## Key Definitions / Theorems

- **Definition 2 ((ε, δ)-DP Programs).** For every adjacent `x, x'` and every pair of input-compatible
  `env, env' ∈ E` and every `S ⊆ Y`:
  `Pr[out(P(x, env)) ∈ S] ≤ e^ε · Pr[out(P(x', env')) ∈ S] + δ`.
- **Definition 3 (ε-OC-Timing Privacy).** Stated above; `T ⊆ R_{≥0}` are the time units, e.g. `T = N` when
  counting executed instructions.
- **Definition 4 (Joint Output/Timing Privacy [Ben Dov et al.]).** Plain DP on the joint variable
  `(out(P(x, env)), T_P(x, env))`.
- **Lemma 30.** Timing-stable programs must have `O(n)` runtime.
- **Lemma 36.** OC-timing privacy plus output privacy implies joint output/timing privacy when both are
  measured with the same privacy measure.

## Connections

- Concept: [computational differential privacy](../concepts/computational-differential-privacy.md) — the
  instructive contrast. CDP bounds the *adversary's* compute; this bounds what the *mechanism's* compute
  leaks. Both are "computational DP" in ordinary English and they are unrelated formally.
- Concept: [verifiable computation](../concepts/verifiable-computation.md).
- [DP20](sok-differential-privacies.md) has no dimension for side channels; this notion does not fit its
  seven axes.
- Same authorship lineage as [MPRV09](computational-differential-privacy.md) and
  [BCV16](separating-cdp-client-server.md) through Vadhan.
- [DP-SGD](deep-learning-differential-privacy.md) is the kind of implementation whose sampler runtimes
  motivated this work.
- Entities: [Salil Vadhan](../entities/salil-vadhan.md).

## Open Questions / Limitations

- Physical CPUs. The authors argue timing stability needs only an upper bound on the time difference one
  record can make, "which seems feasible to estimate in practice," but the guarantee is not proved there.
- Timing-private versions of the discrete Gaussian and exponential mechanisms; user-level and node-level
  privacy; superlinear-time mechanisms, blocked by Lemma 30.
- How far **pure** timing privacy is achievable. Ben-Dov et al. give limitations but do not rule out, e.g.,
  a RAM program that samples `O(1)` records and runs a constant-time DP computation on the subsample, which
  achieves perfect timing privacy on unbounded datasets.

## Quotes / Notable Passages

> "real-world implementations of differential privacy are often exposed to observable side channels that are
> not modeled in the definition of differential privacy."

> "Additionally, constant-time program execution is overkill."

> "one generally compromises on utility to achieve output privacy, while one can instead compromise on
> efficiency (longer runtimes) to achieve timing privacy."
