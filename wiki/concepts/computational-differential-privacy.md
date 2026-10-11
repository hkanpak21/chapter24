---
title: Computational Differential Privacy
type: concept
tags: [cryptography, computational-indistinguishability, differential-privacy, one-way-functions, impossibility-frameworks]
---

## Definition

Differential privacy with the distinguisher restricted to probabilistic polynomial time. Two definitions,
from [Mironov–Pandey–Reingold–Vadhan](../sources/computational-differential-privacy.md):

- **IND-CDP.** `{f_κ}` is `ε_κ`-IND-CDP if for every non-uniform ppt `A`, every polynomial `p`, all adjacent
  `D, D'` of size `≤ p(κ)`, and every advice string of size `≤ p(κ)`:
  `Pr[A(f_κ(D)) = 1] ≤ e^{ε_κ} · Pr[A(f_κ(D')) = 1] + negl(κ)`.
- **SIM-CDP.** `{f_κ}` is `ε_κ`-SIM-CDP if there exists an ensemble `{F_κ}` of `ε_κ`-DP mechanisms —
  **not required to be efficiently computable** — such that `f_κ(D)` and `F_κ(D)` are computationally
  indistinguishable for every `D`.

A third notion, **SIM∀∃-CDP**, weakens SIM-CDP by letting the statistical simulator depend on the pair of
adjacent databases. A fourth, **SIM⁺-CDP**, is the ideal/real-paradigm version for interactive protocols,
with a possibly inefficient simulator.

The pure `δ = 0` computational analogue is vacuous: the indicator of a singleton output is already a legal
ppt distinguisher, so it collapses to statistical `ε`-DP. Every CDP definition therefore carries a negligible
additive slack.

## Intuition

DP's adversary has unlimited time. That is a deliberate and costly choice: it rules out mechanisms that are
obviously safe in practice, such as one that replaces true randomness with a pseudorandom generator, or one
implemented by secure multiparty computation. CDP is the minimal repair — keep the definition, bound the
distinguisher.

The repair pays off spectacularly in the **distributed** setting and barely at all, as far as anyone can
construct, in the **single-curator** setting. That asymmetry is the whole subject.

## Properties / Theorems

**Relations among the notions.**

- SIM-CDP ⟹ SIM∀∃-CDP ⟹ IND-CDP ([MPRV09](../sources/computational-differential-privacy.md) Theorem 1).
- SIM∀∃-CDP ⟺ IND-CDP for `ε_κ ∈ O(log κ)` (Theorem 3), proved by extending the Dense Model Theorem of
  Reingold–Trevisan–Tulsiani–Vadhan with a new symmetry claim.
- **IND-CDP ⟹ SIM-CDP is open.** It was still open when
  [GIKKM23](../sources/towards-separating-cdp.md) wrote. Do not state a general SIM/IND equivalence.
- SIM⁺-CDP ⟹ SIM-CDP, and the converse fails (Theorem 4).

**The utility-as-distinguisher observation.** If the utility function is efficiently computable, no
SIM-CDP-style mechanism can beat statistical DP on *best achievable utility*, because the utility function
itself becomes the distinguisher. Stated in
[GKY11 §1.1](../sources/limits-cdp-client-server.md), as Remark 12 of
[BCV16](../sources/separating-cdp-client-server.md), and as the reason
[GIKKM23](../sources/towards-separating-cdp.md) discards SIM-CDP. Consequence: the live question was always
*efficiency*, and any true impossibility separation must go through IND-CDP.

**Where CDP definitely helps: the distributed setting.** Given oblivious transfer, parties can emulate a
central mechanism by secure computation, so the two-party inner product achieves `O_ε(1)` additive error
against the `Ω_ε(√n)` statistical bound. The cryptographic price of that gain is now largely known:
key agreement is necessary at any non-trivial accuracy
([HMST22](../sources/two-party-dp-complexity.md)), and oblivious transfer is necessary at accuracy
`O(n^{1/6})` ([HMSTY25](../sources/cdp-inner-product-implies-ot.md)). For CDP against an external observer,
key agreement is necessary **and** sufficient.

**Where it was thought not to help: the single curator.** [GKY11](../sources/limits-cdp-client-server.md)
proved two conditional negative results — one for fully black-box constructions from primitives instantiable
by a random object, one for outputs in `R^n` with **constant** `n` under polynomially bounded `L_p`-moment
error. **Read that page's Claim Boundary before citing it.** The authors explicitly exclude queries returning
classifiers, graphs, or synthetic databases; `R^n` with `n` growing in the security parameter; and utilities
with no polynomial error bound. [BCV16 §4](../sources/separating-cdp-client-server.md) widens the second
result to metrics of doubling dimension `O(log k)`, hence `L_p` on `R^d` with `d = O(log k)`, at a
constant-factor rather than negligible cost — incomparable, not strictly stronger.

**The negative result was falsified, twice.**

- [BCV16](../sources/separating-cdp-client-server.md): under sub-exponential OWFs and extractable zaps,
  a client-server task efficiently solvable with CDP and **infeasible** — not impossible — with statistical
  DP. Infeasibility is inherent for a SIM-CDP construction, by the utility-as-distinguisher argument.
- [GIKKM23](../sources/towards-separating-cdp.md): under NIWI **and** laconic collision-resistant keyless
  hash functions **and** differing-inputs obfuscation for public-coin samplers, a task with an `O(1)`-CDP
  mechanism at `1 − o(1)` utility and **no** SDP mechanism at all, including unbounded ones. Both walk
  through GKY11's own exclusion list: circuit-valued output, non-black-box cryptography.

**A reusable proof template.** GIKKM23 establish privacy against **non-adaptive decision-tree adversaries**
first, then lift twice: keyless collision resistance converts adaptive query adversaries into effectively
non-adaptive ones, and differing-inputs obfuscation converts polynomial-time adversaries into query
adversaries. Restricted class first, cryptography second. See
[low-degree polynomial framework](low-degree-polynomial-framework.md) for the same shape used on algorithms
rather than adversaries.

## Where It Appears

- [MPRV09 — Computational Differential Privacy](../sources/computational-differential-privacy.md) (source)
- [GKY11 — Limits of CDP in the Client/Server Setting](../sources/limits-cdp-client-server.md)
- [BCV16 — Separating CDP and SDP in the Client-Server Model](../sources/separating-cdp-client-server.md)
- [GIKKM23 — Towards Separating CDP and SDP](../sources/towards-separating-cdp.md)
- [HMST22 — On the Complexity of Two-Party DP](../sources/two-party-dp-complexity.md)
- [HMSTY25 — CDP Inner-Product Protocols Imply OT](../sources/cdp-inner-product-implies-ot.md)
- [DP20 — SoK: Differential Privacies](../sources/sok-differential-privacies.md), dimension **C**

## Related Concepts

- [Computational indistinguishability](computational-indistinguishability.md)
- [Capacity-bounded privacy](capacity-bounded-privacy.md) — the other way to weaken the adversary: by
  function class rather than by runtime
- [Computational vs statistical memorization](computational-vs-statistical-memorization.md)
- [Local differential privacy](local-differential-privacy.md)
- [One-way functions](one-way-functions.md), [indistinguishability obfuscation](indistinguishability-obfuscation.md)
- [Adversary knowledge taxonomy](adversary-knowledge-taxonomy.md) — the axis the attack-taxonomy literature
  actually uses instead

## Open Questions

- **IND-CDP ⟹ SIM-CDP?** Open since 2009. A separation would also give the first task achievable under
  IND-CDP and impossible under DP, which is what [BCV16](../sources/separating-cdp-client-server.md) asks
  for.
- **A natural separating task.** Both existing separations use contrived, cryptographic utility functions,
  and both papers say so.
- **Weaker assumptions**, or conversely: which cryptographic assumptions are *necessary* for a central-model
  separation? [HMST22](../sources/two-party-dp-complexity.md) answered the analogous question in the
  two-party model.
- **Finer resolution on the axis.** The axis has one bit: PPT or unbounded.
  [GIKKM23](../sources/towards-separating-cdp.md) note from inside that their mechanism is not CDP against
  quasi-polynomial adversaries and that they see "no inherent barrier in proving a separation with CDP that
  holds even against, e.g., sub-exponential time adversaries." A graded computational axis for privacy does
  not exist. [DP20](../sources/sok-differential-privacies.md) confirms the census.
- **Machine learning is in the excluded region.** A released model is a classifier — the first item on
  GKY11's exclusion list. No result in this literature prices the adversary of a released model. The nearest
  obstacle from the other direction is
  [Xiao–Suh–Devadas CCS'24](../sources/xiao-formal-privacy-proof-data-encoding.md): no non-trivial
  property-preserving transformation that keeps encoded samples learnable gets worst-case cryptographic
  security for free. Read that page's provenance note before leaning on it.
