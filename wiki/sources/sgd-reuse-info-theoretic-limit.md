---
title: Neural Network Learns Low-Dimensional Polynomials with SGD Near the Information-Theoretic Limit
type: source
date_ingested: 2026-08-22
authors: [Jason D. Lee, Kazusato Oko, Taiji Suzuki, Denny Wu]
venue: venue unconfirmed from PDF (arXiv:2406.01581v2 [cs.LG], 22 Dec 2024; catalogued in this corpus as NeurIPS 2024)
year: 2024
tags: [learning-theory, sample-complexity, single-index-model, generative-exponent, statistical-query, csq, batch-reuse]
claim_quantifier: universal
antecedent: "Gaussian single-index model y = sigma*(<x, theta>) + noise with x ~ N(0, I_d); for the headline Theta(d polylog d) result, sigma* is an arbitrary degree-q polynomial (Assumption 1); the network is the specific two-layer model (3.1) with randomized Hermite-polynomial activations satisfying Assumptions 2-3, trained by Algorithm 1 (layer-wise, normalized projected SGD with interpolation, each minibatch reused for exactly two steps)"
model_class: "Gaussian single-index target f*(x) = sigma*(<x, theta>), information exponent p, generative exponent p* (Damian et al. 2024). For polynomial sigma*, p* <= 2. NOT multi-index; NOT general non-polynomial links for the linear-sample claim."
algorithm_class: "SGD-based: two-layer network, Phase I normalized projected SGD on first layer with each fresh batch reused in two consecutive steps plus an interpolation (negative-momentum-like) step, Phase II ridge regression on second layer. The point of the analysis is that this sits in SQ but outside CSQ."
---

## Summary

The paper proves that a two-layer neural network trained by an SGD-based algorithm on the squared loss learns arbitrary polynomial Gaussian single-index targets with sample and runtime complexity n ≃ T = Theta(d·polylog d), matching the information-theoretic limit n ≍ d up to polylogarithmic factors. More generally, n = Theta~(d^{(p*-1) ∨ 1}) samples suffice, where p* is the generative exponent of the link — so the complexity is governed by p*, not by the information exponent p, and since p can exceed p* arbitrarily, this disproves the conjecture of Abbe et al. (2023) that n ≍ d^{p/2} is optimal for ERM with SGD on the squared/correlation loss.

The mechanism is batch reuse. Two consecutive gradient steps on the same minibatch produce, in the second step, a term in which the label passes through the activation's derivative — an implicit nonlinear label transformation that a correlational statistical query learner cannot make. Proposition 6 shows monomial transformations suffice: for any degree-<=q polynomial link there is i <= C_q with IE(g^i) <= 2, and IE(g^i) = 1 when g is not even. These transformations are extractable from the SGD update by Taylor expansion, which is what the thresholding transformations of the earlier SQ algorithm (Chen-Meka) are not. The paper thereby closes the gap left by Dandi et al.'s two-step weak-recovery result: it handles arbitrary polynomial links, and converts weak recovery into strong recovery and a generalization bound (Theorems 1, 2, Proposition 5): weak recovery after 2T_{1,1} = C(q)·d·polylog(d) steps, strong recovery (<w, theta> > 1 - eps) after Theta~(d/eps^2) more, then second-layer ridge regression gives population squared error O(eps^2), with total n = T ≍ C(q)(d eps^{-2} ∨ eps^{-8}) polylog(d).

The paper is explicit that the CSQ-to-SGD correspondence it escapes is heuristic in both directions: CSQ lower bounds are translated to sample complexity via tau ≈ n^{-1/2}, and "strictly speaking, the CSQ model does not include empirical risk minimization with gradient descent."

## Claim Boundary

- **Quantified over:** all polynomial link functions sigma* of degree q (the constant hidden in Theta depends on q, exponentially); more generally all links with generative exponent p*, giving n = Theta~(d^{(p*-1) ∨ 1}). Quantified over the specific Algorithm 1, not over SGD variants generally.
- **Antecedent and whether it holds:** the network and algorithm are non-standard in load-bearing ways: layer-wise training (first layer, then second), normalized and projected gradient steps, an interpolation step with momentum parameter xi, activations that are random polynomial combinations of Hermite polynomials up to degree C_sigma (Assumptions 2-3, satisfied by an exp(-Theta(q)) fraction of neurons under the Lemma 4 randomization), vanishing second-layer initialization, and a fixed schedule that reuses each fresh batch exactly twice. These are constructions, not descriptions of standard practice; the paper itself poses standard simultaneous multi-pass SGD as an open question and cites Glasgow's XOR analysis as the model for it.
- **Does not establish:** (a) that standard multi-pass SGD training all parameters simultaneously achieves the same efficiency — stated open in the conclusion; (b) optimality for p* > 2: the upper bound d^{p*-1} does not match the full-SQ lower bound d^{p*/2} of Damian et al. 2024, it is the SQ analogue of the online-SGD d^{p-1} rate, so a gap of the same shape recurs one level up; (c) anything for multi-index targets, hierarchical targets, or non-Gaussian data; (d) any lower bound — the CSQ barrier it "breaks" binds the CSQ class, and the escape is by exiting the class, not by contradicting the bound.
- **Abstract vs theorem:** the abstract's "matches the information theoretic limit up to polylogarithmic factors" is accurate for polynomial links at constant target error; the eps-dependence (n ≍ d eps^{-2} ∨ eps^{-8}) and the exponential-in-q constant C(q) appear only in the body. The abstract states the theorem's algorithm as "an SGD-based algorithm", which is fair notice that it is not vanilla SGD.

## Key Contributions

- Main theorem (informal, Section 1.1): a shallow network with N = Theta~(1) neurons learns arbitrary single-index models to o(1) population loss with n, T = Theta~(d^{(p*-1) ∨ 1}); for polynomial links (p* <= 2), n = Theta(d·polylog d).
- Theorem 1 (weak recovery): after 2T_{1,1} = C(q)·d·polylog(d) Phase-I steps, a Theta~(N) subset of neurons has overlap > c >= 1/polylog(d) with theta, from overlap ≈ d^{-1/2} at initialization.
- Theorem 2 (strong recovery): Theta~(d/eps^2) further steps bring overlap above 1 - eps.
- Proposition 5 (generalization): Phase-II ridge regression achieves population squared error O(eps^2) with T_2 = C(q) N^4 polylog(d) eps^{-4}, N = C(q) polylog(d) eps^{-1}.
- Proposition 6 (monomial transformations): for any degree-q polynomial g, some power g^i with i <= C_q has information exponent <= 2, and = 1 if g is not even; the required degree is uniformly bounded via compactness.
- Disproof of the Abbe et al. 2023 conjecture that d^{p/2} is optimal for ERM-SGD on the squared loss; the correct governing quantity is the generative exponent.

## Detection versus estimation, and the class of the bound

The result is an estimation upper bound: strong recovery of theta plus a population-loss guarantee, not merely weak recovery or detection. The barriers discussed are class-relative: the d^{p/2} lower bound binds CSQ algorithms (with the heuristic tau ≈ n^{-1/2} translation), and the d^{p*/2} lower bound binds full SQ; neither is a bound on all polynomial-time algorithms. No unconditional hardness enters anywhere in the paper.

## Connections

- Defines its unit against [generative-exponent-single-index](generative-exponent-single-index.md) (Damian et al. 2024, whose SQ/LDP lower bound d^{p*/2} it cites as the target) and [information-exponent-online-sgd](information-exponent-online-sgd.md) (Ben Arous et al., the d^{p-1} online-SGD rate it upgrades).
- The batch-reuse mechanism is the same as [reusing-batches-breaks-exponents](reusing-batches-breaks-exponents.md) (Dandi et al. 2024, cited as [DTA+24]), whose weak-recovery-only, example-specific analysis this paper generalizes; and as [repetita-iuvant-data-repetition](repetita-iuvant-data-repetition.md) (Arnaboldi et al., acknowledged as independent and simultaneous, weak recovery with similar complexity).
- The CSQ conjecture disproved is from [leap-complexity-sgd](leap-complexity-sgd.md) (Abbe et al. 2023).
- The full-SQ algorithm matched is Chen-Meka [CM20]; concepts: [CSQ model](../concepts/csq-model.md), [Statistical Query Model](../concepts/statistical-query-model.md), [generative exponent](../concepts/generative-exponent.md), [information exponent](../concepts/information-exponent.md), [single-index model](../concepts/single-index-model.md).
- Contrast: [full-batch-gd-vs-one-pass-sgd](full-batch-gd-vs-one-pass-sgd.md) notes that for even links (p* = 2) the two-pass label-transformation mechanism cannot remove the remaining log d factor, and locates the residual gain in full-batch reuse instead.

## Open Questions / Limitations

- Standard multi-pass SGD, all parameters trained simultaneously, is open (stated in the conclusion).
- p* > 2: upper bound d^{p*-1} vs SQ lower bound d^{p*/2}; whether SGD-like algorithms close this is open.
- Extensions to multi-index and hierarchical targets are named as future directions.
- C(q) grows exponentially with the link degree q.

## Quotes / Notable Passages

> "Core to our analysis is the reuse of minibatch in the gradient computation, which gives rise to higher-order information beyond correlational queries."

> "strictly speaking, the CSQ model does not include empirical risk minimization with gradient descent, due to the non-adversarial noise and existence of non-correlational terms in the gradient computation"

> "this dimension dependence matches the information theoretic limit up to polylogarithmic factors"

> "the SGD algorithm that we employ requires a layer-wise training procedure and a specific batch reuse schedule; one may therefore ask if standard multi-pass SGD training of all parameters simultaneously [Gla23] (as reported in Figure 1) also achieves the same statistical efficiency."
