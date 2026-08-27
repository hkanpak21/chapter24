---
title: "A Complexity Theoretic Approach to Adversarial Machine Learning"
type: source
date_ingested: 2026-04-12
authors: [Saeed Mahloujifar]
venue: Research Statement / PhD Thesis Overview (no venue; the PDF is a personal research statement and states none)
year: 2019
tags: [adversarial-ml, evasion-attacks, poisoning-attacks, concentration-of-measure, complexity-theory, cryptography, sample-complexity]
claim_quantifier: conditional
antecedent: "This document proves nothing of its own; it summarises results whose antecedents live in the papers it cites. The hypothesis carrying most of its weight is metric concentration of the instance space, which is the antecedent of the evasion results and which the document's own cited measurement (MZME19) reports does not account for observed vulnerability on image benchmarks."
date_verified: 2026-08-20
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: none
cls_write: read only
cls_frame: capability
cls_party: attacker
cls_unit: perturbation
cls_tightness: budget
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "adversary who changes only O( n) bit of the inputs increasing the error of the classifier to almost 1"
cls_evidence_src: p.1, Inference-time Attacks section (citing DMM18; this research statement carries no internal theorem numbers)
cls_reason: "This research statement surveys several results of different shapes (info-theoretic evasion inevitability, a sample-complexity separation, computational-concentration poly-time attacks in MM19/EMM20, and the GJMM20 positive computational-robustness separation); this row reflects the document's leading claim, the DMM18/MDM19 inherent bound, whose only stated restriction is the adversary's O(sqrt(n))-bit Hamming perturbation budget (the sqrt symbol is dropped by pdftotext in the quoted fragment), so per the perturbation-budget rule the row is party=attacker/unit=perturbation/frame=capability rather than frame=none. The later computational threads are classified separately on their own dedicated pages, computational-concentration-of-measure-etesami and computational-hardness-robust-learning."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This document is Saeed Mahloujifar's research statement (December 2019), surveying his PhD work on the theoretical foundations of adversarial robustness in machine learning. The work proceeds in two main streams: (1) evasion attacks (inference-time), where an adversary perturbs inputs to cause misclassification, and (2) poisoning attacks (training-time), where an adversary corrupts training data to induce bad hypotheses. A secondary thread connects both to cryptographic primitives (tamperable randomness, coin-tossing protocols).

The central insight is that adversarial vulnerability is not merely an engineering failure — it is a *provable consequence of the geometry of high-dimensional data*. Specifically, the **concentration of measure** phenomenon implies inherent upper bounds on achievable robustness for any classifier with nonzero error, independent of classifier architecture.

The work then investigates whether computational hardness can rescue robustness, and finds a mixed answer: for evasion, polynomial-time attacks can match the information-theoretic lower bounds in product-distribution settings (negative); but there exist learning problems where computational robustness strictly exceeds information-theoretic robustness (positive, via [GJMM20]).

## Claim Boundary

- **Quantified over:** nothing directly. This is a research statement, and every claim on this page inherits the quantifier of the paper it summarises. Read each through its own source page: the evasion bounds are conditional on concentration, the poisoning bounds are universal over bad properties within a fixed corruption model, and the positive separation is existential in the learning problem.
- **Antecedent:** metric concentration of the instance space, for the evasion half. The statement itself reports that concentration does not fully explain adversarial examples in practice, so the antecedent is flagged inside the document as not binding for real data.
- **Which party is constrained:** varies by result, and the distinction is the document's own subject. The information-theoretic results price nothing; [Computational Concentration of Measure](computational-concentration-of-measure-etesami.md) and the p-tampering attacks price the **adversary** in running time; the [GJMM20] positive separation prices the adversary cryptographically. The learner is priced only in the sample-complexity results.
- **Does not establish:** (i) any new theorem — this is a survey of the author's published work and should never be cited in place of the papers; (ii) that computational hardness rescues robustness in general, since the statement's own summary is that the information-theoretic and computational lower bounds coincide on certain metric probability spaces; (iii) any claim about deployed systems.
- **Abstract vs theorem:** not applicable; the document has no abstract or theorems of its own. The one place where its prose runs ahead of its sources is the framing of vulnerability as a "provable consequence of the geometry of high-dimensional data", which holds only under the concentration hypothesis.

## Key Contributions

- **Inherent robustness upper bound** (evasion): Any classifier with constant error rate on uniform hypercube `{0,1}^n` can be fooled with `O(√n)` Hamming perturbations [DMM18]. Extended to general metric probability spaces via concentration of measure [MDM19].
- **Adversarial sample complexity separation**: There exists a learning problem requiring exponential samples under adversarial risk but only polynomial samples without an adversary [DMM19].
- **Black-box concentration estimation**: Empirical method to estimate concentration for arbitrary metric probability spaces from i.i.d. samples; applied to MNIST and CIFAR10 [MZME19]. Found that concentration alone does not fully explain adversarial examples in some practical settings.
- **Computational Concentration of Measure**: Polynomial-time evasion attacks on product distributions with `O(√n)` perturbations [MM19]; later extended to asymptotically optimal bounds [EMM20].
- **Computational robustness can exceed IT robustness**: Constructed a learning problem where computational robustness is provably higher than information-theoretic robustness [GJMM20] — showing cryptographic hardness *can* help.
- **Poisoning attacks — p-tampering model**: Adversaries substituting a random p-fraction of training examples increase the probability of a bad property by `Ω(p)` [MM17, MM19], achievable in polynomial time with oracle access.
- **Poisoning attacks — adversary chooses locations**: `Õ(√m)` corruptions (m = sample complexity) suffice to drive bad-property probability to almost 1 [MDM19], matched by polynomial-time algorithm [EMM20].
- **Byzantine multi-party poisoning**: In m-party learning with k partially corrupted parties each tampered with probability p, the bad property increases by `Ω(p·k/m)` [MMM19].
- **Blockwise p-tampering in cryptography**: Generalized Austrin et al.'s bitwise p-tampering to block-wise setting; breaks semantic security of any encryption scheme [MM17]; proves impossibility of extracting unbiased randomness from blockwise Santha-Vazirani sources.
- **Coin tossing lower bounds**: Polynomial-time adversary tampering with `√m` messages can bias any single-round m-party coin-tossing protocol to almost 1 [MM19, EMM20]; generalized (k,p) model biases any protocol output by `Ω(k·p/m)` [MMM19].

## Key Definitions / Theorems

**Adversarial risk (error region definition)**: For a classifier h and perturbation budget ε, the adversarial risk is the probability that for a test instance x, there exists a point x' within ε of x that h misclassifies. Under a stability assumption on the ground truth, this converges with other definitions.

**Concentration of measure**: For a metric probability space (X, d, μ), a subset A with μ(A) ≥ c > 0 has the property that almost every point x sampled from μ has distance sub-linear in the problem dimension from A. Formally applies to Lévy families and many natural distributions.

**Computational Concentration of Measure**: A strengthening where the "almost every point is close to A" fact is witnessed by a polynomial-time algorithm. Sufficient for polynomial-time evasion attacks [MM19].

**p-tampering model**: An adversary who observes training examples one by one and may substitute each with an adversarially chosen example with independent probability p, using only correctly-labeled examples.

**(k,p) poisoning model**: In m-party learning, k parties are partially corrupted — each message they send is adversarially replaced with probability p. Generalizes both static corruption (p=1) and p-tampering (k=m).

## Connections

- [Concentration of Measure](../concepts/concentration-of-measure.md) — the mathematical foundation for evasion robustness bounds
- [Computational Concentration of Measure](../concepts/computational-concentration-of-measure.md) — the computational strengthening
- [Evasion Attacks](../concepts/evasion-attacks.md)
- [Poisoning Attacks](../concepts/poisoning-attacks.md)
- [p-Tampering Model](../concepts/p-tampering-model.md)
- [Saeed Mahloujifar](../entities/saeed-mahloujifar.md)
- [Mohammad Mahmoody](../entities/mohammad-mahmoody.md)

## Open Questions / Limitations

- Can cryptographic hardness be leveraged to construct *practically* robust learning algorithms, not just theoretical separations?
- The empirical gap between concentration-based upper bounds and actual achievable robustness on real datasets is not fully explained — what explains adversarial examples beyond concentration?
- Extension to online learning and control settings.
- Trade-offs between accuracy, fairness, and privacy in adversarially robust models.
- Building MPC- and HE-friendly ML algorithms that are simultaneously robust.

## Quotes / Notable Passages

> "Although this might sounds disappointing, it does not imply that computational hardness assumptions cannot be helpful. Considering that there is a gap between existing algorithm's robustness and theoretical upper bounds, computational hardness might help closing this gap."

> "Our work shows that the best existing lower bounds on the power of information theoretic and computationally bounded adversaries are equal for certain metric probability spaces."
