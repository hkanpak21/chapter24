---
title: Adam Smith
type: entity
entity_type: author
tags: [differential-privacy, statistical-query, PAC-learning, sample-complexity, learning-theory]
---

## About

Boston University; Pennsylvania State University at the time of the earlier work here. Co-founder of
differential privacy, co-author of the local-DP-equals-SQ characterization, and still active on the question
of what DP parameters actually mean against concrete adversaries.

## Contributions / Works

- [What Can We Learn Privately?](../sources/what-can-we-learn-privately.md) (KLNRS08) — the private Occam's
  razor bound, the efficient private parity learner, and **local DP learnability ⟺ SQ learnability**. Note
  that the SQ restriction there prices the *learner*; the adversary remains the standard unbounded DP
  distinguisher.
- [A Unified Framework for Adversary-Aware Differential Privacy Bounds](../sources/adversary-aware-dp-bounds.md)
  (SAH+25) — a single bound covering membership inference, attribute inference, and reconstruction, with
  multiple targets, non-uniform priors, and approximate success criteria, depending only on the privacy
  parameters and the adversary's baseline. **No computational axis.**
- Credited in [GKY11](../sources/limits-cdp-client-server.md)'s acknowledgements with suggesting the
  client/server CDP problem.

## Connections

- Co-authors here: [Kobbi Nissim](kobbi-nissim.md), [Borja Balle](borja-balle.md).
- Concepts: [statistical query model](../concepts/statistical-query-model.md),
  [local differential privacy](../concepts/local-differential-privacy.md),
  [PAC learning](../concepts/pac-learning.md),
  [adversary knowledge taxonomy](../concepts/adversary-knowledge-taxonomy.md).
