---
title: Hidden Progress in Deep Learning - SGD Learns Parities Near the Computational Limit
type: source
date_ingested: 2026-08-22
authors: [Boaz Barak, Benjamin L. Edelman, Surbhi Goel, Sham Kakade, Eran Malach, Cyril Zhang]
venue: "NeurIPS 2022"
venue_evidence: "dblp search (q=Hidden Progress in Deep Learning SGD Learns Parities): NeurIPS 2022 inproceedings, plus CoRR abs/2207.08799"
year: 2022
tags: [learning-theory, statistical-query, sample-complexity, parity, feature-learning, statistical-computational-gaps]
claim_quantifier: empirical
antecedent: "Empirical Finding 1 holds for small instances (n <= 30, k <= 4) over the enumerated grid of architectures, initializations, batch sizes and learning rates. Theorem 4 requires sign-vector initialization, hinge loss, width r = Omega(2^k k log(k/eps)), batch size B = Omega(n^k log(n/eps)), k even, n odd. Theorems 6-7 require the disjoint-PolyNet architecture and the disjoint (n,k)-parity problem."
model_class: "(n,k)-sparse parity over the uniform Boolean hypercube: y = prod_{i in S} x_i, |S| = k, x ~ Unif({+-1}^n). Statistically easy (Theta(k log n) samples), conjectured to cost n^{Omega(k)} computation at any noise level o(1) (Alekhnovich 2003)."
algorithm_class: "SGD/GD on neural networks (2-layer MLPs, 1-neuron sinusoidal/zigzag nets, simplified Transformers, PolyNets); the lower bound cited is for statistical query algorithms (Kearns 1998), Omega(n^k) constant-noise queries"
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: time
cls_tightness: measured
cls_baseline: n/a
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: samples
cls_assessed: explicit
cls_evidence: "for small n, power law relationships tc ∝ nα·k (for small constants α) are observed for all configurations."
cls_evidence_src: Appendix C
cls_reason: "Not an attack paper: target/family/phase/access/write = none/none/n/a/none/none (rule 2). party=learner (rule 3): the bound binds SGD, not an adversary. unit=time for t_c, the iteration count Finding 1 reports. tightness=measured because Finding 1 is the abstract-led main claim (rule 1) and is claim_quantifier=empirical in front matter, unlike the theorem-led siblings in this batch. second_notion=samples records Theorem 4's own batch-size bound B=Omega(n^k log(n/eps)), a second internally-proven quantity on the same party (rule 4b). baseline=stated against the externally-cited n^Omega(k) SQ query lower bound (Kearns 1998); that comparison is external rather than a class this paper's own theorem is stated over, so it is recorded via baseline, not second_notion=algo class. Caution: the SQ bound is a conjecture for noiseless parity (Alekhnovich 2003), and Gaussian elimination solves noiseless parity outside SQ in poly(n) time (Claim Boundary), so this prices SGD against a restricted-class limit, not an unconditional one. This paper is Boolean/SQ-framed (Kearns 1998), not part of the Gaussian single-index information/generative-exponent line used elsewhere in this batch."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The paper studies how SGD on standard neural networks solves the (n,k)-sparse parity problem, a canonical discrete search problem that is statistically easy and computationally hard. Empirically, a wide range of architectures, initializations and batch sizes solve small instances (n <= 30, k <= 4) within c·n^{alpha·k} iterations, near the n^{Omega(k)} computational scaling that SQ lower bounds impose on gradient-based methods at constant noise. Training curves show long plateaus with no visible progress followed by a sharp phase transition to zero error.

The central claim is mechanistic. The convergence is not Langevin-like random search over parameters or subsets. Four black-box observations rule that out: convergence times adapt to k without any sparse prior; over 10^6 trials no run succeeds early, whereas exhaustive search would have geometrically distributed success times peaked at t = 0; convergence times are determined by the initialization, not the SGD sample randomness; and the power-law scaling breaks at larger n, which random search would not do. Instead, SGD amplifies the sparse solution gradually through a Fourier gap in the population gradient. At an all-ones initialization the population gradient's coordinates are Fourier coefficients of the majority function, and the order-(k-1) coefficients at the relevant coordinates exceed the order-(k+1) coefficients at irrelevant ones by gamma = Theta(n^{-(k-1)/2}), so the support S is recoverable from O~(1/gamma^2) = O~(n^{k-1}) samples. Progress is real but invisible to loss and error metrics, which the paper connects to emergent capabilities and grokking.

Two theorems convert the mechanism into convergence guarantees, and one theorem (Theorem 5) shows the low-width regime lies outside the NTK: any D-dimensional fixed embedding with DR^2 < epsilon^2 · binom(n,k) fails on some parity, so success requires feature learning.

## Claim Boundary

- **Quantified over:** the headline scaling t_c ∝ n^{alpha·k} is an empirical finding, quantified over the tested grid: n in {10,20,30}, k in {2,3,4}, batch sizes 1 to 1024, three initialization families, three losses, fifteen architecture configurations, learning rates in {0.001, 0.01, 0.1, 1}, with success defined as at least 20% of 25 trials converging. Theorems 4, 6, 7 are existential over hyperparameter schedules ("there exist a random initialization scheme, eta_t, and lambda_t") for specific architectures.
- **Antecedent and whether it holds:** the SQ lower bound the empirics are compared against is Omega(n^k) queries at constant noise (Kearns 1998); its application to gradient descent is via the SQ simulation of GD with bounded gradient precision, and holds for noisy parities. For noiseless parities the antecedent fails outside SQ: Gaussian elimination learns them in poly(n) time, so the "computational limit" in the title is the limit of the SQ class, not of all algorithms. The belief that noisy sparse parity costs n^{Omega(k)} is a conjecture (Alekhnovich 2003), not a theorem.
- **Does not establish:** (a) any lower bound — the paper proves upper bounds and cites the SQ bound; (b) that the n^{Theta(k)} scaling persists at large n. The paper itself documents the opposite: the power-law exponent worsens on larger instances (Figure 2 right), so the small-n fit does not extrapolate; (c) that SGD matches the SQ limit exactly — Theorem 4 needs batch size n^{Omega(k)}, at which the parity indices emerge in a single step, and Theorem 7 gives O~((n/k)^{2k-1}) iterations for the disjoint variant, above n^{k/2}-type scalings; (d) anything about noiseless-parity-specific non-SQ algorithms — Gaussian elimination is named as the escape and is not gradient-based.
- **Abstract vs theorem:** the abstract's "at approximately n^{O(k)} iterations; this nearly matches SQ lower bounds" is carried by the small-instance empirics; the theorems cover narrower settings (sign initialization + large batch for MLPs; the disjoint-PolyNet for arbitrary batch). The abstract does not mention the large-n elbow, which the body and appendix state plainly.

## Key Contributions

- Empirical Finding 1: for all small instances (n <= 30, k <= 4), SGD on all tested architectures solves the (n,k)-parity problem with probability >= 0.2 within c·n^{alpha·k} steps, for small constants c, alpha.
- Informal Theorem 2 (Theorem 4 formally): on 2-layer ReLU MLPs of width 2^{Theta(k)} — formally r = Omega(2^k k log(k/eps)) — with batch size n^{O(k)} — formally B = Omega(n^k log(n/eps)) — SGD with hinge loss and sign initialization reaches expected loss <= eps in at most O(k^3 r^2 n / eps^2) iterations. At this batch size the correct indices emerge in a single SGD step.
- Informal Theorem 3 (Theorems 6-7): on disjoint-PolyNets, SGD with any batch size B >= 1 reaches error <= eps within n^{O(k)}·log(1/eps) iterations — formally O~((n')^{2k-1} log(1/eps)) with n' = n/k; and gradient flow spends a 1 - O((n')^{1-k/2}) fraction of its time before convergence at error >= 49%, a proven loss plateau (Theorem 6).
- Definition 1 (Fourier gap) and Proposition 9: a gamma-Fourier gap at S in the population-gradient function allows recovery of S from O~(1/gamma^2) samples; for majority, gamma = Theta(n^{-(k-1)/2}) (Lemma 2).
- Theorem 5: no D-dimensional embedding Psi with sup_x ||Psi(x)|| <= 1 and weights of norm <= R fits all k-sparse parities to error better than 1 - eps when DR^2 < eps^2 · binom(n,k), placing the low-width results outside any fixed-kernel (NTK) regime, which needs size n^{Omega(k)}.
- Hidden progress measures: the weight movement norm ||w_t - w_0||_inf and directly measured Fourier gaps grow smoothly during the loss plateau, distinguishing feature amplification from training on noise.

## Key Empirical Details

- Reporting statistic: convergence times have high variance from unlucky initializations, so 10th percentile convergence times are reported (Figures 7, 9); the histogram over 10^6 trials (Figure 2 left) shows heavy upper tails and no early successes.
- Figure 2 center configuration: width-100 ReLU MLP dynamics shown at B = 128, eta = 0.01; loss curves are strongly correlated with initialization, concentrated conditional on it.
- The elbow: for larger n the log-log slope increases — with constant learning rate and standard training the n^{Theta(k)} scaling does not continue indefinitely (Figure 2 right; Appendix C discussion of the scaling fits, with the counterintuitive-roles discussion in C.2).
- Grokking appears at small fixed sample sizes (Figure 4 right): large gaps between time to zero train error and zero test error.

## Connections

- The SQ lower bound and its interpretation: [Statistical Query Model](../concepts/statistical-query-model.md), [CSQ model](../concepts/csq-model.md).
- The information/leap-exponent line prices the same search for Gaussian data: [information-exponent-online-sgd](information-exponent-online-sgd.md), [leap-complexity-sgd](leap-complexity-sgd.md); sparse parity is the Boolean k-index instance, and the k = 2 case is settled at d·polylog(d) by [sgd-xor-near-optimal](sgd-xor-near-optimal.md).
- Batch reuse changes the class and the answer: [reusing-batches-breaks-exponents](reusing-batches-breaks-exponents.md), [repetita-iuvant-data-repetition](repetita-iuvant-data-repetition.md), [sgd-reuse-info-theoretic-limit](sgd-reuse-info-theoretic-limit.md). This paper's fresh-batch online setting is the regime those works step out of.
- Parameter-efficiency rather than sample-efficiency for the same target: [transformers-sparse-xor-polylog](transformers-sparse-xor-polylog.md) cites this paper's Omega(d^2) single-step-GD sample requirement as the FFNN baseline.
- Streaming/memory hardness of parity: [raz-parity-time-space](raz-parity-time-space.md) (the paper cites Kol et al. 2017 for streaming hardness).
- Noisy parity as a cryptographic assumption: the paper cites Alekhnovich 2003 and LPN-based schemes, connecting to [average-case-parity-problems](average-case-parity-problems.md).

## Open Questions / Limitations

- Fourier gaps ("Fourier anti-concentration" lower bounds on degree-(k-1) coefficients) for population gradients other than majority are open; the paper's empirics suggest they are present at general initializations and along the SGD path, and that the gap grows during training, which the theory does not capture.
- Theorem 4 does not cover small batches, uniform or Gaussian initialization, or losses other than hinge, all of which work empirically.
- The large-n elbow is unexplained: whether an adaptive learning-rate schedule restores n^{Theta(k)} scaling at large n is left open.
- The threshold-vs-scaling question for model size: success time improves with width (parallelization with diminishing returns, Figure 4 left) rather than jumping at a capacity threshold.

## Quotes / Notable Passages

> "Instead, we show that SGD gradually amplifies the sparse solution via a Fourier gap in the population gradient, making continual progress that is invisible to loss and error metrics."

> "Beyond the restricted computational model of statistical queries, noiseless parities can be learned in poly(n) time via Gaussian elimination."

> "for small n, power law relationships tc ∝ nα·k (for small constants α) are observed for all configurations. Note that for larger n, the exponent (i.e. the slope in the log-log plot) increases: with a constant learning rate and standard training, the nΘ(k) does not continue indefinitely." (Appendix C; superscripts flattened by extraction: t_c ∝ n^{alpha·k}, n^{Theta(k)})

> "tc exhibits high variance due to unlucky initializations (see Figure 8); thus, we report 10th percentile convergence times."

> "Histograms of convergence times over 106 random trials, with heavy upper tails but no observed successes near t = 0 (unlike random search)." (Figure 2 caption; 10^6 flattened by extraction)
