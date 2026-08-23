---
title: Capacity Bounded Differential Privacy
type: source
date_ingested: 2026-08-20
authors: [Kamalika Chaudhuri, Jacob Imola, Ashwin Machanavajjhala]
venue: venue unconfirmed from PDF (arXiv:1907.02159v1 [cs.LG], 3 Jul 2019; the PDF footer reads "Preprint. Under review." — cited by DM22 in this corpus as NeurIPS 2019)
year: 2019
tags: [adversarial-ml, learning-theory, differential-privacy, low-degree-polynomial-framework, computational-vs-it-robustness]
claim_quantifier: existential
antecedent: "For post-processing: a composition-closure condition on the function classes (i ∘ g ∈ H for all g ∈ G, i ∈ I). For parallel/sequential composition: H1, H2 convex and translation invariant (and containing a constant function, for sequential). For generalization: H must contain {h_x : x ∈ X} where h_x(q) = q(x)."
adversary_bound: function class (the attack algorithm is drawn from a restricted class H); NOT runtime
cls_target: train data
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: attacker
cls_unit: algo class
cls_tightness: class
cls_baseline: stated
cls_second: none
cls_assessed: explicit
cls_evidence: "bounded not in computational power, but in terms of the function class from which their attack algorithm is drawn"
cls_evidence_src: abstract
cls_reason: "family=none and phase=n/a follow the general-DP-definition pattern also used for computational-differential-privacy in this corpus, since the paper names no specific attack family or ML lifecycle stage; unit=algo class and tightness=class follow directly from the H-restricted divergence definition."
cls_prov: S
cls_date: 2026-08-22
---

## Summary

The nearest thing in the privacy literature to a **function-class-bounded** adversary, and the paper that
matters most in this corpus for the shape of the programme's Phase-2 idea. The adversary is not
computationally bounded in the usual sense; it is bounded by the class of functions its attack can be
drawn from. From the abstract: *"the adversary that distinguishes the output distributions is assumed to
be capacity-bounded – i.e. bounded not in computational power, but in terms of the function class from
which their attack algorithm is drawn."*

The mechanism is elegant. An `f`-divergence has a dual variational form as a supremum over all functions
`h` of `E_P[h] − E_Q[f*(h)]`. Replace the unrestricted supremum by a supremum over a class `H` and you get
an `H`-restricted `f`-divergence. Rényi divergences are not `f`-divergences, but they go through the
corresponding `α`-divergence by a closed-form identity, which yields an `H`-restricted Rényi divergence.
Privacy is then defined by bounding a restricted divergence between the mechanism's output distributions on
adjacent datasets. When `H` is the class of all functions and `Γ` is Rényi, the definition collapses to
Rényi DP; capacity-bounded DP is a strict generalization of RDP and hence a relaxation of `ε`-DP.

The motivating stories are worth keeping. First, "scenarios where the attacker is machine learnt and lies
in some known space of functions (e.g., all linear functions, linear classifiers, multi-layer deep networks
with given structure, etc.)". Second, a **data-usage contract**: if a user is contractually restricted to
computing functions from a given class on the released output, then a capacity-bounded guarantee says no
contract-obeying user can violate privacy. The paper also states, correctly and with a citation to
[GKY11](limits-cdp-client-server.md), the reason for reaching for function classes rather than runtime:
"Unlike computational DP, where computationally bounded adversaries do not meaningfully relax the privacy
definition in the typical centralized differential privacy model [11], we believe that capacity bounded
adversaries will relax the definition to permit more useful algorithms". Note that this is the folk version
of GKY11 in one clause — see the boundary section of [that page](limits-cdp-client-server.md) — but the
*motivation* it produces is sound regardless.

**Post-processing is conditional, not free.** This is the structural price of restricting the adversary and
the paper is explicit about it: "We cannot expect post-processing invariance to hold with respect to all
functions for capacity bounded privacy — otherwise, the definition would be equivalent to privacy for all
adversaries!" Theorem 1 gives post-processing only under a closure condition relating three classes: if
`i ∘ g ∈ H` for every `g ∈ G` and `i ∈ I`, then `(H, Γ)`-privacy of `A` yields `(I, Γ)`-privacy of `g ∘ A`.
Self-invariance is the special case `I = H`. The worked example is linear `G`, `H`, `I`.

**Worked mechanism results are for the linear class only** (plus a plot for low-degree polynomials). Table 1
gives `(lin, KL)` and `(lin, Renyi)` parameters for the Laplace and Gaussian mechanisms in one and `d`
dimensions. The `(lin, KL)` Laplace parameter is slightly better than KL-DP; the Gaussian mechanism gets
**no** improvement in KL, because the maximizing `h` in the variational form for two equal-variance
Gaussians is already linear. For Rényi, the `(lin, Renyi)` upper bound grows as `1 + (2ε)^{α−1}` while the
Renyi-DP lower bound grows as `(e^ε)^{α−1}`, so for any `ε` a moderate `α` makes the restricted bound
smaller. Figure 1b plots exact `(poly, Renyi)` parameters for degrees 1, 2, 3 and shows them converging
to the unrestricted Rényi parameter as degree increases — a graded, degree-indexed family of adversary
strengths, which is the closest thing in this literature to a resolution knob on the computational axis.
Theorem 5 lifts the `d`-dimensional Laplace bound to the Matrix Mechanism by post-processing.

§6 adds a generalization result: under a condition connecting `H` to the statistical query class `Q`
(namely `H ⊇ {h_x : h_x(q) = q(x)}`), `(H, KL)`-capacity-bounded privacy with parameter `ε` implies an
expected generalization gap `≤ √(8ε)` (Theorem 6). A new Pinsker-like inequality for restricted KL
divergences (Theorem 7) is the ingredient, stated for convex, translation-invariant, negation-closed
`H` with range `[−1, 1]`.

## Claim Boundary

- **Quantified over:** the definition quantifies over all `h ∈ H` and all adjacent dataset pairs. The
  property theorems quantify over the stated classes of `H`. The mechanism results quantify over the
  Laplace and Gaussian mechanisms with `H = lin` (and `poly` numerically).
- **Antecedent:** listed in the front matter. Each property carries its own closure or convexity
  condition; none of them is unconditional in `H`.
- **Excluded cases:** post-processing by arbitrary functions is excluded by design. **Adaptive
  composition is not established** — "The composition guarantees offered by Theorem 4 are non-adaptive –
  the mechanisms A and B are known in advance, and B is not chosen as a function of the output of A.
  Whether fully general adaptive composition is possible for the capacity bounded definitions is left as
  an open question for future work." Convexity for restricted **Rényi** does not hold, mirroring the
  unrestricted case. The generalization theorem bounds only an **expectation**, not a high-probability or
  adaptive gap, and "the result would not hold for arbitrary `(H, KL)`-capacity bounded privacy, and a
  condition that connects `H` to `Q` appears to be necessary."
- **Does not establish:** any bound for the function classes the motivation advertises. Kernel classifiers,
  ReLU-network adversaries, and general machine-learnt attackers are named as "an interesting research
  direction," not analyzed. It does not establish that restricting the class always helps — the Gaussian
  mechanism under `(lin, KL)` gains nothing. It does not price the adversary in runtime, samples, or
  queries, and it makes no claim about computational hardness.
- **Abstract vs theorem:** the abstract says the definitions "possess a number of interesting properties
  enjoyed by differential privacy and some of its existing relaxations" — hedged with "a number of," and
  the body is candid about which properties are conditional and which are open. The abstract's "common
  mechanisms such as the Laplace and Gaussian mechanisms enjoy better privacy guarantees for the same added
  noise under these definitions" is looser than the body, where the Gaussian mechanism's `(lin, KL)`
  parameter is *equal*, not better. Minor.

## Key Contributions

- `(H, Γ)`-capacity bounded differential privacy, via restricted `f`- and Rényi divergences.
- Conditional post-processing (Theorem 1), convexity for `f`-divergences (Theorem 2), parallel composition
  (Theorem 3), non-adaptive sequential composition (Theorem 4) — each under explicit conditions on `H`.
- Closed-form and numerical capacity-bounded parameters for Laplace and Gaussian under `lin` and `poly`,
  and the degree-indexed convergence to unrestricted Rényi.
- Matrix Mechanism bound (Theorem 5).
- Algorithmic generalization from capacity-bounded privacy (Theorem 6), and a Pinsker-like inequality for
  restricted KL divergences (Theorem 7) offered as of independent interest to the GAN literature, from
  which the restricted-divergence machinery is borrowed.

## Key Definitions / Theorems

- **Restricted `f`-divergence.** `D_f^H(P, Q) = sup_{h ∈ H} E_{x∼P}[h(x)] − E_{x∼Q}[f*(h(x))]`.
- **Restricted Rényi.** `D_{R,α}^H(P, Q) = log(1 + α(α−1) D_α^H(P, Q))/(α−1)`, via the `α`-divergence.
- **Definition 3 ((H, Γ)-Capacity Bounded Differential Privacy) — verbatim:**

  > "Let H be a class of functions with domain X , and Γ be a divergence. A mechanism A is said to offer
  > (H, Γ)-capacity bounded privacy with parameter ǫ if for any two D and D′ that differ by a single
  > person's value, the H-restricted Γ-divergence between A(D) and A(D′) is at most ǫ:
  > ΓH (A(D), A(D′)) ≤ ǫ"

- **Theorem 1 (Post-processing).** Requires `i ∘ g ∈ H` for all `g ∈ G`, `i ∈ I`; then `(H, Γ)`-privacy of
  `A` gives `(I, Γ)`-privacy of `g ∘ A`, for `Γ` an `f`-divergence or Rényi of order `α > 1`.
- **Theorem 4 (Sequential composition).** `H₁, H₂` convex, translation invariant, containing a constant
  function; `H = {h₁ + h₂}`; `Γ` KL or Rényi `α > 1`; parameters add. Non-adaptive only.
- **Theorem 6 (Algorithmic generalization).** If `H ⊇ {h_x}` and `M` is `(H, KL)`-capacity bounded private
  with parameter `ε`, then `E[|1/n Σ q_S(x_i) − E_{x∼D}[q_S(x)]|] ≤ √(8ε)`.
- **Theorem 7 (Pinsker-like inequality for restricted KL).** `IPM^H(P, Q) ≤ √(8 · ...)` for convex,
  translation-invariant, negation-closed `H` with range `[−1, 1]`. `IPM^H(P,Q) = sup_{h∈H} |E_P[h] − E_Q[h]|`
  (Definition 4).

## Connections

- Concept: [capacity-bounded privacy](../concepts/capacity-bounded-privacy.md) — this is the founding
  source.
- Concept: [low-degree polynomial framework](../concepts/low-degree-polynomial-framework.md) — the
  `(poly, Renyi)` family is a degree-graded adversary class, structurally the same restriction the
  low-degree literature uses for algorithms rather than adversaries.
- Concept: [computational vs statistical memorization](../concepts/computational-vs-statistical-memorization.md).
- Contrasts with [MPRV09](computational-differential-privacy.md): same goal (weaken the adversary), a
  different axis (function class instead of runtime).
- Motivated by the impossibility literature: it cites [GKY11](limits-cdp-client-server.md) as the reason
  the runtime axis is unpromising centrally. Read the boundary section of that page before repeating the
  motivation as stated.
- Directly extended by [DM22](kernel-quantum-renyi-audit.md), which makes the same restrict-the-witness-class
  move with RKHS/kernel classes, cites this paper for the three-properties framing, and closes by naming
  "exploring the link of the learned kernel with adversaries with limited capacity [Chaudhuri et al., 2019]"
  as future work.
- Adjacent on the knowledge axis rather than the class axis: [CHSS24](attaxonomy.md) and
  [SAH+25](adversary-aware-dp-bounds.md) weaken the adversary by prior knowledge, not by class.
- [KLNRS08](what-can-we-learn-privately.md) is the mirror image: there the **learner** is restricted to
  statistical queries and the adversary is the standard unbounded DP distinguisher; here the **adversary**
  is restricted and the learner is not.
- Cautionary neighbour: [PixelDP (LAGHJ19)](certified-robustness-differential-privacy.md) builds a certified
  defence directly on DP's **free post-processing** — "any function of a DP output remains DP." That step is
  exactly what capacity-bounded privacy gives up. Any attempt to port a DP-based robustness certificate to a
  restricted-adversary notion has to re-derive it under the closure condition of Theorem 1.
- [DP20](sok-differential-privacies.md) would file this under a function-class axis it does not have; its
  dimension **C** is runtime only.
- Entities: [Kamalika Chaudhuri](../entities/kamalika-chaudhuri.md).

## Open Questions / Limitations

- **Adaptive composition** is open, and this is the sharpest gap. Without it the definition does not
  compose across a training run.
- High-probability and adaptive generalization bounds are open, blocked on missing information-theoretic
  properties of restricted divergences.
- Mechanisms designed *for* rich classes — kernel, ReLU-network, classifier adversaries — are not
  constructed. The paper calls this "an interesting research direction."
- No relation is established between capacity-bounded and computational DP; the axes are declared
  orthogonal but not compared.

## Quotes / Notable Passages

> "bounded not in computational power, but in terms of the function class from which their attack algorithm
> is drawn"

> "We cannot expect post-processing invariance to hold with respect to all functions for capacity bounded
> privacy – otherwise, the definition would be equivalent to privacy for all adversaries!"

> "The polynomial function classes are too simple to distinguish the two distributions for larger α, but
> their ability to do so increases as the polynomial complexity increases."

> "Whether fully general adaptive composition is possible for the capacity bounded definitions is left as
> an open question for future work."
