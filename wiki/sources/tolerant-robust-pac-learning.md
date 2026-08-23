---
title: "Simplifying Adversarially Robust PAC Learning with Tolerance"
type: source
date_ingested: 2026-04-12
authors: [Hassan Ashtiani, Vinayak Pathak, Ruth Urner]
venue: "venue unconfirmed from PDF. The ingested file is arXiv:2502.07232v1, 11 February 2025, and states no venue. Author affiliations on the file are McMaster University, independent, and York University."
year: 2025
tags: [adversarial-ml, PAC-learning, sample-complexity, robustness, learning-theory]
claim_quantifier: universal
antecedent: "The tolerance relaxation. The learner's adversarial loss is measured under the perturbation type U while the comparator is the best achievable adversarial loss under a strictly larger reference type V. Without that gap none of the bounds is claimed. Theorem 9 additionally requires that the smoothing type W satisfy W(z) inside V(x) and mu_{V(x)}(W(z)) at least 3 eta for all x and all z in U(x). Theorem 12 requires that the discretization be an r*gamma-cover of the space and that the perturbation sets be balls. All algorithms assume access to an ERM or robust ERM oracle."
adversary_bound: "none in any computational resource. The adversary is constrained only by the perturbation set U(x), a geometric budget. Appendix A supplies a second and sharper reading, that tolerant robust learning is exactly robust learning against a SMOOTHED adversary whose chosen point z is then perturbed uniformly at random within W(z). That constrains the adversary in precision, not in compute, queries, or memory. The learner is constrained in samples."
model_class: "binary hypothesis classes H over a domain X of finite VC dimension, with perturbation types U, V, W given as balls in a metric space for the quantitative corollaries."
algorithm_class: "none. The results are information-theoretic sample-complexity bounds. The learners are stated relative to an ERM or robust ERM oracle and no running time is analysed anywhere in the paper."
date_verified: 2026-08-22
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: white box
cls_write: read only
cls_frame: capability
cls_party: attacker
cls_unit: perturbation
cls_tightness: budget
cls_baseline: n/a
cls_second_party: samples
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "a worst-case adversary is allowed to generate points anywhere within U(x)"
cls_evidence_src: Appendix A
cls_reason: "party/unit/tightness/frame follow Rule 5 (norm-ball restriction = attacker/perturbation/budget/capability). second_party=samples is the learner's bound (Thm 9/12, sample complexity linear in VC(H)): per Rule 4, neither bound is computational, so the adversary's bound decides the row and the learner's sample-complexity unit is recorded second. access=white box is inferred from Def 1 (the adversarial loss is a max over ℓ(h,z,y), which requires evaluating h), not from an explicit access-model statement. baseline=n/a: the paper states sample-complexity bounds, not an advantage-over-baseline measure."
cls_prov: P
cls_date: 2026-08-22
---

> **Verified against the primary source.** The page was checked against `raw/APU25_TolerantRobustPAC.pdf`
> on 2026-08-22. Theorem statements and attributions are corrected below.

## Summary

Adversarially robust PAC learning of a VC class requires an improper learner, and the best known
learner of Montasser, Hanneke and Srebro uses a sample complexity that can be exponential in the VC
dimension. A line of work relaxes the problem by *tolerance*, comparing the learner's adversarial loss
under a perturbation type `U` against the best achievable adversarial loss under a slightly larger
reference type `V`. Under tolerance, sample complexity linear in the VC dimension was already known,
but only through a compression-based algorithm or under extra assumptions on the hypothesis class.

This paper removes both. Its claim of priority is narrow and precise, verbatim: *"We prove, for the
first time, the existence of a simpler learner that achieves a sample complexity linear in the
VC-dimension without requiring additional assumptions on H."* The novelty is the simplicity of the
learner and the absence of assumptions, not the linear dependence itself.

The two learners are short to state. Run robust ERM with respect to the reference type `V`, then output
the majority label of the resulting hypothesis over a smoothing neighbourhood. Or discretize the space
by a grid, run robust ERM with respect to the discretized perturbation type, then output the nearest
grid neighbour's label. Both are improper, but the improperness is confined to the last step, so the
output is a smoothed or discretized version of a member of `H`. The authors call this *"almost proper"*.
Improperness cannot be avoided, and they prove that even at VC dimension 1.

Appendix A gives the reading that matters most for pricing an attacker. Tolerant robust learning is
exactly robust learning against a *smoothed* adversary, whose chosen perturbation is then jittered
uniformly at random within a neighbourhood.

## Claim Boundary

- **Quantified over.** The positive results are universal over hypothesis classes of finite VC dimension
  and over all distributions in the relevant class, with no further assumption on `H`. Theorem 7, the
  impossibility, is existential in `H` and universal in the parameters, namely for any radius `r`, any
  dimension `d`, and any bound `g > 0` there exists a class with VC dimension 1 that fails, for every
  tolerance `γ` with `0 < γ ≤ g`.
- **Antecedent.** The tolerance gap, as recorded in the front matter. It is load-bearing. Setting
  `U = V` recovers the standard robust PAC definition of Montasser et al., and none of these bounds is
  claimed there. The headline linear-in-VC bound is therefore conditional on a weakened success
  criterion rather than a strengthening of the untolerant characterization.
- **Which party is constrained and in what resource.** The **learner**, in sample complexity. The
  **comparator**, through the tolerance gap, since it is charged against the larger set `V`. The
  **adversary** is constrained geometrically by `U(x)` and, under the Appendix A reading, in precision
  by the random smoothing of its chosen point. Nothing is priced in compute, queries, or memory on
  either side.
- **Algorithm class.** None. The bounds are information-theoretic. The learners are stated relative to
  an ERM or robust ERM oracle, and the paper never analyses the running time of any procedure. For a
  survey axis about compute-bounded parties, this paper is an empty cell.
- **Does not establish.** It does not establish any bound in the untolerant setting. It does not
  establish computational efficiency, since the RERM oracle is assumed. It does not establish proper
  learnability, which is ruled out even at VC dimension 1. It does not remove the dependence on the
  ambient dimension `d`, which the authors record as their own open problem for `γ = 1`. Theorem 15 is a
  factor-3 agnostic guarantee rather than an additive one.
- **Abstract versus theorem.** The abstract is accurate and the priority claim is correctly scoped, as
  quoted above. A reader who compresses it to "first linear-in-VC bound" overstates it, because
  Ashtiani et al. 2023 and Bhattacharjee et al. 2023 had linear-in-VC bounds under tolerance already.

## Key Contributions

- **Theorem 9 (RERM-and-Smooth, realizable).** For `H` of finite VC dimension, `0 < η < 1/3`, and
  perturbation types with `U ≺ V`, `W(z) ⊆ V(x)` and `μ_{V(x)}(W(z)) ≥ 3η` for all `x` and all
  `z ∈ U(x)`, Algorithm 1 `(U, V)`-tolerantly robustly PAC learns `H` in the tolerantly realizable case
  with sample complexity `Õ((VC(H)·log(VC(H)/η) + log(1/δ)) / ε)`.
- **Remark 10.** For Euclidean balls of radii `r(1+γ)`, `r` and `rγ`, choosing `η = 1/(3(1+1/γ)^d)`
  yields `Õ((VC(H)(log VC(H) + d·log(1+1/γ)) + log(1/δ)) / ε)`.
- **Remark 11.** The learner does not use the discrete perturbation type `C`. Verbatim: *"We emphasize
  that the learner in Algorithm 1 is not employing the discrete perturbation type C and thus does not
  need knowledge (or ability to construct) C."* It is a tool of the analysis only. The agnostic
  modification in Appendix D loses this property.
- **Theorem 12 (RERM-and-Discretize).** For `U` and `V` balls of radii `r` and `r(1+γ)` and a
  discretization `C` that is an `rγ`-cover with induced perturbation sets of size at most `k`,
  Algorithm 2 is a `γ`-tolerant robust PAC learner with sample complexity
  `Õ((VC(H)·log k + log(1/δ)) / ε)` realizable and `Õ((VC(H)·log k + log(1/δ)) / ε²)` agnostic. For an
  evenly spaced grid of side length `2rγ/d`, `k` is bounded by `Θ((1+1/γ)^d · d^{d/2})`, and the grid is
  an `rγ`-cover with respect to any `ℓ_p` norm with `p ≥ 1`. This route drops the `log VC(H)` factor of
  Theorem 9.
- **Theorem 7 (improperness is necessary).** Verbatim: for any `r`, any `d` and any `g > 0`, *"there
  exist a hypothesis class H over X = Rd with VC(H) = 1 that is not properly tolerantly robustly PAC
  learnable (even in the tolerantly realizable case)"* for `U(x) = B_r(x)` and `V(x) = B_{(1+γ)r}(x)`
  for any `γ` with `0 < γ ≤ g`. The sample complexity is allowed to depend on `d` and the impossibility
  still holds.
- **Theorems 14 and 15 (semi-supervised).** Algorithm 3 is a `γ`-tolerant robust learner in the
  realizable setting with unlabeled sample complexity `Õ((VC(H)(d·log(1+1/γ) + log d) + log(1/δ)) / ε)`
  and a smaller labeled complexity. Algorithm 4 gives a factor-3 agnostic guarantee with the analogous
  `1/ε²` unlabeled bound. Both avoid the one-inclusion-graph subroutine of the earlier semi-supervised
  result.

## Key Definitions / Theorems

- **Definition 1 (adversarial loss).** `ℓ^U(h, x, y) = max_{z ∈ U(x)} ℓ^{0/1}(h, z, y)`, with the
  expected and empirical versions defined accordingly, and the adversarial approximation error
  `L^U_P(H) = inf_{h ∈ H} L^U_P(h)`.
- **Definition 3 (tolerant adversarial PAC learner).** Attributed in the paper to Ashtiani, Pathak and
  Urner 2023, not introduced here. For `U ≺ V`, the learner `A` is `(U, V)`-tolerant if with probability
  at least `1 − δ` over a sample of size `m_A(ε, δ)`, `L^U_P(A(S)) ≤ L^V_P(H) + ε`. `U` is the *actual*
  perturbation type and `V` the *reference* type. Setting `U = V` recovers the standard robust PAC
  definition.
- **The tolerance parameter.** When `U(x) = B_r(x)` is inflated by `W(x) = B_{rγ}(x)` to give
  `V(x) = B_{(1+γ)r}(x)`, the quantity `γ > 0` is the tolerance parameter and `(U, V)`-tolerance is also
  called `γ`-tolerance. `W` is called the *smoothing* perturbation type.
- **Definition 4 (`VC_U`-dimension).** `H` `U`-shatters `K ⊆ X` if for every labeling `y ∈ {0,1}^K`
  there is an `h ∈ H` with `h(z) = y(x)` for all `z ∈ U(x)` and all `x ∈ K`. The `VC_U`-dimension is the
  supremum of the sizes of `U`-shattered sets, and it never exceeds `VC(H)`.
- **Definition 5 (ERM and RERM oracles).** An ERM oracle returns any empirical risk minimizer in `H`
  under the 0/1 loss, and an RERM oracle does the same under an adversarial loss. Both are assumed, not
  constructed.
- **Definition 8 (`η`-net for a class).** `C ⊆ X` is an `η`-net for `H` with respect to `D` if whenever
  a label pre-image `h^{-1}(y)` has mass at least `η`, the net meets it. Standard VC theory gives such a
  net of size `O(VC(H)/η)`, which is what supplies the `log(VC(H)/η)` factor in Theorem 9.

## Connections

- [Robust PAC Learning Characterization](robust-pac-learning-characterization.md), Montasser, Hanneke
  and Srebro. This paper's Definition 3 reduces to theirs when `U = V`, and its stated purpose is to
  avoid their one-inclusion-graph and compression subroutines. The paper places them among
  characterizations obtained *"through rather impractical learners"*.
- [Lower Bounds for Adversarially Robust PAC Learning](lower-bounds-robust-pac-learning.md).
- Concepts: [robust-pac-learning](../concepts/robust-pac-learning.md),
  [evasion-attacks](../concepts/evasion-attacks.md).
- Entities: [Hassan Ashtiani](../entities/hassan-ashtiani.md), [Ruth Urner](../entities/ruth-urner.md),
  [Omar Montasser](../entities/omar-montasser.md).
- **Prior work in the tolerance line**, all cited by the paper. Ashtiani, Pathak and Urner, *Adversarially
  robust learning with tolerance*, ALT 2023, which introduced the definition and gave a compression-based
  learner. Bhattacharjee, Hopkins, Kumar, Yu and Chaudhuri, *Robust empirical risk minimization with
  tolerance*, ALT 2023, which needed a regularity assumption. Raman, Subedi and Tewari, NeurIPS 2024.
  Attias, Hanneke and Mansour, NeurIPS 2022, for the semi-supervised comparison. Montasser, Hanneke and
  Srebro, *Transductive robust learning guarantees*, which handles `γ = 1` transductively with a bound
  independent of `d`.

## The tolerance relaxation, read as a constraint on the adversary

This is the part of the paper most relevant to any survey that asks which party is priced and in what
unit. Appendix A rewrites tolerance as a property of the adversary rather than of the comparator.
Standard learning against a worst-case adversary is characterized by the Littlestone dimension, which
can be far larger than the VC dimension. Smoothed analysis restores VC characterization by perturbing
the adversary's chosen points at random. The paper applies that idea here, verbatim:

> "To smooth an adversary, one takes the points generated by the worst-case adversary and perturbs them
> uniformly at random within a neighbourhood. In adversarially robust learning a worst-case adversary is
> allowed to generate points anywhere within U(x). One can consider a smoothed adversary in a similar
> way, where the point z generated by the worst-case adversary is perturbed uniformly at random within
> W(z)."

And then, verbatim:

> "Learning with respect to this adversary is then exactly the problem of tolerantly robust learning.
> Our results essentially show that adversarially robust learning with smoothed adversaries is easier."

The constraint is on the adversary's **precision**, not on its resources. It cannot place its
perturbation exactly, because the placement is jittered. That is a randomness constraint of the same
family as smoothed analysis, and it is not a compute, query, or memory bound. The paper prices no party
in any computational unit.

## Open Questions / Limitations

The paper's own open problem, from Section 5.

- Eliminate the dependence on the ambient dimension `d` for `γ = 1`. Montasser, Hanneke and Srebro prove
  a transductive learner for `γ = 1` whose sample complexity is independent of `d`, and the authors ask
  whether their techniques give the same in the inductive case. They identify the cause. Their bounds
  need a cover of `V(x)` by `W`, of size `(1+1/γ)^d`, whereas covering only `U(x)` would give `1/γ^d`,
  which is dimension-free at `γ = 1`.

Limitations visible from the results and not stated as open problems by the authors.

- The tolerance gap between `U` and `V` cannot be removed. Removing it returns the untolerant problem,
  where the exponential-in-VC bound stands.
- Computational efficiency is not addressed. The learners call an RERM oracle whose implementation is
  outside the paper, and no running time is analysed for halfspaces, neural networks, or any other
  class.
- The quantitative bounds assume perturbation sets that are balls in a metric space and admit a uniform
  measure. Perturbation types outside that shape are not covered.
- Theorem 15 gives a factor-3 rather than an additive agnostic guarantee.
- The agnostic variant of Algorithm 1 in Appendix D requires knowledge of the discrete perturbation
  type, losing the property recorded in Remark 11.

## Quotes / Notable Passages

On the scope of the priority claim:

> "We prove, for the first time, the existence of a simpler learner that achieves a sample complexity
> linear in the VC-dimension without requiring additional assumptions on H."

On the form of improperness:

> "Even though our learner is improper, it is "almost proper" in the sense that it outputs a hypothesis
> that is "similar" to a hypothesis in H."

On what tolerance is for, from Appendix A:

> "tolerance is a good way to capture the user's ambivalence over precisely which perturbation type to
> be robust against"

From the Discussion:

> "The main message of this work is that adding tolerance vastly simplifies the task of adversarially
> robust learning, and is perhaps a more natural formulation of the robust learning problem in the first
> place."
