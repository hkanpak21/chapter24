---
title: "Extending the Formalism and Theoretical Foundations of Cryptography to AI"
type: source
date_ingested: 2026-04-12
authors: [Federico Villa, F. Betül Durak, Tadayoshi Kohno, Tapdig Maharramli, Franziska Roesner]
venue: "arXiv:2603.02590v1 [cs.CR], 3 Mar 2026, confirmed from the PDF's own stamp"
year: 2026
tags: [cryptography, adversarial-ml, agentic-systems, formal-models, access-control, llm-security, confidentiality, integrity, availability]
claim_quantifier: conditional
antecedent: "for the modular composition theorem, that the two component oracles are themselves complete and ATK-ψ-secure. For the confidentiality-versus-utility result, that the AIOracle is DPD-secure, where DPD is the differentially private distinguishability game the paper takes from prior work. No cryptographic hardness assumption is instantiated anywhere; the paper supplies definitions and reductions, not constructions."
adversary_bound: "PPT, with capabilities named by a set ATK drawn from {see_model, inject_learn, inject_infer, black_box}"
date_verified: 2026-08-20
cls_target: train data
cls_family: membership
cls_phase: train time
cls_access: white box
cls_write: corpus
cls_frame: compute
cls_party: attacker
cls_unit: time
cls_tightness: poly
cls_baseline: stated
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "An AIOracle for φ is ε-ATK-ψ-secure if for any PPT adversary A, Adv ≤ ε in the game in Figure 6."
cls_evidence_src: Def 3
cls_reason: "Classified on the paper's own formal results (the dual-construction composition theorem and the confidentiality-vs-utility tension), not on the §7 filtering impossibility, which belongs to Ball et al., is existential, and one of its theorems needs a shared secret key. Of the paper's own two results, the tension is centred over the composition theorem because the abstract states it first ('we show that existing approaches to confidentiality of training data fundamentally conflict with completeness') before the modular-decomposition claim; the composition theorem (Thm 1) is itself target-less and would classify as target=none/family=none if centred instead, which is noted as the alternative reading. family=membership and target=train data follow the paper's own words for the DPD game: 'This perfectly models the membership inference attack from subsection D.2,' and DPD 'treats all data elements from corpus as confidential.' phase=train time and write=corpus because the DPD adversary itself constructs corpus′ (all but the one challenge element z_b) before LEARN runs, not merely queries a fixed corpus. access=white box: step 6 of Algorithm 2 (DPD) hands the adversary A the trained 'model' object directly, matching the paper's 'see_model' capability. party/unit/tightness taken from Definition 3, the general ATK-ψ-secure template DPD instantiates: PPT adversary ⇒ unit=time, tightness=poly. baseline=stated: the DPD advantage analysis in Appendix E.1 writes the success probability as 1/2 + ε_i (the paper's fraction glyphs are split by pdftotext extraction but the value is 1/2, confirmed against the PDF)."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper applies cryptographic methodology — rigorous formal definitions, adversarial models, and reduction-based security proofs — to the security of agentic LLM systems. The central contribution is the **AIOracle** abstraction, a formal model of an agentic AI system with two phases (LEARN and INFER), and a security game framework that simultaneously captures confidentiality, integrity, and availability within a single model.

The authors first survey the landscape of attacks on LLMs (constructing a multi-dimensional taxonomy), then develop formal treatments of access control, helpfulness, and harmlessness. They show that the existing approach to confidentiality of training data conflicts with completeness: a **DPD**-secure AIOracle cannot distinguish a cat from a dog, which undermines its utility. They also formalise a **modular dual construction** that decomposes an AIOracle into a *creative* (CAIO) and a *boring* (BAIO) component, and prove its soundness.

**Correction, 2026-08-20.** This page wrote the confidentiality game's name as "DPP" in four places. The paper calls it **DPD**, for *differentially private distinguishability* (Algorithm 2, Figure 4), and takes the model from references [26, 27]. The string "DPP" does not occur in the paper. One name for one thing: DPD is the paper's.

The paper analyses four existing agentic frameworks (FIDES, Progent, Conseca, Controlvalve) through the AIOracle lens.

## Claim Boundary

- **Quantified over:** definitions and one composition theorem, not systems. Theorem 1 is universal over pairs of component oracles satisfying its hypotheses. The confidentiality-versus-utility result is about the specific DPD model of confidentiality, so it is a statement about that definition, not about privacy-preserving machine learning in general.
- **Antecedent:** for Theorem 1, that BAIO and CAIO are each complete and ATK-ψ-secure for their own predicates. For the tension result, that the AIOracle is DPD-secure, where DPD treats **all** data elements of the corpus as confidential — the paper itself calls this "an overkill" in practice and lists three ways to relax it. No cryptographic hardness assumption is instantiated anywhere; the paper offers a formalism, not constructions.
- **Which party is constrained:** the *adversary*, to probabilistic polynomial time, with its capabilities named by a set `ATK ⊆ {see_model, inject_learn, inject_infer, black_box}`. Completeness (Definition 2) also quantifies over PPT algorithms `B`, though that party is not adversarial. The bound is the standard cryptographic one; nothing finer-grained is priced.
- **Does not establish:** that any deployed agentic system is secure or insecure; that DPD is the right confidentiality notion; or that a secure AIOracle can be built. The paper's own limitation, stated in the abstract's framing, is that it supplies the formalism needed to prove security reductions, not the reductions for a real system.
- **Abstract vs theorem:** the abstract says existing approaches to training-data confidentiality "fundamentally conflict with completeness". The body's claim is narrower: the tension is with the DPD model of confidentiality as it stands, and the paper immediately sketches relaxations that avoid it.

## Key Contributions

- **AIOracle abstraction**: Formal model of an r-round agentic LM system with algorithms `(GENERATE_DATA, LEARN_{1..r}, INFER)`. Separates the LEARN phase (training, fine-tuning) from the INFER phase (inference, tool calls). Unifies prior ad-hoc system descriptions.
- **Multi-dimensional attack taxonomy**: Classifies LLM attacks along five axes — attack vector (data-based / prompt-based), attack phase (LEARN / INFER), adversarial knowledge (white-box / black-box / gray-box), security goals (confidentiality / integrity / availability), and attack persistence (transient / persistent). Covers: prompt injection, jailbreak, data exfiltration, membership inference, data poisoning, backdoor.
- **Security game framework**: Captures all three security objectives (C, I, A) in a single game parameterized by adversary capability set ATK. Adversary wins if predicate φ(prompt, context, result) is violated.
- **Confidentiality vs. utility tension**: a DPD-secure AIOracle cannot distinguish a cat from a dog, which undermines its utility; the claim is shown formally in the paper's subsection E.1. The tension comes from DPD treating every data element of the corpus as confidential, which the paper calls an overkill in practice.
- **Modular dual construction (Theorem 1)**: if BAIO and CAIO are complete and ATK-ψ-secure for `Ψ = Ψ₁` and `Ψ = Ψ₂`, and for `φ′₁` and `φ₂` respectively, then the dual construction is complete and ATK-ψ for `Ψ = Ψ₁ ∨ Ψ₂` and for `φ = φ₁ ∧ φ₂`. **Correction, 2026-08-20:** this page previously gave the conjunction in one place and the disjunction in another, as if they were rival readings. They are both in the theorem, applied to different objects: the adversary predicate composes as a disjunction, the policy predicate as a conjunction.
- **Framework analysis**: Contextualizes FIDES (taint tracking / information flow), Progent (tool access control), Conseca (context-aware policy generation), and Controlvalve (CFG + LM judge) within the AIOracle model.

## Key Definitions / Theorems

**AIOracle (Definition 1)**: An r-round learning phase defined by `2r+1` algorithms `((GENERATE_DATA_i, LEARN_i)_{i=1..r}, INFER)`.

**Completeness (Definition 2)**: An AIOracle is φ-complete if for any PPT algorithm B, the security game returns 1 with probability at least p. The "adversary" in the completeness game does not interfere — it measures correct behavior in the absence of an attack.

**ATK-ψ-secure AIOracle (Definition 3)**: an AIOracle for φ is ε-ATK-ψ-secure if for any PPT adversary A, `Adv ≤ ε` in the game of Figure 6. **Correction, 2026-08-20:** this page previously gave the bound as `≤ (1−p)` and described the advantage as defined relative to the completeness baseline; Definition 3 states `Adv ≤ ε`.

**ATK set**: captures adversary capabilities — `see_model` for white-box access, `inject_learn` for data-based attacks, `inject_infer` for prompt-based attacks, `black_box` for query-only access. Set in Algorithm 4.

**Dual Construction Theorem (Theorem 1)**: as stated in the contributions above; `Ψ` composes disjunctively and `φ` conjunctively. Proof sketch in subsection E.2.

**DPD game (Algorithm 2, Figure 4)**: differentially private distinguishability, taken from references [26, 27], used as the paper's typical example of a confidentiality definition.

## Connections

- [AIOracle Framework](../concepts/aioracle-framework.md)
- [Attack Taxonomy for LLMs](../concepts/attack-taxonomy-llms.md)
- [Federico Villa](../entities/federico-villa.md)
- [Tadayoshi Kohno](../entities/tadayoshi-kohno.md)
- [Franziska Roesner](../entities/franziska-roesner.md)
- [F. Betül Durak](../entities/betul-durak.md)
- Relates to [Evasion Attacks](../concepts/evasion-attacks.md) and [Poisoning Attacks](../concepts/poisoning-attacks.md) — this paper extends those concepts to the agentic LLM setting

## Open Questions / Limitations

- The framework focuses on formal security definitions; it does not provide efficient constructions of secure AIOracles.
- Completeness and security may be in tension beyond the DPD case — further impossibility results are needed. **Correction, 2026-08-20:** "DPP" here was the same misspelling of DPD corrected above.
- The ATK model is grey-box (restricted white-box) — fully adaptive adversaries with model internals are not fully captured.
- The policy predicate φ (defining what is "harmless") must be manually specified; no general method for deriving φ is given.
- Empirical validation of the taxonomy against real-world LLM attack deployments is left to future work.

## Quotes / Notable Passages

> _Not verbatim. Checked against `raw/VDKMR26_CryptoToAI.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> Our studies suggest that if we were to design a secure system with measurable security, then we might want to use a modular approach to break the problem into sub-problems and let the composition on different modules complete the design.

> _Not verbatim. Checked against `raw/VDKMR26_CryptoToAI.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> The tension is that if we have a DPP-secure AIOracle (i.e. the classifier), then AIOracle cannot distinguish a cat from a dog which undermines the utility of an AIOracle.

Verified against `raw/VDKMR26_CryptoToAI.pdf` on 2026-08-20. Both paraphrases differ from the paper by one word each. The first silently corrects the paper's grammar; the second renames the security notion, which is the more damaging change.

> "Our studies suggests that if we were to design a secure system with measurable security, then we might want to use a modular approach to break the problem into sub-problems and let the composition on different modules complete the design. Our studies show that this natural approach with the relevant formalism is needed to prove security reductions."

— abstract, with the paper's own "suggests".

> "The tension is that if we have a DPD-secure AIOracle (i.e. the classifier), then AIOracle cannot distinguish a cat from a dog which undermines the utility of an AIOracle. We show this claim formally in subsection E.1."

— §6, with the notion's correct name.

> "The tension between confidentiality and utility comes from the fact that DPD security treats all data elements from corpus as confidential. In practice, it is an overkill because we do not necessarily need and want to protect all data elements."

— §6, the authors' own bound on how far the tension result reaches.
