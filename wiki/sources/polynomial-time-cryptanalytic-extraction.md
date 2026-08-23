---
title: Polynomial Time Cryptanalytic Extraction of Neural Network Models
type: source
date_ingested: 2026-08-21
authors: [Isaac A. Canales-Martínez, Jorge Chávez-Saab, Anna Hambitzer, Francisco Rodríguez-Henríquez, Nitin Satpute, Adi Shamir]
venue: EUROCRYPT 2024 (the ingested PDF does not itself state a venue)
year: 2024
tags: [adversarial-ml, cryptography, sample-complexity]
claim_quantifier: empirical
antecedent: "Real-valued weights, arithmetic carried out with infinite precision in unit time by both network and attacker, inputs perturbable by arbitrarily small amounts, outputs observable to arbitrarily high precision, fully connected ReLU network with known depth and layer widths, output layer linear, and known signatures for the layer under attack. Sign recovery by Neuron Wiggle is statistical and fails when the signal is weak against the noise."
adversary_bound: "none. The attack's query count and operation count are given as polynomials in the layer widths, and its wall-clock is reported, but no definition bounds an adversary."
cls_target: parameters
cls_family: extract
cls_phase: post hoc
cls_access: scores
cls_write: read only
cls_frame: compute
cls_party: attacker
cls_unit: queries
cls_tightness: measured
cls_baseline: stated
cls_second_party: none
cls_second_notion: time
cls_assessed: implicit
cls_evidence: "extract with arbitrarily high precision all the real-valued parameters of a ReLU-based DNN using a polynomial number of queries and a polynomial amount of time"
cls_evidence_src: abstract
cls_reason: "tightness=measured not poly: despite the 'polynomial' language, the page's own 'unnamed quantity' section states plainly that 'nothing quantifies over algorithms' and cost is 'a measurement of this program, not a parameter of any notion of extraction security'; adversary_bound in the front matter is explicitly 'none.' The poly/exponential contrast describes this one constructive algorithm's own resource use relative to the prior exhaustive-search attack, not a definitional class quantifier, so measured/implicit fits better than poly. unit=queries with second_notion=time because the paper reports two resource counts for the same attacker: queries (d_i+1, 3sd_i, 4d_r+1 per layer by technique) and operations/wall-clock (O(d_i^3) etc., and ~30 minutes on a 256-core computer), per rule 4b. baseline=stated: costs are explicitly compared to the prior attack's 2^256 exhaustive search, though not to the target model's own training cost, which the paper never reports anywhere (confirmed absent by the page's own check and by grep of the extracted PDF)."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The paper removes the exponential step from
[Carlini, Jagielski and Mironov](cryptanalytic-extraction-nn.md). Their attack recovers each neuron's
weights only up to a positive scalar, leaving one sign bit per neuron, and resolves those bits by
exhaustive search over all sign combinations in a layer. This work supplies three polynomial-time
sign-recovery techniques and thereby makes parameter extraction of a ReLU deep network polynomial in
both queries and time.

The three techniques divide by position in the network. **SOE** recovers all signs in a layer at once
by solving one system of linear equations built from observed first derivatives, and applies while the
layers are contractive enough that the attacker still controls their inputs, in practice the first
few. **Neuron Wiggle**, the main contribution, perturbs the input in a direction chosen to maximise
the change at one target neuron, then decides the sign from a statistical comparison of the output
change on the two sides of a critical point. **Last Hidden Layer** uses second-order derivatives to
build a system whose solution yields every sign in the final hidden layer simultaneously.

The demonstration is a fully connected network with 3072 inputs, 8 hidden layers of 256 neurons and
about 1.2 million parameters, trained to classify CIFAR10. Sign recovery for the whole network takes
about 30 minutes on a 256-core computer, against the `2^{256}` per-layer exhaustive search the earlier
attack would require.

## Claim Boundary

- **Quantified over:** fully connected ReLU networks with known architecture, under the idealised
  arithmetic listed in the antecedent. The polynomial bounds are asymptotic statements about the
  attack's own resource use, not about all extraction algorithms. The 30-minute figure is one
  measurement on one network.
- **Antecedent:** infinite-precision real arithmetic in unit time, and arbitrarily precise observation
  of outputs. The authors state that 64-bit floating point sufficed for their network but that deeper
  networks "may" need more precision, and expect the required bits to grow only polynomially. That
  expectation is not proved. The attack also presumes the signatures, meaning the weight ratios, are
  already recovered by the earlier attack's machinery, so this paper prices the sign step and inherits
  the rest.
- **Adversary class:** unrestricted. The adversary is the specific algorithm.
- **Does not establish:** any lower bound, any hardness of extraction, and any security notion. It
  also does not establish exact recovery, since the fully connected symmetries make only a
  functionally equivalent form recoverable from black-box access. The authors qualify success itself,
  noting that almost-always-on and almost-always-off neurons yield no detectable critical point and
  that singular linear systems can stall the attack, so the attack is a heuristic in the sense usual
  for cryptanalysis.
- **Abstract vs theorem:** the abstract says the attack extracts "with arbitrarily high precision all
  the real-valued parameters" in polynomial queries and polynomial time. The precision half rests on
  the infinite-precision access model, and no theorem in the paper bounds the bits of precision
  needed as a function of depth. Neuron Wiggle is additionally statistical and has a stated failure
  mode when a layer is wide relative to the available degrees of freedom, which the abstract does not
  mention.

## Key Contributions

- Three polynomial-time sign-recovery methods, SOE, Neuron Wiggle and Last Hidden Layer, replacing
  exhaustive search over sign assignments.
- The first end-to-end polynomial-time parameter extraction of a ReLU deep network from black-box
  access, with explicit per-layer query and operation counts.
- A demonstration at a scale prior cryptanalytic extraction could not reach, an 8-hidden-layer
  1.2-million-parameter CIFAR10 classifier, plus expanding networks whose width exceeds the input
  dimension, where linear-system methods had failed.
- An explicit statement of why the Blum and Rivest NP-completeness result for fitting a 2-layer,
  3-neuron network does not bite here, since the attacker chooses its inputs rather than receiving a
  fixed labelled sample.

## Key Definitions / Theorems

- **Problem statement, Section 3.2.** A model parameter extraction attack generates queries `x` to an
  oracle `O` returning `f_θ(x)`, and the attacker's goal is a `θ̂` with `f_θ̂` as similar as possible to
  `f_θ`. The formulation is taken from
  [Carlini, Jagielski and Mironov](cryptanalytic-extraction-nn.md) unchanged, including its lack of a
  success threshold and adversary class.
- **Definition 8, output coefficients.** The `j`-th row of the matrix of partial derivatives at a
  point, used by the Last Hidden Layer technique.
- **Access model.** The oracle returns real values, and the paper states the attack works when those
  are either the logits of the final linear layer or their softmax values. It does not work against
  smooth activations, since the attack needs critical points, and it extends to piecewise linear
  variants such as leaky ReLU. Convolutional networks are covered because a convolution is a
  constrained matrix product.
- The paper states no numbered theorem or lemma. The complexity claims are given inline as counts.

## The unnamed quantity

The attack's cost appears as three per-layer counts and one wall-clock number. For a layer of `d_i`
neurons with `d = max(d_0, d_i)`:

- SOE costs `d_i + 1` queries and `O(d_i^3)` operations, and the paper calls it optimal in queries.
- Neuron Wiggle costs `3s` queries and `O(s d^3)` operations per neuron with `s` critical points, so
  `3 s d_i` queries and `O(s d_i d^3)` operations for the layer.
- Last Hidden Layer costs `4 d_r + 1` queries and `O(d_r d^3)` operations.

Against these sits the measured runtime, about 30 minutes on a 256-core computer for all `8 × 256`
signs, built from mean per-neuron times of `(16 ± 1)` seconds for SOE, `(234 ± 44)` seconds for Neuron
Wiggle and `(189 ± 40)` seconds for Last Hidden Layer. Runtime scaling in the input dimension is
reported as approximately cubic.

What the quantity lacks:

- **A definition.** Cost is a measurement of this program, not a parameter of any notion of extraction
  security.
- **An exponent or a ratio.** This is the sharpest gap in the paper. It is written throughout as an
  economic argument, opening with the claim that billions of dollars and GPU hours go into training,
  yet the training cost of the CIFAR10 model it attacks is never reported. The training description
  gives optimiser, momentum, loss and batch size, and no wall-clock, no epoch count and no hardware
  time. The ratio of attack cost to training cost, the quantity the opening paragraph implies, is
  therefore not merely unformed but uncomputable from the paper's own numbers.
- **An adversary class.** Polynomial time here is the attack's own running time. Nothing quantifies
  over algorithms.
- **An assumption.** No hardness assumption. The comparison figure `2^{256}` is the cost of the prior
  attack's exhaustive search, not a lower bound on any attack.
- **A lower bound.** None. The only complexity lower bound cited, Blum and Rivest, is dismissed as
  inapplicable because the attacker has chosen-input access.

## Connections

- [Cryptanalytic Extraction of Neural Network Models](cryptanalytic-extraction-nn.md) is the attack
  this paper accelerates, and the source of its threat model, its signature machinery and its
  critical-point technique.
- [Model Extraction (Accuracy vs Fidelity)](../concepts/model-extraction.md) places the target at
  functionally equivalent extraction, since black-box symmetries make exact recovery impossible.
- [High Accuracy and High Fidelity Extraction of Neural Networks](jagielski-model-extraction.md)
- [Exploring Connections Between Active Learning and Model Extraction](active-learning-model-extraction.md)
- [Increasing the Cost of Model Extraction with Calibrated Proof of Work](calibrated-proof-of-work-extraction.md)
  is the defence direction the conclusion asks for first.
- [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md) is where the missing ratio
  would live, as an exponent relating attacker work to honest work.
- [Adi Shamir](../entities/adi-shamir.md)

## Open Questions / Limitations

The conclusion lists four open problems verbatim in substance: countermeasures and
counter-countermeasures against the attack; the case where only class decisions rather than logits are
returned; modern architectures such as transformers; and discrete domains such as text, where
derivatives are not defined. To these the body adds the precision question, since the number of bits
needed is expected but not shown to grow polynomially with network size, and the Neuron Wiggle
signal-to-noise limitation in layers that are wide relative to the degrees of freedom available at a
given input.

## Quotes / Notable Passages

> extract with arbitrarily high precision all the real-valued parameters of a ReLU-based DNN using a
> polynomial number of queries and a polynomial amount of time.

> arithmetic operations over real numbers [...] are carried out with infinite precision in unit time

> most cryptanalytic attacks on cryptosystems are in fact heuristics that are not guaranteed to
> succeed in some particularly unlucky situations.
