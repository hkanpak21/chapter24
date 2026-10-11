---
title: "Proof-of-Learning: Definitions and Practice"
type: source
date_ingested: 2026-07-26
date_verified: 2026-08-20
authors: [Hengrui Jia, Mohammad Yaghini, Christopher A. Choquette-Choo, Natalie Dullerud, Anvith Thudi, Varun Chandrasekaran, Nicolas Papernot]
venue: "IEEE S&P 2021"
venue_evidence: "dblp: conf/sp/JiaYCDTCP21 (inproceedings, IEEE S&P 2021, pp. 1039-1056, DOI 10.1109/SP40001.2021.00106); confirms the PDF's own stated venue"
year: 2021
tags: [complexity theory, adversarial-ml, certification, hardness-reductions, verifiable-computation]
claim_quantifier: conditional
antecedent: "The compute-comparison claim rests on the paper's own Conjecture 1, which the authors state because they are \"not aware of a mechanism to prove this formally.\" The two actual theorems (entropy growth, reverse entropy growth) assume i.i.d. hardware/library noise `z` in the training process; the paper notes counter-based PRNGs can remove that noise, voiding the assumption. Nothing rests on a standard complexity assumption."
cls_target: training run
cls_family: forge
cls_phase: post hoc
cls_access: white box
cls_write: model
cls_frame: compute
cls_party: attacker
cls_unit: time
cls_tightness: relative
cls_baseline: absent
cls_baseline_checked: yes
cls_second_party: time
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "Property 2. Let CA be the cost random variable associated with any spoofing strategy attempted by any A aside from the honest strategy (i.e. training fWT ). We require that E[CT ] ≤ E[CA ]"
cls_evidence_src: "Section III, Property 2, raw/JYC+21_ProofOfLearning.pdf"
cls_reason: "Hand-classified 2026-08-22 against codebook revision 2, then migrated through revisions 3 to 5. Carries no verbatim evidence quote, unlike the delegated rows. RECODE 2026-09-03 (R1, revision 7): tightness unstated -> relative. RECODE 2026-09-03 (R1, honest party unit): second_party none -> time."
cls_prov: P
cls_date: 2026-08-22
---

> **Provenance.** Verified against the primary PDF on 2026-08-20 (`raw/JYC+21_ProofOfLearning.pdf`,
> extracted with `pdftotext`). The earlier secondhand-sweep banner is **retired**: that version of this
> page reported *one* bare compute inequality. There are **three**, and all three are quoted verbatim
> below. Slug and inbound links are unchanged.

## Summary

A prover `T` trains a model and logs the training trajectory; the proof `P(T, f_{W_T}) = (W, I, H, A)`
is that log — ordered sets of weight checkpoints, batch indices, data signatures, and auxiliary
metadata. A verifier `V` re-executes a *subset* of the logged gradient steps (the `top-Q` largest
updates per epoch) and accepts if each re-execution lands within a tolerance `δ` of the logged next
checkpoint. Verification is duplicated execution, not cryptography: the paper explicitly forgoes
interactive proof systems so that the training algorithm need not be modified.

The security story is entirely about **compute accounting**. A *spoof* is a proof produced by an
adversary `A` who has `W_T` but not the log; the paper's threat model calls a spoof **dishonest**
exactly when it cost less than honest training. Around that notion the paper writes three separate
cost inequalities over the random variables `C_T` (trainer cost), `C_V` (verifier cost), and `C_A`
(adversary cost). **None of the three is a theorem about the construction.** Properties 1 and 2 sit
in §IV-B under the heading "Desired Guarantees", introduced by the sentence "We formalize the
computational requirements below"; Definition 2 is a definition. The two objects the paper actually
*proves* — Theorem 1 (entropy of the forward training process grows linearly in `T`) and Theorem 2
(the unconstrained reverse process has entropy `H(Θ_{−T}) ≥ H(Θ_T)`) — are information-theoretic
statements about path multiplicity, not cost bounds.

The gap between the two is closed only by prose, and the paper says so. After an argument that any
numerical solve of the inverse gradient step `β(W_{t−1}) = 0` costs at least one gradient evaluation,
§VII-B3a concludes: *"attempting to create a PoL such that `P(A, f_{W_T}) ≠ P(T, f_{W_T})` but that
passes verification would be at least as computationally expensive as what it took `T`."* Then, two
pages later: *"given that we are not aware of a mechanism to prove this formally, we present the
following as a conjecture"* — **Conjecture 1**. So the central security claim is a conjecture in the
body and a result in the abstract. That discrepancy is recorded in **Claim Boundary** below, and it
was subsequently vindicated as a real gap by the authors' own follow-up,
[Proof-of-Learning is Currently More Broken Than You Think](pol-more-broken.md).

## Claim Boundary

- **Quantified over:** Property 2 quantifies universally over adversaries — `C_A` is "the cost random
  variable associated with any spoofing strategy attempted by any `A` aside from the honest strategy."
  No resource class, no circuit size, no oracle model, no algorithm family. The adversary is
  constrained only by the threat model's *information*: full knowledge of architecture, weights, loss,
  optimizer, hyperparameters, and the training set, but **not** the randomness sources (batching,
  initialization, seeds, accelerator nondeterminism). The only *analysed* adversaries are two
  hand-enumerated families — inverse gradient methods (backwards) and directed retraining (forwards) —
  and the analysis of both is empirical.
- **Antecedent:** for the compute claim, the paper's own **Conjecture 1**, stated for numerical
  root-finding methods only. For Theorems 1 and 2, the presence of i.i.d. noise `z` arising from
  hardware and low-level libraries; §VIII concedes counter-based PRNGs "can potentially remove most, if
  not all, noise in the training process", which would collapse the entropy argument. No standard
  cryptographic or fine-grained assumption (no OWF, no SETH, no lattice problem) appears anywhere.
- **Does not establish:** (i) that spoofing is *hard* in any complexity-theoretic sense — there is no
  reduction to any reference problem; (ii) that Property 2 *holds* for the proposed construction — it is
  a requirement placed on schemes, and the only case where the paper asserts it is satisfied is the
  trivial one, the "honest spoof" of simply retraining, where `E[C_A] ≥ E[C_T]` by definition; (iii)
  anything about extraction, surrogate models, or connecting a model to a distillate — §VIII disclaims
  all three; (iv) any guarantee for long chains of PoLs, since the success probability "degrades
  multiplicatively with each usage."
- **Abstract vs theorem:** the abstract states as a finding that *"our analyses and experiments show
  that an adversary seeking to illegitimately manufacture a proof-of-learning needs to perform at least
  as much work than is needed for gradient descent itself."* The body states the same content as
  **Conjecture 1**, prefaced by the authors' admission that they cannot prove it. The abstract also
  says "Our analysis shows that inverting gradient descent takes at least as much work as training"
  (§I) — again, no such theorem exists in the paper. This is the sharpest abstract-vs-body gap in the
  compute-accounting batch, and it is not a reading artifact: `F+23` opens by saying the original
  authors "were unable to provide a formal analysis of security for the proof verification mechanism
  they proposed."

## The unnamed quantity

The paper writes the quantity three times, as an expectation over cost random variables that bundle
computation and storage together ("the cost (both computation and storage) associated with `T`
training `f_{W_T}`"). Verbatim:

- **Property 1** — verifier cost at most trainer cost:
  > "Let CT denote a random variable representing the cost (both computation and storage) associated
  > with T training fWT . Let CV denote the cost random variable of the verification procedure. We thus
  > require that
  > E[CV ] ≤ E[CT ]"

- **Property 2** — trainer cost at most any spoofing adversary's cost:
  > "Let CA be the cost random variable associated with any spoofing strategy attempted by any A aside
  > from the honest strategy (i.e. training fWT ). We require that
  > E[CT ] ≤ E[CA ]"

- **Definition 2 (Dishonest Spoof)** — the adversary-cheaper-than-trainer threshold:
  > "Any spoof for a prover's model fWT that passes verification, and where the adversary expends fewer
  > computational resources than the trainer, i.e., E[CA ] < E[CT ], is dishonest."

What each one lacks, specifically:

| Missing | Property 1 | Property 2 | Definition 2 |
|---|---|---|---|
| A unit for `C` (FLOPs? steps? wall-clock? bytes?) | missing | missing | missing |
| An exponent or ratio parameter (`honest^{1+δ}`, `c·E`) | missing | missing | missing |
| An adversary class (circuit size, algorithm family, oracle model) | n/a | missing — "any `A`" | missing |
| An assumption it is conditional on | none | none (Conjecture 1 is offered *instead* of a proof) | none |
| A lower bound proving it | none | none | n/a (definition) |
| Asymptotic parameter (security parameter, `n`, `T`) | absent | absent | absent |

Two further notes on the shape. First, Property 1 and Property 2 are **desiderata**, aligned with the
qualitative goals `G1`–`G6` in the same section (`G2. Security`, `G3. Verification Efficiency` — the
latter hedged with "ideally"); they are conditions a PoL scheme *should* satisfy, not properties the
construction is shown to have. Second, the inequalities are **non-strict and unnormalised**: `E[C_T] ≤
E[C_A]` is satisfied by an adversary who spends one extra FLOP. Nothing in the paper distinguishes
"barely more expensive" from "prohibitively more expensive", which is exactly the distinction a
δ-indexed or exponent-indexed family would supply. Compare `F+23`'s **Definition 6**, which does index
the ratio (`E[C(F(D, W_T))] < cE`, `c ∈ [0,1)`) — a multiplicative constant, still not an exponent, and
attached to an *assumption* rather than a theorem.

## Key Contributions

- The PoL notion: proof = training trajectory; verification = spot-checked duplicated execution.
- The three compute inequalities above, and the `E[C_A] < E[C_T]` dishonesty threshold.
- The `top-Q` verification heuristic: verify the `Q` largest-norm updates per epoch, trading confidence
  against verifier cost. (This heuristic is the attack surface both later papers exploit.)
- A Kolmogorov–Smirnov test on the claimed initial weights, to force the spoofer's chain back to a
  distribution in a public pool of known initialisation schemes.
- Chain-of-trust: a proof may start from pre-trained weights that themselves carry a valid PoL.

## Key Definitions / Theorems

- **Definition 1 (PoL)**: `P(T, f_{W_T}) = (W, I, H, A)`, ordered sets indexed by step `t ∈ [T]`.
- **Definition 2 (Dishonest Spoof)**: quoted above.
- **Property 1 / Property 2**: quoted above — **requirements, not results**.
- **Theorem 1 (Entropy Growth)**: "The entropy of the training process ΘT grows linearly in the number
  of training steps T." Proved, from the entropy rate of a Markov process plus the noise term `H(z_0)`.
  Used to argue *retraining-based* spoofing (reproducing the log exactly) is hopeless — which cuts
  against reproducibility for the honest prover too.
- **Theorem 2 (Reverse Entropy Growth)**: the unconstrained reverse process is Markov and has
  `H(Θ_{−T}) ≥ H(Θ_T)`, with equality iff the conditional gradient is deterministic. The paper does
  **not** verify the equality condition for DNNs — it hypothesises it from confidence intervals in
  Figures 11 and 13b and leaves "the rigorous verification of these conditions" to future work.
- **Conjecture 1**: "Inverting a training sequence using numerical root finding methods will always be
  at least as computationally expensive as training, given the same model." Unproved, and scoped to
  numerical root-finding.
- Four spoofing scenarios (retraining-based, stochastic, structurally correct, distillation-based) and
  two analysed strategies (inverse gradient methods, directed retraining: PoL concatenation and
  directed weight minimisation). The concatenation attack is defeated *empirically* by `top-Q`, and the
  paper itself flags the escape: an adversary who knows `Q` "may make Q (or more) legitimate updates in
  every epoch by training with an arbitrarily large learning rate, which will bypass Algorithm 2."
  `F+23` builds precisely that attack.

## Connections

- **Broken, then re-broken.** Zhang, Liu, Ding, Wang, Wu, Ren, *"Adversarial examples" for
  proof-of-learning*, S&P 2022 (arXiv:2108.09454) — first counter-example. Then
  [Fang et al.](pol-more-broken.md), which shows Zhang et al. targeted a weakened instantiation and
  gives reproducible, far cheaper attacks, while formalising the missing assumptions and showing they
  "reduce to open problems in learning theory." *(Venue for Zhang et al. taken from the bibliography of
  `DJY+25_PoLO.pdf`; the F+23 PDF lists it as an arXiv preprint only.)*
- **Successor schemes that keep the inequality and change the security notion.**
  [PoLO](polo-proof-of-learning-ownership.md) replaces trajectory replay with chained watermarks and
  reports a measured `1.1–4×` forging ratio; [PoL with Incentive
  Security](pol-incentive-security.md) abandons Byzantine security for a game-theoretic guarantee,
  citing `F+23` as the reason it cannot be had.
- **Lifted into governance.** [What does it take to catch a Chinchilla?](catch-a-chinchilla-compute-monitoring.md)
  §5.1 defines **Proof-of-Training-Transcript** as a strictly harder variant of this problem — the
  adversary knows the true transcript *and* may spend more than the original training compute — and
  parameterises it as `J`-efficient and `F`-hard. That is a compute-indexed definition of the same
  quantity, still with no construction proved to meet it.
- Concepts: [Proof-of-Learning (the notion)](../concepts/proof-of-learning.md),
  [Verifiable Computation](../concepts/verifiable-computation.md),
  [Fiber of the Training Map](../concepts/fiber-of-the-training-map.md),
  [Compute Monitoring](../concepts/compute-monitoring.md).
- **The same quantity as fiber navigation, priced in compute.** A spoof is a point of the training
  map's fiber over `W_T` plus a path to it; Property 2 asserts that finding both costs at least what
  the honest path cost. See [Fiber of the Training Map](../concepts/fiber-of-the-training-map.md).
- **Adjacent forging line** *(not from this PDF)*: [Thudi et al., USENIX Security
  2022](auditable-unlearning-definitions.md) takes the PoL log as its definition of dataset
  feasibility while disclaiming any attack on PoL; Kong, Roy Chowdhury, Chaudhuri arXiv:2303.03648
  (proofs of repudiation); [Suliman et al.](suliman-data-forging-attacks.md);
  [Zhang et al. ICML'24](unlearning-verification-fragile.md), whose Prop. 4.5 writes an actual ratio —
  but in wall-clock complexity, not as a security parameter.
- **The bare inequality has company.** The same unparameterised attacker-vs-defender cost shape appears
  as the extraction cost inequality in [Beyond Labeling Oracles](beyond-labeling-oracles.md) and as
  `T_unlearn = o(T_retrain)` in [Yu et al.](impossibility-retrain-equivalence.md).
- Entity: [Nicolas Papernot](../entities/nicolas-papernot.md), [Hengrui Jia](../entities/hengrui-jia.md),
  [Anvith Thudi](../entities/anvith-thudi.md).

## Open Questions / Limitations

- Conjecture 1 is the open problem. `F+23` recasts it as the **cheapness assumption** and shows that
  settling it requires knowing whether access to one local minimum of a non-convex objective pins down
  a trajectory — an open problem in learning theory.
- Both theorems assume hardware/library noise; the paper concedes counter-based PRNGs may remove it.
- Verification requires sharing the training data with the verifier. The paper suggests MPC-based
  private inference; `F+23` replaces this with cryptographic commitments.
- Storage: full `float16` checkpoint sequences. Merkle-tree hashing is rejected because verifier
  reproduction error breaks exact hash equality; fuzzy extractors or LSH are left as future work.
- Success probability degrades multiplicatively along chains of PoLs.

## Quotes / Notable Passages

> "Dishonest spoofing is any strategy that requires lesser computational expenditure than that made by
> the prover in generating the proof"

> "In particular, the computational resources needed should (ideally) be the same or more as the cost of
> valid proof generation. We formalize the computational requirements below:"

> "From the argument we have made (G2), and given that we are not aware of a mechanism to prove this
> formally, we present the following as a conjecture:"
