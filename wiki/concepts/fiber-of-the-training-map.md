---
title: Fiber of the Training Map
type: concept
tags: [reconstruction, complexity theory, learning-theory, one-way-functions]
---

## Definition

For a training procedure `L` mapping a dataset (and randomness) to weights, the **fiber over `w`** is

```
L⁻¹(w) = { (D, r) : L(D; r) = w }
```

— the set of training sets that would have produced exactly this model. In the real-valued case,
equality is replaced by `‖L(D; r) − w‖ ≤ δ`.

Two questions attach to it, and they are not the same:

- **Size.** How large is the fiber, or how much does the induced distribution over `w` move when one
  record changes? This is the information-theoretic question, and it is what differential privacy,
  mutual-information memorization measures, and PAC Privacy all quantify.
- **Navigability.** Given `w` and side information `σ`, can an efficient algorithm *find* a point of the
  fiber consistent with `σ`? This is the computational question.

## Intuition

A haystack is only a hiding place if you cannot sort hay. A model may hide its training set in an
enormous fiber and still leak everything, if that fiber is easy to compute in.

Ordinary least squares is the worked counterexample. The weights depend on the data only through
`(XᵀX, Xᵀy)`, so the fiber has dimension roughly `nd` under `d` constraints — enormous. But fixing any
full-rank `X` and solving `Xᵀy = (XᵀX)w` for `y` produces a member in one linear solve, and intersecting
the fiber with "the attacker knows all but one entry" gives a unique solution — the missing entry,
recovered exactly. **Huge fiber, zero protection, because it was flat.**

## Properties / Theorems

- **`FIBER-SEARCH ∈ FNP`.** Verification is retraining, which is polynomial-time for a fixed step
  budget; the witness `(D, r)` is polynomial-size. This is the one place learning has a native
  find-hard/check-easy asymmetry without an imported trapdoor.
- **Asking whether `L` is hard to invert is asking whether training is a one-way function.**
  [Cohen et al. ITCS'25](../sources/cohen-data-reconstruction.md) Def C.1 already proves the equivalence
  between one-wayness and a computational reconstruction-resilience notion.
- The defender's multiplicity of acceptable solutions and the attacker's multiplicity of candidate
  preimages are the same quantity. There is no resource asymmetry between the parties — only a direction
  of travel.

## Where It Appears

- [Dinur–Nissim PODS'03](../sources/dinur-nissim-revealing-information.md) — **the size/navigability
  separation, with the poly-versus-exponential adversary split as the main theorem.** Any claim to have
  introduced this distinction is wrong.
- [Cohen et al. ITCS'25](../sources/cohen-data-reconstruction.md) — the computational security notion,
  equivalent to one-wayness.
- [Kaplan et al. ITCS'26](../sources/kaplan-bayesian-memorization-reconstruction.md) — the same split as
  computational versus statistical memorization.
- [Suliman et al. USENIX Sec'25](../sources/suliman-data-forging-attacks.md) — **the open conjecture**:
  navigating the fiber *under domain constraints* may be infeasible. Unproved.
- [Proof-of-Learning](../sources/proof-of-learning.md) — the same quantity priced in compute; a spoof is
  a fiber navigation cheaper than honest training.
- [fibers-of-the-training-map](../../output/fibers-of-the-training-map.md) — the programme's exposition.

## Related Concepts

- **Not** the fiber of the *evaluation* map `w ↦ M_w`, which concerns redundant parameterization rather
  than data loss. That object is studied by Grigsby et al. (arXiv:2209.04036, *"fibers of the realization
  map"*) and its decision problem is NP-hard —
  [Jagielski et al.](../sources/jagielski-model-extraction.md). Keeping the two apart is much of this
  page's purpose.
- [one-way-functions](one-way-functions.md), [pac-learning](pac-learning.md).

## Open Questions

- **Prove or refute Suliman's conjecture** for the training map. Jagielski proved the evaluation-map
  analogue; nobody has done this one.
- Apply computational/statistical DP to reconstruction from weights — verified unoccupied across the
  whole CDP line (Beimel–Nissim–Omri → Ghazi et al. FOCS'23).
- **Obstacle:** Xiao–Suh–Devadas CCS'24 — no non-trivial property-preserving transformation that keeps
  samples learnable gets worst-case cryptographic computational security. Training does not become
  one-way for free.
