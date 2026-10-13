# Sweep 2026-10-13, lane computation

Counts are OpenAlex cited_by_count and Semantic Scholar citationCount, both read on 2026-10-13. OpenAlex splits a paper over its arXiv and publisher records, so the smaller figure undercuts. Theorem numbers are from the PDF copies in raw/ (usually the arXiv version) and are marked "seen". Where a statement comes from an abstract only it says "(abstract)". Epistemic labels in the statement lines are Proven, Heuristic, Empirical, Open.

## 1. What the field has in this lane

The lane rests on one template and five defining results. The template is KV94, a reduction from public key cryptanalysis to learning, so that a polynomial time learner for a class would break RSA, factoring of Blum integers and quadratic residuosity. The first defining result is BLPR19 with DNV19. Robust classification is cheap in samples but hard in statistical queries or time, and DNV19 shows that any such task implies one way functions. The second is GKVZ22, which plants backdoors that no polynomial time observer detects, strengthened to statistical undetectability in BRV26 and answered by the defences CHLX25 and GSVV25. The third is CGZ24, a language model watermark that is undetectable under one way functions, with ZEF+24 as its limit under two oracle assumptions. The fourth is CJM20 with CCHRSS24, which treats parameter extraction as cryptanalysis and moves the attacker's time from exponential to polynomial in the neuron count. The fifth is BCV16 with GIKKM23, which separates computationally bounded from unbounded privacy adversaries. Verification of training (GRSY21, JYC+21) and restricted adversary classes (CIM19, CK21) sit beside these, but they state their bounds as relative costs or as function classes.

## 2. Sheets

### KV94
- key: KV94
- title: Cryptographic limitations on learning Boolean formulae and finite automata
- authors: Michael Kearns, Leslie Valiant
- venue: Journal of the ACM 41(1), pages 67 to 95
- venue_evidence: https://doi.org/10.1145/174644.174647 (Crossref record opened, which carries volume, issue, pages and the abstract. The ACM page returned 403)
- year: 1994
- link: https://doi.org/10.1145/174644.174647
- lane: C
- honest task: learn a Boolean formula, a deterministic finite automaton or a constant depth threshold circuit in the PAC model, with any hypothesis representation
- adversary task: break RSA, factor Blum integers, decide quadratic residuosity, using the learner as the tool
- bounded party: the learner
- resource: time, polynomial
- adversary class: polynomial time PAC learners, even with only a slight advantage over guessing
- assumption: hardness of RSA, of factoring Blum integers and of quadratic residuosity (abstract)
- statement: Proven under those assumptions (abstract). A polynomial time learner for the three classes would give polynomial time algorithms for the three number theoretic problems, whatever representation the learner outputs. Seen in the Crossref abstract.
- technique: reduction from cracking public key cryptosystems to the learning problem (abstract)
- gap sign: not a gap result. It is the reduction template, with the honest task at least as hard as the cryptanalytic task, conditionally.
- prominence: J. ACM. OpenAlex 733, Semantic Scholar 994
- in_corpus: no
- prerequisite: the PAC model, representation independent hardness, the three number theoretic assumptions
- tier: read

### BLPR19
- key: BLPR19
- title: Adversarial examples from computational constraints
- authors: Sebastien Bubeck, Yin Tat Lee, Eric Price, Ilya Razenshteyn
- venue: ICML 2019 (PMLR 97)
- venue_evidence: https://proceedings.mlr.press/v97/bubeck19a.html (opened, citation metadata lists the four authors and the conference)
- year: 2019
- link: https://proceedings.mlr.press/v97/bubeck19a.html and arXiv v1 https://arxiv.org/abs/1805.10204 (three authors, the statistical query task only)
- lane: A, with C for the second task
- honest task: learn a robust binary classifier from samples
- adversary task: evade, by a perturbation of the input
- bounded party: the learner
- resource: statistical queries for the first task, time under a cryptographic assumption for the second task, samples for the information theoretic side
- adversary class: statistical query algorithms for the first task, polynomial time algorithms for the second
- assumption: none for the statistical query task. A cryptographic assumption for the second task (PMLR abstract). The DNV19 abstract names the hardness of factoring.
- statement: Proven. For a broad set of tasks the existence of a robust classifier implies it is found by a possibly exponential time algorithm from few samples (Theorem 3.1 in arXiv v1, sample size proportional to the log of the class size). Two binary tasks in high dimension are easy to learn robustly information theoretically, learnable non-robustly by a linear separator, and not efficiently robustly learnable, the first against any statistical query algorithm (Theorem 4.1 in arXiv v1, Theorem 1.1 informal), the second under a cryptographic assumption (PMLR abstract).
- technique: a high dimensional generalization of an earlier statistical query hard construction of Diakonikolas et al. (arXiv v1 overview). Planted structure in a Gaussian along a random subspace.
- gap sign: existence only. The honest task, robust learning, costs few samples and exponentially many statistical queries.
- prominence: ICML. OpenAlex 119 (arXiv record), Semantic Scholar 242
- in_corpus: adversarial-examples-computational-constraints (arXiv v1), adversarial-examples-prg (arXiv 1811.06418, the cryptographic task)
- prerequisite: the statistical query model, robust PAC learning, Blum integer or pseudorandom generator hardness
- tier: deep

### DNV19
- key: DNV19
- title: Computational Limitations in Robust Classification and Win-Win Results
- authors: Akshay Degwekar, Preetum Nakkiran, Vinod Vaikuntanathan
- venue: COLT 2019 (PMLR 99)
- venue_evidence: https://proceedings.mlr.press/v99/degwekar19a.html (opened)
- year: 2019
- link: https://arxiv.org/abs/1902.01086
- lane: C
- honest task: learn a robust classifier
- adversary task: evade, by a perturbation of the input
- bounded party: the learner
- resource: time
- adversary class: polynomial time learners
- assumption: average case hard functions with error correcting codes (Theorem 2.1), one way functions (Theorem 2.2), learning parity with noise or learning with errors in the public key regime (Theorem 2.3)
- statement: Proven (informal Theorems 2.1 to 2.4, and Theorem 9.1, seen). There are tasks where an efficient non-robust classifier exists, an inefficient robust one exists, and no efficient robust one is learnable, with no cryptographic assumption beyond average case hardness. Under one way functions there is a task with an efficient robust classifier tolerating m/8 perturbations that no efficient learner finds. Under learning parity with noise the tolerated perturbation is on the order of the square root of m, and fresh samples can still be generated. Conversely any task with an efficient robust classifier that is hard to learn implies one way functions.
- technique: encode an average case hard function in the label through an error correcting code, and a reduction in the other direction from hard-to-learn robust classifiers to one way functions
- gap sign: existence only, with a converse. Any such gap implies cryptography.
- prominence: COLT. OpenAlex 3 (arXiv record), Semantic Scholar 40
- in_corpus: win-win-robust-learning
- prerequisite: BLPR19, one way functions, learning parity with noise
- tier: deep

### GJMM20
- key: GJMM20
- title: Adversarially Robust Learning Could Leverage Computational Hardness
- authors: Sanjam Garg, Somesh Jha, Saeed Mahloujifar, Mohammad Mahmoody
- venue: ALT 2020 (PMLR 117)
- venue_evidence: https://proceedings.mlr.press/v117/garg20a.html (opened)
- year: 2020
- link: https://arxiv.org/abs/1905.11564
- lane: C
- honest task: classify test inputs correctly
- adversary task: find an adversarial example within a perturbation budget
- bounded party: the adversary
- resource: time, and the perturbation budget
- adversary class: polynomial time adversaries against information theoretic adversaries
- assumption: unforgeable signatures with error correcting codes (Construction 7, seen). No assumption for the converse.
- statement: Proven (Theorems 8, 14 and 18 seen). There is a classifier that is computationally robust against polynomial time adversaries with budget linear in n, while an information theoretic adversary succeeds with a budget polylogarithmic in n above the base robustness (Theorem 8). In the second construction (Theorem 14) the classifier has risk 0 and computational adversarial risk 0, while an information theoretic adversary with budget ell(n) reaches risk at least 1/2. Conversely, a learner whose computational robustness beats its information theoretic robustness by 1/poly, on an efficiently samplable distribution, implies a hard sampler for NP (Theorem 18).
- technique: append a signature and an error-correcting encoding of the verification key to the input, so that an efficient adversary must change linearly many bits and an unbounded adversary forges the signature
- gap sign: adversary dearer. The efficient adversary needs a linear budget where the unbounded adversary needs a polylogarithmic one.
- prominence: ALT. OpenAlex 8 (arXiv record), Semantic Scholar 24
- in_corpus: computational-hardness-robust-learning
- prerequisite: digital signatures, error correcting codes, adversarial risk under a budget
- tier: deep

### GKVZ22
- key: GKVZ22
- title: Planting Undetectable Backdoors in Machine Learning Models (the FOCS record prints the suffix "Extended Abstract")
- authors: Shafi Goldwasser, Michael P. Kim, Vinod Vaikuntanathan, Or Zamir
- venue: FOCS 2022
- venue_evidence: https://doi.org/10.1109/FOCS54457.2022.00092 (Crossref record opened, container is the 63rd FOCS)
- year: 2022
- link: https://arxiv.org/abs/2204.06974
- lane: C
- honest task: train a classifier, possibly delegated to a service provider
- adversary task: plant a backdoor in the classifier, and for the user to detect it or to find an input where the two models differ
- bounded party: the user, as a polynomial time distinguisher
- resource: time
- adversary class: black-box polynomial time distinguishers for the signature construction, white-box polynomial time distinguishers for the random Fourier feature construction
- assumption: one way functions, through strongly unforgeable signatures (Theorems 2.1 and 5.4). Worst case lattice problems through continuous learning with errors (Theorems 2.2 and 6.5).
- statement: Proven under those assumptions (informal Theorems 2.1 and 2.2 and Theorem 7.1 seen, arXiv v2 numbering). For every training procedure there is a non-replicable backdoor that is black-box undetectable. For random Fourier features there is a backdoor undetectable even given all weights, so every input has an adversarial example. Backdoors can be neutralized for Lipschitz ground truth with a uniform marginal (Theorem 7.1).
- technique: signatures on the input for the black-box case. Planting continuous learning with errors structure in the sampled features for the white-box case.
- gap sign: adversary cheaper. Planting costs about the training cost and no efficient detector exists under the assumption.
- prominence: FOCS. OpenAlex 40 (FOCS record) and 9 (arXiv record), Semantic Scholar 109
- in_corpus: planting-undetectable-backdoors
- prerequisite: digital signatures, learning with errors, random Fourier features
- tier: deep

### CHLX25
- key: CHLX25
- title: Backdoor defense, learnability and obfuscation
- authors: Paul Christiano, Jacob Hilton, Victor Lecomte, Mark Xu
- venue: ITCS 2025 (LIPIcs 325, 38:1 to 38:21)
- venue_evidence: arXiv journal_ref field on https://arxiv.org/abs/2409.03077 (opened), with DOI 10.4230/LIPIcs.ITCS.2025.38. Crossref does not resolve that DOI.
- year: 2025 (arXiv 2024)
- link: https://arxiv.org/abs/2409.03077
- lane: D, with C
- honest task: evaluate a function from a class and learn it (PAC)
- adversary task: modify the function on a random trigger input. The defender detects the trigger at evaluation time.
- bounded party: the defender, and the attacker
- resource: samples in the unbounded setting (VC dimension), time in the efficient setting
- adversary class: unbounded attackers, and polynomial time attackers
- assumption: none in the unbounded setting. Random oracle for Theorem 5.3. One way functions and indistinguishability obfuscation for Theorem 5.5.
- statement: Proven (Theorems 4.1, 5.3, 5.5 and 6.1 seen). The best confidence with which a class is epsilon-defendable is the maximum of 1/2 and 1 minus a Theta term in VC(F) times epsilon. In the random oracle model some class is efficiently defendable but not efficiently PAC learnable. Under one way functions and indistinguishability obfuscation, polynomial size circuits are not efficiently defendable. Polynomial size decision trees are efficiently uniform-defendable with no calls to the example oracle. Efficient PAC learnability implies efficient defendability and not conversely (abstract).
- technique: the voting algorithm of Hanneke et al. for the unbounded case (abstract), obfuscation for the lower bound, a depth check on the reached leaf for decision trees (Theorem 6.1)
- gap sign: existence only. In the efficient regime defence lies strictly between learning and obfuscation, and in the VC regime the defender needs only the sample cost of learning.
- prominence: ITCS. OpenAlex 2, Semantic Scholar 3
- in_corpus: backdoor-defense-learnability-obfuscation
- prerequisite: GKVZ22, VC dimension, indistinguishability obfuscation
- tier: deep

### GSVV25
- key: GSVV25
- title: Oblivious Defense in ML Models: Backdoor Removal without Detection
- authors: Shafi Goldwasser, Jonathan Shafer, Neekon Vafa, Vinod Vaikuntanathan
- venue: STOC 2025 (57th ACM Symposium on Theory of Computing)
- venue_evidence: https://doi.org/10.1145/3717823.3718245 (Crossref record opened)
- year: 2025
- link: https://arxiv.org/abs/2411.03279
- lane: C, with D
- honest task: learn, and use a model that an attacker may have backdoored
- adversary task: plant a backdoor, possibly an undetectable one
- bounded party: the defender, as an efficient black-box mitigator
- resource: time, samples and oracle calls to the possibly backdoored function
- adversary class: any attacker-chosen function, under total variation security and a cutoff distance security (Definitions 4.6 and 4.7 seen)
- assumption: none cryptographic. The ground-truth labels must be close to a Fourier-heavy function, or close to a linear or polynomial function over the reals.
- statement: Proven (informal Theorem 6.3 and Theorems 7.1, 7.7, 7.12 and 8.1 listed, seen in arXiv v1). An efficient global mitigator outputs a function secure in total variation distance with L2 loss O(tau squared), when the population is O(tau squared) close in L2 to a tau-heavy function and the possibly backdoored function has L2 loss O(tau squared). Local mitigators exist for linear and for polynomial ground truth. All constructions are black-box.
- technique: random self-reducibility, correlated sampling, robust mean estimation
- gap sign: not a gap result. It bypasses the detection barrier of GKVZ22 by a condition on the labels.
- prominence: STOC. OpenAlex 1, Semantic Scholar 7
- in_corpus: oblivious-defense-backdoor-removal
- prerequisite: GKVZ22, Fourier analysis on the Boolean cube
- tier: read

### BRV26
- key: BRV26
- title: Statistically Undetectable Backdoors in Deep Neural Networks
- authors: Andrej Bogdanov, Alon Rosen, Neekon Vafa
- venue: ICML 2026 (poster, 8 July 2026)
- venue_evidence: https://icml.cc/virtual/2026/poster/65521 (opened). The arXiv comment field also reads ICML 2026.
- year: 2026
- link: https://arxiv.org/abs/2607.09532
- lane: C, with I for the undetectability
- honest task: train a deep feedforward network
- adversary task: plant a backdoor that gives invariance-based adversarial examples for every input. The user cannot find such examples without it.
- bounded party: the user of the model
- resource: total variation distance for undetectability, time for finding the adversarial examples
- adversary class: unbounded distinguishers with full white-box access for undetectability, polynomial time algorithms for example generation
- assumption: standard cryptographic assumptions (abstract). The anonymous ICLR 2026 submission copy in raw/ states average case hardness of a symmetric bounded perceptron problem and of a short integer vector problem for Gaussian matrices (Assumptions 1 and 2). The ICML version was not compared.
- statement: Proven under those assumptions (abstract). The backdoored and the honestly trained model are close in total variation distance given all weights, so no distinguisher succeeds. Without the backdoor, producing any invariance-based adversarial example in polynomial time is impossible. The authors read this as a power asymmetry between trainers and users.
- technique: backdoors for random Gaussian projections and for bi-Lipschitz layers (Theorem 2 and Definition 7, seen in the submission copy only)
- gap sign: adversary cheaper. It upgrades the white-box computational undetectability of GKVZ22 to statistical undetectability.
- prominence: ICML. OpenAlex 0, Semantic Scholar 1
- in_corpus: no (raw/20344_Statistically_Undetectab.pdf holds the anonymous submission copy, and wiki/sources/io-undetectable-backdoors-nn.md mentions it)
- prerequisite: GKVZ22, lattice-type average case hardness, total variation distance
- tier: deep

### GG25
- key: GG25
- title: A Cryptographic Perspective on Mitigation vs. Detection in Machine Learning
- authors: Greg Gluch, Shafi Goldwasser
- venue: arXiv preprint
- venue_evidence: https://arxiv.org/abs/2504.20310 (opened, no journal reference, and a web search found no proceedings entry)
- year: 2025
- link: https://arxiv.org/abs/2504.20310
- lane: D, with C
- honest task: train a model and defend it at inference time
- adversary task: produce inference-time inputs that fool the trained model
- bounded party: both parties, in a three-round protocol
- resource: sample complexity in the first task, time in the second
- adversary class: resource-bounded attackers
- assumption: identity-based fully homomorphic encryption, publicly verifiable zk-SNARKs and strongly unforgeable signatures for the first separation. Non-parallelizing languages with average case hardness, incrementally verifiable computation and identity-based fully homomorphic encryption for the second.
- statement: Proven under those assumptions (abstract). Defence by detection and defence by mitigation are equivalent for classification. For generative learning tasks there are two tasks where mitigation is possible and detection is provably impossible, and the mitigation uses far less computation than training.
- technique: not read beyond the abstract
- gap sign: existence only, between two defender tasks
- prominence: arXiv preprint. OpenAlex 0, Semantic Scholar 1
- in_corpus: no (cited in wiki/analyses/native-asymmetry-in-learning.md and wiki/log.md, without a source page)
- prerequisite: GKVZ22, CHLX25, GSVV25
- tier: read

### CGZ24
- key: CGZ24
- title: Undetectable Watermarks for Language Models
- authors: Miranda Christ, Sam Gunn, Or Zamir
- venue: COLT 2024 (PMLR 247)
- venue_evidence: https://proceedings.mlr.press/v247/christ24a.html (opened)
- year: 2024
- link: https://arxiv.org/abs/2306.09194
- lane: C
- honest task: generate text with an embedded watermark that the key holder detects
- adversary task: distinguish watermarked from unwatermarked output, with adaptive prompts
- bounded party: the distinguisher
- resource: time and queries
- adversary class: polynomial time adaptive distinguishers
- assumption: one way functions (abstract)
- statement: Proven (Definition 9, Theorems 1 and 6, Lemma 4 and Theorem 10, seen in the raw copy). For every model there is an undetectable, sound watermarking scheme whose completeness parameter is on the order of the security parameter times the square root of the output length. Undetectability holds only against computationally bounded adversaries, because polynomially many queries and exponential time detect any nontrivial scheme (Lemma 4). Outputs of low empirical entropy cannot be watermarked undetectably, since exp(t) queries and time detect a scheme that marks a non-negligible fraction of outputs with entropy at most t (Theorem 10).
- technique: the embedder waits until the empirical entropy of the output so far is high, then seeds a pseudorandom function with that output to choose later tokens (introduction and Algorithms 1 and 2, Theorem 3, seen in the raw copy)
- gap sign: existence only. The embedder pays generation cost, and no efficient observer without the key notices a change.
- prominence: COLT. OpenAlex 9 (arXiv record), Semantic Scholar 304
- in_corpus: undetectable-watermarks-lm
- prerequisite: pseudorandom functions, language model sampling, empirical entropy
- tier: deep

### ZEF+24
- key: ZEF+24
- title: Watermarks in the Sand: Impossibility of Strong Watermarking for Language Models (ICML page). The arXiv version reads "for Generative Models".
- authors: Hanlin Zhang, Benjamin L. Edelman, Danilo Francati, Daniele Venturi, Giuseppe Ateniese, Boaz Barak
- venue: ICML 2024
- venue_evidence: https://icml.cc/virtual/2024/poster/33645 (opened). The arXiv comment field also reads ICML 2024.
- year: 2024
- link: https://arxiv.org/abs/2311.04378
- lane: C
- honest task: embed a watermark in model output so that it can be verified later
- adversary task: erase the watermark while the output keeps its quality
- bounded party: the attacker
- resource: queries to a quality oracle and a perturbation oracle, and time
- adversary class: computationally bounded attackers with black-box access to the model, weaker than the watermarked model
- assumption: two oracle assumptions, a quality oracle and a perturbation oracle whose random walk on high quality outputs mixes efficiently. No cryptographic assumption.
- statement: Proven under the two oracle assumptions (abstract). Strong watermarking is impossible, also when insertion and detection share a secret key unknown to the attacker. The attack needs neither the key nor the scheme. It is instantiated against three published language model schemes.
- technique: a random walk over high quality outputs driven by the two oracles (abstract)
- gap sign: adversary cheaper. The attacker needs less computation than the watermarked model, under the stated assumptions.
- prominence: ICML. OpenAlex 9 (arXiv record), Semantic Scholar 114
- in_corpus: no (cited in wiki/analyses/native-asymmetry-in-learning.md, without a source page)
- prerequisite: CGZ24, Markov chain mixing
- tier: deep

### CJM20
- key: CJM20
- title: Cryptanalytic Extraction of Neural Network Models
- authors: Nicholas Carlini, Matthew Jagielski, Ilya Mironov
- venue: CRYPTO 2020
- venue_evidence: Crossref volume record https://doi.org/10.1007/978-3-030-56877-1 (Advances in Cryptology, CRYPTO 2020, Part III), chapter https://doi.org/10.1007/978-3-030-56877-1_7 (opened)
- year: 2020
- link: https://arxiv.org/abs/2003.04884
- lane: C
- honest task: train a ReLU network
- adversary task: recover its parameters up to floating point precision
- bounded party: the attacker
- resource: queries to the oracle, and time
- adversary class: chosen-input black-box attackers with access to the output values
- assumption: none. The attack uses the piecewise linear structure of ReLU networks.
- statement: Empirical (abstract, Definition 1 and Table 1 seen). A differential attack extracts a 100,000 parameter MNIST network with about 2^21.5 queries in under an hour, with worst-case error 2^-25. The paper states no theorem. The later CCHRSS24 abstract describes the attack as polynomial in queries and exponential in time as a function of the neuron count.
- technique: queries at the critical points of the piecewise linear function reveal weights (abstract)
- gap sign: existence only. The attack cost is not compared with the training cost.
- prominence: CRYPTO. OpenAlex 105, Semantic Scholar 179
- in_corpus: cryptanalytic-extraction-nn
- prerequisite: ReLU networks as piecewise linear maps, differential cryptanalysis
- tier: read

### CCHRSS24
- key: CCHRSS24
- title: Polynomial Time Cryptanalytic Extraction of Neural Network Models
- authors: Isaac A. Canales-Martinez, Jorge Chavez-Saab, Anna Hambitzer, Francisco Rodriguez-Henriquez, Nitin Satpute, Adi Shamir
- venue: EUROCRYPT 2024
- venue_evidence: Crossref volume record https://doi.org/10.1007/978-3-031-58734-4 (Advances in Cryptology, EUROCRYPT 2024, Part III), chapter https://doi.org/10.1007/978-3-031-58734-4_1 (opened)
- year: 2024
- link: https://arxiv.org/abs/2310.08708
- lane: C
- honest task: train a ReLU network
- adversary task: recover all real-valued parameters with arbitrarily high precision
- bounded party: the attacker
- resource: queries and time
- adversary class: chosen-input black-box attackers with access to output values
- assumption: none
- statement: Empirical (abstract, no theorem). The CJM20 attack needs exponentially much time in the neuron count. The new attack uses polynomially many queries and polynomial time. It extracts a CIFAR10 network with 3072 inputs and 8 hidden layers of 256 neurons in 30 minutes on a 256-core machine.
- technique: three new sign recovery techniques, the first by solving a linear system built from observed first derivatives (Our Contributions, seen)
- gap sign: existence only. Time falls from exponential to polynomial, with no ratio to training cost.
- prominence: EUROCRYPT. OpenAlex 13, Semantic Scholar 35 (ePrint record)
- in_corpus: polynomial-time-cryptanalytic-extraction
- prerequisite: CJM20
- tier: read

### BCV16
- key: BCV16
- title: Separating Computational and Statistical Differential Privacy in the Client-Server Model
- authors: Mark Bun, Yi-Hsiu Chen, Salil Vadhan
- venue: TCC 2016-B
- venue_evidence: Crossref volume record https://doi.org/10.1007/978-3-662-53641-4 (Theory of Cryptography, TCC 2016-B, Part I), chapter https://doi.org/10.1007/978-3-662-53641-4_23 (opened)
- year: 2016
- link: https://doi.org/10.1007/978-3-662-53641-4_23
- lane: C
- honest task: perform a statistical task privately in the client-server model
- adversary task: the data analyst infers information about an individual
- bounded party: the analyst, polynomial time under computational differential privacy
- resource: time
- adversary class: polynomial time analysts against information theoretic analysts
- assumption: sub-exponentially secure one way functions and two-message witness indistinguishable proofs (zaps) for NP
- statement: Proven under those assumptions (Theorem 1 informal and Theorem 11 seen, with the abstract). There is a task performed efficiently with computational differential privacy in the client-server model that is infeasible with information theoretic differential privacy. The GIKKM23 abstract records that a task achievable under computational privacy and by no statistical mechanism at all, unbounded ones included, was still open afterwards.
- technique: extractable zap proofs for NP (Theorem 8)
- gap sign: existence only
- prominence: TCC. OpenAlex 10, Semantic Scholar 16
- in_corpus: separating-cdp-client-server
- prerequisite: computational differential privacy of Mironov et al., witness indistinguishability, Groce-Katz-Yerukhimovich TCC 2011
- tier: read

### GIKKM23
- key: GIKKM23
- title: Towards Separating Computational and Statistical Differential Privacy
- authors: Badih Ghazi, Rahul Ilango, Pritish Kamath, Ravi Kumar, Pasin Manurangsi
- venue: FOCS 2023
- venue_evidence: https://doi.org/10.1109/focs57990.2023.00042 (Crossref record opened, container is the 64th FOCS). The arXiv comment field also reads FOCS 2023.
- year: 2023
- link: https://arxiv.org/abs/2301.00104
- lane: C, with A for the decision tree step
- honest task: a differentially private mechanism that reaches constant utility on a task
- adversary task: distinguish the outputs on neighbouring datasets
- bounded party: the privacy adversary
- resource: time, and decision tree queries for the intermediate step
- adversary class: computationally bounded adversaries against unbounded adversaries, with decision tree adversaries as the stepping stone
- assumption: non-interactive witness indistinguishable proofs, laconic collision-resistant keyless hash functions, differing-inputs obfuscation for public-coin samplers (abstract)
- statement: Proven under those assumptions (abstract, and Theorem 5 as the main result, seen in the raw copy). There is a task with an epsilon-CDP mechanism, epsilon constant, of utility 1 minus o(1), while any (epsilon, delta)-SDP mechanism, unbounded ones included, with constant utility needs a super-constant epsilon or an inverse-polynomially large delta.
- technique: show privacy against decision tree adversaries, then lift it to computationally bounded adversaries with cryptography (abstract)
- gap sign: existence only
- prominence: FOCS. OpenAlex 4, Semantic Scholar 6
- in_corpus: towards-separating-cdp
- prerequisite: BCV16, differing-inputs obfuscation, hash functions
- tier: deep

### CIM19
- key: CIM19
- title: Capacity Bounded Differential Privacy
- authors: Kamalika Chaudhuri, Jacob Imola, Ashwin Machanavajjhala
- venue: NeurIPS 2019
- venue_evidence: https://arxiv.org/abs/1907.02159 (opened, comment field reads NeurIPS 2019). The Semantic Scholar venue field agrees.
- year: 2019
- link: https://arxiv.org/abs/1907.02159
- lane: A, with D
- honest task: release a statistic with a privacy guarantee
- adversary task: distinguish the outputs on neighbouring datasets
- bounded party: the privacy adversary
- resource: the capacity of the function class the attack is drawn from. Computation is not the bound.
- adversary class: attacks from a function class H, measured by restricted f-divergences
- assumption: none
- statement: Proven (Definition 3, Theorems 1 and 7 seen). A mechanism is (H, Gamma)-capacity bounded private if the H-restricted divergence Gamma between its outputs on neighbouring datasets is at most epsilon. With H all functions and Gamma a Renyi divergence this is Renyi differential privacy. Post-processing by a function from G keeps privacy for the class I, whenever I composed with G lies in H (Theorem 1). A Pinsker-like inequality holds for restricted KL divergences (Theorem 7).
- technique: restricted f-divergences, which are integral probability metrics over a function class
- gap sign: not a gap result. It is a definition with a weaker adversary class.
- prominence: NeurIPS. OpenAlex 7 (arXiv record), Semantic Scholar 41
- in_corpus: capacity-bounded-dp
- prerequisite: Renyi differential privacy, f-divergences
- tier: deep

### CK21
- key: CK21
- title: Covert Learning: How to Learn with an Untrusted Intermediary
- authors: Ran Canetti, Ari Karchmer
- venue: TCC 2021
- venue_evidence: Crossref volume record https://doi.org/10.1007/978-3-030-90456-2 (Theory of Cryptography, TCC 2021, Part III), chapter https://doi.org/10.1007/978-3-030-90456-2_1 (opened)
- year: 2021
- link: https://doi.org/10.1007/978-3-030-90456-2_1
- lane: C, with D
- honest task: learn a function by oracle queries, agnostically, for parities and decision trees
- adversary task: an intermediary who watches the queries learns the function or the learner's hypothesis class, and in the verifiable model also modifies the responses
- bounded party: the intermediary, polynomial time
- resource: time
- adversary class: polynomial time eavesdroppers, and polynomial time intermediaries that modify responses
- assumption: hardness of learning parity with noise, and its sub-exponential form for the DNF result (Theorem 1.8 informal)
- statement: Proven under those assumptions (abstract, informal Theorems 1.3 to 1.9 listed, seen). Covert learning algorithms exist for agnostic parities and decision trees, where an eavesdropper learns nothing about the function or the hypothesis. Covert verifiable learning algorithms keep the guarantees when the intermediary modifies responses and the learner may abort. The abstract states that the work exposes limits of current defences against model extraction.
- technique: not summarised beyond the learning parity with noise assumption
- gap sign: existence only
- prominence: TCC. OpenAlex 5, Semantic Scholar 10
- in_corpus: covert-learning
- prerequisite: learning parity with noise, membership-query learning, GRSY21
- tier: read

### GRSY21
- key: GRSY21
- title: Interactive Proofs for Verifying Machine Learning
- authors: Shafi Goldwasser, Guy N. Rothblum, Jonathan Shafer, Amir Yehudayoff
- venue: ITCS 2021 (LIPIcs 185, 41:1 to 41:19)
- venue_evidence: https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2021.41 (opened)
- year: 2021
- link: https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2021.41
- lane: I, with C
- honest task: verify with labelled samples and an untrusted prover that a hypothesis is approximately correct
- adversary task: the untrusted prover convinces the verifier of a bad hypothesis
- bounded party: the verifier
- resource: random samples, and verifier running time
- adversary class: an untrusted prover. The page summary does not state a computational bound on it.
- assumption: none stated in the page summary
- statement: Proven (abstract, as summarised by the page fetch, and corroborated by the GJK+24 abstract). For a specific class, verification needs far fewer samples than learning, even in one round. For Fourier-sparse Boolean functions a multi-round protocol lets the prover use membership queries while the verifier uses random samples. For another class verification needs about as many samples as learning, up to a logarithmic factor.
- technique: interactive proofs, with an interactive Goldreich-Levin protocol for the Fourier-sparse case (named in the GJK+24 abstract)
- gap sign: verification cheaper than learning for some classes, equal for another
- prominence: ITCS. OpenAlex 1, Semantic Scholar 57 (ECCC record)
- in_corpus: no
- prerequisite: PAC learning, interactive proofs, Goldreich-Levin
- tier: read

### JYC+21
- key: JYC+21
- title: Proof-of-Learning: Definitions and Practice
- authors: Hengrui Jia, Mohammad Yaghini, Christopher A. Choquette-Choo, Natalie Dullerud, Anvith Thudi, Varun Chandrasekaran, Nicolas Papernot
- venue: IEEE Symposium on Security and Privacy 2021
- venue_evidence: https://doi.org/10.1109/SP40001.2021.00106 (Crossref record opened). The arXiv comment field also reads the 42nd IEEE S&P.
- year: 2021
- link: https://arxiv.org/abs/2103.05633
- lane: C
- honest task: train a model and keep a record of the optimization as a proof
- adversary task: spoof a valid proof of learning for given weights at lower cost than training
- bounded party: the spoofer
- resource: expected computation cost
- adversary class: any spoofing strategy (Property 2), including stochastic, structurally correct and distillation-based spoofing
- assumption: none
- statement: Heuristic (Definition 2 and Property 2 seen). A spoof is dishonest if the adversary's expected cost is below the trainer's. A valid scheme requires the trainer's expected cost to be at most the adversary's, for every spoofing strategy. The paper supports this by analysis and experiments and does not prove it. The bound is a bare inequality and carries no exponent.
- technique: stochastic gradient descent accumulates secret information through its randomness, so a transcript of checkpoints and data order serves as the proof (abstract)
- gap sign: adversary dearer or equal, claimed
- prominence: IEEE S&P. OpenAlex 75, Semantic Scholar 151
- in_corpus: proof-of-learning (and pol-more-broken, pol-incentive-security, polo-proof-of-learning-ownership)
- prerequisite: stochastic gradient descent, proof of work
- tier: deep

### GSG+23
- key: GSG+23
- title: LLM Censorship: A Machine Learning Challenge or a Computer Security Problem?
- authors: David Glukhov, Ilia Shumailov, Yarin Gal, Nicolas Papernot, Vardan Papyan
- venue: arXiv preprint
- venue_evidence: https://arxiv.org/abs/2307.10719 (opened, no journal reference or venue comment)
- year: 2023
- link: https://arxiv.org/abs/2307.10719
- lane: D (a computability argument)
- honest task: censor model output that is semantically impermissible
- adversary task: recover impermissible output from a collection of permissible outputs
- bounded party: the censor
- resource: decidability
- adversary class: knowledgeable attackers that use the instruction-following ability of the model
- assumption: none
- statement: Proven in the paper's framing, not checked past the abstract (abstract). Semantic censorship can be viewed as an undecidable problem, and attackers can reconstruct impermissible output from permissible pieces. The authors conclude that censorship should be treated as a security problem.
- technique: reduction to undecidability, and the combination of permitted outputs (abstract)
- gap sign: not a gap result. It is an impossibility by computability.
- prominence: arXiv preprint. OpenAlex 19, Semantic Scholar 87
- in_corpus: no (related pages: jailbreak-paradox, filter-impossibility-ai-alignment)
- prerequisite: Rice's theorem, instruction-following language models
- tier: skim

## 3. Triage table

| key | title | venue | year | lane | gap sign | in_corpus | tier |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KV94 | Cryptographic limitations on learning Boolean formulae and finite automata | J. ACM | 1994 | C | not a gap result (reduction) | no | read |
| BLPR19 | Adversarial examples from computational constraints | ICML | 2019 | A, C | existence only | adversarial-examples-computational-constraints, adversarial-examples-prg | deep |
| DNV19 | Computational Limitations in Robust Classification and Win-Win Results | COLT | 2019 | C | existence only, with converse | win-win-robust-learning | deep |
| GJMM20 | Adversarially Robust Learning Could Leverage Computational Hardness | ALT | 2020 | C | adversary dearer | computational-hardness-robust-learning | deep |
| GKVZ22 | Planting Undetectable Backdoors in Machine Learning Models | FOCS | 2022 | C | adversary cheaper | planting-undetectable-backdoors | deep |
| CHLX25 | Backdoor defense, learnability and obfuscation | ITCS | 2025 | D, C | existence only | backdoor-defense-learnability-obfuscation | deep |
| GSVV25 | Oblivious Defense in ML Models: Backdoor Removal without Detection | STOC | 2025 | C, D | not a gap result | oblivious-defense-backdoor-removal | read |
| BRV26 | Statistically Undetectable Backdoors in Deep Neural Networks | ICML | 2026 | C, I | adversary cheaper | no | deep |
| GG25 | A Cryptographic Perspective on Mitigation vs. Detection in Machine Learning | arXiv preprint | 2025 | D, C | existence only | no | read |
| CGZ24 | Undetectable Watermarks for Language Models | COLT | 2024 | C | existence only | undetectable-watermarks-lm | deep |
| ZEF+24 | Watermarks in the Sand: Impossibility of Strong Watermarking | ICML | 2024 | C | adversary cheaper | no | deep |
| CJM20 | Cryptanalytic Extraction of Neural Network Models | CRYPTO | 2020 | C | existence only | cryptanalytic-extraction-nn | read |
| CCHRSS24 | Polynomial Time Cryptanalytic Extraction of Neural Network Models | EUROCRYPT | 2024 | C | existence only | polynomial-time-cryptanalytic-extraction | read |
| BCV16 | Separating Computational and Statistical Differential Privacy in the Client-Server Model | TCC | 2016 | C | existence only | separating-cdp-client-server | read |
| GIKKM23 | Towards Separating Computational and Statistical Differential Privacy | FOCS | 2023 | C, A | existence only | towards-separating-cdp | deep |
| CIM19 | Capacity Bounded Differential Privacy | NeurIPS | 2019 | A, D | not a gap result | capacity-bounded-dp | deep |
| CK21 | Covert Learning: How to Learn with an Untrusted Intermediary | TCC | 2021 | C, D | existence only | covert-learning | read |
| GRSY21 | Interactive Proofs for Verifying Machine Learning | ITCS | 2021 | I, C | verification cheaper than learning, class dependent | no | read |
| JYC+21 | Proof-of-Learning: Definitions and Practice | IEEE S&P | 2021 | C | adversary dearer or equal, claimed | proof-of-learning | deep |
| GSG+23 | LLM Censorship: A Machine Learning Challenge or a Computer Security Problem? | arXiv preprint | 2023 | D | not a gap result | no | skim |

### Opened beyond the cap of 20 sheets

These eleven were opened (arXiv, DOI or Crossref record) and are left without a sheet because of the cap of 20. They cover items the lane scope names and the forward citation found. Statements are from abstracts.

| key | title | venue (evidence) | year | lane | gap sign | in_corpus | tier |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KS09 | Cryptographic hardness for learning intersections of halfspaces (Klivans, Sherstov) | J. Comput. Syst. Sci. 75(1), 2 to 12 (https://doi.org/10.1016/j.jcss.2008.07.008, Crossref). Abstract not retrieved. OpenAlex 98 | 2009 | C | not a gap result (reduction) | no | read |
| DLS14 | From average case complexity to improper learning complexity (Daniely, Linial, Shalev-Shwartz) | STOC 2014 (https://doi.org/10.1145/2591796.2591820, Crossref, arXiv 1311.2272 opened). Abstract: hardness of improper learning from average case hardness of refuting random constraint satisfaction problems, covering DNF, agnostic halfspaces within a constant ratio, and intersections of omega(1) halfspaces. OpenAlex 60, Semantic Scholar 127 | 2014 | C | not a gap result (reduction) | no | read |
| ML23 | Computational Asymmetries in Robust Classification (Marro, Lombardi) | ICML 2023 (arXiv journal_ref, https://arxiv.org/abs/2306.14326). Abstract: attacking ReLU classifiers is NP-hard, ensuring robustness at training time is Sigma-2-P-hard even on one example, and a counter-attack defence reverses the asymmetry. OpenAlex 0, Semantic Scholar 3 | 2023 | C | adversary cheaper (worst case, NP against Sigma-2-P) | no | read |
| GLU24 | On the Computability of Robust PAC Learning (Gourdeau, Lechner, Urner) | COLT 2024 (arXiv comment, https://arxiv.org/abs/2406.10161). Abstract: robust computable PAC learnability is not implied by computable PAC and robust PAC learnability together. Semantic Scholar 6 | 2024 | D | not a gap result | no | skim |
| CPD+24 | Stealing Part of a Production Language Model (Carlini, Paleka, Dvijotham, and eleven others) | ICML 2024 (Semantic Scholar venue field only, https://arxiv.org/abs/2403.06634). Abstract: recovers the embedding projection layer up to symmetries from API access, for under 20 US dollars on Ada and Babbage. Empirical. Semantic Scholar 216 | 2024 | C | existence only | no | read |
| CCH+26 | Polynomial Time Cryptanalytic Extraction of Deep Neural Networks in the Hard-Label Setting (Carlini, Chavez-Saab, Hambitzer, Rodriguez-Henriquez, Shamir) | J. Cryptology 2026 (https://doi.org/10.1007/s00145-026-09586-5 per OpenAlex and Semantic Scholar, publisher page not opened. arXiv 2410.05750 opened). Abstract: polynomial queries and polynomial time with label-only outputs, where Chen et al. (Asiacrypt 2024) needed exponential time. Semantic Scholar 33 | 2026 | C | existence only | no | read |
| CGZ26 | Proofs of Ownership for Machine Learning Models (Canetti, Goldwasser, Zamir) | arXiv preprint (https://arxiv.org/abs/2606.30423). Abstract: for black-box classifiers, under standard cryptographic assumptions, ownership of a concept class is provable if and only if the class is not self-correctable. Semantic Scholar 0 | 2026 | C, D | not a gap result (dichotomy) | no | read |
| DMDS26 | AI Models Can Provably Hide Arbitrary Capabilities (Draguns, Motwani, Douglas, Schroeder de Witt) | arXiv preprint, accepted at NeurIPS 2026 per the arXiv comment (https://arxiv.org/abs/2610.13928). Abstract: encrypted networks inside host weights, activated by a trigger, hard to elicit under cryptographic assumptions, with a small proof of concept. | 2026 | C | adversary cheaper | no (the earlier unelicitable-backdoors-lms is in the corpus) | skim |
| ERGS26 | Backdoor Channels Hidden in Latent Space: Extending Cryptographic Undetectability to Modern Neural Networks (Eggen, Reiestad, Gjosteen, Strumke) | arXiv preprint (https://arxiv.org/abs/2605.13214). Abstract: undetectability is reduced to a hypothesis test between two unknown distributions over parameters, which the authors conjecture intractable, and the evidence is empirical on ResNet and Vision Transformer models. Empirical and Open, no proof. | 2026 | C | existence only, conjectured | no | cite |
| ZCSL24 | Verification of Machine Unlearning is Fragile (Zhang, Chen, Shen, Li) | ICML 2024 (arXiv comment, https://arxiv.org/abs/2408.00929). Abstract: two adversarial unlearning processes circumvent the two kinds of verification strategy, with theoretical analysis and experiments. Semantic Scholar 33 | 2024 | C | adversary cheaper | unlearning-verification-fragile | cite |
| GJK+24 | On the Power of Interactive Proofs for Learning (Gur, Jahanara, Khodabandeh, Rajgopal, Salamatian, Shinkar) | STOC 2024 (arXiv comment and DOI 10.1145/3618260.3649784, https://arxiv.org/abs/2404.08158). Abstract: doubly-efficient proof systems for agnostic PAC learning, a verifier with poly(t) examples for the t largest Fourier characters, and a trivial model if the proof system need not be doubly-efficient. Semantic Scholar 8 | 2024 | I, C | verification cheaper than learning | no | skim |

## 4. Searches that returned nothing

- dblp. The search API on dblp.org answered 429 and then reset the connection. The mirror dblp.uni-trier.de answered with an anti-bot challenge page, which I did not attempt to pass. No venue below rests on dblp. Venue evidence is Crossref (publisher DOIs and the Springer proceedings volume records), PMLR and ICML pages, the DROPS page, and arXiv comment fields.
- Verification of unlearning is computationally hard. Vocabulary: machine unlearning, verification, computationally hard, cryptographic impossibility, proof of unlearning, theorem. The results held no peer-reviewed theorem that verifying unlearning is hard or impossible. One ICLR 2025 workshop paper by Srivastava claims coNP-hardness of exact unlearning and an Exponential Time Hypothesis bound for approximate unlearning. I saw only a search snippet of it, so it is not listed. The nearest opened item is ZCSL24 (fragility of verification). Eisenhofer et al., Verifiable and Provably Secure Machine Unlearning (arXiv 2210.09126, comment field reads SaTML 2025), had only its title and comment opened, so it is not listed.
- Computational hardness of membership inference or reconstruction under a cryptographic assumption. Vocabulary: membership inference, training data reconstruction, cryptographic assumption, information theoretically possible, efficient attacker cannot. Nothing appeared. The hits were sample complexity or query complexity results (the corpus holds haghifam-sample-complexity-mia and query-complexity-reconstruction) and provable efficient attacks on shallow networks.
- Statistical query or low-degree lower bounds against a backdoor or poisoning adversary. Vocabulary: statistical query, lower bound, data poisoning, backdoor detection, computational-statistical gap. Nothing appeared in backdoor detection. The hits were information theoretic (Pichler et al., arXiv 2402.16926, a no-free-lunch result for backdoor detection as hypothesis testing, snippet only and not listed) and an upper bound that is polynomial where an earlier test was exponential.
- Forward citation of CHLX25 on Semantic Scholar gave 3 records, none a new defendability or backdoor defence result. Forward citation of GIKKM23 gave 6 records, none a new separation of computational and statistical privacy (CDP surveys and the corpus paper cdp-inner-product-implies-ot).
- Forward citation of GRSY21 on OpenAlex gave one unrelated record. Semantic Scholar was not queried for GRSY21, JYC+21, KV94 or BCV16, so later work on verification and on the template reduction is covered only by the corpus and by the sheets above.
- ACM and Springer chapter pages returned 403 or an authentication redirect. The KV94 abstract comes from Crossref and the KS09 abstract was not retrieved.
- Request count. Roughly 90 HTTP requests were made, above the guide of about 60, because the dblp route failed and venue evidence had to come from Crossref one DOI at a time.
