---
title: A Framework for Cryptographic Verifiability of End-to-End AI Pipelines
type: source
date_ingested: 2026-04-12
authors: [Kar Balan, Robert Learney, Tim Wood]
venue: "IWSPA '25 (ACM International Workshop on Security and Privacy Analytics), 6 June 2025, Pittsburgh, stated in the PDF's own footer (arXiv:2503.22573v1, 28 Mar 2025)"
year: 2025
tags: [cryptography, zero-knowledge-proofs, ml-verification, commitments, formal-models, compliance]
claim_quantifier: empirical
antecedent: "none. No theorem is stated, so nothing rests on a hypothesis."
adversary_bound: "none stated. The paper surveys proof systems whose soundness is computational by construction, but it defines no adversary and proves nothing about one."
date_verified: 2026-08-20
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: none
cls_party: none
cls_unit: none
cls_tightness: unstated
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed:
cls_evidence: absent
cls_evidence_src: "no adversary, game, or advantage defined anywhere in the paper; §2 defines ZKP/signature soundness generically ('computationally infeasible for an adversary'; 'computationally-bounded adversary'), background only, not a threat model of the paper's own; wiki Claim Boundary confirms 'none is modelled'"
cls_reason: "Framework/gap-analysis survey, no theorem, no formal security game; front matter's own adversary_bound field already states this. All attack-scenario and adversary-assumption fields are none/unstated/n/a per rule 2."
cls_prov: P
cls_date: 2026-08-22
---

## Summary
This is a **framework and gap-analysis paper**, not a theorem-proving paper. Balan (University of Surrey, DECaDE), Learney and Wood (Digital Catapult) propose a six-stage cryptographic verifiability framework for AI pipelines — (1) verification of raw dataset, (2) extraction and analysis, (3) model training, (4) model evaluation, (5) model inference, (6) machine unlearning — and survey which cryptographic tools are deployable at each stage. The organising requirement is that each process be shown to have run honestly *and* that the inputs of each process be the outputs of the previous one.

The paper's formal content is limited to standard definitions. The novelty is the mapping exercise, together with the observation that no work has yet achieved a full end-to-end verifiable pipeline. Its stated conclusion is that cryptographic tools must be efficiently **linkable** across processes, not merely efficient in isolation.

**Correction, 2026-08-20.** Three tools previously named here are absent from the paper: `zkLLM`, `snarkGPT` and `zkPoUL`. The figure "zkLLM: 803s per 13B token" does not appear in it either, and neither does "Bulletproofs" or "Art. 17". The claim that "ZKPoT and ZKPoI use incompatible polynomial representations of models" also overstates: the paper says the two kinds of scheme "often use different, sometimes bespoke proof systems that are not directly compatible, e.g. quantisation is done differently", calls this "not an insurmountable challenge", and names ZKAUDIT as a system that already links the two directly. Tools that are in the paper: C2PA, ZKAUDIT, KAIZEN, zkDL, zkCNN, DECORAIT, FairProof, vTune, and Eisenhofer et al.

## Claim Boundary

- **Quantified over:** the survey covers the tools its authors reviewed as of early 2025. There is no universal claim and no theorem. The one general statement — that no work has yet achieved a full end-to-end verifiable pipeline — is qualified by the authors as "to the authors' knowledge".
- **Antecedent:** none, since nothing is proved.
- **Which party is constrained:** none is modelled. The proof systems surveyed are computationally sound, so a prover is implicitly polynomial-time bounded, but the paper defines no adversary, no game and no advantage. A reader looking here for a formal threat model will not find one.
- **Does not establish:** any impossibility, any soundness guarantee for a composed pipeline, or any efficiency claim of its own. It also does not establish that ZKPs hide what a reader might assume: the paper notes that ZKPoTs do not hide the training process, since it is encoded in the public proof or verification algorithm, and that in ZKPoI the model architecture is the proof circuit and so is publicly accessible.
- **Abstract vs theorem:** there is no theorem. The abstract is a description of a framework and reads as one.

**Flag to wiki**: this paper is less formal than its framing suggests. It is a systems and policy survey with cryptographic flavour, not an impossibility or verification theorem. Useful as an entry point to ZK-for-ML tooling and for EU AI Act compliance context, but it contributes no new formal security definitions or proofs.

## Key Contributions
- Six-stage framework for cryptographic verifiability across the AI lifecycle, with the linking requirement between consecutive stages as the organising idea.
- Categorisation of existing tools by pipeline stage: C2PA and DECORAIT for provenance, ZKAUDIT and KAIZEN for training, zkDL and zkCNN for inference, FairProof for fairness certificates, vTune for fine-tuning, Eisenhofer et al. for unlearning. **Correction, 2026-08-20:** zkLLM, ZKPoUL and snarkGPT were listed here and are not in the paper.
- Gap analysis: to the authors' knowledge no work has achieved a full end-to-end verifiable pipeline, and ZKPoI and ZKPoT schemes often use different, sometimes bespoke proof systems that are not directly compatible — though ZKAUDIT already links them, showing feasibility.
- The observation that ZKPoI takes an *arithmetised* model as input, so the user must trust that the circuit honestly represents the model; linking ZKPoI to ZKPoT is what closes that gap.
- Regulatory framing around the EU AI Act, GDPR and CCPA. **Correction, 2026-08-20:** the specific citation "GDPR Art. 17" was here and does not appear in the paper.

## Key Definitions / Theorems
No new theorems. Standard definitions invoked:
- **ZKP (completeness / soundness / zero-knowledge)** — interactive proof between prover P and verifier V.
- **Commitment (hiding / binding)**.
- **Digital signature (EUF-CMA)**.
- Classes discussed: zk-SNARK, zk-STARK, NIZK. **Correction, 2026-08-20:** Bulletproofs was listed here and does not appear in the paper.

## Connections
- ZK for ML inference connects to the broader program of [verifiable computation](../concepts/verifiable-computation.md) applied to learning.
- Related to [extending-formalism-cryptography-ai](extending-formalism-cryptography-ai.md) (Villa et al.) which provides a cryptographic formalism for AI more broadly.
- Related to [formalizing-llm-agent-security](formalizing-llm-agent-security.md) (AIOracle) for game-based security definitions.
- Authors: [Kar Balan](../entities/kar-balan.md), [Robert Learney](../entities/robert-learney.md), [Tim Wood](../entities/tim-wood.md).

## Open Questions / Limitations
- No unified cryptographic "AI pipeline proof" primitive; the authors motivate but do not construct one.
- ZK-SNARK efficiency for modern LLM-scale models is an open engineering + theory problem.
- No formal soundness definition tying multi-stage proofs; linking is identified as a gap.
- No treatment of privacy leakage *from* a ZKP about a model (side-channel through proof structure).

## Quotes / Notable Passages

> _Not verbatim. Checked against `raw/BLW25_ZKMLVerification.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> ZKPs do not necessarily hide algorithms used … and so a ZKPoT doesn't hide implementation details if the representation of the model differs, for example, from that of a ZKPoI.

> _Not verbatim. Checked against `raw/BLW25_ZKMLVerification.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> We propose a framework for end-to-end verifiable AI pipelines, identifying key components and analyzing existing cryptographic tools … [and] identify the gaps and challenges.

Verified against `raw/BLW25_ZKMLVerification.pdf` on 2026-08-20.

> "In this paper, we propose a framework for complete verifiable AI pipelines, identifying key components and analyzing existing cryptographic approaches that contribute to verifiability across different stages of the AI lifecycle, from data sourcing to training, inference, and unlearning."

— abstract. The paper says "complete", not "end-to-end", and "approaches", not "tools".

> "ZKPs do not necessarily hide algorithms such as the training process, so regulators may need to verify proofs of proprietary models on behalf of users to allow service providers to keep their model architectures private while giving strong cryptographic security guarantees."

— §5, on what zero knowledge does not buy.

> "ZKPoTs do not hide the training process (which is often a trade secret) since it is essentially encoded in the (public) proof and/or verification algorithm."

— §4.2, the same point stated sharply.

> "while ZKPoI ensures that sensitive information like model weights and input data remain private, the model architecture itself is the ZKP circuit, and is thus publicly accessible."

— §4.3, the inference-side counterpart.

> "Our findings underscore the importance of ongoing research to develop cryptographic tools that are not only efficient for isolated AI processes, but that are efficiently 'linkable' across different processes within the AI pipeline, to support the development of end-to-end verifiable AI technologies."

— abstract, the paper's own conclusion.
