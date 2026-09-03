---
title: "LAMP: Extracting Text from Gradients with Language Model Priors"
type: source
date_ingested: 2026-08-22
authors: [Mislav Balunović, Dimitar I. Dimitrov, Nikola Jovanović, Martin Vechev]
venue: "NeurIPS 2022"
venue_evidence: "dblp: conf/nips/BalunovicDJV22, inproceedings, confirms the PDF's own stated venue"
year: 2022
tags: [adversarial-ml, reconstruction, robustness]
claim_quantifier: empirical
antecedent: "The server observes one client gradient computed on the exact parameter snapshot it distributed; the task is binary classification, so all label assignments can be enumerated; the sequence length is assumed known (with the stated fallback of running the attack for every length); and the adversary holds a pretrained GPT-2 sharing the target BERT model's tokenizer."
adversary_bound: "None formally. The adversary is an honest-but-curious federated-learning server that does not modify the protocol. It is bounded by the channel (one gradient) and by auxiliary knowledge (an auxiliary language model, known sequence length). Cost is reported in wall-clock GPU hours and in optimization steps, never as a complexity class."
date_verified: 2026-08-20
cls_target: train data
cls_family: reconstruct
cls_phase: train time
cls_access: gradients
cls_write: read only
cls_frame: compute
cls_party: attacker
cls_unit: time
cls_tightness: measured
cls_baseline: absent
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: none
cls_assessed: implicit
cls_evidence: "They took between 50 hours per experiment for the LAMPCos and LAMPL2 +L1 methods and 70 hours for TAG, which executes two times more continuous optimization steps."
cls_evidence_src: Appendix E
cls_reason: "No formal adversary bound exists (adversary_bound: none in front matter); party/unit/tightness instead record the attack's only priced quantity, the attacker's own GPU-hours cost, per the assigning note. baseline=absent because the paper reports no gradient-free or language-model-only control."
cls_prov: S
cls_date: 2026-08-22
---

> **Provenance.** Read from the primary PDF: abstract, §1, §2, §3 (federated learning, gradient leakage
> attacks, transformers, perplexity), §4 (the attack), §5 (datasets, models, metrics, experimental
> setup, main results, batch sizes, ablation, defended networks), Appendix D (hardware and
> hyperparameters), Appendix E (total runtime). Quoted passages verbatim.

## Summary

This is an **empirical attack paper**. It defines no security game, states no success predicate, and
proves nothing; it reports ROUGE scores. That is worth recording plainly, because the paper is
frequently cited as evidence that gradients leak, and what it establishes is that a specific optimizer
with a specific prior recovers a specific fraction of tokens on three small datasets.

The **channel** is precise and narrow. In federated learning with `C` clients, the server distributes
parameters `θ^k` at iteration `k`; each client computes `∇_{θ^k} L(x*_c, y*_c)` on its own private
sample and returns it. The adversary is the server, or a party that has compromised it, and what it
observes is exactly that one gradient, at exactly the snapshot it sent. The attack solves
`argmin_{(x_c,y_c)} δ(∇_{θ^k} L(x*_c, y*_c), ∇_{θ^k} L(x_c, y_c))` for a distance `δ` — cosine in
LAMP_Cos, an `L2 + L1` combination in LAMP_{L2+L1}. The server is **honest-but-curious**: it does not
modify the training protocol, which distinguishes this from malicious-server attacks that plant
parameters. Batch normalization statistics are **not** assumed known. Labels are recovered by
enumeration, which works because the three tasks are binary classification.

The contribution over prior text attacks (DLG, TAG) is two mechanisms. First, a **language model
prior**: candidate reconstructions are scored by a pretrained GPT-2's perplexity as well as by gradient
match, pushing the search toward natural text. Second, **alternating continuous and discrete
optimization**: gradient descent on embeddings, interleaved with discrete token transformations (such as
moving a token) whose candidates are ranked by the combined reconstruction loss and perplexity. The
final reconstruction maps each embedding to its nearest vocabulary neighbour.

Results are on CoLA, SST-2 and RottenTomatoes with BERT_BASE, BERT_LARGE, TinyBERT_6 and a fine-tuned
BERT_BASE, over 100 sequences per setting. At batch size 1 on CoLA/BERT_BASE, LAMP_Cos reaches
ROUGE-1/2/L of 89.6/51.9/76.2 against TAG's 78.9/10.2/53.3 and DLG's 59.3/7.7/46.2. The paper claims to
be the first to recover inputs from batch sizes greater than 1 in this domain, and reports batch sizes 2
and 4, FedAvg as well as FedSGD, fine-tuned targets, and two defences (Gaussian noise on gradients, and
zeroing a fraction of gradient entries).

## Claim Boundary

- **Quantified over:** three binary-classification datasets (CoLA, SST-2, RottenTomatoes), four
  transformer configurations, batch sizes 1, 2 and 4, 100 sequences evaluated per setting. Nothing is
  quantified over models, over text, or over federated deployments in general.
- **Antecedent:** named individually in the front matter. Two deserve emphasis. The **known sequence
  length** is assumed *"for simplicity"* with the argument that the adversary could otherwise run the
  attack once per candidate length — which multiplies the already-reported cost by the number of
  candidate lengths and is not measured. The **binary classification** setting is what makes label
  recovery free; the paper notes that this makes the setting harder than the masking setting of prior
  work in one respect while removing the label problem in another.
- **Which party is constrained, and in what resource:** the adversary, in *channel* and in *protocol
  compliance*. It sees one gradient at one known snapshot and may not modify the protocol. It is not
  constrained in computation. The defender is constrained only in the defence experiments, by the noise
  scale `σ` or the gradient-masking fraction.
- **The success criterion:** **not formally defined.** Success is reported as ROUGE-1, ROUGE-2 and
  ROUGE-L F-scores against the true sequence — recovered unigrams, recovered bigrams, and the longest
  matching subsequence as a fraction of sequence length. These are continuous scores with no threshold;
  no ROUGE value is declared to constitute a reconstruction. The criterion is therefore
  tolerance-carrying in effect and unparameterized in statement, which is the opposite of
  [reconstruction robustness](reconstructing-informed-adversaries.md), where the tolerance `η` is an
  explicit parameter of the definition.
- **The baseline:** prior attacks, DLG and TAG, reimplemented by the authors for TAG. There is no
  model-free or gradient-free baseline — nothing measures what ROUGE score a language model alone
  achieves on these sentences without the gradient, which is the natural null for an attack whose main
  new ingredient is a language model prior. The ablation (Table 4) isolates the contribution of the
  prior against LAMP's own variants, not against a no-gradient control.
- **Does not establish:**
  - **not** that federated learning leaks in deployment. Every experiment is a single client's
    FedSGD-style update on a short sentence, with the length known.
  - **not** a bound of any kind. There is no claim that these ROUGE scores are near-optimal, and no
    lower bound on what the channel permits.
  - **not** that the defences fail. Table 5 shows degradation with `σ`, alongside the target task's MCC
    dropping from 0.551 at `σ = 0.001` to 0.364 at `σ = 0.01`; the paper's reading is that defences must
    be evaluated against strong attacks, not that noise is ineffective.
  - **not** anything about long documents. The datasets were chosen for short sequences — 5 to 9 words
    (CoLA), 3 to 13 (SST-2), 14 to 27 (RottenTomatoes) — because prior work established length as the
    limiting factor.
  - **not** a comparison against APRIL, whose exact-leakage technique is excluded on the grounds that it
    assumes batch size 1 and learnable positional embeddings.
- **Abstract vs theorem:** none found, with one phrase to note. The abstract's *"we are the first to
  recover inputs from batch sizes larger than 1 for textual models"* is a priority claim about the
  literature, not a measurement, and the paper qualifies it in §2 by excluding malicious-server attacks
  and a concurrent work limited to jointly trained token embeddings. The closing claim that gradient
  updates *"leak more information than previously thought"* is a comparison to prior attacks, which is
  what the tables support.

## Key Contributions

- **LAMP**: gradient inversion for text that adds a pretrained language model's perplexity to the
  reconstruction objective and alternates continuous embedding optimization with discrete token
  transformations.
- A two-step initialization — 500 Gaussian samples ranked by gradient loss, then 500 permutations of the
  best — reported as materially useful in the ablation.
- The first reported text reconstruction from gradients at batch sizes above 1 in this threat model, and
  evaluation against FedAvg as well as FedSGD.
- Evaluation against already fine-tuned targets, which prior vision work had shown to be harder.
- Evaluation against two defences, Gaussian noise on gradients and gradient masking, with the target
  task's utility reported alongside.
- **A reported cost.** Appendix E gives wall-clock GPU time per experiment, which is unusual in this
  literature and is the paper's most directly usable number for a survey that prices adversaries.

## Key Definitions / Theorems

None. The two formal objects in the paper are the attack's objective and the channel it reads.

**The channel.** At iteration `k`, client `c` computes `∇_{θ^k} L(x*_c, y*_c)` on a sample from its own
dataset and returns it; the server aggregates
`θ^{k+1} = θ^k − (λ/C) Σ_{c=1}^{C} ∇_{θ^k} L(x*_c, y*_c)`. The adversary observes the client's gradient.

**The objective.** `argmin_{(x_c,y_c)} δ(∇_{θ^k} L(x*_c, y*_c), ∇_{θ^k} L(x_c, y_c))`, reducing to
`argmin_{x_c} δ(∇_{θ^k} L(x*_c, y*_c), ∇_{θ^k} L(x_c, y*_c))` when the label is known.

**The prior.** Perplexity of a token sequence under an auxiliary language model,
`L_lm(t_1,...,t_n) = −(1/n) Σ_{l=0}^{n−1} log P(t_{l+1} | t_1,...,t_l)`, combined with the
reconstruction loss to rank discrete candidates.

**Reported cost.** BERT_LARGE runs took *"between 50 hours per experiment for the LAMPCos and
LAMPL2 +L1 methods and 70 hours for TAG"*; batch-size-1 runs on the other networks took 8 to 16 hours;
batch-size-4 runs took 8 to 36 hours, with LAMP up to 4× slower than the baselines because of the
discrete step. Hardware: a single NVIDIA RTX 2080 Ti (11 GB), except BERT_LARGE on a single RTX 3090 Ti
(24 GB). Optimization budget: 2000 continuous steps for BERT_BASE and TinyBERT_6, 5000 for BERT_LARGE,
against 2500 and 10 000 for the baselines.

## Connections

- [Data Reconstruction Attack](../concepts/data-reconstruction-attack.md) — LAMP is a reconstruction
  attack whose extra knowledge is a gradient and a language model rather than a dataset.
- [Reconstructing Training Data with Informed Adversaries](reconstructing-informed-adversaries.md) —
  the contrast in channel is drawn there: *"whilst a gradient leakage adversary has access to
  information involving only a mini-batch of training points, our attacks needs to invert the entire
  training procedure."* It is also the paper that supplies the tolerance parameter LAMP's evaluation
  lacks.
- [SoK: Data Reconstruction Attacks](sok-data-reconstruction-attacks.md) — the taxonomy in which
  gradient inversion is the dynamic-training, white-box case.
- [Deep Learning with Differential Privacy](deep-learning-differential-privacy.md) — the defence
  §5 approximates by adding Gaussian noise to gradients.
- [Language Models: Do They Preserve Privacy?](language-model-preserve-privacy.md) — the other direction
  of language-model leakage, from the trained model rather than from the gradient.
- [Membership Inference Attacks Against Machine Learning Models](membership-inference-shokri.md) — the
  weaker leakage question, one bit rather than the record.
- [SoK: Security and Privacy in Machine Learning](sok-security-privacy-machine-learning.md) — places
  this in the confidentiality-of-training-data cell of its goal axis; the federated channel postdates the
  taxonomy.
- [Blind Baseline](../concepts/blind-baseline.md) — the missing control here. An attack whose novelty is
  a language model prior wants a language-model-only baseline, and the paper does not report one.
- [Attaxonomy](attaxonomy.md), [Adversary Knowledge Taxonomy](../concepts/adversary-knowledge-taxonomy.md).

## Open Questions / Limitations

- Success is never defined. Without a threshold on ROUGE, "reconstructed" is a matter of reading a
  table, and two attacks with equal ROUGE-1 and different ROUGE-2 cannot be ordered by any stated
  criterion.
- The known-sequence-length assumption is waved away by an enumeration argument whose cost is never
  added to the reported hours.
- No baseline that omits the gradient. The paper's ablation removes LAMP's components but never the
  channel, so the fraction of the ROUGE score attributable to English rather than to leakage is not
  measured.
- Batch sizes stop at 4, and the trend across 1, 2, 4 is degradation. Where the attack stops working is
  not located.
- Only binary classification tasks, only short sequences, only BERT-family targets.
- The privacy-utility trade-off under the noise defence is reported but not characterised; no `ε` is
  computed for any of the `σ` values, so the defence is not connected to a formal guarantee.

## Quotes / Notable Passages

> A gradient leakage attack is an attack executed by the server (or a party which compromised it) that
> tries to obtain the private data (x∗c , yc∗ ) of a client using the gradient updates ∇θk L(x∗c , yc∗ )
> sent to the server.

(§3.1. The channel, stated exactly.)

> Gradient leakage attacks usually assume honest-but-curious servers which are not allowed to modify the
> federated training protocol outlined above.

(§3.1. The protocol-compliance constraint, which is what separates this from malicious-server attacks.)

> Following TAG [3], we measure the success of our methods based on the ROUGE family of metrics [20].

(§5. The whole of the paper's success criterion.)

> for simplicity we assume the lengths of sequences are known, as otherwise an adversary can simply run
> the attack for all possible lengths

(§5. An assumption discharged by an argument about cost, in a paper that elsewhere measures cost in
tens of hours.)

> They took between 50 hours per experiment for the LAMPCos and LAMPL2 +L1 methods and 70 hours for TAG,
> which executes two times more continuous optimization steps.

(Appendix E. The reported price of the attack.)
