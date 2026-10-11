---
title: Capacity-Bounded Privacy
type: concept
tags: [differential-privacy, adversarial-ml, learning-theory, low-degree-polynomial-framework, computational-vs-it-robustness]
---

## Definition

A privacy guarantee in which the adversary is restricted by the **function class its attack is drawn from**,
rather than by its running time.

Given an `f`-divergence with dual variational form
`D_f(P, Q) = sup_{h ∈ F} E_{x∼P}[h(x)] − E_{x∼Q}[f*(h(x))]`, replace the unrestricted supremum by one over a
class `H ⊆ F` to get the `H`-restricted divergence `D_f^H`. Rényi divergences are handled through the
corresponding `α`-divergence by a closed-form identity.

**Definition 3 of [Chaudhuri–Imola–Machanavajjhala](../sources/capacity-bounded-dp.md), verbatim:**

> "Let H be a class of functions with domain X , and Γ be a divergence. A mechanism A is said to offer
> (H, Γ)-capacity bounded privacy with parameter ǫ if for any two D and D′ that differ by a single person's
> value, the H-restricted Γ-divergence between A(D) and A(D′) is at most ǫ:
> ΓH (A(D), A(D′)) ≤ ǫ"

With `H` all functions and `Γ` Rényi, this is Rényi differential privacy, so capacity-bounded privacy is a
generalization of RDP and a relaxation of `ε`-DP.

## Intuition

Two motivating stories, both from the founding paper. The attacker is **machine-learnt** and therefore lives
in a known hypothesis space — linear functions, kernel classifiers, ReLU networks of a fixed architecture.
Or the recipient is under a **data-usage contract** restricting which functions they may compute on the
release, in which case a capacity-bounded guarantee says no contract-obeying recipient can breach privacy.

The axis is genuinely different from runtime. A class can be small and yet contain functions that are
expensive to evaluate, or large and cheap. It is also the axis on which the low-degree and SQ literatures
already have a graded scale — degree, query count, tolerance — where the runtime axis has only PPT and
unbounded.

## Properties / Theorems

**Post-processing is conditional, and this is structural, not an artefact.** Free post-processing plus a
restricted adversary would collapse the definition: "We cannot expect post-processing invariance to hold with
respect to all functions for capacity bounded privacy — otherwise, the definition would be equivalent to
privacy for all adversaries!" Theorem 1 of [CIM19](../sources/capacity-bounded-dp.md) gives post-processing
only under a **closure condition**: if `i ∘ g ∈ H` for every `g ∈ G`, `i ∈ I`, then `(H, Γ)`-privacy of `A`
yields `(I, Γ)`-privacy of `g ∘ A`. Self-invariance is the case `I = H`.

The same tax is paid, independently, by the kernel version:
[DM22](../sources/kernel-quantum-renyi-audit.md) Theorems 1 and 2 give post-processing only under a kernel
factorization `k(x, x') = k'(g(x), g(x')) k̃(x, x')`, or its expectation form for randomized `g`. **Any
restricted-divergence privacy notion pays a post-processing tax.** Treat a claim of free post-processing
under a restricted adversary as a red flag.

**Other properties, each conditional.**

- Convexity holds for `f`-divergences (CIM19 Theorem 2); as in the unrestricted case, it fails for Rényi.
- Parallel composition holds for `H₁, H₂` convex and translation invariant, with `H = {h₁ + h₂}` (Theorem 3).
- Sequential composition holds under the same conditions plus a constant function, and parameters add
  (Theorem 4) — but **non-adaptively only**. Adaptive composition is open.
- Generalization: if `H ⊇ {h_x : h_x(q) = q(x)}` for the statistical query class `Q`, then `(H, KL)`-privacy
  with parameter `ε` gives an expected generalization gap `≤ √(8ε)` (Theorem 6), via a new Pinsker-like
  inequality for restricted KL divergences (Theorem 7).

**What is actually computed.** Worked results are for the **linear** class, plus numerics for low-degree
polynomials. `(lin, KL)` gives a slightly better parameter than KL-DP for Laplace and **the same** parameter
for Gaussian — because for two equal-variance Gaussians the variational maximizer is already linear. For
Rényi, the `(lin, Renyi)` upper bound grows as `1 + (2ε)^{α−1}` against `(e^ε)^{α−1}` unrestricted, so a
moderate `α` makes the restricted bound smaller for any `ε`. The `(poly, Renyi)` parameters for degrees
1, 2, 3 converge to the unrestricted Rényi parameter as degree rises — the one place in the privacy
literature where an adversary's strength is a **graded** quantity.

## Where It Appears

- [CIM19 — Capacity Bounded Differential Privacy](../sources/capacity-bounded-dp.md) — the founding source
- [DM22 — Auditing DP with the Kernel Quantum Rényi Divergence](../sources/kernel-quantum-renyi-audit.md) —
  the same restriction, motivated as auditing; closes by naming the link back to capacity-bounded adversaries
  as unfinished work
- [DP20 — SoK: Differential Privacies](../sources/sok-differential-privacies.md) — **has no dimension for
  this**; its seven axes cover knowledge and runtime but not function class

## Related Concepts

- [Computational differential privacy](computational-differential-privacy.md) — the runtime axis; declared
  orthogonal to this one, and never formally compared to it
- [Low-degree polynomial framework](low-degree-polynomial-framework.md) — the `(poly, Renyi)` family is a
  degree-graded adversary class; the low-degree literature grades **algorithms** the same way. But note the
  standing caveat that low-degree-bounded and quasi-polynomial-time are provably different things.
- [Statistical query model](statistical-query-model.md) — the other restricted-access class with a graded
  cost; in [KLNRS08](../sources/what-can-we-learn-privately.md) the restriction sits on the **learner**
- [Computational vs statistical memorization](computational-vs-statistical-memorization.md)
- [Adversary knowledge taxonomy](adversary-knowledge-taxonomy.md) — the *knowledge* axis, used by
  [CHSS24](../sources/attaxonomy.md) and [SAH+25](../sources/adversary-aware-dp-bounds.md)

## Open Questions

- **Adaptive composition.** Open, and the sharpest gap: without it the notion does not compose across a
  training run.
- **Mechanisms for rich classes.** Kernel, ReLU-network, and classifier adversaries are advertised in the
  motivation and not analyzed. Only linear (and numerically, low-degree polynomial) results exist.
- **High-probability and adaptive generalization bounds**, blocked on missing information-theoretic
  properties of restricted divergences.
- **Learning the class.** [DM22](../sources/kernel-quantum-renyi-audit.md) proposes taking a supremum over a
  family of kernels — making the restricted class adaptive rather than fixed — and names the connection to
  limited-capacity adversaries as future work. Nobody has built the bridge from auditing tool to adversary
  model.
- **Relation to computational DP.** Never established in either direction.
