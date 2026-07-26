---
title: Towards a Re-evaluation of Data Forging Attacks in Practice
type: source
date_ingested: 2026-07-26
authors: [Mohamed Suliman, Anisa Halimi, Swanand Kadhe, Nathalie Baracaldo, Douglas Leith]
venue: USENIX Security 2025
year: 2025
tags: [adversarial-ml, complexity theory, reconstruction, poisoning-attacks, hardness-reductions]
---

> **Provenance.** Built from a verified sweep; the conjecture below is verbatim from the paper's HTML.
> **Read this in full first.** It carries the single best-defined open problem found in the
> 2026-07 sweeps.

## Summary

*Data forging* asks whether a party can produce a different mini-batch that yields the same gradient
update — thereby "proving" it trained on data it did not use. The attack matters for unlearning
verification and for proof-of-training claims.

The paper's re-evaluation is largely negative about forging *in practice*, and in the course of it the
authors state the obstruction precisely: the set of gradient-equivalent mini-batches is infinite, but
the batches that also satisfy the **domain constraints** — pixel values in `[0,255]`, one-hot labels —
are what an attacker actually needs, and no efficient technique for finding those is known. They
conjecture there may be none, even for logistic regression.

**That conjecture is the surviving open problem for the programme's reconstruction corner.** It is
stated and abandoned in a single paragraph, which makes it a target that cannot be scooped by
reframing.

## Key Contributions

- Empirical re-evaluation showing forging is substantially harder in practice than prior work implied.
- **Proposition 1**: at batch size 1, gradient equality forces `x = x′` — the fiber is a singleton.
- The explicit statement that unconstrained fiber size and constrained fiber navigability come apart.

## Key Definitions / Theorems

- **The conjecture (verbatim):** *"Of the infinite, distinct, solutions that may exist, there are
  currently no known efficient techniques for finding solutions that correspond to a mini-batch that
  falls within the allowed domain 𝒳×𝒴."* … *"finding those that are within the allowed domain e.g.
  pixel values between 0−255 and one hot labels is a non-trivial task, and one that **we conjecture may
  be computationally infeasible**, even for relatively simple linear models such as logistic
  regression."*
- **Proposition 1**: batch size 1 ⟹ gradient equality forces identity of the example.

## Connections

- **The programme's designated first theorem.** Prove or refute this. Compare
  [Jagielski et al. USENIX Sec'20](jagielski-model-extraction.md), which proved NP-hardness for the
  *evaluation* map (functional equivalence of two weight vectors) — the *training*-map version is open.
- Predecessor: Suliman & Leith, *Data Forging Is Harder Than You Think*, Private ML @ ICLR 2024.
- Forging as an attack on unlearning: Thudi et al., USENIX Security 2022 (arXiv:2110.11891);
  Kong–Roy Chowdhury–Chaudhuri, arXiv:2303.03648 — efficient proofs of repudiation defeating MIA.
- Unforgeability certificates: Baluta–Nikolić–Jain–Aggarwal–Saxena, ACM CCS 2023 — efficiently checkable
  conditions under which a checkpoint's fiber is a singleton.
- Concept: [fiber-of-the-training-map](../concepts/fiber-of-the-training-map.md).

## Open Questions / Limitations

- **The conjecture itself is unproved.** No hardness assumption is named, no reference problem
  identified, no adversary class fixed. All three are the work.
- Domain constraints are what make it plausible — the unconstrained problem is linear-algebraic and
  easy. So the hardness, if real, comes from the *intersection* of a linear condition with a box
  constraint, which is the shape of an integer-programming or lattice problem rather than a learning one.
- Stated for gradient equality on a single step, not for the full training map over many steps.

## Quotes / Notable Passages

> "we conjecture may be computationally infeasible, even for relatively simple linear models such as
> logistic regression"
