# Venue mining, run 2026-08-22

Recovers venues for the wiki pages marked `venue-unconfirmed`, by reading how the
other papers in this corpus cite them. No web access. Produced by
`tools/mine-venues.py`. **Nothing here is written back to the wiki automatically.**
Each row needs a human to accept it, and the evidence column is there to make that
a two-second decision.

| | count |
| --- | --- |
| Unconfirmed venues mined | 103 |
| Two or more citers agree | 14 |
| One citer only | 8 |
| No citer in the corpus | 81 |

## Agreed, two or more independent citing papers

| Wiki page | Year | Venue | Votes | Evidence |
| --- | --- | --- | --- | --- |
| `adversarial-examples-computational-constraints` | 2019 | **arXiv preprint** | 8 | [DMM19_LowerBoundsRobustPAC] om generators. arXiv preprint arXiv:1811.06418, 2018a. Bubeck, S.,  |
| `bandeira-franz-parisi-criterion` | 2022 | **Neural Information Processing Systems** | 6 | [CV+25_AlmostOrthonormal] eira, Ahmed El Alaoui, Samuel Hopkins, Tselil Schramm, Alexander S Wei |
| `capacity-bounded-dp` | 2019 | **Neural Information Processing Systems** | 3 | [DM22_KernelQuantumRenyiAudit] . In Advances in Neural Information Processing Systems, volume 32 |
| `certified-defenses-data-poisoning` | 2017 | **Neural Information Processing Systems** | 3 | [BBHS22_RobustlyReliableLearners] . Advances in Neural Information Processing Systems, 30, 2017. |
| `dinur-nissim-revealing-information` | 2003 | **PODS** | 7 | [BCH22_ReconstructingInformedAdversaries] ,” in ACM Symposium on Principles of Database Systems  |
| `explaining-neural-scaling-laws` | 2024 | **arXiv preprint** | 2 | [BAP24_DynamicalScalingLaws] . arXiv preprint arXiv:2102.06701, 2021. Acknowledgements Bodin, A. |
| `fine-grained-cryptography` | 2016 | **CRYPTO** | 7 | [ACMS23_FineGrainedNIKE] . Traditional cryptography requires hardness of cryptographic primitive |
| `generative-leap-multi-index` | 2025 | **arXiv preprint** | 2 | [DKLM26_NoiseSensitivityExponent] g Theory, pages 1262–1262. PMLR, 2024. A. Damian, J. D. Lee, a |
| `membership-inference-shokri` | 2017 | **arXiv preprint** | 3 | [CCNSTT22_MIAFirstPrinciples] . arXiv preprint arXiv:1610.05820, 2016. [61] Liwei Song and Prate |
| `robust-generalization-more-data` | 2018 | **arXiv preprint** | 6 | [CBM18_PACEvasionAdversaries] . arXiv preprint arXiv:1804.11285, 2018. 11 [66] Uri Shaham, James |
| `scaling-laws-neural-lm` | 2020 | **arXiv preprint** | 9 | [BAP24_DynamicalScalingLaws] . arXiv preprint arXiv:2001.08361, 2020. d’Ascoli, S., Refinetti, M |
| `sgd-reuse-info-theoretic-limit` | 2024 | **Neural Information Processing Systems** | 6 | [ADKPS24_RepetitaIuvant] near the information-theoretic limit. In Thirty-eighth Annual Conferenc |
| `towards-separating-cdp` | 2023 | **FOCS** | 3 | [C+25_DataReconstructionSeeIt] ,” in 2023 IEEE 64th Annual Symposium on Foundations of Computer  |
| `undetectable-watermarks-lm` | 2023 | **arXiv preprint** | 2 | [KKO+24_iOBackdoorsNN] . arXiv preprint arXiv:2306.09194, 2023. [CHN` 23] Nicolas Carlini, Jamie |

## One citer only, treat as a lead

| Wiki page | Year | Candidate | Evidence |
| --- | --- | --- | --- |
| `adversarial-spheres` | 2018 | arXiv preprint | [PSV23_ConcentrationAvoidable] examples. arXiv preprint arXiv:1801.02774, 2018. [22] Chuan Guo,  |
| `chinchilla-replication` | 2024 | ICLR | [PPXP24_FourPlusThreePhases] . arXiv preprint arXiv:2404.10102, 2024. [8] Blake Bordelon and Cen |
| `crypto-backdoor-boon-bane` | 2025 | CRYPTO | [NCM25_CryptoBackdoorBoonBane] d Bane arXiv:2509.20714v1 [cs.CR] 25 Sep 2025 Anh Tu Ngo, Anupam  |
| `distribution-inference-risks` | 2022 | USENIX Security | [DSM+24_DoMIAsWorkLLMs] . In Privacy Enhancing Technologies Symposium, 2022. Xinyu Tang, Saeed M |
| `dp-adaptive-analysis-bounded-space` | 2023 | CRYPTO | [DSWZ23_DPAdaptiveBoundedSpace] Bounded Space Itai Dinur∗ Uri Stemmer† David P. Woodruff‡ Samson |
| `forgeability-and-unlearning` | 2023 | arXiv preprint | [S+25_DataForgingAttacks] arXiv preprint arXiv:2303.03648, 2023. [26] Mohamed Suliman, Swanand K |
| `single-index-harmonic-decomposition` | 2025 | Neural Information Processing Systems | [KJWSM26_FullBatchGDvsSGD] . In Advances in Neural Information Processing Systems, 2025. Filip K |
| `song-cryptographic-hardness-score-estimation` | 2024 | Neural Information Processing Systems | [W25_LowDegreeSurvey] . In Conference on Neural Information Processing Systems, 2024. [SS24] Jus |

## No citing paper in this corpus

These need an external lookup. 81 pages.

- `adaptive-vs-oblivious-streaming` (2021)
- `adversarially-robust-pac-regression` (2023)
- `adversary-aware-dp-bounds` (2026)
- `algorithmic-progress-lm` (2024)
- `attaxonomy` (2024)
- `authentication-bounded-storage` (2022)
- `average-case-fine-grained-hardness` (2017)
- `average-case-parity-problems` (2025)
- `backdoor-defense-learnability-obfuscation` (2025)
- `beyond-labeling-oracles` (2024)
- `bogdanov-low-degree-planted-subgraph` (2024)
- `bounded-storage-simple-schemes` (2019)
- `catch-a-chinchilla-compute-monitoring` (2023)
- `cdp-inner-product-implies-ot` (2025)
- `cdp-wider-parameter-regimes` (2025)
- `certificates-statistical-algorithms` (2026)
- `certified-robustness-differential-privacy` (2019)
- `chinchilla-compute-optimal` (2022)
- `cohen-data-reconstruction` (2024)
- `computational-concentration-of-measure-etesami` (2020)
- `compute-optimal-phases` (2024)
- `covert-learning` (2021)
- `critical-evaluation-backdoor-countermeasures` (2022)
- `difficulty-of-mia` (2021)
- `dp-against-timing-attacks` (2024)
- `evaluating-nn-backdoor-defenses` (2020)
- `fine-grained-erm` (2017)
- `fine-grained-gradient-llm` (2024)
- `fine-grained-nike-lower-bounds` (2023)
- `fine-grained-nike-revisited` (2024)
- `formalizing-llm-agent-security` (2026)
- `full-batch-gd-vs-one-pass-sgd` (2026)
- `generative-exponent-single-index` (2024)
- `haghifam-sample-complexity-mia` (2025)
- `hardness-one-hidden-layer` (2024)
- `hardness-single-periodic-neurons` (2021)
- `hidden-progress-sgd-parities` (2022)
- `impossibility-retrain-equivalence` (2025)
- `imtm-prompt-injections-protocols` (2025)
- `information-exponent-online-sgd` (2021)
- `io-undetectable-backdoors-nn` (2024)
- `kaplan-bayesian-memorization-reconstruction` (2025)
- `kernel-quantum-renyi-audit` (2022)
- `language-model-preserve-privacy` (2022)
- `leap-complexity-sgd` (2023)
- `learnability-deep-random-networks` (2019)
- `learning-rate-induces-generative-exponent` (2025)
- `merged-staircase-property` (2022)
- `mia-cannot-prove-training` (2025)
- `noise-sensitivity-exponent` (2026)
- `oblivious-defense-backdoor-removal` (2025)
- `overparameterization-computational-constraints` (2022)
- `pac-learning-evasion-adversaries` (2018)
- `permissionless-consensus-fine-grained` (2024)
- `planted-orthogonal-vectors` (2025)
- `pol-incentive-security` (2026)
- `pol-more-broken` (2023)
- `polo-proof-of-learning-ownership` (2026)
- `preventing-false-discovery-hard` (2014)
- `query-complexity-reconstruction` (2024)
- `raz-parity-time-space` (2016)
- `repetita-iuvant-data-repetition` (2024)
- `reusing-batches-breaks-exponents` (2024)
- `robust-estimators-high-dimensions` (2016)
- `robust-multi-index-sq-bounds` (2025)
- `robust-pac-learning-characterization` (2022)
- `robust-single-index-efficient` (2024)
- `robustly-reliable-learners-poison` (2022)
- `robustness-at-odds-accuracy` (2019)
- `separating-cdp-client-server` (2016)
- `sgd-xor-near-optimal` (2024)
- `sok-adversary-knowledge` (2024)
- `sok-backdoor-defense-evaluation` (2025)
- `sok-black-box-attack-pitfalls` (2024)
- `sok-data-reconstruction-attacks` (2025)
- `speak-much-remember-little` (2021)
- `suliman-data-forging-attacks` (2025)
- `tolerant-robust-pac-learning` (2025)
- `transformers-sparse-xor-polylog` (2025)
- `two-party-dp-complexity` (2022)
- `universal-law-of-robustness` (2021)

## 2026-09-03, web check of the load-bearing tier-3 citations

| Key | Resolved to | Evidence |
| --- | --- | --- |
| WLBZ25 | USENIX Security 2025 | usenix.org/conference/usenixsecurity25/presentation/wen |
| ZDKT25 | IEEE SaTML 2025 | ieeexplore.ieee.org/document/10992516 |
| FK24 | still a preprint, arXiv:2402.14937 | no refereed venue found |
| SSEP24 | TMLR 2024 | dblp record Trans. Mach. Learn. Res. 2024, confirmed after the first search missed it |

The introduction called all three systematizations preprints and Section 2 called
Zhang et al. unrefereed. Both sentences corrected the same day. Journal entries are
still emitted as inproceedings by gen-bib.py, and the checklist wants article.
