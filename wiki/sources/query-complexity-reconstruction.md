---
title: On the Query Complexity of Training Data Reconstruction in Private Learning
type: source
date_ingested: 2026-08-20
authors: [Prateeti Mukherjee, Satya Lokam]
venue: "arXiv:2303.16372"
venue_evidence: "dblp: no match for this title/authors (searched directly, no inproceedings/article entry exists); arXiv abstract page (https://arxiv.org/abs/2303.16372) has no Journal-ref field; confirmed no refereed venue"
year: 2024
tags: [differential-privacy, data-reconstruction-attack, sample-complexity, learning-theory]
claim_quantifier: universal
antecedent: "(ε, δ)-DP (or (α, ε)-RDP, or ε-metric DP) learner; training data on a compact metric space (Z, ρ) for Theorem 1, locally compact for Theorem 2; a fixed known dataset D_− of N−1 records shared by learner and adversary; success measured by expected squared reconstruction error against a worst-case target."
adversary_bound: query count (number of draws from the learner's output distribution) — NO computational restriction whatsoever
cls_target: train data
cls_family: reconstruct
cls_phase: post hoc
cls_access: white box
cls_write: read only
cls_frame: compute
cls_party: attacker
cls_unit: queries
cls_tightness: budget
cls_baseline: absent
cls_baseline_checked: yes
cls_second_party: privacy budget
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "Adversary makes n queries to the model, i.e., she draws n samples h1, . . . hn ∼ M(D) from the learner's output distribution"
cls_evidence_src: "§3"
cls_reason: "party=attacker/unit=queries/tightness=budget: n is an explicit numeric query allowance with no stated relation to the learner's own resource use (rule on tightness=budget). access=white box: the paper's own §3 calls this 'a powerful white-box reconstruction adversary' (Remark 8), and D_- is fixed and known to the adversary. second_party=privacy budget: the mechanism M is separately restricted to (ε,δ)-DP (or the Rényi/metric-DP variants), the other party's bound in rule 4's two-parties case; since queries is the only computational-frame bound present (frame=compute per the codebook's 'queries' example) and privacy budget is capability-frame, the computational bound (attacker/queries) decides the row per rule 4's first clause. baseline=absent: the value function V(M,n) is a squared-error threshold with no stated advantage-over-baseline term, matching the Dinur-Nissim precedent for reconstruction bounds with no baseline. phase=post hoc: the adversary queries a learner's output distribution after training, with no further training of its own."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

Has the **right shape** for a programme that wants the adversary's budget as a dependent variable, and the
**wrong unit**. The paper derives lower bounds on the number of queries `n` that a white-box reconstruction
adversary must make to a private learner in order to reach a stated reconstruction error `β`, as a function
of the learner's privacy parameters. Query count is the resource; nothing else about the adversary is
constrained.

The threat model is a privacy game inherited from Balle–Cherubin–Hayes and Guo et al. A dataset `D_−` of
`N−1` records is **known to both learner and adversary**. The learner appends a target `z` and outputs
`h ∼ M(D_− ∪ {z})`. The adversary draws `n` i.i.d. samples `h_1, …, h_n` from that output distribution and
emits a reconstruction. The value function is
`V(M, n) = inf_A sup_{z∈Z} E[ρ(A(h_1, …, h_n), z)²]`, a two-player zero-sum game, and the whole paper lower
bounds `V(M, n)`. The adversary in that infimum ranges over **all** functions of `n` samples; it may take
arbitrary time.

Three results:

- **`(ε, δ)`-DP, compact metric space.** Any adversary needs at least
  `Ω( ln(diam(Z)²/β²) / ln((e^ε+1)/(2(1−δ))) )` queries to guarantee squared error `≤ β²`. Minimax optimal
  up to constants, for **every** `ε ≥ 0`, `δ ∈ [0,1]`, with `ε`-DP and `(0, δ)`-DP as corollaries.
- **`(α, ε)`-Rényi DP.** `Ω( ln(diam(Z)²/β²) / ln(((1+e^{γε})^{-1} + (1+e^{γε})^{-1/γ})^{-1}) )` with
  `γ = 1 − 1/α`; valid for any `α > 1`, `ε ≥ 0`; recovers the `ε`-DP bound as `α → ∞`. Uses a new total
  variation bound on Rényi-DP output distributions.
- **`ε`-metric DP, locally compact (possibly unbounded) space.** `Ω( d̃ / (ε²β²) )` where `d̃` is the metric
  entropy of the unit ball. Minimax optimal up to logarithmic factors. Claimed as the first reconstruction
  analysis applying directly to unbounded spaces such as all of `R^d`, and the first attempt to quantify the
  semantics of metric DP. An appendix shows the Gaussian mechanism, SGD, and projected noisy SGD satisfy
  metric DP with little or no modification.

The unit is the reason this does not settle anything for our programme. **A query-count lower bound and a
compute lower bound are different objects**, and this paper is only the former. An adversary limited to few
queries may still be arbitrarily powerful per query; an adversary allowed many queries may still be unable to
compute the reconstruction. The paper's own remark concedes the modelling is stylized and defends it as a
worst case: "theoretical lower bounds on the adversary's error suggest that such algorithms implicitly
protect against reconstruction of training samples by less powerful, more realistic adversaries."

## Claim Boundary

- **Quantified over:** all data reconstruction adversaries `A` making at most `n` queries; all target points
  `z ∈ Z` (worst case, via the supremum); all `(ε, δ)` for Theorem 1 and all `α > 1, ε ≥ 0` for the Rényi
  result.
- **Antecedent:** as in the front matter. Note in particular that `D_−` is **fixed and known to the
  adversary** — this is the informed-adversary model, and the bounds are not claimed for a less-informed
  one. Success is expected **squared** error against a metric `ρ`; other loss functions are not covered.
- **Excluded cases:** the metric-DP bound is optimal only up to logarithmic factors. Nothing is claimed for
  `α = 1` or `α ≤ 1` in the Rényi result. Nothing is claimed about *efficient* adversaries — the bounds hold
  regardless, but they also say nothing about which adversaries can be realized.
- **Does not establish:** any computational statement. The bounds are information-theoretic in `n`. It does
  not establish that a real attacker needs that many queries in wall-clock or sample terms, and it does not
  establish an upper bound on the number of queries a deployed system may safely answer in practice.
- **Abstract vs theorem:** none found. The abstract states the bounds as functions of privacy parameters and
  calls them minimax optimal, which matches the theorems.

## Key Contributions

- Query complexity as an explicit dependent variable in a reconstruction bound, parameterized by the
  learner's `(ε, δ)`.
- Minimax-optimal bounds for all `(ε, δ)` regimes on arbitrary compact metric spaces.
- The first non-asymptotic reconstruction analysis for `(α, ε)`-Rényi DP valid for all `α > 1`, with a novel
  total-variation bound for Rényi-DP output distributions.
- Reconstruction bounds under metric DP on unbounded, locally compact spaces, and the observation that the
  Gaussian mechanism, SGD, and projected noisy SGD already satisfy metric DP.

## Key Definitions / Theorems

- **Definition 3 (Packing number).** `M(η, Z, ρ)`, used throughout the lower bounds.
- **Definition 4 (Pure DP).** Standard, plus the max-divergence form.
- **The game.** `V(M, n) = inf_A sup_{z∈Z} E_{h_1,…,h_n ∼ M(D_−∪{z})}[ρ(A(h_1,…,h_n), z)²]`.
- **Theorem 1 / Theorem 9 (`(ε, δ)`-DP).** `V(M, n) ≳ diam(Z)² · ((2(1−δ))/(e^ε+1))^{...}`, equivalently
  the query lower bound stated above; minimax optimal up to constants.
- **Theorem 2 (`ε`-metric DP).** `Ω(d̃/(ε²β²))` queries, minimax optimal up to logarithmic factors.

## Connections

- Concept: [data reconstruction attack](../concepts/data-reconstruction-attack.md).
- Concept: [computational vs statistical memorization](../concepts/computational-vs-statistical-memorization.md)
  — this paper sits entirely on the statistical side, with `n` as the only budget.
- Same informed-adversary reconstruction game as [CHSS24](attaxonomy.md) Definition 4.1, which then relaxes
  the *knowledge* dimension while this paper varies the *query* dimension. The two relaxations are
  orthogonal and, as far as either paper says, uncombined.
- [SAH+25](adversary-aware-dp-bounds.md) unifies the bound landscape without a query dimension; this paper
  supplies one and is not in that unification.
- [Cohen et al.](cohen-data-reconstruction.md) gives reconstruction a **computational** security definition;
  contrast the units.
- [Dinur–Nissim PODS'03](dinur-nissim-revealing-information.md) is the ancestor, and the paper says so:
  the error tolerance `β` is "a smoothed version of the notion of blatant non-privacy proposed in the seminal
  work of Dinur and Nissim (2003)." But Dinur–Nissim's separation is by *compute*; this one is by *queries*.
- [HU14](preventing-false-discovery-hard.md) is the other query-count-as-security-parameter result, and it
  does add a computational hypothesis.
- [DP-SGD](deep-learning-differential-privacy.md) is the mechanism whose metric-DP property the appendix
  establishes.
- [Haghifam–Smith–Ullman](haghifam-sample-complexity-mia.md) prices an MIA adversary in samples rather than
  queries — a third unit, same information-theoretic posture.

## Open Questions / Limitations

- The stylized threat model. The adversary knows `N−1` records exactly and draws i.i.d. from the output
  distribution; real attackers do neither.
- No computational restriction, so the bounds cannot distinguish an expensive attack from a cheap one.
- Metric-DP bound is tight only modulo logarithmic factors.
- **Venue unconfirmed.** Treat as preprint until resolved.

## Quotes / Notable Passages

> "the number of interactions between the adversary and the learner, which we call the adversary's query
> complexity n, is crucial to the success of the attack."

> "What is the maximum number of queries that a private learner can safely answer, while avoiding highly
> accurate reconstruction of training samples by any adversary?"

> "Since adversaries are generally resource bounded in almost all practical settings, we assume that the
> query complexity of A, i.e., the number of times that A can query M is finite."
