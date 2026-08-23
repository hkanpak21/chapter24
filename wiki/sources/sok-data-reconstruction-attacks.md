---
title: "SoK: Data Reconstruction Attacks Against Machine Learning Models: Definition, Metrics, and Benchmark"
type: source
date_ingested: 2026-08-20
authors: [Rui Wen, Yiyong Liu, Michael Backes, Yang Zhang]
venue: venue unconfirmed from PDF (arXiv:2506.07888v1, 9 Jun 2025; formatted as a USENIX-style SoK with Ethics Considerations and acknowledgement of anonymous reviewers)
year: 2025
tags: [adversarial-ml, reconstruction, sample-complexity, learning-theory]
claim_quantifier: empirical
antecedent: "The benchmark conclusions are conditional on the vision domain, on the ten attacks selected, and on the choice of distance measure µ — the paper states that µ-exact reconstruction is 'a necessary and insufficient condition for the perfect reconstruction, depending on the choice of measure µ'. The definitional gap claim itself carries no antecedent; it is a survey observation."
cls_target: train data
cls_family: reconstruct
cls_phase: post hoc
cls_access: black box
cls_write: read only
cls_frame: none
cls_party: none
cls_unit: none
cls_tightness: unstated
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed:
cls_evidence: "absent"
cls_evidence_src: "no bound in Def 3.1, 3.2, 4.1-4.4; Open Questions: 'No computational quantity appears anywhere. The adversary is described by knowledge, never by compute, queries, or time.'"
cls_reason: "Extra Knowledge K (Def 3.1) has model access as black-box/white-box without fixing one, hence access=black box; the same axis also spans static/dynamic training type, and the ten-attack benchmark is predominantly the static (post-hoc, fixed released model) case, so phase=post hoc with the dynamic case as a documented exception. The cardinality constraint |D_rec|=|D_tar| closes an enumeration loophole but is not an adversary resource bound, so it does not populate unit."
cls_prov: S
cls_date: 2026-08-22
---

## Summary

A systematization of data reconstruction attacks whose stated premise is that the subfield lacks a
definition. The abstract says so directly:

> "there is currently no consensus on a formal definition of data reconstruction attacks or
> appropriate evaluation metrics for measuring their quality."

and §1 repeats it as the paper's motivating defect: "one of the major problems in the field of data
reconstruction is that there does not exist a rigorous and unified definition for the attack."

The repair proposed is a taxonomy plus a pair of metrics, and — unlike the extraction case in
[Beyond Labeling Oracles](beyond-labeling-oracles.md) — it *is* written down formally. Extra knowledge
`K` is factored into three axes (training type static/dynamic; model access black-box/white-box;
dataset access none/similar-distribution/same-distribution). A reconstruction algorithm is
`A : M × K → D` producing `D_rec = A^k(m)` of **the same cardinality as the target dataset** — a
deliberate stipulation, because unbounded output would let an adversary enumerate pixel combinations
and trivially subsume the target. Success is then parameterized by a distance measure `µ`:
`µ`-exact reconstruction when `µ(A^k(m), D_tar) = 0`, and `(ε, µ)`-approximate reconstruction when
`µ(A^k(m), D_tar) ≤ ε`.

The metric layer is where the paper is most careful, and where it concedes the most. Sample-level
distances (MSE, PSNR, SSIM) do not capture whether the reconstruction *covers* the dataset; a
train-a-model-on-the-reconstruction accuracy metric does not capture precision, demonstrated by a
counterexample built with data-free model extraction — a stolen model with high accuracy whose
training set is "vastly dissimilar" from the target. So the paper proposes two metrics: a
dataset-level FID distance, and a sample-level pair `(S-Dis, α)` where `S-Dis` is the averaged
minimal distance from each reconstructed sample to its nearest target sample and `α = |f(A^k(m))| /
|D_tar|` is coverage. Empirically, none of the ten evaluated attacks achieves exact reconstruction,
and reconstruction success correlates with model memorization — higher memorization of individual
samples, higher vulnerability; larger training sets, lower memorization and lower vulnerability. The
pattern replicates on Swin and MAE architectures and in the text domain (Vec2Text, prompt recovery).

## Claim Boundary

- **Quantified over:** the definitional-gap claim is about the data-reconstruction literature as a
  whole. Everything else is scoped to **the vision domain** — stated explicitly ("while our present
  investigation concerns the realm of vision") — and to ten named attacks across three families
  (optimization-based, training-based, analysis-based), on MNIST, CIFAR-10 and CelebA. Text-domain
  results are an extension in an appendix with two attacks, not part of the benchmark.
- **Antecedent:** `µ`-exact reconstruction is only as strong as `µ`. The paper states the dependency
  itself: it is "a necessary and insufficient condition for the perfect reconstruction, depending on
  the choice of measure µ". So the definition is a *schema* awaiting a measure, not a closed
  predicate — the same structural position as an unparameterized cost inequality, one layer up.
- **Does not establish:** (a) that reconstruction is hard, easy, or bounded — there is no hardness
  claim and no computational bound anywhere in the paper; (b) that the proposed definition is the
  right one or is complete — it is offered as a first proposal ("we take the first step"); (c) that
  memorization *causes* reconstruction vulnerability — the reported relationship is correlational
  ("strongly correlated with reconstruction performance"); (d) anything about adversary compute — the
  adversary is characterized entirely by its *knowledge* (`K`), never by its resources.
- **Abstract vs theorem:** none found. There are no theorems; the abstract's claims about proposing a
  taxonomy, metrics and a benchmark match the body. The one place to read carefully is that the
  abstract's "formal definitions of data reconstruction attacks" delivers Definitions 3.1–3.2 and
  4.1–4.4, which are definitions of the *object and its measurement*, not of *success against a
  bounded adversary*.

## Key Contributions

- The explicit statement that data reconstruction has **no consensus formal definition and no agreed
  metrics** — and a diagnosis of why (diversity of threat models and training paradigms).
- A three-axis taxonomy of adversary knowledge (training type, model access, dataset access).
- A formal reconstruction algorithm signature with a **cardinality constraint** on the output, closing
  the enumerate-everything loophole.
- A stated desiderata list for metrics: quantifiability, consistency, precision, diversity.
- Two metrics — dataset-level FID, and sample-level `(S-Dis, α)` with explicit coverage — plus an
  LLM-as-judge visual metric.
- A benchmark of ten attacks, and the finding that no attack achieves exact reconstruction.

## Key Definitions / Theorems

- **Definition 3.1 (Extra Knowledge `K`)**: three dimensions — training type (static or dynamic),
  model access (black-box or white-box), dataset access (no data / similar distribution / same
  distribution).
- **Definition 3.2 (Reconstruction Algorithm)**: `A : M × K → D`, `D_rec = A^k(m)`, with
  `|D_rec| = |D_tar|`. In the static setting `D_tar` is the whole training set; in the dynamic
  setting it is the subset that directly contributes to the model change.
- **Definition 4.1 (Dataset-level metric)**: `µ : D × D → R`, instantiated as FID.
- **Definition 4.2 (Sample-level metric)**: `µ : D × D → R²` giving `(S-Dis, α)`, with
  `S-Dis = (1/|A^k(m)|) Σ d(x_i, f(x_i))` for the nearest-target map `f`, and coverage
  `α = |f(A^k(m))| / |D_tar| ∈ (0,1]`.
- **Definition 4.3 (`µ`-Exact Reconstruction)**: `µ(A^k(m), D_tar) = 0`.
- **Definition 4.4 (`(ε, µ)`-Approximate Reconstruction)**: `µ(A^k(m), D_tar) ≤ ε`.

Nothing here is a hardness statement. `ε` is a reconstruction-quality tolerance, not a security
parameter, and no adversary resource appears in any definition.

## Connections

- **The reconstruction entry in the batch's pattern**: three subfields, three admissions that the
  central success predicate is undefined. See also [Beyond Labeling Oracles](beyond-labeling-oracles.md)
  (extraction) and [On the Necessity of Auditable Algorithmic Definitions](auditable-unlearning-definitions.md)
  (unlearning).
- **The definition this paper says does not exist, exists — in cryptographic units.**
  [Cohen et al., *Data Reconstruction: When You See It and When You Don't*](cohen-data-reconstruction.md)
  gives computational Narcissus resiliency (Def. C.1) and proves it equivalent to one-wayness. This SoK
  does not cite it. The two papers are answering the same question in incompatible units: `(ε, µ)`
  approximation quality versus poly-time adversarial advantage.
- **The separation this paper's `ε` does not make.**
  [Dinur–Nissim](dinur-nissim-revealing-information.md) already separates an exponential adversary from
  a polynomially bounded one for reconstruction; that separation is restated as
  [computational vs statistical memorization](../concepts/computational-vs-statistical-memorization.md)
  by [Kaplan et al.](kaplan-bayesian-memorization-reconstruction.md). An SoK organized on *knowledge*
  axes has no place to record which side of that line an attack sits on.
- The memorization–vulnerability correlation is the empirical shadow of the memorization theory on
  [computational vs statistical memorization](../concepts/computational-vs-statistical-memorization.md).
- Reconstruction as fibre navigation:
  [fiber-of-the-training-map](../concepts/fiber-of-the-training-map.md). The cardinality constraint
  `|D_rec| = |D_tar|` is, read structurally, a constraint on which fibre elements count as an answer.
- Sample-complexity pricing of a *related* attack (MIA) in information-theoretic units:
  [Haghifam–Smith–Ullman](haghifam-sample-complexity-mia.md). The SoK's §1 argues MIA and
  reconstruction are different problems — decision versus search, sample-level versus dataset-level —
  and notes nobody has built reconstruction out of MIA.
- Concept: [Data Reconstruction Attack](../concepts/data-reconstruction-attack.md).

## Open Questions / Limitations

- The definition is parameterized by `µ` and is therefore only as sharp as the measure supplied; the
  paper says so.
- No computational quantity appears anywhere. The adversary is described by knowledge, never by
  compute, queries, or time. A "successful" reconstruction under Definition 4.4 says nothing about
  what it cost.
- Vision-first by design; the text extension is exploratory.
- The LLM-as-judge metric substitutes a model for human judgement and inherits that model's biases;
  the paper offers it as a mitigation of visualization's subjectivity, not a solution.
- Memorization is correlated with vulnerability, but no mechanism or bound links them.

## Quotes / Notable Passages

> "there is currently no consensus on a formal definition of data reconstruction attacks or
> appropriate evaluation metrics for measuring their quality."

> "one of the major problems in the field of data reconstruction is that there does not exist a
> rigorous and unified definition for the attack."

> "We argue that without a clear-stated definition and metrics, it is hard to conduct further
> investigation in this direction."

> "Note that µ-Exact Reconstruction is a necessary and insufficient condition for the perfect
> reconstruction, depending on the choice of measure µ"

> "An attack that can only recover a few samples accurately is not regarded as a successful
> reconstruction attack."

> "Overall, none of the attacks can achieve exact reconstruction, and their quality varies
> significantly."
