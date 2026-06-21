---
title: "Learning in Pessiland via Inductive Inference"
type: source
date_ingested: 2026-04-23
authors: [Shuichi Hirahara, Mikito Nanashima]
venue: FOCS 2023 (ECCC TR23-100)
year: 2023
tags: [learning-theory, complexity-theory, impagliazzo-worlds, pessiland, inductive-inference, one-way-functions]
---

## Summary

This paper (HN23) proves a striking result about **Impagliazzo's Pessiland** (the world where NP is hard on average but no one-way functions exist): **Pessiland is a wonderland for machine learning**. In Pessiland, the universal extrapolation algorithm of Impagliazzo-Levin — a Solomonoff-inductive-inference-inspired algorithm — efficiently solves a broad class of learning tasks. This is surprising because Pessiland is traditionally considered the most pessimistic world (NP-hard on average, no useful cryptography), but for learning, it turns out to be the most *optimistic* in terms of algorithmic power.

The key technical contribution is a **unified framework for constructing strong learning algorithms under the non-existence of a one-way function**. Assuming ¬OWF, the authors show that a generic algorithm based on universal extrapolation efficiently solves:
- PAC learning of concepts with small circuit complexity,
- Agnostic learning for a wide class of hypothesis families,
- Error-tolerant learning,
- Certain statistical estimation tasks,
and more — essentially, any learning problem where the relevant hypothesis is "simple" in a circuit-complexity sense.

This result has deep implications for the **formal theory of AI security**: it places learning-theoretic results in the context of Impagliazzo's worlds, showing that adversarial robustness, secure learning, and statistical-computational gaps are fundamentally tied to the existence of cryptographic primitives (OWFs). Specifically:
- If OWFs do not exist, ML is "easy" in a strong sense.
- If OWFs exist, ML encounters computational barriers (Bubeck-Lee-Price-Razenshteyn, Degwekar-Nakkiran-Vaikuntanathan, etc.).

The dichotomy is close to sharp and tightens the structural understanding of computational robustness for ML.

## Key Contributions

- **Pessiland is a learning-theoretic wonderland**: under ¬OWF, universal-extrapolation-based algorithms efficiently solve a broad class of learning tasks.
- **Unified framework based on Solomonoff inductive inference**: the universal extrapolation algorithm of Impagliazzo-Levin is the generic tool.
- **Bridges Impagliazzo's five worlds to ML security**: adversarial robustness hardness ⇔ existence of OWFs, now placed alongside cryptographic landscape.
- **Strengthens Win-Win framing**: together with Degwekar-Nakkiran-Vaikuntanathan and Bubeck-Lee-Price-Razenshteyn, yields a near-complete characterization: ML-hard ⇔ OWF-hard.
- **Removes Pessiland as a candidate world for adversarial-robustness impossibility**: if we are in Pessiland, then adversarial robustness is achievable efficiently.

## Key Definitions / Theorems

- **Impagliazzo's Pessiland**: complexity world where NP is hard on average (Heuristica fails) but no OWF exists.
- **Universal extrapolation algorithm (Impagliazzo-Levin)**: a generic predictor that, given a sequence, predicts the next element by enumerating short programs consistent with the observations.
- **Main theorem (informal)**: Assuming no OWF exists (Pessiland or better), the universal extrapolation algorithm efficiently solves (a) PAC learning of concepts with poly-size circuits, (b) agnostic learning, (c) error-tolerant learning for a broad class.
- **Corollary**: adversarial robustness impossibility for natural problems requires OWFs — Pessiland doesn't give us the hardness we need for computationally-unlearnable-but-IT-robust tasks.

## Connections

- Source: [Adversarial Examples from Computational Constraints (BPR19)](adversarial-examples-computational-constraints.md) — assumes OWFs to construct hard-to-robustly-learn tasks; HN23 shows this is *necessary* — without OWFs, such tasks cannot exist.
- Source: [Adversarial Examples from Cryptographic PRG (BLPR19)](adversarial-examples-prg.md) — uses standard PRGs / OWFs; HN23 is the converse.
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

> "Pessiland is considered the most pessimistic world because it offers neither algorithmic nor cryptographic benefits. However, we demonstrate that Pessiland is, in fact, a wonderland for machine learning in which various learning tasks can be efficiently solved by the generic algorithm of universal extrapolation."

> "We develop a unified framework for constructing strong learning algorithms under the non-existence of a one-way function."
