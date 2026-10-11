---
title: Publicly-Verifiable Certificates for Statistical Algorithms
type: source
date_ingested: 2026-08-21
authors: [Michael Ngo, Michael P. Kim]
venue: "arXiv:2607.15528"
venue_evidence: "https://arxiv.org/abs/2607.15528; no refereed venue found by web search as of 2026-09-03"
year: 2026
tags: [learning-theory, statistical-query, verifiable-computation, cryptography]
claim_quantifier: conditional
antecedent: "The algorithm being certified is an adaptive statistical query algorithm making k queries to a tau-accurate SQ oracle. Theorem 2 requires it to be deterministic. Theorem 3 requires it to be randomized over O(1) epochs, correct against a public-state SQ oracle, and holds in the Random Oracle Model with computational soundness. Completeness assumes the prover and verifier hold the same distribution."
adversary_bound: "none on the cheating prover. Definition 3.2's universal soundness quantifies over computationally unbounded provers; the SQ restriction constrains the algorithm being certified and the verifier's query budget, not the adversary."
cls_target: training run
cls_family: evade audit
cls_phase: post hoc
cls_access: none
cls_write: responses
cls_frame: statistical
cls_party: auditor
cls_unit: samples
cls_tightness: relative
cls_baseline: n/a
cls_second_party: samples
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "Verifier sample complexity: mV ≤ O(log(k)/τ 2 )"
cls_evidence_src: "Thm 2 (§3.1)"
cls_reason: "party = auditor (the verifier), not the cheating prover, per the task's audit warning: soundness (Def 3.1/3.2) quantifies over an unrestricted prover, and the query/sample bound sits on the verifier and on the algorithm A being certified. frame = statistical, not compute: the paper states its own efficiency notion is statistical throughout ('efficiency ... primarily focuses on statistical resources, rather than computation'), and Corollary 6 is a barrier showing the statistical savings do NOT become computational. tightness = exponent because the verifier's O(log k) cost is stated directly against the honest prover's Θ~(sqrt k) cost (the paper's headline 'exponential gap'). Theorem 3 additionally proves computational soundness (PPT cheating prover, Random Oracle Model, Fiat-Shamir) for randomized SQ algorithms of O(1) epochs -- a different party (the cheating prover, not the verifier) under a different, secondary theorem; not reflected in this row per Rule 1, since the abstract leads with the statistical sample-complexity gap and says nothing about PPT/ROM. family = evade audit and target = training run are judgment calls: the paper is a certification/defense construction, not an attack paper, but its soundness game (cheating prover tries to get an invalid hypothesis accepted for a claimed SQ execution) is the closest fit in the vocabulary to what it defends against. write = responses: the cheating prover fabricates the transcript of query-answer pairs presented as the certificate. RECODE 2026-09-03 (R1, revision 7): tightness exponent -> relative. RECODE 2026-09-03 (R1, honest party unit): second_party none -> samples."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The paper introduces a non-interactive proof of learning. A **publicly-verifiable Certificate of
Statistical Validity**, or pvCSV, lets a well-resourced learner publish a hypothesis `h` with a
certificate `π` once, after which any downstream user holding their own distribution can read the pair
and decide whether the hypothesis is valid for *their* distribution. This replaces the interactive PAC
Verification framework of Goldwasser, Rothblum, Shafer and Yehudayoff, which requires prover and
verifier to be online together and which leaves every user who did not run the protocol trusting
whoever did.

The construction is concrete and simple. The prover runs the adaptive SQ algorithm `A` against its own
oracle, records the transcript of queries and answers, and publishes it as the certificate. The
verifier re-runs `A`, answering each query from the transcript rather than from its own oracle, and
rejects immediately if the execution ever calls for a query the transcript does not contain. If the
transcript is consistent, the verifier issues the recorded queries as a single non-adaptive batch to
its own oracle and checks each reported answer.

The payoff is a sample complexity gap. Adaptive data analysis is expensive, and answering `k`
adaptively chosen queries takes roughly `sqrt(k)` samples, a dependence that is essentially tight. But
once the query sequence exists, checking it is non-adaptive, so the verifier needs only `O(log k / τ²)`
samples. The verifier therefore certifies in exponentially fewer samples than learning would take. The
randomized case needs more machinery, a canonical-form lemma turning mixed-message private-query SQ
protocols into public-coin public-query ones, followed by a Fiat-Shamir compilation whose soundness
loss grows exponentially in the protocol's epoch complexity.

## Claim Boundary

- **Quantified over:** Theorem 2 quantifies over all deterministic SQ algorithms that learn a goal `G`
  with `k` adaptive queries. Theorem 3 quantifies over randomized SQ algorithms of constant epoch
  complexity that are correct against a public-state SQ oracle. The soundness property in both
  quantifies over all verifier distributions and over all prover strategies.
- **Antecedent:** as in the front matter. Completeness assumes `D_P = D_V`, and the paper flags that a
  robust completeness notion tolerating distributional closeness is left to future work. Theorem 3
  additionally lives in the Random Oracle Model and is computationally rather than statistically sound.
- **Adversary class: this is the field most likely to be misread, and it has been.** Definition 3.1
  states universal soundness for SQ protocols as holding "for any prover `P̃`", and Definition 3.2
  states it as holding "for any prover strategy". The paper then says in its own remarks that
  Definition 3.2 considers universal soundness with respect to computationally unbounded provers, and
  that the computationally sound variant restricts to probabilistic polynomial time in the Random
  Oracle Model. **No definition in this paper quantifies soundness over statistical query adversaries.**
  The SQ model enters in two other places. It is the model of the algorithm `A` being certified, and it
  is the access model that gives the verifier its query budget, a single non-adaptive batch of `k`
  queries answered to accuracy `τ`.
- **Does not establish:** any security notion for learning against a restricted adversary class. It
  also does not establish computational savings for the verifier, only statistical ones. The paper is
  explicit that efficiency here means statistical resources rather than computation, and that the
  verifier must re-run `A`, so verifier time scales roughly with the original algorithm's running time.
  A barrier is proved for the computational side, below.
- **Abstract vs theorem:** the abstract is faithful. It says the construction is in the context of
  adaptive SQ algorithms and reports the `O(log k)` against `Õ(sqrt k)` gap, both of which are the
  theorems. The misreading risk is external, in summarising "certificates for statistical algorithms"
  as soundness against statistical algorithms.

## The correction this page exists to record

An earlier note in this repository described this work as supplying SQ-quantified soundness, meaning a
security definition whose adversary is restricted to statistical queries. That reading is wrong and is
retracted. The cheating prover in Definition 3.1 and Definition 3.2 is unrestricted, and the paper
states in its own remarks on Definition 3.2 that soundness there is with respect to computationally
unbounded provers. The result is a **query-bounded verifier** result. The verifier is the party whose
statistical access is limited, to `O(log k / τ²)` samples and one non-adaptive batch of queries, and
the SQ model describes the algorithm under certification. Anyone looking here for a security definition
that quantifies over a restricted adversary class will not find one.

## Key Contributions

- Definition 3.2, the pvCSV, a non-interactive proof of statistical validity that any verifier can
  check against a distribution the prover never saw.
- Theorem 2. Every deterministic adaptive SQ algorithm making `k` queries to a `τ`-accurate oracle has
  a pvCSV with honest prover sample complexity `mP ≤ Õ(sqrt(k)/τ²)`, verifier sample complexity
  `mV ≤ O(log(k)/τ²)`, and certificate size `|π| ≤ O(k log(1/τ))`.
- Theorem 3. The same complexities for randomized SQ algorithms of `O(1)` epochs correct against a
  public-state SQ oracle, with computational soundness in the Random Oracle Model.
- Lemma 4, the canonical-form result. Any mixed-message, private-query SQ protocol can be compiled into
  a public-coin, public-query protocol with the same completeness and soundness, where the canonical
  verifier makes a single non-adaptive batch of `k` queries and the canonical prover makes at most `k`
  extra queries.
- Proposition 5. Verification of a large class of public-query SQ protocols can be made statistically
  non-adaptive, giving verifier sample complexity `O(log(k)/τ²)`.
- Corollary 6, the barrier. For a class of VC dimension `d`, any such SQ protocol that `ε`-PAC verifies
  it with `τ ≈ ε` forces the verifier to make `2^{Ω(sqrt d)}` statistical queries. Statistical savings
  therefore do not carry over to computational savings in this model.
- Proposition 7. The verifiers of these pvCSVs can be implemented under differential privacy at
  sample complexity `O(log(k)/τ² + log(k)/τε)`, essentially the non-private cost.

## Key Definitions / Theorems

- **Definition 3.1, universal soundness for SQ protocols.** An SQ protocol `(P, V)` has
  `γ`-universal soundness when for any verifier distribution `D_V`, any `τ_V`-accurate SQ oracle `O_V`
  for it, and **any prover `P̃`**, with probability at least `1 − γ` the interaction either outputs
  `g ∈ G(D_V)` or `V` rejects. The paper notes this is a restatement of standard soundness with the
  distribution renamed, and that its value lies in letting one reason about a prover and verifier
  holding different distributions, since an honest prover on `D_P` is a possible cheating prover from
  the perspective of a verifier on `D_V`.
- **Definition 3.2, pvCSV.** Completeness when `D_P = D_V`, plus universal soundness for any verifier
  distribution and any prover strategy. The remarks record that this is soundness against
  computationally unbounded provers, and that a computationally sound variant is proved in the Random
  Oracle Model.
- **Public-state versus oblivious SQ oracle.** A public-state oracle may choose its answers as a
  function of the algorithm's internal randomness. An oblivious oracle may not. Theorem 3 requires
  correctness against the stronger, public-state oracle.
- **Epoch complexity.** A randomized SQ algorithm runs in `ℓ` epochs when it decomposes into `ℓ`
  deterministic SQ algorithms each taking a fresh random string. The Fiat-Shamir soundness loss is
  exponential in `ℓ`, which is why Theorem 3 is stated for `O(1)` epochs.
- **Theorem 2, Theorem 3, Lemma 4, Proposition 5, Corollary 6, Proposition 7** as listed above.

## Connections

- [Statistical Query Model](../concepts/statistical-query-model.md) is the model of the algorithm being
  certified and of the verifier's access, and is not a restriction on the adversary here.
- [Adaptive Data Analysis](../concepts/adaptive-data-analysis.md) supplies the `sqrt(k)` sample cost
  that the `O(log k)` verifier cost is measured against.
- [Verifiable Computation](../concepts/verifiable-computation.md)
- [Proof-of-Learning](../concepts/proof-of-learning.md) and
  [Proof-of-Learning: Definitions and Practice](proof-of-learning.md) are the compute-witness analogue,
  where the transcript is a training trajectory rather than a query log.
- [Zero-Knowledge Verifiable AI Pipelines](zk-verifiable-ai-pipelines.md) and
  [ZK-ML Verification](../concepts/zk-ml-verification.md) are the cryptographic route to the same
  delegation goal.
- [Preventing False Discovery in Interactive Data Analysis is Hard](preventing-false-discovery-hard.md)
  is the hardness side of adaptive data analysis.
- [Computational Differential Privacy](../concepts/computational-differential-privacy.md) and
  [Deep Learning with Differential Privacy](deep-learning-differential-privacy.md) sit behind
  Proposition 7's private verifier.
- [Statistical Query Algorithms and Low-Degree Tests Are Almost Equivalent](brennan-sq-lowdegree-equivalence.md)
  is the bridge that would be needed if one wanted an SQ-bounded adversary, which this paper does not
  supply.

## Open Questions / Limitations

- Robust completeness. Completeness is stated only for `D_P = D_V`, and a notion tolerating a measured
  distributional gap is left open.
- Epoch complexity. Theorem 3 covers constant epochs, because the Fiat-Shamir soundness loss is
  exponential in the number of epochs. Algorithms with many epochs, which includes gradient descent
  read literally, are not covered.
- Computational efficiency. Corollary 6 shows that the statistical savings do not generically become
  computational, since the verifier's query count can be `2^{Ω(sqrt d)}`. The paper states that its
  notion of efficiency is statistical throughout.
- Distributional access. The pvCSV notion is developed for SQ access, and the paper notes that a more
  general notion of universal soundness would be needed for other forms of statistical access.
- Randomness. For randomized algorithms the prover cannot simply be trusted with the coins, which is
  what forces the public-coin epoch structure and the public-state oracle assumption.

## Quotes / Notable Passages

> Universal Soundness: for any verifier V with distribution D_V, for any (possibly-cheating) prover
> pair (h̃, π̃), if V accepts, then h̃ is actually valid for D_V.

> Definition 3.2 considers universal soundness with respect to computationally-unbounded provers.

> In these works, and in our paper, "efficiency" primarily focuses on statistical resources, rather
> than computation.
