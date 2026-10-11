---
title: Salil Vadhan
type: entity
entity_type: author
tags: [cryptography, differential-privacy, pseudorandomness, computational-indistinguishability]
---

## About

Harvard. The central figure in computational differential privacy: co-author of the definitions, of the first
client-server separation, and of the survey whose open problems the later separations answer. Also co-author
of the framework treating a mechanism's runtime as a leakage channel, and of the Dense Model Theorem work
that the CDP equivalence proof extends.

## Contributions / Works

- [Computational Differential Privacy](../sources/computational-differential-privacy.md) (MPRV09) — IND-CDP,
  SIM-CDP, SIM∀∃-CDP, SIM⁺-CDP; SIM∀∃-CDP ⟺ IND-CDP via an extension of the Dense Model Theorem of
  Reingold–Trevisan–Tulsiani–Vadhan; the candidate two-party Hamming-distance separation.
- [Separating Computational and Statistical Differential Privacy in the Client-Server Model](../sources/separating-cdp-client-server.md)
  (BCV16) — the first client-server separation, an infeasibility result; and §4's strengthening of the
  Groce–Katz–Yerukhimovich dimension barrier to metrics of doubling dimension `O(log k)`.
- [A Framework for Differential Privacy Against Timing Attacks](../sources/dp-against-timing-attacks.md)
  (RV24) — output-conditional timing privacy; DP for programs rather than functions.
- His survey supplies Open Problem 10.6 (is there a task solvable with CDP but not information-theoretic DP
  in the client-server model) and Open Problem 10.8 (the multi-pair dense model extension). Both are answered
  by [GIKKM23](../sources/towards-separating-cdp.md) — 10.6 positively, 10.8 negatively.
- The minimal-assumption question for a CDP/DP separation, raised in the survey, drives
  [HMST22](../sources/two-party-dp-complexity.md) and [HMSTY25](../sources/cdp-inner-product-implies-ot.md).

## Connections

- Co-authors in this wiki: [Kobbi Nissim](kobbi-nissim.md), [Adam Smith](adam-smith.md) (via the DP
  foundations and robust fingerprinting codes), [Jonathan Ullman](jonathan-ullman.md).
- Concepts: [computational differential privacy](../concepts/computational-differential-privacy.md),
  [computational indistinguishability](../concepts/computational-indistinguishability.md),
  [pseudorandomness](../concepts/pseudorandomness.md).
