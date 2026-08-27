---
title: "Planting Undetectable Backdoors in Machine Learning Models"
type: source
date_ingested: 2026-04-12
authors: [Shafi Goldwasser, Michael P. Kim, Vinod Vaikuntanathan, Or Zamir]
venue: "arXiv:2204.06974v2 (9 Nov 2024). The FOCS 2022 attribution carried on this page is not stated in the PDF in `raw/`; the only FOCS mentions in it are bibliography entries."
year: 2022
tags: [cryptography, adversarial-ml, poisoning-attacks, backdoor, one-way-functions, hardness-reductions, formal-models]
claim_quantifier: existential
antecedent: "one-way functions exist (black-box result, Theorem 2.1); hardness of worst-case lattice problems via Continuous LWE (white-box result for Random Fourier Features, Theorem 2.2); hardness of Sparse PCA (white-box result for random ReLU networks). All are standard."
adversary_bound: "PPT distinguisher — with oracle access to the honest and backdoored models in the black-box theorem, with the complete network description and the training data in the white-box theorems"
date_verified: 2026-08-20
cls_target: parameters
cls_family: backdoor
cls_phase: train time
cls_access: black box
cls_write: model
cls_frame: compute
cls_party: auditor
cls_unit: time
cls_tightness: poly
cls_baseline: stated
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: absent
cls_evidence_src: "classified by hand in the first batch, before the evidence requirement was added to the brief"
cls_reason: "Hand-classified 2026-08-22 against codebook revision 2, then migrated through revisions 3 to 5. Carries no verbatim evidence quote, unlike the delegated rows."
cls_prov: hand
cls_date: 2026-08-22
---

## Summary

Under standard cryptographic assumptions a malicious learner can plant a backdoor into a classifier so that the backdoored model cannot be told apart from an honestly trained one by any computationally bounded observer. The consequence for delegated training is that no efficient procedure certifies that a model was trained honestly.

Two constructions are given, with **incomparable** guarantees. The first uses **digital signatures** and works for *any* training procedure, but its undetectability is **black-box**: the distinguisher has query access only. The second replaces the random features of a **Random Fourier Features** learner with a Continuous LWE distribution and is **white-box** undetectable — the distinguisher sees all the weights — but it holds only for that specific training paradigm. A third white-box construction covers random ReLU networks under the hardness of Sparse PCA. A complementary **persistence theorem** shows that a network can be transformed so that gradient descent leaves it unchanged.

**Correction, 2026-08-20.** This summary previously read that "any ML model can be backdoored in a way that is computationally indistinguishable from an honest model — even to an auditor with full white-box access", merging the two theorems into one. The paper does not prove that. The result that holds for any model is black-box; the white-box results hold for two specific learning paradigms. The paper's own comparison table is reproduced by [KKO+24](io-undetectable-backdoors-nn.md), which states that white-box undetectability for arbitrary training procedures is "unlikely".

## Claim Boundary

- **Quantified over:** Theorem 2.1 is universal over training procedures, but only for **black-box** undetectability and only over PPT distinguishers with oracle access. Theorem 2.2 is existential in the training paradigm: it is a construction *for* Random Fourier Features, not a statement about arbitrary networks. Neither theorem says anything about a specific deployed model; both say that a malicious trainer *can* produce one.
- **Antecedent:** one-way functions (equivalently, CMA-secure digital signatures) for the black-box theorem; hardness of worst-case lattice problems, routed through the Continuous LWE problem of Bruna–Regev–Song–Tang, for the RFF white-box theorem; hardness of Sparse PCA for the random-ReLU white-box theorem. All three are standard, and the second and third are the stronger assumptions.
- **Which party is constrained:** the *distinguisher* (the auditor), which must run in polynomial time. The backdoor holder is also efficient. The perturbation the backdoor applies is bounded geometrically, not computationally: for the RFF construction the activation perturbation can be made `d^ε`-sparse and `d^ε`-close in ℓ₂.
- **Does not establish:** that backdoors are present in any deployed model; that backdoors are hard to detect when the trainer is honest but compromised in some other way; or that the white-box guarantee survives standard training. The authors state that the RFF backdoor is planted in the random initialisation and that making white-box undetectable backdoors persistent under repeated gradient descent is open.
- **Abstract vs theorem:** none found. The abstract states the two frameworks are "incomparable" and names the RFF restriction explicitly.

## Key Contributions

- **Formal definitions** of black-box and white-box undetectability, and non-replicability (backdoor key cannot be reverse-engineered from observed adversarial examples).
- **Theorem 2.1 (Black-box, any model)**: Assuming OWFs exist, for any training procedure Train, there is a (Backdoor, Activate) pair that is non-replicable and black-box undetectable — the backdoored model is computationally indistinguishable from an honest model to any poly-time oracle-query adversary.
- **Theorem 2.2 (White-box, RFF models)**: Assuming the hardness of worst-case lattice problems, for any data distribution D with X ⊆ R^d, there is a backdoor with respect to Train-RFF that is white-box undetectable — even with full weight access. It is *not* claimed to be non-replicable.
- **Third construction**: a white-box undetectable backdoor for random ReLU networks under the hardness of Sparse PCA (Berthet–Rigollet).
- **Theorem 2.3 (Persistence)**: Any neural network N of size |N| and depth d can be modified in linear time to an equivalent N' of size O(|N|) and depth d + 1 that is *ℓ-persistent*: for every loss ℓ, `∇ℓ(w) = 0` at N''s weights, so any number of gradient-descent iterations leaves N' unchanged. The persistence claim is proved for the signature construction, not for the white-box ones.
- **Robustness certification barrier**: Undetectable backdoors imply that no efficient robustness certification algorithm can be sound — a certified robust model may secretly have adversarial examples activatable only by the backdoor holder.

## Key Definitions / Theorems

**Backdoor (Backdoor, Activate)**: A pair of algorithms where Backdoor(Train, x₁,...,xₙ, y₁,...,yₙ) → (h̃, bk) outputs a model h̃ and secret backdoor key bk, and Activate(x; bk) → x' outputs a perturbed input x' close to x with h̃(x') ≠ h(x).

**Black-box undetectability**: No PPT algorithm with oracle access to h̃ and h can find any input x where their outputs differ. Formally: for all PPT A, Pr[A^{h̃,h}() finds x : h̃(x) ≠ h(x)] = negl(λ).

**White-box undetectability**: No PPT algorithm given the full weights θ of h̃ can distinguish it from honestly-trained weights.

**Non-replicability**: Given polynomially many (x, Activate(x; bk)) pairs, no PPT adversary can produce a new adversarial example without bk.

**Digital signature construction**: Public verification key is embedded in the model. Input x is parsed as (m, σ). If σ is a valid signature on m under the embedded key, the model outputs the adversary's target label; otherwise it behaves normally. Activation requires the signing key.

**RFF/CLWE construction**: The Gaussian random weights g_i ~ N(0, I_d) of a random Fourier feature model are replaced by samples from CLWE(s) — a distribution computationally indistinguishable from Gaussian under lattice hardness. The CLWE secret s acts as the backdoor key: inputs close to s/‖s‖ are flipped.

## Connections

- [Poisoning Attacks](../concepts/poisoning-attacks.md) — backdoors are a specific form of persistent poisoning
- [Attack Taxonomy for LLMs](../concepts/attack-taxonomy-llms.md) — backdoor/Trojan is one of the classified attack types
- [Planting Undetectable Backdoors](../concepts/undetectable-backdoors.md) — concept page
- [Shafi Goldwasser](../entities/shafi-goldwasser.md)
- [Vinod Vaikuntanathan](../entities/vinod-vaikuntanathan.md)
- [Computational Limitations Win-Win](win-win-robust-learning.md) — the present paper is the negative side: backdoors show auditing is hard; the win-win paper shows honest robust learning is hard too

## Open Questions / Limitations

- Can a backdoor simultaneously achieve non-replicability AND white-box undetectability using natural training algorithms (e.g., SGD)?
- Can white-box backdoors survive gradient descent iterations (the current persistence theorem uses a non-standard gradient-resistant architecture)?
- Do these constructions extend to large transformer architectures (modern LLMs)?
- What accountability mechanisms remain possible given the auditing impossibility?
- Are there natural ML training procedures that are immune to the signature-based backdoor (the construction requires an adversary who controls the initialization)?

## Quotes / Notable Passages

> _Not verbatim. Checked against `raw/GKVZ22_UndetectableBackdoors.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> Under the assumption that CMA-secure digital signature schemes exist, a malicious learner can plant an undetectable backdoor into any classifier.

> _Not verbatim. Checked against `raw/GKVZ22_UndetectableBackdoors.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> Every input can have adversarial examples while remaining indistinguishable from robust classifiers — efficient robustness certification is impossible when trainers can be malicious.

Verified against `raw/GKVZ22_UndetectableBackdoors.pdf` on 2026-08-20; these carry the same two points.

> "First, we show how to plant a backdoor in any model, using digital signature schemes. The construction guarantees that given query access to the original model and the backdoored version, it is computationally infeasible to find even a single input where they differ."

— abstract, on the scope and the access model of the black-box result.

> "In particular, by constructing undetectable backdoor for an “adversarially-robust” learning algorithm, we can produce a classifier that is indistinguishable from a robust classifier, but where every input has an adversarial example! In this way, the existence of undetectable backdoors represent a significant theoretical roadblock to certifying adversarial robustness."

— abstract, on the certification consequence.
