---
title: "The Random Oracle Methodology, Revisited"
type: source
date_ingested: 2026-08-22
authors: [Ran Canetti, Oded Goldreich, Shai Halevi]
venue: "STOC 1998, extended abstract (stated in the PDF's own front matter); full version JACM 51(4), 2004 — the journal venue is not stated in the ingested arXiv PDF (cs/0010019)"
year: 2004
tags: [cryptography, hardness-reductions, complexity-theory]
claim_quantifier: existential
antecedent: "The existence of one-way functions for the signature and encryption counterexamples; the CS-proof counterexample needs no computational assumption beyond what the Random Oracle Model itself provides."
---

## Summary

The paper that bounds what an idealized-oracle proof can promise. It constructs
signature and encryption schemes that are secure in the Random Oracle Model and
insecure under every instantiation of the oracle by a concrete function ensemble.
The scheme is built to recognise any concrete implementation of its own oracle and
misbehave exactly then, so the idealized proof is sound and every real
instantiation fails.

## Claim Boundary

- **Quantified over:** the constructed schemes are existential objects; the
  instantiation failure is universal over function ensembles implementing the
  oracle.
- **Antecedent:** one-way functions, for the signature and encryption cases.
- **Does not establish:** that the random oracle methodology fails for natural
  schemes, and the authors do not claim it. The counterexamples are contrived by
  design, and the methodology's practical record is untouched by them.
- **Abstract vs theorem:** none found.

## Key Contributions

- Signature and encryption schemes secure in the Random Oracle Model with, in the
  paper's words, "no implementation" that is secure.
- The diagonalization technique, which the paper notes "can be applied to
  practically any cryptographic application", including CS-proofs.

## Connections

- [Fine-Grained One-Way Functions](fine-grained-one-way-functions.md) — the Random
  Language Model there is an idealization of the same methodological family.

## Open Questions / Limitations

- The gap between contrived and natural uninstantiability is the standing question
  the paper leaves open.

## Quotes / Notable Passages

Verified against `raw/CGH04_RandomOracleRevisited.pdf` on 2026-08-22.

> "it will be easy for an adversary to make sure that the former case always occurs under any implementation of the Random Oracle Model, thus no implementation may be secure"

> "the same technique can be applied to practically any cryptographic application"
