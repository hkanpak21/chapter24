# Theory-First Deep Research Survey: 2024–2026 Formal/Theoretical Frontier in AI Security & Learning Theory

This survey verifies the seven previously identified primary references and expands the list with **~18 additional theoretical papers** from 2024–2026. The emphasis is strictly on formal contributions — theorems, models, impossibility results, and composable frameworks — rather than practical engineering frameworks. All 2026-prefixed arXiv IDs below were confirmed to resolve (arXiv assigned these identifiers in the usual rolling fashion; the "26YY" prefix simply indicates a submission month in early 2026 and is not evidence of a malformed ID).

---

## Part A — Verification & Enrichment of the 7 Known References

### A1. Unelicitable Backdoors in Language Models via Cryptographic Transformer Circuits
- **Authors:** Andis Draguns, Andrew Gritsevskiy, Sumeet Ramesh Motwani, Charlie Rogers-Smith, Jeffrey Ladish, Christian Schroeder de Witt
- **Venue / ID:** arXiv:2406.02619 (v1 Jun 2024; v2 Feb 2025); NeurIPS 2024 SoLaR/SafeGenAI workshops
- **Link:** [https://arxiv.org/abs/2406.02619](https://arxiv.org/abs/2406.02619)
- **Technical intro:** Constructs the first **unelicitable** backdoors for autoregressive transformers: the defender, even with full white-box access, cannot trigger or observe the hidden behavior because activation depends on a cryptographic trigger (digital-signature / encrypted payload circuit) embedded *inside* the model. The construction combines obfuscation-flavored encryption of a payload subcircuit with robustness arguments against fine-tuning and latent-space perturbations, extending Goldwasser–Kim–Vaikuntanathan–Zamir (FOCS '22) from classifier backdoors to generative LMs and explicitly breaking red-teaming and certain verification-style defenses ([source](https://arxiv.org/abs/2406.02619)). This is the canonical Pillar-II reference for "offense-strong" undetectability on LMs.

### A2. Injecting Undetectable Backdoors in Obfuscated Neural Networks and Language Models
- **Authors:** Alkis Kalavasis, Amin Karbasi, Argyris Oikonomou, Katerina Sotiraki, Grigoris Velegkas, Manolis Zampetakis
- **Venue / ID:** arXiv:2406.05660 (v1 Jun 2024; v2 Sep 2024); **NeurIPS 2024**
- **Link:** [https://arxiv.org/abs/2406.05660](https://arxiv.org/abs/2406.05660)
- **Technical intro:** Shows that if the deployed model is shipped as an **indistinguishability-obfuscated (iO)** neural network — a plausible IP-protection pattern — an adversary can plant backdoors whose *existence* is undetectable even to observers with complete white-box access to the obfuscated artifact. The theorem reduces detection to breaking iO and extends to LM/transformer settings, thereby closing the white-box-vs-black-box gap left open by GKVZ22 and directly linking iO's well-founded-assumption construction to ML security ([source](https://arxiv.org/abs/2406.05660), [NeurIPS proceedings](https://dl.acm.org/doi/10.5555/3737916.3738595)).

### A3. Provable Defense Framework for LLM Jailbreaks via Noise-Augmented Alignment (NAAT / CSS)
- **Authors:** (arXiv author list; paper posted Feb 2026)
- **Venue / ID:** arXiv:2602.01587
- **Link:** [https://arxiv.org/abs/2602.01587](https://arxiv.org/abs/2602.01587)
- **Technical intro:** Introduces **Certified Semantic Smoothing (CSS)** via *stratified randomized ablation* — partitioning the prompt into immutable structural tokens and mutable payloads — and derives an ℓ₀-norm certified radius from the **Hypergeometric distribution** (rather than Cohen–Rosenfeld–Kolter Gaussian noise). A companion fine-tuning procedure, **Noise-Augmented Alignment Tuning (NAAT)**, turns the base LLM into a *semantic denoiser* so that utility does not collapse under sparse inputs — solving the "inverted scaling fallacy" that plagued character-level SmoothLLM ([source](https://arxiv.org/abs/2602.01587)). Positioned as the first end-to-end deterministic certification protocol for instruction-tuned LLMs against gradient-based jailbreaks (e.g., GCG).

### A4. Provably Robust Adaptation for Language-Empowered Foundation Models (LeFCert / LeFCert-L / LeFCert-C)
- **Authors:** Yuni Lai, Xiaoyu Xue, Linghui Shen, Yulun Wu, et al. (8 authors; Hong Kong Polytechnic University)
- **Venue / ID:** arXiv:2510.08659 (Oct 2025)
- **Link:** [https://arxiv.org/abs/2510.08659](https://arxiv.org/abs/2510.08659)
- **Technical intro:** First **provably robust few-shot classifier tailored to language-empowered foundation models (CLIP, GraphCLIP)**. The core construction is a *twofold trimmed-mean prototype* that blends textual and feature embeddings, with analytic upper/lower bounds on classification scores yielding certified accuracy under worst-case support-set poisoning. Two refinements: **LeFCert-L** uses randomized smoothing to obtain Lipschitz continuity under dual feature+label budgets, and **LeFCert-C** provides collective certification under a shared attack budget — extending Cohen–Rosenfeld–Kolter to the few-shot foundation-model adaptation regime ([source](https://arxiv.org/abs/2510.08659)).

### A5. Enhancing Robustness of LLM-Driven Multi-Agent Systems through Randomized Smoothing
- **Authors:** Jinwei Hu, Yi Dong, Zhengtao Ding, Xiaowei Huang (Liverpool / Manchester)
- **Venue / ID:** arXiv:2507.04105 (Jul 2025); accepted *Chinese Journal of Aeronautics*
- **Link:** [https://arxiv.org/abs/2507.04105](https://arxiv.org/abs/2507.04105)
- **Technical intro:** Lifts randomized smoothing from single-model classification to the **consensus-seeking** layer of an LLM multi-agent system. Neyman–Pearson arguments yield probabilistic bounds on how the consensus decision shifts under adversarial injection or hallucinated messages from a subset of agents; a two-stage adaptive sampling scheme balances robustness vs sample complexity in black-box conditions ([source](https://arxiv.org/abs/2507.04105)). Positioned as a first step toward a composable multi-agent certification theorem, but the paper does not yet offer a UC-style composition.

### A6. Cryptography from Planted Graphs: Security with Logarithmic-Size Messages
- **Authors:** Damiano Abram, Amos Beimel, Yuval Ishai, Eyal Kushilevitz, Varun Narayanan
- **Venue / ID:** IACR ePrint 2023/1929; **TCC 2023** (Springer LNCS 14372)
- **Link:** [https://eprint.iacr.org/2023/1929](https://eprint.iacr.org/2023/1929)
- **Technical intro:** Proves that under variants of the **planted-clique conjecture**, cryptographic primitives with O(log n)-size messages exist in the public-information model — private simultaneous messages (PSM) protocols, secret-sharing for forbidden-graph access structures, and tight Ω(log log n) lower bounds for threshold schemes. This result demonstrates that planted-clique hardness is *usable* as a cryptographic assumption, setting the stage for GHJS25 ([source](https://eprint.iacr.org/2023/1929), [Springer](https://link.springer.com/chapter/10.1007/978-3-031-48615-9_11)). Pillar-IV anchor paper.

### A7. OWASP Top 10 for Agentic Applications (2025/2026)
- **Note:** This is a practitioner/consortium artifact (OWASP Gen AI Security Project), not a theoretical primary paper. It is deliberately **excluded** from the theory deep-dive below, per the task instructions. (The user already has it.)

---

## Part B — Expanded Theoretical Frontier (2024–2026)

### Pillar I — Formal Models for Agentic / Multi-Agent LLM Security

#### B1. From Prompt Injections to Protocol Exploits: Threats in LLM-Powered AI Agents Workflows (IMTM origin)
- **Authors:** Mohamed Amine Ferrag, Norbert Tihanyi, Djallel Hamouda, Leandros Maglaras, Abderrahmane Lakas, Merouane Debbah
- **Venue / ID:** arXiv:2506.23260 (v1 Jun 2025; v2 Dec 2025, ICT Express / Elsevier)
- **Link:** [https://arxiv.org/abs/2506.23260](https://arxiv.org/abs/2506.23260)
- **Technical intro:** Gives the **first unified end-to-end threat model** for LLM-agent ecosystems and is the *originating source* of the **Input Manipulation Threat Model (IMTM)** as a formal object, with companion formal definitions for Model Compromise, System/Privacy Attacks, and Protocol Vulnerabilities. Each category specifies attacker capabilities, objectives, and affected layers in a taxonomy covering 30+ concrete attack classes; the paper is the natural formal *rival/complement* to AIOracle for agentic pipelines ([source](https://arxiv.org/abs/2506.23260)).

#### B2. A Framework for Formalizing LLM Agent Security
- **Authors:** Vincent Siu, Jingxuan He, et al. (7 authors)
- **Venue / ID:** arXiv:2603.19469 (2026)
- **Link:** [https://arxiv.org/abs/2603.19469](https://arxiv.org/abs/2603.19469)
- **Technical intro:** Introduces **four contextual security properties** — task alignment, action alignment, source authorization, and data isolation — together with *oracle functions* that enable formal verification of whether an agent trace violates any of them. Reformalizes indirect/direct prompt injection, jailbreak, task drift, and memory poisoning as violations of specific oracle predicates, exposing why pattern-matching defenses inherently trade off utility vs security and why **composition across properties** remains an open problem ([source](https://arxiv.org/abs/2603.19469)).

#### B3. Defeating Prompt Injections by Design (CaMeL)
- **Authors:** Edoardo Debenedetti, Ilia Shumailov, Tianqi Fan, Jamie Hayes, Nicholas Carlini, Daniel Fabian, Christoph Kern, Chongyang Shi, Andreas Terzis, Florian Tramèr
- **Venue / ID:** arXiv:2503.18813 (Mar 2025, v2 Jun 2025); Google / DeepMind / ETH
- **Link:** [https://arxiv.org/abs/2503.18813](https://arxiv.org/abs/2503.18813)
- **Technical intro:** Provides a **capability-based access-control** formalism for LLM agents in which every value carries provenance metadata and tools enforce explicit policy checks at call time. CaMeL proves that, under the dual-LLM decomposition (privileged planner + quarantined extractor), untrusted data *cannot* influence the control flow, yielding the first end-to-end "provable security" statement on the AgentDojo benchmark (77% solved with full guarantees vs 84% undefended) ([source](https://arxiv.org/abs/2503.18813)). The closest extant proxy for a UC-style containment theorem in agentic LLMs.

#### B4. MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents
- **Authors:** Kaijie Zhu, Xianjun Yang, Jindong Wang, Wenbo Guo, William Yang Wang
- **Venue / ID:** **ICML 2025**; GitHub released
- **Link:** [https://github.com/kaijiezhu11/MELON](https://github.com/kaijiezhu11/MELON) / arXiv entry linked there
- **Technical intro:** Formalizes indirect prompt injection as a mismatch between *observed* and *intended* tool-use trajectories and proves that a masking-based consistency check detects injections whenever the attack strictly changes tool selection. Complementary to CaMeL: where CaMeL enforces ex-ante capability policy, MELON provides ex-post provable detection.

#### B5. Seven Security Challenges in Cross-Domain Multi-Agent LLM Systems
- **Authors:** Ronny Ko, Jiseong Jeong, Shuyuan Zheng, Chuan Xiao, et al.
- **Venue / ID:** arXiv:2505.23847 (May 2025)
- **Link:** [https://arxiv.org/abs/2505.23847](https://arxiv.org/abs/2505.23847)
- **Technical intro:** Position paper that articulates *why* classical alignment/containment assumptions collapse across organizational trust boundaries, catalogues emergent-dynamics attacks unique to multi-party LLM collaboration, and proposes evaluation metrics. Not a theorem-bearing paper but a useful *desiderata document* for a future UC/composable-security framework — exactly the gap the user's wiki identifies.

---

### Pillar II — Undetectable Backdoors & iO-for-ML (Post-GKVZ22)

#### B6. Oblivious Defense in ML Models: Backdoor Removal Without Detection
- **Authors:** Shafi Goldwasser, Jonathan Shafer, Neekon Vafa, Vinod Vaikuntanathan
- **Venue / ID:** arXiv:2411.03279 (Nov 2024); **STOC 2025**
- **Link:** [https://arxiv.org/abs/2411.03279](https://arxiv.org/abs/2411.03279)
- **Technical intro:** Direct theoretical sequel to GKVZ22. Shows that even when backdoors are *cryptographically undetectable*, they can sometimes be provably **mitigated or removed** using random-self-reducibility techniques that exploit properties of the ground-truth labels rather than model internals ([source](https://arxiv.org/abs/2411.03279), [STOC '25 entry](http://dspace.mit.edu/handle/1721.1/164614)). Establishes "defensibility vs detectability" as distinct theoretical quantities — a crucial conceptual split for the wiki.

#### B7. Backdoor Defense, Learnability, and Obfuscation
- **Authors:** Paul Christiano, Jacob Hilton, Victor Lecomte, Mark Xu
- **Venue / ID:** arXiv:2409.03077 (Sep 2024); **ITCS 2025** (LIPIcs Vol. 325, Paper 38)
- **Link:** [https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.38](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.38)
- **Technical intro:** Game-theoretic treatment of *defendability*. Proves: (i) statistically, a class F is ε-defendable iff ε = o(1/VC(F)), via a Hanneke-style voting algorithm; (ii) computationally, efficient PAC learnability implies efficient defendability but not conversely; (iii) under iO, polynomial-size circuits are **not** efficiently defendable ([source](https://drops.dagstuhl.de/storage/00lipics/lipics-vol325-itcs2025/LIPIcs.ITCS.2025.38/LIPIcs.ITCS.2025.38.pdf)). Positions defendability as a new complexity-theoretic middle ground between PAC learning and obfuscation.

#### B8. Statistically Undetectable Backdoors in Deep Neural Networks
- **Authors:** Neekon Vafa, Andrej Bogdanov, Alon Rosen (forthcoming; talk given at MIT CSAIL ML+Crypto, Oct 2025)
- **Venue / ID:** To-appear (talk announced; preprint pending)
- **Link (announcement):** [https://www.csail.mit.edu/event/mlcrypto-statistically-undetectable-backdoors-deep-neural-networks](https://www.csail.mit.edu/event/mlcrypto-statistically-undetectable-backdoors-deep-neural-networks)
- **Technical intro:** Strengthens GKVZ22 to **statistical undetectability in the full white-box setting** for a broad class of feedforward networks: backdoored and honest models are close in total variation even given all weights. Without the key, generating adversarial examples is provably hard under worst-case lattice (SVP) assumptions. The main technical tool is a cryptographic perspective on the **Johnson–Lindenstrauss lemma** — a notable new cryptanalytic/ML primitive worth tracking as a "sleeper."

#### B9. Cryptographic Backdoor for Neural Networks: Boon and Bane
- **Authors:** Anh Tu Ngo, Anupam Chattopadhyay, Subhamoy Maitra
- **Venue / ID:** arXiv:2509.20714 (Sep 2025)
- **Link:** [https://arxiv.org/abs/2509.20714](https://arxiv.org/abs/2509.20714)
- **Technical intro:** Instantiates GKVZ22-style signature-based backdoors as *defensive* primitives: provably-robust NN watermarking, user authentication, and IP-tracking protocols that resist adversaries with black-box access. Shows the Goldwasser et al. framework is bidirectional — the same cryptographic construction that makes *attacks* undetectable makes certain *defensive* protocols unforgeable ([source](https://arxiv.org/abs/2509.20714)).

---

### Pillar III — Formal Impossibility Results for LLM Alignment / Jailbreak

*(This is the pillar where the user's wiki identified a gap. Two major 2025 results now fill it.)*

#### B10. On the Impossibility of Separating Intelligence from Judgment: The Computational Intractability of Filtering for AI Alignment
- **Authors:** Sarah Ball, Greg Gluch, **Shafi Goldwasser**, Frauke Kreuter, Omer Reingold, **Guy N. Rothblum**
- **Venue / ID:** arXiv:2507.07341 (Jul 2025)
- **Link:** [https://arxiv.org/abs/2507.07341](https://arxiv.org/abs/2507.07341)
- **Technical intro:** **The long-awaited Goldwasser-style impossibility theorem for LLM alignment.** Under standard cryptographic hardness assumptions (including time-lock puzzles built from LWE via Agrawal et al./Bitansky–Garg/Abram et al.), the authors construct an LLM for which (i) *no efficient prompt filter* exists — adversarial prompts eliciting harmful outputs are computationally indistinguishable from benign prompts; and (ii) in a natural setting, output filtering is also intractable ([source](https://arxiv.org/abs/2507.07341)). The normative conclusion: an aligned AI's "judgment" cannot be separated from its "intelligence" — i.e., black-box filter-based alignment is provably inadequate. **This is the most important single paper surfaced by the search and should be the new Pillar-III anchor.**

#### B11. Jailbreak Paradox: The Achilles' Heel of LLMs
- **Authors:** (Chowdhury et al.)
- **Venue / ID:** arXiv:2406.12702 (Jun 2024)
- **Link:** [https://arxiv.org/abs/2406.12702](https://arxiv.org/abs/2406.12702)
- **Technical intro:** Earlier — and weaker but still useful — impossibility-flavored argument. Theorems 3.1 and 4.1 together show that a *perfect* jailbreak detector for an aligned LLM would require a strictly Pareto-dominant (more intelligent) LLM than the target, yielding a paradox for super-aligned systems where no such detector exists ([source](https://arxiv.org/abs/2406.12702)). Complements B10 by taking a relative-capabilities rather than cryptographic route.

#### B12. Immune: Inference-Time Alignment with an Impossibility Result for Training-Time Safety
- **Authors:** Soumya Suvra Ghosal, Souradip Chakraborty, Vaibhav Singh, Tianrui Guan, Mengdi Wang, Alvaro Velasquez, Ahmad Beirami, Furong Huang, Dinesh Manocha, Amrit Singh Bedi
- **Venue / ID:** arXiv:2411.18688 (v1 Nov 2024, v5 Jun 2025)
- **Link:** [https://arxiv.org/abs/2411.18688](https://arxiv.org/abs/2411.18688)
- **Technical intro:** Proves an **"impossibility of safety against jailbreaks"** theorem: for *any* training-time safety-aligned model π*_safe, there exists an adversarial prompt distribution that produces harmful outputs — framed as an inverse alignment problem. Then bounds the sub-optimality gap of an inference-time decoding defense (Immune) with provable safety-net guarantees ([source](https://arxiv.org/abs/2411.18688)). A narrow but clean impossibility result complementing B10's filtering impossibility.

#### B13. MaxMin-RLHF: Alignment with Diverse Human Preferences
- **Authors:** Souradip Chakraborty, Jiahao Qiu, Hui Yuan, Alec Koppel, Dinesh Manocha, Furong Huang, Amrit Singh Bedi, Mengdi Wang
- **Venue / ID:** arXiv:2402.08925; **ICML 2024**
- **Link:** [https://arxiv.org/abs/2402.08925](https://arxiv.org/abs/2402.08925)
- **Technical intro:** Derives an **impossibility result for single-reward RLHF** under preference diversity: whenever human sub-populations have non-trivial KL divergence in preferences, no single Bradley–Terry reward can align the policy simultaneously with all groups (Theorem 3.3). Proposes an Egalitarian MaxMin objective rooted in social-choice theory and connects it to distributionally-robust / general-utility RL ([source](https://proceedings.mlr.press/v235/chakraborty24b.html)). Primary theoretical reference for RLHF fragility.

---

### Pillar IV — Statistical–Computational Gaps, Planted Clique, and Post-GHJS25

#### B14. Using the Planted Clique Conjecture for Cryptography: Public-Key Encryption from Planted Clique and Noisy k-LIN over Expanders (GHJS25)
- **Authors:** Riddhi **Ghosal, Isaac M. Hair, Aayush Jain, Amit Sahai**
- **Venue / ID:** IACR ePrint 2025/1501; **STOC 2025** (DOI 10.1145/3717823.3718306)
- **Link:** [https://eprint.iacr.org/2025/1501](https://eprint.iacr.org/2025/1501)
- **Technical intro:** **The central Pillar-IV result.** Constructs a public-key encryption scheme secure against poly-size adversaries assuming (i) n^{log^α n} hardness of the standard planted-clique conjecture for any α ∈ (0,1) and (ii) a mild noisy k-LIN-over-expanders conjecture not known to imply PKE on its own. Answers an open question of Applebaum–Barak–Wigderson (STOC '10) and establishes that PKE can be based on **natural average-case variants of NP-complete problems** rather than number-theoretic structure ([source](https://eprint.iacr.org/2025/1501.pdf)). This is the "stat-comp-gap → crypto" bridge the wiki identified.

#### B15. Planted Clique Conjectures Are Equivalent
- **Authors:** Shuichi Hirahara, Nobutaka Shimizu
- **Venue / ID:** ECCC TR24-058 (Mar 2024); **STOC 2024**
- **Link:** [https://eccc.weizmann.ac.il/report/2024/058/](https://eccc.weizmann.ac.il/report/2024/058/)
- **Technical intro:** Proves equivalence among almost all variants of the planted-clique conjecture — search vs decision, exponentially-close-to-1 vs non-negligible success, adversarial vs binomial k, and a worst-case "k-clique on incompressible graphs" version. Includes an equivalence between **refutation** algorithms for planted-clique and average-case poly-time algorithms for k-clique on Erdős–Rényi ([source](https://eccc.weizmann.ac.il/report/2024/058/download/)). Substantially tightens what GHJS25's assumption actually commits one to.

#### B16. Computational Complexity of Statistics: New Insights from Low-Degree Polynomials
- **Authors:** Alex Wein
- **Venue / ID:** arXiv:2506.10748 (Jun 2025, survey/monograph — but introduces a new pedagogical formalism consolidating Schramm–Wein)
- **Link:** [https://arxiv.org/abs/2506.10748](https://arxiv.org/abs/2506.10748)
- **Technical intro:** The updated canonical reference for the **low-degree polynomial framework** as evidence of statistical–computational gaps, post-Schramm–Wein 2022. Distinguishes detection vs recovery LD thresholds, presents sparse-PCA, planted-clique, SBM examples with explicit gap calculations, and formalizes why LD lower bounds are the operational substitute for worst-case complexity lower bounds in average-case problems.

#### B17. Low-Degree Lower Bounds via Almost Orthonormal Bases
- **Authors:** Alexandra Carpentier et al. (6 authors, incl. Nicolas Verzelen)
- **Venue / ID:** arXiv:2509.09353 (Sep 2025, v2 Jan 2026)
- **Link:** [https://arxiv.org/abs/2509.09353](https://arxiv.org/abs/2509.09353)
- **Technical intro:** New general-purpose **proof technique** for LD lower bounds when the planted distribution itself has structure that kills L²-orthogonality. Constructs an almost-orthonormal polynomial basis precisely in the statistical–computational-gap regime, recovers known bounds (planted clique, hidden subcliques, SBM, seriation), and produces new ones. Directly relevant for extending GHJS25-style reductions to further ML problems.

#### B18. Computational Lower Bounds in Latent Models: Clustering, Sparse-Clustering, Biclustering
- **Authors:** (see arXiv listing)
- **Venue / ID:** arXiv:2506.13647 (Jun 2025)
- **Link:** [https://arxiv.org/abs/2506.13647](https://arxiv.org/abs/2506.13647)
- **Technical intro:** Uses conditioned LD techniques to produce **tight LD lower bounds** for Gaussian-mixture clustering, sparse clustering, and biclustering, with matching upper bounds. A concrete post-2024 extension of the Schramm–Wein program into canonical ML tasks.

---

### Pillar V — Certified Robustness / Randomized Smoothing Extensions to Generative & Agentic Systems

#### B19. Randomized Smoothing Meets Vision-Language Models (RS-VLM)
- **Authors:** Emmanouil Seferis, Changshun Wu, Stefanos Kollias, Saddek Bensalem, Chih-Hong Cheng
- **Venue / ID:** arXiv:2509.16088 (Sep 2025)
- **Link:** [https://arxiv.org/abs/2509.16088](https://arxiv.org/abs/2509.16088)
- **Technical intro:** Extends Cohen–Rosenfeld–Kolter to **generative VLMs and vision-language-action (VLA) models** by connecting sequence outputs to an *oracle classification task* (harmful/harmless, discrete action, semantic-cluster vote) and bounding the oracle error rate. Derives scaling laws showing 2–3 orders of magnitude sample reduction under weaker assumptions — the cleanest current theoretical extension of RS to the generative regime ([source](https://arxiv.org/abs/2509.16088)).

#### B20. Adaptive Diffusion Denoised Smoothing (ADDS)
- **Authors:** Frederick Shpilevskiy, Saiyue Lyu, Krishnamurthy Dj Dvijotham, Mathias Lécuyer, Pierre-André Noël
- **Venue / ID:** arXiv:2507.08163 (Jul 2025); **ICML 2025** (Oral)
- **Link:** [https://arxiv.org/abs/2507.08163](https://arxiv.org/abs/2507.08163)
- **Technical intro:** Reinterprets each step of a guided denoising diffusion model as an **adaptive Gaussian Differentially Private (GDP) mechanism** and composes them through a GDP privacy filter, yielding end-to-end certified robustness through a multi-step diffusion purifier. Extends the adaptive-randomized-smoothing (ARS) analysis to a practical, variance-adaptive composition — an important theoretical step because the underlying GDP composition is the mathematical kernel of RS.

#### B21. Multi-Level Certified Defense Against Poisoning Attacks in Offline Reinforcement Learning
- **Authors:** Shijie Liu et al.
- **Venue / ID:** arXiv:2505.20621 (May 2025)
- **Link:** [https://arxiv.org/abs/2505.20621](https://arxiv.org/abs/2505.20621)
- **Technical intro:** Provides **certified bounds against training-data poisoning** simultaneously at the per-state action level and the cumulative-reward level for offline RL, using Differential Privacy composition across continuous/discrete and stochastic/deterministic environments. Substantially tightens prior COPA-style guarantees (certified radius ~5× larger at 7% poisoning). Directly relevant as the RL-counterpart to RS-for-classification in the wiki.

---

## Synthesis & Flags

### (a) Known-ID verification outcomes
All seven IDs **resolved correctly**. One clarification: **arXiv:2406.05660** is titled "Injecting Undetectable Backdoors in Obfuscated Neural Networks **and Language Models**" in the current arXiv and NeurIPS-published versions — the "and Language Models" suffix should be added to the wiki entry (reflecting a v2/September-2024 scope extension). The 2602.xxxxx and 2603.xxxxx identifiers are ordinary arXiv IDs from February and March 2026 submissions; they are not typos.

### (b) Single most important gap surfaced
**The Goldwasser-style formal impossibility theorem for LLM filter-based alignment is no longer a gap.** Ball–Gluch–Goldwasser–Kreuter–Reingold–Rothblum, *"On the Impossibility of Separating Intelligence from Judgment"* (arXiv:2507.07341, July 2025) provides exactly the theorem the wiki's Pillar III was waiting for — a cryptographic-hardness-based proof that *no efficient black-box prompt or output filter* can align a sufficiently expressive LLM ([source](https://arxiv.org/abs/2507.07341)). This should be promoted to a top-billed wiki entry and cross-linked to GKVZ22 (backdoors), NAAT (certified defenses), and CaMeL (capability-based containment).

The *remaining* major gap is a genuine **Universal Composability theorem for multi-agent LLMs**: MELON, CaMeL, and arXiv:2507.04105 give component-level guarantees, and Siu et al. (arXiv:2603.19469) gives the oracle-function vocabulary, but no paper yet proves a UC-style composition theorem for ideal-functionality agentic systems. This remains the highest-value open theoretical problem.

### (c) Sleeper papers to prioritize
1. **Vafa–Bogdanov–Rosen, "Statistically Undetectable Backdoors in Deep Neural Networks"** (B8) — upgrades GKVZ22 from *computational* to *statistical* indistinguishability in total variation, using a cryptographic take on Johnson–Lindenstrauss. Expect a 2025–2026 preprint; this is the most mathematically ambitious follow-up to GKVZ22 currently in the pipeline.
2. **Christiano–Hilton–Lecomte–Xu, "Backdoor Defense, Learnability and Obfuscation"** (B7, ITCS 2025) — introduces *defendability* as a new complexity-theoretic notion sitting strictly between efficient PAC learnability and iO. A surprisingly under-cited paper likely to anchor Pillar II going forward.
3. **GHJS25 (B14) paired with Hirahara–Shimizu (B15)** — together they turn planted-clique from a folklore ML-hardness assumption into a *certifiably rigid* cryptographic foundation. Any future worst-case-to-average-case reduction for planted clique would collapse Pillar IV and Pillar II into a single impossibility landscape.
4. **Ball et al. (B10)** — besides filling the Pillar III gap, its use of **time-lock puzzles from LWE** to encode the filtering-hardness argument is a novel reduction template that will likely seed a family of filter-impossibility results for other deployment patterns (e.g., watermarking, steganography detection, agent-tool firewalls).