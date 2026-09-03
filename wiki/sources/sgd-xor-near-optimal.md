---
title: SGD Finds then Tunes Features in Two-Layer Neural Networks with Near-Optimal Sample Complexity - A Case Study in the XOR Problem
type: source
date_ingested: 2026-08-22
authors: [Margalit Glasgow]
venue: "ICLR 2024"
venue_evidence: "https://proceedings.iclr.cc/paper_files/paper/2024/file/e6d37cc5723e810b793c834bcb6647cf-Paper-Conference.pdf; official ICLR 2024 proceedings, also OpenReview https://openreview.net/forum?id=HgOJlxzB16"
year: 2024
tags: [learning-theory, sample-complexity, parity, feature-learning, leap-complexity, minibatch-sgd]
claim_quantifier: universal
antecedent: "Boolean data x ~ Unif({-1,1}^d) labeled by the 2-sparse XOR y = -x_1 x_2 (rotationally invariant algorithm, so any basis); 2-layer ReLU network of width 1/theta <= p <= d^C with theta = 1/log^C(d), both layers trained simultaneously by online minibatch SGD on the logistic loss with minibatch size m >= d/theta, step size d^{-C} <= eta <= theta, initialization scale theta/sqrt(p); fresh samples at every step"
model_class: "k = 2 XOR (2-sparse parity) on the Boolean hypercube; leap complexity L = 2, degree D = 2. NOT general k-sparse parity, NOT Gaussian data, NOT regression."
algorithm_class: "standard online minibatch SGD, both layers trained simultaneously, logistic loss; minibatch size d·polylog(d) with fresh samples per step (no batch reuse); batch size 1 is open"
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: samples
cls_tightness: exponent
cls_baseline: n/a
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: algo class
cls_assessed: explicit
cls_evidence: "we can learn the XOR function up to ǫ population loss in Θ (dpolylog(d)) samples and iterations on a polynomial-width network"
cls_evidence_src: "§3, restating Thm 3.1"
cls_reason: "Not an attack paper: target/family/phase/access/write = none/none/n/a/none/none. party=learner (rule 3): the bound binds the minibatch-SGD-trained two-layer network, not an adversary. unit=samples/tightness=exponent for Theorem 3.1's explicit Theta(d polylog d) sample-and-iteration threshold. second_notion=algo class records footnote 1's own class-relative yardstick, 'for algorithms that are rotationally invariant, Theta~(d) samples are required', a symmetry class the paper's own algorithm and initialization satisfy by construction (Remark 2.1), not an SQ/CSQ class. baseline=stated against that same footnote-1 floor. This is an ESTIMATION result (o(1) population loss on the learned classifier), stated explicitly in the page's own Detection versus estimation section, placing it alongside sgd-reuse-info-theoretic-limit rather than the weak-recovery-only learning-rate-induces-generative-exponent, both in this same batch. This is the k=2 Boolean-hypercube instance of the leap-complexity conjecture Theta~(d^{max(L-1,1)}), confirmed here with a fully standard algorithm; it is not itself an information- or generative-exponent result on Gaussian data."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The paper proves that standard minibatch SGD, training both layers of a polynomial-width two-layer ReLU network simultaneously on the logistic loss, learns the Boolean XOR function y = -x_1 x_2 to o(1) population error in Theta(d·polylog(d)) samples and iterations (Theorem 3.1). This is the first Theta~(d) guarantee for XOR on a standard architecture with standard training: prior Theta~(d) results either found the global optimum or trained infinite-width networks (Wei et al.), used quadratic-NTK constructions with modified architecture and training (Bai-Lee, Chen et al.), or assumed knowledge of the coordinate system and hence were not rotationally invariant (Abbe et al. 2023). The NTK itself needs Theta(d^2). Footnote 1 fixes the optimality yardstick: Theta~(d) samples are required for rotationally invariant algorithms, so d·polylog(d) is near-optimal within that class.

The analysis splits SGD's trajectory into two phases. In the signal-finding phase the network is small, the loss is approximated by its linearization at zero output, and neurons evolve nearly independently; a sufficient fraction escape the saddle at initialization and align with the signal directions mu_1, mu_2. In the signal-heavy phase, an inductive hypothesis maintains that signal components dominate, and the simultaneous training of both layers does real work: neurons whose first-layer weight is signal-heavy grow large second-layer weights, and the resulting positive feedback amplifies exactly those neurons. If only the first layer were trained, non-signal components could grow at the same order as signal components.

Within the leap framework, XOR is the k = 2, L = 2 instance, and the result confirms the Theta~(d^{max(L-1,1)}) conjecture of Abbe et al. at this instance with a fully standard algorithm.

## Claim Boundary

- **Quantified over:** one target function class — the 2-sparse XOR on the Boolean hypercube in any basis (the algorithm and initialization are rotationally invariant, Remark 2.1) — for all widths, step sizes and batch sizes in the stated polylogarithmic-to-polynomial windows. The guarantee is a high-probability (1 - d^{-omega(1)}) statement for large d.
- **Antecedent and whether it holds:** minibatch size m >= d/theta = d·polylog(d) with fresh samples at each of the ~C log(d)/eta steps. The claimed total of Theta(d·polylog d) samples comes from setting eta = theta and m = d/theta. The batch size is load-bearing: it gives per-step concentration to the population gradient, and the paper states that extending to batch size 1 is open.
- **Does not establish:** (a) anything for k >= 3 parities or general multi-index functions — this is k = 2 only, and the L >= 2, k >= 2 general case remains governed by the (then-)conjectured Theta~(d^{max(L-1,1)}) of the leap papers; (b) Gaussian data — the discussion states the results hold only for Boolean data, Phase 1 could plausibly extend, and the author knows no direct extension of Phase 2 to the Gaussian case because imbalanced cluster margins could grow wsig in the wrong direction; (c) regression — the classification margin argument does not carry over, and on Gaussian data regression would require neuron specialization the analysis does not provide; (d) GD on a fixed empirical loss — uniform convergence of the empirical gradient would cost Omega(d^2) samples, so the fresh-minibatch result is stronger than what uniform-convergence tooling can give.
- **Abstract vs theorem:** consistent. The abstract's "dpolylog(d) samples" and "standard minibatch SGD" match Theorem 3.1; "population error o(1)" is what is proven (expected logistic loss o(1), which bounds classification error).

## Key Contributions

- Theorem 3.1: with theta = 1/log^C(d), width 1/theta <= p <= d^C, minibatch size m >= d/theta, step size d^{-C} <= eta <= theta, initialization scale theta/sqrt(p), some t <= C log(d)/eta has E_x[l_{rho_t}(x)] <= o(1) with probability 1 - d^{-omega(1)}; instantiated at eta = theta, m = d/theta this is Theta(d polylog d) samples and iterations.
- The two-phase mechanism (signal-finding then signal-heavy) with the simultaneous-layer feedback argument; Remark 4.3 records why layer-wise training would break the balance argument.
- Escaping the saddle takes super-constant time, which rules out mean-field and SDE-limit approaches that break down after constant time; the analysis tracks the dynamics directly.

## Detection versus estimation, and the class of the bound

The guarantee is an estimation result: o(1) population loss on the learned classifier, not weak recovery or detection of the relevant coordinates. The near-optimality claim is class-relative in a different way from SQ statements: the Theta~(d) floor invoked in footnote 1 binds rotationally invariant algorithms (a symmetry class, not a query class); a coordinate-aware algorithm can do better on the Boolean hypercube, which is exactly how Abbe et al. 2023 achieve their complexity without rotational invariance. No computational lower bound is proven in the paper.

## Connections

- Confirms at k = L = 2 the conjectured SGD complexity of [leap-complexity-sgd](leap-complexity-sgd.md) with a standard algorithm; the general conjecture Theta~(d^{max(L-1,1)}) is separate and was later disproved for batch-reusing algorithms by [reusing-batches-breaks-exponents](reusing-batches-breaks-exponents.md).
- The k-sparse parity phase-transition phenomenology this sharpens at k = 2: [hidden-progress-sgd-parities](hidden-progress-sgd-parities.md) (whose one-step analyses need Omega(d^L) samples, as this paper notes).
- Cited as the model for "standard multi-pass SGD" in the open problem of [sgd-reuse-info-theoretic-limit](sgd-reuse-info-theoretic-limit.md); note the regimes differ — this paper uses fresh minibatches (online), not batch reuse.
- Parameter-efficiency counterpart on the same target: [transformers-sparse-xor-polylog](transformers-sparse-xor-polylog.md) cites this result as the Omega(d)-parameter FFNN baseline at d·polylog(d) samples.
- Concepts: [leap complexity](../concepts/leap-complexity.md), [multi-index model](../concepts/multi-index-model.md), [information exponent](../concepts/information-exponent.md).

## Open Questions / Limitations

- Batch size 1 (pure online SGD) is open; drift-martingale techniques are suggested.
- Gaussian data: Phase 1 plausibly extends; Phase 2 has no known extension.
- Regression and neuron specialization beyond the four-cluster classification geometry are open.
- k >= 3 and general L >= 2 multi-index targets are untouched by this technique.

## Quotes / Notable Passages

> "To our knowledge, this work is the first to give a sample complexity of Õ(d) for efficiently learning the XOR function on isotropic data on a standard neural network with standard training."

> "we can learn the XOR function up to ǫ population loss in Θ (dpolylog(d)) samples and iterations on a polynomial-width network" (extraction glyphs: ǫ is the PDF's varepsilon, and the spacing flattens Theta(d polylog(d)))

> "We consider this near-optimal in the sense that for algorithms that are rotationally invariant, Θ̃(d) samples are required." (footnote 1)

> "One limitation of this work is that our results only hold for boolean data, and not gaussian data"

> "Extending our results to SGD with a batch size of 1 is an interesting open question"
