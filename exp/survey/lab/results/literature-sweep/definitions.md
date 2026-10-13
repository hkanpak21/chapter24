# Sweep 2026-10-13, lane definitions

Scope. (1) Formal security and privacy definitions of the ML field, game based or simulation based, with the quantifier over the adversary. (2) Systematizations, surveys and position papers, with what each covers and leaves out. Twenty papers are sheeted. Every sheet was opened on a publisher, proceedings, Crossref DOI or arXiv record, and for the content fields on the extracted text of the paper (two CRYPTO papers have Crossref records only, noted on their sheets). Citation counts are OpenAlex cited_by_count on 2026-10-13. OpenAlex splits a paper into an arXiv record and a published record, so the figure given is the larger record, and it undercounts.

## 1. What the field has in this lane

The definitions the field uses are mostly games or simulation conditions with an unbounded adversary, and the few that bound it do so by a security parameter, a circuit size or a query count. SCEKPSTZ23 (S&P 2023) unifies membership, attribute, property, DP distinguishing and reconstruction as games, orders them by reductions with an explicit constant, and states that most games do not limit the adversary's resources. CKMMNST25 (ITCS 2025) defines reconstruction resistance against the attacker's own baseline and proves that, for efficiently computable well-spread functions, its computational form is equivalent to one-wayness. MPRV09 (CRYPTO 2009) is the origin of definitions that quantify over probabilistic polynomial-time distinguishers, in an indistinguishability and a simulation form. GKVZ22 (FOCS 2022) and CGZ24 (COLT 2024) use the same quantifier for undetectable backdoors and undetectable watermarks, while ZEFVAB24 (ICML 2024) shows that strong unremovability fails against an efficient attacker with a quality oracle and a perturbation oracle. JYCDTCP21 (S&P 2021) is the one definition in this sweep that states the honest-against-adversary cost relation as an inequality, and its authors leave it as a conjecture. The definitions in this sweep with explicit resource parameters for both parties are from 2025 to 2026: GG25 and GTNP25 state gaps in samples, time and circuit size, and LEX26 (S&P 2026) states extraction as at least 2 to the power b expected queries and proves that indistinguishability and extractability are incomparable. Unlearning definitions (GGVZ19, GJNRSW21, GGHM20) are distributional closeness to retraining for an unbounded observer, and the only resource in them is the update cost against the retraining cost. No systematization found in this sweep organizes ML security by a complexity or information-theoretic unit. PMSW18 asks for PAC-style theory in its abstract and organizes by attack surface, goal and capability.

## 2. Sheets

Status words follow the CLAUDE.md convention (Proven, Heuristic, Empirical, Open).

### SCEKPSTZ23

- key: SCEKPSTZ23
- title: SoK: Let the Privacy Games Begin! A Unified Treatment of Data Inference Privacy in Machine Learning
- authors: Ahmed Salem, Giovanni Cherubin, David Evans, Boris Köpf, Andrew Paverd, Anshuman Suri, Shruti Tople, Santiago Zanella-Béguelin
- venue: IEEE Symposium on Security and Privacy (S&P)
- venue_evidence: https://doi.org/10.1109/SP46215.2023.10179281 (Crossref record, container "2023 IEEE Symposium on Security and Privacy (SP)"). arXiv comment: "to appear in 2023 IEEE Symposium on Security and Privacy".
- year: 2023
- link: https://arxiv.org/abs/2212.10986
- lane: D
- honest task: none. The training pipeline is fixed and not costed.
- adversary task: membership inference, attribute inference, property inference, DP distinguishing, data reconstruction, each as a game with a challenger.
- bounded party: none. Section II (paragraph "Resource constraints", page 4) says most game formulations do not limit the adversary, so they consider information-theoretic adversaries, and that limits can be set outside the game, by instrumenting an oracle, or inside the measure of success.
- resource: none in the games. The paper names query counts, memory and computation as possible limits.
- adversary class: all algorithms, as stated in the paragraph above.
- assumption: none
- statement: Proven (Section IV and appendix, Theorems 1 to 13). Definition 2 defines a reduction between games with an explicit constant c, in the style of concrete security, and Definition 3 defines p-resilience. Proposition 1 states that if G1 reduces to G2 with constant c and G1 is p-resilient, then G2 is p/c-resilient. Membership and attribute inference reduce to each other (Theorems 1 and 2, from Yeom et al.). Property inference separates from every other game. Reconstruction and DP distinguishing are the strongest threat models (Section IV.B).
- technique: game-based reductions, separation by explicit training pipelines, a Neyman-Pearson likelihood-ratio test inside one separation proof.
- gap sign: not a gap result. The constant c relates advantages across games, not adversary cost to honest cost.
- prominence: S&P (tier 1). OpenAlex cited_by_count 37 (2026-10-13).
- in_corpus: no
- prerequisite: cryptographic game definitions, advantage, concrete security, the YGFJ18 experiments.
- tier: deep

### YGFJ18

- key: YGFJ18
- title: Privacy Risk in Machine Learning: Analyzing the Connection to Overfitting
- authors: Samuel Yeom, Irene Giacomelli, Matt Fredrikson, Somesh Jha
- venue: IEEE Computer Security Foundations Symposium (CSF)
- venue_evidence: https://doi.org/10.1109/CSF.2018.00027 (Crossref record, container "2018 IEEE 31st Computer Security Foundations Symposium (CSF)")
- year: 2018
- link: https://arxiv.org/abs/1709.01604
- lane: D (with I)
- honest task: learn a model from n samples of D with low generalization error.
- adversary task: membership (Experiment 1) and attribute inference (Experiment 2) on a challenge point.
- bounded party: none
- resource: none for the adversary. The quantities are generalization gap, DP parameter and stability rate.
- adversary class: any algorithm. The text states no bound on the adversary's time or queries.
- assumption: none for Theorems 1 to 3. Theorem 4 assumes an ARO-stable learner, bounded loss, a finite domain, keyed pseudorandom functions, and that x determines (x,y).
- statement: Proven. Definition 4 defines membership advantage as 2 Pr[Exp = 1] minus 1, with a fair coin b and a challenge from the training set or from D, so the baseline advantage is zero by construction ("the only way to gain advantage is through access to the model", Section II). Definition 5 defines attribute advantage as a difference of success rates over b. Definition 6 replaces the second term with a Bayes optimal simulator. Theorem 1 states that an epsilon-DP learner gives membership advantage at most e^epsilon minus 1. Theorem 2 states that Adversary 1, which predicts non-membership with probability proportional to the loss at the challenge point, has advantage equal to the generalization error divided by the loss bound B. Theorem 4 states that an ARO-stable learner can be modified to leak membership with advantage 1 minus mu(n,D) minus 2^(-mk), so stability does not preclude leakage.
- technique: direct analysis of the experiment, a colluding learner built on pseudorandom functions, reductions between membership and attribute inference (Theorems 6 and 7).
- gap sign: not a gap result. Theorem 4 is an existence result.
- prominence: CSF. OpenAlex cited_by_count 951 (2026-10-13). Origin of the membership advantage definition used by SCEKPSTZ23.
- in_corpus: privacy-risk-overfitting
- prerequisite: differential privacy, generalization error, algorithmic stability.
- tier: read

### XD23

- key: XD23
- title: PAC Privacy: Automatic Privacy Measurement and Control of Data Processing
- authors: Hanshen Xiao, Srinivas Devadas
- venue: CRYPTO 2023 (Advances in Cryptology, LNCS)
- venue_evidence: https://doi.org/10.1007/978-3-031-38545-2_20 (Crossref record of the chapter, in the volume "Advances in Cryptology, CRYPTO 2023" (the volume title uses an en dash), DOI 10.1007/978-3-031-38545-2). The Springer page redirects to a login, so the chapter page itself was not read.
- year: 2023
- link: https://arxiv.org/abs/2210.03458
- lane: I (with D)
- honest task: compute and release M(X) for data X drawn from D.
- adversary task: return an estimate of X that meets a measure rho with probability at least 1 minus delta.
- bounded party: none. The mechanism's noise is calibrated to a simulated bound.
- resource: information (mutual information, f-divergence, posterior advantage) and the number of Monte Carlo trials in the proof procedure.
- adversary class: unrestricted. The text says no restriction is placed on D or on the adversary's strategy (below Definition 1).
- assumption: none. The adversary knows D and M.
- statement: Proven for the bounds, with an Empirical simulation step for the black-box case. Definition 1 defines (delta, rho, D)-PAC privacy as the impossibility of the reconstruction experiment. Definition 3 defines the optimal prior success rate, Definition 4 PAC advantage privacy as a bound on posterior over prior advantage, Definition 5 PAC membership privacy, Definition 6 PAC individual privacy. Theorem 1 bounds the posterior advantage by an f-divergence through the data processing inequality, and for KL by mutual information. Theorem 4 gives the noise, sample and confidence trade-off of the automatic Monte Carlo analysis. The abstract says the definition measures the information-theoretic hardness of recovery, is instance based and simulatable, and needs perturbation that can be O(1) where worst-case analysis needs order square root of d (abstract).
- technique: f-divergence data processing, Gaussian noise calibration, Monte Carlo estimation of mutual information for a black-box mechanism.
- gap sign: not a gap result. The comparison is the adversary with the output against the adversary with the prior only (Definitions 3 and 4).
- prominence: CRYPTO (tier 1). OpenAlex cited_by_count 7 (2026-10-13).
- in_corpus: no source page. The phrase "PAC privacy" appears in kaplan-bayesian-memorization-reconstruction and xiao-formal-privacy-proof-data-encoding.
- prerequisite: f-divergence, mutual information, Fano-type reconstruction bounds, differential privacy.
- tier: deep

### CKMMNST25

- key: CKMMNST25
- title: Data Reconstruction: When You See It and When You Don't
- authors: Edith Cohen, Haim Kaplan, Yishay Mansour, Shay Moran, Kobbi Nissim, Uri Stemmer, Eliad Tsfadia
- venue: Innovations in Theoretical Computer Science (ITCS) 2025, LIPIcs
- venue_evidence: https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.39 (page reads "16th Innovations in Theoretical Computer Science Conference (ITCS 2025)")
- year: 2025
- link: https://arxiv.org/abs/2405.15753
- lane: D (with C)
- honest task: release M(S) for a dataset S.
- adversary task: output z with R(S,z) = 1 (reconstruction), or an L-program A that outputs a solution of the extraction relation (Definition 1.13).
- bounded party: the attacker, in Appendix C (polynomial in lambda). The main text bounds nothing, and Definition 1.13 bounds the attacker's program length.
- resource: success probability against a baseline, program length in Kolmogorov complexity K_L (Definition 1.12), and time poly(lambda) in Appendix C.
- adversary class: all attackers (Definition 1.6), non-uniform poly(lambda)-time attackers (Definition C.1), L-programs of length |A| (Definition 1.13).
- assumption: none for Definition 1.6. Theorem C.5 assumes f efficiently computable and well-spread (Definition C.4) and gives equivalence with one-wayness.
- statement: Proven. Definition 1.4 (from BCH22 and CHSS24) compares the attacker with a fixed baseline. Definition 1.6 (Narcissus resiliency) requires, for every attacker, that its success on the real dataset is at most e^epsilon times its success on a fresh dataset from the same distribution plus delta, so the attacker is its own baseline. Section 2 and Appendix C show that it contains DP, membership resilience, one-wayness and encryption security as special cases. Theorem C.5 states that an efficiently computable well-spread f is one-way if and only if M_f is computationally Narcissus resilient. The abstract says "a single all-encompassing definition may not exist".
- technique: self-referential baseline, Kolmogorov complexity of the solution set, reduction to one-wayness.
- gap sign: equivalence with a hardness assumption (Theorem C.5, conditional). Otherwise not a gap result.
- prominence: ITCS. OpenAlex cited_by_count 1 (published record, 2026-10-13).
- in_corpus: cohen-data-reconstruction
- prerequisite: the baseline definition of BCH22, one-way functions, Kolmogorov complexity.
- tier: deep

### CCGJY20

- key: CCGJY20
- title: Exploring Connections Between Active Learning and Model Extraction
- authors: Varun Chandrasekaran, Kamalika Chaudhuri, Irene Giacomelli, Somesh Jha, Songbai Yan
- venue: USENIX Security Symposium
- venue_evidence: https://www.usenix.org/conference/usenixsecurity20/presentation/chandrasekaran (page reads "29th USENIX Security Symposium (USENIX Security 20), 2020")
- year: 2020
- link: https://arxiv.org/abs/1811.02054
- lane: D (with A)
- honest task: active learning of a public hypothesis class F in the query synthesis scenario, with query complexity q(epsilon, delta) (Definition 2).
- adversary task: epsilon-extraction of the server's model f* in F through the query interface (Definition 3).
- bounded party: the adversary, by a query budget q.
- resource: queries.
- adversary class: any adversary using at most q queries, with F public.
- assumption: none. Proposition 1 needs a server whose label noise rho on the target is below one half.
- statement: Proven. Definition 3 states that an adversary implements an epsilon-extraction attack of complexity q and confidence gamma against F if the extraction experiment returns 1 with probability at least gamma for every f* in F. Proposition 1 states that an active learner with query complexity q(epsilon, delta) gives an extraction adversary with confidence 1 minus 2 delta whose query count is q(epsilon, delta) times a logarithmic factor and a noise factor of order 1/(1 minus 2 rho)^2 (exact constant in the paper). Example 2 gives equation solving as a 0-extraction of linear regression with d+1 queries and confidence 1. The abstract says the paper takes a first step by formalizing model extraction (abstract).
- technique: reduction from extraction to active learning, repeated queries with majority vote against label noise.
- gap sign: equal up to a logarithmic and a noise factor. The result is an upper bound on the adversary's cost and states no lower bound.
- prominence: USENIX Security (tier 1). OpenAlex cited_by_count 22 (arXiv record, 2026-10-13).
- in_corpus: active-learning-model-extraction
- prerequisite: PAC learning, active learning label complexity.
- tier: read

### MPRV09

- key: MPRV09
- title: Computational Differential Privacy
- authors: Ilya Mironov, Omkant Pandey, Omer Reingold, Salil Vadhan
- venue: CRYPTO 2009 (Advances in Cryptology, LNCS 5677)
- venue_evidence: https://doi.org/10.1007/978-3-642-03356-8_8 (Crossref record of the chapter, in the volume "Advances in Cryptology, CRYPTO 2009" (Crossref prints a hyphen), DOI 10.1007/978-3-642-03356-8). The Springer page redirects to a login, so the chapter page itself was not read.
- year: 2009
- link: https://doi.org/10.1007/978-3-642-03356-8_8
- lane: D (with C)
- honest task: release f(D) with DP-like privacy and accuracy.
- adversary task: distinguish f(D) from f(D') for adjacent data sets, or f(D) from a DP simulator F(D).
- bounded party: the adversary.
- resource: time (non-uniform probabilistic polynomial time in the security parameter kappa) and advice of size p(kappa).
- adversary class: non-uniform PPT distinguishers (Definitions 3 and 4).
- assumption: none for the definitions. The protocol of Theorem 5 uses additive homomorphic encryption.
- statement: Proven. Definition 3 (IND-CDP) bounds Pr[A(f(D)) = 1] by e^epsilon Pr[A(f(D')) = 1] plus a negligible term for every PPT A. Definition 4 (SIM-CDP) requires an epsilon-DP mechanism F with f(D) and F(D) computationally indistinguishable. Theorem 1 gives SIM-CDP implies SIM-forall-exists-CDP implies IND-CDP. Theorem 3 gives that IND-CDP with epsilon in O(log kappa) implies SIM-forall-exists-CDP, by an extension of the dense model theorem (Theorem 2). A remark after Definition 3 states that the computational analogue of pure epsilon-DP (delta zero) equals information-theoretic epsilon-DP. The abstract states that a two-party distance approximation protocol is substantially more accurate when it is only computationally DP (Theorems 5 and 6).
- technique: pseudodense sets and the dense model theorem, additive homomorphic encryption for the protocol.
- gap sign: existence only (abstract: more accurate mechanisms exist under the computational notion). The separation is not stated as a theorem in what was read.
- prominence: CRYPTO (tier 1). OpenAlex cited_by_count 231 (2026-10-13).
- in_corpus: computational-differential-privacy
- prerequisite: differential privacy, computational indistinguishability, non-uniform adversaries.
- tier: deep

### GGVZ19

- key: GGVZ19
- title: Making AI Forget You: Data Deletion in Machine Learning
- authors: Antonio Ginart, Melody Guan, Gregory Valiant, James Zou (arXiv prints Melody Y. Guan)
- venue: Advances in Neural Information Processing Systems 32 (NeurIPS 2019)
- venue_evidence: https://papers.nips.cc/paper/2019/hash/cb79f8fa58b91d3af6c9c991f63962d3-Abstract.html
- year: 2019
- link: https://arxiv.org/abs/1907.05012
- lane: D
- honest task: train A on D, then delete a point i and return a model with the distribution of A(D without i).
- adversary task: none. The observer must not tell the deletion output from retraining.
- bounded party: the deleter, by amortized runtime. The observer is not bounded.
- resource: time (amortized runtime of m deletions against the Omega(n) cost of training) and the memory of the stored metadata (posed as a question in Section 3).
- adversary class: unbounded observer for exact deletion. The robust variant (Definition A.3) adds an adaptive adversary that issues deletion requests with read access to the server state.
- assumption: none
- statement: Proven. Definition 3.1 defines a data deletion operation by equality in distribution of A(D without i) and R_A(D, A(D), i). Section 3 states that retraining is a trivial deletion operation, so "the challenge of data deletion is computational". Definition A.6 defines delta-approximate deletion as a one-sided ratio bound. Appendix A compares exact deletion with perfect secrecy and retraining with the one-time pad. Theorem 4.1 and Proposition 4.2 give deletion-efficient algorithms for Q-k-means and DC-k-means.
- technique: online amortized analysis, quantization and divide-and-conquer to localize the influence of a point.
- gap sign: honest update cheaper than honest retraining, by design, for k-means (existence). No adversary cost is compared.
- prominence: NeurIPS (tier 1). OpenAlex cited_by_count 67 (arXiv record, 2026-10-13).
- in_corpus: no
- prerequisite: k-means, online algorithms, differential privacy (Appendix A).
- tier: read

### GJNRSW21

- key: GJNRSW21
- title: Adaptive Machine Unlearning
- authors: Varun Gupta, Christopher Jung, Seth Neel, Aaron Roth, Saeed Sharifi-Malvajerdi, Chris Waites
- venue: Advances in Neural Information Processing Systems 34 (NeurIPS 2021)
- venue_evidence: https://proceedings.neurips.cc/paper/2021/hash/87f7ee4fdb57bdfd52179947211b7ebb-Abstract.html
- year: 2021
- link: https://arxiv.org/abs/2106.04378
- lane: D (with I)
- honest task: update a model after a sequence of additions and deletions at a cost below retraining.
- adversary task: the update requester chooses the next update as a function of the published models (Definition 2.2).
- bounded party: none
- resource: information (differential privacy parameter, max-information).
- adversary class: every update requester, adaptive or not, and every measurable event (Definition 2.3).
- assumption: none for the definition. Theorem 4.1 assumes the publishing functions are differentially private.
- statement: Proven. Definition 2.3 defines (alpha, beta, gamma)-unlearning: for all data sets and update requesters, at every round, with probability at least 1 minus gamma over the update sequence, every event E has probability under the unlearning algorithm at most e^alpha times its probability under retraining plus beta. The guarantee is one-sided, following GGVZ19 (Remark 2.1). Theorem 3.1 reduces adaptive guarantees to non-adaptive ones through max-information. Theorem 4.1 gives unlearning guarantees when the publishing functions are DP, and Theorem 4.2 gives run-time guarantees. Theorem 5.1 states that there are learning and unlearning algorithms in the SISA framework that are not (alpha, beta, gamma)-unlearning for any alpha and any beta and gamma below 1/4. The abstract reports a practical attack on SISA with CIFAR-10, MNIST and Fashion-MNIST (Empirical).
- technique: DP and its connection to max-information (Theorem 2.1, from Rogers et al.).
- gap sign: not a gap result.
- prominence: NeurIPS (tier 1). OpenAlex cited_by_count 42 (arXiv record, 2026-10-13).
- in_corpus: no
- prerequisite: GGVZ19, differential privacy, adaptive data analysis.
- tier: read

### GGHM20

- key: GGHM20
- title: Certified Data Removal from Machine Learning Models
- authors: Chuan Guo, Tom Goldstein, Awni Hannun, Laurens van der Maaten (the PMLR page prints Laurens Van Der Maaten)
- venue: International Conference on Machine Learning (ICML 2020), PMLR 119
- venue_evidence: https://proceedings.mlr.press/v119/guo20c.html
- year: 2020
- link: https://arxiv.org/abs/1911.03030
- lane: D (with I)
- honest task: remove a training point x from A(D) with a mechanism M that avoids retraining.
- adversary task: distinguish M(A(D), D, x) from A(D without x).
- bounded party: none
- resource: information (max-divergence epsilon, slack delta) traded against removal efficiency.
- adversary class: every event T in the hypothesis set, so information-theoretic.
- assumption: L2-regularized linear models with a differentiable convex loss, and loss perturbation to mask the residual.
- statement: Proven for the definition and for the mechanism. Section 2 defines epsilon-certified removal (Equation 1): the ratio of the probabilities that M(A(D), D, x) and A(D without x) land in T lies in [e^(-epsilon), e^epsilon] for all T, D, x, and gives an (epsilon, delta) version. Section 2 places retraining from scratch and DP at the two ends of the utility and removal-efficiency spectrum. The mechanism is a Newton step whose residual decreases quadratically with training set size (abstract).
- technique: Newton step, objective perturbation (Chaudhuri et al. 2011).
- gap sign: not a gap result. Removal is cheaper than retraining by design and no adversary cost is compared.
- prominence: ICML (tier 1). OpenAlex cited_by_count 17 (arXiv record, 2026-10-13). The count is low for this paper, so treat it as an OpenAlex artefact.
- in_corpus: no
- prerequisite: differential privacy max-divergence, convex empirical risk minimization.
- tier: skim

### TJSP22

- key: TJSP22
- title: On the Necessity of Auditable Algorithmic Definitions for Machine Unlearning
- authors: Anvith Thudi, Hengrui Jia, Ilia Shumailov, Nicolas Papernot
- venue: USENIX Security Symposium
- venue_evidence: https://www.usenix.org/conference/usenixsecurity22/presentation/thudi (page reads "31st USENIX Security Symposium (USENIX Security 22), 2022")
- year: 2022
- link: https://arxiv.org/abs/2110.11891
- lane: D
- honest task: unlearn a point, exactly by retraining or approximately by an update.
- adversary task: forge a data set D' disjoint from D that produces the same model or the same training log.
- bounded party: none in the theorems.
- resource: probability, minibatch size b, number of samples from D.
- adversary class: a forging adversary with freedom over b and unbounded sampling access to D (Theorem 3).
- assumption: i.i.d. data, a minibatch-mean SGD update, bounded variance (Theorems 2 and 3).
- statement: Proven (Theorems 1 to 3). The abstract states that approximate unlearning defined by closeness in parameter space is incorrect because different data sets can give the same model, and that even for a given training trajectory one cannot prove the absence of a data point, so unlearning is defined only at the algorithm level. Theorem 1 characterizes the epsilon-zero equivalence classes (two data sets are forgeable if and only if they give the same sequence of logs). Theorem 2 gives an explicit lower bound on the probability that D' forges D. Theorem 3 states that for every epsilon and almost every data set D there is a larger data set that a disjoint data set forges. Empirical: forging experiments.
- technique: gradient-log equivalence classes, Chebyshev-type concentration.
- gap sign: existence only (negative result on verification of unlearning from the model).
- prominence: USENIX Security (tier 1). OpenAlex cited_by_count 13 (arXiv record, 2026-10-13).
- in_corpus: auditable-unlearning-definitions
- prerequisite: SGD, exact versus approximate unlearning, GJNRSW21.
- tier: read

### ERCGOP25

- key: ERCGOP25
- title: Verifiable and Provably Secure Machine Unlearning
- authors: Thorsten Eisenhofer, Doreen Riepel, Varun Chandrasekaran, Esha Ghosh, Olga Ohrimenko, Nicolas Papernot
- venue: IEEE Conference on Secure and Trustworthy Machine Learning (SaTML 2025)
- venue_evidence: https://doi.org/10.1109/SaTML64287.2025.00033 (Crossref record, container "2025 IEEE Conference on Secure and Trustworthy Machine Learning (SaTML)"). arXiv comment: "Accepted at IEEE SaTML2025".
- year: 2025
- link: https://arxiv.org/abs/2210.09126
- lane: D (with C)
- honest task: the server trains on D with a proof, then unlearns a point d and proves correct execution and that d is not in the new data set.
- adversary task: a malicious server produces an accepted proof of unlearning for data it did not unlearn.
- bounded party: the adversary.
- resource: time (PPT), and the prover overhead (Table I).
- adversary class: PPT adversaries with an extractor, over benign auxiliary inputs (Definition 2, game GameUnlearn, Figure 2).
- assumption: a collision-resistant hash function and a secure (knowledge-sound) SNARK (Theorem 2). A complete SNARK and the hash give completeness (Theorem 1).
- statement: Proven. The abstract states that this is the first cryptographic definition of verifiable unlearning, and that the unlearning technique is abstracted as admissible functions. Definition 1 defines completeness, and Definition 2 defines unlearning security as a negligible winning probability for every PPT adversary. The protocol is instantiated with SNARKs and hash chains and implemented for linear regression, logistic regression and neural networks (abstract). Empirical: run-time overhead of the prover (Table I).
- technique: SNARK proof of training and unlearning steps, hash-chain non-membership.
- gap sign: not a gap result. Security by reduction, with the honest prover's overhead measured.
- prominence: SaTML (not on the brief's venue list). OpenAlex cited_by_count 15 (published record) and 5 (arXiv record), 2026-10-13. Included as the origin of the cryptographic unlearning definition.
- in_corpus: no
- prerequisite: SNARK knowledge soundness, collision-resistant hashing, TJSP22.
- tier: read

### GKVZ22

- key: GKVZ22
- title: Planting Undetectable Backdoors in Machine Learning Models
- authors: Shafi Goldwasser, Michael P. Kim, Vinod Vaikuntanathan, Or Zamir
- venue: IEEE Symposium on Foundations of Computer Science (FOCS 2022), extended abstract
- venue_evidence: https://doi.org/10.1109/FOCS54457.2022.00092 (Crossref record, container "2022 IEEE 63rd Annual Symposium on Foundations of Computer Science (FOCS)")
- year: 2022
- link: https://arxiv.org/abs/2204.06974
- lane: C (with D)
- honest task: train a hypothesis from D with Train (Definition 3.1), and detect a backdoor.
- adversary task: plant a backdoor (Backdoor, Activate) that flips any input under a small perturbation while remaining undetectable (Definitions 4.1, 4.2).
- bounded party: the detector.
- resource: time, in three access modes.
- adversary class: probabilistic polynomial-time distinguishers that may sample D, in three variants of Definition 4.6: white-box (full description), black-box (query access), and (Q, epsilon) statistic-access (a class Q of statistical queries).
- assumption: strongly unforgeable digital signatures (Theorem 5.4). Hardness of Continuous LWE (Theorem 6.4 with Theorem 6.5 from Bruna et al.) for white-box undetectability of random Fourier feature models. Sparse PCA for random ReLU networks (abstract). Worst-case lattice hardness in Theorem 2.2 (informal).
- statement: Proven, conditional. Definition 4.6 requires the hypotheses from Train and from Backdoor to be indistinguishable for the stated distinguisher class. Definition 4.7 defines non-replicability. Theorem 5.4 gives a black-box undetectable, non-replicable backdoor in any model from signatures. Theorem 6.4 gives a white-box undetectable backdoor for random Fourier features under Hypothesis 3.7, which the abstract identifies as the hardness of Continuous LWE. Section 7 (Theorem 7.1, title read, statement not read) concerns neutralizing backdoors.
- technique: signature-triggered backdoors, tampering with the random coins of random Fourier features.
- gap sign: adversary cheaper than defender (planting costs the training cost, detection is infeasible for PPT), conditional on the assumptions.
- prominence: FOCS (tier 1). OpenAlex cited_by_count 40 (published record) and 9 (arXiv record), 2026-10-13.
- in_corpus: planting-undetectable-backdoors
- prerequisite: digital signatures, LWE, indistinguishability, random Fourier features.
- tier: deep

### CGZ24

- key: CGZ24
- title: Undetectable Watermarks for Language Models
- authors: Miranda Christ, Sam Gunn, Or Zamir
- venue: Conference on Learning Theory (COLT 2024), PMLR 247
- venue_evidence: https://proceedings.mlr.press/v247/christ24a.html
- year: 2024
- link: https://arxiv.org/abs/2306.09194
- lane: C (with D)
- honest task: sample from a language model, embed a watermark and detect it with a secret key.
- adversary task: distinguish watermarked output from the model's own output (undetectability), and remove the watermark.
- bounded party: the distinguisher.
- resource: time and adaptive queries to Model and to the watermarked model.
- adversary class: polynomial-time distinguishers with adaptive oracle access to both (Definition 9).
- assumption: one-way functions (abstract).
- statement: Proven. Definition 9 states that the oracle outputs of Model and of the watermarked model differ by a negligible amount for every polynomial-time distinguisher, so output quality is identical. Definitions 6 to 8 define soundness, completeness and substring completeness. Section 6.2 gives an attack that removes the watermark from any undetectable scheme for prefix-specifiable models by sampling token by token, and the paper concludes that no undetectable scheme is completely unremovable. The paper adds that removal may need significantly more resources and does not quantify them.
- technique: empirical entropy of the response (Section 2.3), a construction first in the random oracle model with high min-entropy (Section 3.1) and then from one-way functions.
- gap sign: undetectability holds against PPT under a one-way function (conditional). Unremovability fails, with the attacker's cost not quantified (existence only).
- prominence: COLT (tier 1). OpenAlex cited_by_count 9 (arXiv record, 2026-10-13).
- in_corpus: undetectable-watermarks-lm
- prerequisite: pseudorandom functions, language model sampling, computational indistinguishability.
- tier: read

### ZEFVAB24

- key: ZEFVAB24
- title: Watermarks in the Sand: Impossibility of Strong Watermarking for Language Models (PMLR title). arXiv v5 prints "for Generative Models".
- authors: Hanlin Zhang, Benjamin L. Edelman, Danilo Francati, Daniele Venturi, Giuseppe Ateniese, Boaz Barak
- venue: International Conference on Machine Learning (ICML 2024), PMLR 235
- venue_evidence: https://proceedings.mlr.press/v235/zhang24o.html
- year: 2024
- link: https://arxiv.org/abs/2311.04378
- lane: C (with D)
- honest task: watermark a generative model and detect with a secret key while preserving quality Q.
- adversary task: erase the watermark while keeping quality Q(x, y') at least Q(x, y) (Definition 5).
- bounded party: the adversary.
- resource: queries to a perturbation oracle, about t_max over epsilon_pert, where t_max is the mixing time of the random walk (Theorem 2).
- adversary class: an efficient, oracle-aided, key-independent adversary with black-box access to the model, a quality oracle Q and a perturbation oracle P. The bound is a query bound in an oracle model, not a standard-model time bound.
- assumption: a quality oracle, a perturbation oracle that preserves quality with probability epsilon_pert and whose quality-q graph is irreducible and aperiodic, and a false positive rate epsilon_pos (Theorem 2).
- statement: Proven under those assumptions (Theorem 2, a simplified form of Theorem 6 in Appendix C). Definition 5 states that an adversary epsilon-breaks a scheme if, for every model and prompt, it produces an undetected output of at least the original quality with probability at least epsilon. Theorem 2 gives an adversary that epsilon-breaks any such scheme with epsilon about (1 minus epsilon_pos) over 2. The scope is strong watermarking, and the paper excludes weak watermarking with an edit-distance limited attacker. The abstract argues that the oracles can be built by an attacker weaker than the model. Empirical: the attack removes the watermarks of three LLM schemes and two vision-language schemes with minor quality loss (abstract).
- technique: rejection sampling with a random walk on high-quality outputs, mixing-time analysis.
- gap sign: adversary cheaper than the honest party (abstract, argued), existence of an attack under oracle assumptions.
- prominence: ICML (tier 1). OpenAlex cited_by_count 9 (arXiv record, 2026-10-13).
- in_corpus: no
- prerequisite: CGZ24, Markov chain mixing, watermarking schemes for language models.
- tier: deep

### JYCDTCP21

- key: JYCDTCP21
- title: Proof-of-Learning: Definitions and Practice
- authors: Hengrui Jia, Mohammad Yaghini, Christopher A. Choquette-Choo, Natalie Dullerud, Anvith Thudi, Varun Chandrasekaran, Nicolas Papernot
- venue: IEEE Symposium on Security and Privacy (S&P 2021)
- venue_evidence: https://doi.org/10.1109/SP40001.2021.00106 (Crossref record, container "2021 IEEE Symposium on Security and Privacy (SP)")
- year: 2021
- link: https://arxiv.org/abs/2103.05633
- lane: D (with C)
- honest task: train a model and record a proof, then verify at a cost below training.
- adversary task: spoof a proof with less computation, by retraining, stochastic, structurally correct or distillation-based spoofing (Section IV-A).
- bounded party: both prover and adversary, by expected cost.
- resource: expected computation and storage cost.
- adversary class: spoofers with full knowledge of architecture, weights and data, and without access to the trainer's randomness (Section IV-A).
- assumption: none proven. Conjecture 1.
- statement: Proven for the entropy results and Open for the security claim. Definition 1 defines a PoL as the tuple (W, I, H, A). Property 1 requires expected verifier cost at most expected trainer cost. Property 2 requires expected trainer cost at most expected cost of any spoofing strategy other than honest training. Definition 2 calls a spoof dishonest if its expected cost is below the trainer's. Theorem 1 (entropy growth) and Theorem 2 (reverse entropy growth) support the claim. The security analysis (Section VII) presents Conjecture 1, that inverting a training sequence by numerical root finding costs at least as much as training, because the authors "are not aware of a mechanism to prove this formally". Later work finds attacks (pol-more-broken, in corpus).
- technique: checkpoint re-execution with a distance threshold, entropy argument.
- gap sign: adversary at least as dear as honest (required by Property 2), unproven.
- prominence: S&P (tier 1). OpenAlex cited_by_count 75 (published record) and 5 (arXiv record), 2026-10-13.
- in_corpus: proof-of-learning
- prerequisite: SGD, checkpointing, spoofing and forging (TJSP22).
- tier: deep

### GG25

- key: GG25
- title: A Cryptographic Perspective on Mitigation vs. Detection in Machine Learning
- authors: Greg Gluch, Shafi Goldwasser
- venue: arXiv preprint (v2, 10 Jul 2025). The PDF states "Preprint. Under review."
- venue_evidence: https://arxiv.org/abs/2504.20310. A web search for a published version found none.
- year: 2025
- link: https://arxiv.org/abs/2504.20310
- lane: C (with D)
- honest task: a trainer and defender: P_TRAIN produces a classifier and a private key, then P_DETECT flags or P_MITIGATE repairs adversarial inputs at inference time (Definitions 2 and 3).
- adversary task: a verifier V crafts inference-time inputs on which the classifier errs and the defense does not respond.
- bounded party: both. P_TRAIN, P_DETECT and V run in time polynomial in n, log(1/epsilon), 1/delta.
- resource: samples (K_TRAIN, K_DETECT, K_MITIGATE, K_ATTACK) and time (T_TRAIN, T_MITIGATE, T_ATTACK), Definition 4.
- adversary class: polynomial-size V (Soundness in Definition 2).
- assumption: Theorem 1 assumes identity-based fully homomorphic encryption, a publicly verifiable zk-SNARK and strongly unforgeable signatures. Theorem 2 assumes average-case non-parallelizing languages, incrementally verifiable computation and identity-based FHE.
- statement: Proven, conditional. The abstract states that defense by detection and defense by mitigation are equivalent for classification and separate for generative tasks. Theorem 1 states that for a task and every sample budget K, a defense by mitigation exists with K_TRAIN equal to K and K_MITIGATE of order square root of K, while no defense by detection exists with K_TRAIN equal to K even when K_DETECT is polynomial in n and K_ATTACK is O(1). Theorem 2 states that, with eta the gap of an average-case non-parallelizing language, a defense by mitigation exists with T_TRAIN equal to T, T_MITIGATE of order T^(1/(2 eta)) and T_ATTACK of order T, while no defense by detection exists with T_TRAIN equal to T even when T_DETECT is polynomial and T_ATTACK is of order T^(1/(2 eta)).
- technique: cryptographic puzzles embedded in the learning task, SNARKs and IVC to make mitigation cheap and detection impossible.
- gap sign: the defender's repair is strictly cheaper than training, and an attack against detection is cheaper than training. Three parties, two gaps.
- prominence: arXiv preprint, OpenAlex cited_by_count 0. Included for fit to the organizing notion and not for prominence. The repo CLAUDE.md names this paper as occupying the restricted-class attacker unit in cryptography.
- in_corpus: no source page. Named in CLAUDE.md, AGENTS.md, wiki/log.md and wiki/analyses/native-asymmetry-in-learning.md.
- prerequisite: IB-FHE, zk-SNARK, IVC, learning tasks as ensembles.
- tier: deep

### GTNP25

- key: GTNP25
- title: The Good, the Bad and the Ugly: Meta-Analysis of Watermarks, Transferable Attacks and Adversarial Defenses
- authors: Grzegorz Głuch, Berkant Turan, Sai Ganesh Nagarajan, Sebastian Pokutta (arXiv spelling. The NeurIPS page prints Greg Gluch.)
- venue: Advances in Neural Information Processing Systems 38 (NeurIPS 2025)
- venue_evidence: https://proceedings.neurips.cc/paper_files/paper/2025/hash/736f811dffcd2cb1150d82417a0bd70b-Abstract-Conference.html. Crossref DOI 10.52202/085713-2683.
- year: 2025
- link: https://arxiv.org/abs/2410.08864
- lane: C (with D)
- honest task: learn a classifier for a task with circuit complexity S(n), embed a watermark, or defend.
- adversary task: remove the watermark, break the defense, or run a transferable attack that produces in-distribution queries fooling every efficient defender.
- bounded party: both, by circuit size S_A(n) and S_B(n).
- resource: circuit size.
- adversary class: circuits of size S_B(n) (Definitions 3 to 5, informal, with formal versions in Appendix C).
- assumption: none for Theorem 1 (a minimax argument, Theorem 4 of Lipton and Young). Fully homomorphic encryption with IND-CPA security for Theorem 2.
- statement: Proven. Definition 3 gives a backdoor-based watermark with correctness, uniqueness, unremovability and undetectability, the last two against provers of size S_B. Theorem 1 (informal) states that for every epsilon, size S and task learnable to error epsilon with circuit size S(n), at least one of three exists: a watermark with removal adversaries up to size o(sqrt(S)/log S), a defense against attackers up to size o(sqrt(S)/log S) with a defender of size O(S), or a transferable attack of size S against defenders of size S. Theorem 2 (informal) gives a task with a transferable attack of size about 1/epsilon against defenders of size Omega(1/epsilon^2). Theorem 3 (informal) states that a transferable attack implies an (S_A, S_B)-EFID pair, an efficiently samplable, statistically far, computationally indistinguishable pair. The abstract adds that bounded VC dimension tasks admit defenses against all attackers and a subclass admits watermarks secure against fast adversaries.
- technique: zero-sum game on a large payoff matrix (Lipton and Young), FHE-based construction, EFID pairs.
- gap sign: unremovability and defense hold only against adversaries smaller than the honest party by a square root factor, and a transferable attack with a quadratic size gap exists for one task. Adversary cheaper than honest.
- prominence: NeurIPS (tier 1). OpenAlex cited_by_count 0 (published and arXiv records, 2026-10-13).
- in_corpus: no
- prerequisite: GKVZ22, backdoor-based watermarking, FHE, minimax theorem.
- tier: deep

### LEX26

- key: LEX26
- title: Beyond Indistinguishability: Measuring Extraction Risk in LLM APIs
- authors: Ruixuan Liu, David Evans, Li Xiong
- venue: IEEE Symposium on Security and Privacy (S&P 2026)
- venue_evidence: https://doi.org/10.1109/SP63933.2026.00165 (Crossref record, container "2026 IEEE Symposium on Security and Privacy (SP)", issued 2026-05-18). arXiv v1 dated 20 Apr 2026.
- year: 2026
- link: https://arxiv.org/abs/2604.18697
- lane: D (with I)
- honest task: serve an LLM through an API with a sampling and decoding configuration.
- adversary task: make the API emit a protected l-gram subsequence of the training data.
- bounded party: the adversary.
- resource: expected number of independent black-box trials (queries), at least 2^b.
- adversary class: black-box adversary in a worst-case extraction game (Definition 2).
- assumption: none for Definition 2. A local log-Lipschitz regularity assumption (Assumption 1) for the approximate-extraction extension.
- statement: Proven for the separations and Empirical for the estimator. Definition 2 defines (l, b)-inextractability as an expected number of independent trials of at least 2^b to extract any subsequence of at least l grams of the protected set, modelled on the security level in cryptography (Section 3.1). Theorem 2 states that resilience to DP distinguishing does not imply resilience to extraction. Theorem 3 states that resilience to extraction does not bound DP distinguishing. Lemma 2 gives the equivalence of inextractability and min-entropy. Definition 3 adds a failure probability delta, and Theorem 5 extends to untargeted extraction. The abstract states that indistinguishability and inextractability are incomparable.
- technique: rank-based upper bound on greedy and probabilistic extraction, min-entropy argument.
- gap sign: not a gap result. The bound is absolute, in queries, with no comparison to honest cost.
- prominence: S&P (tier 1). OpenAlex cited_by_count 0 (2026-10-13). Cites SCEKPSTZ23.
- in_corpus: no
- prerequisite: SCEKPSTZ23 games, DP distinguishing, min-entropy, LLM decoding.
- tier: deep

### PMSW18

- key: PMSW18
- title: SoK: Security and Privacy in Machine Learning (EuroS&P title). The arXiv title is "Towards the Science of Security and Privacy in Machine Learning".
- authors: Nicolas Papernot, Patrick McDaniel, Arunesh Sinha, Michael P. Wellman
- venue: IEEE European Symposium on Security and Privacy (EuroS&P 2018)
- venue_evidence: https://doi.org/10.1109/EuroSP.2018.00035 (Crossref record, container "2018 IEEE European Symposium on Security and Privacy"). The PDF header reads "2018 IEEE European Symposium on Security and Privacy".
- year: 2018
- link: https://arxiv.org/abs/1611.03814
- lane: D
- honest task: not a result paper.
- adversary task: it taxonomizes attacks by attack surface (training, inference), goals (confidentiality, integrity, availability) and capabilities (Section 3).
- bounded party: none as a rule. Section 4 notes that an unbounded poisoning adversary can make the learner learn any function, so the attacks it lists bound the adversary. Section 5 says a key metric for comparing extraction attacks is the information the oracle returns and the number of oracle queries, and it cites Lowd et al. for evasion cost in queries and ACRE learnability, which is NP-hard for discrete features.
- resource: query counts appear as a metric in Section 5. No resource organizes the paper.
- adversary class: not stated as a quantifier.
- assumption: none
- statement: Systematization. The abstract states that a theoretical understanding of the sensitivity of ML algorithms to the data they analyze, "à la PAC theory", will foster a science of security and privacy in ML. What it covers is the threat model and the attack and defense catalogue as of 2018. What it leaves out is any organization by a computational or information unit. Reading of Section 3 (Threat Model): it lists surface, goal and capability and no resource, and the authors do not state the omission.
- technique: threat model taxonomy, literature survey.
- gap sign: not a gap result.
- prominence: EuroS&P. OpenAlex cited_by_count 448, plus 421 on the arXiv-title record (2026-10-13). Origin of the standing taxonomy.
- in_corpus: sok-security-privacy-machine-learning
- prerequisite: none beyond ML basics.
- tier: skim

### ZGC+25

- key: ZGC+25
- title: SoK: Watermarking for AI-Generated Content
- authors: Xuandong Zhao, Sam Gunn, Miranda Christ, Jaiden Fairoze, Andres Fabrega, Nicholas Carlini, Sanjam Garg, Sanghyun Hong, Milad Nasr, Florian Tramer, Somesh Jha, Lei Li, Yu-Xiang Wang, Dawn Song
- venue: IEEE Symposium on Security and Privacy (S&P 2025)
- venue_evidence: https://doi.org/10.1109/SP61157.2025.00178 (Crossref record, container "2025 IEEE Symposium on Security and Privacy (SP)"). arXiv comment: "IEEE S&P 2025".
- year: 2025
- link: https://arxiv.org/abs/2411.18479
- lane: D
- honest task: embed a hidden signal in generated content and detect it with a key.
- adversary task: detect, remove or forge the watermark.
- bounded party: polynomial-time algorithms in Definitions 3.2, 3.3 and 3.6. Robustness (Definition 3.5) is stated against a channel E.
- resource: time (polynomial), error epsilon.
- adversary class: computationally bounded or unbounded distinguishers for distortion-freeness (Definition 3.2 gives both), polynomial-time for undetectability and unforgeability, a fixed channel for robustness.
- assumption: none stated for the definitions.
- statement: Systematization with formal definitions. Definition 3.1 defines distortion, Definition 3.2 distortion-freeness in a computational and a statistical form, Definition 3.3 undetectability in the computational form only because statistical undetectability is impossible (citing CGZ24), Definition 3.4 the false positive rate, Definition 3.5 robustness to a channel with error epsilon for a property P, Definition 3.6 unforgeability against polynomial-time algorithms. Reading of Definition 3.5: unremovability is stated against a named channel, not against all efficient adversaries, so ZEFVAB24 is the result that quantifies over efficient removal. The conclusion names cryptographic, information-theoretic and statistical principles as future directions. ZEFVAB24 is in the reference list.
- technique: definitional survey, threat models, evaluation strategies.
- gap sign: not a gap result.
- prominence: S&P (tier 1). OpenAlex cited_by_count 23 (2026-10-13).
- in_corpus: no
- prerequisite: CGZ24, ZEFVAB24, watermarking schemes.
- tier: read

## 3. Triage

| key | title | venue | year | lane | gap sign | in_corpus | tier |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SCEKPSTZ23 | SoK: Let the Privacy Games Begin! | S&P | 2023 | D | not a gap result | no | deep |
| YGFJ18 | Privacy Risk in Machine Learning: Analyzing the Connection to Overfitting | CSF | 2018 | D | not a gap result | privacy-risk-overfitting | read |
| XD23 | PAC Privacy: Automatic Privacy Measurement and Control of Data Processing | CRYPTO | 2023 | I | not a gap result | no | deep |
| CKMMNST25 | Data Reconstruction: When You See It and When You Don't | ITCS | 2025 | D | equivalence with a hardness assumption | cohen-data-reconstruction | deep |
| CCGJY20 | Exploring Connections Between Active Learning and Model Extraction | USENIX Security | 2020 | D | equal up to log and noise factor | active-learning-model-extraction | read |
| MPRV09 | Computational Differential Privacy | CRYPTO | 2009 | D | existence only | computational-differential-privacy | deep |
| GGVZ19 | Making AI Forget You: Data Deletion in Machine Learning | NeurIPS | 2019 | D | honest update cheaper than retraining | no | read |
| GJNRSW21 | Adaptive Machine Unlearning | NeurIPS | 2021 | D | not a gap result | no | read |
| GGHM20 | Certified Data Removal from Machine Learning Models | ICML | 2020 | D | not a gap result | no | skim |
| TJSP22 | On the Necessity of Auditable Algorithmic Definitions for Machine Unlearning | USENIX Security | 2022 | D | existence only (negative) | auditable-unlearning-definitions | read |
| ERCGOP25 | Verifiable and Provably Secure Machine Unlearning | SaTML | 2025 | D | not a gap result | no | read |
| GKVZ22 | Planting Undetectable Backdoors in Machine Learning Models | FOCS | 2022 | C | adversary cheaper than defender, conditional | planting-undetectable-backdoors | deep |
| CGZ24 | Undetectable Watermarks for Language Models | COLT | 2024 | C | undetectability conditional, removal existence | undetectable-watermarks-lm | read |
| ZEFVAB24 | Watermarks in the Sand: Impossibility of Strong Watermarking | ICML | 2024 | C | adversary cheaper, existence | no | deep |
| JYCDTCP21 | Proof-of-Learning: Definitions and Practice | S&P | 2021 | D | adversary at least as dear, unproven | proof-of-learning | deep |
| GG25 | A Cryptographic Perspective on Mitigation vs. Detection in Machine Learning | arXiv preprint | 2025 | C | defender and adversary cheaper than trainer | no | deep |
| GTNP25 | The Good, the Bad and the Ugly: Meta-Analysis of Watermarks, Transferable Attacks and Adversarial Defenses | NeurIPS | 2025 | C | adversary cheaper (square root and quadratic gaps) | no | deep |
| LEX26 | Beyond Indistinguishability: Measuring Extraction Risk in LLM APIs | S&P | 2026 | D | not a gap result (absolute query bound) | no | deep |
| PMSW18 | SoK: Security and Privacy in Machine Learning | EuroS&P | 2018 | D | not a gap result | sok-security-privacy-machine-learning | skim |
| ZGC+25 | SoK: Watermarking for AI-Generated Content | S&P | 2025 | D | not a gap result | no | read |

## 4. Searches that returned nothing, and method notes

Nothing found, with the vocabulary used.

- WebSearch "position paper computational complexity cryptographic foundations for machine learning security definitions adversary resource bound": no position paper that argues for complexity-theoretic foundations as the standard. Hits were primary papers (Bubeck et al., Mahloujifar and Mahmoody, a query-complexity paper, GG25).
- WebSearch "survey cryptographic perspective on adversarial machine learning hardness robustness backdoors watermarks theory 2024 2025": no survey. Hits were GTNP25, a data-hiding survey, MIT 6.S976 course notes.
- WebSearch "survey theoretical foundations of adversarial robustness computational hardness sample complexity PAC cryptographic assumptions survey": no dedicated survey. Hits were primary papers (Gourdeau, Kanade, Kwiatkowska and Worrell, JMLR 2021, and robust PAC learning papers).
- WebSearch "position paper machine learning security needs formal threat models adversary resources computational bounded position privacy attacks evaluation theory 2025": no 2025 position paper centered on a computationally bounded adversary. Hits were the three works listed in 4b.
- OpenAlex title.search "SoK" with title_and_abstract.search for each of unlearning, watermark, model extraction, adversarial examples, poisoning, backdoor, membership inference, differential privacy, machine learning governance, certified, proof of learning, memorization, privacy auditing, reconstruction (2018 to 2026): no SoK in the 2018 to 2026 range whose title or abstract states a complexity or information-theoretic organization. The "proof of learning" query returned only zkVM, zero-knowledge and federated learning SoKs, none on proof-of-learning definitions.
- dblp: both dblp.org and its trier mirror timed out from the shell, so no venue was confirmed on dblp. Venue evidence is Crossref DOI records and publisher or proceedings pages instead.
- Springer chapter pages for XD23 and MPRV09 redirect to a login. Their CRYPTO venue rests on the Crossref volume records.
- Tool use. 24 WebSearch and WebFetch calls, and about 90 scripted HTTP requests (OpenAlex, Crossref, arXiv) in 15 shell calls. arXiv PDFs were read as extracted text in a scratch directory, and the arXiv API returned HTTP 429 after the batch.

### 4b. Opened but not sheeted (cap of 20), and leads not opened

Opened, not sheeted.

- CHLX25, Backdoor Defense, Learnability and Obfuscation (Christiano, Hilton, Lecomte, Xu), ITCS 2025, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.38, in corpus as backdoor-defense-learnability-obfuscation. Definition 3.1 defines epsilon-defendability as a game. Theorem 4.1 gives the best confidence as max of one half and 1 minus Theta(VC(F) epsilon). Definition 5.1 defines efficient defendability. Theorem 5.5 states that, assuming one-way functions and indistinguishability obfuscation, polynomial size circuits are not efficiently defendable.
- VDKMR26, Extending the Formalism and Theoretical Foundations of Cryptography to AI (Villa, Durak, Kohno, Maharramli, Roesner), arXiv 2603.02590, in corpus as extending-formalism-cryptography-ai. Security game for agentic access control. Position-style framework, not a venue paper in what was read.
- LXL23, SoK: Certified Robustness for Deep Neural Networks (Li, Xie, Li), S&P 2023, arXiv 2009.04131 (arXiv comment "To appear at 2023 IEEE Symposium on Security and Privacy"), OpenAlex 125. Definition 2 defines the (l_p, epsilon)-adversary as a perturbation ball and Definition 3 robustness verification. It states that complete verification is NP-complete, citing two works, and names a convex relaxation barrier. It organizes by the perturbation ball and verifier complexity, which the BRIEF puts out of scope as a foundation. It states no resource for the attacker.
- Papernot, A Marauder's Map of Security and Privacy in Machine Learning, arXiv 1811.01134 (abstract page opened). Position paper. Directions include formal frameworks that align generalization with robustness and privacy. No venue confirmed.
- Biggio and Roli, Wild Patterns: Ten Years After the Rise of Adversarial Machine Learning, Pattern Recognition 2018, arXiv 1712.03141 (arXiv comment: accepted for publication on Pattern Recognition, 2018). Survey of threat models and attacks by knowledge, capability and goal.
- Allouah, Guerraoui, Stephan, Balancing Privacy, Robustness, and Efficiency in Machine Learning, arXiv 2312.14712 (v3 26 Jun 2025, no venue note on the page). Position paper on relaxing worst-case threat models. Abstract read as a summary from the fetch tool, so treat the wording as unverified.

Leads seen only in OpenAlex or search listings, not opened, not entered.

- SoK: Dataset Copyright Auditing in Machine Learning Systems (S&P 2025). SoK: Model Inversion Attack Landscape (CSF 2023). SoK: Membership Inference is Harder Than Previously Thought (PoPETs 2023). SoK: Differential Privacy as a Causal Property (S&P 2020). SoK: Computational and Distributed Differential Privacy for MPC (PoPETs 2025, DOI 10.56553/popets-2025-0023, Crossref record only). SoK: Unintended Interactions among Machine Learning Defenses and Risks (S&P 2024). SoK: The Hitchhiker's Guide to Efficient, End-to-End, and Tight DP Auditing (SaTML 2026). Position: Gaussian DP for Reporting Differential Privacy Guarantees in Machine Learning (SaTML 2026). Sandcastles in the Storm: Revisiting the (Im)possibility of Strong Watermarking (arXiv 2505.06827). Query Complexity of Adversarial Attacks (arXiv 2010.01039). Gourdeau, Kanade, Kwiatkowska, Worrell, On the Hardness of Robust Classification (NeurIPS 2019 and JMLR 2021). Tramèr et al., Stealing Machine Learning Models via Prediction APIs (USENIX Security 2016, arXiv metadata opened only). Gilmer et al., Motivating the Rules of the Game for Adversarial Example Research (arXiv 1807.06732, metadata opened only).
