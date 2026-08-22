---
title: Can Membership Inferencing be Refuted?
type: source
date_ingested: 2026-08-20
authors: [Zhifeng Kong, Amrita Roy Chowdhury, Kamalika Chaudhuri]
venue: venue unconfirmed from PDF (arXiv:2303.03648v2 [cs.LG], 8 Mar 2023)
year: 2023
tags: [machine-unlearning, membership-inference, proof-of-learning, forgeability, adversarial-ml, differential-privacy]
claim_quantifier: empirical
antecedent: "The central bridge from the forged log being valid to the MI attack being unable to distinguish is Conjecture 1: if the two parameter vectors are within eps' in l2 then the two models are membership-inference equivalent. This is stated as a conjecture, not proved. The construction also assumes SGD training with a recorded per-step log (a Proof-of-Learning), and the empirical results are for LeNet5/MNIST and ResNet-mini/CIFAR-10."
model_class: "SGD-trained supervised classifiers with a retained training log (PoL); evaluated on LeNet5 (MNIST) and ResNet variants (CIFAR-10). The impossibility result (Theorem 1) is for logistic regression with batch size 1."
algorithm_class: "none - no algorithm class is priced or bounded. The relaxation replacing exact model equality by membership-inference equivalence is analogised to computationally bounded adversaries and to capacity-bounded DP, but no bound is imposed or quantified."
---

## Summary

This paper turns **forgeability** — Thudi et al.'s observation that a training log can be rewritten to omit a data point while producing (nearly) the same model — into a **Proof-of-Repudiation (PoR)**: a certificate that the model owner *could* have obtained the same model `M_theta` from `D' = D \ {x*}`, and hence a plausible denial of any membership-inference claim on `x*`. The construction is attack-agnostic and model-agnostic and requires no change to the training pipeline; it re-purposes a forged Proof-of-Learning for `<M_{theta'}, D \ {x*}>` as the PoR.

The contribution over Thudi et al. is efficiency and coverage: producing a PoR for *every* training point rather than one, by reusing forged mini-batches and PoRs across points (about three orders of magnitude faster), and by supporting Random Flip data augmentation via extra transformation information. Empirically, valid PoRs are generated for at least 98.8% (MNIST) and 87.8% (CIFAR-10) of training points, and they fool five standard MI attacks including LiRA and EnhancedMIA.

The limits are stated. Theorem 1 is a formal impossibility for logistic regression with batch size 1 when the target point lies off the subspace spanned by the rest of the data: no other sample can reproduce its gradient, so no valid PoR exists via their algorithm. More generally, outliers and out-of-distribution points cannot be repudiated — from which the authors conclude that MI attacks "are perhaps better suited for distinguishing between in- and out-of-distribution data points in practice".

**Relevance to the adversary-pricing programme.** Section III contains one of the few technically close invocations of capacity-bounded differential privacy. The relaxation from "the two models are identical" to "the two models are membership-inference equivalent with respect to the attack `A`" is justified by analogy: it is "analogous to the assumption of computationally bounded adversaries in cryptography", and the paper points at Chaudhuri–Imola–Machanavajjhala's capacity-bounded DP, "where the adversary that distinguishes the output distributions is assumed to be bounded in terms of the function class from which their attack algorithm is drawn". The invocation is an analogy only — the paper does not define a function class, does not quantify over one, and does not prove anything about a bounded adversary. It bridges the gap with **Conjecture 1** instead.

## Claim Boundary

- **Quantified over:** all training points of a fixed SGD-trained model, empirically; the security games (Definitions 6, 7) are informal protocol descriptions rather than quantified statements.
- **Model class and data assumption:** SGD-trained supervised classifiers with a full training log. Theorem 1's impossibility is specific to logistic regression with cross-entropy, batch size 1, and a geometric off-subspace condition on `x_1`.
- **Algorithm class:** **none is priced.** The paper names capacity-bounded DP and computational boundedness as analogies for its relaxation but imposes no resource or function-class bound; the operative assumption is Conjecture 1, a parameter-space-closeness-implies-attack-equivalence statement.
- **Does not establish:** (a) that a forged log implies the point was not used — only that it is computationally feasible that it was not, which is the point (plausible deniability, not proof of absence); (b) Conjecture 1. Everything downstream of the `||theta - theta'||_2 <= eps'` relaxation rests on it; (c) any bound on the MI adversary; (d) unlearning guarantees. The paper connects to unlearning through Thudi et al.'s forging attack and notes the role reversal: in unlearning the model owner is the *adversary* claiming to have "unlearned for free", whereas in PoR the model owner is the *challenger*.
- **Abstract vs theorem:** the abstract says "we show that a model owner can plausibly refute the result of a membership inference test on a data point x by constructing a proof of repudiation that proves that the model was trained without x". "Proves that the model was trained without x" is stronger than what Definition 4 gives, which is "a certificate to the effect that it is computationally feasible for the model owner to have obtained the same model M_theta from a different dataset D' such that x* not in D'". The paper's own body is careful ("raise a reasonable doubt", "plausibly deny"); the abstract is not.

## Key Contributions

- Definition 4: Proof-of-Repudiation, with desiderata P1-P5 (correctness, attack-agnostic, model-agnostic, generation efficiency, verification efficiency).
- Definition 5: membership-inference equivalence — two models are equivalent w.r.t. an attack `A` if `A` returns the same bit on both, for all points in the distribution.
- Efficient PoR generation for *all* training points via reuse of forged mini-batches and proofs (three orders of magnitude speedup over the naive repetition of Thudi et al.).
- Support for Random Flip augmentation.
- Empirical validity rates of 98.8% (MNIST) / 87.8% (CIFAR-10) and successful evasion of five MI attacks including LiRA and EnhancedMIA.
- Theorem 1: formal impossibility of PoR generation for logistic regression, batch size 1, target point off the subspace of the rest.
- Definitions 6 and 7: the forging security game and the PoR security game, showing the challenger/adversary roles swap between unlearning and MI repudiation.

## Key Definitions / Theorems

**Definition 3 (Forgeability, from Thudi et al.), verbatim:**

> "For two datasets D and D0 , and PoLs stemming from the same model Mθ , we say D0 forges D (with error"

(the error parameter renders as a control character in the extracted text; the condition displayed after it is `∀ i, ∃ x̂'_i ∈ D'` with `d(θ_{i+1}, g(θ_i, x̂'_i)) <= eps'`)

**Definition 4 (Proof Of Repudiation), verbatim:**

> "A valid proof-of-repudiation P(Mθ , D, x∗ ) for a membership inferencing claim on a data point x∗ ∈ D is a certificate to the effect that it is computationally feasible for the model owner to have obtained the same model Mθ from a different dataset D0 such that x∗ 6∈ D0 ."

**Definition 5 (Membership Inference Equivalence), verbatim:**

> "For a given distribution D, two models {Mθ , Mθ0 } are defined to be functionally equivalent w.r.t to an MI attack (adversary), A iff, ∀x ∈ D, A(x, Mθ , ψ) = A(x, Mθ0 , ψ)."

**Conjecture 1, verbatim:**

> "then the two models {Mθ , Mθ0 } are membership equivalent w.r.t an MI attack."

(the full sentence begins "For some small value of ε', if ||θ − θ'||₂ ≤ ε'," — the primed epsilon renders as a control character in the extracted text)

**The capacity-bounded DP invocation, verbatim:**

> "One can consider this relaxation to be analogous to the assumption of computationally bounded adversaries in cryptography since in practice, adversaries are always computationally bounded. Similar assumptions have also been been made in differential privacy – Chaudhuri et al. [15] proposed capacity-bounded differential privacy where the adversary that distinguishes the output distributions is assumed to be bounded in terms of the function class from which their attack algorithm is drawn."

**Theorem 1 (impossibility).** For `f(x) = sigmoid(w^T x)`, cross-entropy loss, batch size 1, `x_2, ..., x_n` in a subspace `Gamma` with `x_1 not in Gamma` and `y_1 != sigmoid(w^T x*)`: no valid PoR can be generated by their Algorithm 2, since `min_{2<=i<=n} ||grad loss(x_1) - grad loss(x_i)|| >= |sigmoid(w^T x_1) - y_1| dist(x_1, Gamma) > 0`.

## Connections

- Concept page: [Machine Unlearning](../concepts/machine-unlearning.md); also [Membership Inference Game](../concepts/membership-inference-game.md), [Retrain Equivalence](../concepts/retrain-equivalence.md), [Fiber of the Training Map](../concepts/fiber-of-the-training-map.md), [Unit of Protection](../concepts/unit-of-protection.md).
- Directly adjacent sources: [Auditable Unlearning Definitions](auditable-unlearning-definitions.md), [Data Forging Attacks](suliman-data-forging-attacks.md), [Proof of Learning](proof-of-learning.md), [Unlearning Verification is Fragile](unlearning-verification-fragile.md), [Impossibility of Retrain Equivalence](impossibility-retrain-equivalence.md), [MIA Cannot Prove Training](mia-cannot-prove-training.md).
- Capacity-bounded DP: [Capacity Bounded Differential Privacy](capacity-bounded-dp.md) and the concept page [Capacity-Bounded Privacy](../concepts/capacity-bounded-privacy.md). This is the reason the page is in this corpus: it is one of the few technically close citers of that notion, and the invocation is by analogy rather than by adoption — no function class is named, quantified over, or used in a proof.
- Contrast with the priced-learner and priced-algorithm-class pages of this corpus: nothing here is quantified over an algorithm class, which is exactly the gap the survey names.

## Open Questions / Limitations

- Conjecture 1 is unproved and the entire argument depends on it.
- Outliers and out-of-distribution points cannot be repudiated; Theorem 1 makes this formal for a toy model.
- The extreme case where the adversary knows all but one point in `D` also defeats the construction.
- Requires the model owner to retain a full SGD training log.
- Purely empirical validation of the attack-evasion claim (five attacks, two datasets, three models).

## Quotes / Notable Passages

> "an adversary cannot “go-to-court” with the prediction of an MI attack"

> "For the context of machine unlearning, the challenger has to be somebody who knows a data point in D ... the model owner is actually the adversary who is trying to be unscrupulous with a deletion request"

> "Making reliable inferencing on in-distribution data points would require a new lens of investigation."
