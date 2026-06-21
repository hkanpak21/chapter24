---
title: Reading Pathway for the Formal-Security Corpus
type: analysis
date: 2026-04-23
tags: [reading-guide, pedagogy, synthesis, formal-security]
---

## Question / Motivation

The `raw/` folder holds 45 papers spanning three research programs (adversarial robustness via concentration, statistical-computational gaps via average-case reductions, cryptographic security for AI) plus cross-cutting defense and verification work. Read in arbitrary order the corpus is overwhelming; read in the right order each paper sets up the next. This analysis gives a recommended reading pathway, clustered by program and ordered by prerequisite structure.

## Findings

### The three-pillar structure

The corpus organizes around three intersecting research programs. Most papers fit cleanly in one pillar; a minority (e.g., the Mahloujifar-Mahmoody "computational concentration" line, the Goldwasser et al. backdoor paper) bridge two.

- **Pillar I — Adversarial robustness from concentration and complexity**: inherent impossibilities, PAC characterization, hardness reductions, certified defenses.
- **Pillar II — Statistical-computational gaps from average-case reductions**: planted-clique framework, low-degree/SOS/SQ frameworks, cryptographic use of planted problems.
- **Pillar III — Formal AI security models**: cryptographic games for AI (AIOracle), undetectable backdoors, covert learning, RLHF impossibility, verification.

### Recommended pathway

For each pillar, read the foundational paper first, then build outward. Don't try to read a pillar end-to-end before moving on — the pillars illuminate each other, and you want the whole shape in your head before sinking into any one line.

#### Phase 0 — Orientation (read in order, ~1 week)

1. **[Mahloujifar 2019 — Complexity-Theoretic Approach to Adversarial ML](../sources/complexity-theoretic-adversarial-ml.md)** — research statement/PhD summary. Skim to get the taxonomy; you'll return to component papers later.
2. **[Brennan & Bresler 2020 — Reducibility and Statistical-Computational Gaps](../sources/reducibility-statistical-computational-gaps.md)** — read the intro and summary of results (pp. 1–20) only; the full 175-page paper is for reference.
3. **[Villa et al. 2026 — Extending Formalism of Cryptography to AI](../sources/extending-formalism-cryptography-ai.md)** — read fully; defines the frontier and motivates the other work.

After Phase 0 you have the three-pillar map. Now descend.

#### Phase I — Adversarial robustness (read roughly in order)

**I.a — Concentration-of-measure foundations (prerequisite for everything else in this pillar)**:

1. [Fawzi, Fawzi, Fawzi 2018 — Adversarial Vulnerability for Any Classifier](../sources/adversarial-vulnerability-any-classifier.md) — Gaussian-isoperimetry case; easiest entry to the geometric argument.
2. **[Mahloujifar, Diochnos, Mahmoody 2019 — Curse of Concentration](../sources/curse-of-concentration.md)** — the unification. Once you grasp this, the sphere/Gaussian/hypercube special cases fall out.
3. **[Mahloujifar, Zhang, Mahmoody, Evans 2019 — Empirically Measuring Concentration](../sources/empirically-measuring-concentration.md)** — asks whether the theoretical bound binds in practice. The answer reshapes priors for every subsequent paper.
4. **[Etesami, Mahloujifar, Mahmoody 2020 — Computational Concentration of Measure](../sources/computational-concentration-of-measure-etesami.md)** — makes the attacks algorithmic. The algorithmic-reduction framework is reusable.

**I.b — Poisoning attacks**:

5. **[Mahloujifar, Mahmoody, Mohammed 2019 — Universal Multi-Party Poisoning](../sources/multi-party-poisoning.md)** — (k,p) model; generalizes p-tampering with correlation.
6. [Steinhardt, Koh, Liang 2017 — Certified Defenses for Data Poisoning](../sources/) — the first matching-upper-bounds-and-attacks certified defense.
7. [Diakonikolas, Kamath, Kane, Li, Moitra, Stewart 2016 — Robust Estimators in High Dimensions](../sources/) — optimal-rate robust mean/covariance, algorithmic.
8. [Balcan, Blum, Hanneke, Sharma 2022 — Robustly-Reliable Learners](../sources/robustly-reliable-learners-poison.md) — instance-targeted certified guarantees.

**I.c — PAC characterization of robust learning**:

9. [Cullina, Bhagoji, Mittal 2018 — PAC-Learning in the Presence of Evasion Adversaries](../sources/pac-learning-evasion-adversaries.md) — adversarial VC dimension.
10. [Montasser, Hanneke, Srebro 2019 (COLT) — VC Classes Are Robustly Learnable but Only Improperly](../sources/vc-classes-adversarially-robustly-learnable.md) — the proper vs. improper separation.
11. **[Montasser, Hanneke, Srebro 2022 (NeurIPS) — Generic Minimax Optimal Learner](../sources/robust-pac-learning-characterization.md)** — the full characterization via global one-inclusion graph dimension.
12. [Ashtiani, Pathak, Urner 2025 — Tolerant Robust PAC Learning](../sources/tolerant-robust-pac-learning.md) — linear-in-VC-dim sample complexity under tolerance relaxation.
13. [Attias, Hanneke 2023 — Robust PAC Learnability for Regression](../sources/) — fat-shattering-dimension extension.

**I.d — Crypto-hardness angle (bridges to Pillar III)**:

14. [Bubeck, Price, Razenshteyn 2019 — Adversarial Examples from Computational Constraints](../sources/adversarial-examples-computational-constraints.md) — learning problems where IT-robust but computationally not.
15. **[Degwekar, Nakkiran, Vaikuntanathan 2019 — Win-Win Theorem](../sources/win-win-robust-learning.md)** — robust-learning hardness ⇔ OWF exists. Deepest structural result.
16. [Garg, Jha, Mahloujifar, Mahmoody 2020 — Computational Hardness for Robust Learning](../sources/computational-hardness-robust-learning.md) — positive side: PRF-based robust classifiers exceed IT robustness.
17. **[Bubeck, Sellke 2021 — Universal Law of Robustness via Isoperimetry](../sources/universal-law-of-robustness.md)** — why overparameterization is necessary; NeurIPS Outstanding Paper.

**I.e — Certified defenses**:

18. [Cohen, Rosenfeld, Kolter 2019 — Randomized Smoothing](../sources/) — the practical certified defense.
19. [Lecuyer et al. 2019 — PixelDP](../sources/) — the DP-to-certified-robustness connection.
20. [Salman et al. 2019 — SmoothAdv](../sources/) — adversarial training + smoothing.
21. [Wong, Kolter 2018 — Convex Outer Polytope](../sources/) — ℓ∞ certified defenses.
22. [Tsipras et al. 2019 — Robustness May Be at Odds with Accuracy](../sources/) — the tradeoff.

#### Phase II — Statistical-computational gaps

**II.a — Planted clique foundations**:

1. [Feldman, Grigorescu, Reyzin, Vempala, Xiao 2017 — SQ Lower Bound for Planted Clique](../sources/feldman-statistical-algorithms-planted-clique.md) — the SQ lower bound matching √n threshold.
2. [Barak, Hopkins, Kelner, Kothari, Moitra, Potechin 2019 — SOS Lower Bound for Planted Clique](../sources/barak-sos-lower-bound-planted-clique.md) — via pseudo-calibration.
3. **[Brennan & Bresler 2020 — Reducibility (full ingest)](../sources/reducibility-statistical-computational-gaps.md)** — the PC_ρ framework; now read Parts II–III.
4. **[Hirahara & Shimizu 2024 — Planted Clique Conjectures Are Equivalent](../sources/hirahara-planted-clique-conjectures-equivalent.md)** — the equivalence web among PC variants.

**II.b — Low-degree and SOS frameworks**:

5. **[Brennan, Bresler, Hopkins, Li, Schramm 2021 — SQ ≈ Low-Degree](../sources/brennan-sq-lowdegree-equivalence.md)** — the formal equivalence.
6. [Holmgren & Wein 2021 — Counterexamples to Low-Degree Conjecture](../sources/holmgren-counterexamples-low-degree.md) — why the conjecture needs refinement.
7. [Zadik, Song, Wein, Bruna 2022 — Lattice Methods Surpass SOS](../sources/zadik-lattice-surpass-sos.md) — the algebraic-structure counterexample.
8. [Bandeira et al. 2022 — Franz-Parisi Criterion](../sources/bandeira-franz-parisi-criterion.md) — physics-inspired justification.
9. [Gamarnik, Jagannath, Wein 2021/2022 — Circuit Lower Bounds for p-Spin](../sources/gamarnik-hardness-random-optimization-circuits.md) + [2022 p-spin follow-up](../sources/gamarnik-circuit-lower-bounds-pspin.md).
10. **[Wein 2025 — Low-Degree Polynomials Survey](../sources/low-degree-polynomials-survey.md)** — the synthesis; read last in this cluster to understand the landscape.

**II.c — Applications and extensions**:

11. [Bresler & Jiang 2023 — Detection-Recovery-Refutation Gaps](../sources/detection-recovery-refutation-gaps.md) — different computational tasks, different thresholds.
12. [Ding et al. 2025 — Low-Degree Conjecture in SBM](../sources/ding-low-degree-community-detection.md) — community detection below Kesten-Stigum.
13. [Bruna, Regev, Song, Tang 2021 — Continuous LWE](../sources/bruna-continuous-lwe.md) — bridge to lattice crypto; Pillar III connection.

#### Phase III — Formal AI security models

**III.a — Foundations from cryptography**:

1. [Canetti & Karchmer 2021 — Covert Learning](../sources/covert-learning.md) — the first formal crypto-style learning security definition with matching impossibility.
2. [Abadi et al. 2016 — DP-SGD](../sources/) — the most-deployed formal-privacy mechanism.

**III.b — AI-specific formal models**:

3. **[Villa et al. 2026 — AIOracle (full re-read)](../sources/extending-formalism-cryptography-ai.md)** — the comprehensive cryptographic framework for agentic AI.
4. [Siu, He, Montgomery, Song et al. 2026 — Formalizing LLM Agent Security](../sources/formalizing-llm-agent-security.md) — the Berkeley/Song group's complementary framework (operational authorization vs. game-based security).

**III.c — Fundamental impossibilities**:

5. **[Goldwasser, Kim, Vaikuntanathan, Zamir 2022 — Undetectable Backdoors](../sources/planting-undetectable-backdoors.md)** — the auditing-impossibility result. The Pillar III analogue of the win-win theorem.
6. [Immune 2024 — RLHF Jailbreak Impossibility](../sources/immune-rlhf-jailbreak-defense.md) — formal fragility of RLHF alignment.
7. [MaxMin-RLHF 2024 — Single-Reward RLHF Impossibility](../sources/maxmin-rlhf-impossibility.md) — preference-diversity impossibility.
8. [Rando & Tramèr 2023 — Universal Jailbreak Backdoors from Poisoned RLHF](../sources/) — connects Pillar III to poisoning (Pillar I).

**III.d — Verification**:

9. [Lean Rademacher 2025](../sources/lean-rademacher-formalization.md) — mechanized generalization bounds.
10. [ZK Proofs for ML Pipelines 2025](../sources/zk-verifiable-ai-pipelines.md) — cryptographic verifiability.

### Dependency graph summary

Entry points by background:

- **Cryptography background**: Phase 0 → Phase III.a → Phase III.b → Phase I.d → Phase III.c → Phase II.
- **Learning theory background**: Phase 0 → Phase I.a → Phase I.c → Phase I.b → Phase I.d → Phase II → Phase III.
- **Statistics / high-dimensional probability background**: Phase 0 → Phase II.a → Phase II.b → Phase I.a → Phase I.d → Phase III.
- **Adversarial-ML practitioner**: Phase 0 → Phase I.e → Phase I.a → Phase I.b → Phase I.d → Phase III.c → Phase II (optional).

### Time estimate

- Phase 0: ~1 week (skim Mahloujifar thesis; read Villa + Brennan-Bresler intros carefully).
- Phase I: ~4–6 weeks for full depth, ~2 weeks for key papers only.
- Phase II: ~4 weeks; density is high, many papers heavy on probability-theoretic proof.
- Phase III: ~2 weeks for formal papers; more if you want to verify mechanized proofs yourself.

## Implications for the Wiki

- The 4 Mahloujifar-cluster papers (ingested 2026-04-23) now fully cover the Phase I.a reading block. Phase I.b needs more depth (Steinhardt, Balcan, Diakonikolas are scaffolded but not deeply ingested); this is the natural next ingest batch.
- Phase II.a — Feldman 2017 and Barak 2019 are in `raw/` but only scaffolded. The lowest-cost next step for the statistical-computational pillar is deep-ingesting these two and then Hirahara-Shimizu.
- Phase III.b and III.c are mostly deeply ingested already; III.a and III.d need work.
- A corpus-wide lint pass is overdue: many source pages in `wiki/sources/` are scaffolding from an earlier session without full CLAUDE.md-spec ingests. The next lint should reconcile the log with the sources folder and flag which pages need real ingests.

## References

- [Mahloujifar cluster ingests, 2026-04-23](../log.md) — log entries for the four Phase I.a papers.
- [Deep Research Prompt (Formalizing AI Security)](deep-research-prompt-formalizing-ai-security.md) — complementary structured-question view of the same corpus.
