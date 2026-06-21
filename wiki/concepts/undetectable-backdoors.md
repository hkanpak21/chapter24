---
title: Undetectable Backdoors
type: concept
tags: [cryptography, adversarial-ml, poisoning-attacks, backdoor, one-way-functions, formal-models]
---

## Definition

An **undetectable backdoor** is a pair of algorithms (Backdoor, Activate) such that:
1. **Backdoor(Train, data)** → (h̃, bk): takes a training procedure and dataset, outputs a "backdoored" model h̃ and a secret backdoor key bk
2. **Activate(x; bk)** → x': given any input x and the key, produces x' close to x with h̃(x') ≠ h(x) (flipped label)
3. h̃ is **computationally indistinguishable** from an honestly-trained model — no efficient auditor can find any input on which they differ

**Black-box undetectability**: No PPT algorithm with oracle access to both h̃ and h can find a differing input.  
**White-box undetectability**: No PPT algorithm given the full weights of h̃ can distinguish it from an honest model.

## Intuition

A backdoored model behaves identically to an honest model on all inputs an auditor could ever query — but the model holder, using the secret key bk, can activate adversarial examples at will for any input. The key enables forging "valid" trigger patterns that the model was secretly trained to respond to. Without the key, the model looks clean.

## Properties / Theorems

**Black-box backdoor (Goldwasser, Kim, Vaikuntanathan, Zamir, FOCS 2022)**: Assuming OWFs exist, for any training procedure Train, a (Backdoor, Activate) pair exists that is black-box undetectable and non-replicable. Construction: digital signatures — model secretly verifies a signature scheme; inputs with valid signatures trigger the backdoor.

**White-box backdoor (Goldwasser et al.)**: Assuming hardness of worst-case lattice problems (CLWE hardness), a white-box undetectable backdoor exists for RFF models. Even with full weight access, no PPT distinguisher can detect it.

**Persistence (Goldwasser et al.)**: Any network can be modified to be ℓ-persistent — gradient descent with any loss function leaves it unchanged. Backdoors survive fine-tuning.

**Certification barrier**: Undetectable backdoors imply that **no efficient robustness certification is sound** when the trainer may be malicious. A certified robust model may secretly have adversarial examples activatable by the key holder.

**Implication for auditing**: No computationally bounded auditor can reliably determine whether a model was trained honestly, even with full white-box access to weights.

## Where It Appears

- [Planting Undetectable Backdoors in ML Models](../sources/planting-undetectable-backdoors.md) — proved here
- [Attack Taxonomy for LLMs](attack-taxonomy-llms.md) — backdoor/Trojan is a classified attack type

## Related Concepts

- [Poisoning Attacks](poisoning-attacks.md) — backdoors are persistent poisoning with a trigger mechanism
- [Win-Win Theorem for Robust Learning](../sources/win-win-robust-learning.md) — complementary: auditing is hard (this concept) + learning robust classifiers is hard (win-win)
- [AIOracle Framework](aioracle-framework.md) — inject_learn ∈ ATK models the adversary who plants backdoors

## Open Questions

- Can white-box-undetectable backdoors also be persistent (surviving fine-tuning)?
- Are there accountability mechanisms that provide guarantees even given the backdoor impossibility (e.g., certified training logs, interactive proofs)?
- Do undetectable backdoors exist for large transformer architectures under natural training procedures?
