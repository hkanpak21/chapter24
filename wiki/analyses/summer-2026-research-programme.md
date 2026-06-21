---
title: Summer 2026 Research & Reading Programme — Toward a Computationally Bounded Theory of Learning
type: analysis
date: 2026-06-21
tags: [reading-guide, programme, chapter-24, formal-security, complexity-theory, planning]
---

## Question / Motivation

Mursit is building **Chapter 24** of Arora–Barak ([output/chapter_24.md] working dialogue): the claim that a
**learning system is a first-class abstract machine** — a learner `L` synthesizing an advice program `w`
from bounded oracle access to a source `Π`, with inference = non-uniform evaluation `eval(w,·)` (the P/poly
floor) and **capacity = |w|**. Accuracy *and* security are theorems about that one object; an attack is not a
taxonomy entry but a **capability vector `κ`** over the machine's tapes (the CPA move).

**North star (Mursit's framing):** *the "Goldwasser theorem of AI"* — port security's historical transition
**from Shannon's information-theoretic security to modern reduction-based cryptography** into AI, i.e. take
today's **statistical** AI to a **computationally bounded and understood** AI. We read learning
*computationally* (reductions, classes, one-wayness), not *statistically* (sample complexity, concentration).

This page is the **June–September 2026 calendar** that interleaves the Arora–Barak textbook (Mursit is at
**§2.3 Cook–Levin**) with the paper corpus and drives toward the Chapter 24 deliverables.

**Settings for this plan:**
- **Spine = primary.** Mursit's own thesis leads. Durak's agentic/verification agenda is a *September
  commentary coda*, not a parallel track.
- **Pacing = moderate (~10–12 hrs/wk).** AB chapters stay on schedule; ~1–2 *deep* paper reads per week,
  the rest skimmed *for the map*. Deliverables may slip ~2–3 weeks but the arc holds.
- Papers tagged **[DEEP]** (read in full) vs **[map]** (skim for the idea, file for later).

> Complements [reading-pathway-formal-security](reading-pathway-formal-security.md), which gives the
> *depth order within a cluster*. This page gives the *when*, tied to the textbook and the chapter.

## Findings

### The arc

**reductions → non-uniformity/randomness → one-wayness/average-case → interactive proofs/verification.**
Each month a real Arora–Barak chapter unlocks both a paper cluster and a section of the Chapter 24 dialogue.

---

### JUNE — Reductions & the object defined

- **Arora–Barak:** finish **Ch. 2** (NP-completeness; the *full theory of reductions* — the grammar the whole
  thesis speaks), skim **Ch. 3** (diagonalization), begin **Ch. 6** (Boolean circuits / P/poly — the inference floor).
- **Papers:**
  - **[DEEP]** [Mahloujifar 2019 research statement](../sources/complexity-theoretic-adversarial-ml.md) — re-read
    *to formalize* your taxonomy critique, not to learn it.
  - **[DEEP]** **Valiant, "A Theory of the Learnable" (1984)** *(external — not in corpus)* — the original
    "learning as a computational object." Acquire and ingest.
  - **[DEEP]** [Feldman–Grigorescu–Reyzin–Vempala–Xiao 2017, SQ lower bound](../sources/feldman-statistical-algorithms-planted-clique.md)
    — SQ/MQ/iid/chosen-input *are* your `κ_in` access modes.
  - **[map]** [Canetti–Karchmer 2021, Covert Learning](../sources/covert-learning.md) — crypto-style learning-security definition.
- **Deliverable:** turn the [ideas.md] critique into a *definition* — write `κ` formally; exhibit
  evasion / poisoning / backdoor as **instances of one game**. Advance the lödeg↔nannosh dialogue, points (1)–(2).
- **Durak thread (background):** re-read [VDKMR26 AIOracle](../sources/extending-formalism-cryptography-ai.md)
  asking "what would a *real* reduction here look like?" → start the gap list.

### JULY — Non-uniformity, randomness, and the *computational* adversary

- **Arora–Barak:** **Ch. 6** (P/poly; advice = capacity — supports `capacity = |w|`), **Ch. 7** (BPP,
  BPP ⊆ P/poly), begin **Ch. 9** (one-way functions / PRGs).
- **Papers — the dossier on "does bounding the adversary *computationally* buy anything?" (your exact objection
  to the IT = PPT collapse):**
  - **[DEEP]** [Bubeck–Lee–Price–Razenshteyn, Adversarial Examples from Computational Constraints](../sources/adversarial-examples-computational-constraints.md)
    + [from cryptographic PRGs](../sources/adversarial-examples-prg.md) — IT-robust yet poly-time-vulnerable.
  - **[DEEP]** [Degwekar–Nakkiran–Vaikuntanathan, Win-Win](../sources/win-win-robust-learning.md) —
    robust-learning hardness ⇔ OWF exist. The structural hinge.
  - **[map]** [Garg–Jha–Mahloujifar–Mahmoody, crypto can help robustness](../sources/computational-hardness-robust-learning.md).
  - **[map]** [Etesami–Mahloujifar–Mahmoody, Computational Concentration](../sources/computational-concentration-of-measure-etesami.md)
    — the collapse you want to push *past*; read to know exactly where it bites.
- **Deliverable:** define your **"learning adversary"** — bounded not by perturbation budget but by
  computational/learning resources over the *larger-than-exponential* search space *with an approximate
  objective*. This is the central conjecture; July is where it becomes a definition.
- **Durak thread:** compare [Siu et al., operational authorization](../sources/formalizing-llm-agent-security.md)
  vs AIOracle — which (if either) does your machine model subsume?

### AUGUST — One-wayness, average-case hardness, and the gap engine

- **Arora–Barak:** finish **Ch. 9** (OWF — nannosh's "inversion / one-wayness reading of learning"),
  **Ch. 18** (Levin average-case — your `Π`-as-program *is* an average-case source), **Ch. 19** (hardness
  amplification, hardcore lemma).
- **Papers — backdoors = your cleanest game, + the stat–comp gap engine:**
  - **[DEEP]** [Goldwasser–Kim–Vaikuntanathan–Zamir, Undetectable Backdoors](../sources/planting-undetectable-backdoors.md)
    — the crisp crypto↔ML reduction; your best counterexample to the taxonomy.
  - **[DEEP]** [Christiano–Hilton–Lecomte–Xu, Defendability](../sources/backdoor-defense-learnability-obfuscation.md)
    — already framed as a *game* with confidence/indistinguishability; closest existing object to yours.
  - **[map]** [Kalavasis et al., iO backdoors in NNs](../sources/io-undetectable-backdoors-nn.md);
    [Goldwasser–Shafer–Vafa–Vaikuntanathan, Oblivious Defense](../sources/oblivious-defense-backdoor-removal.md).
  - **[DEEP]** [Brennan–Bresler, Secret-Leakage Planted Clique](../sources/reducibility-statistical-computational-gaps.md)
    (intro + Part II); **[map]** [Wein, Low-Degree survey](../sources/low-degree-polynomials-survey.md).
- **Deliverable:** write the **"accuracy and security as theorems about one object"** section — instantiate
  *one full game* (backdoor-detection or covert-learning) inside your machine model with `κ`. Dialogue points (4)–(5).

### SEPTEMBER — Interactive proofs, verification, synthesis, and the Durak commentary

- **Arora–Barak:** **Ch. 8** (interactive proofs; IP = PSPACE, MIP, ZK), optional PCP skim (Ch. 11).
- **Papers:**
  - **[DEEP]** [Hirahara–Nanashima, Learning in Pessiland](../sources/learning-in-pessiland.md) —
    inductive-inference reading of learning; fuel for nannosh's inversion view.
  - **[DEEP]** [Ball–Gluch–Goldwasser–Kreuter–Reingold–Rothblum, intractability of filtering for alignment](../sources/filter-impossibility-ai-alignment.md)
    — a hardness theorem in *your* idiom; close to the "Goldwasser theorem of AI" target.
  - **[map]** **Neural Interactive Proofs** (Hammond–Adam-Day, ICLR'25, arXiv 2412.08897) — *now* it fits:
    the IP/delegation instantiation of your **integrity / verifiable-delegation** game. A side-track example,
    not a foundation. *(Candidate ingest.)*
- **Deliverables:**
  1. Define the **native complexity class and reduction** (dialogue point 6) — the canonical hard problem for
     *learning-as-synthesis* and what reduces to it; draft the open-fork (point 7).
  2. **Durak coda:** a written critical commentary positioning AIOracle / Siu et al. / verifiable-computation
     (NIP, [ZK pipelines](../sources/zk-verifiable-ai-pipelines.md)) as *projections* of your object — the
     "useful shadows" framing made rigorous.
  - **Target:** by end of September, a defensible Chapter 24 skeleton ready for the `HUMAN consent` tick.

---

### On arXiv 2412.08897 (the paper Durak's group flagged)

**Neural Interactive Proofs** (Hammond & Adam-Day, ICLR'25). Mursit's instinct — "doesn't fit my
understanding" — is correct *at the level of the core thesis*:
- It lives at the **inference/deployment layer** (verifying an untrusted computation's output), not at the
  layer of formalizing the learner-as-machine. A **"useful shadow"** — the *interactive-proof projection*.
- Its contribution is **ML methodology** (RL-train a verifier), **not a reduction / hardness theorem**; it is
  game-*theoretic* (equilibria), not game-*based-security* (indistinguishability).
- **Where it does connect:** it is a candidate instantiation of the **verification-of-computation / "correct
  outputs under ZK"** objective Mursit named in ideas.md. Read it in **September, after AB Ch. 8**, as one
  worked example in the taxonomy-of-games — and as a signal that Durak's axis is agentic/verifiable computation.

## Implications for the Wiki

- **Candidate ingests this summer (not yet in corpus):** Valiant 1984 (PAC origin); Neural Interactive Proofs
  (Hammond–Adam-Day 2025). Acquire and ingest per CLAUDE.md when reached.
- Each month's **deliverable** should be appended to [output/chapter_24.md] as dialogue turns; concept pages
  (`capability-vector-kappa`, `learning-adversary`, `learning-as-synthesis`) should be created when those
  definitions stabilize — currently they exist only as prose in the dialogue.
- The **Durak coda** (September) is a natural future analysis page once written.
- Unverified raw titles to confirm opportunistically: `S25_PACLearningSurvey.pdf`,
  `20344_Statistically_Undetectab.pdf` (see [raw/SOURCES.md]).

## References

- [output/chapter_24.md] — the Chapter 24 working dialogue (the spine this programme serves).
- [output/ideas.md] — Mursit's critique of Mahloujifar & Durak that motivates the `κ`-game.
- [reading-pathway-formal-security](reading-pathway-formal-security.md) — depth order within each cluster.
- [overview.md](../overview.md) — current three-pillar synthesis.
