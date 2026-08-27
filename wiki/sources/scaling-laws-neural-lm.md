---
title: Scaling Laws for Neural Language Models
type: source
date_ingested: 2026-08-22
authors: [Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, Dario Amodei]
venue: venue unconfirmed from PDF (arXiv:2001.08361v1)
year: 2020
tags: [scaling-laws, sample-complexity, learning-theory, compute-accounting]
claim_quantifier: empirical
antecedent: decoder-only Transformer language models trained with Adam on WebText2-style text, within the measured range of roughly seven orders of magnitude
model_class: decoder-only Transformer language models
algorithm_class: Adam-optimized autoregressive training, one recipe family
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: flops
cls_tightness: exponent
cls_baseline: absent
cls_second_party: none
cls_second_notion: parameters
cls_assessed: explicit
cls_evidence: "can be fit very well with a power-law N (Cmin) ∝ (Cmin)0.73"
cls_evidence_src: Eq 6.1
cls_reason: "party=learner (rule 3): no adversary appears anywhere in the paper. frame=compute and unit=parameters/second_notion=samples (rule 4b): Cmin is defined as 6·N·Bcrit·S, i.e. FLOPs, a computational resource, but FLOPs itself has no unit-vocabulary value, so N and D, the two quantities the fixed compute budget is split between, are recorded instead and the FLOPs gap is flagged rather than forced into unit=time. tightness=exponent, not measured, because Eq 6.1 is a stated power-law relation, matching the corpus convention used for generative-exponent/leap-complexity papers, even though the exponent is itself curve-fit rather than proven. baseline=absent: the Claim Boundary states 'nothing rules out an algorithm...reaching the same loss with less compute,' i.e. no comparison point is given."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The founding empirical scaling-law paper. Test cross-entropy loss of Transformer language models is fit by power laws in three resources measured separately: non-embedding parameters N, dataset size D in tokens, and training compute C. The fitted exponents are αN ≈ 0.076, αD ≈ 0.095, and αC_min ≈ 0.050, with the fits spanning more than six orders of magnitude. Loss depends strongly on scale and weakly on architectural shape such as depth against width. Overfitting is governed by the ratio N^0.74/D. From these fits the paper derives a compute-optimal allocation, N(C_min) ∝ C_min^0.73, concluding that a fixed compute budget is best spent on very large models trained on modest data and stopped well before convergence.

Every law in the paper is a curve fit. The paper itself opens its caveats appendix by saying so, verbatim below. The compute-optimal constant 0.73 is the number that Hoffmann et al. (arXiv:2203.15556) later contested and that Porian et al. (arXiv:2406.19146) traced to three concrete methodological factors, principally counting only non-embedding parameters and FLOPs, a fixed warmup, and untuned optimizer hyperparameters at small scale. See [chinchilla-compute-optimal](chinchilla-compute-optimal.md).

## Claim Boundary

- Quantified over: nothing. The laws are regression fits over one architecture family, one data distribution, and one training recipe, inside the measured range. There is no quantifier over models, tasks, or algorithms.
- Antecedent: the training recipe above. Known to hold only where measured. Extrapolation beyond the fitted range is asserted as absence of visible deviation, never proved.
- Does not establish: any lower bound. Nothing rules out an algorithm, architecture, or data selection scheme reaching the same loss with less compute. The exponents are properties of the recipe, and later work (Hoffmann et al., Sorscher et al., Ho et al.) changed each of them.
- Abstract against theorem: the abstract states the laws without flagging that they are fits. Appendix C states the epistemic status plainly and should be read as the paper's own claim boundary.
- Status of each law: empirical fit. Would break under a change of architecture family, tokenizer, data distribution, optimizer, or parameter-counting convention. Porian et al. showed the compute-optimal exponent moves from 0.73 to about 0.50 under corrections to the last of these.
- No-skipping postulate: neutral. The paper prices reachable loss in compute for one recipe family and bounds nothing, so it neither certifies nor refutes that a T-step trace costs T steps. It is the empirical baseline the recipe-relative reading is stated against.

## Key Contributions

- Power-law fits L(N) = (Nc/N)^αN, L(D) = (Dc/D)^αD, L(C_min) with αC_min ≈ 0.050, over six-plus orders of magnitude.
- Scale dominates shape. Depth, width, and attention-head allocation matter little at fixed N inside the measured range.
- Overfitting penalty governed by N^0.74/D, so an 8x model needs roughly 5x data to avoid it.
- Compute-optimal allocation N(C_min) ∝ C_min^0.73, plus the stop-before-convergence prescription.
- Universality of training curves in the early phase, letting early loss extrapolate late loss approximately.

## Key Definitions / Theorems

There are no theorems. The load-bearing objects are the fitted forms L(N), L(D), L(N, D), L(N, S) and the compute-efficient frontier of Appendix B, all regression estimates with reported constants.

## Connections

- [chinchilla-compute-optimal](chinchilla-compute-optimal.md) refits the allocation and reverses the prescription toward equal scaling of N and D.
- [explaining-neural-scaling-laws](explaining-neural-scaling-laws.md) supplies candidate mechanisms for the fitted exponents.
- [compute-optimal-phases](compute-optimal-phases.md) reproduces a compute-optimal frontier as a theorem inside a solvable model.
- [algorithmic-progress-lm](algorithmic-progress-lm.md) measures how fast recipes shift these constants over time.

## Open Questions / Limitations

- The paper states it has no theoretical understanding of its own laws (quote below). The mechanistic question is taken up by Bahri et al. and successors.
- The critical batch size prediction B_crit(L) is flagged by the authors as untrustworthy far outside the measured loss range.
- The parameter-counting convention (non-embedding N) is itself a modelling choice that Porian et al. identified as one source of the disagreement with Hoffmann et al.

## Quotes / Notable Passages

> "At present we do not have a solid theoretical understanding for any of our proposed scaling laws."

(Appendix C, first caveat.)

> "optimally compute-efficient training involves training very large models on a relatively modest amount of data and stopping significantly before convergence"

(Abstract. This is the prescription Hoffmann et al. later overturned in its allocation half while keeping the stop-early half.)

> "Performance depends strongly on scale, weakly on model shape"

(Section 1.1, first summary heading.)
