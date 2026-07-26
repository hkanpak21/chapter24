---
title: "Proof-of-Learning: Definitions and Practice"
type: source
date_ingested: 2026-07-26
authors: [Hengrui Jia, Mohammad Yaghini, Christopher A. Choquette-Choo, Natalie Dullerud, Anvith Thudi, Varun Chandrasekaran, Nicolas Papernot]
venue: IEEE S&P 2021
year: 2021
tags: [complexity theory, adversarial-ml, certification, hardness-reductions]
---

> **Provenance.** Verified sweep, not a full read. **Must-cite** for anything about fiber navigation —
> this is the same quantity under a different name.

## Summary

A prover wants to demonstrate it performed the computation of training. The proof is the sequence of
intermediate checkpoints; a verifier spot-checks that consecutive checkpoints are consistent with a few
gradient steps.

The security notion is what matters here. A **spoof** is any proof that verifies but was obtained with
**strictly less computation than honest training**, given the final weights. That is exactly fiber
navigation priced in compute: the spoofer must produce a trajectory landing at `w` — a point of the
training map's fiber, plus a path to it — and the security claim is that doing so costs at least what
honest training cost.

**So the programme's central quantity already has an operational definition in the security
literature.** It is not called navigability, and it is stated as a compute-comparison rather than as a
complexity class, but it is the same object.

## Key Contributions

- Formal definition of proof-of-learning with completeness and spoof-resistance.
- The compute-relative security notion: spoofing must not be cheaper than training.
- A concrete verification protocol over checkpoint sequences.

## Key Definitions / Theorems

- **Spoof**: a verifying proof produced with strictly less computation than honest training, given the
  final weights.

## Connections

- **The same quantity as** [fibers-of-the-training-map](../../output/fibers-of-the-training-map.md), under
  another name and with a compute-comparison instead of a hardness statement.
- **Broken twice.** Zhang et al., IEEE S&P 2022 (arXiv:2108.09454); Fang et al., EuroS&P 2023
  (arXiv:2208.03567) — the latter noting the assumptions needed for security *"reduce to open problems in
  learning theory."* That sentence is the programme's opening: the open problems in question are the
  ones being attacked.
- Adjacent forging line: Thudi et al., USENIX Security 2022 (arXiv:2110.11891) — *"one can obtain the
  same model using different datasets"*, used as a definitional attack on unlearning; Kong–Roy
  Chowdhury–Chaudhuri arXiv:2303.03648 — efficient proofs of repudiation defeating MIA;
  [Suliman et al.](suliman-data-forging-attacks.md).
- Concept: [fiber-of-the-training-map](../concepts/fiber-of-the-training-map.md).

## Open Questions / Limitations

- The definition is relative to *honest training cost*, not to a complexity class or a reference
  problem — so it cannot be reduced to anything, only measured.
- Both published attacks exploit that the verifier checks local consistency, not global provenance.
- Fang et al.'s reduction of the needed assumptions to "open problems in learning theory" is unresolved
  and is where a hardness theorem would land.

## Quotes / Notable Passages

> "reduce to open problems in learning theory" — Fang et al., EuroS&P 2023, on what proof-of-learning
> security would require.
