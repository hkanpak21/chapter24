---
title: "Jailbreak Paradox: The Achilles' Heel of LLMs"
type: source
date_ingested: 2026-04-23
authors: [Abhinav Rao, Monojit Choudhury, Somak Aditya]
venue: "arXiv:2406.12702v2 (21 Jun 2024). The PDF carries the line 'Disclaimer: This work is currently a work in progress.' and names no venue."
year: 2024
tags: [llm-security, jailbreak, impossibility, paradox, relative-capabilities]
claim_quantifier: existential
antecedent: "That the space of LLMs has a most powerful member which can be jailbroken, where power is measured by accuracy and alignment over all of Sigma-star, and that the ordering by power is well founded enough for that maximum to exist. Neither is argued."
adversary_bound: "none — no party is bounded in compute, queries, or memory. The obstruction is a definitional maximality argument, not a hardness result."
date_verified: 2026-08-20
cls_target: outputs
cls_family: evade audit
cls_phase: test time
cls_access: black box
cls_write: read only
cls_frame: none
cls_party: none
cls_unit: none
cls_tightness: unstated
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed:
cls_evidence: absent
cls_evidence_src: "no bound in the Theorem 3.1 proof, Def 4.1/4.2, or the Theorem 4.1 proof"
cls_reason: "Verified against the flagged theorem-swap: Theorem 3.1 is the existential impossibility ('There will always exist LLMs for which there will be no strong jailbreak classifier') and Theorem 4.1 is the Pareto-dominance statement ('A pareto-dominant model can detect jailbreaks of a dominated model, but a dominated model can never detect all jailbreaks of a pareto-dominant model') — this page already carries the correct, unswapped content. Theorem 4.1's Pareto-dominance is a raw performance ordering over an arbitrary pair of models, not a designed resource restriction (no norm-ball, query budget, or algorithm-class definition is imposed on the detector), so party/unit/frame=none/none/none per Rule 2, matching the page's own verified adversary_bound field. family=evade audit since both paradoxes concern a classifier's (F_jb, or L-) ability to detect jailbreaks, not an attack construction."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper (RC24) gives an **impossibility-flavored argument** for jailbreak detection via a capability-based paradox: a *perfect* jailbreak detector for an aligned LLM would require a **strictly Pareto-dominant (more intelligent) LLM** than the target, yielding a paradox for super-aligned systems where no such detector exists.

Two main theorems, verbatim from the paper. The paraphrases an earlier version of this page gave for them were garbled and are corrected here, 2026-08-20; the two statements had been run together and their content exchanged.

- **Theorem 3.1**: "There will always exist LLMs for which there will be no strong jailbreak classifier, where a strong classifier is a classifier achieving arbitrarily good accuracy."
- **Theorem 4.1**: "A pareto-dominant model can detect jailbreaks of a dominated model, but a dominated model can never detect all jailbreaks of a pareto-dominant model."

Neither says what the earlier page said. Theorem 3.1 is existential over LLMs and says nothing about how capable a detector must be. Theorem 4.1 is the one that concerns relative capability, and its negative half is about a dominated model failing to detect all jailbreaks of a dominant one, not about a maximal model having no detector at all. The maximality claim appears in the paper's discussion, not in either theorem.

The result complements [Ball-Gluch-Goldwasser et al. 2025 (BGGKRR25)](filter-impossibility-ai-alignment.md) via a different route: BGGKRR25 uses **cryptographic hardness** (time-lock puzzles, OWFs, PKE); RC24 uses **relative-capabilities** (Pareto dominance in the space of LLM capabilities). BGGKRR25 is strictly stronger technically — it gives computational indistinguishability rather than merely "needs equal capability" — but RC24 is pedagogically valuable as a simpler argument accessible without cryptographic background.

Note: flagged as "work in progress" on arXiv; the formal proofs may evolve.

## Claim Boundary

- **Quantified over:** Theorem 3.1 is existential — it asserts that some LLMs admit no strong jailbreak classifier, not that all do. Theorem 4.1 ranges over pairs of models standing in a Pareto-dominance relation, where dominance means the dominant model performs better on at least one capability, that capability being identified with a subset S of Σ*.
- **Antecedent:** the proof of Theorem 3.1 assumes that G̃, "the most powerful LLM possible that can be jailbroken", exists, with power measured by accuracy and alignment over all sequences in Σ*. It then composes G with its own classifier, G′ = G ⊙ F_jb, argues G′ is more powerful than G̃, and takes the contradiction. The existence of that maximum, and the well-foundedness of the ordering that would make it meaningful, are assumed rather than argued. The proof also takes it without loss of generality that F_jb is a Transformer-based LLM. Theorem 4.1's proof turns on x and ⟨p; x⟩ falling inside or outside the capability set S and is a two-case argument in prose.
- **Which party is constrained:** neither, in any resource. This is a definitional maximality argument in the spirit of a diagonalization, not a computational hardness result. Nothing here bounds a detector's running time, sample budget, or memory, and nothing bounds the jailbreaker's.
- **Does not establish:** that detection is computationally hard, that it is undecidable, or that a detector must be a strictly more capable model. It also does not establish anything about approximate detection: Theorem 3.1 concerns classifiers "achieving arbitrarily good accuracy", so a detector with a fixed nontrivial error rate is untouched. The Tamil case study on Llama-2, Tamil-LLaMa, and GPT-4o is an illustration on three models and four jailbreaks, not a test of either theorem.
- **Abstract vs theorem:** the abstract says "it is impossible to construct a perfect jailbreak classifier". Theorem 3.1 proves only that some LLM lacks one. The universal reading of that sentence is not what is proved, and the paper is labelled a work in progress.

## Key Contributions

- **Capability-based jailbreak detection impossibility**: formalized via Pareto dominance in LLM capability space.
- **Theorem 3.1**: some LLM admits no jailbreak classifier of arbitrarily good accuracy.
- **Theorem 4.1**: a dominated model cannot detect all jailbreaks of a Pareto-dominant one.
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

> _Not a quotation from the paper. This characterization was carried over from a secondary survey artifact during an earlier ingest and was wrongly presented in quotation marks. Retained unquoted, corrected 2026-08-20; verify against the primary source before citing._
>
> A perfect jailbreak detector for an aligned LLM would require a strictly Pareto-dominant (more intelligent) LLM than the target, yielding a paradox for super-aligned systems where no such detector exists.

The paper's own statement of the two paradoxes, verbatim from the abstract:

> "We introduce two paradoxes concerning jailbreak of foundation models: First, it is impossible to construct a perfect jailbreak classifier, and second, a weaker model cannot consistently detect whether a stronger (in a pareto-dominant sense) model is jailbroken or not."
