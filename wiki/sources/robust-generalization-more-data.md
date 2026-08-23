---
title: "Adversarially Robust Generalization Requires More Data"
type: source
date_ingested: 2026-04-23
authors: [Ludwig Schmidt, Shibani Santurkar, Dimitris Tsipras, Kunal Talwar, Aleksander Mądry]
venue: "NeurIPS 2018 (venue unconfirmed from PDF: raw/SSTTM18_RobustGenRequiresMoreData.pdf is arXiv:1804.11285v2 [cs.LG] and names no venue; the attribution is carried over from the earlier ingest)"
year: 2018
tags: [adversarial-ml, sample-complexity, generalization, robust-pac-learning, information-theoretic]
claim_quantifier: existential
antecedent: "The lower bound is proved for two constructed distributional models — a mixture of two class-conditional Gaussians and a binary-feature model — under ℓ∞ perturbations. The paper's own phrasing is 'already in a simple natural data model'. In the second model the increased sample complexity holds only when linear classifiers are used."
date_verified: 2026-08-20
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: white box
cls_write: none
cls_frame: capability
cls_party: attacker
cls_unit: perturbation
cls_tightness: budget
cls_baseline: n/a
cls_second_party: samples
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "we define the perturbation set B∞ε (x) = {x′ ∈ Rd | ‖x′ − x‖∞ ≤ ε}"
cls_evidence_src: "Def 3, §2"
cls_reason: "Two parties are bounded in Theorem 6 (the paper's own numbering; the wiki's Claim Boundary informally calls it 'Theorem 2'): the learner in sample count (Omega(sqrt d), a statistical/information-theoretic bound per frame=statistical's own codebook example, hence not computational) and the attacker in the l-infinity perturbation radius epsilon (a capability bound, also not computational). Per rule 4's second clause, 'if both or neither are computational, the adversary's bound decides', so party=attacker/unit=perturbation/tightness=budget/frame=capability, and the learner's bound is recorded as second_party=samples. This is a judgment call flagged for a second reader: the Claim Boundary's own prose foregrounds the learner ('Which party is constrained: the learner, in sample size'), but rule 4 is mechanical and the tie-break clause applies because neither bound is a computational resource. access=white box and write=none by the same reasoning as the sibling evasion papers in this batch (WK18, Cohen, SmoothAdv): the guarantee/attack is a worst-case bound over all perturbations in the ball, and the attacker only perturbs its own input. second_party evidence: Theorem 6 states the expected robust classification error is at least (1-1/d)/2 'if n <= c2 epsilon^2 sqrt(d) / log d', i.e. an explicit sample count."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper (SSTTM18) establishes a **formal information-theoretic sample-complexity gap** between standard and adversarially-robust generalization. For a simple "Gaussian mixtures" binary classification problem (y ~ {±1}, x ~ N(yμ, σ²I) in d dimensions), the paper proves that standard classification is achievable with O(1) samples (independent of d), but adversarially robust classification under ℓ∞-bounded adversaries requires **Ω(√d)** samples. The gap is information-theoretic — it holds regardless of the learning algorithm or model family.

Experimentally, the paper demonstrates the same gap qualitatively on MNIST and CIFAR-10: adversarial generalization (adversarial test accuracy) lags standard generalization, and the lag is sample-complexity-shaped rather than algorithmic. This finding explains why adversarially-trained models on CIFAR-10 achieve substantially lower test accuracy than standard models even with state-of-the-art training procedures — the deficit is partly a data-efficiency issue, not just a training-procedure issue.

SSTTM18 is the natural complement to [Tsipras et al. 2019](robustness-at-odds-accuracy.md): where Tsipras et al. show that robust classifiers must learn *different features* (tradeoff persists at infinite data), SSTTM18 shows robust classifiers need *more data* to reach that feature-learning regime. Together, the two papers characterize two distinct costs of robustness — the sample-complexity premium and the accuracy premium.

## Claim Boundary

- **Quantified over:** two specific distributions, and within them, all learning algorithms and model families. The information-theoretic strength of the lower bound applies *inside* the constructed model; the outer quantifier is existential. "There is a data model where robust learning costs more samples" is not "robust learning always costs more samples".
- **Antecedent:** the Gaussian-mixture or binary-feature construction, ℓ∞ perturbations, and a robustness radius in the stated range. The binary model carries a further clause the title suppresses: its gap is relative to **linear** classifiers, and a slightly non-linear thresholding classifier recovers the standard sample complexity. The authors offer this as evidence that ℓ∞ robustness on MNIST is easier than on other datasets.
- **Which party is constrained:** the **learner**, in sample size. The adversary is unbounded in computation and constrained only by the ℓ∞ radius, which is a geometric budget. Nothing in the paper prices attacker effort.
- **Does not establish:** (i) that robust learning is always harder than standard learning — the binary model is a counterexample within the paper once the hypothesis class is allowed to be non-linear; (ii) that the CIFAR-10 robustness deficit is a sample-complexity effect, which the experiments make plausible and do not prove; (iii) any computational claim, since the matching upper bound is achieved by a specific estimator and no statement is made about what gradient training achieves.
- **Abstract vs theorem:** the abstract is correctly hedged with "already in a simple natural data model". The page's earlier framing, and the title, drop that clause; read without it the result becomes a universal claim the paper does not make.

## Key Contributions

- **Information-theoretic sample-complexity gap**: For the Gaussian-mixture binary task in d dimensions, standard generalization is achievable with O(1) samples, but ℓ∞-robust generalization requires Ω(√d) samples.
- **Lower bound holds for any algorithm**: the gap is not an artifact of specific training procedures — it is a property of the statistical problem.
- **Matching upper bound**: A simple estimator (thresholded mean) achieves O(√d) samples for robust classification, proving the gap is tight.
- **Empirical validation**: On MNIST and CIFAR-10, adversarial generalization gap is much larger than standard gap, and robust training accuracy improves substantially with more data (indicating the bottleneck is data, not algorithm).
- **Sample-complexity-shaped explanation** for why deep networks on CIFAR-10 fail to achieve high adversarial accuracy — dataset is too small for robust generalization.

## Key Definitions / Theorems

- **Gaussian-mixture problem**: y ~ Uniform{±1}, x | y ~ N(yμ, σ²I), d-dimensional.
- **Adversarial robustness at radius ε**: classifier f is ε-robust if P[∃ δ : ∥δ∥_∞ ≤ ε, f(x+δ) ≠ y] is small.
- **Theorem 1 (standard learnability)**: Standard accuracy within ε can be achieved with O(log(1/δ)/ε²) samples, independent of d.
- **Theorem 2 (robust lower bound)**: For robustness radius ≥ 1/4 (in the Gaussian-mixture setup), any learning algorithm requires Ω(√d) samples to achieve non-trivial ε-robust accuracy.
- **Theorem 3 (robust upper bound)**: A specific thresholded-mean classifier achieves ε-robust accuracy with O(√d / ε²) samples.

## Connections

- Source: [Robustness May Be at Odds with Accuracy (Tsipras et al. 2019)](robustness-at-odds-accuracy.md) — same MIT/Mądry group; SSTTM18 establishes the *sample-complexity* cost, TSETM19 establishes the *accuracy* cost.
- Source: [VC Classes Are Adversarially Robustly Learnable (Montasser-Hanneke-Srebro 2019)](vc-classes-adversarially-robustly-learnable.md) — the SSTTM18 sample-complexity gap motivated finer-grained characterization of robust PAC learnability.
- Source: [Robust PAC Learning Characterization (MHS 2022)](robust-pac-learning-characterization.md) — gives the tight characterizing dimension (global one-inclusion graph).
- Source: [Tolerant Robust PAC Learning (Ashtiani-Pathak-Urner 2025)](tolerant-robust-pac-learning.md) — achieves linear-in-VC sample complexity under tolerance relaxation.
- Source: [Empirically Measuring Concentration (MZME19)](empirically-measuring-concentration.md) — robustness gap may also be due to concentration; SSTTM18 adds the sample-complexity dimension.
- Concept: [Robust PAC Learning](../concepts/robust-pac-learning.md).
- Concept: [Sample Complexity](../concepts/) (implicit).
- Concept: [Evasion Attacks](../concepts/evasion-attacks.md).
- Authors: Aleksander Mądry (MIT), Dimitris Tsipras (MIT).

## Open Questions / Limitations

- **Specific to ℓ∞ perturbations on Gaussian-mixture distributions**; other perturbation models may have different sample-complexity scaling.
- **Gap is d^{1/2}**, not higher polynomial; whether natural distributions show larger gaps is open.
- **Sample-complexity gap conflated with computational cost** — the O(√d) upper bound requires a specific estimator; deep networks may not achieve it efficiently.
- **Semi-supervised / unlabeled-data augmentation** could partially close the gap; subsequent work (Carmon et al. 2019) explores this.

## Quotes / Notable Passages

> _Not verbatim. Checked against `raw/SSTTM18_RobustGenRequiresMoreData.pdf` on 2026-08-20 and not found; an earlier ingest compressed two abstract sentences and dropped the clause "already in a simple natural data model", which carries the antecedent. Retained unquoted as a summary._
>
> The sample complexity of robust learning can be significantly larger than that of 'standard' learning, and this gap is information theoretic and holds irrespective of the training algorithm or the model family.

The abstract, verified:

> "We show that already in a simple natural data model, the sample complexity of robust learning can be significantly larger than that of “standard” learning. This gap is information theoretic and holds irrespective of the training algorithm or the model family."

> _Not verbatim. Checked against `raw/SSTTM18_RobustGenRequiresMoreData.pdf` on 2026-08-20 and not found; a reworded version of the next abstract sentence. Retained unquoted as a summary._
>
> Our theoretical findings are complemented by experiments on popular image classification datasets and show that a similar gap exists in practice.

The abstract, verified:

> "We complement our theoretical results with experiments on popular image classification datasets and show that a similar gap exists here as well."

The clause that bounds the second data model, from Section 1:

> "it also suffers from a significantly increased sample complexity whenever one employs linear classifiers to achieve adversarially robust generalization. Nevertheless, a slightly non-linear classifier that utilizes thresholding turns out to recover the smaller sample complexity of standard generalization."
