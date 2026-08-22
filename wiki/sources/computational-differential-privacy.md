---
title: Computational Differential Privacy
type: source
date_ingested: 2026-08-20
authors: [Ilya Mironov, Omkant Pandey, Omer Reingold, Salil Vadhan]
venue: CRYPTO 2009 — not stated in this PDF; attribution taken from the reference lists of DP20_SoKDifferentialPrivacies ("Advances in Cryptology-CRYPTO 2009, Springer, 2009") and from the abstracts of BCV16 and GIKKM23, both of which cite it as "CRYPTO 2009"
year: 2009
tags: [cryptography, computational-indistinguishability, pseudorandomness, differential-privacy, one-way-functions]
claim_quantifier: existential
antecedent: "For the main equivalence: ε_κ ∈ O(log κ), non-uniform ppt adversaries, and the Dense Model Theorem of Reingold–Trevisan–Tulsiani–Vadhan extended by Claim II of their Theorem 2. For the Hamming-distance protocol: additively homomorphic encryption."
adversary_bound: PPT (non-uniform polynomial-size circuits)
---

## Summary

The definitional paper. It introduces the computational relaxations of differential privacy that every
later paper in this corpus takes as given, and it proves the one non-trivial relation among them.

Two definitional routes are offered. **IND-CDP** replaces the unbounded distinguisher of `(ε, δ)`-DP by
a non-uniform ppt one and lets `δ` be negligible; the authors note that starting from pure `ε`-DP instead
gives nothing new, because the indicator of a singleton is already a legal distinguisher — "The reason we
do not consider the computational analogue of ε_κ-dp (with δ = 0) is that it ends up being equivalent to
information-theoretic ε-dp." **SIM-CDP** asks instead that the mechanism be computationally
indistinguishable from some `ε`-DP mechanism `F`, where `F` need not be efficiently computable, "it only
has to exist, and be (information theoretically) differentially private." **SIM∀∃-CDP** weakens SIM-CDP
by reversing quantifiers: the statistical simulator may depend on the pair of adjacent databases.

**The precise logical situation, and the thing most often misstated: they prove SIM-CDP ⟹ SIM∀∃-CDP ⟹
IND-CDP (Theorem 1) and leave the converse of the first implication open.** The main technical theorem is
the equivalence of the *weaker* SIM∀∃-CDP with IND-CDP (Theorem 3), and it holds under a stated
condition, `ε_κ ∈ O(log κ)`. There is no general SIM/IND equivalence in this paper, and the SIM-CDP ⟸
IND-CDP question was still open when [GIKKM23](towards-separating-cdp.md) wrote — which cites it as
Vadhan's Open Problem 10.8 and notes that its resolution in the affirmative would have collapsed CDP to
SDP.

The proof of Theorem 3 is the paper's real content and the reason it sits in a cryptography venue. The
authors observe that the DP conditions are literally density conditions on distributions: `f` is `ε`-DP
iff `f(D)` is `e^ε`-dense in `f(D')` for all adjacent pairs, and IND-CDP iff `f_κ(D)` is
`(e^{ε_κ}, 1/s(κ))`-**pseudodense** in `f_κ(D')` against circuits of size `s(κ)`. The Dense Model Theorem
of Reingold–Trevisan–Tulsiani–Vadhan (itself descended from Green–Tao and Tao–Ziegler) says pseudodensity
decomposes into density plus indistinguishability. That gives one side. The new ingredient is **Claim II**
of their Theorem 2: if `Y` is also `e^ε`-dense in `X`, the model `M` can be chosen so that `Y` and `M` are
*mutually* `e^ε`-dense. This symmetrization is what the symmetric definition of differential privacy
requires, and it is proved by a minimax/LP-duality argument against the convex set of mutually dense
distributions.

The paper also extends the definitions to interactive two-party protocols, where it isolates a fourth
notion, **SIM⁺-CDP**, phrased in the ideal/real paradigm with a possibly inefficient simulator, and
separates it from SIM-CDP (Theorem 4.2). And it proposes the two-party Hamming-distance problem as a
candidate separation — a `sim-cdp` protocol with `O(1)` additive error (Theorem 5), against an
information-theoretic protocol with only multiplicative error (Theorem 6). A footnote records that the
gap was subsequently shown inherent, citing Reingold–Vadhan personal communication; the published version
is McGregor et al. FOCS'10.

## Claim Boundary

- **Quantified over:** non-uniform ppt distinguishers (equivalently polynomial-size circuit families),
  all adjacent database pairs of size at most `p(κ)`, all advice strings of size at most `p(κ)`.
  Theorem 3 quantifies over ensembles `{f_κ}` that are `ε_κ`-IND-CDP with `ε_κ ∈ O(log κ)`.
- **Antecedent:** Theorem 3 requires `ε_κ ∈ O(log κ)` and rests on Theorem 2, which requires
  pseudodensity with respect to the *enlarged* class `T(A)` of threshold-of-`k`-functions from `A ∪ Ā`
  with `k = O(1/δ² log(e^ε/4δ))` — a standard reduction-slack condition. The Hamming-distance protocols
  require additively homomorphic encryption and (in the malicious case) the usual machinery; the
  information-theoretic protocol `π*_h` sanitizes Kushilevitz–Ostrovsky–Rabani sketches by randomized
  response.
- **Excluded cases:** the `δ = 0` computational analogue is excluded as vacuous (it collapses to
  statistical `ε`-DP). Composition and group privacy are proved for all notions **except** that group
  privacy is not directly proved for SIM∀∃-CDP: "for all but sim∀∃-cdp we directly prove group privacy."
  Adaptive composition of the interactive notions is deferred to the full version. Theorem 6's utility
  guarantee holds only for `h(a,b) ∈ ω(1/(ε²δ²) (ln(5n/η))⁴)`; below that the accuracy claim lapses
  (privacy does not).
- **Does not establish:** SIM-CDP ⟺ IND-CDP. It establishes SIM∀∃-CDP ⟺ IND-CDP and SIM-CDP ⟹
  SIM∀∃-CDP. It does not establish a separation between CDP and DP — the Hamming-distance protocols are
  offered as a *candidate*, and the paper says "We propose the problem ... as a candidate for separating
  the power of computational and information-theoretic definitions of privacy." It does not establish
  anything about the single-curator client/server model.
- **Abstract vs theorem:** the abstract says "We extend the dense model theorem of Reingold et al. to
  demonstrate equivalence between two definitions (indistinguishability- and simulatability-based) of
  computational differential privacy." Read alone this invites the reading that SIM-CDP ⟺ IND-CDP. The
  body is explicit that the equivalence is with the weaker SIM∀∃ variant and that the SIM-CDP converse is
  open: "The converse of this statement, however, is an intriguing question that we leave open in this
  work." Flagging this as the one place the abstract is looser than the theorem.

## Key Contributions

- IND-CDP, SIM-CDP, SIM∀∃-CDP, and (interactive) SIM⁺-CDP.
- The observation that the pure-`ε` computational analogue is vacuous, which is why every CDP definition
  carries a negligible additive slack.
- SIM-CDP ⟹ SIM∀∃-CDP ⟹ IND-CDP; SIM∀∃-CDP ⟺ IND-CDP for `ε_κ ∈ O(log κ)`.
- The dictionary between DP and pseudodensity, and the symmetric extension (Claim II) of the Dense Model
  Theorem — a contribution to the pseudorandomness literature independent of privacy.
- SIM⁺-CDP, and its separation from SIM-CDP: there is a protocol computing `h` exactly that is SIM-CDP
  but not SIM⁺-CDP.
- The candidate two-party Hamming-distance separation, with `O(1)` additive error under CDP.

## Key Definitions / Theorems

- **Definition 3 (IND-CDP).** For every non-uniform ppt `A`, every polynomial `p`, all adjacent
  `D, D' ∈ D` of size `≤ p(κ)`, and every advice string `z_κ`:
  `Pr[A_κ(f_κ(D)) = 1] ≤ e^{ε_κ} · Pr[A_κ(f_κ(D')) = 1] + negl(κ)`.
- **Definition 4 (SIM-CDP).** There exists an ensemble `{F_κ}` of `ε_κ`-DP mechanisms with
  `|Pr[A_κ(f_κ(D)) = 1] − Pr[A_κ(F_κ(D)) = 1]| ≤ negl(κ)` for every `D`. `F_κ` need not be ppt.
- **Definition 5 (SIM∀∃-CDP).** For all sequences of adjacent pairs there exist `{F_κ(D_κ)}`,
  `{F_κ(D'_κ)}` that are two-sided `ε_κ`-DP on that pair and each indistinguishable from the
  corresponding `f_κ`.
- **Theorem 1.** SIM-CDP ⟹ SIM∀∃-CDP ⟹ IND-CDP. "The first implication is by construction, the second
  follows by a hybrid argument."
- **Theorem 2.** Dense Model Theorem with symmetry. Claim I (from RTTV): pseudodensity ⟹ density +
  indistinguishability. **Claim II (new):** if additionally `Y` is `e^ε`-dense in `X`, the model can be
  chosen mutually `e^ε`-dense with `Y`.
- **Theorem 3.** `ε_κ`-IND-CDP with `ε_κ ∈ O(log κ)` ⟹ `ε_κ`-SIM∀∃-CDP.
- **Theorem 4.** SIM⁺-CDP ⟹ SIM-CDP, and SIM-CDP ⇏ SIM⁺-CDP.
- **Theorem 5.** A two-round protocol `π_h` for Hamming distance with `Pr[|h* − ĥ| ≥ γ] ≤ ξ` for
  constants `γ, ξ` depending only on `ε, γ`, providing `ε_κ`-SIM-CDP. Error independent of `n`.
- **Theorem 6.** An `ε`-DP protocol `π*_h` with multiplicative guarantee
  `Pr[h* ≤ ĥ ≤ (1+γ)h*] ≥ 1 − η`, valid only above the stated threshold on `h(a,b)`.

## Connections

- Concept: [computational differential privacy](../concepts/computational-differential-privacy.md).
- Concept: [computational indistinguishability](../concepts/computational-indistinguishability.md).
- [GKY11](limits-cdp-client-server.md) relies on the SIM∀∃-CDP ⟺ IND-CDP equivalence to extend its
  Theorem 2 from SIM-CDP to IND-CDP, and *weakens* Definition 6 relative to this paper (requiring the
  simulator only `(ε, negl)`-DP) in order to strengthen its own impossibility.
- [BCV16](separating-cdp-client-server.md) achieves the *stronger* notion (PURE-SIM-CDP) and thereby
  can only get infeasibility, not impossibility.
- [GIKKM23](towards-separating-cdp.md) works exclusively with IND-CDP and states why: "SIM-CDP cannot be
  used for the separation we are looking for." It also records that MPRV09's own remark — that extending
  the dense model theorem to multiple pairs would collapse CDP into SDP — is negatively answered by
  their separation.
- [HMST22](two-party-dp-complexity.md) and [HMSTY25](cdp-inner-product-implies-ot.md) take the
  two-party Hamming/inner-product problem posed here and settle its cryptographic complexity: key
  agreement is necessary, and at accuracy `O(n^{1/6})` oblivious transfer is necessary.
- [DP20](sok-differential-privacies.md) catalogues IndCDP and SimCDP as the sole occupants of its
  dimension **C**, computational power, and reproduces both definitions.
- [CIM19](capacity-bounded-dp.md) positions capacity-bounded DP as orthogonal to this paper's axis: its
  adversary is bounded by function class, not runtime.
- Entities: [Salil Vadhan](../entities/salil-vadhan.md).

## Open Questions / Limitations

- **IND-CDP ⟹ SIM-CDP is left open** and remained open at least through 2023.
- Fully general adaptive composition for the interactive notions is deferred.
- The candidate separation is two-party, not client/server; the paper says nothing about the single
  curator, which is the setting [GKY11](limits-cdp-client-server.md) then attacks.

## Quotes / Notable Passages

> "The converse of this statement, however, is an intriguing question that we leave open in this work."

> "Note that the definition does not require F to be computable in probabilistic polynomial time; it only
> has to exist, and be (information theoretically) differentially private."

> "The reason we do not consider the computational analogue of ǫκ-dp (with δ = 0) is that it ends up being
> equivalent to information-theoretic ǫ-dp."

> "In fact, ind-cdp can be stated in terms of pseudodensity of the mechanism's distribution over adjacent
> datasets"
