---
title: "PoLO: Proof-of-Learning and Proof-of-Ownership at Once with Chained Watermarking"
type: source
date_ingested: 2026-08-20
authors: [Haiyu Deng, Yanna Jiang, Guangsheng Yu, Qin Wang, Xu Wang, Baihe Ma, Wei Ni, Ren Ping Liu]
venue: "arXiv:2505.12296"
venue_evidence: "dblp: no match found (dblp.org unreachable this session); arXiv abstract page (arxiv.org/abs/2505.12296) has no Journal-ref field despite v1->v2 revision through 2026; no conference acceptance found by web search — unconfirmed refereed venue"
year: 2026
tags: [adversarial-ml, certification, verifiable-computation, watermarking]
claim_quantifier: empirical
antecedent: "Two stated 'core assumptions', both economic rather than computational: (1) any attack whose total cost is no less than honest training is 'economically unviable and therefore irrational'; (2) inside an enforceable model marketplace, a model without a unique verifiable watermark cannot be monetised, so a rational attacker must both erase the incumbent watermark and embed a replacement. The unforgeability game additionally assumes the hash H is collision- and preimage-resistant — but no theorem is proved from that assumption."
cls_target: training run
cls_family: forge
cls_phase: train time
cls_access: white box
cls_write: model
cls_frame: compute
cls_party: attacker
cls_unit: time
cls_tightness: measured
cls_baseline: absent
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "Forging PoLO demands 1.1–4× more resources than honest proof generation"
cls_evidence_src: abstract
cls_reason: "Classified on the OFA family per Rule 1: the Claim Boundary states the abstract's 1.1x-4x headline 'describes the OFA family only,' since WMA, the paper's other named attack, is three orders of magnitude cheaper and excluded from that ratio by failing on accuracy rather than cost. phase=train time because OFA fine-tunes all weights with training data (further training to erase and re-embed); WMA's direct weight overwrite would be post hoc but is not the classified row. write=model, not corpus (contrast pol-more-broken and the auditable-unlearning-definitions/forgeability-and-unlearning cluster): PoLO's verifier extracts the watermark from W_x and checks only that, and the page states explicitly 'no training data disclosed,' so no claimed dataset or log is ever forged, only the model's weights. tightness=measured not exponent: the page's own 'unnamed quantity' analysis states the 1.1x-4x figure is 'a measured multiplicative interval, not a parameterised family,' indexed to nothing (not model size, not shard count S, not a security parameter), matching the assigning note's expectation for this cluster. assessed=explicit because the ratio instantiates the paper's own named unforgeability-game symbols (C_A, C_honest, win condition C_A < C_honest) and is the abstract's headline reported result, not an incidental side cost. baseline=stated: C_honest is the explicit named comparator."
cls_prov: S
cls_date: 2026-08-22
---

> **Provenance.** Verified against the primary PDF on 2026-08-20 (`raw/DJY+25_PoLO.pdf`, extracted with
> `pdftotext`).

## Summary

Replaces trajectory replay with a hash chain of watermarks. Training is partitioned into `S` **shards**;
for shard `s_x`, the watermark `Λ_x`, embedding key `k_x`, and selection matrix `Y_x` are derived by a
hash `H(·)` over the previous shard's weights `W_{x−1}`, auxiliary information, and a verifier-supplied
nonce `µ`. The watermark is embedded during training via a regularisation term; a shard is declared
complete when the detection rate `η` crosses `η_G^{emb} = 0.99`. The complete set of watermarks is the
proof of learning; the final watermark is the proof of ownership. Verification extracts `Λ̂_x` from `W_x`
and accepts if `η_x ≥ η_G^{ver} = 0.70` — no gradient replay, and no training data disclosed.

This page exists because of what the paper does with numbers. Three compute ratios are reported to two
significant figures — verification at `1.5%–10%`, forging at `1.1×–4×`, and (in the body) OFA at
"roughly a 5× increase" — and **not one of them is the conclusion of a theorem**. They are wall-clock
seconds measured on one machine (dual Xeon Gold 6126, 2× Tesla V100) across eight model/dataset pairs
and three watermark sizes, against two hand-built attacks. The paper does write an **unforgeability
game** (challenger/adversary, three win conditions, one of them `C_A < C_honest`) and does name an
assumption (collision- and preimage-resistant `H`) — and then discharges the game with a two-case prose
argument rather than a proof. There is no theorem environment anywhere in the paper.

The thesis in miniature: a compute ratio reported to two significant figures, never defined.

## Claim Boundary

- **Quantified over:** two named attack families on the authors' own instantiation. **OFA** (Overhaul
  Fine-tuning Attack) fine-tunes all weights, with training data, to erase and re-embed; **WMA**
  (Weight Manipulation Attack) directly overwrites selected weights without training data. Table 2
  claims most watermarking-literature attacks "instantiate either of the two representative attack
  families", and Table 9 is flagged in the PDF as "an analytical (non-experimental) applicability check"
  for replay-PoL attacks. Pure watermark-removal attacks are **excluded by fiat** as "economically
  irrational". The adversary is given all checkpoints `W_x` but not the legitimate keys `(k_x, Y_x)`.
  There is no adversary complexity class; "polynomial-time adversary" appears once, in the definition of
  economic unforgeability, and is never used in an argument.
- **Antecedent:** the two economic assumptions in the frontmatter, plus collision- and
  preimage-resistance of `H`. Both economic assumptions are *definitional exclusions* rather than
  hypotheses that do work in a proof: they delete attack classes from the threat model.
- **Does not establish:** (i) that forging is expensive — WMA, one of the paper's own two attacks, costs
  `11.32–344.94s` (`$0.01–$0.06`) against `25,051.72s` (`$4.43`) for honest generation on
  VGG16/TinyImageNet, i.e. **three orders of magnitude cheaper**; the defence against WMA is accuracy
  degradation, not cost. The `1.1×–4×` headline therefore describes the OFA family only. (ii) That the
  scheme is unforgeable in the game it defines — the win condition is stated, the assumption is stated,
  no proof follows. (iii) Anything about attacks outside the two families, or about non-marketplace
  settings; the paper scopes out "grey markets, internal theft, or pure availability attacks". (iv) A
  sweep over the verification threshold: `η_G^{ver} = 0.70` is chosen post hoc from the observed data
  ("above the worst-case attacked rate"), and "a full parametric sweep of `η_G^{ver}` is left to future
  work."
- **Abstract vs theorem:** **two discrepancies found.**
  1. *Denominator drift.* The abstract says verification is cut "to just 1.5–10% **of traditional
     methods**"; contribution bullet (ii) says it "reduces verification cost to 1.5%–10% **of
     training**"; the same paragraph's next bullet reverts to "compared to traditional PoL methods"; the
     conclusion says "of training". The same figure is attributed to two different denominators. It
     happens to be numerically robust — in the paper's Table, vanilla-PoL verification is itself
     approximately the cost of training (e.g. AlexNet/CIFAR-10, 512-bit: `P_verify` `83.37` for PoLO vs
     `891.99` for PoL (Vanilla) vs `970.45` baseline training) — but the paper never says so, and the
     equivalence of denominators is an artifact of the object being measured, not a stated result.
  2. *Ratio drift.* The abstract and conclusion say forging "demands 1.1x–4x more resources"; §5's
     narrative says OFA is "roughly a 5× increase" and the takeaway box says "OFA incurs up to 5× the
     cost of proof generation". Abstract `4×`, body `5×`.

## The unnamed quantity

The paper's compute quantities, exactly as written:

- Abstract: *"cutting verification costs to just 1.5–10% of traditional methods. Forging PoLO demands
  1.1–4× more resources than honest proof generation"*.
- Contribution (ii): *"shard-level watermark checking reduces verification cost to 1.5%–10% of training"*.
- Unforgeability game, win condition (ii): *"`C_A < C_honest`, the cost of honestly training shard `s_x`"*.
- Design rationale: forging a watermark mid-chain *"incurs a computational cost equivalent to honestly
  training a new model"*; *"the cost of forgery scales with depth and exceeds rational benefits"*.

What it lacks:

- **A definition.** `C_A` and `C_honest` appear only inside the win condition. No cost function is
  defined; the measurements are wall-clock seconds (and US dollars) on one hardware configuration, so the
  quantity is not even hardware-independent, let alone architecture-independent.
- **An exponent.** `1.1×–4×` is a measured multiplicative interval, not a parameterised family. Nothing
  indexes it to model size, shard count `S`, dataset size, or a security parameter. Note the design
  argument claims forgery cost "scales with chain depth" — that is the one place a growth rate is
  asserted, and it is asserted, not measured: no experiment varies `S` and reports the resulting cost
  curve.
- **An adversary class.** OFA and WMA are two specific algorithms. "No polynomial-time adversary" is
  written once and never used.
- **An assumption doing work.** Collision- and preimage-resistance of `H` is named, then the game is
  discharged by the sentence "The chained structure ensures that producing a valid `W'_{x−1}` requires
  either (a) possessing the genuine checkpoint (no cost advantage) or (b) reconstructing the chain from
  scratch (cost `≥ C_honest`)". Option (a)/(b) is an exhaustiveness claim about adversary strategies,
  which is precisely what a proof would have to establish.
- **A lower bound.** None. The paper's own WMA is a counterexample to any naive reading of the headline
  ratio as a lower bound on forging cost.

The **verification** figure is worth separating from the forging figure. `1.5%–10%` is the ratio the
paper actually measured well: `P_verify` for PoLO against `P_verify` for PoL (Vanilla) and PoL (hash) in
the same table, across eight configurations. That is a genuine engineering measurement of the Property 1
quantity (`E[C_V] ≤ E[C_T]`) from [the original PoL paper](proof-of-learning.md) — reported as a
percentage, still with no definition of the cost function and no analytic bound.

## Key Contributions

- **PoX (Proof-of-Anything), Definition 1**: a prover sends a proof whose verification cost is
  "negligible compared to the computational overhead incurred during the generation of `P`", via an
  irreversible function `Θ`. This is a definitional home for the asymmetry, written qualitatively
  ("negligible") rather than quantitatively.
- **Definition 3 (PoL)** restated in this frame: trajectory `P := (W_t, B_t, A_t)_{t=0}^T` with
  verification condition `‖W_{t+1} − Θ(W_t, B_t)‖ ≤ ε`.
- **Definition 4 (PoO)** and **Definition 5 (PoLO)**: the ownership proof *is* the training proof.
- The chained-watermark construction: `(Λ_x, k_x, Y_x) = H(W_{x−1}, aux, µ)`; Gaussian noise added once
  `η` crosses threshold, for robustness against inference attacks.
- **Backward verification**: recursively validate `s_x, s_{x−1}, s_{x−2}, …` to accumulate confidence, so
  that partial manipulation of recent checkpoints is detectable.
- Shard-count-based reward: compensation proportional to verified shards `S` and test accuracy, which the
  paper argues blocks workload inflation because `(k_{x+1}, Y_{x+1})` are pinned to the previous
  checkpoint and the verifier nonce.
- **Unforgeability game** with challenger, adversary, and three win conditions including `C_A < C_honest`
  and a non-triviality clause `(W'_{x−1}, W'_x) ≠ (W_{x−1}, W_x)`.
- Empirical results across AlexNet, ResNet18/34, WideResNet, VGG16, TextCNN, MiniBERT on
  CIFAR-10/100, TinyImageNet, AG News; watermark sizes 512/1024/2048 bits.

## Key Definitions / Theorems

**No theorems.** Definitions 1–5 plus the unforgeability game. The strongest formal object is the game's
success predicate; it is never instantiated in a proof. Numerical anchors worth keeping:

- Honest `Training + P_gen` on VGG16/TinyImageNet, 2048-bit: `25,051.72s` (`$4.43`); proof generation
  alone `20.27s`; `P_verify` `342.17s` against `24,693.31s` for PoL (Vanilla).
- OFA on the same configuration: `113,771.31s` (`$20.22`) — the "roughly 5×" figure. Legitimate watermark
  survives with `η` between `64.53%` and `98.43%` (worst case across the table: `η = 64.27%`, MiniBert,
  512-bit).
- WMA: `11.32–344.94s` (`$0.01–$0.06`); legitimate detection stays `91.48%–99.81%`; forged proof rejected
  because main-task accuracy falls below threshold.
- Thresholds: `η_G^{emb} = 0.99` for shard completion, `η_G^{ver} = 0.70` for verification.
- Reference point for the ZK alternative: "PoL (zkp)" (Abbaszadeh, Pappas, Katz, Papadopoulos, CCS 2024,
  per this PDF's bibliography) "incurs around 15 mins of proof generation time per iteration on VGG-11
  with CIFAR-10 (excluding training time)".

## Connections

- Successor to [Proof-of-Learning: Definitions and Practice](proof-of-learning.md), whose Property 1
  quantity it measures and whose Property 2 quantity it re-reports as a measured interval.
- Cites [Fang et al.](pol-more-broken.md) (as [13]) and Zhang et al. S&P 2022 (as [11]) as the reasons
  gradient-replay PoL is abandoned.
- Cites [Thudi et al., USENIX Security 2022](auditable-unlearning-definitions.md) (as [12]) among the
  works showing trajectories can be fabricated.
- Its Table 1 row "PoL (hash)" is [PoL with Incentive Security](pol-incentive-security.md); its row
  "PoL (zkp)" is the ZK-proof-of-training line, cf.
  [zk-verifiable-ai-pipelines](zk-verifiable-ai-pipelines.md) and
  [ZK-ML verification](../concepts/zk-ml-verification.md).
- Concepts: [Proof-of-Learning (the notion)](../concepts/proof-of-learning.md),
  [Verifiable Computation](../concepts/verifiable-computation.md),
  [Fiber of the Training Map](../concepts/fiber-of-the-training-map.md).
- Contrast with [Suliman et al.](suliman-data-forging-attacks.md): the forging question there is asked as
  a hardness conjecture; here it is answered as a measurement.
- The governance analogue of the same measured-ratio move is
  [catch-a-chinchilla-compute-monitoring](catch-a-chinchilla-compute-monitoring.md), which at least
  writes the ratio as a definitional parameter (`F`-hard).

## Open Questions / Limitations

- No theorem for the unforgeability game the paper defines. Supplying one — even under an idealised hash
  — would be the obvious next step and is not attempted.
- WMA's cost is three orders of magnitude below honest generation. The claim that forging is expensive
  survives only because WMA fails on accuracy; nothing rules out a cheap attack that preserves accuracy.
- `η_G^{ver} = 0.70` is fitted to the observed attack results. No parametric sweep.
- "Forgery cost scales with chain depth" is asserted from the chain structure, never measured against `S`.
- The economic framing quietly assumes the attacker's benefit is monetisation inside a compliant
  marketplace. Outside that setting the excluded attack classes return.

## Quotes / Notable Passages

> "Any attack whose total computational cost is no less than that of the corresponding honest training is
> considered economically unviable and therefore irrational."

> "PoLO is economically unforgeable if no polynomial-time adversary can win the above game with
> non-negligible probability, assuming the cryptographic hash function H is collision-resistant and
> preimage-resistant."
