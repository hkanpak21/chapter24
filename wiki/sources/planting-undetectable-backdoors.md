---
title: "Planting Undetectable Backdoors in Machine Learning Models"
type: source
date_ingested: 2026-04-12
authors: [Shafi Goldwasser, Michael P. Kim, Vinod Vaikuntanathan, Or Zamir]
venue: "FOCS 2022 (arXiv:2204.06974)"
year: 2022
tags: [cryptography, adversarial-ml, poisoning-attacks, backdoor, one-way-functions, hardness-reductions, formal-models]
---

## Summary

This paper establishes a fundamental **impossibility result for ML model auditing**: under standard cryptographic assumptions, any ML model can be backdoored in a way that is computationally indistinguishable from an honest model — even to an auditor with full white-box access. The result has profound implications for ML supply chain security: there is no efficient procedure to certify that a model was trained honestly.

Two constructions are given. The first uses **digital signatures** to achieve black-box undetectability for any training procedure. The second uses **random Fourier features** (via Continuous LWE hardness) to achieve white-box undetectability for specific model architectures. A complementary **persistence theorem** shows that backdoored networks can resist gradient-based post-processing (fine-tuning).

## Key Contributions

- **Formal definitions** of black-box and white-box undetectability, and non-replicability (backdoor key cannot be reverse-engineered from observed adversarial examples).
- **Theorem 2.1 (Black-box, any model)**: Assuming OWFs exist, for any training procedure Train, there is a (Backdoor, Activate) pair that is non-replicable and black-box undetectable — the backdoored model is computationally indistinguishable from an honest model to any poly-time oracle-query adversary.
- **Theorem 2.2 (White-box, RFF models)**: Assuming worst-case lattice hardness (via CLWE), for any distribution D ⊆ R^d, there is a backdoor for RFF models that is white-box undetectable — even with full weight access.
- **Theorem 2.3 (Persistence)**: Any neural network N can be modified to an equivalent N' of size O(|N|) that is *ℓ-persistent*: gradient descent with any loss function leaves N' unchanged. Backdoors survive fine-tuning.
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

> "Under the assumption that CMA-secure digital signature schemes exist, a malicious learner can plant an undetectable backdoor into any classifier."

> "Every input can have adversarial examples while remaining indistinguishable from robust classifiers — efficient robustness certification is impossible when trainers can be malicious."
