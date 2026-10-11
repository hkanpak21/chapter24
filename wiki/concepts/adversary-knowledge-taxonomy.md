---
title: Adversary Knowledge Taxonomy
type: concept
tags: [adversarial-ml, threat-model, evasion-attacks, cryptography, evaluation-methodology]
---

## Definition

A structured account of *what an attacker is assumed to know*, replacing the informal white-box / grey-box / black-box / no-box vocabulary. Two 2024 systematizations give incompatible but complementary structures for the same space.

**Order-theoretic (FK24).** An **Information Extraction Oracle** (IEO) is a stateful machine `O : {0,1}* → {0,1}*` answering queries with information. A **domination** relation `⊏` partially orders IEOs by their outputs; the base case carrying complexity content is that for element-valued outputs, `O₂ ⊏ O₁` when some probabilistic polynomial-time `f` maps `O₁`'s output to `O₂`'s. Incomparable oracles combine as `O_{A&B}(x) = [O_A(x), O_B(x)]`. Knowledge is then partitioned into four categories, each with its own Hasse diagram under `⊏`:

- **model** — parameters `θ_M`, exact architecture `φ_M`, a set of possible architectures, query access to scores, query access to labels;
- **data** — the training set `D`, other same-distribution data `D'`, out-of-distribution data `E`;
- **training** — the exact `Train` function, or a set `T = {Train' | g_Train(Train') = True}` of functions sharing a known property;
- **defence** — full awareness of algorithm and parameters `(ρ, ϱ)`, partial awareness (algorithm only), or a set of possible defences.

**Axis-based (SSK+24), for black-box attacks.** Four independent dimensions, each ordered by increasing knowledge:

- **query access** — none, or interactive;
- **API feedback** — hard label, top-`k` scores (`1 ≤ k < N`), or the complete confidence vector;
- **quality of initial auxiliary data** — no overlap, partial overlap, or complete overlap with the target's training *distribution* (overlap defined over feature and label space, on distributions rather than datasets);
- **quantity of initial auxiliary data**;

with the availability of pretrained models as a sub-axis interacting with the others.

A third, informal predecessor is the enumeration in [ACW18 §6.1](../sources/obfuscated-gradients.md): rather than redefining the vocabulary, list what may be secret — model architecture, model weights, training algorithm, training data, test-time randomness (values or only the distribution), and whether query access is granted and at what output granularity.

## Intuition

Robustness claims are comparable only if the threat models are. Two attacks reporting 90% success are incomparable if one had the weights and the other had a thousand label queries. The purpose of a knowledge taxonomy is to make the assumptions a lattice coordinate rather than an adjective, so that (a) a claim of improvement can be checked at matched knowledge, and (b) empty regions of the space become visible as research targets.

Both papers use the structure to overturn published claims. [SSK+24](../sources/sok-black-box-attack-pitfalls.md) invalidates a state-of-the-art claim by giving the *baseline* the same knowledge the new attack assumed. [FK24](../sources/sok-adversary-knowledge.md) finds that transferable attacks come within 7.3% expected success rate of white-box attacks on CIFAR-10 once they are credited with the training data and training function they silently use to build surrogates.

## Properties / Theorems

**Theorems 1–4 (FK24)**: each of the four Hasse diagrams (model, data, training, defence) holds under the `⊏` ordering. These are universal statements about a finite set of defined oracles, and follow from the definition of `⊏`; they are structural facts about the framework, not results about attacks.

**Ordering is partial, not total.** Definition 9's combination rule exists because incomparable knowledge is the normal case. There is no single scalar "amount of knowledge".

**Order does not determine value.** [FK24](../sources/sok-adversary-knowledge.md) takeaway 3: "Information categories matter, but their effect on performance is not straightforward." Strictly more knowledge does not translate monotonically into attack success across categories.

**Occupancy is uneven and does not track practical relevance.** [SSK+24](../sources/sok-black-box-attack-pitfalls.md) places 164 attacks in its grid and finds that the cells matching deployed APIs — top-`k` scores, and abundant non-overlapping data — are nearly empty, while the full-confidence-vector cell is crowded. A new attack built for the top-`k` cell sets the state of the art there and still trails attacks from the strictly more restrictive hard-label cell, which the authors read as a technical rather than an intrinsic gap.

**Composition with other attack families.** Given auxiliary data and pretrained models, model extraction and model inversion move an attacker between cells; the taxonomy makes this visible as a path rather than a separate literature [SSK+24 §VI-C].

**Kerckhoffs's principle as a standing constraint.** Both formalisms assume the defence algorithm is known. [CAP+19 §2.2.3](../sources/on-evaluating-adversarial-robustness.md) states the two conditions any legitimately secret value must satisfy: it must be efficiently replaceable if leaked, and non-extractable by a querying adversary.

## Where It Appears

- [SoK: Analyzing Adversarial Examples (FK24)](../sources/sok-adversary-knowledge.md) — IEOs, `⊏`, the four Hasse diagrams, and a cryptographic-style adversarial example game with an explicit distinguisher.
- [SoK: Pitfalls in Evaluating Black-Box Attacks (SSK+24)](../sources/sok-black-box-attack-pitfalls.md) — the four black-box axes, the occupancy map over 164 attacks, and the addition of local attack runtime as a comparison metric.
- [Obfuscated Gradients (ACW18)](../sources/obfuscated-gradients.md) — the informal enumeration that both later frameworks refine, and the distinction it draws within "test time randomness (either the values chosen or the distribution)", which neither later framework drops.
- [On Evaluating Adversarial Robustness (CAP+19)](../sources/on-evaluating-adversarial-robustness.md) — threat model as goals + capabilities + knowledge; Kerckhoffs's principle; the two conditions on admissible secrets.
- [RobustBench (CAS+21)](../sources/robustbench.md) — fixes one point in the space (fully white-box, fixed `ε`) and standardizes there, which is why the benchmark cannot see knowledge-restricted defences.
- [Input Manipulation Threat Model](input-manipulation-threat-model.md) and [AIOracle Framework](aioracle-framework.md) — the same formalization move carried out for LLM-agent systems rather than image classifiers.

## Related Concepts

- [Adaptive Attacks](adaptive-attacks.md) — an attack "only restricted by the threat model" is exactly as precise as the knowledge taxonomy behind it.
- [Evasion Attacks](evasion-attacks.md).
- [Computational Indistinguishability](computational-indistinguishability.md) — the source of [FK24](../sources/sok-adversary-knowledge.md)'s distinguisher-based definition of imperceptibility, adapted via the "human-like distinguisher" whose capabilities match a human or any human-made system.
- [Computational vs Information-Theoretic Robustness](computational-vs-it-robustness.md) — the axis that both taxonomies leave out.

## Open Questions

- **No compute axis in either taxonomy.** [FK24](../sources/sok-adversary-knowledge.md) §3 announces that adversary knowledge includes "access to data and computing resources", then formalizes four categories, none of which is computation: compute survives only as the PPT quantifier inside `⊏` and as a query counter in oracle state. [SSK+24](../sources/sok-black-box-attack-pitfalls.md) measures local runtime, but as an evaluation metric for ranking attacks, never as a threat-model coordinate. Neither framework can distinguish two defences that leak identical information at different attacker cost.
- Completeness is asserted by survey construction in both papers, never proved. Nothing rules out a fifth axis, and [FK24](../sources/sok-adversary-knowledge.md)'s own prose supplies a candidate.
- The two structures have not been reconciled. [FK24](../sources/sok-adversary-knowledge.md) gives an order with no cost dimension; [SSK+24](../sources/sok-black-box-attack-pitfalls.md) gives a cost dimension with no order. Neither cites the other in the versions read, despite appearing within months of each other.
- Query *budget* is under-theorized. [SSK+24](../sources/sok-black-box-attack-pitfalls.md) distinguishes interactive from non-interactive access but treats the number of permitted queries as a practical footnote (rate limits, cost, suspicion), not as a parameter; [FK24](../sources/sok-adversary-knowledge.md) carries it as an oracle's state with no ordering over budgets.
- Both frameworks describe knowledge held *at attack time*. Neither models an adversary who acquires knowledge over time, which is what an attacker composing model extraction with evasion actually does.
