---
title: "Lower Bounds for Adversarially Robust PAC Learning"
type: source
date_ingested: 2026-05-07
authors: [Dimitrios I. Diochnos, Saeed Mahloujifar, Mohammad Mahmoody]
venue: "arXiv:1906.05815 (2019)"
year: 2019
tags: [adversarial-ml, PAC-learning, sample-complexity, concentration-of-measure, learning-theory, evasion-attacks, poisoning-attacks]
---

## Summary

This paper initiates a formal study of PAC learning under *error-region* evasion attacks — where the adversary's goal is to misclassify the perturbed instance under the *true label of the perturbed point*, i.e., $h(\tilde{x}) \neq c(\tilde{x})$. This is distinct from the *corrupted-input* notion used in all prior robust PAC learning work (Madry, Attias, Bubeck, Montasser, Cullina), where the adversary succeeds if $h(\tilde{x}) \neq c(x)$ using the original label. For natural image distributions the two notions coincide; in general they can diverge, and the distinction drives an exponential separation in sample complexity.

The paper proves two main results. First, for any realizable learning problem over a Normal Lévy family input space with an $\alpha$-close concept class, PAC learning robust to sublinear perturbations requires exponentially many samples in $n$, even though the same problem is PAC learnable with polynomially many samples without an adversary. Second, under *hybrid attacks* (a poisoning phase followed by an evasion phase), PAC learning is sometimes *impossible* altogether, even for concept classes with VC dimension bounded by $n$.

## Key Contributions

- **Definitional clarification**: Distinguishes error-region adversarial risk ($h(\tilde{x}) \neq c(\tilde{x})$) from corrupted-input risk ($h(\tilde{x}) \neq c(x)$). All prior polynomial-overhead results used corrupted-input; this paper shows error-region requires exponential overhead.
- **Theorem 3.4 — Exponential lower bound (Part 1a)**: For any realizable problem satisfying the two conditions below, any PAC learner robust against all sublinear $b = o(n)$ perturbation budgets requires sample complexity $m \geq 2^{\Omega(n)}$.
- **Theorem 3.4 — Super-polynomial lower bound (Part 1b)**: For perturbation budget $b = \tilde{O}(\sqrt{n})$, robust PAC learning requires $m \geq n^{\omega(1)}$ samples.
- **Theorem 3.4 — Hybrid attack impossibility (Part 2)**: If a poisoner can remove even a $1/n^{10}$ fraction of training examples, a subsequent evasion attacker with budget $\tilde{O}(\sqrt{n})$ renders PAC learning *impossible regardless of sample complexity*, even when VC dimension is $\leq n$.
- **Lemma 3.5 — Quantitative lower bound**: For tampering budget $b = \rho \cdot n$ with $\rho = o(1)$, any PAC learner requires $m(n) \geq 2^{\Omega(\rho^2 \cdot n)}$ samples.

## Two Conditions for the Main Theorem

The result applies to any realizable classification problem $\mathcal{P}_n = (\mathcal{X}, \mathcal{Y}, \mathcal{C}, D, \mathcal{H})$ satisfying:

**Condition 1 — Normal Lévy family**: The input space $(\mathcal{X}_n, \mathsf{d}_n, D_n)$ is a Normal Lévy family with concentration function $\alpha_n(b) \leq k_1 \cdot e^{-k_2 b^2/n}$. Examples: isotropic Gaussian in $\mathbb{R}^n$ under $\ell_2$, uniform on $\{0,1\}^n$ under Hamming, uniform on the $n$-sphere, any product distribution under Hamming.

**Condition 2 — $\alpha$-close concept class (Definition 3.3)**: For all $\alpha \in [2^{-\Theta(n)}, 1]$, there exist $c_1, c_2 \in \mathcal{C}$ with $\Pr_{x \leftarrow D}[c_1(x) \neq c_2(x)] = \alpha$. Examples: halfspaces in $\mathbb{R}^n$ under Gaussian; monotone conjunctions $c_1 = x_1 \wedge \cdots \wedge x_{k-1}$ vs. $c_2 = x_1 \wedge \cdots \wedge x_k$ under uniform on $\{0,1\}^n$ (disagreement $2^{-k}$); homogeneous halfspaces.

## Key Definitions / Theorems

**Error-region adversarial risk (Definition 2.1)**:
$$\text{AdvRisk}_\mathcal{A}(D, c, h) = \Pr_{x \leftarrow D,\, \tilde{x} \leftarrow \mathcal{A}[D,c,h](x)}\!\left[h(\tilde{x}) \neq c(\tilde{x})\right]$$

**PAC learning under hybrid attacks (Definition 2.2)**: A learning algorithm $L$ achieves sample complexity $m(\varepsilon, \delta, n)$ under hybrid attacks $\mathcal{A} = (A_1, A_2)$ if for all $n, c \in \mathcal{C}, D \in \mathcal{D}$ and all $(A_1, A_2) \in \mathcal{A}$, training on the poisoned sample $\tilde{\mathcal{S}} \leftarrow A_1[D,c](\mathcal{S})$ produces $h = L(\tilde{\mathcal{S}})$ with $\text{AdvRisk}_{A_2}(h, c, D) \leq \varepsilon$ with probability $\geq 1-\delta$.

**Lemma 3.2 (Concentration → AdvRisk)**: If $h$ has $\text{Risk}(D_n, c, h) \geq \alpha$ on a Normal Lévy family, then for perturbation budget $b = O(\sqrt{n/k_2} \cdot (\sqrt{\ln(k_1/\alpha)} + \sqrt{\ln(k_1/\beta)}))$, any attacker $\mathcal{A}_b$ achieves $\text{AdvRisk}_{\mathcal{A}_b}(h,c) \geq 1 - \beta$.

**Proof sketch for Lemma 3.5**: If $m = 2^{o(n)}$ then $1/m = \omega(2^{-\Theta(n)})$, so by the $\alpha$-close condition there exist $c_1, c_2$ with disagreement $\Delta(c_1,c_2)$ of measure $\sim 1/m$. With probability $\geq 0.99$, no training sample falls in $\Delta(c_1,c_2)$, so the learner cannot distinguish $c_1$ from $c_2$ and produces $h$ with $\text{Risk}(h,c) \geq \Omega(1/m)$. Lemma 3.2 then yields $\text{AdvRisk} \geq 0.99$ for sublinear budget $b \leq \rho \cdot n$, contradiction.

## Connections

- [Curse of Concentration](curse-of-concentration.md) — Lemma 3.2 (the core concentration→AdvRisk step) is directly from MDM19
- [Empirically Measuring Concentration](empirically-measuring-concentration.md) — the empirical gap this paper explains theoretically
- [Computational Concentration of Measure](computational-concentration-of-measure-etesami.md) — the algorithmic companion (poly-time attacks)
- [PAC-Learning in the Presence of Evasion Adversaries](pac-learning-evasion-adversaries.md) — CBM18 uses corrupted-input notion; this paper shows error-region requires exponentially more samples
- [VC Classes Are Adversarially Robustly Learnable](vc-classes-adversarially-robustly-learnable.md) — MHS19 shows proper robust learning needs more data; this paper gives exponential separation
- [Robust PAC Learning Characterization](robust-pac-learning-characterization.md) — MHS22 eventually characterizes robust learnability; DMM19 lower bounds motivate why characterization is needed
- [Concentration of Measure](../concepts/concentration-of-measure.md)
- [Robust PAC Learning](../concepts/robust-pac-learning.md)
- [Evasion Attacks](../concepts/evasion-attacks.md)
- [Poisoning Attacks](../concepts/poisoning-attacks.md)
- [Saeed Mahloujifar](../entities/saeed-mahloujifar.md)
- [Mohammad Mahmoody](../entities/mohammad-mahmoody.md)
- [Dimitrios Diochnos](../entities/dimitrios-diochnos.md)

## Open Questions / Limitations

- The result uses $\varepsilon = 0.9, \delta = 0.49$ — non-trivial but large parameters. What happens for small $\varepsilon$?
- Extension 4 (randomized predictors): result extends but requires the relaxed "approximate error region" $\mathcal{AE}(h,c) = \{x \mid \Pr_h[h(x) \neq c(x)] \geq 1/2\}$ — tighter analysis for randomized $h$ is open.
- No upper bound matching the exponential lower bound is provided — closing the gap requires constructing an efficient robust learner for these classes or ruling one out.
- The hybrid attack result uses removal-only poisoning (clean labels). Whether adding poisoning can do more in the error-region model is open.
- Connection to Montasser–Hanneke–Srebro: how does the global one-inclusion graph dimension interact with the $\alpha$-close condition and Normal Lévy structure?

## Quotes / Notable Passages

> "We prove that for many theoretically natural input spaces of high dimension $n$, PAC learning of certain problems under sublinear perturbations of the test instances requires *exponentially* many samples in $n$, even though the problem in the no-attack setting is PAC learnable using polynomially many samples."

> "In the realizable setting, learning a model with adversarial risk close to zero requires exponentially many samples. Recent impossibility results should not cause us to lose hope in the possibility of finding more robust classifiers." *(paraphrasing the empirical-measuring-concentration companion finding)*
