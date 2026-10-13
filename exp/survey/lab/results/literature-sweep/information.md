# Sweep 2026-10-13, lane `information`

Scope: what an adversary unbounded in time can and cannot infer from a learned artifact or a learning interaction, priced in samples, queries, bits or memory, and the information-theoretic necessity of leakage.

Method notes. Every paper below was opened on an arXiv, publisher, PMLR, NeurIPS or USENIX page, and every statement marked with a theorem number was read in the PDF text. dblp was unreachable from the sandbox (curl and WebFetch both failed), so venue evidence is the Crossref record of the DOI or the proceedings page. OpenAlex counts are taken on 2026-10-13 and under-count, because OpenAlex splits a paper over its arXiv and proceedings records. Epistemic labels in the statement lines follow the house words: Proven, Heuristic, Empirical, Open.

## 1. What the field has in this lane

Six results define it. Dinur and Nissim (DN03) price reconstruction from noisy subset sums: perturbation o(n) lets an exponential-time adversary reconstruct, perturbation o(sqrt n) lets a polynomial-time adversary reconstruct, and sqrt T is the matching price against time T. Feldman (F20) and Brown, Bun, Feldman, Smith and Talwar (BBFST21) show that accurate learning forces the model to carry information about its training set, as excess error under a long-tailed subpopulation prior in F20 and as Omega(nd) bits of mutual information in BBFST21. Steinke and Zakynthinou (SZ20) define conditional mutual information (CMI), the information the output carries about which element of each pair in a supersample was the training element, and bound generalization by it, with differential privacy (DP) implying a CMI bound. Haghifam, Smith and Ullman (HSU25), building on Dwork, Smith, Steinke, Ullman and Vadhan (DSSUV15), show that a membership-inference attacker matching a fully informed one can need Omega(n + n^2 rho^2) reference samples while the trainer used n. Balle, Cherubin and Hayes (BCH22) define reconstruction robustness and bound an informed adversary's reconstruction success by the success of the best oblivious guess times a DP factor, and Cairney-Leeming, Bombari and Mondelli (CLBM26) locate the sharp threshold of that bound at privacy budget rho of the order of the dimension. On robust learning, Schmidt et al. (SSTTM18) show an information-theoretic sqrt d sample gap between standard and robust learning in a Gaussian model, while Hanneke and Shaeiri (HS26) show that over VC classes, distribution-free, the gap vanishes up to constants.

## 2. Sheets

### DN03
- key: DN03
- title: Revealing information while preserving privacy
- authors: Irit Dinur, Kobbi Nissim
- venue: PODS 2003, pp. 202-210
- venue_evidence: Crossref record of https://doi.org/10.1145/773153.773173 gives "Proceedings of the twenty-second ACM SIGMOD-SIGACT-SIGART symposium on Principles of database systems", 2003. The PDF header was read.
- year: 2003
- link: https://doi.org/10.1145/773153.773173 (PDF read: https://www.cs.cornell.edu/~shmat/courses/cs6431/dn03.pdf)
- lane: I (Theorem 2), with C content (Theorems 3 and 5)
- honest task: answer subset-sum queries on an n-bit database, each answer within perturbation E of the true sum.
- adversary task: reconstruct all but epsilon n bits of the database from the perturbed answers.
- bounded party: the adversary (queries and time), against the curator's perturbation magnitude E.
- resource: perturbation magnitude E as a function of adversary time. Exponential time with all 2^n queries, polynomial time with n (log n)^2 random queries, time T(n).
- adversary class: unrestricted (Thm 2), polynomial-time (Thm 3), T(n)-time machines (Thm 5).
- assumption: none for Thms 2 and 3. Thm 5 takes the database uniform over {0,1}^n, which the paper uses to model an adversary with no prior information.
- statement: Proven (Thm 2, section 3.1 "Exponential Adversary"): a database within o(n) perturbation is exp(n)-non-private. Proven (Thm 3, section 3.2 "Polynomially Bounded Adversary"): within o(sqrt n) perturbation it is poly(n)-non-private, by a linear program over t = n (log n)^2 random subset queries that returns a candidate within epsilon n of the database for every epsilon > 0. Proven (Thm 5): for T(n) > polylog(n) there is an algorithm with perturbation O~(sqrt T(n)) that is (T(n), delta)-private. Read in the PDF text.
- technique: linear-programming decoding with random queries, a Disqualifying Lemma (Lemma 4) and a union bound over the (k+1)^n rounded candidates, Azuma's inequality.
- gap sign: adversary cheaper than the honest accuracy requirement. Polynomial time and n polylog n queries suffice below E = sqrt n, and the honest curator pays noise of order sqrt T against a time-T adversary.
- prominence: PODS, which is not on the brief's tier list. OpenAlex cited_by_count 980 (W2110868467, 2026-10-13). It is the reconstruction attack that HSU25 cites for reconstruction in general.
- in_corpus: dinur-nissim-revealing-information
- prerequisite: linear programming, Azuma concentration, the subset-sum query model.
- tier: deep

### DSSUV15
- key: DSSUV15
- title: Robust Traceability from Trace Amounts
- authors: Cynthia Dwork, Adam Smith, Thomas Steinke, Jonathan Ullman, Salil Vadhan
- venue: FOCS 2015, pp. 650-669
- venue_evidence: Crossref record of https://doi.org/10.1109/FOCS.2015.46 gives "2015 IEEE 56th Annual Symposium on Foundations of Computer Science". The Harvard DASH copy states the same citation.
- year: 2015
- link: https://doi.org/10.1109/FOCS.2015.46 (PDF read: https://dash.harvard.edu/server/api/core/bitstreams/7312037d-cc95-6bd4-e053-0100007fdf3b/content)
- lane: I
- honest task: release approximate one-way marginals of n samples from {+1,-1}^d, accurate in bias only (alpha-accurate).
- adversary task: decide IN or OUT for a target y, given the released vector and a reference sample z from the population.
- bounded party: the attacker's reference samples (one in Thm 1) and the dimension d against n.
- resource: dimension d at least of order n^2 log(1/delta), reference samples m of order log n / alpha^2 for tracing several individuals.
- adversary class: an arbitrary function A(y, q, z), soundness s and completeness c.
- assumption: a product prior over the marginals whose marginals are "strong" (Defs 6 and 27), and a mechanism that is alpha-accurate for a universal constant alpha.
- statement: Proven (Thm 1, informal version in the results subsection of the introduction): for d >= O(n^2 log(1/delta)) there is an attacker that accepts an independent y with probability at most delta and accepts some x_i with probability at least 1 - delta. The dimension d = O~(n^2) is tight up to polylogarithmic factors, because d = Omega~(n^2) marginals can be released under (o(1), 1/n^omega(1))-DP. Proven (Thm 17, informal): with d >= O(alpha^2 n^2 log(1/delta)) and m >= O(log n / alpha^2) reference samples the attacker traces Omega(1/alpha^2) members. Read in the PDF text.
- technique: a fingerprinting-code style correlation statistic and tail bounds under the strong-distribution condition.
- gap sign: existence of a threshold in d against n, with a cheap attacker (one reference sample) against the n samples of the trainer.
- prominence: FOCS. OpenAlex cited_by_count 137 (W2198253679, 2026-10-13). HSU25 builds on it.
- in_corpus: no
- prerequisite: DP, fingerprinting codes (Bun, Ullman, Vadhan), the membership-inference game.
- tier: read

### F20
- key: F20
- title: Does learning require memorization? A short tale about a long tail
- authors: Vitaly Feldman
- venue: STOC 2020, pp. 954-959
- venue_evidence: Crossref record of https://doi.org/10.1145/3357713.3384290 gives "Proceedings of the 52nd Annual ACM SIGACT Symposium on Theory of Computing". The arXiv page (1906.05271, v4) lists no venue.
- year: 2020
- link: https://arxiv.org/abs/1906.05271
- lane: I
- honest task: learn a classifier with near-optimal generalization error from n labeled examples drawn from a mixture of subpopulations with a frequency prior pi and a label prior F.
- adversary task: none. The paper defines label memorization mem(A, S, i), the effect of the label y_i on the prediction at x_i, and says only in prose that memorization is a privacy risk.
- bounded party: the learning algorithm's label memorization gamma.
- resource: label memorization gamma against excess generalization error, with n samples and N subpopulations.
- adversary class: none.
- assumption: a long-tailed frequency prior (Zipf for the concrete corollary), N at least n, and labels that are uniform and k-wise independent across subpopulations for the concrete corollary.
- statement: Proven (Thms 2.3 and 2.4): err(pi, F, A) >= opt(pi, F) + tau_1 * E[ sum over singleton-subpopulation examples of conf(S, i, F) * Pr[h(x_i) != y_i] ], where tau_1 is a ratio of moments of the frequency prior. Proven (Cor 4.6): a gamma-memorization-limited algorithm pays excess error, and the text after the corollary states that for a Zipf prior and N >= n, any algorithm with constant gamma < 1 - 1/|Y| has excess error Omega(1), so optimal generalization needs memorizing Omega(n) labels. Proven (Thm 4.8): an (epsilon, delta) label-private algorithm is (e^epsilon - 1 + delta)-memorization limited and pays the same excess error. Read in the PDF text.
- technique: Bayesian posterior analysis of the unseen mass, with singleton examples as the source of the cost.
- gap sign: not a gap result. It is a necessary-leakage lower bound on the honest learner, with no adversary.
- prominence: STOC. OpenAlex cited_by_count 276 (W2950181023, 2026-10-13).
- in_corpus: no
- prerequisite: missing-mass (Good-Turing) estimates, label DP.
- tier: deep

### BBFST21
- key: BBFST21
- title: When is memorization of irrelevant training data necessary for high-accuracy learning?
- authors: Gavin Brown, Mark Bun, Vitaly Feldman, Adam Smith, Kunal Talwar
- venue: STOC 2021, pp. 123-132
- venue_evidence: Crossref record of https://doi.org/10.1145/3406325.3451131 gives "Proceedings of the 53rd Annual ACM SIGACT Symposium on Theory of Computing". The arXiv page (2012.06421) carries the journal reference "STOC 2021 Pages 123-132".
- year: 2021
- link: https://arxiv.org/abs/2012.06421
- lane: I
- honest task: learn a next-symbol prediction task or a cluster labeling task to error within a small constant epsilon of optimal.
- adversary task: none in the theorems. Section 5 runs black-box attacks on logistic regression and neural classifiers over synthetic data (Empirical).
- bounded party: the learner, through the mutual information I(X; M | P) between sample X and model M.
- resource: bits. I(X; M | P) = Omega(nd) for examples in {0,1}^d, where H(X) <= nd.
- adversary class: none. The authors state that the bound does not show that a computationally efficient attacker can recover training data.
- assumption: a meta-distribution q over tasks, so the learner does not know P. The whole-sample statement (Thm 1.2) rests on Corollary 3.1 for next-symbol prediction and on Conjecture 4.1 (one-way information complexity) for cluster labeling.
- statement: Proven (Thm 1.1, informal, via Cors 3.1 and 4.1): for all n and d there are natural tasks on which every learner with err <= opt + epsilon has I(X; M | P) = Omega(nd), independent of algorithm and model class. Proven (Thm 1.2, informal): on some tasks a subset X_S of expected size Omega(n) is encoded nearly completely, I(X_S; M | P) = (1 - o(1)) H(X_S | P). Read in the PDF text.
- technique: reduction from one-way communication problems with new information-complexity lower bounds.
- gap sign: existence only. Leakage is necessary for accuracy, and no computational adversary is priced.
- prominence: STOC. OpenAlex cited_by_count 34 (W3113004165, 2026-10-13).
- in_corpus: no
- prerequisite: one-way communication complexity, mutual information, F20.
- tier: deep

### ADHLR24
- key: ADHLR24
- title: Information Complexity of Stochastic Convex Optimization: Applications to Generalization, Memorization, and Tracing (arXiv v1 and v2 title ends "Generalization and Memorization")
- authors: Idan Attias, Gintare Karolina Dziugaite, Mahdi Haghifam, Roi Livni, Daniel M. Roy
- venue: ICML 2024 (PMLR 235), pp. 2035-2068
- venue_evidence: https://proceedings.mlr.press/v235/attias24a.html, "Proceedings of the 41st International Conference on Machine Learning".
- year: 2024
- link: https://arxiv.org/abs/2402.09327 (PDF read)
- lane: I
- honest task: epsilon-learn an L2-Lipschitz stochastic convex optimization (SCO) problem.
- adversary task: identify, with soundness xi, a number m of the training samples from the learner's output.
- bounded party: the learner's CMI. The adversary of Thm 4.5 is stated to be efficient.
- resource: CMI in nats against excess error epsilon, with dimension d >= Omega(n^2 log n).
- adversary class: an efficient membership-style certifier (xi-sound, recall m).
- assumption: a 1-Lipschitz convex loss over the unit ball, d >= Omega(n^2 log(n/xi)), and for Thm 4.5 sample size n = N(epsilon, delta) = Theta(log(1/delta)/epsilon^2).
- statement: Proven (Thm 4.1): there is a loss such that every epsilon-learner with n >= N(epsilon, delta) and d >= Omega(n^2 log n) has CMI_D(A_n) = Omega(1/epsilon^2) on some distribution D, and a learner with CMI O(1/epsilon^2) exists. Proven (Thm 4.2): Omega(1/epsilon) in the strongly convex case. Proven (Thm 4.5): an efficient xi-sound adversary certifies recall Omega(1/epsilon^2) training samples against every epsilon-learner, Omega(1/epsilon) in the strongly convex case (Thm 4.6). Proven (Thm 5.2): CMI-based generalization bounds are vacuous for sample-optimal SCO learners. Read in the PDF text.
- technique: a high-dimensional construction with d >= Omega(n^2 log n) and an adversary that traces training samples. The proofs were not read beyond the theorem statements.
- gap sign: existence only. Every accurate learner must leak a number of samples of the order of the training-set size at the optimal n.
- prominence: ICML. OpenAlex cited_by_count 0 on the arXiv record (W4391871165), which lags.
- in_corpus: no
- prerequisite: SZ20, SCO, tracing and fingerprinting.
- tier: read

### SZ20
- key: SZ20
- title: Reasoning About Generalization via Conditional Mutual Information
- authors: Thomas Steinke, Lydia Zakynthinou
- venue: COLT 2020 (PMLR 125), pp. 3437-3452
- venue_evidence: https://proceedings.mlr.press/v125/steinke20a.html, "Proceedings of Thirty Third Conference on Learning Theory". The arXiv PDF states "Accepted for publication at the 33rd Annual Conference on Learning Theory (COLT 2020)".
- year: 2020
- link: https://arxiv.org/abs/2001.09122
- lane: I
- honest task: output a hypothesis that generalizes, from n i.i.d. samples.
- adversary task: none. CMI measures how well the output identifies which of each pair in a supersample was the training element (abstract: how well "the input can be recognized given the output"), which is a membership-inference game against an unbounded recognizer.
- bounded party: the algorithm, through its CMI.
- resource: CMI in nats, 0 <= CMI <= n log 2.
- adversary class: information-theoretic, no computational bound.
- assumption: i.i.d. data. The stability and compression corollaries need KL stability, DP or a compression scheme.
- statement: Definition 1.1: CMI_D(A) = I(A(Z_S); S | Z), with Z a 2n-sample supersample and S a uniform selector. Proven (Thm 1.2): for a [0,1] loss the expected generalization gap is at most sqrt((2/n) CMI_D(A)), with squared-gap and realizable variants. Proven (Thm 4.7): epsilon-KL, ALKL or MI stable algorithms, and sqrt(2 epsilon)-DP algorithms, have CMI(A) <= epsilon n. Proven (Thm 4.12): for a class of VC dimension d there exists an ERM with CMI(A) <= d log n + 2. CMI composes non-adaptively (Thm 3.1) and is closed under post-processing (Thm 3.3). Read in the PDF text.
- technique: supersample (ghost sample) symmetrization and the data-processing inequality.
- gap sign: not a gap result. It is an information measure that ties generalization to membership recognizability.
- prominence: COLT. OpenAlex cited_by_count 17 on the arXiv record (W3002329345, 2026-10-13).
- in_corpus: no
- prerequisite: mutual information, DP, VC theory.
- tier: deep

### DRS22
- key: DRS22
- title: Gaussian Differential Privacy
- authors: Jinshuo Dong, Aaron Roth, Weijie J. Su
- venue: Journal of the Royal Statistical Society Series B (Statistical Methodology), 2022, pp. 3-37
- venue_evidence: Crossref record of https://doi.org/10.1111/rssb.12454.
- year: 2022
- link: https://arxiv.org/abs/1905.02383 (PDF read)
- lane: D
- honest task: release M(S) so that distinguishing neighbouring datasets is at least as hard as distinguishing P from Q.
- adversary task: a hypothesis test between M(S) and M(S') for neighbouring S and S', the general form of membership inference.
- bounded party: none. The test phi is any measurable rejection rule, so the adversary is unbounded.
- resource: the pair of type I and type II error rates, summarized by the trade-off function.
- adversary class: all Neyman-Pearson tests.
- assumption: none for the definition. The central limit theorem for composition needs many compositions of mechanisms of small privacy loss (conditions on the kl, kappa_2 and kappa_3 of the trade-off functions).
- statement: Definition 2.1: trade-off function T(P, Q). Definition 2.3: M is f-DP if T(M(S), M(S')) >= f for all neighbouring S and S'. Definition 2.6: mu-GDP. Proven (Thm 3.5): under the stated conditions the composition of f-DP guarantees converges to a Gaussian trade-off function. Proven (Thm 4.2): subsampling acts on f through an operator C_p. Proven (Prop 2.8): post-processing preserves f-DP. Read in the PDF text.
- technique: Neyman-Pearson trade-off curves and convex duality.
- gap sign: not a gap result.
- prominence: JRSS Series B. OpenAlex cited_by_count 371 (W3189333525, 2026-10-13). It is the origin of the f-DP definition.
- in_corpus: no
- prerequisite: Neyman-Pearson lemma, (epsilon, delta)-DP.
- tier: read

### SDSOJ19
- key: SDSOJ19
- title: White-box vs Black-box: Bayes Optimal Strategies for Membership Inference
- authors: Alexandre Sablayrolles, Matthijs Douze, Cordelia Schmid, Yann Ollivier, Herve Jegou
- venue: ICML 2019 (PMLR 97), pp. 5558-5567
- venue_evidence: https://proceedings.mlr.press/v97/sablayrolles19a.html, "Proceedings of the 36th International Conference on Machine Learning".
- year: 2019
- link: https://arxiv.org/abs/1908.11229 (PDF read)
- lane: I
- honest task: train parameters theta whose posterior has Gibbs form, proportional to exp(-(1/T) sum_i m_i loss(theta, z_i)).
- adversary task: compute M(theta, z_1) = P(m_1 = 1 | theta, z_1), the membership posterior of a sample.
- bounded party: none. The Bayes-optimal rule is intractable and the paper supplies approximations (abstract).
- resource: knowledge of the data distribution, the training procedure and the other samples' memberships (averaged over T).
- adversary class: Bayes optimal.
- assumption: the Gibbs-form posterior of the parameters (Eq. 2). The abstract describes it as a few assumptions on the distribution of the parameters.
- statement: Proven (Thm 2): M(theta, z_1) = E_T[ sigma( s(z_1, theta, p_T) + t_lambda ) ], with s = (tau_p(z_1) - loss(theta, z_1)) / T. The optimal rule reads theta only through the loss, so a white-box attacker gains nothing over a loss-only black-box attacker. Proven (Property 1): epsilon-DP implies P(m_1 = 1 | theta, z_1) <= lambda + epsilon/4. Read in the PDF text.
- technique: Bayes' rule with a Gibbs posterior.
- gap sign: not a gap result. It is an equivalence between white-box and black-box optimal attackers under the stated assumption.
- prominence: ICML. OpenAlex cited_by_count 106 on the arXiv record (W2945237470, 2026-10-13). HSU25 cites it as the case where threshold-calibrated attacks are exactly optimal.
- in_corpus: no
- prerequisite: Bayesian inference, the membership-inference game.
- tier: read

### HSU25
- key: HSU25
- title: The Sample Complexity of Membership Inference and Privacy Auditing
- authors: Mahdi Haghifam, Adam Smith, Jonathan Ullman
- venue: FOCS 2026 (to appear)
- venue_evidence: arXiv listing https://arxiv.org/abs/2508.19458, v2 submitted 8 October 2026, comment "To appear in FOCS 2026". The existing corpus page records no refereed venue and predates this comment.
- year: 2025 (v1), 2026 (v2)
- link: https://arxiv.org/abs/2508.19458 (v2 PDF read)
- lane: I
- honest task: estimate the mean of N(mu, Sigma) from n samples with E||mu_hat - mu||_Sigma^2 <= d rho^2 + d/n (rho-accurate).
- adversary task: membership inference, deciding IN or OUT for a target given mu_hat and m reference samples, with true-positive rate at least 0.51 and false-positive rate at most 0.49.
- bounded party: the number m of reference samples. Computation is unbounded.
- resource: reference samples m against n.
- adversary class: any function psi_m, required to succeed for every (mu, Sigma) and every rho-accurate noise-addition algorithm.
- assumption: d >= d*(n, rho) = n + n^2 rho^2, the threshold at which a fully informed attacker succeeds. Sigma is unknown to the attacker. The hard instance is a distribution over population and algorithm pairs, with mu_hat = empirical mean + rho Z for Z ~ N(0, Sigma).
- statement: Proven (Thm 1.1, informal version of Thm 3.1): every sample-based membership attack needs m >= Omega(n^2 rho^2 + n) samples, even for arbitrarily large d. Proven (Thm 1.2, informal version of Thm 4.1): with Sigma known, m >= Omega(min{n, 1/rho^2}) is necessary, and an m-sample attack exists only if d >= Omega(n + n^2 rho^2 + n^2/m). The straightforward attack uses Theta(d) samples, so a gap to the lower bound remains for d much larger than d*. The authors list a separation for a single mechanism as an open question. Read in the PDF text.
- technique: a reduction to membership inference with zero auxiliary samples for a related problem (section 1.3), then chi-squared divergence calculations in the technique the paper attributes to Ingster and Suslina (stated at the start of one of its proofs).
- gap sign: attacker dearer than trainer (Omega(n + n^2 rho^2) against n) to match a fully informed attacker, and not dearer when Sigma is known.
- prominence: FOCS 2026 per the arXiv comment. OpenAlex cited_by_count 0 (W7078134051).
- in_corpus: haghifam-sample-complexity-mia
- prerequisite: DSSUV15, Gaussian mean estimation, chi-squared divergence.
- tier: deep

### BCH22
- key: BCH22
- title: Reconstructing Training Data with Informed Adversaries
- authors: Borja Balle, Giovanni Cherubin, Jamie Hayes
- venue: IEEE S&P 2022, pp. 1138-1156
- venue_evidence: Crossref record of https://doi.org/10.1109/SP46214.2022.9833677 gives "2022 IEEE Symposium on Security and Privacy (SP)".
- year: 2022
- link: https://arxiv.org/abs/2201.04845 (PDF read)
- lane: I, with D content (reconstruction robustness)
- honest task: release a model from a mechanism M that is (alpha, epsilon)-Renyi DP or epsilon-DP.
- adversary task: reconstruct the one unknown training point z within error eta, knowing the other n - 1 points and a prior pi on z.
- bounded party: none on the attack R. The privacy parameter bounds the success.
- resource: epsilon or rho against the anti-concentration kappa of the prior.
- adversary class: any reconstruction attack R, informed of D_-.
- assumption: a prior pi with small-ball probability kappa_{pi,l}(eta) = sup_{z0} P_{Z ~ pi}[l(Z, z0) <= eta], the success of the best oblivious guess.
- statement: Definition 2: M is (eta, gamma)-ReRo if for every D_- and every R, P[l(Z, R(theta)) <= eta] <= gamma. Proven (Thm 2): (alpha, epsilon)-RDP implies (eta, gamma)-ReRo with gamma = (kappa e^epsilon)^((alpha-1)/alpha). Proven (Cor 3): epsilon-DP gives gamma = kappa e^epsilon. Proven (Cor 4): rho-zCDP with rho < log(1/kappa) gives gamma = exp(-(sqrt(log(1/kappa)) - sqrt(rho))^2). Proven (Prop 6): for the uniform prior on the unit ball, epsilon = o(d) or rho = o(d) gives gamma = e^(-Omega(d)). Empirical: reconstructor-network attacks on MNIST and CIFAR-10. Read in the PDF text.
- technique: probability preservation under Renyi DP, and small-ball anti-concentration of the prior.
- gap sign: not a gap result. It bounds attack success by the oblivious baseline times a DP factor.
- prominence: IEEE S&P. OpenAlex cited_by_count 83 (W3211753216, 2026-10-13).
- in_corpus: reconstructing-informed-adversaries
- prerequisite: Renyi DP, zCDP.
- tier: deep

### GKCM22
- key: GKCM22
- title: Bounding Training Data Reconstruction in Private (Deep) Learning
- authors: Chuan Guo, Brian Karrer, Kamalika Chaudhuri, Laurens van der Maaten
- venue: ICML 2022 (PMLR 162), pp. 8056-8071
- venue_evidence: https://proceedings.mlr.press/v162/guo22c.html, "Proceedings of the 39th International Conference on Machine Learning".
- year: 2022
- link: https://arxiv.org/abs/2201.12383 (PDF read)
- lane: I
- honest task: train with a (2, epsilon)-Renyi DP algorithm, or with output perturbation or DP-SGD under Fisher information leakage (FIL) accounting.
- adversary task: estimate a training sample z in a bounded domain Z of R^d from the trained model h.
- bounded party: none on the estimator. The privacy parameter or the FIL bounds the error.
- resource: mean squared error of the reconstruction against epsilon or FIL.
- adversary class: any estimator z_hat(h).
- assumption: a bounded domain. The FIL bound (Thm 2) needs regularity of the log-density of the model given the sample.
- statement: Proven (Thm 1): for a (2, epsilon)-RDP algorithm, E||z_hat - z||^2 / d >= (sum_i gamma_i^2 diam_i(Z)^2 / 4d) / (e^epsilon - 1) + ||mu(z) - z||^2 / d, and for an unbiased estimator the bound reads (sum_i diam_i(Z)^2 / 4d) / (e^epsilon - 1). Proven (Thm 2, under the regularity conditions of its Thm A.2): E||z_hat - z||^2 / d >= Tr(J I_h(z)^(-1) J^T)/d + ||mu(z) - z||^2 / d, and for an unbiased estimator >= d / Tr(I_h(z)) >= 1/eta^2, where I_h(z) is the Fisher information of the model about z and eta^2 bounds its diagonal entries. Proven (Thm 4): a FIL accounting equation for DP-SGD, whose body was not read. Read in the PDF text. The FIL notion is credited in the text to Hannun et al. (2021), whose paper was not opened.
- technique: the identity D_2(P||Q) = log(1 + chi^2(P||Q)) with a chi-squared variance lower bound, then Cramer-Rao.
- gap sign: not a gap result.
- prominence: ICML. OpenAlex cited_by_count 4 (W4221142579, 2026-10-13), which is low for a paper this central to the reconstruction line.
- in_corpus: no
- prerequisite: Renyi DP, Fisher information, Cramer-Rao.
- tier: read

### GSS23
- key: GSS23
- title: Analyzing Privacy Leakage in Machine Learning via Multiple Hypothesis Testing: A Lesson From Fano
- authors: Chuan Guo, Alexandre Sablayrolles, Maziar Sanjabi
- venue: ICML 2023 (PMLR 202), pp. 11998-12011
- venue_evidence: https://proceedings.mlr.press/v202/guo23e.html, "Proceedings of the 40th International Conference on Machine Learning".
- year: 2023
- link: https://proceedings.mlr.press/v202/guo23e.html (arXiv 2210.13662, PDF not read)
- lane: I
- honest task: an (alpha, epsilon)-Renyi DP learning algorithm on discrete data.
- adversary task: reconstruction of discrete data, posed as multiple hypothesis testing.
- bounded party: none (abstract).
- resource: the RDP parameter epsilon against the adversary's advantage.
- adversary class: any reconstruction adversary (abstract).
- assumption: discrete data and (alpha, epsilon)-RDP.
- statement: Proven (abstract): variants of Fano's inequality upper-bound the adversary's advantage against an (alpha, epsilon)-RDP algorithm, and the bound is numerically computable. The PMLR abstract adds that it supports the empirical finding that DP resists reconstruction at relatively large epsilon. No theorem number was read.
- technique: Fano's inequality and its variants.
- gap sign: not a gap result.
- prominence: ICML. OpenAlex cited_by_count 3 on the arXiv record (W4307415497, 2026-10-13).
- in_corpus: no
- prerequisite: Fano's inequality, RDP.
- tier: skim

### CLBM26
- key: CLBM26
- title: A Sharp Transition in Data Reconstruction under Differential Privacy
- authors: Max Cairney-Leeming, Simone Bombari, Marco Mondelli
- venue: arXiv preprint 2609.37344, 29 September 2026
- venue_evidence: the arXiv listing https://arxiv.org/abs/2609.37344 shows no journal reference or comment.
- year: 2026
- link: https://arxiv.org/abs/2609.37344 (PDF read)
- lane: I
- honest task: release a model from a rho-zero-concentrated DP (zCDP) mechanism, with output-perturbed private linear regression for the attack side.
- adversary task: reconstruct one d-dimensional training sample while knowing all the other training data.
- bounded party: none on the attacker in Thm 1. The budget rho is compared with d, or with the dimension s of the subspace the data lie in.
- resource: privacy budget rho against dimension d, or effective dimension s.
- adversary class: any attack for the lower bound, a simple explicit attack on private linear regression for the upper side.
- assumption: a target independent of the rest of the data. For the attack, Assumption 1 and output perturbation.
- statement: Proven (Thm 1): for every rho-zCDP mechanism and every attack, E||x_t - x_hat||^2 / E||x_t||^2 >= (1/2 pi e) exp((2/d)(h(x'_t) - rho)), where h is the differential entropy of the normalized target. Hence reconstruction is information-theoretically impossible for priors of large entropy when rho << d. Proven (abstract, Thms 2 to 4 not read): a simple attack succeeds for rho >> d, and the transition moves to rho of the order of s for data in an s-dimensional subspace. Appendix F compares with BCH22.
- technique: entropy-based lower bound on estimation error.
- gap sign: not a gap result. It is a sharp threshold in the budget.
- prominence: arXiv preprint, two weeks old at the sweep date. OpenAlex cited_by_count 0 (W7214969527).
- in_corpus: no
- prerequisite: zCDP, differential entropy, BCH22.
- tier: read

### SSTTM18
- key: SSTTM18
- title: Adversarially Robust Generalization Requires More Data
- authors: Ludwig Schmidt, Shibani Santurkar, Dimitris Tsipras, Kunal Talwar, Aleksander Madry
- venue: NeurIPS 2018 (Advances in Neural Information Processing Systems 31)
- venue_evidence: https://proceedings.neurips.cc/paper_files/paper/2018/hash/f708f064faaf32a43e4d3c784e6af9ea-Abstract.html.
- year: 2018
- link: https://arxiv.org/abs/1804.11285 (PDF read)
- lane: I
- honest task: learn a classifier with 1% standard error in the (theta*, sigma)-Gaussian model with ||theta*|| = sqrt d and sigma = c d^(1/4).
- adversary task: l_infinity perturbation of size epsilon at test time, so the learner must reach 1% l_infinity-robust error.
- bounded party: the learner's sample size n. The perturbing adversary has no stated budget.
- resource: samples.
- adversary class: l_infinity ball of radius epsilon.
- assumption: the Gaussian model, theta drawn from N(0, I) for the lower bound. Any learning algorithm.
- statement: Proven (Thm 4): one sample gives the linear classifier w = y x with at most 1% standard error. Proven (Thm 5): the weighted sample mean has robust error at most 1% once n >= c_2 epsilon^2 sqrt d, for epsilon between (1/4) d^(-1/4) and 1/4. Proven (Thm 6): any learner with n <= c_2 epsilon^2 sqrt d / log d has expected robust error at least (1 - 1/d)/2. The abstract states that the gap is information theoretic and holds irrespective of the training algorithm or model family. Empirical: the abstract reports a similar gap on popular image classification datasets. Read in the PDF text.
- technique: Gaussian concentration and a Bayesian lower bound over theta ~ N(0, I).
- gap sign: the robust task is dearer than the standard task, by a factor of about sqrt d in samples.
- prominence: NeurIPS. OpenAlex cited_by_count 476 (W2799032899, 2026-10-13).
- in_corpus: robust-generalization-more-data
- prerequisite: Gaussian concentration, minimax lower bounds.
- tier: read

### CBM18
- key: CBM18
- title: PAC-learning in the presence of adversaries (arXiv title: PAC-learning in the presence of evasion adversaries)
- authors: Daniel Cullina, Arjun Nitin Bhagoji, Prateek Mittal
- venue: NeurIPS 2018 (Advances in Neural Information Processing Systems 31)
- venue_evidence: https://proceedings.neurips.cc/paper_files/paper/2018/hash/8f85517967795eeef66c225f7883bdcb-Abstract.html.
- year: 2018
- link: https://arxiv.org/abs/1806.01471 (PDF read)
- lane: I
- honest task: PAC-learn a class H with robust risk against an evasion adversary.
- adversary task: perturb a test point inside a relation R, so the learner minimizes adversarial expected risk.
- bounded party: the learner's samples. The adversary is any relation R and is unbounded.
- resource: samples as a function of the adversarial VC dimension.
- adversary class: a binary adversarial relation R, with R convex and origin-symmetric for the halfspace theorem.
- assumption: none for Thm 1. Thm 2 needs a nonempty, closed, convex, origin-symmetric set B.
- statement: Definition 5: the adversarial VC dimension AVC(H, R). Proven (Thm 1): m_{H,R}(delta, epsilon) <= C (d log(d/epsilon) + log(1/delta)) / epsilon^2 with d = AVC(H, R). Proven (Thm 2): for halfspaces in R^d, AVC = d + 1 - dim(V_B), which is d + 1 for a bounded l_p ball, equal to the VC dimension. Proven (Thm 3): for every d there is a class with VC = 1 and AVC >= d. Read in the PDF text.
- technique: corrupted hypothesis classes, Rademacher complexity via Massart's lemma and the Sauer-Shelah lemma.
- gap sign: equal to the standard cost for halfspaces under l_p balls, dearer in constructed classes where AVC exceeds VC.
- prominence: NeurIPS. OpenAlex cited_by_count 39 on the NeurIPS record (W2892179671) and 16 on the arXiv record (W2807539765), 2026-10-13.
- in_corpus: pac-learning-evasion-adversaries
- prerequisite: VC theory, Rademacher complexity.
- tier: read

### MHS19
- key: MHS19
- title: VC Classes are Adversarially Robustly Learnable, but Only Improperly
- authors: Omar Montasser, Steve Hanneke, Nathan Srebro
- venue: COLT 2019 (PMLR 99), pp. 2512-2530
- venue_evidence: https://proceedings.mlr.press/v99/montasser19a.html, "Proceedings of the Thirty-Second Conference on Learning Theory".
- year: 2019
- link: https://arxiv.org/abs/1902.04217 (PDF read)
- lane: I
- honest task: robustly PAC-learn a class H of finite VC dimension against a perturbation set U.
- adversary task: any perturbation of a test point in U(x).
- bounded party: the learner's samples. Proper learners are the restricted class.
- resource: samples, in terms of vc(H) and the dual dimension vc*(H).
- adversary class: an arbitrary perturbation map U.
- assumption: none beyond finite VC dimension.
- statement: Proven (Thm 1): there is a class with vc(H) <= 1 and an adversary U such that H is not properly robustly PAC learnable in the realizable setting. Proven (Cor 5, via Thm 4 and Assouad's vc* < 2^(vc+1)): the realizable sample complexity is 2^O(vc(H)) (1/epsilon) log(1/epsilon) + O((1/epsilon) log(1/delta)), read from extracted text, so check the typeset formula. Proven (Cor 7): an agnostic bound of the same exponential form in vc(H). Read in the PDF text.
- technique: sample compression, and a reduction from the agnostic to the realizable case.
- gap sign: robust learning dearer by at most a factor exponential in the VC dimension (upper bound only). HS26 and Mon26 later remove the exponential.
- prominence: COLT. OpenAlex cited_by_count 56 (W2915022044, 2026-10-13).
- in_corpus: vc-classes-adversarially-robustly-learnable
- prerequisite: PAC learning, sample compression, dual VC dimension.
- tier: read

### HS26
- key: HS26
- title: Adversarially Robust PAC Learning with Optimal VC Rates
- authors: Steve Hanneke, Amirreza Shaeiri
- venue: arXiv preprint 2609.24260, 21 September 2026
- venue_evidence: the arXiv listing https://arxiv.org/abs/2609.24260 shows no comments or journal reference.
- year: 2026
- link: https://arxiv.org/abs/2609.24260 (PDF read)
- lane: I
- honest task: robustly PAC-learn a VC class H of dimension d against any perturbation map U known to the learner.
- adversary task: any perturbation of a test point in U(x).
- bounded party: the learner's samples.
- resource: samples, independent of U.
- adversary class: an arbitrary map U.
- assumption: finite VC dimension, improper learner.
- statement: Proven (Thm 1, main result): for every VC-d class and every U there is an improper learner whose robust risk is at most R*_{U,D}(H) + C( sqrt(R* (d + log(1/delta))/m) + (d + log(1/delta))/m ). Proven (corollaries): O((d + log(1/delta))/epsilon) samples in the realizable case and O((d + log(1/delta))/epsilon^2) in the agnostic case, uniformly over U, matching classical PAC lower bounds, so robustness adds no distribution-free statistical cost and the bounds improve MHS19 exponentially. The paper states that concurrent independent work by Montasser (arXiv:2608.13514, "Bagging Robustly Learns VC Classes with Linear Sample Complexity", opened) reaches the same sample bound by bagging and proves that Omega(d*) robust-ERM oracle calls are necessary whatever the sample size (its Thm 2). Read in the PDF text.
- technique: binomial bagging.
- gap sign: equal, up to universal constants, in samples over the VC class, distribution-free. The cost that remains is in oracle calls.
- prominence: arXiv preprint, three weeks old at the sweep date. OpenAlex cited_by_count 0 (W7214043332).
- in_corpus: no
- prerequisite: MHS19, bagging, robust empirical risk minimization.
- tier: read

### CCGJY20
- key: CCGJY20
- title: Exploring Connections Between Active Learning and Model Extraction
- authors: Varun Chandrasekaran, Kamalika Chaudhuri, Irene Giacomelli, Somesh Jha, Songbai Yan
- venue: USENIX Security 2020 (29th USENIX Security Symposium)
- venue_evidence: https://www.usenix.org/conference/usenixsecurity20/presentation/chandrasekaran.
- year: 2020
- link: https://arxiv.org/abs/1811.02054 (v6 PDF read, November 2019, so the USENIX camera-ready may differ)
- lane: I, with D content (Definition 3 of an extraction attack)
- honest task: serve black-box labels f*(x) for a model f* in a public class F.
- adversary task: learn f_hat with Err(f_hat) <= epsilon using q queries, with confidence gamma.
- bounded party: the adversary's query count q.
- resource: queries.
- adversary class: query-synthesis (QS) learners with no knowledge of the data distribution.
- assumption: F is public and the server answers faithfully, or with label noise rate rho below 1/2.
- statement: Definition 3: an epsilon-extraction attack of complexity q and confidence gamma. Proven (Observation 1): any QS active learner with query complexity q_L yields an extraction attack of the same complexity. Proven (Example 2): d + 1 linearly independent queries give 0-extraction of a linear regression model. Proven (Prop 1): returning each label correctly with probability above 1/2 is broken, at a multiplicative cost of (8/(1 - 2 rho)^2) times a logarithmic factor in q_L. Remarks 3 and 4 state passive and active learning sample bounds (nu the optimal error in the class, theta the disagreement coefficient): a passive learner needs O~(((nu + epsilon)/epsilon^2) d) examples with a matching Omega~ lower bound, and disagreement-based active learning needs O~((nu^2/epsilon^2) d theta) queries. The remarks give these without proof in the v6 text read. Read in the PDF text.
- technique: a reduction from extraction to active learning, and majority voting over repeated queries.
- gap sign: existence only. Upper bounds by reduction, and the lower bounds are those of active learning.
- prominence: USENIX Security. OpenAlex cited_by_count 22 on the arXiv record (W2918814112, 2026-10-13).
- in_corpus: active-learning-model-extraction
- prerequisite: PAC and active learning, query complexity.
- tier: read

### L23
- key: L23
- title: Information Theoretic Lower Bounds for Information Theoretic Upper Bounds
- authors: Roi Livni
- venue: NeurIPS 2023 (Advances in Neural Information Processing Systems 36), pp. 37716-37727
- venue_evidence: Crossref record of https://doi.org/10.52202/075280-1640. The arXiv listing (2302.04925) names no venue.
- year: 2023
- link: https://arxiv.org/abs/2302.04925
- lane: I
- honest task: learn in stochastic convex optimization (SCO) with a dimension-free sample complexity.
- adversary task: none.
- bounded party: the learner's mutual information with its sample.
- resource: bits of mutual information.
- adversary class: none.
- assumption: SCO, true risk minimization (abstract).
- statement: Proven (abstract only, theorems not read): for true risk minimization in SCO the mutual information between model and sample must depend on the dimension, so mutual-information generalization bounds cannot explain SGD and regularized ERM, whose sample complexity is dimension-free. ADHLR24 states that its CMI-accuracy tradeoff answers an open question posed in this paper.
- technique: not read.
- gap sign: not a gap result. It is a limit on the information-theoretic generalization bounds.
- prominence: NeurIPS. OpenAlex cited_by_count 2 (W7133212988, 2026-10-13).
- in_corpus: no
- prerequisite: Xu and Raginsky style mutual-information bounds, SZ20.
- tier: skim

### KGKDT24
- key: KGKDT24
- title: Attack-Aware Noise Calibration for Differential Privacy
- authors: Bogdan Kulynych, Juan Felipe Gomez, Georgios Kaissis, Flavio du Pin Calmon, Carmela Troncoso
- venue: NeurIPS 2024 (Advances in Neural Information Processing Systems 37), pp. 134868-134901
- venue_evidence: Crossref record of https://doi.org/10.52202/079017-4286. The arXiv comment reads "Appears in NeurIPS 2024".
- year: 2024
- link: https://arxiv.org/abs/2407.02191
- lane: D
- honest task: calibrate the DP noise scale to a chosen attack-risk level rather than to epsilon.
- adversary task: inference attacks measured by sensitivity or specificity (abstract).
- bounded party: none stated in the abstract.
- resource: attack risk, as false-negative and false-positive rates.
- adversary class: not read.
- assumption: not read.
- statement: Proven (abstract only, theorems not read): calibrating noise directly to an attack-risk level gives a smaller noise scale and better accuracy at the same risk than the two-step route through epsilon.
- technique: not read.
- gap sign: not a gap result.
- prominence: NeurIPS. OpenAlex cited_by_count 13 (W4415800646, 2026-10-13).
- in_corpus: no
- prerequisite: DRS22.
- tier: skim

## 3. Triage

| key | title | venue | year | lane | gap sign | in_corpus | tier |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DN03 | Revealing information while preserving privacy | PODS | 2003 | I (C content) | adversary cheaper, price sqrt T on the curator | dinur-nissim-revealing-information | deep |
| DSSUV15 | Robust Traceability from Trace Amounts | FOCS | 2015 | I | existence of a threshold, cheap attacker | no | read |
| F20 | Does learning require memorization? | STOC | 2020 | I | not a gap result | no | deep |
| BBFST21 | When is memorization of irrelevant training data necessary | STOC | 2021 | I | existence only | no | deep |
| ADHLR24 | Information Complexity of SCO: Generalization, Memorization, and Tracing | ICML | 2024 | I | existence only | no | read |
| SZ20 | Reasoning About Generalization via CMI | COLT | 2020 | I | not a gap result | no | deep |
| DRS22 | Gaussian Differential Privacy | JRSS B | 2022 | D | not a gap result | no | read |
| SDSOJ19 | White-box vs Black-box: Bayes Optimal Strategies for MI | ICML | 2019 | I | not a gap result | no | read |
| HSU25 | The Sample Complexity of Membership Inference and Privacy Auditing | FOCS (to appear) | 2025 and 2026 | I | attacker dearer than trainer, equal with known covariance | haghifam-sample-complexity-mia | deep |
| BCH22 | Reconstructing Training Data with Informed Adversaries | IEEE S&P | 2022 | I (D content) | not a gap result | reconstructing-informed-adversaries | deep |
| GKCM22 | Bounding Training Data Reconstruction in Private (Deep) Learning | ICML | 2022 | I | not a gap result | no | read |
| GSS23 | Analyzing Privacy Leakage ... A Lesson From Fano | ICML | 2023 | I | not a gap result | no | skim |
| CLBM26 | A Sharp Transition in Data Reconstruction under DP | arXiv preprint | 2026 | I | not a gap result | no | read |
| SSTTM18 | Adversarially Robust Generalization Requires More Data | NeurIPS | 2018 | I | robust learner dearer, about sqrt d | robust-generalization-more-data | read |
| CBM18 | PAC-learning in the presence of adversaries | NeurIPS | 2018 | I | equal for halfspaces, dearer for constructed classes | pac-learning-evasion-adversaries | read |
| MHS19 | VC Classes are Adversarially Robustly Learnable, but Only Improperly | COLT | 2019 | I | dearer by at most exp(VC) | vc-classes-adversarially-robustly-learnable | read |
| HS26 | Adversarially Robust PAC Learning with Optimal VC Rates | arXiv preprint | 2026 | I | equal up to constants | no | read |
| CCGJY20 | Exploring Connections Between Active Learning and Model Extraction | USENIX Security | 2020 | I (D content) | existence only | active-learning-model-extraction | read |
| L23 | Information Theoretic Lower Bounds for Information Theoretic Upper Bounds | NeurIPS | 2023 | I | not a gap result | no | skim |
| KGKDT24 | Attack-Aware Noise Calibration for Differential Privacy | NeurIPS | 2024 | D | not a gap result | no | skim |

## 4. Searches that returned nothing, and what was opened but not sheeted

Searches with no usable result.

- Forward citers on OpenAlex (`filter=cites:`) of F20, BBFST21, SZ20, DN03 and DSSUV15, newest first and by count, with the vocabulary "memorization lower bound", "tracing", "information-theoretic", "conditional mutual information membership inference generalization bound", "reconstruction attack". The lists are dominated by surveys, unlearning and empirical memorization papers. The CMI query on SZ20 for 2023 onward returned no theory paper. The frontier in this file was found instead through the reference lists of the newer papers that were read (ADHLR24 cites F20, SZ20, BBFST21 and Livni. HSU25 cites DN03, DSSUV15 and SDSOJ19. CLBM26 cites BCH22. HS26 cites MHS19) and through WebSearch.
- "query complexity lower bound model extraction information-theoretic", "model stealing PAC query complexity lower bound number of queries". The results were upper bounds and algorithms. No tight information-theoretic query lower bound for extracting a trained neural network to a stated fidelity was found. The only extraction results with stated query counts that were opened are CCGJY20 and Carlini et al., "Stealing part of a production language model", ICML 2024 (PMLR 235, pp. 5680-5705, page https://proceedings.mlr.press/v235/carlini24a.html opened, abstract only: it recovers the embedding projection layer up to symmetries, with no lower bound read).
- dblp, by curl and by WebFetch. Both failed in this sandbox.

Opened but not sheeted, because of the cap of 20.

- Montasser, "Bagging Robustly Learns VC Classes with Linear Sample Complexity", arXiv:2608.13514, 13 August 2026. Thm 1 gives a realizable robust risk O(d/n + (1/n) log(1/delta)) from O(d*) bootstrap runs of robust ERM, Thm 2 gives the Omega(d*) oracle lower bound. Not in the corpus. Tier read. The oracle lower bound belongs to the algorithmic-class lane.
- Kaplan, Mansour, Nissim, Stemmer, "Bayesian Perspective on Memorization and Reconstruction", arXiv:2505.23658 (abstract page opened). Already in the corpus as kaplan-bayesian-memorization-reconstruction.
- Che, Xu, Yuan, "Memorization Is Not Extraction: Tight Differential-Privacy Bounds and Audit Blind Spots", arXiv:2608.27782, 27 August 2026 (abstract page opened). It bounds an adaptive extraction attack with a list budget under f-DP against an oblivious baseline. Arxiv-only, no citations, three authors, so it fails the prominence rule. Not in the corpus.

Not searched in this lane, so no negative result is claimed. Bayes-optimal membership inference beyond SDSOJ19. The origin of the hypothesis-testing view of DP before DRS22. Memory-bounded privacy adversaries, which the repository CLAUDE.md records as an open slot. Dinur, Stemmer, Woodruff and Zhou (EUROCRYPT 2023) bounds the space of the mechanism and is already in the corpus as dp-adaptive-analysis-bounded-space, so it is left to the algorithmic-class lane.

Leads seen only in a reference list or a search result, not opened, and therefore not listed as papers.

- From the reference lists of papers that were read. Sankararaman et al. (SOJH09) and Bun, Ullman, Vadhan (BUV14), cited by HSU25 as theory testbeds for membership inference on mean estimation. Hannun et al. (2021) on Fisher information leakage, cited by GKCM22. Xu and Raginsky, "Information-theoretic analysis of generalization capability of learning algorithms", NeurIPS 2017, pp. 2524-2533, and Haghifam, Dziugaite, Moran and Roy, "Towards a Unified Information-Theoretic Framework for Generalization", NeurIPS 34 (2021), both from the ADHLR24 reference list.
- From search results. Hayes, Mahloujifar, Balle, "Bounding Training Data Reconstruction in DP-SGD", arXiv:2302.07225, NeurIPS 2023. Kaissis et al., "Bounding data reconstruction attacks with the hypothesis testing interpretation of differential privacy", arXiv:2307.03928. "Privacy Auditing with One (1) Training Run" (OpenAlex W4376654471, 2023). Khouna et al., arXiv:2502.05325, query complexity of extracting tree ensembles. Chen, Klivans, Meka, "Efficiently Learning Any One Hidden Layer ReLU Network From Queries", NeurIPS 2021, an upper bound in queries. "Reconstruction Attacks on Aggressive Relaxations of Differential Privacy", Journal of Privacy and Confidentiality 2024, a citer of DN03.
