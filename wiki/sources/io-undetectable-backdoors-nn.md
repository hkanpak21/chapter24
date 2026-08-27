---
title: "Injecting Undetectable Backdoors in Obfuscated Neural Networks and Language Models"
type: source
date_ingested: 2026-04-23
authors: [Alkis Kalavasis, Amin Karbasi, Argyris Oikonomou, Katerina Sotiraki, Grigoris Velegkas, Manolis Zampetakis]
venue: "arXiv:2406.05660v2 (7 Sep 2024). The NeurIPS 2024 attribution carried on this page is not stated anywhere in the PDF in `raw/` and is unconfirmed from the primary source."
year: 2024
tags: [backdoor, cryptography, indistinguishability-obfuscation, llm-security, undetectable-backdoors]
claim_quantifier: existential
antecedent: "one-way functions exist and computationally secure, efficient indistinguishability obfuscators for polynomial-size circuits exist (Assumption 2.7); for the language-model extension, additionally access to a steganographic function. iO is a standard but strong assumption."
adversary_bound: "PPT distinguisher with white-box access to the obfuscated model (architecture and weights)"
date_verified: 2026-08-20
cls_target: parameters
cls_family: backdoor
cls_phase: post hoc
cls_access: white box
cls_write: model
cls_frame: compute
cls_party: auditor
cls_unit: time
cls_tightness: poly
cls_baseline: stated
cls_baseline_checked: yes
cls_second_party: perturbation
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "for all probabilistic polynomial time (in 𝜆) algorithms 𝒜, the distinguishing advantage of 𝒜 on P and Q is negligible"
cls_evidence_src: Def 2.1, invoked by Def 2.3 (Backdoor Detection)
cls_reason: "party=auditor models the PPT distinguisher of Def 2.3 (Rule 6), acting post hoc on the released obfuscated model with no further training. The Backdoor/Activate construction is also PPT (Def 2.2) but this is a construction-efficiency requirement, not the security-defining bound, so it is not treated as a competing computationally-bounded party. second_party=perturbation records Activate's separate ||x-x1||_inf <= gamma bound (Def 2.2), a capability constraint distinct from either party's time bound. write=model since Backdoor(.) outputs a backdoored ANN; target=parameters since the backdoor is planted into the model's weights. Verified against the flagged claim: [GKVZ22] 'leave open the question of whether undetectability is possible for general models under white-box access' (§1, verbatim) — the paper moves, not closes, the white-box restriction (RFF -> honest obfuscated pipeline), matching the page's existing 2026-08-20 correction."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

If a neural network or language model is shipped as an **indistinguishability-obfuscated (iO)** circuit — an IP-protection pattern the paper motivates as plausible — an adversary can plant a backdoor whose existence is undetectable to a polynomial-time observer holding the complete obfuscated artifact. Detection reduces to breaking iO.

The paper's own comparison table (Table 1) locates the contribution precisely. GKVZ22 gives black-box undetectability with non-replicability for **arbitrary** training processes, and white-box undetectability **without** non-replicability for the Random Fourier Features process. This paper gives white-box undetectability **with** non-replicability for the class of training processes that end in an obfuscation step — what it calls the **honest obfuscated pipeline** (Assumption 1.2). The paper states directly that white-box undetectability for arbitrary training procedures is "unlikely", so the obfuscation step is an antecedent, not a convenience.

The construction extends to language models by way of steganography. It is complementary to [Draguns et al. 2024 unelicitable backdoors](unelicitable-backdoors-lms.md): where DGM+24 embeds cryptographic subcircuits directly, KKO+24 uses generic iO to hide the backdoor structure.

**Correction, 2026-08-20.** This page previously read that the paper "closes the GKVZ22 white-box gap" and that its result is "general" where GKVZ22 "required specific classifier structure". The paper does not claim to close the gap; it moves the restriction from one structural class (RFF) to another (pipelines that obfuscate before release). The itemisation "iO from LWE + LPN + NC⁰ PRGs + SXDH", previously attributed here to the paper, does not appear in it. The paper cites Jain–Lin–Sahai 2021 only as a candidate construction and states its own requirement as OWFs plus iO (Assumption 2.7).

## Claim Boundary

- **Quantified over:** every honest obfuscated pipeline, that is, an arbitrary training method **followed by an iO step**. The claim is existential in the backdoor: for each such pipeline there *exists* a (Backdoor, Activate) pair. It says nothing about a model released in the clear, and nothing about any specific deployed model.
- **Antecedent:** existence of one-way functions and of computationally secure, efficient indistinguishability obfuscators for polynomial-size circuits (Assumption 2.7). The language-model theorem (Theorem 4.9) additionally assumes access to a steganographic function. iO is a well-studied assumption with candidate constructions, but it is strictly stronger than OWFs.
- **Which party is constrained:** the *defender/distinguisher*, which must run in polynomial time even though it holds the full weights. The attacker is also polynomial time. The activation perturbation is bounded in ‖·‖∞ and is a geometric, not computational, constraint.
- **Does not establish:** that backdoors are undetectable in models released as ordinary weights; that iO-wrapped deployment is current practice; or that detection is impossible information-theoretically. Undetectability here is computational only.
- **Abstract vs theorem:** the abstract says "even if the weights and architecture of the obfuscated model are accessible, the existence of the backdoor is still undetectable", which is accurate but reads as broader than it is unless "of the obfuscated model" is given its full weight. The restriction to obfuscated pipelines is stated in the body as Assumption 1.2.

## Key Contributions

- **Obfuscation for neural networks is well defined (Theorem 1.1)**: if iO exists for Boolean circuits, then an obfuscation procedure exists for artificial neural networks. This rests on transformations between Boolean circuits and ANNs (Theorems 3.6 and 3.7).
- **White-box undetectable *and* non-replicable backdoors under iO (Theorem 1.5 / Theorem 4.2)**: for every honest obfuscated pipeline, backdoor existence is indistinguishable from a clean network even with complete weight access.
- **Reduction to iO hardness**: detecting the backdoor implies distinguishing obfuscations.
- **Extension to language models (Theorem 4.9)**: an undetectable backdoor attack for LMs, under the additional assumption of access to a steganographic function.
- **Moves, rather than removes, the structural restriction**: GKVZ22 covers arbitrary training black-box, and RFF white-box; this paper covers arbitrary training followed by obfuscation, white-box, with non-replicability. **Correction, 2026-08-20:** this bullet previously read "Closes the GKVZ22 white-box gap ... KKO+24 is general", which the paper does not claim.
- **Compatibility with common IP-protection patterns**: the paper motivates obfuscated release as a plausible deployment pattern, while noting its own constructions are "purely theoretical".

## Key Definitions / Theorems

- **Honest obfuscated pipeline (Assumption 1.2)**: train `h = sgn(f)` with an arbitrary Train; obfuscate `f` to get `f̃`; release `h̃ = sgn(f̃)`. The main theorem is stated relative to this pipeline.
- **Undetectability (Definition 1.3, after GKVZ22)**: no efficient distinguisher separates `h` from `h̃`, for any data distribution. *White-box* gives the distinguisher the complete explicit description of both models; *black-box* gives only query access. The paper calls white-box "a much more challenging task" and its main goal.
- **Non-replicability (Definition 1.4, after GKVZ22)**: no polynomial-time algorithm, given feature vectors and their backdoored versions, generates a new backdoored pair.
- **Main theorem (Theorem 1.5, informal; formal at Theorem 4.2)**: assuming one-way functions and indistinguishability obfuscation exist, for every honest obfuscated pipeline there is a backdoor attack for ANNs that is both white-box undetectable and non-replicable.
- **Language-model theorem (Theorem 4.9)**: the same under the additional steganographic-function assumption.

## Connections

- Source: [Planting Undetectable Backdoors (GKVZ22)](planting-undetectable-backdoors.md) — direct predecessor; KKO+24 closes the white-box case.
- Source: [Unelicitable Backdoors in LMs (DGM+24)](unelicitable-backdoors-lms.md) — sister NeurIPS 2024 result using cryptographic circuits directly; both establish LLM-scale backdoor impossibility.
- Source: [Backdoor Defense, Learnability and Obfuscation (CHLX25)](backdoor-defense-learnability-obfuscation.md) — defendability framework; KKO+24 provides the non-defendability instantiation for obfuscated models.
- Source: [Oblivious Defense (GSVV25)](oblivious-defense-backdoor-removal.md) — complementary mitigation direction.
- Concept: [Indistinguishability Obfuscation](../concepts/indistinguishability-obfuscation.md) — central cryptographic primitive.
- Concept: [Undetectable Backdoors](../concepts/undetectable-backdoors.md) — KKO+24 extends to white-box.
- Concept: [Learning With Errors](../concepts/learning-with-errors.md) — iO is built from LWE + LPN + ...

## Open Questions / Limitations

- **iO efficiency**: current practical iO schemes have large overhead; deployed iO-wrapped models are not yet practical.
- **Compositionality**: can iO-backdoors be composed with GSVV25-style structural mitigation? Open.
- **Statistical (not computational) undetectability**: undetectability here is computational only. **Attribution unverified, 2026-08-20:** this line previously named "a forthcoming result by Vafa-Bogdanov-Rosen". The corresponding paper in `raw/` (`20344_Statistically_Undetectab.pdf`, "Statistically Undetectable Backdoors in Deep Neural Networks") is under double-blind review and its authors are withheld, so the attribution cannot be checked here and should not be carried into writing. Its own claim is that backdoored and honestly trained models are close in total variation distance given full model descriptions.
- **Post-quantum iO**: the paper does not analyse post-quantum security. **Correction, 2026-08-20:** the previous claim that "current iO uses bilinear groups (SXDH) which is not post-quantum" is not stated in this paper; it concerns the cited Jain–Lin–Sahai construction and belongs on a page about that work.
- **Weaker primitives**: the authors ask whether cryptographic schemes weaker than iO suffice for white-box undetectability.
- **Heuristic obfuscation**: the constructions are described by the authors as purely theoretical; instantiating them with heuristic obfuscation is left open.

## Quotes / Notable Passages

> _Not a quotation from the paper. This characterization was carried over from a secondary survey artifact during an earlier ingest and was wrongly presented in quotation marks. Retained unquoted, corrected 2026-08-20; verify against the primary source before citing._
>
> If the deployed model is shipped as an indistinguishability-obfuscated neural network — a plausible IP-protection pattern — an adversary can plant backdoors whose existence is undetectable even to observers with complete white-box access to the obfuscated artifact.

Verified against `raw/KKO+24_iOBackdoorsNN.pdf` on 2026-08-20.

> "Our method to plant backdoors ensures that even if the weights and architecture of the obfuscated model are accessible, the existence of the backdoor is still undetectable."

— abstract, on the access model.

> "As observed in Table 1, we know that black-box undetectable and non-replicable backdoors can be injected to arbitrary training procedures [GKVZ22]. However, this is unlikely for white-box undetectable ones. Hence, one has to consider a subset of training tasks in order to obtain such strong results."

— §1.1, the authors' own statement of why the obfuscation step is needed.
