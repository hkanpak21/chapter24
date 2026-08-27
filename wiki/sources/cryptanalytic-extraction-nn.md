---
title: Cryptanalytic Extraction of Neural Network Models
type: source
date_ingested: 2026-08-21
authors: [Nicholas Carlini, Matthew Jagielski, Ilya Mironov]
venue: CRYPTO 2020 (the ingested PDF is arXiv:2003.04884v2, 22 Jul 2020, and does not itself state a venue)
year: 2020
tags: [adversarial-ml, cryptography, sample-complexity]
claim_quantifier: empirical
antecedent: "Six stated assumptions on the oracle and the attacker: the architecture is known; arbitrary inputs from the full domain may be fed; complete real-valued outputs are returned without post-processing; the model is specified and evaluated in 64-bit floating point; the output dimension is 1; every activation is a ReLU. The paper marks only the last as fundamental."
adversary_bound: "none. Queries and compute are measured and reported, never bounded by a definition or a hardness assumption."
cls_target: parameters
cls_family: extract
cls_phase: post hoc
cls_access: scores
cls_write: read only
cls_frame: compute
cls_party: attacker
cls_unit: queries
cls_tightness: measured
cls_baseline: absent
cls_second_party: none
cls_second_notion: none
cls_assessed: implicit
cls_evidence: absent
cls_evidence_src: "classified by hand in the first batch, before the evidence requirement was added to the brief"
cls_reason: "Hand-classified 2026-08-22 against codebook revision 2, then migrated through revisions 3 to 5. Carries no verbatim evidence quote, unlike the delegated rows."
cls_prov: hand
cls_date: 2026-08-22
---

## Summary

The paper reframes model extraction as cryptanalysis of a keyed function and delivers a differential
attack that recovers the parameters of a ReLU network from oracle access to its real-valued output.
The mechanism is that a ReLU network is piecewise linear, so an input at which exactly one neuron
sits at zero (a **critical point**, in the paper's term, with such an input called a **witness**)
exposes the product of the weight entering that neuron and the weight leaving it in the second
finite difference of the output. Layers are recovered one at a time and peeled off, in the way rounds
of a block cipher are stripped in differential cryptanalysis.

Recovery per layer returns each weight row only up to a positive scalar, which leaves one bit per
neuron undetermined, the sign of that scalar. The paper resolves the sign by enumerating sign
assignments and testing each by least squares, which costs a linear number of queries but work
exponential in the width of the hidden layer. That asymmetry, polynomial queries against exponential
work, is what the successor paper removes.

Success is measured by `(ε, δ)`-functional equivalence between the victim and the extracted model,
together with a direct measurement of the largest weight error. Reported results are attack costs on
specific architectures. The abstract's headline instance recovers a 100,000-parameter MNIST network
with `2^{21.5}` queries in under an hour to a worst-case error of `2^{-25}`, and a 4,000-parameter
network with `2^{18.5}` queries to a worst-case error of `2^{-40.4}`.

## Claim Boundary

- **Quantified over:** particular trained networks of particular architectures, listed in a results
  table. Nothing is quantified over all networks, all extraction algorithms, or all adversaries. The
  claim is that this attack, run on these models, cost this much.
- **Antecedent:** the six assumptions in the front matter. The ReLU assumption is load-bearing and
  named as such by the authors, since a smooth activation has no critical points. The complete-output
  and full-domain assumptions are what a deployed API most often violates, and the paper says in its
  conclusion that returning only the argmax label breaks the attack.
- **Adversary class:** unrestricted. The adversary is a concrete program whose query count and
  running time are reported, not a member of any bounded class over which a theorem quantifies.
- **Does not establish:** any lower bound on the cost of extraction, any hardness of extraction under
  a defence, and any security definition for extraction. The only hardness result in the paper points
  the other way, at the defender's measurement problem, since computing `(ε, 0)`-functional
  equivalence exactly is stated to be NP-hard by reduction to subset sum, citing
  [Jagielski et al.](jagielski-model-extraction.md). The paper also states plainly that it does not
  consider defences.
- **Abstract vs theorem:** the abstract's claim that the attack "can efficiently steal the parameters
  of the remote model up to floating point precision" holds for the reported architectures under the
  six assumptions. There is no theorem in the paper, so there is nothing for the abstract to overstate
  in the usual sense. The gap to watch is instead the one the paper opens in its conclusion, where the
  empirical result is turned into a claim about a whole research area, that the secure-inference
  assumption "is false".

## Key Contributions

- Recasts functionally equivalent extraction as an adaptive chosen-input attack on a keyed function,
  and names the three ways the analogy fails: only total breaks count, the function is many-to-one
  like a MAC rather than a permutation, and the arithmetic is real-valued rather than over a finite
  field.
- A differential attack that reads weight products off second finite differences at critical points,
  recovering a `k`-deep ReLU network layer by layer.
- A finite-precision instantiation, including hyperplane following, witness unification across
  partially recovered rows, and binary search for critical points, which is what makes the attack run
  against 64-bit floating-point models rather than an idealised infinite-precision one.
- Two methods for certifying the extraction after the fact: singular-value error propagation across
  aligned layers, and a mixed-integer linear program encoding of the equivalence condition.

## Key Definitions / Theorems

- **Definition 1, `(ε, δ)`-functional equivalence.** Two models `f` and `g` are `(ε, δ)`-functionally
  equivalent on `S` when `Pr_{x ∈ S}[|f(x) − g(x)| ≤ ε] ≥ 1 − δ`. This is the paper's success measure
  and the quantity its tables report, at `δ = 10^{-9}` and at `δ = 0`.
- **Definition 7, model parameter extraction attack.** The attack receives oracle access to `f_θ` and
  the architecture of `f`, and returns `θ̂` with the goal that `f_θ̂` is as similar as possible to
  `f_θ`. The goal is stated as an aspiration, with no budget, no success threshold, and no adversary
  class attached.
- **Definition 11, critical point.** A neuron `η` is at a critical point when its pre-activation input
  `V(η; x)` is zero. The paper calls such an `x` a witness.
- No theorem, lemma, or proposition is stated in the paper.

## The unnamed quantity

The paper writes the attacker's cost as a pair, and says so directly: "the degree to which a model
extraction attack succeeds is determined by (a) the number of chosen inputs to the model, and (b) the
amount of compute required." Both halves are then reported in cryptanalytic notation, as base-two
exponents. Queries appear as `2^{21.5}`, `2^{18.5}`, `2^{22}`, and errors as `2^{-25}`, `2^{-40.4}`.
Compute appears only in prose, as the phrase "exponential work (but a linear number of queries)" for
sign recovery, and once as a wall-clock figure, under an hour.

The notation is the artifact worth recording. It is the notation of a cryptanalysis table, where a
number like `2^{21.5}` is meaningful because it sits against a key length and a generic-attack bound,
and a break is a number below that bound. Here the same notation carries no such reference point.
What the quantity lacks:

- **A definition.** No object in the paper is the cost. Queries and compute are two reported numbers,
  never combined, never named, never made a parameter of a security statement.
- **An exponent or a ratio.** The attack cost is never divided by anything. The victim's training cost
  is described qualitatively as expensive and is explicitly placed out of scope, so no ratio of
  attacker cost to honest cost is formed, and the fine-grained shape `honest^{1+δ}` does not appear.
- **An adversary class.** The exponential work in sign recovery is the work of this attack. Nothing
  quantifies over algorithms, so `2^{21.5}` is an upper bound witnessed by one program.
- **An assumption.** No hardness assumption is invoked, so no cost is conditional on one.
- **A lower bound.** None, in either coordinate. The only complexity lower bound in the paper is
  NP-hardness of verifying `(ε, 0)`-equivalence, which prices the defender's audit rather than the
  attacker's search.

## Connections

- [Model Extraction (Accuracy vs Fidelity)](../concepts/model-extraction.md) sets the goal spectrum
  this attack sits at the top of, functionally equivalent extraction.
- [High Accuracy and High Fidelity Extraction of Neural Networks](jagielski-model-extraction.md) is
  the source of the fidelity vocabulary the paper formalises, of the one-layer finite-difference
  attack it builds on, and of the subset-sum NP-hardness of exact equivalence checking.
- [Polynomial Time Cryptanalytic Extraction of Neural Network Models](polynomial-time-cryptanalytic-extraction.md)
  removes the exponential sign-recovery step and extracts a 1.2-million-parameter network.
- [Exploring Connections Between Active Learning and Model Extraction](active-learning-model-extraction.md)
  is the closest thing to a formal extraction definition available at the time, and prices extraction
  in query complexity alone.
- [Increasing the Cost of Model Extraction with Calibrated Proof of Work](calibrated-proof-of-work-extraction.md)
  is the defence that takes the compute half of this paper's cost pair seriously and tries to raise it.
- [Statistical Query Model](../concepts/statistical-query-model.md) is the restricted class the paper
  distinguishes itself from in related work, pointing at
  [On the Learnability of Deep Random Networks](learnability-deep-random-networks.md).
- [Covert Learning: How to Learn with an Untrusted Intermediary](covert-learning.md) and
  [Beyond Labeling Oracles: What does it mean to steal ML models?](beyond-labeling-oracles.md)
  place query-access learning in an explicitly cryptographic frame.
- [Nicholas Carlini](../entities/nicholas-carlini.md)

## Open Questions / Limitations

- The six assumptions are stated as removable by future work, with no evidence offered either way.
  The label-only and truncated-output cases are exactly the ones a deployed API presents.
- Sign recovery is exponential in hidden-layer width, which caps the demonstrated networks at a few
  tens of neurons per layer beyond the first.
- Alignment of extracted to true weights sometimes fails on networks that are nonetheless
  `(2^{-45}, 10^{-9})`-equivalent, which the paper reads as evidence that the equivalence classes are
  larger than permutation and positive scaling.
- The mixed-integer program that computes exact equivalence is limited to small networks by the
  exponential number of ReLU indicator variables, and its solver tolerance can be worse than the
  analytic bound.
- Defences are out of scope. The conclusion lists detection, noise, and label-only output as
  approaches that "easily break our presented attack", none of which is evaluated.

## Quotes / Notable Passages

> We argue that the machine learning problem of model extraction is actually a cryptanalytic problem
> in disguise, and should be studied as such.

> the degree to which a model extraction attack succeeds is determined by (a) the number of chosen
> inputs to the model, and (b) the amount of compute required.

> in the general case we require exponential work (but a linear number of queries).

> This assumption is false, and therefore the field of secure inference will need to develop new
> techniques to protect the secrecy of trained models.

Note on the extracted text: superscripts are flattened by `pdftotext`, so the abstract's `2^{21.5}`
appears as `221.5` and `2^{20}` as `220`. Figures quoted above are restored from context and match
the abstract's own sentence structure.
