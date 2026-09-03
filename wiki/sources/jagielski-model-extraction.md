---
title: High Accuracy and High Fidelity Extraction of Neural Networks
type: source
date_ingested: 2026-07-26
date_verified: 2026-08-20
authors: [Matthew Jagielski, Nicholas Carlini, David Berthelot, Alex Kurakin, Nicolas Papernot]
venue: "USENIX Security 2020"
venue_evidence: "arXiv:1909.01838 abstract page's own Comments field: 'USENIX Security 2020, 18 pages, 6 figures' — primary-source confirmation, correcting the earlier note that the PDF does not state a venue"
year: 2020
tags: [adversarial-ml, complexity theory, hardness-reductions, statistical-query, sample-complexity]
claim_quantifier: existential
antecedent: "Theorem 1 needs input-output (logit) access only — it fails under side-channel access, as the paper itself notes. Theorem 2 is stated for domain {0,1}^d. Theorem 3 is inherited from Das et al. (arXiv:1904.03866) and holds only for adversaries expressible as SQ algorithms over deep random networks."
cls_target: parameters
cls_family: extract
cls_phase: post hoc
cls_access: black box
cls_write: read only
cls_frame: compute
cls_party: attacker
cls_unit: algo class
cls_tightness: class
cls_baseline: stated
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "Random networks with domain {0, 1}d and range {0, 1} and depth h require exp(O(h)) samples to learn in the SQ learning model."
cls_evidence_src: "Theorem 3 (Informal, attributed to Das et al. [27]), Section 3.3 (\"Learning approaches struggle with fidelity\"), raw/JCB+20_ExtractionAccuracyFidelity.pdf"
cls_reason: "Hand-classified 2026-08-22 against codebook revision 2, then migrated through revisions 3 to 5. Carries no verbatim evidence quote, unlike the delegated rows."
cls_prov: P
cls_date: 2026-08-22
---

> **Provenance.** Verified against the primary PDF on 2026-08-20 (`raw/JCB+20_ExtractionAccuracyFidelity.pdf`,
> extracted with `pdftotext`). The earlier sweep-only banner is retired. Theorem statements, the
> subset-sum reduction, and the SQ lower bound below are quoted or paraphrased from text actually
> extracted. Two items in **Connections** are *not* from this PDF and are flagged inline.

## Summary

Systematizes model extraction around two adversarial objectives — **accuracy** (perform well on the
task distribution) and **fidelity** (agree with the victim on any input, errors included) — and shows
they conflict for an imperfect victim: a high-fidelity copy must reproduce the victim's mistakes,
which a high-accuracy copy must not. Above fidelity sits **functionally equivalent extraction**
(agreement on all of `X`), and above that the strawman of **exact extraction** (identical weights),
which the paper dismisses because ReLU networks belong to large behavioural equivalence classes
(neuron rescaling by `c`/`c⁻¹`, dead-neuron insertion, permutation). The best an input-output
adversary can do is identify the equivalence class.

The paper then gives one attack per objective: a query-efficient learning-based attack for accuracy
(scaled to a production classifier trained on a billion proprietary images), and the first practical
functionally-equivalent attack, recovering a two-layer network's weights from `O(dh)` input-output
queries at double precision — query-optimal up to a constant, since the model has `dh` parameters.

For this programme the important stratum is §3.3, "Model Extraction is Hard", which contains three
distinct hardness statements at three different levels — query complexity, decision complexity, and
**restricted-adversary-class** sample complexity. The third is the one the earlier sweep missed:
extraction inherits an **SQ lower bound**. Fidelity extraction of deep random networks by any
adversary expressible as a statistical-query algorithm — which includes SGD and PCA — requires
`exp(O(h))` samples in the depth `h`. That is an attacker priced in the units of a restricted
algorithm class, published in 2020, inside a security paper.

## Claim Boundary

- **Quantified over:** each hardness result is existential over a *constructed family*, not universal
  over networks. Theorem 1 exhibits a class of width-`3k`, depth-2 ReLU networks on `[0,1]^d`
  requiring `Θ(p^k)` queries; it does not say typical networks are hard to extract. Theorem 2 is
  worst-case NP-hardness of a decision problem over `{0,1}^d`, established by reduction from subset
  sum — it says nothing about average-case instances. Theorem 3 quantifies over adversaries
  (all SQ algorithms) and over deep *random* networks; it is not a statement about trained networks.
- **Antecedent:** Theorem 1 assumes the adversary sees only input-output behaviour. The paper says so
  explicitly and names the escape: Batina et al.'s differential-power-analysis attack performs
  functionally-equivalent extraction, because it breaks the assumption. Theorem 3's antecedent — that
  the attack is an SQ algorithm — is the hypothesis that makes it interesting *and* the hypothesis
  the paper's own functionally-equivalent attack violates.
- **Does not establish:** (a) that model extraction is hard — the same paper extracts a
  production-grade model and recovers a two-layer network's weights exactly; (b) that functional
  equivalence is hard to *achieve*, only that it is hard to *verify* given both weight vectors
  (Theorem 2 is a decision problem about a pair of networks, not about the extraction task); (c) any
  average-case or cryptographic hardness; (d) any statement about the **training** map — every
  theorem here concerns the evaluation map `w ↦ M_w`.
- **Abstract vs theorem:** the abstract's "inherent limitations that prevent any learning-based
  strategy from extracting a truly high-fidelity model" is stronger than what is proved. Theorem 3
  bounds *SQ* algorithms on *random* networks; "any learning-based strategy" is the informal gloss.
  The paper is careful about this in §3.3 ("most learning-based approaches ... will inherit this
  inefficiency"), but the abstract is not.

## Key Contributions

- The accuracy/fidelity taxonomy for extraction, with functionally-equivalent extraction as the
  fidelity limit and exact extraction as an acknowledged strawman.
- Three hardness statements at three levels: query complexity (Thm 1), decision complexity (Thm 2),
  and SQ sample complexity (Thm 3, imported).
- A learning-based accuracy attack reported as `16×` more query-efficient than prior work, applied to
  a model trained on one billion images.
- The first practical functionally-equivalent extraction attack from input-output access alone, at
  `O(dh)` queries, previously requiring power side-channels or gradient access.
- A hybrid method combining both.

## Key Definitions / Theorems

- **Exact extraction**: produce `Ô_θ = O_θ`. Declared "purely a strawman" — impossible for ReLU
  networks because of behavioural equivalence classes.
- **Functionally equivalent extraction**: `∀x ∈ X, Ô(x) = O(x)`. "the hardest possible goal using
  only input-output pairs."
- **Fidelity extraction**: given target distribution `D_F` and similarity `S`, maximize
  `Pr_{x∼D_F}[S(Ô(x), O(x))]`. This work uses label agreement only.
- **Task accuracy extraction**: maximize `Pr_{(x,y)∼D_A}[argmax Ô(x) = y]`. The easiest goal, since
  it need not match the victim's mistakes.
- **Definition A.1 — `k`-rectangle bounded function**: `f` on `[0,1]^d` with vectors `a, b` such that
  `f(x) ≠ 0 ⟹ a ⪯ x ⪯ b`, constrained in exactly `k` coordinates. Lemma 1 builds one from a
  3-ReLU gadget `T_i(x; a, b)` at width `3k`, depth 2; Lemma 2 constructs `p^k` disjoint such
  functions, of which a query rules out at most one.
- **Theorem 1**: there exists a class of width-`3k`, depth-2 networks on `[0,1]^d` with precision-`p`
  features, `d ≥ k`, that require `Θ(p^k)` logit queries to extract. (For 8-bit pixels, `p = 256`.)
- **Theorem 2**: "Checking whether two networks with domains `{0,1}^d` are functionally equivalent is
  NP-hard." Proved by reduction from **subset sum**: `f₁ ≡ 0`, and `f₂` is built with first-layer
  weights `v_i` so that `⟨x, v⟩` is the subset sum of `{i : x_i = 1}`, with the same 3-ReLU gadget
  forcing nonzero output iff the target `T` is hit. The paper notes a 3-SAT-based reduction for a
  different statement appears in its reference [58].
- **Theorem 3 (informal, imported)**: random networks with domain `{0,1}^d`, range `{0,1}` and depth
  `h` require `exp(O(h))` samples to learn in the SQ model. Attributed in the PDF to
  **A. Das, S. Gollapudi, R. Kumar, R. Panigrahy, "On the learnability of deep random networks",
  CoRR abs/1904.03866, 2019** (reference [27]). The paper's gloss: "most learning-based approaches to
  model extraction will inherit this inefficiency. A sample-efficient approach therefore must either
  make assumptions about the model to be extracted ... or must access its dataset without statistical
  queries."

## Connections

- **The contrast case for [Suliman et al. USENIX Sec'25](suliman-data-forging-attacks.md).**
  Evaluation map: hardness proved (Thm 1, Thm 2). Training map: conjectured, open. Keeping the two
  maps apart is the reason
  [fiber-of-the-training-map](../concepts/fiber-of-the-training-map.md) exists as a separate page.
- **Theorem 3 is a restricted-adversary-class security statement in the wild.** It prices the
  *attacker* in SQ units — the exact move the programme has been treating as unclaimed in the
  learning-adversary corner. Note the difference from
  [Bubeck–Price–Razenshteyn ICML'19](adversarial-examples-computational-constraints.md)-style separations
  already logged: there the *defender* fails; here the attacker is the SQ-bounded party. See
  [statistical-query-model](../concepts/statistical-query-model.md).
- **The success predicate.** [Beyond Labeling Oracles](beyond-labeling-oracles.md) says ME has no
  formal success definition. The accuracy/fidelity taxonomy here is the field's closest approach to
  one, and it is a taxonomy of *goals* with no cost or budget attached — which is exactly why
  Shafran et al. can still say no formal criterion exists five years later.
- Concept: [Model Extraction (Accuracy vs Fidelity)](../concepts/model-extraction.md).
- **Not from this PDF, recorded in an earlier sweep and not verified here:** the follow-on line
  Carlini–Jagielski–Mironov, *Cryptanalytic Extraction of Neural Network Models*, CRYPTO 2020
  (arXiv:2003.04884), made polynomial by Canales-Martínez, Chávez-Saab, Hambitzer,
  Rodríguez-Henríquez, Satpute and Shamir, EUROCRYPT 2024 (eprint 2023/1526). Neither appears in this
  PDF's reference list. If the pairing is used in writing, it must be checked against those papers
  directly. The cautionary reading stands on its own inside this paper, though: Theorem 2 is
  worst-case NP-hardness and §6 of the same paper gives an efficient practical inversion of the same
  map. **An NP-hardness result about the map did not prevent an efficient practical inversion.**
- **Not from this PDF:** Grigsby–Lindsey–Meyerhoff–Wu, arXiv:2209.04036 on "fibers of the realization
  map"; Sussmann 1992; Fefferman 1994; Phuong–Lampert ICLR 2020; Vlačić–Bölcskei *Adv. Math.* 376
  (2021). Carried over from the earlier sweep; not cited in this PDF.
- Cited **in** this PDF and verifiable from it: Tramèr–Zhang–Juels–Reiter–Ristenpart, USENIX Security
  2016 (the origin of ME); Batina–Bhasin–Jap–Picek (CSI NN, side-channel functionally-equivalent
  extraction); Milli–Schmidt–Dragan–Hardt (model reconstruction from explanations); Orekondy–Schiele–Fritz
  (Knockoff Nets).

## Open Questions / Limitations

- Theorem 2 is worst-case and did not obstruct efficient inversion of the same map — including by the
  authors themselves in §6. A worst-case hardness theorem is not a security guarantee. Any
  training-map hardness theorem must be stated so the same gap cannot open under it.
- Theorem 1's `Θ(p^k)` bound is over a constructed adversarial family. Nothing here says a naturally
  trained network is hard to extract.
- Theorem 3 is imported, informal in the body, and its scope (SQ adversaries, random networks) is
  narrower than the abstract's "any learning-based strategy". The formal statement lives in
  arXiv:1904.03866, which is **not** in this wiki and has not been read.
- The functionally-equivalent attack assumes a two-layer network and double-precision inference; the
  paper flags scaling it as open.

## Quotes / Notable Passages

> "Theorem 2. Checking whether two networks with domains {0,1}^d are functionally equivalent is NP-hard."

> "Any attack which can claim to perform functionally equivalent extraction efficiently (both in
> number of queries used and in running time) must make some assumptions to avoid these pathologies."

> "As a result, most learning-based approaches to model extraction will inherit this inefficiency. A
> sample-efficient approach therefore must either make assumptions about the model to be extracted
> (to distinguish it from a deep random network), or must access its dataset without statistical
> queries."

> "This definition is purely a strawman—it is the strongest possible attack, but it is fundamentally
> impossible for many classes of neural networks, including ReLU networks, because any individual
> model belongs to a large equivalence class of networks which are indistinguishable from
> input-output behavior."
