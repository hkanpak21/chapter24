---
title: Impossibility Frameworks (for AI Alignment)
type: concept
tags: [impossibility, formal-models, alignment, social-choice]
---

## Definition
A class of formal results showing that, under stated modeling assumptions, *no* algorithm of a given form can achieve a specified alignment / safety / learning objective. In the AI-alignment setting, impossibility frameworks typically:
1. Define a ground-truth object (e.g., a mixture of preference distributions p* = Σ η(u) p*_u).
2. Define a parametric solution class (e.g., single-reward RLHF with linear r_φ = ⟨φ, ψ⟩).
3. Prove a quantitative lower bound on the gap between any solution in the class and the group-optimal solution, as a function of a diversity / structural parameter.

## Intuition
The pattern mirrors classical impossibility results in social choice (Arrow, Gibbard–Satterthwaite): when the preference domain is rich enough, aggregation into a single scalar objective cannot satisfy all stakeholders simultaneously. Quantitative impossibility bounds give *rates* rather than binary yes/no answers.

## Properties / Theorems
- **MaxMin-RLHF impossibility (Theorem 1, Chakraborty et al. 2024)**: Align-Gap(π_RLHF) ≥ λ_ψ · ε(1−η(u)) / (64 β² L_π D²) for the minority subgroup u, where ε is the minimum diversity between its preference and other groups', η(u) its mixing weight, β the KL regularization, and λ_ψ the minimum eigenvalue of the reward feature Gram matrix.
- **Proof pattern**: Lipschitz parametric family (here Bradley–Terry) + total-variation lower bound via triangle inequality on most-distant group pair + KL-regularized strong convexity → reward-gap → policy-gap.
- Generic template: diversity ε > 0 AND convex aggregation ⇒ minority alignment gap bounded below by a function of ε and (1 − majority weight).

## Where It Appears
- [maxmin-rlhf-impossibility](../sources/maxmin-rlhf-impossibility.md) (primary).
- Contrast / escape route: Egalitarian (max-min) objective aggregation — the paper's "one possibility" result.

## Related Concepts
- [rlhf-formal-model](rlhf-formal-model.md).
- [undetectable-backdoors](undetectable-backdoors.md) — another form of impossibility (detection), different machinery (cryptographic).
- [win-win-theorem](win-win-theorem.md) — structurally similar: "good X for all inputs is impossible unless Y".

## Open Questions
- Can the bound be tightened to match an upper bound for MaxMin-RLHF itself?
- Impossibility results for nonlinear reward heads / transformer-parameterized rewards.
- Game-theoretic strategyproofness of MaxMin aggregation (do users have incentive to misreport preferences)?
