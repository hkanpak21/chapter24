---
title: From Information to Generative Exponent, Learning Rate Induces Phase Transitions in SGD
type: source
date_ingested: 2026-08-22
authors: [Konstantinos Christopher Tsiolis, Alireza Mousavi-Hosseini, Murat A. Erdogdu]
venue: venue unconfirmed from PDF (arXiv:2510.21020v1 says Preprint)
year: 2025
tags: [scaling-laws, learning-theory, sample-complexity, statistical-query]
claim_quantifier: conditional
antecedent: Gaussian single-index models under the paper's Assumptions 3.1 and 3.2, online iterative algorithms of the stated one-step form with initialization overlap of order d^{-1/2}; per-corollary coefficient positivity conditions (e.g. mu_p, mu_p2 > 0 for alternating SGD)
model_class: Gaussian single-index models, information exponent p, generative exponent p*
algorithm_class: online (one-pass) gradient-type updates including vanilla SGD, batch-reuse SGD, and layer-wise alternating SGD; the learning rates are part of the class
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: samples
cls_tightness: exponent
cls_baseline: stated
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "iterations of Algorithm 2 are necessary and sufficient to achieve weak recovery."
cls_evidence_src: Cor. 4.3
cls_reason: "Not an attack paper: target/family/phase/access/write = none/none/n/a/none/none. party=learner (rule 3): the bound binds the online algorithm, not an adversary. unit=samples/tightness=exponent for Corollary 4.3's explicit closed-form threshold T(eta)=Theta~(d^{(p-1)v1}) wedge Theta~(eta^{-2} d^{(p2-1)v1}), matching how this corpus already prices the sibling generative-exponent-single-index result. second_notion=none: unlike leap-complexity-sgd or reusing-batches-breaks-exponents, this paper gives one unified formula rather than two separately-proven resource bounds on the learner. baseline=stated: the paper explicitly measures the induced threshold against the plain information-exponent regime (vanilla online SGD's d^{p-1}) it improves on. Caution flagged per assignment brief: Corollary 4.3 proves only WEAK recovery (a detection-shaped guarantee), never full estimation; this is the opposite emphasis from sgd-reuse-info-theoretic-limit in this same batch, which proves strong recovery plus a generalization bound and states so explicitly in its own Detection versus estimation section. Do not conflate the two exponents either: this paper's large-learning-rate regime attains the generative exponent p* (Damian et al. 2024), while its small-learning-rate regime recovers exactly the information-exponent rate of Ben Arous-Gheissari-Jagannath; both are cited correctly in the page's own Connections section."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The sample-complexity exponent of SGD on Gaussian single-index models is shown to be a function of the learning rate, with proven phase transitions between an information-exponent regime and a generative-exponent regime. The framework (Theorem 3.3) covers a class of online one-step update rules through their effective query function psi(y, z) and Hermite-type coefficients mu_i(eta), and gives matching upper and lower bounds (weak recovery, necessary and sufficient iteration counts) as a function of the learning-rate hyperparameters. Specializations: vanilla online SGD recovers the Ben Arous-Gheissari-Jagannath complexity d^{(p-1) or 1}. Batch-reuse SGD interpolates between d^{(p*-1) or 1} at large first-step learning rate and the online-SGD complexity as learning rates shrink, so the batch-reuse escape recorded in [reusing-batches-breaks-exponents](reusing-batches-breaks-exponents.md) is itself learning-rate-conditional. This also resolves the puzzle that full-batch gradient flow, which reuses the whole dataset every step, still carries information-exponent complexity in the best known bounds: small effective learning rate keeps the dynamics in the correlational regime.

The result this ingest was asked to verify at theorem level: the claim that a two-timescale algorithm beats correlational queries without sample reuse. Verified against Section 4.3, with two clauses that the abstract compresses. Algorithm 2 (alternating SGD) is one-pass: at each iteration a fresh i.i.d. sample is drawn and never revisited, so there is no batch reuse. Within an iteration, the single fresh sample is used twice, first in a second-layer update with learning rate eta, then in the first-layer update, and the paper marks this as essential ("Crucially, the same sample (x, y) is used in these two updates"). Substituting the updated second layer into the first-layer step makes the effective update psi(y, z) = y a sigma'(z) + eta y^2 sigma(z) sigma'(z), a non-correlational query through the y^2 term, on the plain squared loss. Corollary 4.3 then proves T(eta) = Theta-tilde(d^{(p-1) or 1}) wedge Theta-tilde(eta^{-2} d^{(p2-1) or 1}) iterations are necessary and sufficient for weak recovery, where p2 = IE(sigma_*^2). So the two-layer algorithm's complexity is governed by IE(sigma_*^2), the information exponent of the squared link, and it beats CSQ-type complexity whenever squaring lowers the information exponent and eta is large enough. Reaching the generative exponent p* in general needs the depth-D extension: with D >= I layers (I from Lemma 2.3, IE(sigma_*^I) = p*, finite for polynomial links) and eta above 1/polylog d, sample complexity is Theta-tilde(d), under additional Hermite-coefficient assumptions.

## Claim Boundary

- Quantified over: one algorithm class (the paper's online one-step framework with its Assumptions 3.1, 3.2) on Gaussian single-index targets. Upper and lower bounds are both within this class. CSQ and SQ enter as motivation and as the source of the exponents' meaning, and SGD is only heuristically a (C)SQ algorithm, a gap the paper states.
- Antecedent: Gaussianity of inputs, single-index structure, initialization overlap of order d^{-1/2}, coefficient positivity (mu_p, mu_p2 > 0, which holds with constant probability under a randomized activation construction), and per-result learning-rate scalings. All stated, all constructions, none verified for any practical training run.
- Does not establish: anything for multi-index or non-Gaussian targets under this framework, full recovery guarantees beyond weak recovery in the quoted corollary, complexity p* for plain two-layer alternating SGD when IE(sigma_*^2) > 2 (depth is needed), or any claim that practical networks operate in the large-eta regime.
- Abstract against theorem: "without reusing samples" is correct in the one-pass sense (no sample appears in more than one iteration) and must not be read as each sample entering only one gradient evaluation, since the within-iteration double use is exactly what generates the non-correlational query. "Go beyond correlational queries" is proven, with near-linear complexity conditional on IE of a power of the link being at most 2, or on sufficient depth.
- Status: proven within model and algorithm class. The thresholds would break outside Gaussian single-index structure, below the learning-rate thresholds (proven, that is the phase transition itself), and under loss or architecture changes not covered by the update framework.
- No-skipping postulate: threatening to exponent-based recipe-independent pricing, supporting the recipe-relative reading with the recipe drawn finely. The same data, model, and loss yield sample-complexity exponent p - 1 or p* - 1 depending on a learning-rate schedule, so a trace's cost is well-defined only when hyperparameters are counted as part of the recipe.

## Key Contributions

- Theorem 3.3: learning-rate-explicit necessary-and-sufficient iteration counts for weak recovery, for a general class of online one-step updates.
- Proven phase transitions in sample complexity as a function of learning rate, locating the crossover (for alternating SGD at p >= 2) at eta ≍ d^{-[(p - p2) or (p - 2)]/2}.
- Unification of vanilla online SGD and batch-reuse SGD in one framework, making the batch-reuse escape learning-rate-conditional.
- Alternating SGD: a one-pass, squared-loss, layer-wise two-timescale algorithm realizing a non-correlational query, with complexity governed by IE(sigma_*^2), and near-linear complexity when that is at most 2.
- The depth-D extension reaching Theta-tilde(d) for polynomial targets when D >= I, with the number of learning-rate phase transitions tied to the number of distinct IE(sigma_*^i).
- An explanation for why full-batch gradient flow's known bounds remain information-exponent-limited despite total data reuse.

## Key Definitions / Theorems

- Information exponent p = IE(sigma_*): first nonzero Hermite coefficient index of the link. Generative exponent p* = GE(sigma_*): the minimum of IE over L2 label transformations, p* <= p always.
- Lemma 2.3 (from Lee-Oko-Suzuki-Wu): there exists I with IE(sigma_*^I) = p*, and I <= C_q for polynomial links of degree q.
- Corollary 4.3 (alternating SGD): under mu_p, mu_p2 > 0, eta at most order 1, gamma ≍ max(d^{-(p/2 or 1)}, eta d^{-(p2/2 or 1)}), initialization overlap d^{-1/2}, with high probability T(eta) = Theta-tilde(d^{(p-1) or 1}) wedge Theta-tilde(eta^{-2} d^{(p2-1) or 1}) iterations are necessary and sufficient for weak recovery.
- Depth extension: T = max over i <= D of Theta-tilde(eta^{-2(i-1)} d^{(p_i - 1) or 1}), p_i = IE(sigma_*^i).

## Connections

- [generative-exponent-single-index](generative-exponent-single-index.md): supplies the exponent p* this paper's large-learning-rate regime attains.
- [reusing-batches-breaks-exponents](reusing-batches-breaks-exponents.md): the batch-reuse escape is subsumed and sharpened, holding only above a learning-rate threshold. This adds a clause to the standing note that the information exponent is a property of single-pass SGD: it is a property of single-pass SGD at correlational learning-rate scalings, and one-pass algorithms with layer-wise two-timescale updates sit outside it too.
- [information-exponent-online-sgd](information-exponent-online-sgd.md): the small-learning-rate regime, recovered exactly.
- [feature-learning-improves-scaling](feature-learning-improves-scaling.md): the same algorithm-relativity of exponents on the compute axis, and both use second-layer/first-layer timescale separation as the mechanism carrier.
- For the programme: this is the sharpest current instance of the unit (a sample-complexity exponent) moving under a hyperparameter, so any adversary priced in these exponents must have its learning-rate schedule written into the class definition.

## Open Questions / Limitations

- Multi-index targets and non-Gaussian data under the framework. Open.
- Whether practically trained networks sit in the large-eta regime for natural tasks. Empirical, untested here beyond simulations.
- Strong recovery and generalization error beyond weak recovery for the new algorithm at matching sharpness. The paper's focus is weak recovery.

## Quotes / Notable Passages

> "introducing a new layer-wise training algorithm that leverages a two-timescales approach (via different learning rates for each layer) to go beyond correlational queries without reusing samples or modifying the loss from squared error"

(Abstract. Verified against Section 4.3 with the two clauses recorded in the Claim Boundary.)

> "Crucially, the same sample (x, y) is used in these two updates."

(Section 4.3. The within-iteration double use that generates the y^2 term.)

> "iterations of Algorithm 2 are necessary and sufficient to achieve weak recovery"

(Corollary 4.3.)

> "alternating SGD improves over online SGD if squaring the target reduces its information exponent"

(Section 4.3, after Corollary 4.3.)

> "the choice of learning rate is as important as the design of the algorithm in achieving statistical and computational efficiency"

(Abstract.)
