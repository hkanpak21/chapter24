---
title: "Beyond Labeling Oracles: What does it mean to steal ML models?"
type: source
date_ingested: 2026-08-20
authors: [Avital Shafran, Ilia Shumailov, Murat A. Erdogdu, Nicolas Papernot]
venue: Preprint (every page is stamped "A PREPRINT"; arXiv:2310.01959v3, 13 Jun 2024) — venue unconfirmed from PDF
year: 2024
tags: [adversarial-ml, learning-theory, sample-complexity, computational-cost]
claim_quantifier: empirical
antecedent: "For the negative cost conclusion: that the victim controls the informativeness of its OOD responses (the authors' own hybrid-model instrumentation V_h), and that commercial labeling prices are those quoted in §3.2. Neither is known to hold of deployed systems — the instrumentation is the authors' construction, not a shipped defence."
cls_target: parameters
cls_family: extract
cls_phase: post hoc
cls_access: black box
cls_write: read only
cls_frame: none
cls_party: none
cls_unit: none
cls_tightness: unstated
cls_baseline: absent
cls_second_party: none
cls_second_notion: none
cls_assessed: 
cls_evidence: absent
cls_evidence_src: "classified by hand in the first batch, before the evidence requirement was added to the brief"
cls_reason: "Hand-classified 2026-08-22 against codebook revision 2, then migrated through revisions 3 to 5. Carries no verbatim evidence quote, unlike the delegated rows."
cls_prov: hand
cls_date: 2026-08-22
---

## Summary

The paper attacks the standing motivation for model extraction (ME): that stealing a deployed model
is cheaper than training one. It disentangles the adversary into a 3-tuple `(D_IND, D_OOD, Π)` —
in-distribution prior data, out-of-distribution query distribution, and query-selection policy — and
then holds two of the three fixed to see which drives attack performance. The answer is prior
knowledge, not the policy. With the victim's OOD responses decorrelated from its in-distribution
behaviour, the attacker's success collapses back onto how much in-distribution data it already had,
and the victim model degenerates into a labelling oracle that is not obviously cheaper than a
crowdsourced annotator.

For this programme the empirical content is secondary. The load-bearing sentence is in §3.2, and it
is a **statement about the absence of a definition**:

> "We are not aware of any ME literature that formally defines what makes model extraction attacks
> successful."

What follows is the part worth recording. The authors' proposed repair is **a cost inequality**, not
an accuracy predicate: ME "can be considered successful if stealing a model costs less than
developing it." They then write the inequality down in dollars —

```
defender cost   c  = n  * (pl  + cc)
attacker cost   ca = na * (pla + cca)
attack succeeds when   n * (pl + cc)  >  na * (pla + cca)
```

— instantiate it on CIFAR-10 (a 20M-query data-free attack must buy labels at under `$0.00012` each
to break even), and **stop**. The inequality is never made a definition, never parameterized, never
given units beyond currency, and — critically — the model-training term is dropped: the three cost
components named are data collection, data labelling, and model training, but only the first two
appear in `c` and `ca`. Compute is named and then discarded.

The gap closes visibly inside the paper itself. Having said no formal success criterion exists and
proposed a cost criterion, the evaluation reverts to accuracy: "We define a successful attack as one
that produces a model that performs on a task nearly as well as the victim model." So the paper
contains, in a single document, the diagnosis (no formal success predicate), the correct shape of the
repair (a computational-cost inequality between attacker and defender), and the failure to carry the
repair into its own measurements.

## Claim Boundary

- **Quantified over:** accuracy-driven ME attacks on vision and language classification benchmarks
  (CIFAR-10, MNLI, SST-2 and similar), with black-box query access returning full probability
  vectors. Fidelity-driven and cryptanalytic extraction are **explicitly excluded** from scope
  ("this line of research falls outside the scope of our work"), as are side-channel attacks. The
  "no formal definition" claim is quantified over the ME literature known to the authors, and is
  stated as their awareness, not as a proof of non-existence.
- **Antecedent:** the cost-ineffectiveness conclusion holds *given* that OOD queries are made
  uninformative about IND behaviour. That is achieved by the authors' hybrid victim `V_h` = original
  model `V_o` plus a fake-boundary module `V_f` selected by a confidence threshold. Absent that
  instrumentation, the paper's own §5.3 concedes OOD queries *can* reduce data costs. So the
  antecedent is a defence the authors built, not a property of currently deployed APIs.
- **Does not establish:** (a) that ME is impossible or infeasible — §5.1 says extraction
  "definitively works"; (b) that no formal success definition for ME *can* exist — only that the
  authors know of none; (c) that the cost inequality is a security definition — it is a two-line
  accounting model in a case study, with no adversary class, no asymptotics, and no exponent; (d)
  that compute is priced — the training-compute term is named and then omitted from the cost model.
- **Abstract vs theorem:** the abstract's "we thoroughly evaluate this assumption and find that the
  attacker often does not [save cost]" is fair to the experiments. The stronger reading — that ME is
  never cost-effective — is not supported and the paper does not make it; §5.5 explicitly preserves
  the medical-data case where victim queries *are* the cheapest labels. One place to watch: the
  Introduction's "the practical threat posed by ME attacks is often exaggerated" is a position
  statement, marked as such ("our position is"), not a result.

## Key Contributions

- The explicit observation that ME has **no formal success predicate** in its literature.
- A proposed replacement predicate that is a **cost comparison between attacker and defender** —
  left informal.
- The `(D_IND, D_OOD, Π)` decomposition of an ME adversary, which makes prior knowledge separable
  from attack policy as an experimental variable.
- OOD instrumentation (`V_h` = `V_o` + `V_f` under a confidence-threshold decision rule) that lets
  the victim's OOD informativeness be dialled down while keeping IND behaviour intact.
- The empirical finding that with OOD informativeness controlled, the victim model reduces to a
  labelling oracle.

## Key Definitions / Theorems

There are no theorems. The formal objects are:

- **ME adversary** as `(D_IND, D_OOD, Π)`.
- **Cost model** `c = n(pl + cc)` for the defender and `ca = na(pla + cca)` for the attacker, with
  success asserted when `c > ca`. `n` is the number of points annotated, `pl` per-label cost, `cc`
  data-collection cost.
- **Operational success**, as used in the experiments: the attacker's model "performs on a task
  nearly as well as the victim model".
- **Random-guess baseline attacker**: samples useful information with probability
  `|X_useful| / |X|`; estimated at `0.00001%` for CIFAR-10 and `0.01%` for MNLI.

The one borrowed formal result is Tramèr's reduction (§4.2): robust adversarial-example detection is
as hard as robust classification, used here to argue that an attacker able to detect IND robustly
could already classify, so the victim is superfluous.

## Connections

- **The extraction half of the "no success predicate" pattern.** Companion documents:
  [SoK: Data Reconstruction Attacks](sok-data-reconstruction-attacks.md) (reconstruction has no
  consensus definition or metric) and
  [On the Necessity of Auditable Algorithmic Definitions](auditable-unlearning-definitions.md)
  (unlearning has no model-level definition at all).
- Sharpens and partly contests
  [Jagielski et al., High Accuracy and High Fidelity Extraction](jagielski-model-extraction.md):
  that paper's accuracy/fidelity taxonomy is the closest thing ME has to a success definition, and
  this paper still calls the field's success criterion undefined — because the taxonomy names goals
  without pricing them.
- The cost inequality is the informal shadow of a fine-grained security statement. Compare the
  bare-inequality problem already recorded on
  [Proof-of-Learning](proof-of-learning.md), whose Property 2 asserts `E[C_A] ≥ E[C_T]` without a
  δ-indexed family. Two independent subfields have now written down "attacker cost vs defender cost"
  and neither parameterized it.
- Attacker-sample-complexity-vs-defender is priced in information-theoretic units by
  [Haghifam–Smith–Ullman](haghifam-sample-complexity-mia.md); this paper prices the same comparison in
  dollars. Neither prices it in an exponent.
- [Covert Learning](covert-learning.md) — the query-access learner whose queries reveal nothing — is
  the dual object: here the concern is what the victim's answers reveal to a querying learner.
- Concept: [Model Extraction (Accuracy vs Fidelity)](../concepts/model-extraction.md).

## Open Questions / Limitations

- The cost inequality is left informal and is the paper's own stated repair. Formalizing it — with an
  adversary class, an exponent, and compute inside the cost — is untouched here.
- The training-compute term is dropped from the cost model without argument beyond "not relevant to
  the current ME threat model".
- The OOD instrumentation is a defence with a utility cost the paper does not measure end-to-end
  against strong OOD detectors; the authors note better detectors would "strictly improve" the
  separation, which cuts in the defender's favour but is not evaluated.
- All conclusions are for accuracy-targeted extraction of classifiers. Fidelity and
  functionally-equivalent extraction are out of scope, so nothing here bears on whether *those*
  goals have formal success criteria.

## Quotes / Notable Passages

> "We are not aware of any ME literature that formally defines what makes model extraction attacks
> successful."

> "intuitively, accuracy-driven ME can be considered successful if stealing a model costs less than
> developing it."

> "We define a successful attack as one that produces a model that performs on a task nearly as well
> as the victim model."

> "a model extraction attacker is only as good as their knowledge of the underlying dataset; but if
> this knowledge includes labels, often there is no need to extract models in the first place."

> "We thus conclude that the adversarial goals and incentives of ME attacks should be redefined."
