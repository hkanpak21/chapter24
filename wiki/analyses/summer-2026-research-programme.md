---
title: Summer 2026 Research & Reading Programme — Toward a Computationally Bounded Theory of Learning
type: analysis
date: 2026-06-22
tags: [reading-guide, programme, chapter-24, formal-security, complexity-theory, planning, schedule]
---

## Question / Motivation

Mursit is building **Chapter 24** of Arora–Barak ([../../output/chapter_24.md] — the lödeg↔nannosh dialogue):
a **learning system is a first-class abstract machine**. One universal machine `U`: a **source** `Π`
(a `U`-program on a uniform seed), a **learner** `L` that synthesizes an advice string `w` from
membrane-bounded access to `Π`, and inference `M_w = U(w,·)` for `t_eval` steps. "Model" = time-bounded
universal computation; linear-regression → LLM is one `U`-program at two `(|w|, t_eval)` coordinates.
**Accuracy and security are theorems about that one object**, and an attack is a **capability vector `κ`**
over the machine's tapes — not a per-attack taxonomy.

**North star (Mursit's framing):** *the "Goldwasser theorem of AI"* — port security's historical
transition **from Shannon's information-theoretic security to reduction-based cryptography** into AI:
take today's **statistical** AI to a **computationally bounded and understood** AI. Read learning
*computationally* (reductions, classes, one-wayness), not *statistically* (sample complexity,
concentration). The dialogue has already reached the slogan **"security *is* learning lower bounds"**
(the τ-staircase) and one proved **keystone** (the min-`Kt(w)` learner is universal *and* generalizing).

**This page is the dated June 22 → September 30 calendar** that interleaves the Arora–Barak textbook
(Mursit is at **§2.3 Cook–Levin**) with the paper corpus and drives toward the Chapter 24 deliverables.

### Design decisions settled in the June 2026 brainstorming (the objective this schedule serves)

- **Spine = primary.** Mursit's own thesis leads; Durak's agentic/verification agenda is a **September
  coda**, not a parallel track. (The dialogue's Phase 3 already unifies the two — see below.)
- **Adversary = all PPT first**, the **learning-shaped (SQ/low-degree) adversary** as a Phase-2 extension.
- **Engine = crypto reductions used as *measuring instruments* (concrete/exact security)** — "breaking X
  in time `t`, advantage `ε` ⟹ solving reference problem in `t'≈t`, `ε'≈ε`." *Measurable, not merely
  asymptotic.*
- **Anchor game = `COMP-MEM`** (Computational Membership Indistinguishability) — the *floor* of the
  `COMP-TW` (Computational Training-World Indistinguishability) schema, where two training-worlds differ by
  a controlled `Δ` (one example → MI; backdoor insertion → backdoor-detection; poisoned batch → poisoning).
  `COMP-MEM` is the **privacy corner of the dialogue's `Risk*` functional** and the **bottom rung of the
  τ-staircase**. Pillar discipline: it is the *necessary floor* of confidentiality, **not** a master-key —
  integrity (evasion/correctness) needs a separate `EUF-CMA`-analogue generator (Phase 2).
- **Adversary calibration:** `κ = (O observation-map, T timeline-phase, B budget, mode passive/chosen)`,
  folded into the adversary. The dataset is the **secret**, so the baseline `κ₀` is *prior/public knowledge*
  (distribution, architecture, "model card") **not** the realized training set; security is the **marginal
  advantage** `Adv(κ) − Adv(κ₀)` — what the *trained model* leaks beyond the prior. Build on the simplest
  lattice point first: `κ_inf` (black-box, inference-only, passive), then climb.
- **Crown jewel = a reduction at a threshold:** *past a certain point, learning reduces to breaking a OWF.*
  Not an identity; a **regime change**. Lineage: Kearns–Valiant 1994 → BFKL 1993 → DNV19 Win-Win → HN23
  Pessiland.
- **Bridge to deep learning = average-case PAC over structured-but-natural distributions** = the
  **planted-models / stat-comp-gap** corpus (Brennan–Bresler, SQ, low-degree). This is *load-bearing*, not
  background: it is the interpolant between abstract PAC-hardness and deep learning.
- **Pacing = moderate (~10–12 hrs/wk):** ~1 AB chapter per 1–2 weeks + **1–2 deep reads/week**; everything
  else is **[map]** (skim for the idea) or **[shelf]** (pull on demand). Papers are tagged accordingly.

> The depth-order *within* a cluster lives in [reading-pathway-formal-security](reading-pathway-formal-security.md).
> This page is the *when*, tied to the textbook and the chapter deliverables.

---

## The dated calendar (14 weeks)

Arc: **reductions → non-uniformity/randomness → one-wayness/average-case → interactive proofs/verification.**

### Phase A — Reductions & the object defined · **W1–W2 (Jun 22 – Jul 5)**

- **Arora–Barak:** *finish* **Ch. 2** (NP-completeness; the full theory of reductions — the grammar the
  whole thesis speaks); *skim* **Ch. 3** (diagonalization).
- **[DEEP]** [M19 — Mahloujifar 2019 research statement](../sources/complexity-theoretic-adversarial-ml.md)
  — re-read *to formalize* the taxonomy critique, not to learn it.
- **[DEEP] Kearns–Valiant 1994**, *Cryptographic Limitations on Learning Boolean Formulae & Finite Automata*
  — *(external, acquire)* the founding theorem "learning ≤ breaking RSA/factoring/DLOG"; the prototype of
  the crown jewel.
- **[map]** [FGRVX17 — SQ lower bound for planted clique](../sources/feldman-statistical-algorithms-planted-clique.md)
  (SQ = the `κ_in` access mode); **Kearns–Vazirani** PAC textbook *(external, reference backbone)*;
  [CK21 — Covert Learning](../sources/covert-learning.md).
- **[map] privacy incumbent** (what `COMP-MEM` computational-izes): [ACG+16 — DP-SGD](../sources/deep-learning-differential-privacy.md),
  [LAGHJ19 — PixelDP](../sources/certified-robustness-differential-privacy.md). DP = the *Shannon-style, IT*
  membership bound; `COMP-MEM` is its computational analogue.
- **Deliverable:** formal `κ` + the `COMP-MEM` / `COMP-TW` game definitions, with `κ₀` baseline and the
  marginal-advantage `Adv(κ)−Adv(κ₀)`. Append as a dialogue turn.

### Phase B — Non-uniformity, randomness, the computational adversary · **W3–W6 (Jul 6 – Aug 2)**

- **W3 — AB Ch. 6 (circuits / P/poly; advice = capacity = `|w|`).**
  **[DEEP]** [BPR19 — Adversarial Examples from Computational Constraints](../sources/adversarial-examples-computational-constraints.md).
  **[map]** [BLPR19 — from cryptographic PRGs](../sources/adversarial-examples-prg.md),
  [GMF+18 Adversarial Spheres](../sources/adversarial-spheres.md),
  [FFF18 Adversarial Vulnerability](../sources/adversarial-vulnerability-any-classifier.md).
- **W4 — AB Ch. 7 (BPP; BPP ⊆ P/poly).**
  **[DEEP]** [DNV19 — Win-Win](../sources/win-win-robust-learning.md): hardness of robust classification ⇔
  OWF exist (the bridge-direction template). **[map]** [GJMM20](../sources/computational-hardness-robust-learning.md).
- **W5 — AB Ch. 9 begins (OWF / PRG).**
  **[DEEP] BFKL 1993**, *Cryptographic Primitives from Hard Learning Problems* *(external, acquire)* — the
  reverse bridge (OWF *out of* hard learning; ancestor of LWE). **[map]** [BW08 — PKC from different
  assumptions](../sources/pkc-from-different-assumptions.md).
- **W6 — concrete security + the IT-robustness incumbent.**
  **[DEEP]** [BS21 — Universal Law of Robustness via Isoperimetry](../sources/universal-law-of-robustness.md)
  (the capacity/overparameterization axis — `|w|` as attack surface).
  **[map]** [MDM19 Curse of Concentration](../sources/curse-of-concentration.md),
  [EMM20 Computational Concentration](../sources/computational-concentration-of-measure-etesami.md),
  [MZME19 Empirically Measuring Concentration](../sources/empirically-measuring-concentration.md),
  **Bellare–Rogaway concrete-security notes** *(external)*.
  **Deliverable:** the **"learning adversary"** definition + a **concrete-security reduction template**
  (attack-resource ↦ reference-problem-resource).

### Phase C — One-wayness, average-case & the gap engine; the backdoor games · **W7–W10 (Aug 3 – Aug 30)**

- **W7 — AB Ch. 9 finishes (OWF).**
  **[DEEP]** [GKVZ22 — Undetectable Backdoors](../sources/planting-undetectable-backdoors.md): the crisp
  crypto↔ML reduction — a `COMP-TW` instance with `Δ = insertion`. **[map]**
  [KKO+24 iO backdoors](../sources/io-undetectable-backdoors-nn.md),
  [NCM25 crypto backdoor boon/bane](../sources/crypto-backdoor-boon-bane.md).
- **W8 — AB Ch. 18 (Levin average-case; `Π`-as-program is an average-case object).**
  **[DEEP]** [CHLX25 — Defendability](../sources/backdoor-defense-learnability-obfuscation.md) (already
  game-framed; closest existing object to `COMP-TW`). **[map]**
  [DGM+24 unelicitable backdoors](../sources/unelicitable-backdoors-lms.md),
  [GSVV25 oblivious defense](../sources/oblivious-defense-backdoor-removal.md).
- **W9 — AB Ch. 19 (hardness amplification, hardcore lemma).**
  **[DEEP]** [BB20 — Reducibility & Stat-Comp Gaps from Secret Leakage](../sources/reducibility-statistical-computational-gaps.md)
  (intro + Part II — the bridge-to-deep-learning engine). **[map]**
  [BBHLS21 SQ≈low-degree](../sources/brennan-sq-lowdegree-equivalence.md),
  [W25 low-degree survey](../sources/low-degree-polynomials-survey.md),
  [HS24 PC conjectures equivalent](../sources/hirahara-planted-clique-conjectures-equivalent.md).
- **W10 — gap-engine consolidation + planted→deep bridge.**
  **[DEEP]** [BRST21 — Continuous LWE](../sources/bruna-continuous-lwe.md) (planted structure ↔ lattice
  crypto — the interpolant). **[shelf — pull as the reduction needs]** the rest of the stat-comp-gap corpus:
  [BHKKMP19 SOS-LB](../sources/barak-sos-lower-bound-planted-clique.md),
  [BEHSWZ22 Franz–Parisi](../sources/bandeira-franz-parisi-criterion.md),
  [SW22 low-degree estimation](../sources/low-degree-estimation-schramm-wein.md),
  [HW21 counterexamples-LD](../sources/holmgren-counterexamples-low-degree.md),
  [CV+25 almost-orthonormal](../sources/low-degree-almost-orthonormal.md),
  [DHSS25 low-degree SBM](../sources/ding-low-degree-community-detection.md),
  [BJ23 detection-recovery gaps](../sources/detection-recovery-refutation-gaps.md),
  [LM25 latent-models LB](../sources/lb-latent-models-clustering.md),
  [DKKLMS16 robust estimators](../sources/robust-estimators-high-dimensions.md),
  [ZSWB22 lattice surpass SOS](../sources/zadik-lattice-surpass-sos.md),
  [GHJS25 PKE from PC](../sources/pke-from-planted-clique.md),
  [ABIKN23 crypto from planted graphs](../sources/cryptography-from-planted-graphs.md),
  GJW21/GJW22 circuit-LBs ([1](../sources/gamarnik-hardness-random-optimization-circuits.md),
  [2](../sources/gamarnik-circuit-lower-bounds-pspin.md)).
  **Deliverable:** instantiate `COMP-MEM` fully in the machine model; prove **one** reduction
  `COMP-MEM → reference problem` (planted-clique or cLWE). This is the dialogue's `Risk*` privacy-corner /
  τ_stat rung, made concrete.

### Phase D — Interactive proofs, verification, synthesis & the Durak coda · **W11–W14 (Aug 31 – Sep 30)**

- **W11 — AB Ch. 8 (interactive proofs; IP = PSPACE, MIP, ZK).**
  **[DEEP]** [HN23 — Learning in Pessiland](../sources/learning-in-pessiland.md) (the threshold/world reading
  — *the crown-jewel regime*). **[map] Neural Interactive Proofs** (Hammond–Adam-Day, ICLR'25, arXiv
  2412.08897) — the IP/delegation side-track; now it fits, as the integrity/verifiable-delegation example.
  *(Candidate ingest.)*
- **W12 — hardness-of-alignment in our idiom.**
  **[DEEP]** [BGGKRR25 — Impossibility of Filtering for Alignment](../sources/filter-impossibility-ai-alignment.md)
  (Goldwasser et al.; a hardness theorem in the target idiom). **[map]**
  [BLW25 ZK pipelines](../sources/zk-verifiable-ai-pipelines.md),
  [SKMTO25 Lean Rademacher](../sources/lean-rademacher-formalization.md) (formalization/verification angle).
- **W13 — Durak coda, part 1 (integrate, using the dialogue's Phase-3 result).**
  **[DEEP]** [VDKMR26 — AIOracle](../sources/extending-formalism-cryptography-ai.md) (re-read) +
  `raw/AIOracles_for_Practitioners.html` (the Phase-3 source). The dialogue already proved AIOracle and
  Chapter-24 are **two layers of one theory** joined at `φ ↔ (T, r_judge)`; the coda makes that rigorous and
  printable. **[map]** [Siu et al. — formalizing LLM agent security](../sources/formalizing-llm-agent-security.md).
- **W14 — Durak coda, part 2 + synthesis.**
  **Deliverables:** (1) **native complexity class + the threshold-reduction draft** (learning → OWF at the
  certain point); (2) the **Durak critical coda** written; aim for the Chapter-24 `HUMAN consent` skeleton.

---

## Reference shelf — pull on demand, NOT scheduled deep reads

These are real parts of the corpus but **off the spine** (the spine is PPT crypto-reductions + the
gap-engine + the abstract-machine theory). At moderate pace they are read *if a deliverable needs them*,
not on a fixed week. Stated explicitly so nothing is silently dropped.

- **Robust-PAC characterization:** [MHS19](../sources/vc-classes-adversarially-robustly-learnable.md),
  [MHS22](../sources/robust-pac-learning-characterization.md),
  [AH23](../sources/adversarially-robust-pac-regression.md),
  [CBM18](../sources/pac-learning-evasion-adversaries.md),
  [BBHS22](../sources/robustly-reliable-learners-poison.md),
  [tolerant robust PAC](../sources/tolerant-robust-pac-learning.md), `S25_PACLearningSurvey` *(title unverified)*.
  *(Relevant when OP1 — the robust comp-stat gap — is engaged; MHS19's Montasser dimension is its statistical value.)*
- **Certified defenses (practical):** [CRK19 randomized smoothing](../sources/certified-robustness-randomized-smoothing.md),
  [SYL+19 SmoothAdv](../sources/provably-robust-smoothadv.md), [WK18 convex polytope](../sources/provable-defenses-convex-polytope.md),
  [SKL17 certified poisoning](../sources/certified-defenses-data-poisoning.md),
  [TSETM19](../sources/robustness-at-odds-accuracy.md), [SSTTM18](../sources/robust-generalization-more-data.md).
- **Applied LLM / agentic security (the Durak-coda evidence base):**
  [DS+25 CaMeL](../sources/camel-defeating-prompt-injections.md), [ZYWGW25 MELON](../sources/melon-indirect-prompt-injection.md),
  [FTH+25 IMTM](../sources/imtm-prompt-injections-protocols.md), [K+25 Seven Challenges](../sources/seven-challenges-cross-domain-mas.md),
  [C24 Jailbreak Paradox](../sources/jailbreak-paradox.md), [RT23 universal jailbreak RLHF](../sources/universal-jailbreak-rlhf-backdoors.md),
  [CQY+24 MaxMin-RLHF](../sources/maxmin-rlhf-impossibility.md), [GCS+24 Immune](../sources/immune-rlhf-jailbreak-defense.md),
  [HDDH25 RS-LLM-MAS](../sources/rs-llm-multi-agent.md), [SWKBC25 RS-VLM](../sources/rs-meets-vlm.md),
  [SLDLN25 ADDS](../sources/adds-adaptive-diffusion-smoothing.md), [NAAT26 semantic smoothing](../sources/naat-certified-semantic-smoothing.md),
  [LXS+25 LeFCert](../sources/lefcert-foundation-models.md), [L+25 certified offline RL](../sources/multi-level-certified-offline-rl.md),
  `20344_Statistically_Undetectab` *(title unverified)*.

## Implications for the Wiki

- **Candidate ingests this summer (not yet in corpus):** Kearns–Valiant 1994; Blum–Furst–Kearns–Lipton 1993;
  Kearns–Vazirani textbook; Bellare–Rogaway concrete-security notes; Neural Interactive Proofs (Hammond–Adam-Day);
  **and `raw/AIOracles_for_Practitioners.html`** — the dialogue's Phase-3 flagged it for ingestion as
  `wiki/sources/aioracles-for-practitioners.md` (cites Ball et al. 2025, Bellare–Kohno 2003, the GLM).
- **New concept pages to create when their definitions stabilize:** `comp-mem-game`, `comp-tw-schema`,
  `capability-vector-kappa`, `learning-adversary`, `kt-on-u`, `the-membrane`, `tau-staircase`,
  `keystone-universal-generalizing`. They currently exist only as prose in [../../output/chapter_24.md].
- Each Phase deliverable is a dialogue turn appended to [../../output/chapter_24.md]; the Durak coda (W13–14)
  is a future analysis page.
- Confirm the two unverified raw titles (`S25_PACLearningSurvey`, `20344_Statistically_Undetectab`) — see
  [../../raw/SOURCES.md].

## References

- [../../output/chapter_24.md] — the lödeg↔nannosh dialogue (the theory this programme serves; 3 phases,
  Phase-2 verdict = "organizing theory," Phase-3 = AIOracle unification).
- [../../output/ideas.md] — Mursit's critique of Mahloujifar & Durak motivating the `κ`-game.
- [intro-computational-security-of-learning](../../output/intro-computational-security-of-learning.md) —
  the blog-style field introduction (companion to this schedule).
- [reading-pathway-formal-security](reading-pathway-formal-security.md) — depth order within each cluster.
