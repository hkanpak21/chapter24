---
title: Overview — Formal Security
type: overview
last_updated: 2026-04-23
sources_ingested: 15
---

# Formal Security: Research Overview

*Evolving synthesis of the wiki. Updated after each ingest.*

---

## The Central Question

How do formal tools from cryptography and complexity theory apply to the security and robustness of machine learning systems? Specifically:

- When is it **computationally hard** to attack or subvert a learning system?
- Can we build **provably robust** learners under cryptographic assumptions?
- Where do **statistical learnability** and **computational learnability** diverge — and why?
- How do we **formally model** the security of modern AI agents so that we can prove security, not just claim it?

---

## Major Themes

### 1. Adversarial Robustness: The Geometry of Hardness

The Mahloujifar line of work establishes that adversarial vulnerability is not an engineering failure but a mathematical inevitability for any classifier with nonzero error, in sufficiently concentrated metric probability spaces. The key tool is **concentration of measure**: in high dimensions, any set of constant measure is close to almost every point, meaning an adversary with sub-linear perturbation budget can always find adversarial examples for any imperfect classifier. [Mahloujifar, Diochnos, Mahmoody AAAI 2019](sources/curse-of-concentration.md) unifies prior sphere/Gaussian/hypercube results under the Lévy-family framework.

**The computational twist**: On product distributions, polynomial-time adversaries are as powerful as information-theoretic adversaries — [computational concentration of measure (Etesami, Mahloujifar, Mahmoody SODA 2020)](sources/computational-concentration-of-measure-etesami.md) closes the gap via the MUCIO algorithm, resolving the [MM19] open question for the full 1/poly(n) range. This is a negative result: hardness assumptions don't help there. But there exist carefully constructed learning problems where computational robustness strictly exceeds information-theoretic robustness ([Garg, Jha, Mahloujifar, Mahmoody ALT 2020](sources/computational-hardness-robust-learning.md); [Degwekar, Nakkiran, Vaikuntanathan COLT 2019](sources/win-win-robust-learning.md)), showing cryptographic hardness *can* help in principle.

**Empirical reality check**: [Mahloujifar, Zhang, Mahmoody, Evans NeurIPS 2019](sources/empirically-measuring-concentration.md) provides the first provably-convergent estimator of the concentration function from samples and finds that on MNIST and CIFAR-10, the concentration-based intrinsic-robustness bound is **order-of-magnitude higher than SOTA robust-classifier accuracy**. Concentration does not explain the full observed vulnerability — either current defenses are far from optimal, or there is an additional barrier (e.g., manifold structure, local Lipschitz constraints) beyond concentration.

**Multi-party extension**: [Mahloujifar, Mahmoody, Mohammed ICML 2019](sources/multi-party-poisoning.md) generalizes poisoning to the (k, p) multi-party model, proving universal μ → μ^{1−pk/m} amplification via generalized p-tampering — handling correlated tamperable indices that broke prior independent-p-tampering proofs.

**Key tension**: Concentration of measure sets an information-theoretic ceiling on robustness. Computational complexity may or may not help depending on the structure of the problem. The boundary is not yet fully characterized, and empirical evidence suggests concentration is not the tightest binding constraint on natural data.

### 2. Statistical vs. Computational Gaps: The Reduction Frontier

Brennan & Bresler (2020) attack the longstanding problem of why efficient algorithms require more data than necessary in high-dimensional structured problems. They introduce **Secret Leakage Planted Clique (PC_ρ)** — a mild generalization of the planted clique conjecture where the hidden clique vertex set is drawn from a structured distribution ρ rather than uniformly.

This small change has large consequences: it enables reductions to problems with very different distributional structure, breaking out of the "sparse submatrix + noise" straitjacket that limited prior average-case reductions. The result is the first web of reductions simultaneously evidencing statistical-computational gaps for: robust sparse mean estimation, SBMs, sparse PCA, tensor PCA, mixtures of sparse linear regressions, hidden partition models, and more.

**Key insight**: The "leakage" of ρ is information about the hidden clique's structure that can be encoded into the target problem's natural distribution. By varying ρ (k-partite, bipartite, hypergraph variants), reductions reach structurally diverse problems.

### 3. Formalizing AI Security with Cryptographic Rigor

Villa et al. (2026) apply cryptographic methodology to the newest frontier: agentic LLM systems. The **AIOracle** framework models an agentic AI system as a two-phase oracle (LEARN, INFER) with formal security games capturing confidentiality, integrity, and availability simultaneously.

The paper makes the formal apparatus of cryptography available for AI security: adversary capability sets (ATK), security games, reduction proofs, composition theorems. The dual construction theorem provides a modular way to compose helpful (CAIO) and safe (BAIO) AIOracles while preserving both properties.

**Key tension**: DPP-secure (privacy-preserving) training fundamentally conflicts with completeness. This formalizes why privacy and utility are in tension in AI systems — not just heuristically, but provably.

---

## Cross-Cutting Themes

### Hardness Assumptions as Building Blocks
All three papers rely on assumptions that cannot be proven from first principles:
- Mahloujifar: implicitly assumes product/concentrated distributions
- Brennan & Bresler: assume PC_ρ conjecture (k-HPC^s is strongest)
- Villa et al.: assume cryptographic hardness (DLP mentioned for DPD game)

The choice of starting assumption matters enormously for what can be reduced/proven.

### The Cryptography–ML Interface
A recurring theme: cryptographic techniques (hardness assumptions, reduction proofs, security games, tamper models) transfer to ML security in both directions:
- Crypto → ML: p-tampering model, computational hardness for robustness, formal security games for AI
- ML → Crypto: adversarial sample complexity has direct analogues in coin tossing; concentration of measure informs randomness extraction impossibility

### What Formal Methods Buy
Formal treatment provides: precise problem definitions, provable separations, impossibility results, and composition theorems. Without formalism, it's hard to know whether a proposed defense is robust or merely heuristic. Villa et al. make this point explicitly — existing AI safety frameworks lack a common formal foundation, making them hard to compare or compose.

---

## Current Thesis

*The field of formal AI security is at an inflection point. The complexity-theoretic and cryptographic tools needed to prove hardness results for ML robustness exist — concentration of measure, average-case reductions, formal security games — but connecting them into a coherent theory requires bridging three traditionally separate research communities: learning theory, complexity theory, and cryptography. The three papers in this wiki represent significant steps in each bridge: Mahloujifar builds the complexity-ML bridge for robustness; Brennan & Bresler build the complexity-statistics bridge for hardness of inference; Villa et al. build the cryptography-AI bridge for agentic system security. The next major open problem is connecting all three: a unified theory of provably secure, efficient, and robust learning.*

---

## Key Open Problems

1. Can cryptographic hardness be leveraged to build *practically* robust learning algorithms (beyond theoretical existence proofs)?
2. Is PC the right starting assumption for statistical reductions, or is k-HPC^s (or something else) the canonical hard problem?
3. Can the AIOracle security framework be instantiated with efficient constructions?
4. What is the tight sample complexity of adversarially robust PAC learning for general concept classes?
5. Can statistical-computational gaps be proven from worst-case complexity assumptions?
6. Do concentration of measure bounds and statistical-computational gaps interact — are there problems where high concentration implies both easy adversarial attacks and computational hardness of learning?

---

## Sources Contributing to This Overview

- [A Complexity Theoretic Approach to Adversarial ML](sources/complexity-theoretic-adversarial-ml.md) — Mahloujifar 2019
- [Extending the Formalism and Theoretical Foundations of Cryptography to AI](sources/extending-formalism-cryptography-ai.md) — Villa et al. 2026
- [Reducibility and Statistical-Computational Gaps from Secret Leakage](sources/reducibility-statistical-computational-gaps.md) — Brennan & Bresler 2020
