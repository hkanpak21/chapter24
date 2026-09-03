---
title: On the Cryptographic Hardness of Learning Single Periodic Neurons
type: source
date_ingested: 2026-08-20
authors: [Min Jae Song, Ilias Zadik, Joan Bruna]
venue: "NeurIPS 2021"
venue_evidence: "dblp search (q=Cryptographic Hardness of Learning Single Periodic Neurons): NeurIPS 2021, pp.29602-29615, inproceedings, plus CoRR abs/2106.10744"
year: 2021
tags: [cryptography, hardness-reductions, continuous-lwe, lattice-cryptography, single-index-model, lll-algorithm, statistical-query]
claim_quantifier: conditional
antecedent: "Hardness (Theorem 3.3 / Corollary 3.4) is conditional on the quantum worst-case hardness of O(d/tau)-approximate SVP (Conjecture 2.3), routed through the CLWE hardness of Bruna-Regev-Song-Tang (Theorem 2.2). It additionally requires POLYNOMIALLY SMALL BOUNDED ADVERSARIAL noise: |xi| <= beta with beta/(L tau) = omega(sqrt(log d)), gamma = omega(sqrt(log d)) (Cor 3.4: gamma >= 2 sqrt(d), gamma/tau = poly(d))."
model_class: "Periodic neurons over isotropic Gaussian inputs: F_gamma^phi = {f(x) = phi(gamma <w,x>) : w in S^{d-1}} with phi 1-periodic, L-Lipschitz, [-1,1]-valued. Cosine neuron f(x) = cos(2 pi gamma <w,x>) is the running case. Well-approximated by a poly(gamma)-width ONE-HIDDEN-LAYER ReLU network on compact sets (their Appendix E) - the network statement is via approximation, not native."
algorithm_class: "ALL polynomial-time algorithms (conditional on the lattice assumption), strictly extending prior gradient-based and SQ lower bounds; the positive results are an exponential-time cover-search algorithm and a poly-time LLL-based algorithm"
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: time
cls_tightness: poly
cls_baseline: stated
cls_baseline_checked: yes
cls_second_party: perturbation
cls_assessed: explicit
cls_evidence: "such learning task is hard for any polynomial-time algorithm, based on the widely-believed cryptographic assumption that (approximate) SVP is computationally intractable against quantum algorithms"
cls_evidence_src: "§1 (Introduction)"
cls_reason: "target=none and family=none per codebook convention for foundational cryptographic hardness-of-learning works; there is no adversary attacking a trained model, only a reduction pricing the learner. party=learner (not attacker) per rule 3: the bound (all polynomial-time algorithms) binds the learning algorithm, and the Summary states this explicitly ('this paper prices the learner, not an attacker'). second=perturbation for the beta-bounded adversarial noise on labels (Cor 3.4: beta/tau = omega(sqrt(log d))), a capability-style bound on a distinct quantity from the learner's poly-time bound, not itself a resource-bounded strategic party. baseline=stated from Definition 2.1's trivial-loss/edge formulation."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper prices the **learner**, not an attacker, and does so in cryptographic units. It gives a simple reduction showing that weakly learning a single periodic neuron over isotropic Gaussian inputs under polynomially small bounded adversarial noise is hard for *every* polynomial-time algorithm, conditional on the quantum worst-case hardness of approximate SVP — routed through [Continuous LWE](bruna-continuous-lwe.md).

The reduction (Theorem 3.3) is short: a CLWE sample `(x, gamma<w,x> + xi mod 1)` becomes a periodic-neuron sample `(x, phi(gamma<w,x> + xi))` by 1-periodicity, and `L`-Lipschitzness converts the CLWE Gaussian noise into bounded adversarial noise of size `<= L tau <= beta`. A weak learner for `F_gamma^phi` therefore distinguishes CLWE from the null distribution. Corollary 3.4 composes this with Bruna–Regev–Song–Tang to get: a poly-time weak learner for the cosine neuron class under `beta`-bounded adversarial noise implies a poly-time *quantum* algorithm for `O(d/tau)`-approximate SVP.

The paper's second half maps the whole noise landscape, and the picture is that noise is *necessary* for the hardness. Theorem 3.1 gives an `exp(O(d log(gamma/tau)))`-time cover-search algorithm at small constant noise (so the task is information-theoretically feasible there). Theorem 3.6 gives a **polynomial-time** LLL-based algorithm that weakly learns the cosine neuron from exactly `d + 1` samples when the noise is exponentially small `beta <= exp(-(d log d)^3)`. This algorithm is neither gradient-based nor SQ, and applied to noiseless CLWE detection it improves the quadratic-in-`d` sample complexity of BRST to `d + 1` — a concrete instance of an algorithm that escapes SQ/low-degree predictions.

Nothing here prices an attacker. The adversary in "bounded adversarial noise" is a corruption of magnitude `<= beta` with no computational or informational budget of its own; the party whose resources are counted is the learner.

## Claim Boundary

- **Quantified over:** all polynomial-time (improper) learning algorithms, for the class `F_gamma^phi` with any 1-periodic `L`-Lipschitz `phi`; the target is *weak* learning (edge `eps` inverse-polynomial in `d`, per Definition 2.1).
- **Model class and data assumption:** isotropic Gaussian inputs `N(0, I_d)`, a single periodic neuron with a hidden unit direction, frequency `gamma` scaling polynomially with `d`. The one-hidden-layer ReLU statement is by *approximation* (Appendix E), at the cost of an additional approximation error — it is not a native hardness result for ReLU networks. That upgrade is [LZZ24](hardness-one-hidden-layer.md).
- **Algorithm class:** the hardness is against all poly-time algorithms, but *conditionally*. The paper is careful about the trade: "SQ lower bounds are unconditional because they are of an information-theoretic nature. Therefore, our result, which is conditional on a computational hardness assumption ... and SQ lower bounds" are complementary, not nested.
- **Does not establish:** (a) hardness with Gaussian noise. The noise is bounded *adversarial*; the Gaussianization step is [LZZ24](hardness-one-hidden-layer.md)'s contribution; (b) hardness at exponentially small noise — Theorem 3.6 shows the opposite, via LLL; (c) any bound on an attacker. The adversary is uncosted noise; (d) a native ReLU-network hardness result.
- **Abstract vs theorem:** none found. The abstract says the reduction shows "any polynomial-time algorithm ... for learning such functions under small noise implies a polynomial-time quantum algorithm for solving worst-case lattice problems" and immediately flags "We show that if (polynomially) small noise is added to the labels", plus "we demonstrate the necessity of noise in the hardness result". The conditionality and the noise requirement are both stated up front.

## Key Contributions

- Theorem 3.3: reduction from `CLWE_{tau,gamma}` to weakly learning `F_gamma^phi` under `beta`-bounded adversarial noise, for any 1-periodic `L`-Lipschitz `phi`.
- Corollary 3.4: cryptographic hardness of the cosine neuron under inverse-polynomial noise, via `O(d/tau)`-approximate SVP.
- Theorem 3.1 / Corollary 3.2: information-theoretic feasibility at small constant noise via an `exp(O(d log(gamma/beta)))`-time cover-search algorithm.
- Theorem 3.6 / Corollary 3.7: an LLL-based polynomial-time algorithm weakly learning the cosine neuron with `d + 1` samples under exponentially small noise — neither gradient-based nor SQ.
- Corollary 3.11 / Theorem 3.12: exact recovery for phase retrieval with `d + 1` samples under exponentially small noise, shown optimal under norm priors.
- Improvement of CLWE detection sample complexity from quadratic in `d` to `d + 1` in the noiseless case.

## Key Definitions / Theorems

**Definition 2.1 (Weak learning).** `A` `eps`-weakly learns `{F_d}` over the standard Gaussian if for every `f in F_d` it outputs `h_d` with `L_{D_f}(h_d) <= L_{D_f}(E[f(x)]) - eps` w.p. `>= 1 - delta`. `L_D(E[f(x)]) = Var(f(Z))` is the "trivial loss" and `eps` the "edge".

**Periodic neurons, Eq. (2), verbatim:** `F_gamma^phi = {f : R^d -> [-1,1] | f(x) = phi(gamma<w,x>), w in S^{d-1}}`.

**Cosine distribution, Eq. (3):** `z = cos(2 pi gamma <w,x>) + xi` with `x ~ N(0,I_d)` and "some bounded adversarial noise |ξ| ≤ β".

**Theorem 3.3, verbatim:**

> "Moreover, let L > 0, let φ : R →√[−1, 1] be an L-Lipschitz 1-periodic univariate function, and τ = τ (d) be such that β/(Lτ ) = ω( log d). Then, a polynomial-time (improper) algorithm that weakly learns the function class Fγφ = {fγ,w (x) ="

> "φ(γhw, xi) | w ∈ S d−1 } over Gaussian inputs x ∼ N (0, Id ) under β-bounded adversarial noise"

> "implies a polynomial-time algorithm for CLWEτ,γ ."

(the statement opens `Let d ∈ N, γ = ω(sqrt(log d)), β = β(d) ∈ (0,1)`; the stray √ and the floating "i.i.d." between the fragments are extraction artefacts)

(the statement opens `Let d ∈ N, γ = ω(sqrt(log d)), β = β(d) ∈ (0,1)`; the stray √ before `[−1,1]` is an extraction artefact of the `omega(sqrt(log d))` appearing on the following line)

**Corollary 3.4.** With `gamma >= 2 sqrt(d)`, `gamma/tau = poly(d)`, `beta/tau = omega(sqrt(log d))`: such a learner implies a poly-time quantum algorithm for `O(d/tau)`-approximate SVP.

**Theorem 2.2 (imported from Bruna–Regev–Song–Tang, their Corollary 3.2).** For `beta in (0,1)`, `gamma >= 2 sqrt(d)` with `gamma/beta` polynomially bounded: a poly-time quantum reduction from `O(d/beta)`-approximate SVP to `CLWE_{beta,gamma}`.

**Theorem 3.6 (LLL).** For `1 <= gamma <= d^Q` and `beta <= exp(-(d log d)^3)`, Algorithm 2 on `d+1` samples returns `w'` with `min{||w' - w||, ||w' + w||} = O(beta/gamma)` in `poly(d)` steps w.p. `1 - exp(-Omega(d))`.

## Connections

- Direct dependency: [Continuous LWE](bruna-continuous-lwe.md) and the concept pages [Continuous LWE](../concepts/continuous-lwe.md), [Learning With Errors](../concepts/learning-with-errors.md), [LLL Algorithm](../concepts/lll-algorithm.md).
- Upgraded to ReLU one-hidden-layer networks and to *Gaussian* noise by [On the Hardness of Learning One Hidden Layer Neural Networks](hardness-one-hidden-layer.md).
- Cited by [Computational-Statistical Gaps in Gaussian Single-Index Models](generative-exponent-single-index.md) as the reason the phase-retrieval gap disappears in the noise-free setting: "there are computationally efficient algorithms based on lattice reduction that achieve the information-theoretic threshold".
- The LLL escape route parallels [Lattice-Based Methods Surpass Sum-of-Squares in Clustering](zadik-lattice-surpass-sos.md).
- Same crypto-to-learning arrow: [Cryptographic Hardness of Score Estimation](song-cryptographic-hardness-score-estimation.md).
- Frameworks and contrasts: [Statistical Query Model](../concepts/statistical-query-model.md), [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md), [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md), [Single-Index Model](../concepts/single-index-model.md).
- Authors: [Ilias Zadik](../entities/ilias-zadik.md), [Joan Bruna](../entities/joan-bruna.md).

## Open Questions / Limitations

- Noise is essential: the hardness disappears at exponentially small noise (Theorem 3.6) and the task is information-theoretically easy at small constant noise (Theorem 3.1).
- Bounded *adversarial* rather than Gaussian noise; closed by LZZ24.
- Conditional on a quantum lattice assumption, hence not comparable to unconditional SQ bounds.
- The one-hidden-layer ReLU statement is via approximation with residual error.
- Nothing prices an attacker; the adversary is an uncosted `beta`-bounded perturbation.

## Quotes / Notable Passages

> "Our result therefore extends the hardness of learning such functions from a restricted family of algorithms, such as gradient-based algorithms or SQ, to all polynomial-time algorithms by leveraging cryptographic assumptions"

> "we demonstrate the necessity of noise in the hardness result"

> "SQ lower bounds are unconditional because they are of an information-theoretic nature"
