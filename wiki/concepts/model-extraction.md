---
title: Model Extraction (Accuracy vs Fidelity)
type: concept
tags: [adversarial-ml, complexity theory, sample-complexity, statistical-query]
---

## Definition

**Model extraction** (also model stealing): an adversary with query access to a deployed victim model
`O : X → Y` runs an extraction algorithm `A(O)` producing `Ô`, an approximate copy.

[Jagielski et al.](../sources/jagielski-model-extraction.md) organize the goal into a spectrum of
decreasing precision:

| Goal | Formal target |
|---|---|
| Exact extraction | `Ô_θ = O_θ` — identical weights. A declared strawman: ReLU networks have large behavioural equivalence classes. |
| Functionally equivalent extraction | `∀x ∈ X, Ô(x) = O(x)`. The hardest goal reachable from input-output pairs. |
| Fidelity extraction | maximize `Pr_{x∼D_F}[S(Ô(x), O(x))]` for a target distribution `D_F` and similarity `S`. |
| Task accuracy extraction | maximize `Pr_{(x,y)∼D_A}[argmax Ô(x) = y]`. The easiest goal. |

**Accuracy and fidelity conflict** whenever the victim is imperfect: a high-fidelity copy must
reproduce the victim's mistakes; a high-accuracy copy must not.

## Intuition

Fidelity asks "does my copy behave like *that model*"; accuracy asks "does my copy do *that job*".
An extraction that scores well on the task while disagreeing with the victim on its errors is a good
accuracy attack and a bad fidelity attack. Downstream attacks pick sides: transferable adversarial
examples and membership inference want fidelity; commercial theft wants accuracy.

## Properties / Theorems

From [Jagielski et al.](../sources/jagielski-model-extraction.md):

- **Query hardness (Thm 1, existential).** There exists a class of width-`3k`, depth-2 ReLU networks
  on `[0,1]^d` at feature precision `p` requiring `Θ(p^k)` logit queries. Constructed family, not a
  statement about trained networks. Broken by side-channel access.
- **Verification hardness (Thm 2, worst-case).** Deciding functional equivalence of two networks over
  `{0,1}^d` from their weights is NP-hard, by reduction from subset sum. About *checking*, not
  *extracting*, and did not obstruct the same paper's efficient `O(dh)` functionally-equivalent attack
  on two-layer networks.
- **Restricted-class sample hardness (Thm 3, imported).** Fidelity extraction of deep random networks
  by any adversary expressible as a [statistical query](statistical-query-model.md) algorithm — which
  includes SGD and PCA — needs `exp(O(h))` samples in the depth. Attributed to Das, Gollapudi, Kumar
  and Panigrahy, arXiv:1904.03866.

## The missing predicate

There is **no formal definition of extraction success** in the literature.
[Shafran, Shumailov, Erdogdu and Papernot](../sources/beyond-labeling-oracles.md) state this directly
and propose a replacement that is a **cost inequality** — extraction succeeds when stealing costs less
than developing —

```
defender  c  = n  (pl  + cc)
attacker  ca = na (pla + cca)
success when   c > ca
```

— and leave it informal, with the model-training term dropped from both sides. Their own experiments
then fall back on an accuracy criterion. The taxonomy above names *goals*; it attaches no budget to
any of them, which is why a taxonomy and a missing success predicate coexist.

Note also that the two papers price different things. Jagielski et al. price the adversary in
**queries** and in **algorithm class** (SQ). Shafran et al. price it in **dollars for data and
labels**. Nobody prices it in an exponent over the honest training cost.

## Where It Appears

- [High Accuracy and High Fidelity Extraction of Neural Networks](../sources/jagielski-model-extraction.md)
- [Beyond Labeling Oracles: What does it mean to steal ML models?](../sources/beyond-labeling-oracles.md)
- Used as a *counterexample generator* in
  [SoK: Data Reconstruction Attacks](../sources/sok-data-reconstruction-attacks.md), where data-free
  extraction produces a high-accuracy stolen model from data "vastly dissimilar" to the victim's
  training set — showing that train-a-model-on-it accuracy is a bad reconstruction metric.

## Related Concepts

- [Statistical Query Model](statistical-query-model.md) — the restricted class Theorem 3 quantifies over.
- [Fiber of the Training Map](fiber-of-the-training-map.md) — extraction concerns the *evaluation* map
  `w ↦ M_w`; keeping the two maps apart is the whole point of that page.
- [Data Reconstruction Attack](data-reconstruction-attack.md) — the analogous subfield with the
  analogous missing definition.
- [Computational Indistinguishability](computational-indistinguishability.md).

## Open Questions

- A success predicate for extraction that is a *definition*, quantifies over a bounded adversary, and
  keeps compute inside the cost. The cost inequality exists in prose; nobody has parameterized it.
- Whether fidelity and functionally-equivalent extraction have success criteria — Shafran et al.
  exclude them from scope, so the "no formal definition" claim is only established for the
  accuracy-driven line.
- Average-case hardness of any extraction goal. Everything proved so far is worst-case or over a
  constructed family.
