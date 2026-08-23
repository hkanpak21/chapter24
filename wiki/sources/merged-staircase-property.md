---
title: The merged-staircase property - a necessary and nearly sufficient condition for SGD learning of sparse functions on two-layer neural networks
type: source
date_ingested: 2026-08-20
authors: [Emmanuel Abbe, Enric Boix-Adserà, Theodor Misiakiewicz]
venue: venue unconfirmed from PDF (arXiv:2202.08658v2 [cs.LG], 26 Aug 2024; cited elsewhere in this corpus as COLT 2022)
year: 2022
tags: [learning-theory, sample-complexity, hypercube, mean-field, feature-learning, leap-complexity]
claim_quantifier: existential
antecedent: "Conditions A0-A3 (bounded three-times-differentiable activation, one-pass fresh samples with bounded response, rotationally structured initialization, bounded and Lipschitz hyperparameters); latent dimension P fixed and independent of d; mean-field scaling. Sufficiency additionally holds only almost surely over the non-zero Fourier coefficients (measure mu_S), and for polynomial activations sigma(x) = (1+x)^L with L = 2^{8P}."
model_class: "Sparse functions on the Boolean hypercube: x ~ Unif({+1,-1}^d), f*(x) = h*(x_I) for an unknown coordinate subset I of size P, plus bounded independent zero-mean label noise. Hypercube inputs, NOT Gaussian; depth-2 network in the mean-field regime."
algorithm_class: "one-pass batch-SGD on a depth-2 mean-field network (square loss, layer-wise l2 regularization, time-varying step sizes); equivalently the dimension-free gradient-flow PDE"
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: algo class
cls_tightness: class
cls_baseline: n/a
cls_second_party: none
cls_second_notion: samples
cls_assessed: explicit
cls_evidence: "Let h∗ : {+1, −1}P → R be a function without MSP. Then there exists c > 0 such that for any ξ a , ξ w : R → R and regularizations λa , λw ≥ 0, we have inf t≥0 R(ρt ) ≥ c."
cls_evidence_src: Thm 7
cls_reason: "party=learner, not attacker: this is a pure learning-theory result with no adversary, so the attack-scenario fields (target/family/phase/access/write) are all none/n/a. unit=algo class rather than samples: Theorem 7 quantifies over all choices of SGD hyperparameters (xi^a, xi^w, lambda^a, lambda^w), i.e. over the algorithm class of one-pass mean-field batch-SGD, and the Claim Boundary explicitly denies a graded sample-complexity relation exists here ('MSP is a binary property... with no exponent attached to non-MSP targets'), so tightness=exponent would overstate the result; tightness=class matches the restricted-algorithm-family shape instead, analogous to SQ or low-degree. second_notion=samples records the O(d) scaling at which the algorithm-class question is posed, per Definition 3. frame=compute because the restriction is explicitly to SGD as opposed to any sample-efficient algorithm, and the field definition lists algorithm-class restriction as a computational bound."
cls_prov: F
cls_date: 2026-08-22
---

## Summary

This paper asks which sparse Boolean functions a depth-2 network trained by one-pass batch-SGD in the mean-field regime can learn with `O(d)` samples, and answers with the **merged-staircase property (MSP)**: the non-zero Fourier-Walsh coefficients of the latent function `h*` can be ordered `S_1, ..., S_m` so that each set adds at most one new coordinate, `|S_i \ ∪_{i' < i} S_{i'}| <= 1`. MSP is *necessary* (Theorem 7) and *nearly sufficient* (Theorem 9, almost surely over the coefficients) for what they call strong SGD-learnability in `O(d)`-scaling.

The technical engine is a *dimension-free* dynamics (DF-PDE) on `R^{P+2}`, independent of `d`, that approximates the mean-field SGD trajectory for `P`-sparse targets (Theorem 5). Theorem 6 turns learnability into a reachability question: `h*` is strongly `O(d)`-SGD-learnable iff the DF-PDE from the initialization `rho_0 = mu_a ⊗ delta_{u_0 = 0} ⊗ delta_{s_0 = c}` reaches arbitrarily small risk. Necessity then follows from a symmetry argument: for non-MSP targets some first-layer coordinates remain identically zero along the flow, so any Fourier coefficient containing them is never learned.

Sufficiency needs a genericity caveat. Some symmetric MSP functions — the paper's example is `z_1 + z_2 + z_1 z_3 + z_2 z_4` — have degenerate dynamics and are *not* strongly `O(d)`-learnable, so Theorem 9 is stated almost surely with respect to the Lebesgue measure on the non-zero coefficients. Vanilla staircases `alpha_1 z_1 + alpha_2 z_1 z_2 + ... + alpha_P z_1 ... z_P` need no genericity (Theorem 10), only `sigma^{(r)}(0) != 0` for `r = 0, ..., P`.

Contribution (4) gives a superpolynomial separation from linear methods: with `P` growing slowly in `d`, MSP functions stay at `d^{O(1)}` for SGD while any linear method needs `d^{omega_d(1)}` (Propositions 11, 12).

## Claim Boundary

- **Quantified over:** a single fixed latent function `h*` and fixed `P`, uniformly over all latent coordinate subsets `I ⊆ [d]` of size `P`. The hyperparameters may be tuned per target (Definition 3), restricted by A0-A3 to a "continuous" (`b = o(d)`, `eta = o(1)`, `Theta(1/eta)` steps) or "discrete" (`b = Theta(d)`, `eta = Theta(1)`, `Theta(1)` steps) regime.
- **Model class and data assumption:** **hypercube** inputs `Unif({+1,-1}^d)`, depth-2 fully-connected network, mean-field scaling, one-pass (fresh samples each step, A1). This is not a Gaussian result and not a result about deeper networks. The Gaussian generalisation is [ABM23](leap-complexity-sgd.md).
- **Algorithm class:** batch-SGD in the mean-field regime with square loss, via the DF-PDE approximation. Not SQ, not CSQ, not low-degree. The separation result (contribution 4) is against *linear/kernel* methods, a different and weaker comparison class.
- **Does not establish:** (a) a graded cost. MSP is a **binary** property — a target either is or is not strongly `O(d)`-SGD-learnable — with no exponent attached to non-MSP targets. The paper states as an open direction extending to `alpha > 1` and relating this to the leap; that is [ABM23](leap-complexity-sgd.md)'s contribution; (b) sufficiency for all MSP functions — degenerate symmetric counterexamples exist (Section 4); (c) tractability. Definition 3 allows hyperparameter tuning per target, and the sufficiency proof uses `sigma(x) = (1+x)^L` with `L = 2^{8P}`; (d) anything under batch reuse. [DTA+24](reusing-batches-breaks-exponents.md) shows multi-pass GD escapes the staircase restriction.
- **Abstract vs theorem:** the abstract's "necessary and nearly sufficient" is honest, and "nearly" is exactly the almost-sure caveat. One residual gap: the sufficiency theorem in the main text is proved for the specific polynomial activation `(1+x)^L` (with a footnote that it must be truncated to be bounded); extension to generic smooth activations is relegated to Appendix F "with a small technical caveat".

## Key Contributions

- Definition of MSP set structures and MSP functions (Definitions 1, 2).
- Dimension-free dynamics approximating mean-field batch-SGD for `P`-sparse targets, with non-asymptotic bounds (Theorem 5), and the resulting equivalence with strong `O(d)`-SGD-learnability (Theorem 6).
- MSP necessity (Theorem 7): non-MSP targets keep the DF-PDE risk bounded away from 0 for all `xi^a, xi^w, lambda^a, lambda^w`.
- MSP near-sufficiency (Theorem 9): almost surely over `mu_S`, MSP targets are strongly `O(d)`-SGD-learnable with `sigma(x) = (1+x)^L`, `L = 2^{8P}`.
- Vanilla staircases without genericity (Theorem 10).
- Improved dimension lower bounds for linear/kernel methods on non-almost-orthogonal function classes (Proposition 11), yielding a superpolynomial SGD-vs-linear separation.
- Explicit degenerate MSP counterexamples showing genericity is needed.

## Key Definitions / Theorems

**Definition 1 (MSP set structure), verbatim:**

> "We say that S = {S1 , . . . , Sm } ⊆ 2[P ] is a Merged-Staircase Property (MSP) set structure if the sets can be ordered so that for each i ∈ [m], |Si \ ∪i′ <i Si′ | ≤ 1."

**Definition 2 (Merged-Staircase Property), verbatim:**

> "Let S ⊂ 2[P ] be the non-zero Fourier coefficients of h∗ , i.e., ... We say that h∗ satisfies the merged-staircase property (MSP) if S is a MSP set structure."

(The elided clause is the display `ĥ∗(S) != 0 iff S ∈ S`, whose combining accent does not survive text extraction cleanly.)

**Definition 3 (SGD-learnability in `O(d^alpha)`-scaling).** Learnability with `n <= C(eps,H) d^alpha` samples, uniformly over all latent subsets `I`, at probability `>= 9/10`; strong `O(d)`-SGD-learnability restricts to fixed `P`, `alpha = 1`, and the two hyperparameter regimes.

**Theorem 6, verbatim:** "A function h∗ : {+1, −1}P → R is strongly O(d)-SGD-learnable if and only if for any ε > 0, there exists λa , λw ≥ 0 and Lipschitz ξ a , ξ w : R>0 → R>0 , such that inf t≥0 R(ρt ) < ε."

**Theorem 7, verbatim:** "Let h∗ : {+1, −1}P → R be a function without MSP. Then there exists c > 0 such that for any ξ a , ξ w : R → R and regularizations λa , λw ≥ 0, we have inf t≥0 R(ρt ) ≥ c."

**Theorem 9, verbatim:** "For any MSP set structure S ⊆ 2[P ] , h∗ is strongly O(d)-SGD-learnable almost surely with respect to µS , using activation function σ(x) = (1 + x)L where L = 28P ."

**Theorem 10.** Vanilla staircases with all `alpha_i != 0` are strongly `O(d)`-SGD-learnable for any `sigma in C^{2^{P-1}+1}(R)` with `sigma^{(r)}(0) != 0` for `r = 0, ..., P`.

## Connections

- Concept pages: [Leap Complexity](../concepts/leap-complexity.md) (MSP is leap-1), [Information Exponent](../concepts/information-exponent.md), [Multi-Index Model](../concepts/multi-index-model.md).
- Generalised to graded cost and Gaussian data by [SGD Learning on Neural Networks: Leap Complexity and Saddle-to-Saddle Dynamics](leap-complexity-sgd.md), which states `Leap(h*) = 1` exactly recovers MSP.
- Contradicted as a learnability boundary by [Reusing Batches Breaks the Information and Leap Exponents](reusing-batches-breaks-exponents.md): "the network achieves in just two time steps an overlap with the target subspace even for functions not satisfying the staircase property".
- The CSQ-side reading of MSP appears in [ABM23](leap-complexity-sgd.md); the SQ-side improvement is the [generative exponent](generative-exponent-single-index.md) / [generative leap](generative-leap-multi-index.md).
- Frameworks: [Statistical Query Model](../concepts/statistical-query-model.md), [CSQ Model](../concepts/csq-model.md).
- Authors: [Emmanuel Abbe](../entities/emmanuel-abbe.md), [Enric Boix-Adserà](../entities/enric-boix-adsera.md), [Theodor Misiakiewicz](../entities/theodor-misiakiewicz.md).

## Open Questions / Limitations

- Extending beyond `O(d)`-scaling to `O(d^alpha)`, `alpha > 1`, and connecting to the leap — done in ABM23 as a conjecture plus a specialisation.
- Whether the measure-zero degenerate MSP set can be characterised; the paper only exhibits examples.
- Mean-field / gradient-flow approximation breaks down beyond `O(d)` steps (their own remark, and ABM23's stated reason for a different proof technique).
- Tractability: Definition 3 permits per-target hyperparameter tuning and the proof uses a doubly-exponential-degree activation.

## Quotes / Notable Passages

> "tight necessity results are difficult to obtain in such a setting since SQ-like arguments ... are not expected to be tight"

> "the degenerate cases are a measure-zero set"
