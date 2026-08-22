---
title: "Learning in Pessiland via Inductive Inference"
type: source
date_ingested: 2026-04-23
authors: [Shuichi Hirahara, Mikito Nanashima]
venue: "Electronic Colloquium on Computational Complexity, Report No. 100 (2023). The FOCS 2023 attribution carried on this page is not stated in the PDF in `raw/`; the only FOCS mentions in it are citations to other work."
year: 2023
tags: [learning-theory, complexity-theory, impagliazzo-worlds, pessiland, inductive-inference, one-way-functions]
claim_quantifier: conditional
antecedent: "the non-existence of an infinitely-often one-way function. Every headline statement is an equivalence with that hypothesis, not a theorem about our world."
adversary_bound: "none. There is no adversary in this paper. The bounded party is the learner, which is polynomial-time in the average-case statements and, in the worst-case variants, runs in time exponential in the computational depth of the instance."
model_class: "adaptively changing distributions; P/poly-samplable distributions; all polynomial-length multi-output functions; P/poly with membership queries under the uniform distribution"
algorithm_class: "universal extrapolation, following Solomonoff's inductive inference and Impagliazzo–Levin (FOCS'90)"
date_verified: 2026-08-20
---

## Summary

This paper (HN23) proves a striking result about **Impagliazzo's Pessiland** (the world where NP is hard on average but no one-way functions exist): **Pessiland is a wonderland for machine learning**. In Pessiland, the universal extrapolation algorithm of Impagliazzo-Levin — a Solomonoff-inductive-inference-inspired algorithm — efficiently solves a broad class of learning tasks. This is surprising because Pessiland is traditionally considered the most pessimistic world (NP-hard on average, no useful cryptography), but for learning, it turns out to be the most *optimistic* in terms of algorithmic power.

The key technical contribution is a **unified framework for constructing strong learning algorithms under the non-existence of a one-way function**. The hypothesis throughout is the non-existence of an **infinitely-often** one-way function, and the conclusions are stated as equivalences with it. Theorem 2.4 lists four learning statements each equivalent to that hypothesis:

- learning **adaptively changing distributions** in polynomial time, improving Naor–Rothblum (ICML'06) in sample complexity from `O(s·ε⁻⁴δ⁻²)` to `O(s·ε⁻²δ⁻¹)` and making the learner universal;
- **distributional learning** of `P/poly`-samplable distributions in polynomial time on average;
- **agnostic learning** of all polynomial-length multi-output functions in polynomial time on average, with sample complexity `O(s(n)/ε²)`, optimal up to a constant, generalising Blum–Furst–Kearns–Lipton (Crypto'93) from PAC to agnostic, from binary to polynomial-length labels, and to joint distributions over samples;
- **weak PAC learning of `P/poly` with membership queries** under the uniform example distribution.

**Correction, 2026-08-20.** The list previously given here — "PAC learning of concepts with small circuit complexity, agnostic learning, error-tolerant learning, certain statistical estimation tasks" — includes two items with no counterpart in the paper. The strings "error-tolerant" and "statistical estimation" do not occur in it.

The paper also gives the first characterisation of the existence of a one-way function by the **worst-case** hardness of a promise problem in AM, and a Bloom-filter corollary: without one-way functions, a legitimate user must spend super-polynomially more time than the adversary to build a non-trivial Bloom filter.

## Claim Boundary

- **Quantified over:** learning tasks whose samples come from efficiently samplable distributions, in an **average-case** setting. Theorem 2.4's items are equivalences; the paper is not asserting that any of them holds. Theorem 2.3's agnostic result is universal over multi-output target classes containing polynomial-size circuits, and the authors note that the same task is provably impossible in the worst case.
- **Antecedent:** non-existence of an **infinitely-often** one-way function — a hypothesis widely believed false. Every "Pessiland is a wonderland" statement is downstream of it. The infinitely-often qualifier is load-bearing and is easy to drop when citing.
- **Which party is constrained:** the *learner*. In the average-case statements it is polynomial time. In the worst-case variants, Theorems 2.8 and 2.9, the algorithms run in time exponential in the **computational depth** of the instance, which the abstract states plainly. There is no adversary anywhere in the paper.
- **Does not establish:** anything about adversarial robustness, evasion attacks, or security. Neither "adversarial" nor "robust" in that sense appears in the paper. The inferences drawn elsewhere on this page from Pessiland to adversarial-robustness impossibility are the wiki's, not the authors'.
- **Abstract vs theorem:** none found. The abstract states the infinitely-often qualifier implicitly through "the non-existence of a one-way function" but names the exponential-in-computational-depth running time explicitly, which the theorems bear out.

This result has deep implications for the **formal theory of AI security**: it places learning-theoretic results in the context of Impagliazzo's worlds, showing that adversarial robustness, secure learning, and statistical-computational gaps are fundamentally tied to the existence of cryptographic primitives (OWFs). Specifically:
- If OWFs do not exist, ML is "easy" in a strong sense.
- If OWFs exist, ML encounters computational barriers (Bubeck-Lee-Price-Razenshteyn, Degwekar-Nakkiran-Vaikuntanathan, etc.).

The dichotomy is close to sharp and tightens the structural understanding of computational robustness for ML.

## Key Contributions

- **Pessiland is a learning-theoretic wonderland**: absent an infinitely-often one-way function, universal extrapolation solves the four learning tasks of Theorem 2.4 in polynomial time on average.
- **Unified framework based on Solomonoff inductive inference**: the universal extrapolation algorithm of Impagliazzo–Levin (FOCS'90) is the generic tool. The paper notes that Impagliazzo and Levin left the algorithm unspecified and its relationship to other learning models unclear.
- **Robustness of average-case learnability**: Theorem 2.4 yields reductions from agnostic to PAC learning, from general to uniform distributions, from distribution learning to binary classification, and from membership-query to random-sample learning — a computational counterpart to the fundamental theorem of statistical learning.
- **First characterisation of one-way function existence by worst-case hardness of a promise problem in AM.**
- **Bloom filter corollary (Corollary 2.2)**: without one-way functions, a legitimate user must spend super-polynomially more time than the adversary to construct a non-trivial Bloom filter.
- **Correction, 2026-08-20:** two bullets here previously read "Bridges Impagliazzo's five worlds to ML security: adversarial robustness hardness ⇔ existence of OWFs" and "Removes Pessiland as a candidate world for adversarial-robustness impossibility". The paper contains no adversarial-robustness result and no such biconditional; both were inferences from it, and are kept in the Connections section below where they can be read as such.

## Key Definitions / Theorems

- **Impagliazzo's Pessiland**: complexity world where NP is hard on average (Heuristica fails) but no OWF exists.
- **Universal extrapolation algorithm (Impagliazzo-Levin)**: a generic predictor that, given a sequence, predicts the next element by enumerating short programs consistent with the observations.
- **Theorem 2.1 (informal; formal at Theorem 9.7)**: there exists no infinitely-often one-way function if and only if there is an efficient randomized algorithm that ε-closely learns every unknown adaptively changing distribution with an `s`-bit initial state, with sample complexity `O(s·ε⁻²δ⁻¹)`.
- **Theorem 2.3 (informal; formal at Theorem 10.6)**: for any multi-output target class `C` containing polynomial-size circuits, non-existence of an infinitely-often one-way function is equivalent to `C` being efficiently agnostically learnable on average, with sample complexity `O(s(n)/ε²)` and hypothesis description length `O(n·s(n)/ε²)`.
- **Theorem 2.4**: the four-way equivalence listed in the summary, which the authors present as a computational analogue of the fundamental theorem of statistical learning.
- **Theorems 2.8 and 2.9**: worst-case variants of Theorems 2.1 and 2.3, whose algorithms run in time exponential in computational depth.
- **Correction, 2026-08-20:** the previous entries here stated a "main theorem" listing error-tolerant learning, and a "corollary" that adversarial robustness impossibility requires OWFs. Neither is in the paper; the second is an inference from it.

## Connections

- Source: [Adversarial Examples from Computational Constraints (BPR19)](adversarial-examples-computational-constraints.md) — an SQ lower bound with no cryptographic assumption, so it is not in HN23's scope. **Correction, 2026-08-20:** this line previously read "assumes OWFs to construct hard-to-robustly-learn tasks"; BPR assumes no such thing.
- Source: [Adversarial Examples from Cryptographic PRG (BLPR19)](adversarial-examples-prg.md) — constructs a hard-to-robustly-learn task under quadratic residuosity, via a trapdoor PRG. The relation to HN23 is suggestive rather than a converse: HN23 characterises the non-existence of infinitely-often one-way functions by average-case *learnability*, not by robust learnability, and it does not treat adversarial perturbations at all.
- Source: [Win-Win Theorem (Degwekar-Nakkiran-Vaikuntanathan 2019)](win-win-robust-learning.md) — robust-learning hardness ⇒ OWF; HN23 closes the loop by showing ¬OWF ⇒ no hard learning tasks (a sharper rephrasing of Pessiland's ML tractability).
- Source: [Low-Degree Polynomials Survey (Wein 2025)](low-degree-polynomials-survey.md) — low-degree predictions for ML hardness; HN23 shows these must rely on OWF-existing worlds.
- Concept: [One-Way Functions](../concepts/one-way-functions.md).
- Concept: [Win-Win Theorem](../concepts/win-win-theorem.md).
- Concept: [Computational vs. IT Robustness](../concepts/computational-vs-it-robustness.md).
- Concept: [PAC Learning](../concepts/pac-learning.md).

## Open Questions / Limitations

- **Only covers learning tasks with "simple" true concepts** (poly-size circuits); tasks where the true concept is complex may behave differently.
- **Non-uniform learners**: the framework uses uniform polynomial-time learners; non-uniform analogues may differ.
- **Quantitative tightness**: the sample complexity achieved by universal extrapolation is not optimal for specific problems.
- **Beyond classification**: extensions to regression, distribution learning, RL etc. are partially covered but not fully.
- **Does not address heuristic-case vs worst-case hardness**: HN23 is about average-case Pessiland; distinguishing Pessiland from Heuristica is a separate question.

## Quotes / Notable Passages

> _Not verbatim. Checked against `raw/HN23_LearningInPessiland.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> Pessiland is considered the most pessimistic world because it offers neither algorithmic nor cryptographic benefits. However, we demonstrate that Pessiland is, in fact, a wonderland for machine learning in which various learning tasks can be efficiently solved by the generic algorithm of universal extrapolation.

Verified against `raw/HN23_LearningInPessiland.pdf` on 2026-08-20. The paraphrase above splices two separated abstract sentences; the originals are:

> "This world is considered the most pessimistic because it offers neither algorithmic nor cryptographic benefits."

> "Conceptually, the framework demonstrates that Pessiland is, in fact, a wonderland for machine learning in which various learning tasks can be efficiently solved by the generic algorithm of universal extrapolation."

— abstract.

> "We develop a unified framework for constructing strong learning algorithms under the non-existence of a one-way function."

> "Our learning algorithms are worst-case algorithms that run in exponential time with respect to computational depth, and as a by-product, we present the first characterization of the existence of a one-way function by the worst-case hardness of some promise problem in AM."

— abstract, the sentence that bounds "efficiently".
