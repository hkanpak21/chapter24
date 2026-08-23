---
title: "Cryptographic Backdoor for Neural Networks: Boon and Bane"
type: source
date_ingested: 2026-04-23
authors: [Anh Tu Ngo, Anupam Chattopadhyay, Subhamoy Maitra]
venue: "arXiv:2509.20714v1 (25 Sep 2025). The PDF is typeset in the IEEE journal template; no venue is named in it, so the 'journal submission' attribution is unconfirmed from the primary source."
year: 2025
tags: [backdoor, cryptography, watermarking, authentication, ip-protection, defensive-backdoors]
claim_quantifier: empirical
antecedent: "existence of strongly unforgeable digital signature schemes, for the non-replicability result carried over from Goldwasser et al. The three defensive protocols are argued, not proved; the authors state that the proofs relating to the defence need further study."
adversary_bound: "black-box access to the network, for the three defensive protocols. The backdoor-enabled adversarial attack is stated to be unpreventable under the standard assumptions."
date_verified: 2026-08-20
cls_target: outputs
cls_family: backdoor
cls_phase: post hoc
cls_access: black box
cls_write: read only
cls_frame: compute
cls_party: attacker
cls_unit: queries
cls_tightness: budget
cls_baseline: n/a
cls_second_party: none
cls_second_notion: time
cls_assessed: implicit
cls_evidence: "Consider a real-world q-query admissible adversary Areal who gets access backdoored model h̃. Areal makes q queries to the ACTIVATE(·, sk) oracle"
cls_evidence_src: Thm II.1, proof
cls_reason: "Classified on Theorem II.1, the paper's only theorem environment, per the wiki's own note that the three defensive protocols are argued rather than proved, even though the abstract's 'main contribution' language foregrounds the defensive protocols. family=backdoor rather than forge, since the object under study is a planted cryptographic backdoor's (non-)replicability, though the reduction mechanism is literally signature forgery. second_notion=time/assessed=implicit records the accompanying PPT bound on the forger, which the proof states only as 'computationally infeasible' and never as a named parameter of the theorem, alongside the theorem's own explicit q-query budget."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper (NCM25) instantiates [Goldwasser-Kim-Vaikuntanathan-Zamir 2022](planting-undetectable-backdoors.md) signature-based backdoors as ***defensive* primitives** rather than attacks: provably-robust neural-network watermarking, user authentication, and IP-tracking protocols that resist adversaries with black-box access.

The key conceptual contribution: **the Goldwasser et al. framework is bidirectional** — the same cryptographic construction that makes backdoor *attacks* undetectable makes certain *defensive* protocols unforgeable. A signature-based backdoor can be used:
- **As an attack** (planted by malicious provider): the attacker alone can trigger the hidden behavior using their signing key.
- **As a defense** (planted by the legitimate owner): the owner alone can prove model ownership by demonstrating backdoor triggering; unauthorized copies lack the signing key.

The paper formalizes three defensive applications:
1. **NN watermarking**: embed a signature-based trigger that only the owner can activate; proves model provenance.
2. **User authentication**: each authorized user has a signing key; the model responds correctly only to signed queries.
3. **IP tracking**: backdoor-based tracking of unauthorised sharing of the network. **Correction, 2026-08-20:** this line previously read "fingerprints that survive fine-tuning and model distillation". The paper claims survival under fine-tuning, because the watermark is independent of the model's parameters, and states explicitly that the watermark "does not protect the model from distillation or extraction".

The cryptographic circuit is connected **in parallel** with the network rather than woven into its weights, which is why the watermark is independent of the model parameters and so survives fine-tuning.

## Claim Boundary

- **Quantified over:** three constructed protocols plus one attack instantiation, evaluated empirically on standard architectures. The single theorem carried over from the cryptographic side, Theorem II.1, is universal over training procedures: assuming strongly unforgeable digital signatures exist, for every `TRAIN` there is a non-replicable backdoor. The defensive claims are not of that form.
- **Antecedent:** existence of strongly unforgeable digital signature schemes. The paper notes that post-quantum primitives can be substituted, and its implementation uses Dilithium. The defensive protocols rest on the same signature unforgeability, but the authors say in the abstract that "the proofs related to the defense need further studies", so the word "provably" in the paper's own section headings should not be read as a completed security proof.
- **Which party is constrained:** the *adversary against the defensive protocols*, which is restricted to **black-box** access to the network. The attack side is the mirror image: the backdoor-enabled adversarial attack is stated to be unpreventable under the standard assumptions.
- **Does not establish:** that the defensive backdoor resists model extraction. The paper states the opposite for watermarking: the watermark "does not protect the model from distillation or extraction", and proposes query limits or the authentication mechanism as a separate remedy. It also does not establish white-box security for the defensive protocols.
- **Abstract vs theorem:** the abstract's "all these instantiated practical protocol implementations are provably robust" is stronger than the body supports, and the same abstract concedes two sentences later that the defence-side proofs need further study.

## Key Contributions

- **Bidirectional use of the Goldwasser et al. construction**: the same cryptographic backdoor serves as attack and as defence.
- **The attack instantiation**: extends the black-box undetectable backdoor of Goldwasser et al. to image classification, which the authors describe as the first direct link from a cryptographic backdoor to an adversarial attack.
- **Signature-based NN watermarking**: the cryptographic circuit is connected in parallel with the network, so the watermark does not degrade under fine-tuning.
- **User authentication protocols**: model-level access control via signed queries.
- **IP tracking**: tracking unauthorised sharing of the network.
- **Empirical study**: effectiveness and computational overhead measured on standard architectures, which the authors note the underlying theoretical work did not do.
- **Post-quantum instantiation**: the construction can be built on post-quantum primitives; the implementation uses Dilithium.
- **Correction, 2026-08-20:** the bullet "IP tracking: fingerprinting resistant to fine-tuning and distillation" is corrected above; the paper states the watermark does not protect against distillation or extraction.

## Key Definitions / Theorems

**Theorem II.1**, the only theorem environment in the paper, restates the non-replicability half of the cryptographic backdoor: assuming that strongly unforgeable digital signature schemes exist, for every procedure `TRAIN` there exists a backdoor `(BACKDOOR, ACTIVATE)` which is non-replicable. The proof is a reduction against a `q`-query admissible adversary with access to the backdoored model. The three defensive protocols are presented as constructions with security arguments rather than as theorems.

## Connections

- Source: [Planting Undetectable Backdoors (GKVZ22)](planting-undetectable-backdoors.md) — foundational; NCM25 inverts offense-to-defense.
- Source: [Unelicitable Backdoors (DGM+24)](unelicitable-backdoors-lms.md) — LM attack; NCM25's defensive version for LMs.
- Source: [Oblivious Defense (GSVV25)](oblivious-defense-backdoor-removal.md) — shows backdoors may be mitigated; NCM25 shows defensive backdoors are intentional.
- Source: [Backdoor Defense, Learnability, Obfuscation (CHLX25)](backdoor-defense-learnability-obfuscation.md) — defendability; NCM25 is the defensive-instrumentation angle.
- Concept: [Undetectable Backdoors](../concepts/undetectable-backdoors.md).
- Concept: [Pseudorandomness](../concepts/pseudorandomness.md) — digital signatures.
- Concept: [One-Way Functions](../concepts/one-way-functions.md).

## Quotes / Notable Passages

> _Not a quotation from the paper. This characterization was carried over from a secondary survey artifact during an earlier ingest and was wrongly presented in quotation marks. Retained unquoted, corrected 2026-08-20; verify against the primary source before citing._
>
> The same cryptographic construction that makes attacks undetectable makes certain defensive protocols unforgeable.

Verified against `raw/NCM25_CryptoBackdoorBoonBane.pdf` on 2026-08-20.

> "The protocols for watermarking, authentication and IP tracking resist an adversary with black-box access to the NN, whereas the backdoor-enabled adversarial attack is impossible to prevent under the standard assumptions."

— abstract, on which access model each side of the paper assumes.

> "While the theoretical tools used for our attack is mostly in line with the Goldwasser et. al. ideas, the proofs related to the defense need further studies."

— abstract, the authors' own limit on the word "provably".
