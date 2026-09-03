---
title: Verification of Machine Unlearning is Fragile
type: source
date_ingested: 2026-08-20
authors: [Binchi Zhang, Zihan Chen, Cong Shen, Jundong Li]
venue: ICML 2024 (PMLR 235, Vienna; stated in the PDF footer). Ingested copy is arXiv:2408.00929v2
year: 2024
tags: [adversarial-ml, verifiable-computation, poisoning-attacks, reconstruction]
claim_quantifier: existential
antecedent: "Both attacks require the adversary to be the model provider itself, with full control of mini-batch sampling under mini-batch SGD; under full-batch gradient descent the paper states the gradient difference 'is deterministic and cannot be manipulated'. Proposition 4.3 additionally assumes bounded gradient (G), bounded mixed second derivative (L_x), and L-smoothness, with γ ≤ 1/L. Proposition 4.4 holds only for step sizes inside explicit ranges and for ε > 0."
cls_target: training run
cls_family: evade audit
cls_phase: train time
cls_access: white box
cls_write: model
cls_frame: compute
cls_party: attacker
cls_unit: time
cls_tightness: relative
cls_baseline: n/a
cls_second_party: time
cls_second_notion:
cls_assessed: implicit
cls_evidence: "Assume the time complexity of naive retraining is T (n). The time complexity of Algorithm 1 is T (n)"
cls_evidence_src: Prop 4.5
cls_reason: "Abstract's headline claim (Prop 4.2, valid PoRT at epsilon=0) is a bare existence result with no resource bound; Prop 4.5's cost relation to naive retraining T(n) is the only quantified bound on the attacker, and Claim Boundary calls the results 'upper bounds on what an attacker must spend.' assessed=implicit because Prop 4.5's cost is not part of Def 4.1's validity criterion (that is epsilon-based), only a reported comparison. The verification tolerance epsilon (Def 4.1, Prop 4.2/4.4) also bounds the attacker under a second, incomparable notion (a reproduction-error threshold) but has no matching unit in the vocabulary; left blank as a vocabulary gap rather than forced into perturbation or privacy budget. RECODE 2026-09-03 (R1, revision 7): tightness exponent -> relative. RECODE 2026-09-03 (R1, honest party unit): second_party none -> time."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

A constructive attack paper, not an impossibility paper. It asks whether a dishonest model provider
can pass existing unlearning verification while keeping the information it was asked to remove, and
answers yes for both families of verification in current use.

Verification is partitioned into two types. **Backdoor verification**: the data owner injects
poisoned data as a trigger and later asks for it to be unlearned; if unlearning happened, the trigger
should stop firing. **Reproducing verification**: the provider must supply a Proof of Retraining
(PoRT) `P_r = {w_r^{(t)}, d_r^{(t)}, g_r^{(t)}}_{t∈I}` that a verifier can replay step by step.

The attack exploits the *randomness of mini-batch sampling*. Under mini-batch SGD, the provider can
choose which retained points go into each retraining batch, and can choose them to produce gradients
resembling those the unlearned points would have produced. Algorithm 1 (retraining-based) does this
by nearest-neighbour selection within class and yields a valid PoRT at **`ε = 0`** (Proposition 4.2)
— i.e. it defeats even the strictest reproducing verification — while Proposition 4.3 bounds the
gradient norm reached, showing utility is preserved. Algorithm 2 (forging-based) is cheaper: it
reuses the original Proof of Training and updates both parameters and batch data by a single SGD step
on retained data, valid only under an `ε > 0` threshold (Proposition 4.4), with the time-complexity
comparison in Proposition 4.5.

The paper positions itself explicitly against [Thudi et al.](auditable-unlearning-definitions.md):
that forging map "is not realistic because it preserves the model parameters unchanged
`w_r^{(t)} = w^{(t)}`, which can be easily recognized by the verifier" — under repeated verification
requests, a verifier would keep receiving proofs with identical parameters. Algorithm 2 is designed
to move the parameters and stay valid.

The conclusion is a call for better verification, not a claim that verification is impossible:
"there is no strict guarantee for the verification of MUL. Better verification methods are needed to
obtain precise and reliable verification results."

## Claim Boundary

- **Quantified over:** the two verification families the authors identify — backdoor verification and
  reproducing verification — as instantiated in the cited literature, against a dishonest model
  provider under **mini-batch** SGD. Algorithm 1 covers both families; Algorithm 2 covers a subset of
  reproducing verification (`ε > 0` thresholds only). The empirical evidence is on real-world image
  datasets.
- **Antecedent:** the adversary *is* the model provider and controls batch composition. The paper
  states the boundary itself: under full-batch gradient descent the gradients are computed over all
  of `D` and `D \ D_u` and their difference "is deterministic and cannot be manipulated". So the
  attack is a mini-batch-randomness attack. Proposition 4.3's utility bound needs
  `‖∇_w l‖ ≤ G`, `‖∂²l/∂w∂x‖ ≤ L_x`, `‖∇²_w l‖ ≤ L` and `γ ≤ 1/L`; Proposition 4.4 needs step sizes
  inside stated intervals. The framing also assumes the verifier can confirm the deployed model
  matches the final weights in the proofs, "otherwise reproducing verification will never be possible
  and the problem becomes trivial".
- **Does not establish:** (a) that unlearning verification is impossible, ill-posed, or undefinable —
  **this is not an ill-posedness result and must not be read as one**; the paper's own closing move is
  to ask for stronger verification; (b) that unlearning itself is ill-defined — that is
  [Thudi et al.](auditable-unlearning-definitions.md)'s claim, not this one; (c) that trusted-hardware
  or cryptographic verification is broken — SGX-based PoUL is cited as related work and not attacked;
  (d) a lower bound of any kind. There is no hardness statement; the results are upper bounds on what
  an attacker must spend.
- **Abstract vs theorem:** the abstract's "the verification of machine unlearning is fragile" is a
  headline for two constructed attacks and reads stronger than it is. The precise version is in §6:
  "there is no strict guarantee for the verification of MUL." Note also that the paper's four numbered
  results appear as **Propositions** in the body while the surrounding prose calls them "Theorem 4.2"
  through "Theorem 4.5"; the numbering is inconsistent in the PDF and the propositions are the
  statements of record.

## Key Contributions

- A two-way taxonomy of unlearning verification: backdoor verification and reproducing verification.
- Algorithm 1: a retraining-based adversarial unlearning process producing a PoRT valid at `ε = 0`,
  circumventing both families while retaining unlearned-data information.
- Algorithm 2: a cheaper forging-based process that updates parameters as well as batches, valid under
  `ε > 0` — designed to fix the detectability flaw in the earlier forging construction.
- Utility and complexity guarantees for both (Propositions 4.3, 4.4, 4.5).
- Empirical demonstration on real-world datasets.

## Key Definitions / Theorems

- **Definition 4.1 (valid Proof of Retraining)**: `P_r = {w_r^{(t)}, d_r^{(t)}, g_r^{(t)}}_{t∈I}`
  satisfying reproducibility, `‖w_r^{(t)} − g_r^{(t)}(w_r^{(t−1)}, d_r^{(t)})‖ ≤ ε` for all `t`, plus
  a removability property (`d_r^{(t)} ⊆ D \ D_u`). A Proof of Training `P_t = {w^{(t)}, d^{(t)},
  g^{(t)}}` is defined analogously with the unlearned data present.
- **Proposition 4.2**: Algorithm 1 returns a valid PoRT under threshold `ε = 0`.
- **Proposition 4.3**: with `C_D := max_c max_{x∈c} min_{z∈c} ‖x − z‖`, `B = L_x C_D`, and
  `p_u = 1 − (1 − |D_u|/|D|)^m`,
  `E_T[‖∇L(w_r^{(T)}, D)‖²] ≤ (L(w_r^{(0)}, D) − L(w_r^{(T)}, D))/(γT) + (γL/2)(G² + p_u B²) + (1 − γL) p_u G B`.
- **Proposition 4.4**: for vanilla SGD with
  `0 ≤ γ^{(t)} ≤ (1/2L)(√(9 + 4εL/(L_x C_D)) − 3)` and
  `0 ≤ γ_r^{(t)} ≤ (ε − γ^{(t)} L_x C_D)/(G(2 + γ^{(t)} L))`, Algorithm 2 returns a valid PoRT under
  an `ε > 0` threshold.
- **Proposition 4.5**: if naive retraining costs `T(n)`, Algorithm 1 costs `T(n)` and Algorithm 2
  costs `(p_u/P + (1 − p_u)/(mP)) · T(n)` with `P` parallel processes and batch size `m`.
- **The forging map critique**: the earlier construction is rejected because it "preserves the model
  parameters unchanged `w_r^{(t)} = w^{(t)}`, which can be easily recognized by the verifier".

## Connections

- **Direct successor to [Thudi et al.](auditable-unlearning-definitions.md)**, and a corrective to it
  on one specific point: the forging map that keeps parameters fixed is detectable across repeated
  verification requests. Note the difference in kind — Thudi et al. argue the *definition* fails;
  Zhang et al. argue the *practice* of verification fails and can be repaired. When citing the two
  together, keep that seam visible.
- **[Suliman et al.](suliman-data-forging-attacks.md)** supplies the third position: forging is harder
  in practice than either implies once domain constraints are imposed. Zhang et al.'s Algorithm 1
  sidesteps the constraint problem entirely by drawing its substitute batches from **real retained
  data** (nearest neighbours in class), so every candidate is domain-valid by construction. That is a
  meaningful concession of attack power in exchange for feasibility, and it is the same trade Suliman
  et al. identify from the defender's side.
- **This is fibre navigation, priced.** Selecting retained batches whose gradients mimic the removed
  points is a walk in the
  [fiber of the training map](../concepts/fiber-of-the-training-map.md), and Proposition 4.5 is one of
  the few places in this literature where the *cost* of the walk is written down —
  `(p_u/P + (1 − p_u)/(mP)) · T(n)` relative to retraining. Compare
  [Proof-of-Learning](proof-of-learning.md), whose Property 2 states the attacker-cost inequality
  `E[C_A] ≥ E[C_T]` without parameterizing it: here there is an actual ratio, though it is a
  wall-clock complexity comparison rather than a security parameter.
- Backdoor verification is a *deliberately planted* signal used for detection — the constructive
  inverse of the planted-structure detection problems elsewhere in this wiki. See
  [poisoning-attacks](../concepts/poisoning-attacks.md).
- Concepts: [Machine Unlearning](../concepts/machine-unlearning.md),
  [Retrain Equivalence](../concepts/retrain-equivalence.md),
  [verifiable-computation](../concepts/verifiable-computation.md).

## Open Questions / Limitations

- The attack is restricted to mini-batch SGD and the manipulability of batch sampling; full-batch
  training is stated to be immune to this particular manipulation.
- Algorithm 1 costs as much as naive retraining, so the provider's saving is only in model utility,
  not compute; Algorithm 2 is cheaper but weaker (`ε > 0` only).
- No lower bound: nothing here says a stronger verification scheme cannot exist, and the paper asks
  for one.
- Nearest-neighbour batch selection depends on the intra-class diameter `C_D`; the appendix notes its
  benefit "can be diminished" as `C_D` grows, so the attack should degrade on datasets with high
  within-class spread.

## Quotes / Notable Passages

> "our understanding of the safety issues of machine unlearning verification remains nascent."

> "Can model providers successfully circumvent current verification strategies with dishonest
> unlearning?"

> "the forging map is not realistic because it preserves the model parameters unchanged
> `w_r^{(t)} = w^{(t)}`, which can be easily recognized by the verifier"

> "In contrast, under mini-batch gradient descent, the gradients in the original training and the
> retraining are computed over random samples in D and D\Du. With the randomness, it is possible to
> deliberately select the samples that induce a similar model update as the mini-batches in D"

> "This threat poses a novel challenge for the safe verification of machine unlearning: there is no
> strict guarantee for the verification of MUL. Better verification methods are needed to obtain
> precise and reliable verification results."
