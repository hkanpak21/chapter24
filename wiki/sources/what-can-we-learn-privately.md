---
title: What Can We Learn Privately?
type: source
date_ingested: 2026-08-20
authors: [Shiva Prasad Kasiviswanathan, Homin K. Lee, Kobbi Nissim, Sofya Raskhodnikova, Adam Smith]
venue: "FOCS 2008"
venue_evidence: "https://dblp.uni-trier.de/search?q=What%20Can%20We%20Learn%20Privately%20Kasiviswanathan; dblp: FOCS 2008, pp. 531-540 (refereed; confirms PDF's own stated venue). Journal version: SIAM J. Comput. 40(3), pp. 793-826, 2011"
year: 2008
tags: [statistical-query, PAC-learning, learning-theory, differential-privacy, sample-complexity]
claim_quantifier: universal
antecedent: "For the local ⟺ SQ equivalence: efficiency transfer requires TRANSPARENT local randomizers (Definition 5.13); the SQ notion is relaxed to allow a small failure probability β, which the paper argues is necessary because DP algorithms must have nonzero error."
adversary_bound: unbounded (the standard DP distinguisher). The SQ restriction is on the LEARNER, not the adversary.
cls_target: train data
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: algo class
cls_tightness: class
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "We show that a concept class is learnable by a local algorithm if and only if it is learnable in the statistical query (SQ) model."
cls_evidence_src: "Abstract, raw/KLNRS08_WhatCanWeLearnPrivately.pdf"
cls_reason: "Hand-classified 2026-08-22 against codebook revision 2, then migrated through revisions 3 to 5. Carries no verbatim evidence quote, unlike the delegated rows. RECODE 2026-09-03 (R4, no adversary means no phase): phase train time -> n/a."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The paper that ties differential privacy to the statistical query model — and the tie runs through the
**learner**, not the adversary. This distinction is the reason the paper appears in this corpus, and it is
easy to lose.

Four results. (1) A **private Occam's razor**: any concept class `C` is privately agnostically PAC-learnable
with `O(log|C|)` samples, so "almost anything learnable is learnable privately," though not necessarily
efficiently. (2) An **efficient private PAC learner for parity**, whose sample and time complexity are
comparable to the best non-private learner — dispelling the intuition that private learning is just
noise-tolerant learning, since parity is thought hard under random classification noise. (3) The
characterization: **a concept class is learnable by a local (randomized-response) differentially private
algorithm if and only if it is learnable in the SQ model**, with interaction in local algorithms
corresponding to adaptivity in SQ algorithms. (4) A separation: the **masked-parity** class is efficiently
learnable by interactive local algorithms under the uniform distribution but needs exponentially many
samples noninteractively — hence also separating adaptive from nonadaptive SQ learning.

**Where the SQ restriction sits.** A local algorithm accesses the data only through per-record
`ε`-local randomizers (Definition 5.1); `ε`-local algorithms are `ε`-DP (Claim 2.2). The equivalence says
this access restriction on the *learner* is exactly the SQ access restriction on the *learner*. The
adversary in the underlying DP guarantee is the standard one — computationally unbounded, quantified over
all measurable events. **Nothing in this paper measures an adversary in SQ complexity, or in any complexity
at all.** SQ prices the learner under a privacy constraint.

The consequences of (3) are then imported wholesale from learning theory. Because parity needs `2^{d/3}` SQ
queries of tolerance `2^{−d/3}` even with unlimited computing time and uniform examples, but is efficiently
privately PAC-learnable by (2), local learners are a **strict** subset of privately PAC-learnable classes
(Corollary 5.15) — local algorithms require exponentially more data for some tasks than general private
algorithms do.

The paper also raises the "price of privacy" question: the Blum–Dwork–McSherry–Nissim SQ simulation uses
about `t/ε` times more data points than the naive non-private implementation, where `t` is the number of SQ
queries.

## Claim Boundary

- **Quantified over:** (1) all concept classes of cardinality at most `exp(poly(d))`; (3) all concept
  classes `C`, all distributions `X`, with the equivalence stated for interactive local learners versus
  adaptive SQ learners, and for noninteractive versus nonadaptive.
- **Antecedent:** the efficiency half of the equivalence requires **transparent** randomizers — "an
  efficient local learner that uses only transparent randomizers is simulatable by an efficient SQ learner."
  The SQ definition is relaxed to permit failure probability `β`; footnote 6 defends this: "One can show that
  differentially private algorithms must have some non-zero probability of error, so a relaxation along these
  lines is necessary for our results." No distributional assumptions are made for privacy — deliberately,
  since "Such assumptions are fragile and, in particular, would fall apart in the presence of auxiliary
  knowledge."
- **Excluded cases:** the generic learner (1) "might not be efficient." The parity learner (2) does **not**
  extend to agnostic learning, and the paper explains why — agnostic parity is at least as hard as learning
  parity with noise even non-privately. The masked-parity separation (4) is under the **uniform**
  distribution and, per §5.3, "applies only to strong learning."
- **Does not establish:** any statement about a computationally or query-bounded **adversary**. Nor any
  computational hardness of private learning — the sample-complexity results are information-theoretic on
  the learner side.
- **Abstract vs theorem:** none found; the abstract flags "ignoring computational constraints" for result
  (1).

## Key Contributions

- Private Occam's razor: `O(log|C|)` samples suffice for private agnostic PAC learning, so anything learnable
  with polynomially bounded output length is privately learnable with polynomially many samples.
- Efficient private PAC learner for parity, breaking the analogy between private learning and noise-tolerant
  learning.
- **Local DP learnability ⟺ SQ learnability**, preserving interaction/adaptivity and (under transparency)
  efficiency.
- Masked parity: interactive local learning strictly beats noninteractive; adaptive SQ strictly beats
  nonadaptive.
- Corollary 5.15: locally learnable classes are a strict subset of privately PAC-learnable classes.

## Key Definitions / Theorems

- **Definition 5.1 (Local Randomizer).** An `ε`-local randomizer `R : D → W` is an `ε`-DP algorithm on a
  data set of size 1; since all singletons are neighbours, this is a strong condition.
- **Definition 5.2 (LR Oracle), 5.3 (Local algorithm).** An algorithm is `ε`-local if it accesses `z` only
  via `LR_z`, with per-record randomizer budgets summing to at most `ε`. By Claim 2.2, `ε`-local algorithms
  are `ε`-DP.
- **Theorem 3.4 (Generic Private Learner).** For any `C_d` with `|C_d| ≤ exp(poly(d))`, private agnostic
  learning with `n = O((ln|H_d| + ln(1/β)) · max{1/(εα), 1/α²})` labeled examples.
- **Theorem 4.4.** Efficient private PAC learner for parity; sample size differs from the non-private
  `O((d + ln(1/β))/α)` by a factor `O(ln(1/β)/ε)`.
- **Theorem 5.7 (Local simulation of SQ)** and its converse — the two halves of the equivalence.
- **Theorem 5.14 (Equivalence).** `C` is locally learnable using `H` by an interactive local learner with
  access to `LR_z` **iff** `C` is SQ learnable using `H` by an adaptive SQ learner with access to
  `SQ_{c,X}`; with (i) efficient SQ ⟹ efficient local with transparent randomizers, (ii) the converse under
  transparency, (iii) nonadaptive ⟺ noninteractive.
- **Corollary 5.15.** Locally learnable ⊊ privately PAC learnable.
- **Theorem 5.16.** The masked-parity separation.

## Connections

- Concept: [statistical query model](../concepts/statistical-query-model.md) — this is the canonical bridge
  from SQ to privacy, and the page should record that the bridge lands on the learner.
- Concept: [PAC learning](../concepts/pac-learning.md).
- Concept: [local differential privacy](../concepts/local-differential-privacy.md).
- Named by [GKY11](limits-cdp-client-server.md) as reference [9] — the example of a query "that returns
  classifiers," i.e. the first item on that paper's exclusion list. **A private learner is the canonical
  case GKY11 does not cover.**
- Mirror image of [CIM19](capacity-bounded-dp.md): there the adversary is restricted to a function class and
  the learner is not; here the learner is restricted to statistical queries and the adversary is not.
- [HU14](preventing-false-discovery-hard.md) works in the same SQ model but flips the role again: there the
  *analyst* is the adversary and the SQ oracle is the defender, and query count is the resource.
- [DP-SGD](deep-learning-differential-privacy.md) is the practical descendant of private learning.
- Entities: [Kobbi Nissim](../entities/kobbi-nissim.md), [Adam Smith](../entities/adam-smith.md).

## Open Questions / Limitations

- The efficiency of private learning in general — result (1) is not efficient.
- The power of **nonadaptive** SQ learners, which the paper flags as "an important problem" because most
  practically attractive local algorithms are noninteractive.
- The precise price of privacy in samples; the known simulation costs a factor `≈ t/ε`.

## Quotes / Notable Passages

> "We show that a concept class is learnable by a local algorithm if and only if it is learnable in the
> statistical query (SQ) model."

> "This result dispels the similarity between learning with noise and private learning (both must be robust
> to small changes in inputs), since parity is thought to be very hard to learn given random classification
> noise."

> "we do not make any assumptions on the underlying distribution. Such assumptions are fragile and, in
> particular, would fall apart in the presence of auxiliary knowledge"
