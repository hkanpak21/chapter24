---
title: Bayesian Perspective on Memorization and Reconstruction
type: source
date_ingested: 2026-07-26
date_verified: 2026-08-22
authors: [Haim Kaplan, Yishay Mansour, Kobbi Nissim, Uri Stemmer]
venue: "venue unconfirmed from PDF"
year: 2025
claim_quantifier: existential
antecedent: "The security results are proved for one mechanism (the exact average, or the Laplace-noised average) under one meta-distribution (Tardos-Prior, Definition 3.3), with side conditions N ≥ n ≥ Ω(1) and d ≥ Ω(log(n/δ)), and for the Hamming reconstruction relation at γ ≤ 1/25 (Lemma 3.5) or its two-sided variant (Lemma 3.7). No claim is made for arbitrary mechanisms or arbitrary relations, and the authors state that the exact average is NOT secure for the relation 'z is the average of S'."
adversary_bound: "None. Every definition in the paper (3.1, 3.6, 4.1, 4.4, 4.11) reads 'for all attackers A', and the side-information versions add 'and every side information function SideInfo'. The attacker is unbounded in time, in space and in queries. The word 'computational' in the paper's own usage means extraction-based, in the proof-of-knowledge sense, not time-bounded."
tags: [reconstruction, computational-indistinguishability, learning-theory, cryptography]
---

> **Verified against `raw/KMNS26_BayesianMemorization.pdf` on 2026-08-22.** The framing question, the
> name and form of the security definition, Example 1.3, the adversary quantifier in every definition,
> and the quotations below were checked against the extracted text of that file. Still unverified: the
> venue, and the proofs of Lemma 3.7 and the Section 5 material, which were read for statement rather
> than for correctness. The PDF is arXiv:2505.23658v1 dated May 29, 2025 and names no conference, so
> the year above is the PDF's and the ITCS 2026 attribution carried elsewhere in this wiki rests on
> outside authority. One quotation carried by an earlier version of this page was faithful but elided.
> The programme statement joined the paper's numbered items 1 and 2 with an ellipsis that removed the
> clause naming what was revisited and under which conditions. It is restored below. The page title has
> also been corrected to the paper's own, which has no leading article.

## Summary

The paper poses the computational-versus-statistical memorization question directly, in its own words,
and answers it in the affirmative. It sets out the two existing families of definition first.
Computational memorization defines a model as memorizing an example when the example can be extracted
from it, which the authors align with knowledge extraction in proofs of knowledge. Statistical
memorization defines it through mutual information, as in Brown et al.'s `I(S; h | Nature)`
(Definition 1.1), or through susceptibility to membership inference, as in Definition 1.2.

The separation is then delivered in two pieces. Example 1.3 is the intuition. A dataset `S` is an
`n × d` matrix of uniform bits and the mechanism releases the `n × d/2` matrix `H` of pairwise parities
`H[i,j] = S[i,2j−1] ⊕ S[i,2j]`. Then `I(S; H | Nature) = nd/2`, and the mechanism is
`(n, n·2^{−d/2})`-memorizing in the sense of Definition 1.2, yet no attacker at all can recover a row.

The formal piece is a new security definition, **Bayesian extraction-safe**, built on Cohen et al.'s
Narcissus resiliency by replacing the fixed data distribution with a meta-distribution `Prior` from
which `Nature` is drawn. Section 3 then shows that the exact average solves the marginals problem
while satisfying that definition under the Tardos-Prior, the very prior that underlies the
fingerprinting-code impossibility results. Since Attias et al. used that prior to prove statistical
memorization necessary for stochastic convex optimization, the pair of results separates the two
notions on the same instance.

The reason the separation is not the one this programme wants is stated plainly in the definitions
themselves. Every one of them quantifies over all attackers with no resource bound. The paper's
"computational" is the extraction sense, not the time-bounded sense.

## Claim Boundary

**Quantified over.** The security definitions are universal over attackers and, from §4 onward, also
over side-information functions. The security results are existential over mechanisms and specific in
their prior. Lemma 3.5, Lemma 3.7 and Lemma 4.8 each concern one named mechanism under Tardos-Prior.

**Antecedent.** Tardos-Prior (Definition 3.3) with `N ≥ n`, plus dimension conditions
`d ≥ Ω(log(n/δ))` and, for Lemma 3.7, `N ≥ 10n ≥ Ω(log(1/δ))`. Lemma 4.8 additionally fixes
`δ = 2^{−Ω(d)}`, constant `ξ > 0` and `ε = 0`. These hold by construction, since the prior is chosen
rather than assumed about the world.

**Which party is constrained and in what resource.** Neither party is constrained in computation. The
attacker is constrained only through the definition's success criterion, which discounts any
reconstruction it already had prior knowledge of. Section 4 formalises that discount with surprisal,
requiring `h(z | K, S\{z}) ≥ ξ · h(z | S\{z})` for the attack to count.

**The success criterion and its tolerance.** A reconstruction relation `R`, instantiated as the Hamming
relation `R^H_γ(S, z) = 1 iff ∃x ∈ S with Ham(x, z) ≤ γd`. Tolerance is `(ε, δ)`, and in §4 also `ξ`.
Lemma 3.5 covers `γ ≤ 1/25`.

**The baseline.** The attacker's own success against a fresh sample `T ← Nature`, inherited from
Narcissus resiliency, with `Nature` itself drawn from `Prior` in both experiments. Section 4 conditions
the fresh draw on the side information `K`.

**Does not establish.** No complexity separation. Nothing here distinguishes a polynomial-time
attacker from an unbounded one, and the paper never mentions running time. It also does not establish
a privacy guarantee. The authors are explicit that *"our proposed definition is not a privacy
definition. In particular, it does not prevent the attacker from learning potentially sensitive bits
of information about the sample."* Finally it does not refute Attias et al. It reinterprets their
result, arguing that fingerprinting-code attacks are membership inference rather than reconstruction.

**Abstract versus theorem.** The abstract is measured. It says the definition *"in certain settings,
provably prevents reconstruction attacks"*, which matches the scope of Lemmas 3.5, 3.7 and 4.8. The
looser phrase is in the introduction, where the new definition is called *"computational in nature"*.
Read against Definitions 3.1 through 4.11 that word means extraction-based, not resource-bounded, and
a reader who imports the cryptographic sense will overstate the result.

## Key Contributions

- The explicit framing of computational versus statistical memorization as a question, with a proved
  separation on the fingerprinting-code instance.
- **Bayesian extraction-safe** (Definition 3.1), a meta-distribution refinement of Narcissus
  resiliency, extended in Definition 3.6 to a two-sided relation pair, in Definition 4.1 to
  side-information about the sample, in Definition 4.4 to surprisal-discounted exact reconstruction,
  and in Definition 4.11 to targeted relations.
- Lemma 3.5 and Lemma 3.7: the exact average solves the marginals problem securely under Tardos-Prior.
- Lemma 4.8: the Laplace-noised average of Theorem 4.7 is secure under Definition 4.4 for Tardos-Prior
  with a constant noise parameter, whereas resisting membership inference under the same prior needs
  the dataset to grow polynomially in `d`.
- Example 1.3, the high-mutual-information mechanism with no extraction even against an unbounded
  attacker.
- The argument that fingerprinting-code attacks are membership inference rather than reconstruction,
  and therefore that the impossibility results derived from them do not always bind reconstruction.

## Key Definitions / Theorems

- **The question (verbatim):** *"Is there a difference between computational memorization and
  statistical memorization? Could a model be considered "memorizing" under one definition but not the
  other?"*
- **The programme statement (verbatim, both numbered items, previously elided):** *"1. We put forward a
  new security definition, computational in nature, such that algorithms that satisfy it are guaranteed
  to resist extraction attacks. 2. We revisit problems studied in prior work for when
  statistical-memorization is provably necessary, and show that these problems can be solved while
  satisfying our new security notion (under the same conditions as studied in prior work). Therefore
  these examples separate statistical from computational memorization."*
- **The motivating rhetorical (verbatim):** *"Intuitively, if it is impossible for an attacker to
  extract information from the model, then had the model really memorized it?"*
- **Example 1.3 (verbatim):** *"Furthermore, even given H, no attacker (even unbounded) can guess
  noticeably more than half of the coordinates of any single row in S."*
- **Definition 3.1, the adversary quantifier (verbatim):** *"Algorithm M is (ε, δ, Prior, R)-Bayesian
  extraction-safe if for all attackers A it holds that"* the Narcissus inequality with `Nature ← Prior`
  in both experiments.
- **The scope disclaimer (verbatim):** *"We stress that our proposed definition is not a privacy
  definition. In particular, it does not prevent the attacker from learning potentially sensitive bits
  of information about the sample. The goal of our security definition is to protect against
  extraction"*.

## Connections

- Built directly on [Cohen et al.](cohen-data-reconstruction.md). Definition 2.1 of this paper
  reproduces Narcissus resiliency, and Definition 3.1 is its Bayesian extension. That paper carries the
  one-wayness equivalence and the poly-time attacker, this one the memorization framing and an
  unbounded attacker.
- Modern restatement of the memorization half of [Dinur–Nissim](dinur-nissim-revealing-information.md).
- **Occupies the framing of** [fibers-of-the-training-map](../../exp/docs/notes/fibers-of-the-training-map.md) §5,
  with the resource-bound seam noted below.
- Adjacent information-theoretic accounts of memorization as mutual information, and
  [Xiao–Devadas PAC Privacy](../analyses/native-asymmetry-in-learning.md), whose adversary is likewise
  not resource-bounded.
- The membership-inference definition it works against (Definition 1.2) is the Shokri et al. and Yeom
  et al. game. See [membership-inference-game](../concepts/membership-inference-game.md).
- Concepts: [computational-vs-statistical-memorization](../concepts/computational-vs-statistical-memorization.md),
  [data-reconstruction-attack](../concepts/data-reconstruction-attack.md).

## Limits

- The separation is real and proved, but it is a separation between mutual information and
  extractability, both measured against an unbounded attacker. It is not a separation between
  statistical and *polynomial-time* memorization, and no result in the paper distinguishes those.

## Open Questions / Limitations

- **The seam.** A genuinely time-bounded version of the same separation is not what is proved here.
  Nothing in the definitions or the proofs would change if the attacker were given unlimited compute,
  because it already has it.
- The secure mechanisms are the exact average and the noised average on the marginals problem, not
  natural training procedures, and the prior is chosen to match the existing impossibility literature
  rather than to model data.
- Security is shown for particular relations. The authors note that the exact average is not secure for
  the relation that asks the attacker to output the average of `S`, so the choice of `R` carries weight.
- Whether "statistical memorization" deserves the name at all is raised by the authors and left open.

## Quotes / Notable Passages

> "Is there a difference between computational memorization and statistical memorization? Could a
> model be considered "memorizing" under one definition but not the other?"

> "We stress that our proposed definition is not a privacy definition. In particular, it does not
> prevent the attacker from learning potentially sensitive bits of information about the sample."

> "Furthermore, even given H, no attacker (even unbounded) can guess noticeably more than half of the
> coordinates of any single row in S."
