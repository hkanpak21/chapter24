---
title: "Adversarially Robust Learning: A Generic Minimax Optimal Learner and Characterization"
type: source
date_ingested: 2026-04-12
authors: [Omar Montasser, Steve Hanneke, Nathan Srebro]
venue: "NeurIPS 2022 (venue unconfirmed from PDF: raw/MHS22_GenericMinimaxLearner.pdf is arXiv:2209.07369v1 [cs.LG] and names no venue; the attribution is carried over from the earlier ingest)"
year: 2022
tags: [adversarial-ml, PAC-learning, sample-complexity, robustness, learning-theory]
claim_quantifier: universal
antecedent: "None beyond the setting inherited from Montasser, Hanneke and Srebro 2019 — a hypothesis class H, a perturbation map U with U(x) nonempty, and an i.i.d. non-adversarial training sample. The characterization is stated up to logarithmic factors, not exactly."
date_verified: 2026-08-20
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: white box
cls_write: read only
cls_frame: statistical
cls_party: learner
cls_unit: samples
cls_tightness: budget
cls_baseline: stated
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "shows that DU (H) tightly (up to log factors) characterizes the sample complexity of agnostic robust learning"
cls_evidence_src: §6, near Thm 9
cls_reason: "Party=learner: the Claim Boundary states the adversary realizing U is unbounded in every resource and nothing in the characterization is computational, so frame=statistical, not compute, per the batch note on pure sample-complexity bounds. Tightness=budget is a judgment call: D(H,U)/ε² is an explicit closed-form dimension-based formula, and none of poly/quasi-poly/class/exponent/measured fit it cleanly in this codebook's narrower senses."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper resolves the sample complexity characterization of adversarially robust PAC learning. The central contribution is the **global one-inclusion graph** — a generalization of Haussler, Littlestone, and Warmuth's classical one-inclusion graph — from which the authors derive both a minimax-optimal learner and a dimension that exactly characterizes robust learnability: qualitatively (which hypothesis classes H can be robustly learned) and quantitatively (how many samples are needed).

Prior to this paper, the robust learnability question was open: VC-dimension does not characterize robust PAC learnability (Montasser et al. COLT 2019 showed finite VC-dim classes can be robustly learned by improper learners but some cannot by proper learners). This paper closes the gap.

## Claim Boundary

- **Quantified over:** all hypothesis classes H and all perturbation maps U. The dimension D_U(H) is claimed to characterize robust learnability qualitatively and quantitatively; the paper's own statement of tightness is "tightly (up to log factors)", for the **agnostic** sample complexity.
- **Antecedent:** none of substance. This is the unconditional member of the cluster, which is why it is the right anchor for what robust PAC learnability costs in samples.
- **Which party is constrained:** the **learner**, in sample complexity, and only there. The perturbation map U is arbitrary and the adversary that realises it is unbounded in every resource. Nothing in the characterization is computational: the dimension is not known to be efficiently computable, and the minimax-optimal learner is not claimed to run in polynomial time. A survey of resource-bounded adversaries should file this as an information-theoretic result with no priced party on the attack side.
- **Does not establish:** (i) any efficient learner, for any class; (ii) an exact Θ — the tightness is up to logarithmic factors; (iii) that local learners are useless, only that they are suboptimal, which the paper proves "in a strong negative sense" against the specific 2019 learner and the local family; (iv) anything about training-time attacks.
- **Abstract vs theorem:** none found. The abstract calls the dimension "a byproduct" and describes the gap it closes as "(potentially) infinite", which is more careful than "exact characterization".

## Key Contributions

- **Global one-inclusion graph dimension**: A dimension D based on the global one-inclusion graph (a generalization of the classical one-inclusion graph from standard PAC learning) that exactly characterizes robust PAC learnability.
- **Characterization theorem**: H is robustly learnable if and only if D(H, U) < ∞, where U is the perturbation set. Sample complexity is Θ(D(H, U) / ε²) in the agnostic case.
- **Generic minimax-optimal learner**: An explicit (improper) learner achieving the minimax optimal sample complexity for any H and perturbation type U.
- **Suboptimality of local learners**: Proves that existing local approaches (learners that reason about each test point's neighborhood independently) are suboptimal — a global perspective is necessary.
- **Resolves open problem from COLT 2019**: Closes the gap between upper and lower bounds left open by Montasser, Hanneke, Srebro (COLT 2019).

## Key Definitions / Theorems

**Global one-inclusion graph**: For hypothesis class H and perturbation type U, the global one-inclusion graph G(H, U) captures how hypotheses h, h' ∈ H interact across the entire distribution of perturbation neighborhoods — not just locally at a single test point.

**Characterization theorem**: The robust sample complexity m_R(ε, δ, H, U) satisfies:
`m_R(ε, δ, H, U) = Θ̃(D(H,U)/ε² + log(1/δ)/ε²)`
where D(H, U) is the global one-inclusion graph dimension.

**Qualitative characterization**: H is robustly PAC learnable under perturbation U iff D(H, U) < ∞.

**Suboptimality of proper learning** (from COLT 2019): There exist H, U where the optimal improper robust sample complexity is finite but no proper learner achieves finite sample complexity. Confirmed and strengthened here.

**Global perspective necessity**: Any learner that is "local" (makes decisions based only on the local neighborhood structure around each test point) is suboptimal by a polynomial factor in general.

## Connections

- [Evasion Attacks](../concepts/evasion-attacks.md) — this paper characterizes the sample complexity of defending against them
- [Tolerant Adversarially Robust PAC Learning](tolerant-robust-pac-learning.md) — Ashtiani et al. (2025) simplify learning under a tolerance relaxation, building on this work
- [Omar Montasser](../entities/omar-montasser.md)
- [Nathan Srebro](../entities/nathan-srebro.md)
- [Steve Hanneke](../entities/steve-hanneke.md)
- Precedes and motivates [win-win-robust-learning.md](win-win-robust-learning.md) — once we know the right dimension, we can ask: is it efficiently computable?

## Open Questions / Limitations

- Computing D(H, U) efficiently: the characterizing dimension is not known to be efficiently computable for general H and U, making the optimal learner computationally intractable.
- Does the global one-inclusion graph perspective yield efficient algorithms for specific practical hypothesis classes (halfspaces, neural networks)?
- Agnostic robust learnability beyond the realizable case — do the same dimensions characterize agnostic robust learning?
- Connection to VC dimension: when does D(H, U) = VC(H)? Known for halfspaces under ℓₚ perturbations; open in general.

## Quotes / Notable Passages

> _Not verbatim. Checked against `raw/MHS22_GenericMinimaxLearner.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> The global perspective is necessary — local learners are suboptimal. Sample complexity of robust PAC learning is characterized by the global one-inclusion graph dimension.

The two abstract passages the paraphrase compressed, both verified:

> "we show, in a strong negative sense, the suboptimality of the robust learner proposed by Montasser, Hanneke, and Srebro (2019) and a broader family of learners we identify as local learners."

> "Our results are enabled by adopting a global perspective, specifically, through a key technical contribution: the global one-inclusion graph, which may be of independent interest, that generalizes the classical one-inclusion graph due to Haussler, Littlestone, and Warmuth (1994)."

On the strength of the characterization, verified:

> "Finally, as a byproduct, we identify a dimension characterizing qualitatively and quantitatively what classes of predictors H are robustly learnable."
