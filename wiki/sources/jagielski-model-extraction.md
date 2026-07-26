---
title: High Accuracy and High Fidelity Extraction of Neural Networks
type: source
date_ingested: 2026-07-26
authors: [Matthew Jagielski, Nicholas Carlini, David Berthelot, Alex Kurakin, Nicolas Papernot]
venue: USENIX Security 2020
year: 2020
tags: [adversarial-ml, complexity theory, hardness-reductions, evasion-attacks]
---

> **Provenance.** Verified sweep, not a full read.

## Summary

Separates two goals of model extraction — **accuracy** (match the task) and **fidelity** (match the
victim model's decisions, including its errors) — and gives attacks for each. For this programme its
importance is a single structural result: extraction contains a provably hard sub-problem.

**Given two weight vectors, deciding whether they compute the same function is NP-hard.** This is a
hardness theorem about the **evaluation** map `w ↦ M_w` — about the fiber of the *parameterization*,
not of *training*. It is the exact analogue, one level over, of the theorem the programme wants for the
training map, and it is the reason to believe such a theorem is available at all.

Companion line: Carlini–Jagielski–Mironov, *Cryptanalytic Extraction of Neural Network Models*, CRYPTO
2020 (arXiv:2003.04884) reads weights out of a network by differential-cryptanalysis-style queries; the
attack was made **polynomial** by Canales-Martínez, Chávez-Saab, Hambitzer, Rodríguez-Henríquez,
Satpute and Shamir, EUROCRYPT 2024 (eprint 2023/1526). So the evaluation map is now known to be
navigable in polynomial time in the relevant regime, despite the NP-hardness of the decision version.

That pairing is the cautionary lesson: **an NP-hardness result about the map did not prevent an
efficient practical inversion.** Any training-map hardness theorem must be stated so the same gap
cannot open under it.

## Key Contributions

- The accuracy/fidelity distinction for extraction.
- NP-hardness of deciding functional equivalence of two networks.
- Learning-theoretic and practical extraction attacks on production-scale models.

## Key Definitions / Theorems

- **Functional equivalence is NP-hard**: given two weight vectors, deciding whether they induce the same
  function on the input domain.

## Connections

- **The contrast case for [Suliman et al. USENIX Sec'25](suliman-data-forging-attacks.md).** Evaluation
  map: hardness proved. Training map: conjectured, open.
- Fiber of the evaluation map, studied directly: Grigsby–Lindsey–Meyerhoff–Wu, *Functional dimension of
  feedforward ReLU networks*, arXiv:2209.04036 — *"fibers of the realization map"*, disconnected, with
  non-constant functional dimension. Note this literature owns the word "fiber" for the other map.
- Identifiability classics for the evaluation map: Sussmann 1992; Fefferman 1994; Phuong–Lampert ICLR
  2020; Vlačić–Bölcskei *Adv. Math.* 376 (2021).
- Concept: [fiber-of-the-training-map](../concepts/fiber-of-the-training-map.md) — which exists partly to
  keep the two maps apart.

## Open Questions / Limitations

- NP-hardness is worst-case and did not obstruct the EUROCRYPT 2024 polynomial attack on the average
  case. A worst-case hardness theorem is not a security guarantee.

## Quotes / Notable Passages

*(Full read owed; no verbatim passages extracted in the sweep.)*
