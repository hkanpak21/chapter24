---
title: "Fine-Grained Non-Interactive Key Exchange, Revisited"
type: source
date_ingested: 2026-08-20
authors: [Balthazar Bauer, Geoffroy Couteau, Elahe Sadeghi]
venue: "venue unconfirmed from PDF (no venue line; raw/SOURCES.md records CRYPTO 2024)"
year: 2024
claim_quantifier: conditional
antecedent: "Existence of an exponentially secure injective pseudorandom generator plus sub-exponential hardness of CDH (standard-model result); for the Maurer's-GGM result, a non-uniformly exponentially secure injective PRG, an assumption known to be unsatisfiable beyond time 2^{4λ/5}."
tags: [cryptography, fine-grained-cryptography, key-exchange, generic-group-model, computational-indistinguishability]
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: attacker
cls_unit: time
cls_tightness: exponent
cls_baseline: stated
cls_baseline_checked: yes
cls_second_party: time
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "if the honest parties run in time n, an adversary running in time O(n2−ε) for an arbitrary constant ε > 0 should have vanishing probability of breaking the protocol"
cls_evidence_src: "§1 (Introduction)"
cls_reason: "Classified on Theorem 4, the standard-model 4-NIKE with quadratic gap, the first result the abstract leads with, per rule 1; the Maurer-GGM result (Thm 10, secured under a non-uniform PRG assumption and capped at N^1.6 by the MP23/HIW23 time-space tradeoff) is the paper's second, query-counted result and is not the classified claim. Both parties are computationally bounded in time here, unlike the query-counted ACMS23 predecessor, so unit=time not queries."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

Removes the idealization from the positive half of
[Afshar-Couteau-Mahmoody-Sadeghi](fine-grained-nike-lower-bounds.md). The key idea is to delete the
leakage: ACMS23's 4-NIKE had to publish a hash of part of the discrete-log exponent so that Alice and
Bob could find a "half collision", which forced a leakage-resilient Diffie-Hellman variant that
nobody knows how to reduce to a standard assumption. Here, instead, the exponents are **sparsified** —
each party samples exponents as `Gen(s)` for an injective length-doubling PRG `Gen: {0,1}^λ → Z*_p`,
so the image has size `2^λ` and `N = λ·2^{λ/2}` samples collide by the birthday bound with no leakage
at all. Security reduces to a new **PRG-CDH** assumption, which the paper separately reduces to PRG
security plus CDH.

The second half is stranger and is the paper's own highlight: proving the same protocol secure in
**Maurer's** generic group model turns out to be *harder* than in the standard model, because PRGs
cannot exist inside Maurer's GGM. The resolution is to show that either PRG-CDH holds in the MGGM or
there is an efficient standard-model attack on the PRG — but the attack extracted this way is
**non-uniform**, so the PRG must be fixed rather than keyed, and recent time-space tradeoffs
(Mazor-Pass; Hasegawa-Ito-Wagner, as cited) invert any fixed one-way function on `{0,1}^λ` with a
non-uniform circuit of size `2^{4λ/5}`. That caps the provable gap at `N^{1.6}`.

## Claim Boundary

- **Quantified over:** Uniform time-bounded adversaries for Theorem 4 (standard model), running in
  time `N^{2−ε}`; **generic adversaries counted by `(Equal, Add)` oracle queries** for Theorem 10
  (Maurer's GGM). The two are not the same class and the results are not interchangeable.
- **Antecedent:** Non-standard in strength if not in kind. The PRG must have **near-optimal**
  security — secure against `poly(λ)·2^{(1−ε/2)λ}`-time adversaries when brute force is `2^λ`
  evaluations. Remark 5 states plainly that such a PRG **cannot exist non-uniformly**, so the
  standard-model theorem must be read either as a uniform-security assumption or as requiring a keyed
  family plus a common random string. CDH is needed only sub-exponentially, which the authors argue
  is in line with the state of the art for elliptic curves.
- **Does not establish:** Negligible adversarial advantage. Theorem 4 gives only `o(1)`, and Remark 6
  is explicit: *"as a function of N, this advantage is never negligible."* The authors further
  conjecture that parallel-repetition amplification is impossible here, by analogy with the "dream
  XOR lemma", which they report was proven false assuming iO. Nor does it close the ACMS23 gap: the
  Maurer-model result reaches `N^{1.6}`, against a lower bound that rules out only `o(N^2)`.
- **Abstract vs theorem:** Mild, and worth recording. The abstract advertises *"a smaller hardness gap
  (up to N^{1.6})"* for the Maurer result. Theorem 10 itself is stated for **any** generic adversary
  making at most `N^{2−ε}` queries — quadratic in form. The `N^{1.6}` ceiling comes not from the
  theorem's conclusion but from its **hypothesis being unsatisfiable** beyond `ε > 0.4`. A reader
  seeing only Theorem 10 would take away a quadratic statement.

## Key Contributions

- **The sparsified-exponent 4-NIKE**: replaces ACMS23's half-collision-plus-leakage trick with PRG
  images, removing the need for Pollard's kangaroo algorithm and for a leakage-resilient assumption.
- **The PRG-CDH assumption** and its reduction to PRG security plus CDH (Theorem 7).
- **Theorem 4**: 4-NIKE with quadratic security gap in the **standard model**.
- **Corollary 9**: 6-NIKE under PRG + CDH in bilinear groups; and tradeoffs — a 6-NIKE at `N^{1.5−ε}`
  without pairings, or a 9-NIKE with pairings, by shortening the seed to `3λ/4` bits.
- **Theorem 10**: security of the same protocol in Maurer's GGM under a non-uniform exponential PRG.
- Unconditional variants: `N^{1.2−ε}` in Maurer's model from the best-known Sidon-set-like
  construction, or optimal `N^{2−ε}` at the cost of a CRS of length `Ω̃(N^2)` — longer than the
  honest parties' runtime.

## Key Definitions / Theorems

- **Theorem 4.** With `p ≥ 2^{2λ}` and `N = λ·2^{λ/2}`: if no `N^{2−ε}`-time algorithm has `ω(1)`
  advantage against CDH over `G`, and a `(N^{2−ε}, o(1), Z*_p)` injective PRG
  `Gen: {0,1}^λ → Z*_p` exists, then a 4-party NIKE that is `(N^{2−ε}, o(1))`-secure exists.
- **Theorem 10.** With a **non-uniformly** secure `(Õ(N^{2−ε}), µ, Z*_p)` injective PRG, any generic
  adversary making at most `N^{2−ε}` `(Equal, Add)` queries has advantage at most
  `µ + 1/2^λ + N^{4−2ε}/(p−1)` against the Figure 3 protocol.
- **The N^{1.6} explanation, verbatim:** *"two recent breakthrough results [MP23, HIW23] established
  that every fixed one-way function with domain {0, 1}λ can be inverted by a non-uniform circuit of
  size at most 2^{4λ/5}. This implies that our PRG can at best be assumed to be secure against
  2^{2−ε}-time adversaries for ε > 0.4, from which we can only conclude the inexistence of attacks in
  time ≫ N^{1.6}."* (The `2^{2−ε}` is a typo for `N^{2−ε}`; the conclusion is the `N^{1.6}` figure.)
- **Remark 6, verbatim:** *"However, as a function of N, this advantage is never negligible."*

## Connections

- **Direct predecessor:** [Fine-Grained NIKE: Constructions and Lower Bounds](fine-grained-nike-lower-bounds.md).
  This paper's abstract restates the ACMS23 lower bound accurately, and its bibliography is one of the
  in-batch sources confirming that paper's venue.
- **Concurrent and independent:** [Fine-Grained NIKE without Idealized Assumptions](nike-without-idealized-assumptions.md),
  which reports this paper's results in its own related work under the label "Couteau et al." and
  solves the same open question along a different axis (resource classes rather than assumptions).
- Cites [On Building Fine-Grained One-Way Functions](fine-grained-one-way-functions.md) as one of the
  two lower-bound results in the field; the Brzuska-Couteau bibliography entry here is one of the
  in-batch confirmations of that paper's EUROCRYPT 2022 venue.
- **The advantage ceiling is structural, not incidental.**
  [Public-Key Cryptography in the Fine-Grained Setting](pkc-fine-grained-setting.md) makes the same
  observation from a different construction: in the fine-grained setting the adversary can always
  guess, so advantage is bounded below by `1/poly(n)`.
- Concepts: [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md),
  [Security Gap Exponent (δ)](../concepts/security-gap-exponent.md),
  [Pseudorandomness](../concepts/pseudorandomness.md),
  [Computational Indistinguishability](../concepts/computational-indistinguishability.md).

## Open Questions / Limitations

- Building a fine-grained 4-NIKE with **negligible** adversarial advantage in the standard model —
  the authors' own open question, which they suspect is blocked by a dream-XOR-lemma-style impossibility.
- Closing `N^{1.6}` to `N^{2}` in Maurer's GGM. The authors observe the needed object is a mapping
  from short seeds to a set with a Sidon-set-like combinatorial property, and that explicit
  constructions remain open in additive combinatorics.
- The `Ω̃(N^2)`-length-CRS variant achieves the optimal gap but with setup larger than the honest
  computation, which the authors present as a tradeoff rather than a solution.

## Quotes / Notable Passages

> "Somewhat intriguingly, proving the security of our scheme in Maurer's idealized model turns out to
> be significantly harder than proving its security in the standard model."

> "For example, a primitive with a quadratic gap between the runtime of the honest parties and that of
> the best-possible adversary could be realistically usable: running 2^40 operations requires a
> moderate amount of time on a standard computers, while (2^40)^2 = 2^80 remains out of reach of
> anyone but state-level organizations."
