---
title: "Jailbreak Paradox: The Achilles' Heel of LLMs"
type: source
date_ingested: 2026-04-23
authors: [Abhinav Rao, Monojit Choudhury, et al.]
venue: "arXiv:2406.12702 (Jun 2024; work-in-progress)"
year: 2024
tags: [llm-security, jailbreak, impossibility, paradox, relative-capabilities]
---

## Summary

This paper (RC24) gives an **impossibility-flavored argument** for jailbreak detection via a capability-based paradox: a *perfect* jailbreak detector for an aligned LLM would require a **strictly Pareto-dominant (more intelligent) LLM** than the target, yielding a paradox for super-aligned systems where no such detector exists.

Two main theorems:
- **Theorem 3.1**: Detecting jailbreaks perfectly requires a detector at least as capable as the LLM being protected.
- **Theorem 4.1**: For super-aligned LLMs that are maximally capable in their domain, no strictly-more-capable detector can exist, hence no perfect detector.

The result complements [Ball-Gluch-Goldwasser et al. 2025 (BGGKRR25)](filter-impossibility-ai-alignment.md) via a different route: BGGKRR25 uses **cryptographic hardness** (time-lock puzzles, OWFs, PKE); RC24 uses **relative-capabilities** (Pareto dominance in the space of LLM capabilities). BGGKRR25 is strictly stronger technically — it gives computational indistinguishability rather than merely "needs equal capability" — but RC24 is pedagogically valuable as a simpler argument accessible without cryptographic background.

Note: flagged as "work in progress" on arXiv; the formal proofs may evolve.

## Key Contributions

- **Capability-based jailbreak detection impossibility**: formalized via Pareto dominance in LLM capability space.
- **Theorem 3.1**: detector must be at least as capable as detected LLM.
- **Theorem 4.1**: no detector for maximally-capable LLMs.
- **Pedagogical foundation**: accessible impossibility argument complementing the cryptographic BGGKRR25.

## Connections

- Source: [Filter Impossibility (BGGKRR25)](filter-impossibility-ai-alignment.md) — strictly stronger cryptographic-hardness version; RC24 is the capability-theoretic counterpart.
- Source: [Immune (Ghosal et al. 2024)](immune-rlhf-jailbreak-defense.md) — narrower impossibility for RLHF; RC24 is more general (any detector).
- Source: [MaxMin-RLHF (Chakraborty et al.)](maxmin-rlhf-impossibility.md) — impossibility for single-reward RLHF.
- Source: [Universal Jailbreak Backdoors from Poisoned RLHF (Rando-Tramèr 2023)](universal-jailbreak-rlhf-backdoors.md) — practical demonstration.

## Open Questions / Limitations

- **Work-in-progress**: formal proofs may evolve.
- **Pareto dominance definition**: depends on how "capability" is measured; different measures yield different impossibilities.
- **Imperfect detection acceptable**: RC24's impossibility is for *perfect* detection; approximate detection may still be feasible.

## Quotes / Notable Passages

> "A perfect jailbreak detector for an aligned LLM would require a strictly Pareto-dominant (more intelligent) LLM than the target, yielding a paradox for super-aligned systems where no such detector exists."
