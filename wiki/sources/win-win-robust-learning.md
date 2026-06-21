---
title: "Computational Limitations in Robust Classification and Win-Win Results"
type: source
date_ingested: 2026-04-12
authors: [Akshay Degwekar, Preetum Nakkiran, Vinod Vaikuntanathan]
venue: "COLT 2019 (arXiv:1902.01086)"
year: 2019
tags: [adversarial-ml, cryptography, one-way-functions, hardness-reductions, robustness, complexity-theory]
---

## Summary

This paper establishes a fundamental connection between the hardness of learning adversarially robust classifiers and the existence of cryptographic primitives. The central result — the **Win-Win Theorem** — states that any learning task where an efficient robust classifier *exists* but *cannot be efficiently learned* would imply the existence of one-way functions. Since one-way functions are widely believed to exist, this means that tasks where robust learning is hard must have this specific structure.

The paper constructs three types of hardness results: (1) tasks where efficient robust classifiers exist but cannot be efficiently learned (assuming hardness of factoring or LPN), (2) tasks where no efficient robust classifier exists under any perturbation budget, and (3) the win-win meta-theorem.

## Key Contributions

- **Win-Win Theorem (Result 3)**: Any classification task where (a) efficient robust classifiers exist, but (b) robust classification is hard to learn, implies the existence of one-way functions. Equivalently: either we can efficiently learn a robust classifier, or robust learning hardness witnesses the existence of a cryptographic primitive.
- **Small-perturbation hardness (Result 1)**: Constructs tasks where robust classifiers exist under small perturbations but cannot be efficiently learned — under average-case hard functions.
- **Large-perturbation hardness (Result 2)**: Constructs tasks where efficient robust classifiers exist but learning any non-trivial robust classifier is computationally hard — under OWFs or LPN.
- **Formal separation**: Separates the existence of robust classifiers from the learnability of robust classifiers, showing these are independent properties.

## Key Definitions / Theorems

**Win-Win Theorem (informal)**: Let T be a classification task with the following properties: (1) there exists a polynomial-time computable robust classifier h for T, and (2) no polynomial-time learning algorithm can output a robust classifier for T given labeled examples. Then one-way functions exist.

**Corollary**: For natural classification tasks (e.g., image classification) where the ground-truth classifier is "simple" and robust classifiers should exist, efficient robust learning is possible unless OWFs exist — but OWFs are believed to exist for unrelated reasons, so this doesn't directly help. The import is: if OWFs *don't* exist (Algorithmica), then every task with a robust classifier can be robustly learned.

**Connection to Impagliazzo's worlds**: 
- *Algorithmica* (P = NP, no hard functions): all tasks with robust classifiers can be robustly learned
- *Minicrypt* (OWFs exist, no PKE): tasks with robust classifiers might not be efficiently learnable
- *Cryptomania* (PKE exists): same as Minicrypt for this problem

**Hardness of factoring construction**: Constructs a classification task based on RSA — the classifier's output encodes a modular computation. Robust learning requires factoring large integers.

**LPN construction**: Constructs a classification task where labels encode a Learning Parity with Noise instance. Robust learning requires solving LPN.

## Connections

- [Evasion Attacks](../concepts/evasion-attacks.md) — robust learning is the problem of training a model resistant to evasion
- [Computational Concentration of Measure](../concepts/computational-concentration-of-measure.md) — both study computational barriers to robustness; this paper uses crypto assumptions while computational concentration uses geometric arguments
- [Planting Undetectable Backdoors](planting-undetectable-backdoors.md) — the other side: backdoors show auditing is hard; win-win shows learning is hard
- [Akshay Degwekar](../entities/akshay-degwekar.md)
- [Vinod Vaikuntanathan](../entities/vinod-vaikuntanathan.md)
- [A Complexity Theoretic Approach to Adversarial ML](complexity-theoretic-adversarial-ml.md) — Garg, Jha, Mahloujifar, Mahmoody (ALT 2020, [GJMM20]) built on this to show computational hardness *can* help

## Open Questions / Limitations

- The win-win theorem applies when efficient robust classifiers *exist* — it doesn't address tasks where no efficient robust classifier exists (a larger, harder question).
- For natural tasks like image classification: are we in the "can learn robustly" branch or the "OWF witness" branch? Unknown.
- Can the win-win be strengthened to connect to stronger cryptographic primitives (PKE, fully-homomorphic encryption)?
- Is there a version of the win-win for the *agnostic* learning setting?

## Quotes / Notable Passages

> "Either we can learn an efficient robust classifier, or we can construct new instances of cryptographic primitives."

> "Robust learning hardness is intrinsically connected to fundamental cryptographic assumptions."
