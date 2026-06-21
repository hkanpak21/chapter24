# Wiki Log

Append-only chronological record of all operations. Format: `## [YYYY-MM-DD] <operation> | <description>`

Parse the last 5 entries: `grep "^## \[" wiki/log.md | tail -5`

---

## [2026-04-12] init | Wiki initialized

Wiki structure created. Three source PDFs staged in `raw/` awaiting ingestion.

---

## [2026-04-12] ingest | A Complexity Theoretic Approach to Adversarial Machine Learning

**Source**: `raw/A Complexity Theoretic Approach to Adversarial Machine Learning.pdf`  
**Author**: Saeed Mahloujifar (2019 research statement)  
**Pages created**:
- `wiki/sources/complexity-theoretic-adversarial-ml.md`
- `wiki/concepts/concentration-of-measure.md`
- `wiki/concepts/computational-concentration-of-measure.md`
- `wiki/concepts/evasion-attacks.md`
- `wiki/concepts/poisoning-attacks.md`
- `wiki/concepts/p-tampering-model.md`
- `wiki/entities/saeed-mahloujifar.md`
- `wiki/entities/mohammad-mahmoody.md`

**Key result**: Adversarial vulnerability is provably inherent via concentration of measure; polynomial-time attacks match IT bounds on product distributions; (k,p) poisoning attacks with provable lower bounds.

---

## [2026-04-12] ingest | Extending the Formalism and Theoretical Foundations of Cryptography to AI

**Source**: `raw/Extending the Formalism and Theoretical Foundations of Cryptography to AI.pdf`  
**Authors**: Federico Villa, F. Betül Durak, Tadayoshi Kohno, Tapdig Maharramli, Franziska Roesner (arXiv 2026)  
**Pages created**:
- `wiki/sources/extending-formalism-cryptography-ai.md`
- `wiki/concepts/aioracle-framework.md`
- `wiki/concepts/attack-taxonomy-llms.md`
- `wiki/entities/federico-villa.md`
- `wiki/entities/tadayoshi-kohno.md`
- `wiki/entities/franziska-roesner.md`
- `wiki/entities/betul-durak.md`

**Key result**: AIOracle abstraction formalizes agentic LLM security; security game unifies C/I/A; DPP-secure training provably conflicts with completeness; dual construction enables modular composition.

---

## [2026-04-12] ingest | Reducibility and Statistical-Computational Gaps from Secret Leakage

**Source**: `raw/Reducibility and Statistical Computational Gaps from Secret Leakage.pdf`  
**Authors**: Matthew Brennan, Guy Bresler (arXiv 2020, 175 pages — read pages 1-20 covering abstract, intro, summary of results)  
**Pages created**:
- `wiki/sources/reducibility-statistical-computational-gaps.md`
- `wiki/concepts/planted-clique.md`
- `wiki/concepts/secret-leakage-planted-clique.md`
- `wiki/concepts/statistical-computational-gaps.md`
- `wiki/concepts/average-case-reductions.md`
- `wiki/concepts/statistical-query-model.md`
- `wiki/entities/matthew-brennan.md`
- `wiki/entities/guy-bresler.md`

**Key result**: PC_ρ (Secret Leakage Planted Clique) enables first web of average-case reductions among statistically disparate problems; tight gaps for RSME, SBM, sparse PCA, tensor PCA, mixtures of linear regressions, and more.

**Note**: Paper is 175 pages. Only introduction and summary of results (pp. 1-20) were read. Full technical sections (reduction proofs, Parts II-III) not yet ingested — recommend a follow-up deep read of sections 6-17.

---

## [2026-04-12] ingest | A Universal Law of Robustness via Isoperimetry

**Source**: arXiv:2105.12806 (fetched via web)
**Authors**: Sébastien Bubeck, Mark Sellke — NeurIPS 2021 Outstanding Paper
**Pages created**: `wiki/sources/universal-law-of-robustness.md`, `wiki/concepts/universal-law-of-robustness.md`, `wiki/entities/sebastien-bubeck.md`, `wiki/entities/mark-sellke.md`
**Key result**: Smooth interpolation of n points in R^d requires Ω(nd) parameters — formal explanation for why overparameterization is necessary for robustness. ImageNet implication: ~10^11 parameters needed.

---

## [2026-04-12] ingest | Planting Undetectable Backdoors in Machine Learning Models

**Source**: arXiv:2204.06974 (fetched via web)
**Authors**: Shafi Goldwasser, Michael P. Kim, Vinod Vaikuntanathan, Or Zamir — FOCS 2022
**Pages created**: `wiki/sources/planting-undetectable-backdoors.md`, `wiki/concepts/undetectable-backdoors.md`, `wiki/entities/shafi-goldwasser.md`, `wiki/entities/vinod-vaikuntanathan.md`
**Key result**: Under OWFs, backdoors can be planted into any classifier that are black-box computationally undetectable. Under lattice hardness, white-box undetectable backdoors exist for RFF models. Fundamental impossibility for ML auditing.

---

## [2026-04-12] ingest | Computational Limitations in Robust Classification and Win-Win Results

**Source**: arXiv:1902.01086 (fetched via web)
**Authors**: Akshay Degwekar, Preetum Nakkiran, Vinod Vaikuntanathan — COLT 2019
**Pages created**: `wiki/sources/win-win-robust-learning.md`, `wiki/concepts/win-win-theorem.md`, `wiki/entities/akshay-degwekar.md`
**Key result**: Win-Win Theorem — if a classification task has an efficient robust classifier but cannot be robustly learned efficiently, then one-way functions exist. Places adversarial robustness hardness within the cryptographic world structure.

---

## [2026-04-12] ingest | Adversarially Robust Learning: A Generic Minimax Optimal Learner and Characterization

**Source**: arXiv:2209.07369 (fetched via web)
**Authors**: Omar Montasser, Steve Hanneke, Nathan Srebro — NeurIPS 2022
**Pages created**: `wiki/sources/robust-pac-learning-characterization.md`, `wiki/entities/omar-montasser.md`, `wiki/entities/nathan-srebro.md`, `wiki/entities/steve-hanneke.md`
**Key result**: Global one-inclusion graph dimension exactly characterizes adversarially robust PAC learnability — both which classes are robustly learnable and their sample complexity. Resolves open problem from COLT 2019. Local learners are provably suboptimal.

---

## [2026-04-12] ingest | A Framework for Formalizing LLM Agent Security

**Source**: arXiv:2603.19469 (fetched via web)
**Authors**: Vincent Siu, Jingxuan He, Kyle Montgomery, Zhun Wang, Neil Gong, Chenguang Wang, Dawn Song — March 2026
**Pages created**: `wiki/sources/formalizing-llm-agent-security.md`, `wiki/entities/vincent-siu.md`, `wiki/entities/dawn-song.md`
**Key result**: Four security properties (Task Alignment, Action Alignment, Source Authorization, Data Isolation) with formal oracle functions; integrated security predicate; attack taxonomy via property violations. Complementary to Villa et al. — covers operational authorization rather than LEARN/INFER security games.

---

## [2026-04-12] ingest | Computational Complexity of Statistics: New Insights from Low-Degree Polynomials

**Source**: arXiv:2506.10748 (fetched via web)
**Authors**: Alexander S. Wein — survey, June 2025
**Pages created**: `wiki/sources/low-degree-polynomials-survey.md`, `wiki/concepts/low-degree-polynomial-framework.md`, `wiki/entities/alexander-wein.md`
**Key result**: Survey of low-degree framework; SQ-LD equivalence theorem (formal); known counterexamples (Zadik et al. COLT 2022, robust subspace recovery 2026); consensus that framework applies to "structureless" problems but fails for algebraically structured ones.

---

## [2026-04-12] ingest | Detection-Recovery and Detection-Refutation Gaps via Reductions from Planted Clique

**Source**: arXiv:2306.17719 (fetched via web)
**Authors**: Guy Bresler, Tianze Jiang — COLT 2023
**Pages created**: `wiki/sources/detection-recovery-refutation-gaps.md`
**Key result**: PC_ρ conjecture implies detection-recovery and detection-refutation gaps for Planted Dense Subgraph — different computational tasks on the same model have different thresholds. Extends Brennan-Bresler framework beyond detection.

---

## [2026-04-12] ingest | Simplifying Adversarially Robust PAC Learning with Tolerance

**Source**: arXiv:2502.07232 (fetched via web)
**Authors**: Hassan Ashtiani, Vinayak Pathak, Ruth Urner — February 2025
**Pages created**: `wiki/sources/tolerant-robust-pac-learning.md`, `wiki/entities/hassan-ashtiani.md`, `wiki/entities/ruth-urner.md`
**Key result**: First simple learner achieving sample complexity linear in VC-dimension for adversarially robust PAC learning under tolerance relaxation. RERM-and-Smooth and RERM-and-Discretize algorithms. Improper learning is necessary even for VC(H) = 1.

---

## [2026-04-23] raw/ audit | Replaced 10 incorrect PDFs

Audited all 45 PDFs in `raw/`; found 10 where filename-metadata and actual content disagreed (e.g., `Hirahara2024_PlantedCliqueConjecturesEquivalent.pdf` was a Portuguese physics paper on partially coherent beams). Deleted and re-downloaded from correct sources (arXiv, IACR eprint, ECCC). One filename also renamed: `Montasser2022_AdversariallyRobustLearningWithTolerance.pdf` → `Montasser2022_GenericMinimaxOptimalLearner.pdf` (original was doubly wrong — content + attribution). All replacements verified by first-page text extraction.

---

## [2026-04-23] ingest | The Curse of Concentration in Robust Learning

**Source**: `raw/Mahloujifar2019_CurseConcentrationRobustLearning.pdf`
**Authors**: Saeed Mahloujifar, Dimitrios I. Diochnos, Mohammad Mahmoody — AAAI 2019 (arXiv:1809.03063)
**Pages updated/created**: `wiki/sources/curse-of-concentration.md` (deep-ingest refinement), `wiki/concepts/levy-family.md` (new), updates to `wiki/concepts/concentration-of-measure.md`, `wiki/concepts/evasion-attacks.md`, `wiki/concepts/poisoning-attacks.md`.
**Key result**: Any concentrated metric probability space + Ω(1) initial classifier error ⇒ adversarial risk → 1 under O(√n) perturbation. Generalizes Gilmer/Fawzi/Diochnos as special cases of Lévy families. Poisoning corollary: Õ(√m) correctly-labeled offline substitutions drive any bad-property probability from 1/poly(m) to ≈1 (stronger than prior online p-tampering).

---

## [2026-04-23] ingest | Empirically Measuring Concentration: Fundamental Limits on Intrinsic Robustness

**Source**: `raw/Mahloujifar2019_EmpiricallyMeasuringConcentration.pdf`
**Authors**: Saeed Mahloujifar, Xiao Zhang, Mohammad Mahmoody, David Evans — NeurIPS 2019 (arXiv:1905.12202)
**Pages updated/created**: `wiki/sources/empirically-measuring-concentration.md` (added formal Defs 3.1, 3.2, Thms 3.3, 3.5, CR(T,n) family), `wiki/entities/xiao-zhang.md` (new), updates to `wiki/concepts/intrinsic-robustness.md`.
**Key result**: First provably-convergent estimator of the concentration function from samples, via parameterized subset families with controlled complexity penalties for G and G_ε. Empirical headline on MNIST/CIFAR-10: the concentration-based intrinsic-robustness bound is order-of-magnitude larger than SOTA robust-classifier accuracy — concentration alone does not explain adversarial vulnerability; room for better defenses exists.

---

## [2026-04-23] ingest | Universal Multi-Party Poisoning Attacks

**Source**: `raw/Mahloujifar2019_MultiPartyPoisoningAttacks.pdf`
**Authors**: Saeed Mahloujifar, Mohammad Mahmoody, Ameer Mohammed — ICML 2019 (arXiv:1809.03474)
**Pages updated**: `wiki/sources/multi-party-poisoning.md` (corrected main theorem: multiplicative μ → μ^{1−pk/m} rather than additive Ω(kp/m); added generalized p-tampering engine), `wiki/concepts/k-p-poisoning-model.md` (same correction + generalized p-tampering detail), `wiki/concepts/poisoning-attacks.md` (same correction).
**Key result**: (k,p)-poisoning model = k corrupt parties of m, each corrupted message within TV distance p of honest. Poly-time universal attack raises any bad-property probability from μ to μ^{1−pk/m}. Subsumes p-tampering (k=m) and static k-corruption (p=1). Attacks federated learning even with DP/secure aggregation. Technical engine: generalized p-tampering on random processes with correlated tamperable indices, imported from cryptographic coin-tossing literature.

---

## [2026-04-23] ingest | Computational Concentration of Measure: Optimal Bounds, Reductions, and More

**Source**: `raw/Etesami2020_ComputationalConcentrationMeasure.pdf`
**Authors**: Omid Etesami, Saeed Mahloujifar, Mohammad Mahmoody — SODA 2020 (arXiv:1907.05401)
**Pages updated**: `wiki/sources/computational-concentration-of-measure-etesami.md` (preserved; was already thorough). Updates to `wiki/concepts/computational-concentration-of-measure.md`, `wiki/concepts/poisoning-attacks.md` (strong-adaptive-corruption note).
**Key result**: Resolves the [MM19] open question — MUCIO algorithm achieves IT-optimal Hamming-distance O(√(n·ln(1/εδ))) perturbation in poly(n/εδ) time for any set with Pr[S] ≥ ε on product spaces, for the full range 1/poly(n) ≤ ε. Introduces algorithmic reductions between CCoM problems across metric probability spaces; applied to lift to Gaussian ℓ₁. Extensions: weighted Hamming, computational McDiarmid, coin-tossing attacks in strong-adaptive-corruption model, exponential lower bounds for non-adaptive methods.

---

## [2026-04-23] analysis | Reading Pathway for the Formal-Security Corpus

**Page created**: `wiki/analyses/reading-pathway-formal-security.md`
**Purpose**: Provides a recommended order of reading the 45-paper corpus, clustered by the three research programs (adversarial robustness via concentration, statistical-computational gaps via reductions, cryptographic AI security) plus cross-cutting defenses. Includes prerequisite structure and suggested starting points for different backgrounds.

---

## [2026-04-23] ingest-batch | 10 remaining PDFs deeply ingested

Closed the `raw/` ↔ `wiki/sources/` gap. The 10 un-ingested papers from the 2026-04-12 scaffolding are now full ingests:

1. **[Deep Learning with Differential Privacy (ACG+16)](sources/deep-learning-differential-privacy.md)** — DP-SGD + moments accountant; canonical DP mechanism for deep learning.
2. **[Adversarially Robust PAC Regression (AH23)](sources/adversarially-robust-pac-regression.md)** — fat-shattering-dimension characterization for robust real-valued PAC learning.
3. **[Certified Robustness via Randomized Smoothing (CRK19)](sources/certified-robustness-randomized-smoothing.md)** — Neyman-Pearson-tight ℓ₂ certified radius; scales to ImageNet.
4. **[Robust Estimators in High Dimensions (DKKLMS16)](sources/robust-estimators-high-dimensions.md)** — launched algorithmic robust statistics; dimension-independent poly-time robust Gaussian/product estimation.
5. **[Certified Robustness via DP / PixelDP (LAGHJ19)](sources/certified-robustness-differential-privacy.md)** — first DP-based certified adversarial defense.
6. **[Universal Jailbreak Backdoors from Poisoned RLHF (RT23)](sources/universal-jailbreak-rlhf-backdoors.md)** — first universal (not target-specific) backdoor in RLHF-aligned LLMs via annotator poisoning.
7. **[Provably Robust SmoothAdv (SYLZZ+19)](sources/provably-robust-smoothadv.md)** — adversarial training for smoothed classifiers; SOTA ℓ₂ certified robustness.
8. **[Certified Defenses for Data Poisoning (SKL17)](sources/certified-defenses-data-poisoning.md)** — first certified-upper-bound + matching-attack framework for poisoning.
9. **[Robustness May Be at Odds with Accuracy (TSETM19)](sources/robustness-at-odds-accuracy.md)** — provable accuracy-robustness tradeoff persisting at infinite-data limit.
10. **[Provable Defenses via Convex Polytope (WK18)](sources/provable-defenses-convex-polytope.md)** — first certified-training framework for ReLU networks via LP relaxation.

**State**: All 47 raw/ PDFs now have corresponding wiki source pages. Lint: 0 broken links.

---

## [2026-04-23] rename | Standardized raw/ PDF naming to [INITIALS][YY]_[Topic].pdf

Renamed all 45 `raw/` PDFs from ad-hoc formats (`Mahloujifar2019_CurseConcentrationRobustLearning.pdf`, `Reducibility and Statistical Computational Gaps from Secret Leakage.pdf`, etc.) to the standard `[INITIALS][YY]_[Topic].pdf` convention.

**Convention**: initials = first letter of each author's last name (capitalized); truncate to 5 + `+` if more than 5 authors; year = last 2 digits of publication year; topic = compact title keyword.

**Historical references in log.md preserved** — old filenames in prior log entries accurately record state at the time of those operations. The rename is destructive only at the filesystem layer; wiki pages reference sources by page slug, not filename, so no wiki breakage.

**Mapping** (abridged — full list in shell history):
| Old | New |
|---|---|
| `A Complexity Theoretic Approach to Adversarial Machine Learning.pdf` | `M19_ComplexityTheoreticApproach.pdf` |
| `Mahloujifar2019_CurseConcentrationRobustLearning.pdf` | `MDM19_CurseOfConcentration.pdf` |
| `Mahloujifar2019_EmpiricallyMeasuringConcentration.pdf` | `MZME19_EmpiricallyMeasuringConc.pdf` |
| `Mahloujifar2019_MultiPartyPoisoningAttacks.pdf` | `MMM19_MultiPartyPoisoning.pdf` |
| `Etesami2020_ComputationalConcentrationMeasure.pdf` | `EMM20_ComputationalConcentration.pdf` |
| `Reducibility and Statistical Computational Gaps from Secret Leakage.pdf` | `BB20_SecretLeakagePC.pdf` |
| `Extending the Formalism and Theoretical Foundations of Cryptography to AI.pdf` | `VDKMR26_CryptoToAI.pdf` |
| `Bubeck2021_UniversalLawRobustnessIsoperimetry.pdf` | `BS21_UniversalLawRobustness.pdf` |
| `Goldwasser2022_UndetectableBackdoorsMachineLearning.pdf` | `GKVZ22_UndetectableBackdoors.pdf` |
| `Hirahara2024_PlantedCliqueConjecturesEquivalent.pdf` | `HS24_PCConjecturesEquivalent.pdf` |
| …and 35 more analogous renames. |  |

---

## [2026-04-23] ingest-batch | 7 new relevant papers added to raw/ and ingested

Filled the highest-leverage citation gaps identified during the lint pass — papers referenced in the convergence survey or in wiki cross-references but absent from `raw/`:

1. **[GMF+18 — Adversarial Spheres](sources/adversarial-spheres.md)** (Gilmer et al., ICLR Workshop 2018; arXiv:1801.02774) — foundational geometric/isoperimetric explanation for adversarial examples; MDM19's direct predecessor.
2. **[SSTTM18 — Robust Generalization Requires More Data](sources/robust-generalization-more-data.md)** (Schmidt, Santurkar, Tsipras, Talwar, Mądry, NeurIPS 2018; arXiv:1804.11285) — formal information-theoretic √d sample-complexity gap between standard and robust generalization.
3. **[BLPR19 — Adversarial Examples from Cryptographic PRG](sources/adversarial-examples-prg.md)** (Bubeck, Lee, Price, Razenshteyn, arXiv:1811.06418) — strengthens BPR19 under standard OWF/PRG assumption; closes the BPR line.
4. **[SW22 — Computational Barriers to Estimation from Low-Degree Polynomials](sources/low-degree-estimation-schramm-wein.md)** (Schramm, Wein, Annals of Statistics 2022; arXiv:2008.02269) — extends low-degree framework from detection to estimation/recovery.
5. **[GHJS25 — PKE from Planted Clique](sources/pke-from-planted-clique.md)** (Ghosal, Hair, Jain, Sahai, STOC 2025; IACR ePrint 2025/1501) — PKE from standard PC conjecture + noisy k-LIN; closes Applebaum-Barak-Wigderson 2010 open question.
6. **[HN23 — Learning in Pessiland](sources/learning-in-pessiland.md)** (Hirahara, Nanashima, FOCS 2023; ECCC TR23-100) — Pessiland is a wonderland for ML; ¬OWF ⇒ efficient learning via universal extrapolation.
7. **[BW08 — Public-Key Cryptography from Different Assumptions](sources/pkc-from-different-assumptions.md)** (Barak, Wigderson, IACR ePrint 2008/335; ABW10 STOC 2010) — first PKE from combinatorial / planted-subgraph assumptions; predecessor to GHJS25.

**State**: `raw/` now holds 52 PDFs (45 original + 7 new). Wiki sources count: 54 (includes two source pages for Mahloujifar umbrella and its constituent papers). All 54 sources have corresponding `raw/` PDFs; all sources link to the correct entity/concept pages; lint is clean (0 broken links).

---

## [2026-04-23] notes | End-to-end proof in output/ — SQ-hardness for black-box attacks

Created `output/` folder at project root and wrote a primitive end-to-end proof.

**Files**:
- [output/README.md](../output/README.md) — index tying external reports (compass deep-research artifact), wiki analyses (reading-pathway, web-research-frontier, deep-research-prompt), and the proof PDF.
- [output/proof.pdf](../output/proof.pdf) — 6-page LaTeX-compiled proof. Contains an end-to-end derivation: black-box adversary attacking the output of an SQ-implementable learner trained on a planted-clique-encoded dataset has distinguishing advantage bounded by the FGRVX17 SQ-PC lower bound *evaluated at the learner's parameters* — adversary's own query budget does not enter. LaTeX source: `.tools/proof.tex`. Compiled with locally-installed Tectonic 0.16.9 in `.tools/tectonic`.

**The theorem in one line**: For (q_L, τ_L)-SQ-implementable learner L with vertex-row encoding D_G of graph G drawn from P_n,0 or P_n,k, any black-box adversary A satisfies adv(A) ≤ adv_SQ(n, k, q_L, τ_L) — the FGRVX17 SQ-PC distinguishing-advantage bound at the learner's parameters.

**Mechanism**: A's queries to M are post-training computations on M itself, requiring no further SQ access to G. So an SQ algorithm B can simulate L using q_L SQ queries on G's distribution, reconstruct M from the SQ answers (deterministic L), then run A inside the simulation. B inherits A's advantage at L's SQ budget. FGRVX17 bounds B; same bound applies to A.

**Decoupling of query budgets**: this is the load-bearing observation. The adversary's query count q_A does not appear in the bound. Information about G in M is fixed at training time; no amount of post-training querying changes it.

**Capacity is implicit**: M is reconstructed from q_L · log(1/τ_L) bits of SQ answers, so model capacity ≤ q_L · log(1/τ_L) bits is automatic — no separate capacity hypothesis needed.

**Specializations cover (a)–(d)**: attribute inference, backdoor activation, membership inference, model extraction all reduce to the primitive distinguishing advantage bound by instantiating A's decision rule.

**Caveats explicitly stated**: proof breaks for (i) non-SQ-implementable learners (kNN, retrieval-augmented memorization), (ii) non-vertex-row encodings, (iii) white-box adversaries (need separate iO/OWF assumption à la CHLX25), (iv) per-round federated observation (Setting A; needs Mahloujifar generalized-p-tampering composition).

**Citations grounded in wiki**:
- [feldman-statistical-algorithms-planted-clique](sources/feldman-statistical-algorithms-planted-clique.md) — primitive SQ-PC lower bound (FGRVX17 Theorem 1.1).
- [reducibility-statistical-computational-gaps](sources/reducibility-statistical-computational-gaps.md) — PC_ρ secret-leakage variant.
- [hirahara-planted-clique-conjectures-equivalent](sources/hirahara-planted-clique-conjectures-equivalent.md) — robustness of the assumption.
- [pke-from-planted-clique](sources/pke-from-planted-clique.md) — PC as cryptographic primitive at the same regime.
- [backdoor-defense-learnability-obfuscation](sources/backdoor-defense-learnability-obfuscation.md) — template for the white-box extension.
- [multi-party-poisoning](sources/multi-party-poisoning.md) — generalized p-tampering for Setting A extension.
- [computational-concentration-of-measure-etesami](sources/computational-concentration-of-measure-etesami.md) — adjacent algorithmic-reductions framework.

---

## [2026-04-23] ingest-mega-batch | 20 frontier papers from 2024–2026 deep-research survey

Processed a comprehensive theory-first deep-research survey (stored as `compass_artifact_wf-6dd26eed-7b63-4913-af9a-4d6edcae8017_text_markdown.md`) that verified 7 priority candidates from my earlier web research and added ~14 additional theoretical papers. Downloaded all 20 PDFs to `raw/`, verified each by first-page extraction, and wrote full source pages.

**Most significant finding**: The **Goldwasser-style formal impossibility theorem for LLM filter-based alignment** — which my prior 2026-frontier analysis marked as the biggest remaining open gap — **is published**:

**[BGGKRR25 — Ball, Gluch, Goldwasser, Kreuter, Reingold, Rothblum (arXiv:2507.07341)](sources/filter-impossibility-ai-alignment.md)** — *"On the Impossibility of Separating Intelligence from Judgment: The Computational Intractability of Filtering for AI Alignment"*. Three theorems (under Time-Lock Puzzles, OWF+secret-key, and PKE) establishing that no efficient prompt/output filter can align a sufficiently expressive LLM. The 2026-frontier analysis has been corrected.

**Phase 1 — 3 critical papers** (new complexity-theoretic notions):
1. [BGGKRR25 — Filter Impossibility for AI Alignment](sources/filter-impossibility-ai-alignment.md) — the anchor Pillar III impossibility.
2. [GSVV25 — Oblivious Defense in ML Models](sources/oblivious-defense-backdoor-removal.md) (STOC 2025) — Goldwasser-Shafer-Vafa-Vaikuntanathan; establishes defensibility ≠ detectability.
3. [CHLX25 — Backdoor Defense, Learnability, and Obfuscation](sources/backdoor-defense-learnability-obfuscation.md) (ITCS 2025) — Christiano et al.; introduces defendability as complexity-theoretic notion between learnability and iO.

**Phase 2 — 9 high-priority papers** (Pillar II/III LLM extensions + agentic):
4. [DGM+24 — Unelicitable Backdoors in LMs via Cryptographic Transformer Circuits](sources/unelicitable-backdoors-lms.md) (NeurIPS 2024).
5. [KKO+24 — Injecting Undetectable Backdoors in Obfuscated NNs and LMs](sources/io-undetectable-backdoors-nn.md) (NeurIPS 2024).
6. [CYDS26 — NAAT / Certified Semantic Smoothing for LLM Jailbreaks](sources/naat-certified-semantic-smoothing.md).
7. [LXS+25 — LeFCert for Foundation Models](sources/lefcert-foundation-models.md).
8. [HDDH25 — Randomized Smoothing for LLM Multi-Agent Systems](sources/rs-llm-multi-agent.md).
9. [ABIKN23 — Cryptography from Planted Graphs (log-size messages)](sources/cryptography-from-planted-graphs.md) (TCC 2023).
10. [FTH+25 — IMTM Origin / Prompt Injections to Protocol Exploits](sources/imtm-prompt-injections-protocols.md).
11. [DS+25 — CaMeL: Defeating Prompt Injections by Design](sources/camel-defeating-prompt-injections.md).
12. [ZYWGW25 — MELON: Provable IPI Defense](sources/melon-indirect-prompt-injection.md) (ICML 2025).

**Phase 3 — 8 medium-priority papers**:
13. [K+25 — Seven Security Challenges in Cross-Domain MAS](sources/seven-challenges-cross-domain-mas.md).
14. [NCM25 — Cryptographic Backdoor: Boon and Bane](sources/crypto-backdoor-boon-bane.md).
15. [RC24 — Jailbreak Paradox](sources/jailbreak-paradox.md).
16. [CGGV25 — Low-Degree Lower Bounds via Almost Orthonormal Bases](sources/low-degree-almost-orthonormal.md).
17. [EGV25 — Computational Lower Bounds in Latent Models](sources/lb-latent-models-clustering.md).
18. [SWKBC25 — RS Meets Vision-Language Models](sources/rs-meets-vlm.md).
19. [SLDLN25 — Adaptive Diffusion Denoised Smoothing (ADDS)](sources/adds-adaptive-diffusion-smoothing.md) (ICML 2025 Oral).
20. [LCMEBR25 — Multi-Level Certified Defense for Offline RL](sources/multi-level-certified-offline-rl.md) (ICLR 2025).

**New concept pages created**:
- [Defendability](concepts/defendability.md) — complexity-theoretic notion between PAC learnability and iO.
- [Indistinguishability Obfuscation (iO)](concepts/indistinguishability-obfuscation.md) — central cryptographic primitive.
- [Input Manipulation Threat Model (IMTM)](concepts/input-manipulation-threat-model.md) — formal prompt-injection model.

**New entity pages**:
- [Omer Reingold](entities/omer-reingold.md), [Paul Christiano](entities/paul-christiano.md), [Jonathan Shafer](entities/jonathan-shafer.md), [Neekon Vafa](entities/neekon-vafa.md).

**Corrected 2026-frontier analysis**: marked "Formal impossibility proof for LLM jailbreaks" as **Resolved** (was "Unmoved"). The actual remaining biggest gap is now: **UC-style composition theorem for multi-agent LLM security games**. CaMeL (DS+25) and MELON (ZYWGW25) give component-level guarantees; HDDH25 gives RS-for-consensus; Siu et al. give oracle-function vocabulary — but no one yet proves a composition theorem over ideal functionalities.

**Wiki state**:
- sources: 54 → **74** (+20)
- concepts: 44 → **47** (+3)
- entities: 64 → **68** (+4)
- raw/ PDFs: 52 → **72** (all new papers downloaded with [INITIALS][YY]_[Topic].pdf naming convention)
- Broken links: 0

---

## [2026-04-23] analysis | 2026 Research Frontier Web Research

**Page created**: `wiki/analyses/web-research-2026-frontier.md`

Digestion of all 52 raw/ PDFs confirmed complete (all have matching wiki source pages). With the corpus synchronized, conducted web research on what has been published 2024–2026 that extends the wiki's three pillars. Key findings:

- **Pillar III (agentic AI security)** — practical frameworks proliferate (MAESTRO 2025, OWASP Top 10 for Agentic Apps 2025, Microsoft Agent Governance Toolkit 2026, MAAIS framework 2026), but formal theory is still absent. The UC-composition-for-AI gap remains the single biggest open formal problem.
- **Pillar I (adversarial robustness)** — randomized smoothing has successfully scaled from classifiers to LLMs and VLMs in 2025-2026 (NAAT arXiv:2602.01587, LeFCert-L arXiv:2510.08659, RS-for-MAS arXiv:2507.04105, RS-meets-VLM arXiv:2509.16088).
- **Pillar III (undetectable backdoors)** — Goldwasser et al. 2022 auditing-impossibility now extends to LLMs: unelicitable backdoors via cryptographic transformer circuits (arXiv:2406.02619) and iO-based undetectable LM backdoors (arXiv:2406.05660).
- **Pillar II (stat-comp gaps)** — GHJS25 STOC 2025 decisively closed the PKE-from-standard-PC question; no breaking new results post-GHJS25 announced.
- **Formal impossibility for LLM jailbreaks** remains formally unproved despite empirical consensus that prevention is impossible.

**Priority candidate ingests identified** (for a next digestion batch): 6 arXiv papers + 1 IACR eprint covering the 2024-2026 agentic / LLM-certified-robustness / LLM-backdoor extensions. Full list in the analysis page.

**Structural recommendations**: add Part III.d to the reading pathway for "LLM-Extensions of Classifier Theorems"; create concept pages for Input Manipulation Threat Model and Indistinguishability Obfuscation; update rlhf-formal-model with accumulated evidence of RLHF fragility.

---

## [2026-04-23] lint | Corpus-wide integrity pass

**State before lint**: 25 broken links, 11 orphan pages, 10 only-aux-referenced pages.
**State after lint**: 0 broken links, 0 orphans, 1 only-aux (the new reading-pathway analysis, which is a terminal synthesis page — linked from `index.md` only, expected).

**Fixes applied**:
- **Created 13 missing entity pages** referenced by source papers but absent: `tselil-schramm`, `ilias-zadik`, `afonso-bandeira`, `samuel-hopkins`, `aukosh-jagannath`, `david-gamarnik`, `boaz-barak`, `pravesh-kothari`, `ankur-moitra`, `joan-bruna`, `david-steurer`, `jerry-li`, `oded-regev`.
- **Created 4 missing concept pages**: `pac-learning`, `computational-indistinguishability`, `pseudorandomness`, `verifiable-computation`. These were referenced from multiple sources but had no page.
- **Added author entity-links** to the 4 Mahloujifar-cluster source pages (were using plain-text author names in YAML but no markdown entity links in body).
- **Added author entity-links** to `adversarial-examples-computational-constraints` (Bubeck/Price/Razenshteyn) and `adversarial-vulnerability-any-classifier` (the Fawzi trio), fixing 6 orphans in one stroke.
- **Linked `sources/lean-rademacher-formalization.md`** to `concepts/lean-formalized-learning.md` (was an orphan concept).

**Findings not actionable in this pass** (flagged for follow-up):
- The earlier session (2026-04-12) performed ~26 deep ingests that were not logged. Source pages in `wiki/sources/` are mostly 40–85 lines of real content, not scaffolds. Effectively the corpus has ~37 deep-ingested sources, not the 11 recorded in earlier log entries. Index has been updated to reflect "15 deep ingests" (the 11 logged + 4 Mahloujifar-cluster ingested today); a thorough audit could elevate more.
- Two entity pages remain without a clear host source paper (`entities/yin-tat-lee`, `entities/dinesh-manocha`). Yin-Tat Lee corresponds to the Bubeck-Lee-Price-Razenshteyn follow-up paper not yet ingested (arXiv:1903.02334 or similar PRG-security strengthening). Dinesh Manocha is on the Immune paper author list; `sources/immune-rlhf-jailbreak-defense.md` does link to him so the lint script's earlier false flag was due to a same-directory-link regex bug that was subsequently fixed.
- Content-level contradictions: one was found and corrected during the Mahloujifar-cluster ingest — the (k, p)-poisoning bound was stated in additive form (Ω(kp/m)) throughout when the actual paper proves multiplicative μ → μ^{1−pk/m}. Corrected in `sources/multi-party-poisoning.md`, `concepts/k-p-poisoning-model.md`, `concepts/poisoning-attacks.md`.
- No suspected missing concept pages identified beyond those created; the core vocabulary is complete.

---

## [2026-05-07] ingest | Lower Bounds for Adversarially Robust PAC Learning (DMM19)

**Source**: `raw/DMM19_LowerBoundsRobustPAC.pdf` (downloaded from arXiv:1906.05815 during reading session — paper was referenced in M19 research statement but missing from corpus)

**Page created**: `wiki/sources/lower-bounds-robust-pac-learning.md`

**Key content captured**:
- Definitional distinction between error-region adversarial risk (this paper) and corrupted-input risk (all prior work) — the exponential separation depends entirely on this distinction
- Theorem 3.4: two conditions (Normal Lévy family + α-close concept class) sufficient for exponential sample complexity lower bound under sublinear perturbations
- Lemma 3.5: quantitative form — budget b = ρ·n forces m ≥ 2^{Ω(ρ²·n)}
- Hybrid attack impossibility: poisoner removing 1/n^{10} fraction + evasion budget Õ(√n) renders PAC learning impossible regardless of sample complexity
- Proof chain: small m → indistinguishable concepts (α-close) → non-negligible error → high AdvRisk (via Lemma 3.2 from MDM19)

**Index updated**: Sources count 15 → 16.
