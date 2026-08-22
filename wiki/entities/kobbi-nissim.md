---
title: Kobbi Nissim
type: entity
entity_type: author
tags: [differential-privacy, statistical-query, PAC-learning, data-reconstruction-attack, cryptography]
---

## About

Ben-Gurion University at the time of the work catalogued here; later Georgetown. Co-founder of differential
privacy and of the reconstruction-attack literature that motivated it, and co-author of the characterization
tying local DP to the statistical query model.

## Contributions / Works

- [Revealing Information while Preserving Privacy](../sources/dinur-nissim-revealing-information.md)
  (Dinur–Nissim, PODS'03) — the founding reconstruction result, and the first paper to make the
  statistical/computational separation its main theorem: `Ω(n)` perturbation against an unbounded adversary,
  `Õ(√T)` against a time-`T` one.
- [What Can We Learn Privately?](../sources/what-can-we-learn-privately.md) (KLNRS08) — private Occam's razor;
  an efficient private PAC learner for parity; **local DP learnability ⟺ SQ learnability**; the masked-parity
  separation of interactive from noninteractive local learning, hence adaptive from nonadaptive SQ.
- [Separating Adaptive Streaming from Oblivious Streaming](../sources/adaptive-vs-oblivious-streaming.md)
  (Kaplan–Mansour–Nissim–Stemmer) — the first separation between oblivious and adversarially robust
  streaming. The space bound is on the streaming algorithm, and inside the proof that algorithm plays the
  space-bounded adversary against a bounded storage model pseudorandom generator.
- The Beimel–Nissim–Omri line on distributed private data analysis is the other root of computational
  differential privacy, alongside [MPRV09](../sources/computational-differential-privacy.md).

## Connections

- Co-authors here: [Adam Smith](adam-smith.md).
- His reconstruction work is the ancestor of [HMST22](../sources/two-party-dp-complexity.md) Theorem 1.6 and
  of [ML24](../sources/query-complexity-reconstruction.md), which calls its own error tolerance "a smoothed
  version of the notion of blatant non-privacy proposed in the seminal work of Dinur and Nissim (2003)".
- Concepts: [statistical query model](../concepts/statistical-query-model.md),
  [local differential privacy](../concepts/local-differential-privacy.md),
  [data reconstruction attack](../concepts/data-reconstruction-attack.md),
  [computational vs statistical memorization](../concepts/computational-vs-statistical-memorization.md).
