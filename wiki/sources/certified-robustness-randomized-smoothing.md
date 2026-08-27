---
title: "Certified Adversarial Robustness via Randomized Smoothing"
type: source
date_ingested: 2026-04-23
authors: [Jeremy Cohen, Elan Rosenfeld, J. Zico Kolter]
venue: "ICML 2019, stated in the PDF's own footer as Proceedings of the 36th International Conference on Machine Learning, PMLR 97 (arXiv:1902.02918v2, 15 Jun 2019)"
year: 2019
tags: [adversarial-ml, certified-robustness, randomized-smoothing, differential-privacy, robustness]
claim_quantifier: universal
antecedent: "none. The robustness guarantee is a geometric consequence of Gaussian smoothing via the Neyman-Pearson lemma. No hardness assumption is used."
adversary_bound: "none. The attacker is constrained only by an ℓ₂ ball of radius R. The defender's Monte Carlo sample budget enters as a confidence level on the certificate, not as a bound on the attacker."
date_verified: 2026-08-20
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: white box
cls_write: read only
cls_frame: capability
cls_party: attacker
cls_unit: perturbation
cls_tightness: budget
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "g(x + δ) = cA for all ‖δ‖2 < R"
cls_evidence_src: "Thm 1"
cls_reason: "Rule 5, exact match: the only restriction on the attacker is the ℓ2 perturbation radius R, so party=attacker, unit=perturbation, tightness=budget, frame=capability. access=white box: the certificate is stated to hold for the worst case over any perturbation within the ball regardless of the base classifier f or the attacker's knowledge of it ('Theorem 1 assumes nothing about f'), i.e. it covers a fully-informed adversary. second_party=none: the defender's Monte Carlo sample budget is a confidence device on the certificate, not a resource bound on a party, per the Claim Boundary. write=none: the attacker perturbs its own query input at test time, it does not write to a corpus, model, or response channel."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper (CRK19) establishes **randomized smoothing** as the first certified adversarial defense that scales to ImageNet. Given any base classifier f : ℝ^d → Y (including arbitrary deep networks), the smoothed classifier g(x) = argmax_c Pr_{δ∼N(0,σ²I)} [f(x+δ) = c] is provably robust to ℓ₂-bounded adversarial perturbations. The paper's main technical contribution is a **tight robustness radius**: if the top class has smoothed probability at least p_A and the runner-up has at most p_B, then g is provably constant on the ℓ₂ ball of radius R = (σ/2) · (Φ⁻¹(p_A) − Φ⁻¹(p_B)), via the **Neyman-Pearson lemma**. This tight bound improves on the looser randomized-smoothing bounds of Lecuyer et al. (PixelDP) and Li et al.

The certification procedure uses Monte Carlo sampling to estimate p_A, p_B with high-probability lower/upper confidence bounds, making g practically certifiable. On ImageNet, randomized smoothing achieves 49% certified top-1 accuracy under ℓ₂ perturbations of norm ≤ 0.5; no competing certified defense has demonstrated any non-trivial accuracy at ImageNet scale. On CIFAR-10 and smaller datasets where alternatives are viable, smoothing still wins on certified accuracy.

The paper lays the foundation for the [Salman et al. SmoothAdv](provably-robust-smoothadv.md) follow-up, which improves the base classifier by adversarial training against an attack adapted to the smoothed model.

## Claim Boundary

- **Quantified over:** every base classifier. The theorem is universal in `f`, which is the paper's central selling point: no assumption on architecture, activation, or training. What is *not* universal is the certificate, which is per-input and depends on the two class probabilities at that input.
- **Antecedent:** none. The radius follows from the Neyman-Pearson lemma applied to Gaussian smoothing. Nothing cryptographic or complexity-theoretic enters.
- **Which party is constrained:** **neither party is bounded in computation.** The attacker is constrained by an ℓ₂ ball of radius `R` and nothing else; the certificate is a geometric statement about that ball. The defender's Monte Carlo budget appears only as the confidence level attached to the estimated `p_A` — an abstention-and-confidence device, not a resource bound on the attacker. A page in this corpus that reads randomized smoothing as pricing an adversary is misreading it.
- **Does not establish:** robustness in ℓ∞; robustness of the base classifier `f`; or anything for perturbations outside the certified radius. The certificate also does not hold with probability 1 — `CERTIFY` returns a high-probability statement and abstains otherwise.
- **Abstract vs theorem:** none found. The abstract states the ImageNet number with its radius and hedges "e.g.".

## Key Contributions

- **Tight robustness radius via Neyman-Pearson**: R = (σ/2)(Φ⁻¹(p_A) − Φ⁻¹(p_B)) for Gaussian smoothing; provably tight.
- **ImageNet-scale certified defense**: 49% certified top-1 at ε=0.5 (ℓ₂), first certified defense with non-trivial accuracy at ImageNet.
- **Architecture-agnostic**: works for any base classifier; no assumption on ReLU structure or other architectural properties.
- **Monte Carlo certification procedure**: high-probability (p_A, p_B) estimates via PREDICT and CERTIFY algorithms.
- **Robustness-accuracy tradeoff via σ**: noise level σ is the single hyperparameter trading off certified radius vs. standard accuracy.

## Key Definitions / Theorems

- **Smoothed classifier**: g(x) = argmax_c Pr[f(x + δ) = c], δ ~ N(0, σ²I).
- **Main theorem (robust radius)**: If Pr[f(x+δ) = c_A] ≥ p_A ≥ p_B ≥ Pr[f(x+δ) = c_B] for every other class, then g(x+δ') = c_A for all ∥δ'∥₂ ≤ (σ/2)(Φ⁻¹(p_A) − Φ⁻¹(p_B)), where Φ is the standard Gaussian CDF.
- **Tightness**: Without additional assumptions on f, the bound is tight — there exist f saturating it.
- **CERTIFY algorithm**: given x, use Monte Carlo samples to compute a high-probability lower bound on p_A, yielding a high-probability certified radius.
- **PREDICT algorithm**: return g's prediction with controlled abstention rate when confidence is insufficient.

## Connections

- Source: [Certified Robustness via Differential Privacy (PixelDP)](certified-robustness-differential-privacy.md) — Lecuyer et al. predecessor using DP framework; gives looser bounds that this paper tightens via Neyman-Pearson.
- Source: [Provably Robust SmoothAdv](provably-robust-smoothadv.md) — Salman et al. NeurIPS 2019 follow-up combining adversarial training with smoothing.
- Source: [Convex Outer Adversarial Polytope (Wong-Kolter 2018)](provable-defenses-convex-polytope.md) — an alternative certified defense using LP relaxations; scales less well but works on ℓ∞.
- Concept: [Certified Robustness](../concepts/) / [Evasion Attacks](../concepts/evasion-attacks.md).
- Concept: [Concentration of Measure](../concepts/concentration-of-measure.md) — Gaussian smoothing connects to Gaussian isoperimetry and hence to concentration bounds.
- Source: [Universal Law of Robustness](universal-law-of-robustness.md) — Bubeck–Sellke relate the number of parameters to the Lipschitz constant an interpolating classifier must have. **Correction, 2026-08-20:** this line previously said they "establish that overparameterization is necessary for Lipschitzness". That sentence is marked as non-verbatim on the Bubeck–Sellke page itself; their own statement is hedged as "highly speculative in nature".
- Author: J. Zico Kolter (CMU, co-author on [Wong-Kolter 2018](provable-defenses-convex-polytope.md)).

## Open Questions / Limitations

- **Gaussian smoothing gives ℓ₂ robustness but nothing for ℓ∞** (at ImageNet scale, ℓ∞ adversarial training beats smoothing empirically); other smoothing distributions for ℓ∞ or ℓ₁ are less tight.
- **Accuracy cost**: certified accuracy of 49% vs. standard >75% on ImageNet; the gap reflects the σ noise level necessary for meaningful radius.
- **Monte Carlo inefficiency**: certification requires ~100K forward passes per input to achieve tight confidence bounds.
- **Adaptive attacks against the smoothing procedure itself**: the SmoothAdv follow-up partially addresses this but adaptive analysis remains active.
- **Certification of the base classifier's input preprocessing pipeline** (normalization, augmentation) is not straightforward.

## Quotes / Notable Passages

Verified against `raw/CRK19_RandomizedSmoothing.pdf` on 2026-08-20 unless marked otherwise.

> "We show how to turn any classifier that classifies well under Gaussian noise into a new classifier that is certifiably robust to adversarial perturbations under the ℓ₂ norm."

> "No certified defense has been shown feasible on ImageNet except for smoothing."

> _Not verbatim. Checked against `raw/CRK19_RandomizedSmoothing.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> Smoothing delivers higher certified accuracies than competing approaches on smaller-scale datasets where alternatives are viable.

The paper's own sentence, verified:

> "On smaller-scale datasets where competing approaches to certified ℓ2 robustness are viable, smoothing delivers higher certified accuracies."

— abstract.

> "This “randomized smoothing” technique has been proposed recently in the literature, but existing guarantees are loose. We prove a tight robustness guarantee in ℓ2 norm for smoothing with Gaussian noise."

— abstract, on what is new here relative to PixelDP and Li et al.
