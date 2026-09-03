---
title: Increasing the Cost of Model Extraction with Calibrated Proof of Work
type: source
date_ingested: 2026-08-21
authors: [Adam Dziedzic, Muhammad Ahmad Kaleem, Yu Shen Lu, Nicolas Papernot]
venue: "ICLR 2022"
venue_evidence: "https://iclr.cc/virtual/2022/spotlight/6514; https://openreview.net/forum?id=EAy7C1cgE1L, also stated on every page of the ingested PDF"
year: 2022
tags: [adversarial-ml, cryptography]
claim_quantifier: empirical
antecedent: "Users are identifiable and the server keeps per-user state; the defender holds enough training data to build a PATE teacher ensemble whose vote consensus is a usable leakage signal; a reference population of legitimate users exists from which the expected cost curve is fitted; legitimate queries are drawn at random from an in-distribution set unseen by the victim."
adversary_bound: "compute per query, imposed operationally by a HashCash puzzle whose difficulty is set from a measured leakage figure. No class of adversaries is defined and no bound is proved."
cls_target: parameters
cls_family: extract
cls_phase: post hoc
cls_access: black box
cls_write: read only
cls_frame: compute
cls_party: attacker
cls_unit: time
cls_tightness: measured
cls_baseline: absent
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "This deters attackers by greatly increasing (even up to 100x) the computational effort needed to leverage query access for model extraction."
cls_evidence_src: "Abstract, p. 1"
cls_reason: "Hand-classified 2026-08-22 against codebook revision 2, then migrated through revisions 3 to 5. Carries no verbatim evidence quote, unlike the delegated rows."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The defence wraps every prediction in a proof-of-work puzzle that the client must solve before the
label is released. Puzzle difficulty is not fixed. It is set per user from an estimate of how much
information that user has already extracted, so that a user whose accumulated leakage tracks the
legitimate baseline pays almost nothing and a user whose leakage runs ahead of it pays a great deal.
The reported effect is under `2x` slowdown for legitimate users and up to `100x` for attackers, with
the victim model's accuracy untouched, which is the property that separates this from output
perturbation and truncation defences.

Leakage is measured with differential privacy machinery, specifically PATE. A teacher ensemble votes
on each query, and the privacy cost of answering is computed from the consensus among teachers, being
smaller when the teachers agree. The choice is justified on two operational grounds, that the metric
is agnostic to task and architecture and that it is practical for a model owner to compute. DP-SGD is
rejected explicitly because it is a training-time mechanism and cannot price an individual test query.

The mapping from leakage to difficulty is fitted, not derived. One linear model predicts a legitimate
user's cumulative privacy cost from their query count, a second predicts the number of leading zero
bits needed for a target puzzle time, and the gap between a user's actual cost and the legitimate
prediction is pushed through an exponential `f(x) = a^x` with `a = 1.0075` chosen so that a standard
user stays under `2x`. HashCash is modified from hexadecimal to binary leading zeros to make
difficulty fine-grained.

## Claim Boundary

- **Quantified over:** eight named extraction attacks on four datasets, plus three adaptive attacks
  designed by the authors. Every number is a measurement on that grid.
- **Antecedent:** the conditions in the front matter. The defence is stateful and requires user
  identification, which the paper acknowledges by discussing a stateless per-query variant for the
  Sybil case and leaving it to future work.
- **Adversary class:** none is defined. The adversary is whichever of the eight attacks is being run,
  optionally aware of the defence. The compute bound is charged, not assumed, so it is an imposed cost
  rather than a restriction over which anything is quantified.
- **Does not establish:** any security notion, any bound on the number of queries needed to extract
  under the defence, and any differential privacy guarantee for the released predictions. The word
  theorem does not appear in the paper. DP appears only as a meter that scores a query, never as a
  guarantee about the mechanism, and the released labels are exact.
- **Abstract vs theorem:** there is no theorem, so the comparison is between the abstract and the
  evaluation. The abstract's `100x` and `2x` are the extremes of the reported table rather than the
  typical case, and the phrase "deters attackers" describes a cost increase measured on fixed attacks,
  not a demonstrated infeasibility. The adaptive-attack section is the honest part of the claim, since
  it shows the two adversary goals conflict rather than showing that no adaptation works.

## Key Contributions

- A pro-active extraction defence that leaves model accuracy intact, by moving the cost onto the
  client instead of degrading the answer.
- The use of a per-query differential privacy budget as an information-leakage meter, calibrating
  puzzle difficulty to accumulated leakage rather than to raw query count.
- A fine-grained binary HashCash, replacing hexadecimal leading zeros so that difficulty can be tuned
  in single-bit steps and mapped onto a target solving time.
- A taxonomy of extraction attacks by data type, query count, adversary goal and what the victim
  returns, covering MixMatch, active learning, Knockoff, CopyCat CNN, Jacobian and DataFree.
- Three adaptive attacks against the defence, EntropyRev, WorstCase and a Sybil-style multi-account
  attacker, with the observation that minimising measured cost and maximising extracted information
  are opposing objectives.

## Key Definitions / Theorems

- **Model information leakage** is defined in prose as the amount of useful information a user gains
  from a set of queries, and is then operationalised as the PATE privacy budget accumulated by that
  user. There is no formal definition and no accompanying guarantee.
- **Fidelity and task-accuracy extraction** are restated as optimisation objectives over the
  substitute parameters, taken from the extraction literature rather than introduced here.
- **HashCash difficulty.** The expected number of trials for `k` leading zero bits is `2^k`, with
  variance `2^k(2^k − 1)`, verifiable in a single hash.
- No theorem, lemma or proposition appears anywhere in the paper.

## The unnamed quantity

The priced quantity is compute per query, expressed as a puzzle difficulty in leading zero bits and
therefore as an expected `2^k` hash evaluations, converted to seconds by a fitted linear model on the
logarithm of solving time. The difficulty is a function of one input, the absolute difference between
the user's accumulated PATE privacy cost and the cost a legitimate user would have accumulated over
the same number of queries. Reported outcomes are ratios of wall-clock, under `2x` for legitimate
users and up to `100x` for attackers, alongside the observation that attacker leakage accumulates up
to `7x` faster than benign leakage.

What the quantity lacks:

- **A definition.** No notion of extraction security is defined in terms of the imposed compute. The
  defence has no name as a security property, only as a mechanism.
- **An exponent.** The exponential `a^x` with `a = 1.0075` is a fitted curve chosen to hit the `2x`
  legitimate-user target, not an exponent relating attacker work to honest work. Nothing of the form
  `honest^{1+δ}` appears.
- **An adversary class.** The eight attacks are a benchmark, not a class. Nothing quantifies over
  algorithms, so an attack outside the benchmark that keeps its PATE consensus high while extracting
  is unpriced by construction, and the paper's own adaptive-attack section is the argument that such
  an attack is hard to build rather than a proof that it does not exist.
- **An assumption.** No hardness assumption underlies the puzzle beyond the standard preimage
  behaviour of the hash, which is never stated as an assumption.
- **A lower bound.** None. There is no bound on the queries or compute an attacker needs to extract
  under the defence, so the `100x` is a measurement against fixed attacks and not a floor.

The DP usage deserves its own line, because it is the part most likely to be misread. PATE is used
only to score a query. The released prediction is exact and unnoised, so the deployment satisfies no
`(ε, δ)` guarantee, and the accumulated budget is a leakage statistic rather than a privacy loss that
has been paid.

## Connections

- [Model Extraction (Accuracy vs Fidelity)](../concepts/model-extraction.md)
- [High Accuracy and High Fidelity Extraction of Neural Networks](jagielski-model-extraction.md)
  supplies the MixMatch attack that is hardest for this defence to price, because it needs few queries.
- [Cryptanalytic Extraction of Neural Network Models](cryptanalytic-extraction-nn.md) names the two
  cost coordinates, queries and compute, that this defence tries to inflate.
- [Exploring Connections Between Active Learning and Model Extraction](active-learning-model-extraction.md)
  supplies the active-learning attack in the benchmark, and the negative result that output
  randomisation with constant flip probability cannot work.
- [Proof-of-Learning](../concepts/proof-of-learning.md) and
  [Proof-of-Learning: Definitions and Practice](proof-of-learning.md) are the reactive counterpart,
  and are cited here as post-hoc rather than preventive.
- [Computational Differential Privacy](../concepts/computational-differential-privacy.md) is where a
  compute-bounded privacy guarantee would live. This paper does not make one.
- [Capacity Bounded Differential Privacy](capacity-bounded-dp.md) bounds the adversary by a function
  class rather than by compute, and is the nearest formal relative of what this defence gestures at.
- [Deep Learning with Differential Privacy](deep-learning-differential-privacy.md) is the DP-SGD
  approach the paper rejects for being unable to price an individual query.
- [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md)
- [Nicolas Papernot](../entities/nicolas-papernot.md)

## Open Questions / Limitations

- No guarantee of any kind is proved. A defence whose entire content is a cost ratio measured against
  a fixed attack suite is refuted by any attack that keeps teacher consensus high, and no argument
  rules that out.
- Statefulness. The cumulative accounting needs identified users. The stateless per-query variant
  proposed for Sybil attackers is described but neither implemented nor assessed.
- The leakage meter is only as good as the teacher ensemble, and the paper notes the Jacobian attack
  registers a low privacy cost while still being an effective fidelity attack.
- The legitimate baseline must be fitted from observed legitimate traffic. Populations whose costs
  differ widely are handled only by a suggestion to use bounds instead of a single baseline.
- Client compute is heterogeneous. A fixed difficulty in leading zero bits is a different cost to a
  phone and to a rack, which the calibration does not address.

## Quotes / Notable Passages

> we propose to impede model extraction by requiring users to complete a proof-of-work before they can
> read the model's predictions.

> our calibration applies tools from differential privacy to measure the information revealed by a
> query.

> The privacy cost is computed based on the consensus among teachers and it is smaller when teachers
> agree.
