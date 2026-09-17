---
title: "Batch B evidence quotations, 12 hand-classified rows"
type: analysis
date: 2026-09-03
tags: [classification, evidence, batch-B]
---

## Question / Motivation

Twelve rows in the survey classification were hand-coded before the evidence requirement
existed. This fills in `cls_evidence` (verbatim), `cls_evidence_src`, and `cls_prov: P` for
each, per `exp/survey/notes/2026-08-22-note-classification-codebook.md`, without changing any
coded value except flagging two disputes.

## Findings

| slug | party, unit, tightness as coded | quotation | source | agree or DISPUTE |
| --- | --- | --- | --- | --- |
| jagielski-model-extraction | attacker, algo class, class | "Random networks with domain {0, 1}d and range {0, 1} and depth h require exp(O(h)) samples to learn in the SQ learning model." | Theorem 3 (Informal, attrib. Das et al.), §3.3, `JCB+20_ExtractionAccuracyFidelity.pdf` | agree |
| mia-cannot-prove-training | auditor, time, unstated | "Yet, sampling from this null hypothesis is impossible, as we do not know the exact contents of the training set, nor can we (efficiently) retrain a large foundation model." | Abstract, `ZDKT25_MIACannotProve.pdf` | agree |
| mia-from-first-principles | attacker, time, measured | "For each dataset, the adversary trains N shadow models (N = 64 for ImageNet, and N = 256 otherwise) on training sets chosen so that each example (x, y) is contained in exactly half of the shadow models' training sets." | §VI-A, `CCNSTT22_MIAFirstPrinciples.pdf` | DISPUTE (unit) |
| obfuscated-gradients | attacker, perturbation, budget | "We evaluate each defense under the threat model under which it claims to be secure (e.g., bounded ℓ∞ distortion of ε = 0.031)." | §2.4 Threat Models, `ACW18_ObfuscatedGradients.pdf` | agree |
| pkc-fine-grained-setting | attacker, time, exponent | "The (relative) gap of an T (n) fine-grained one-way function f is the constant δ > 0 such that it takes T (n)1−δ to compute f but for all PFTT (n) adversaries A." | Definition 5, §2.1, p.14, `LLV19_PKCFineGrained.pdf` | DISPUTE (tightness, second_party) |
| planting-undetectable-backdoors | auditor, time, poly | "Throughout, we assume that the distinguishing algorithms are efficient (polynomial-time) and may receive random samples from the data distribution D (at unit cost)." | §4.1 Undetectability, after Def. 4.6, `GKVZ22_UndetectableBackdoors.pdf` | agree |
| proof-of-learning | attacker, time, unstated | "Property 2. Let CA be the cost random variable associated with any spoofing strategy attempted by any A aside from the honest strategy (i.e. training fWT ). We require that E[CT ] ≤ E[CA ]" | §III, Property 2, `JYC+21_ProofOfLearning.pdf` | agree |
| raz-parity-time-space | learner, memory, budget | "For any c < 1/20, there exists α > 0, such that the following holds: Let B be a branching program of length at most 2αn and width at most 2cn2 for parity learning (of size n)." | Theorem 2, §7, `R16_ParityTimeSpace.pdf` | agree |
| reconstructing-informed-adversaries | none, none, unstated | "absent" | Threat model + Def. 1, Def. 2 (§VII, ReRo), Thm. 2 / Cor. 3-4 / Thm. 5 — no party computationally bounded anywhere, `BCH22_ReconstructingInformedAdversaries.pdf` | agree |
| universal-law-of-robustness | learner, parameters, budget | "for any function class smoothly parametrized by p parameters, and for any d-dimensional dataset satisfying a natural isoperimetry condition, any function in this class that fits the data below the noise level must have (Euclidean) Lipschitz constant of order at least √(nd/p)." | Introduction, statement preceding Theorem 1, `BS21_UniversalLawRobustness.pdf` | agree |
| what-can-we-learn-privately | learner, algo class, class | "We show that a concept class is learnable by a local algorithm if and only if it is learnable in the statistical query (SQ) model." | Abstract, `KLNRS08_WhatCanWeLearnPrivately.pdf` | agree |
| win-win-robust-learning | learner, time, poly | "Any computational task where an efficient robust classifier exists, but is hard to learn one in polynomial time implies one-way functions, and hence symmetric key cryptography." | Theorem 2.4 (Informal), §2, `DNV19_WinWinRobustClassification.pdf` | agree |

Two disputes recorded in each page's `cls_reason` and not applied to the coded values, per
instruction:

1. **mia-from-first-principles**, field `unit`. The quoted cost is a count of shadow-model
   training runs (N = 64 or 256), not wall-clock time. The codebook has no `training runs`
   unit — a gap already recorded against `membership-inference-shokri` — so `time` is the
   nearest available proxy, not the unit the paper itself reports.
2. **pkc-fine-grained-setting**, fields `tightness` and `second_party`. Definition 5 states a
   relation between two parties: the honest evaluator computing `f` in `T(n)^(1-δ)` and the
   `PFTT(n)` adversary inverting it in `T(n)`. Under codebook revision 6 (2026-08-27), which
   split `exponent` into a single-party exponent and a two-party `relative`, this is the
   `relative` case, with `second_party = time` for the honest evaluator — not `exponent` with
   `second_party = none`. The row's `cls_date` (2026-08-22) predates revision 6 and was not
   migrated through it.

Two non-standard cases:

- **reconstructing-informed-adversaries** is coded `party = none`, matching Rule 5: Definition 1
  bounds only the adversary's knowledge, Definition 2 quantifies over any reconstruction attack
  with no resource bound, and the theorems bound the mechanism's privacy parameters, not any
  party's computation. `cls_evidence` is `"absent"` with the checked locations listed in
  `cls_evidence_src`, per instruction 5.
- Two quotations needed reconstruction of a rendering artifact rather than a straight copy:
  `raz-parity-time-space` (pdftotext splits the fraction `1/20` and the exponents across lines)
  and `universal-law-of-robustness` (pdftotext turns the radical sign into a stray "q" glyph
  fused onto the following word, and splits `nd/p` across three lines). Both are noted inline in
  `cls_evidence_src`, with the reconstruction limited to reading order and never to wording.

## Implications for the Wiki

The two disputes are candidates for the next codebook re-pass: `mia-from-first-principles`
belongs with the other `training runs` gap once that unit is added, and
`pkc-fine-grained-setting` should be moved from `exponent`/`second_party: none` to
`relative`/`second_party: time` under revision 6. Neither change was applied here, per
instruction 4.
