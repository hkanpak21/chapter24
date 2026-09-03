---
title: Obfuscated Gradients Give a False Sense of Security — Circumventing Defenses to Adversarial Examples
type: source
date_ingested: 2026-08-20
authors: [Anish Athalye, Nicholas Carlini, David Wagner]
venue: "ICML 2018"
venue_evidence: "dblp: Obfuscated Gradients Give a False Sense of Security..., ICML 2018, pp. 274-283 (PMLR 80)"
year: 2018
tags: [adversarial-ml, evasion-attacks, robustness, evaluation-methodology, threat-model]
claim_quantifier: existential
antecedent: none
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: white box
cls_write: read only
cls_frame: capability
cls_party: attacker
cls_unit: perturbation
cls_tightness: budget
cls_baseline: absent
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "We evaluate each defense under the threat model under which it claims to be secure (e.g., bounded `∞ distortion of ε = 0.031)."
cls_evidence_src: "Section 2.4, Threat Models, raw/ACW18_ObfuscatedGradients.pdf. pdftotext renders epsilon as an unprintable control byte, a font-encoding artifact; corrected to ε here."
cls_reason: "Hand-classified 2026-08-22 against codebook revision 2, then migrated through revisions 3 to 5. Carries no verbatim evidence quote, unlike the delegated rows."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The paper names a failure mode — *obfuscated gradients*, defined as the special case of gradient masking in which the defence's own design necessarily destroys useful gradient information — and gives three attack techniques that recover an attack in its presence. It then runs those techniques over a complete, named population: the nine non-certified defences accepted at ICLR 2018 that claim white-box robustness. Seven of the nine rely on obfuscated gradients; six are circumvented completely and one partially, each under the threat model its own paper stated.

The three kinds of obfuscation and the matching techniques are: *shattered gradients* (non-differentiable or numerically unstable components), attacked with **Backward Pass Differentiable Approximation** (BPDA) — run the true function forward, substitute a differentiable approximation `g(x) ≈ f^i(x)` on the backward pass; *stochastic gradients*, attacked with **Expectation over Transformation** (EOT), differentiating `E_{t~T} f(t(x))`; and *vanishing or exploding gradients* from unrolled iterative computation, attacked by **reparameterization**, a change of variable `x = h(z)` with `g(h(z)) = h(z)` and `h` differentiable.

§3.1 gives five behavioural indicators that a defence is masking gradients rather than removing adversarial examples: one-step attacks beating iterative ones, black-box beating white-box, unbounded attacks not reaching 100% success, brute-force random sampling finding examples where gradient descent does not, and increasing the distortion bound not increasing success. These five indicators are the ancestor of the sanity-test section of [On Evaluating Adversarial Robustness](on-evaluating-adversarial-robustness.md) and of the AutoAttack unreliability flag in [RobustBench](robustbench.md).

For the survey strand, the load-bearing passage is §6.1. Before [CAP+19](on-evaluating-adversarial-robustness.md) said it, this paper stated the field's position on attacker compute, and stated it as a claim about what *counts* as robustness rather than about what attackers can afford: "It is not meaningful to restrict the computational power of an adversary artificially (e.g., to fewer than several thousand attack iterations). If two defenses are equally robust but generating adversarial examples on one takes one second and another takes ten seconds, the robustness has not increased." A ten-fold difference in attack cost is here declared to be *not a difference in robustness at all*. This is the sharpest available statement of the position that the survey strand documents.

## Claim Boundary

- **Quantified over:** a finite, enumerated population — the nine non-certified ICLR 2018 defences claiming white-box robustness. Within it: seven exhibit obfuscated gradients, six are broken completely, one partially. Two are excluded for having provable security claims (Raghunathan et al.; Sinha et al.) and one for claiming only black-box security (Tramèr et al.). The existential form of the result is: *there exist* attacks — BPDA, EOT, reparameterization — that defeat these named defences, one attack instance per defence.
- **Antecedent:** none — nothing is conditional. But each break is *conditional on the defence's own stated threat model*, which the authors respect deliberately ("We evaluate each defense under the threat model under which it claims to be secure"). The white-box assumption is stated with one exception carried throughout: the adversary knows the defence and its weights "but not test-time randomness (only the distribution)".
- **Does not establish:** (a) that obfuscated gradients *always* indicate a broken defence — the five indicators in §3.1 are explicitly hedged, "These behaviors may not perfectly characterize all cases of masked gradients"; (b) that every gradient-masking defence can be circumvented — no such theorem is proved or attempted; (c) that BPDA, EOT and reparameterization suffice against future defences — [TCBM20](adaptive-attacks-defenses.md) later shows they do not; (d) that the seven defences provide zero robustness in every configuration — the table footnotes that several are reported "alone" with adversarial training stripped out, and that the ∗∗ entry (Defense-GAN) has 0% accuracy only for its "fundamental principle", with imperfections making the theoretically optimal attack fail in practice at 55%.
- **Abstract vs theorem:** the title generalises beyond the result. "Obfuscated Gradients Give a False Sense of Security" reads as a universal about the phenomenon; the evidence is a census of nine papers from one conference in one year. The abstract itself is exact ("In a case study, examining non-certified white-box-secure defenses at ICLR 2018, we find obfuscated gradients are a common occurrence, with 7 of 9 defenses relying on obfuscated gradients"). The paper is honest about the asymmetry it exploits: "to show a defense can be bypassed, it is only necessary to demonstrate one way to do so; in contrast, a defender must show no attack can succeed."

## Key Contributions

- The definition and three-way taxonomy of obfuscated gradients: shattered, stochastic, vanishing/exploding.
- **BPDA** (§4.1): approximate `∇_x f(x)` by a forward pass through the true `f^i` and a backward pass through a differentiable `g ≈ f^i`. The special case `g = identity` recovers the straight-through estimator. The paper reports that replacing `f^i` on *both* passes is "either completely ineffective ... or many times less effective" — the substitution must be backward-only.
- Application of **EOT** to randomized defences, and **reparameterization** to unrolled optimization loops.
- Five behavioural indicators of gradient masking (§3.1).
- The case-study result table: seven of nine ICLR 2018 defences broken, with Madry et al. (47% at `ε=0.031` on CIFAR) and Na et al. (15%) the two that survive.
- §6.1's rejection of computational restrictions on the adversary as a threat-model component.
- The per-example reporting rule `mean_x min_{a∈A} f(a(x))` rather than `min_{a∈A} mean_x f(a(x))` (§6.3).

## Key Definitions / Theorems

No theorems. Definitions introduced:

- **Obfuscated gradients**: the case "where defenses are designed in such a way that the constructed defense necessarily causes gradient masking" — distinguished from prior gradient masking that arises from *learning* to break gradient descent.
- **Shattered gradients**: nonexistent or incorrect gradients from non-differentiability or numeric instability.
- **Stochastic gradients**: randomized network or input transform, so a single sample of the randomness misestimates the true gradient.
- **Exploding & vanishing gradients**: from defences that are many iterations of network evaluation, viewable as an extremely deep unrolled network.
- **BPDA**: `∇_x f(x)` approximated by forward through `f^i`, backward through `g` with `g(x) ≈ f^i(x)`.
- **EOT**: optimize `E_{t~T} f(t(x))` using `∇ E_{t~T} f(t(x)) = E_{t~T} ∇ f(t(x))`.
- **Reparameterization**: choose `h` differentiable with `g(h(z)) = h(z)` for all `z`, then attack `f(h(z))`.
- **Adaptive attack** (§6.3): "one that is constructed after a defense has been completely specified, where the adversary takes advantage of knowledge of the defense and is only restricted by the threat model."

## Connections

- Direct predecessor of [On Evaluating Adversarial Robustness (CAP+19)](on-evaluating-adversarial-robustness.md) — shares two authors, and CAP+19 §4.8 restates §6.1's compute position.
- Direct predecessor of [On Adaptive Attacks to Adversarial Example Defenses (TCBM20)](adaptive-attacks-defenses.md), which reports that the adaptive-attack rate rose from near zero in 2017 to one third in 2018 (this paper's census) to nearly all by 2020, and yet defences still fail.
- The three restrictions imposed by [RobustBench (CAS+21)](robustbench.md) — non-zero input gradients, deterministic forward pass, no inference-time optimization loop — are exactly this paper's three obfuscation types, turned into admission criteria.
- BPDA's limits under many-iteration defences are the starting point of [Evaluating the Adversarial Robustness of Adaptive Test-time Defenses (CGB+22)](adaptive-test-time-defenses-eval.md).
- Concepts: [Obfuscated Gradients](../concepts/obfuscated-gradients.md), [Adaptive Attacks](../concepts/adaptive-attacks.md), [Evasion Attacks](../concepts/evasion-attacks.md).
- Authors: [Nicholas Carlini](../entities/nicholas-carlini.md).

## Open Questions / Limitations

- No characterisation of when obfuscation is defeatable. The paper supplies three techniques and a census; it does not say what property of a defence makes BPDA succeed.
- The five indicators are heuristic and self-declared incomplete.
- The threat model excludes the adversary's knowledge of test-time randomness *values*, which is a genuine restriction on the "full knowledge" claim, and one that later randomized-smoothing work exploits legitimately.
- §6.1's compute claim is asserted, not argued. Its supporting example is a one-second-versus-ten-second gap; the paper does not consider whether some larger gap would count, and gives no threshold at which cost would become robustness.

## Quotes / Notable Passages

The rejection of adversary compute as a threat-model parameter — earlier and blunter than CAP+19's:

> "It is not meaningful to restrict the computational power of an adversary artificially (e.g., to fewer than several thousand attack iterations). If two defenses are equally robust but generating adversarial examples on one takes one second and another takes ten seconds, the robustness has not increased."

On the asymmetry between attack and defence claims:

> "to show a defense can be bypassed, it is only necessary to demonstrate one way to do so; in contrast, a defender must show no attack can succeed."

On the scope of the five indicators:

> "These behaviors may not perfectly characterize all cases of masked gradients."

On what a threat model may not contain:

> "threat models should not contain unrealistic constraints. We believe any compelling threat model should at the very least grant knowledge of the model architecture, training algorithm, and allow query access."
