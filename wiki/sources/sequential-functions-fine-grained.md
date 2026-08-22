---
title: "On Sequential Functions and Fine-Grained Cryptography"
type: source
date_ingested: 2026-08-20
authors: [Jiaxin Guan, Hart Montgomery]
venue: "CRYPTO 2024 (the PDF's own footnote reads \"The version published by Springer-Verlag will be available in the proceedings of CRYPTO 2024\")"
year: 2024
claim_quantifier: existential
antecedent: "For the main separation: existence of a PSPACE oracle. For the fine-grained SKE and MAC: an *ideal* continuous iterative sequential function whose Round function takes exactly the same time for honest parties and adversaries. For fine-grained PKE: a VDF with perfect soundness, unique proofs and proof indistinguishability, plus iO for null circuits."
tags: [cryptography, fine-grained-cryptography, one-way-functions, complexity-theory, verifiable-computation, hardness-reductions]
---

## Summary

Prices a **different resource** from the rest of this corpus: not total work but **depth**. A function
is `(t_C, t_A)`-sequential if an honest party can evaluate it in `k·t_C` in its machine model while no
adversary can do so in less than `k·t_A` in a model with *more parallel power*. The adversary is
otherwise PPT; its total work is unconstrained. This is the one compute axis cryptography has fully
formalized, and it is not the axis on which ML attack cost lives.

The main result is a **black-box oracle separation between sequential functions and one-way
functions**: relative to a PSPACE oracle there is an oracle `O` and a function `f^O` that is
sequential but not one-way. The authors flag this as surprising, since sequential functions are
normally built from assumptions that comfortably imply OWFs and since time-lock puzzles are known to
imply OWFs.

Two complexity results follow. The decisional, worst-case variant of a **continuous iterative
sequential function** (CISF — an ISF whose `Round` is independent of the round count `k`) is
**PSPACE-complete** (Theorem 2), while the more general **dynamic** sequential functions are **not in
PSPACE** relative to a random oracle (Theorem 3), proved via a parallel pebbling argument on the
Paul-Tarjan-Celoni graph.

The paper then asks what can be built from a sequential function that is *not* one-way: fine-grained
symmetric encryption and fine-grained MACs from a CISF, and fine-grained public-key encryption from a
VDF with extra properties plus iO for null circuits. It also defines a **commutative sequential
function** and shows it yields fine-grained key exchange — but supplies no construction of one.

## Claim Boundary

- **Quantified over:** PPT machine tuples `(A_0, A_1, A_2)` where `A_2`'s **running time in the
  parallel model `M_A`** is bounded, and `M_A` has more parallel computation power than the honest
  model `M_C`. The bounded quantity is therefore **depth / sequentiality**, not total work; `A_2`
  remains polynomial-time overall. The main separation is over **oracle** constructions with parallel
  oracle access (`q = poly(λ)` queries per round). The fine-grained SKE/MAC adversaries are ordinary
  PPT adversaries that must answer *before the next round starts* — the paper's own gloss: *"the
  adversary needs to output the bit guess b′ in a more fine-grained time bound (before the next round
  starts) than PPT."*
- **Antecedent:** Layered and, for the constructions, unusually strong. Theorems 4 and 5 assume an
  **ideal** CISF — one whose `Round` *"takes exactly the same time to evaluate for both the honest
  parties and the adversaries"* — which is an idealization of the primitive itself, not merely an
  assumption about hardness. The PKE result needs a VDF with perfect soundness, unique proofs and
  proof indistinguishability, *plus* iO for null circuits.
- **Does not establish:** That fine-grained key exchange follows from any constructible object. §10.4
  is explicit: *"We unfortunately were not able to develop a construction of a commutative sequential
  function that wasn't already a 'regular' key exchange protocol, and we leave this as an interesting
  open problem."* Nor does it establish that the fine-grained PKE construction avoids one-way
  functions in substance — the authors write only that they had to assume a great deal *"to build
  even fine-grained PKE that potentially did not imply one-way functions"* (emphasis on *potentially*).
- **Abstract vs theorem:** One to record. The abstract's *"We do not assume one-way functions"* is
  accurate as a statement about the assumption list, but the assumption list for the PKE result is
  VDF-with-extra-properties plus iO for null circuits, and the paper's own §10.4 hedges on whether
  those avoid OWFs. The abstract's *"show that it implies fine-grained key exchange"* is also
  accurate, but the antecedent primitive has no construction.

## Key Contributions

- **Theorem 1**: black-box oracle separation — a sequential function that is not a one-way function,
  assuming a PSPACE oracle. The paper's main result.
- **Theorem 2**: the Decisional CISF problem is **PSPACE-complete**.
- **Theorem 3**: the Decisional Dynamic Sequential Function problem is **not in PSPACE**, in the
  random oracle model — so the CISF/DSF boundary is a real complexity boundary.
- **Theorem 4 / Theorem 5**: `n`-time fine-grained SKE and fine-grained MAC from an ideal CISF.
- **Theorem 6**: PKE secure against a fine-grained time-bounded adversary, from VDF + iO for null circuits.
- **Definition 31**: commutative sequential functions, and the implied fine-grained NIKE (§10.3).

## Key Definitions / Theorems

**Definition 3 (Sequential Functions), the two conditions verbatim:**

> "1. There exists an algorithm in the computational model MC such that for all k and for all x that
> can be output by Gen, it computes Eval in at most time k · tC(λ). 2. For all λ ∈ N and for all
> tuples of PPT machines (A0, A1, A2), such that A2 runs in time strictly less than k · tA(λ) in the
> computational model MA ..."

- **Definition 8, `(T, ε)`-sequentiality for VDFs:** the parallel running time of `A_2` *"(with
  poly(T, λ) processors)"* is less than `(1 − ε)·T`. The processor count is polynomially unbounded;
  only depth is priced.
- **Definition 4**: an ISF has `Eval(pp,x,k) = Round(pp,·,k)^{(k)}(x)`; a CISF additionally has
  `Round` independent of `k`. The paper gives concrete examples of ISFs that are not CISFs
  (FHE bootstrapping every other round; alternating cube/fifth-power in a group of unknown order).
- **Theorem 1, verbatim:** *"Assuming the existence of a PSPACE oracle, then there exists an oracle O
  and a function f^O with oracle access to O such that f^O is a sequential function, but not a one-way
  function."*

## Connections

- **The axis contrast is the point.** Every other paper in this corpus prices **total work**: circuit
  size in [Brzuska-Couteau](fine-grained-one-way-functions.md), word-RAM time in
  [LaVigne-Lincoln-Vassilevska Williams](pkc-fine-grained-setting.md), oracle queries in
  [Afshar et al.](fine-grained-nike-lower-bounds.md), aggregate per-round power in
  [Ball et al.](permissionless-consensus-fine-grained.md), memory in
  [Wang et al.](nike-without-idealized-assumptions.md)'s BSM construction. This one prices **depth**,
  with total work left free. A cost model that measures an attack in FLOPs cannot be expressed here.
- **Circuit depth appears twice in this corpus under different names.**
  [Fine-Grained Cryptography](fine-grained-cryptography.md) bounds depth by *class* (`AC0`, `NC1`);
  this paper bounds it by a *number of rounds*. Both are the depth axis, formalized incompatibly.
- **Same separation genre.** [On Building Fine-Grained One-Way Functions](fine-grained-one-way-functions.md)
  also proves oracle separations against one-way functions; both are statements about proof
  techniques rather than about the world.
- Concepts: [Sequential Functions](../concepts/sequential-functions.md),
  [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md),
  [One-Way Functions](../concepts/one-way-functions.md),
  [Indistinguishability Obfuscation](../concepts/indistinguishability-obfuscation.md),
  [Verifiable Computation](../concepts/verifiable-computation.md).

## Open Questions / Limitations

- **No construction of a commutative sequential function.** The fine-grained key exchange has no
  instantiation, and the authors say VBB obfuscation would probably suffice but that they do not know
  how to translate it to iO.
- The assumptions underlying practical sequentiality are shaky in a way the paper documents:
  Bernstein-Sorenson parallelize repeated squaring to depth `O(T/lg lg T)` with `T^{1+o(1)}`
  processors, so the standard time-lock assumption *as usually stated* is false.
- Whether an equivalence between commutative sequential functions and fine-grained NIKE can be
  established — the authors say the notation makes this difficult and any construction is "seemingly
  very artificial".

## Quotes / Notable Passages

> "a supercomputing cluster may be able to perform sequential operations faster than a desktop
> computer, but its real advantage over the desktop lies in its parallel processing abilities."

> "We had to make quite a lot of strong assumptions to build even fine-grained PKE that potentially
> did not imply one-way functions, and it is not clear even what sort of primitives would imply
> fine-grained key exchange."
