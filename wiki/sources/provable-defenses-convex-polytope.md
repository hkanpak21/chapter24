---
title: "Provable Defenses against Adversarial Examples via the Convex Outer Adversarial Polytope"
type: source
date_ingested: 2026-04-23
authors: [Eric Wong, J. Zico Kolter]
venue: "ICML 2018, stated in the PDF's own footer as Proceedings of the 35th International Conference on Machine Learning, PMLR 80 (arXiv:1711.00851v3, 8 Jun 2018)"
year: 2018
tags: [adversarial-ml, certified-robustness, convex-optimization, linear-programming, evasion-attacks, relu-networks]
claim_quantifier: universal
antecedent: "none. The bound is a convex relaxation and holds unconditionally for ReLU networks. The relaxation's looseness is the price, not an assumption."
adversary_bound: "none. The attacker is an ℓ∞ ball of radius ε on the input. No computational bound is placed on any party; the defender's cost is a few extra forward and backward passes, possibly with much larger batch sizes."
date_verified: 2026-08-20
---

## Summary

This paper (WK18) provides the first **certified-defense framework for deep ReLU networks** that scales beyond toy models and combines *both* robust training and certified verification in a single procedure. The central idea: for a ReLU network, the set of possible final-layer activations reachable via norm-bounded input perturbations is a non-convex set — the **adversarial polytope** — but it can be tightly *outer-approximated* by a convex set. The authors construct this outer bound via layer-wise linear relaxation of ReLUs, formulate the resulting "worst-case-loss" problem as a linear program (LP), and — crucially — show that the LP's **dual** can be represented as a computation resembling backpropagation, allowing efficient optimization without any actual LP solving.

The training procedure minimizes the LP-dual's worst-case loss, yielding networks whose predictions are certified robust to norm-bounded perturbations on the training data *and* detectably robust on test points. The method was the first certified-robustness result scalable to convolutional networks. On MNIST with ε = 0.1 ℓ∞ perturbations, WK18 achieves <5.8% test error with provable certificates — a result that was a foundational demonstration that certified robustness is practically achievable for non-trivial networks.

This framework established the relax-and-optimise paradigm for certified training.

## Claim Boundary

- **Quantified over:** the guarantee has two different shapes and the difference is easy to lose. On the **training data**, the classifier is provably robust against norm-bounded perturbations. On **previously unseen examples**, the guarantee is weaker and is a *detection* guarantee: the approach is guaranteed to detect all adversarial examples, but may also flag some non-adversarial ones. The paper states both in its first two sentences.
- **Antecedent:** none. The convex outer approximation is a relaxation, valid unconditionally for ReLU networks. What it costs is tightness: the certified error is an upper bound and may be far above the true robust error.
- **Which party is constrained:** **neither party is bounded in computation.** The attacker is an ℓ∞ ball of radius ε. The defender's cost is a few extra forward and backward passes through a modified network, and the paper notes in the same sentence that this may require much larger batch sizes.
- **Does not establish:** robustness for non-ReLU activations; a tight certificate; or scalability to ImageNet. The headline MNIST number is a bound of the same kind: less than 5.8% test error for any adversarial attack with ℓ∞ perturbation bounded by `ε = 0.1`.
- **Abstract vs theorem:** none found. The abstract states the training-data restriction and the false-flag caveat explicitly.

## Key Contributions

- **Convex outer approximation of the adversarial polytope**: tight LP relaxation of ReLU activations reachable via ε-ℓ∞ perturbations.
- **Dual-as-backprop technique**: LP dual for the worst-case loss can be evaluated by a single backward pass through a slightly modified network, avoiding actual LP solving.
- **Certified training procedure**: optimize the worst-case dual loss during training; yields networks both robust and certifiable.
- **First scalable certified defense for ReLU networks**: practical results on MNIST, Fashion-MNIST, SVHN, human activity recognition.
- **Test-time detection guarantee**: any test input either receives a certified-robust prediction or is flagged as potentially adversarial.
- **Foundation of the certified-training literature**: influential framework adopted and refined by many follow-ups.

## Key Definitions / Theorems

- **Adversarial polytope**: for input x and ε-ℓ∞ perturbation, the set {z_final : z = net(x + δ), ∥δ∥_∞ ≤ ε}. Non-convex due to ReLU's piecewise-linear discontinuity.
- **Linear ReLU relaxation**: replace z = max(0, ẑ) with three linear constraints: z ≥ 0, z ≥ ẑ, z ≤ û · (ẑ − l̂) / (û − l̂) where l̂ ≤ ẑ ≤ û are pre-activation bounds. Yields a convex outer-approximation of the adversarial polytope.
- **Worst-case loss LP**: maximize ℓ(z_final, y') over z in the convex outer polytope, for all y' ≠ y.
- **Main theorem (informal)**: the worst-case loss LP's dual admits a closed-form evaluation via a backward pass through a "dual network"; training with this loss yields certified robust classifiers.
- **Robust certification**: at test time, if the dual-loss bound exceeds 0 (i.e., the LP is infeasible for all incorrect labels), the prediction is certified robust.

## Connections

- Source: [Certified Robustness via Randomized Smoothing (Cohen et al. 2019)](certified-robustness-randomized-smoothing.md) — alternative certified-defense paradigm scaling better (to ImageNet) but ℓ₂-only; WK18 handles ℓ∞ but scales less well.
- Source: [Certified Robustness via Differential Privacy (Lecuyer et al. 2019)](certified-robustness-differential-privacy.md) — another alternative certified-defense paradigm.
- Source: [Provably Robust SmoothAdv (Salman et al. 2019)](provably-robust-smoothadv.md) — improves randomized smoothing via adversarial training; WK18's convex-polytope is the alternative route.
- Source: [Robustness May Be at Odds with Accuracy (Tsipras et al. 2019)](robustness-at-odds-accuracy.md) — WK18 empirically exhibits the accuracy-robustness tradeoff.
- Concept: [Evasion Attacks](../concepts/evasion-attacks.md) — the defended attack surface.
- Concept: [Certified Robustness](../concepts/) — the goal.
- Author: J. Zico Kolter (CMU); same author on Cohen et al. 2019 (randomized smoothing).

## Open Questions / Limitations

- **Scales poorly beyond moderate-sized networks**: LP relaxation becomes loose for deep architectures; not demonstrated on ImageNet scale.
- **Relaxation looseness**: the convex outer polytope is not tight; certified accuracy is substantially lower than empirical robustness.
- **ReLU-specific**: framework assumes ReLU activations; extensions to other activations (sigmoid, tanh, swish) require new relaxations.
- **Certified bounds degrade with depth**: each layer's relaxation compounds, making deep certification loose.
- **Comparison with randomized smoothing**: on ImageNet, randomized smoothing scales better; WK18 is more competitive on smaller networks / ℓ∞.

## Quotes / Notable Passages

Verified against `raw/WK18_ConvexOuterPolytope.pdf` on 2026-08-20 unless marked otherwise.

> "We propose a method to learn deep ReLU-based classifiers that are provably robust against norm-bounded adversarial perturbations on the training data. For previously unseen examples, the approach is guaranteed to detect all adversarial examples, though it may flag some non-adversarial examples as well."

> "The basic idea is to consider a convex outer approximation of the set of activations reachable through a norm-bounded perturbation, and we develop a robust optimization procedure that minimizes the worst case loss over this outer region (via a linear program)."

> _Not verbatim. Checked against `raw/WK18_ConvexOuterPolytope.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> By executing a few more forward and backward passes through a slightly modified version of the original network, we can learn a classifier that is provably robust to any norm-bounded adversarial attack.

The paraphrase silently drops a parenthetical that carries a cost. The paper's sentence:

> "The end result is that by executing a few more forward and backward passes through a slightly modified version of the original network (though possibly with much larger batch sizes), we can learn a classifier that is provably robust to any norm-bounded adversarial attack."

— abstract.

> "We illustrate the approach on a number of tasks to train classifiers with robust adversarial guarantees (e.g. for MNIST, we produce a convolutional classifier that provably has less than 5.8% test error for any adversarial attack with bounded ℓ∞ norm less than ε = 0.1)"

— abstract, the headline number with its radius attached.
