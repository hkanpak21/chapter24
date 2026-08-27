---
title: On the Hardness of Learning One Hidden Layer Neural Networks
type: source
date_ingested: 2026-08-20
authors: [Shuchen Li, Ilias Zadik, Manolis Zampetakis]
venue: venue unconfirmed from PDF (arXiv:2410.03477v1 [cs.LG], 4 Oct 2024)
year: 2024
tags: [cryptography, hardness-reductions, continuous-lwe, lattice-cryptography, learning-theory, one-way-functions]
claim_quantifier: conditional
antecedent: "Conditional on the quantum worst-case hardness of approximating GapSVP within polynomial factors (Conjecture 2.3), routed through CLWE (Theorem 2.4, imported from Bruna-Regev-Song-Tang). Requires width k = omega(sqrt(d log d)) and Gaussian label noise of variance sigma = poly(d)^{-1}."
model_class: "Width-k one-hidden-layer ReLU networks f(x) = sum_i a_i (<x_i, w_i> + b_i)_+ over standard Gaussian inputs N(0, I_d), with i.i.d. Gaussian label noise N(0, sigma^2). Target: weak learning (edge inverse-polynomial in d)."
algorithm_class: "ALL polynomial-time estimators (conditional on the lattice assumption); explicitly stronger than the cSQ lower bounds it supersedes"
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
cls_second_party: none
cls_assessed: explicit
cls_evidence: "no polynomial-time estimator can weakly learn the class of one hidden layer neural networks under arbitrary polynomially small Gaussian noise"
cls_evidence_src: "§3, after Thm 3.1"
cls_reason: "Same shape as its direct predecessor hardness-single-periodic-neurons: party=learner (rule 3, the bound binds the estimator, conditional on CLWE/GapSVP), unit=time, tightness=poly, baseline=stated from Definition 2.1's trivial-loss/edge weak-learning formulation (verified present in raw/LZZ24_HardnessOneHiddenLayer.pdf). second_party=none here, unlike the predecessor's second_party=perturbation: the noise in this paper is Gaussian, not adversarial, and the Summary states directly that nothing prices an attacker, the noise is 'a distributional nuisance, not a party with a budget.'"
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper closes the gap left by [Song–Zadik–Bruna](hardness-single-periodic-neurons.md) and shows that learning **one**-hidden-layer ReLU networks over standard Gaussian inputs with polynomially small **Gaussian** noise is hard for all polynomial-time algorithms, conditional on CLWE and hence on the quantum worst-case hardness of GapSVP. The prior picture had hardness for `>= 2` hidden layers (Chen et al., Daniely–Vardi) and for one hidden layer only under bounded *adversarial* noise (SZB21, and via approximation rather than natively); the intermediate case was, in Chen et al.'s words, a main open question.

Two steps do the work. First, Theorem 4.2 improves SZB21's Theorem 3.3 by "Gaussianizing" the adversarial noise: injecting additional Gaussian noise of appropriate variance into the labels produced by the SZB21 reduction turns bounded adversarial noise into Gaussian noise (Lemma 4.1), so CLWE reduces to learning Lipschitz periodic neurons under polynomially small Gaussian noise. Second, instead of using approximation results to move from periodic neurons to ReLU networks (which would reintroduce error too large for the Gaussianization to absorb), Lemma 5.1 explicitly constructs, for any bounded interval `[-R, R]`, a Lipschitz periodic neuron and a polynomial-width ReLU network that **exactly agree** on that interval — zero approximation error. Gaussian tails then handle the rest.

The main statement, Theorem 3.1 / 5.4: for `sigma = poly(d)^{-1}`, `eps = poly(d)^{-1}`, `k = omega(sqrt(d log d))`, a polynomial-time `eps`-weak learner for `F_k^{NN}` under `N(0, sigma^2)` noise implies a polynomial-time quantum algorithm approximating GapSVP within polynomial factors. Composing with CLWE-to-LWE reductions extends this to any `sigma` with `log(1/sigma) = poly(d)` and `k = omega(sqrt(d log d) · log(d/sigma))`, giving a `poly(1/sigma, d)` GapSVP factor. Since the state-of-the-art GapSVP algorithm is LLL with factor `exp(Theta(d))`, any learner succeeding for `sigma >= exp(-o(sqrt(d)))` would be a major lattice breakthrough.

Like SZB21, this prices the **learner**. Nothing here prices an attacker: the noise is a distributional nuisance, not a party with a budget.

## Claim Boundary

- **Quantified over:** all polynomial-time estimators, for the width-`k` one-hidden-layer ReLU class with `k = omega(sqrt(d log d))`, under Gaussian label noise; the target is *weak* learning (Definition 2.1), which is the weakest possible objective and therefore the strongest form of lower bound.
- **Model class and data assumption:** standard Gaussian inputs, ReLU activation, one hidden layer, polynomial width. There is a **width floor**: `k = omega(sqrt(d log d))`. Narrow networks are not covered. Noise must be Gaussian and polynomially small (or, in the extension, with `log(1/sigma) = poly(d)`).
- **Algorithm class:** all polynomial-time algorithms — but conditionally. The paper motivates the strengthening precisely by the weakness of cSQ: "The cSQ model is known in many settings to be underperforming compared to multiple other natural polynomial-time methods ..., which arguably limits the generality of such an unconditional lower bound."
- **Does not establish:** (a) unconditional hardness; (b) hardness at exponentially small noise. The paper explicitly leaves that open and notes that brittle LLL-based algorithms *do* succeed there for the cosine neuron (SZB21) and in several other noiseless settings; (c) hardness for width below `omega(sqrt(d log d))`; (d) any statement about an adversary's resources.
- **Abstract vs theorem:** none found. The abstract lists the three conditions ("(1) the size of the neural network is polynomial in d, (2) its input distribution is a standard Gaussian, and (3) the noise is Gaussian and polynomially small in d") and names the assumption. The width floor `k = omega(sqrt(d log d))` appears in Theorem 1.1 but not in the abstract's numbered list — mild, and Theorem 1.1 is on the same page.

## Key Contributions

- Lemma 4.1 ("Gaussianization"): converting bounded adversarial label noise into Gaussian label noise by injecting extra Gaussian noise, improving SZB21's reduction.
- Theorem 4.2 / Corollary 4.3: CLWE reduces to learning Lipschitz periodic neurons under polynomially small *Gaussian* noise.
- Lemma 5.1: exact agreement on `[-R, R]` between a Lipschitz periodic neuron and a polynomial-width one-hidden-layer ReLU network — zero approximation error, removing the residual error of the SZB21 route.
- Theorem 3.1 / Theorem 5.4: cryptographic hardness of weakly learning width-`k` one-hidden-layer ReLU networks under Gaussian noise, `k = omega(sqrt(d log d))`.
- The extension via CLWE-to-LWE (Gupte–Vafa–Vaikuntanathan) to arbitrary `sigma` with `log(1/sigma) = poly(d)`, and the observation that `sigma >= exp(-o(sqrt(d)))` learners would beat LLL.

## Key Definitions / Theorems

**Theorem 1.1 (Informal), verbatim:**

> "Let ℱ𝑘 the class of width a 𝑘 one hidden layer neural networks and arbitrary noise variance 𝜎 “ 1{polyp𝑑q. For any 𝑘 “ 𝜔p 𝑑 log 𝑑q, if there exists a polynomial-time algorithm that can weakly learn ℱ𝑘 under Gaussian noise of variance 𝜎 then there exists a polynomial-time quantum algorithm that approximates GapSVP within a polyp𝑑q factor."

(The PDF extraction mangles the square-root sign; the condition is `k = omega(sqrt(d log d))`.)

**Theorem 3.1, verbatim:**

> "Let 𝑑 P ℕ, and arbitrary 𝜎 “ polyp𝑑q´1 , 𝜀 “ polyp𝑑q´1 , and 𝑘 “ 𝜔p 𝑑 log 𝑑q. Then a polynomial-time estimator that 𝜀-weakly learns the function class ℱ𝑘NN over Gaussian inputs"

> "𝑥 „ 𝑁p0, 𝐼 𝑑 q under Gaussian noise 𝜉 „ 𝑁p0, 𝜎 2 q implies a polynomial-time quantum algorithm that approximates GapSVP to within polynomial factors."

**Definition 2.1 (Weak learning).** `L_{D_f}(h_d) <= L_{D_f}(E[f(x)]) - eps` w.p. `>= 1 - delta`; trivial loss `= Var(f(Z))`; edge `eps` inverse-polynomial, `delta = 1/3`.

**Lipschitz periodic neurons, Eq. (4.1):** `F_gamma^phi = {f : R^d -> [-1,1] | f(x) = phi(gamma <w,x>), w in S^{d-1}}` with `phi` 1-Lipschitz and 1-periodic.

**Theorem 2.4 (imported CLWE-to-GapSVP reduction).** Cited as Bruna et al., Corollary 3.2, for `beta = 1/poly(d)`, `2 sqrt(d) <= gamma = poly(d)`.

## Connections

- Direct predecessor and the reduction it improves: [On the Cryptographic Hardness of Learning Single Periodic Neurons](hardness-single-periodic-neurons.md).
- Underlying assumption: [Continuous LWE](bruna-continuous-lwe.md); concept pages [Continuous LWE](../concepts/continuous-lwe.md), [Learning With Errors](../concepts/learning-with-errors.md), [LLL Algorithm](../concepts/lll-algorithm.md).
- Contrast class it supersedes: cSQ lower bounds for one-hidden-layer networks; see [CSQ Model](../concepts/csq-model.md) and, for the CSQ-priced picture, [SGD Learning on Neural Networks: Leap Complexity](leap-complexity-sgd.md).
- Same arrow (crypto to learning): [Cryptographic Hardness of Score Estimation](song-cryptographic-hardness-score-estimation.md).
- Concepts: [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md), [One-Way Functions](../concepts/one-way-functions.md), [Statistical Query Model](../concepts/statistical-query-model.md).
- Authors: [Ilias Zadik](../entities/ilias-zadik.md), [Manolis Zampetakis](../entities/manolis-zampetakis.md).

## Open Questions / Limitations

- Exponentially small noise `sigma` is left open — and brittle LLL-based algorithms are known to succeed in analogous noiseless settings, so the answer may well be positive.
- Width floor `k = omega(sqrt(d log d))`.
- Conditional on a quantum lattice assumption.
- The authors note the practical value of "brittle" exponentially-small-noise algorithms "is unfortunately unclear since a non-negligible amount of noise always exists".
- Nothing prices an attacker; only the learner is priced.

## Quotes / Notable Passages

> "we establish that under the CLWE assumption from cryptography [Bru+21] learning the class of one hidden layer neural network with polynomial small Gaussian noise is indeed computationally hard"

> "The cSQ model is known in many settings to be underperforming compared to multiple other natural polynomial-time methods"

> "one could argue that the computational hardness arises exactly because of the addition of adversarial noise and may not be inherent to learning one hidden layer neural networks"
