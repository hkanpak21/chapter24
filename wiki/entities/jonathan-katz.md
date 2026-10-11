---
title: Jonathan Katz
type: entity
entity_type: author
tags: [cryptography, one-way-functions, impossibility-frameworks, differential-privacy]
---

## About

University of Maryland (at the time of the work catalogued here). Cryptographer; in this wiki he appears as
co-author of the black-box and constant-dimension barriers to computational differential privacy in the
client/server setting.

## Contributions / Works

- [Limits of Computational Differential Privacy in the Client/Server Setting](../sources/limits-cdp-client-server.md)
  (GKY11) — two conditional negative results: one against fully black-box constructions from primitives
  instantiable by a random object (using the Gennaro–Gertner–Katz–Trevisan technique), and one for outputs in
  `R^n` with constant `n` under polynomially bounded `L_p`-moment error. **Read that page's Claim Boundary
  before citing the result**; the authors' own limitations subsection excludes classifiers, graphs, synthetic
  databases, growing dimension, and unbounded error.
- The framing observation in the same paper that best achievable utility can never improve when utility is
  efficiently computable, because the utility function becomes the distinguisher — which localizes the whole
  CDP question onto efficiency.

## Connections

- The paper's acknowledgements credit [Adam Smith](adam-smith.md) with suggesting the problem.
- Answered by [BCV16](../sources/separating-cdp-client-server.md) and
  [GIKKM23](../sources/towards-separating-cdp.md), both of which route through the stated exclusions.
- Concepts: [computational differential privacy](../concepts/computational-differential-privacy.md),
  [one-way functions](../concepts/one-way-functions.md).
