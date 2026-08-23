---
title: "Undetectable Watermarks for Language Models"
type: source
date_ingested: 2026-08-22
authors: [Miranda Christ, Sam Gunn, Or Zamir]
venue: "venue unconfirmed from PDF (the file carries the stamp \"arXiv:2306.09194v1 [cs.CR]\" and the dateline \"June 16, 2023\"; no venue line appears)"
year: 2023
tags: [cryptography, computational-indistinguishability, pseudorandomness, one-way-functions, undetectable-backdoors]
claim_quantifier: existential
antecedent: "A pseudorandom function family, which the paper states is equivalent to one-way functions. The warm-up construction of Section 3 additionally assumes a random oracle and initially a min-entropy bound; both are removed before Section 4. The removal attack (Theorem 11) additionally assumes the model is prefix-specifiable."
adversary_bound: "Polynomial-time distinguishers with **adaptive oracle access to two oracles**: `Model` itself, and either `Model` or `Wat_sk` (Definition 9). Uniform p.p.t. as written; the PRF definition quantifies over \"all p.p.t. distinguishers D\". Undetectability is computational by necessity — Lemma 4 shows any sound scheme is statistically distinguishable with poly(K/ε) queries and exp(K) time, K the key length."
date_verified: 2026-08-22
cls_target: outputs
cls_family: evade audit
cls_phase: test time
cls_access: black box
cls_write: responses
cls_frame: compute
cls_party: attacker
cls_unit: queries
cls_tightness: exponent
cls_baseline: stated
cls_second_party: none
cls_second_notion: time
cls_assessed: explicit
cls_evidence: "there exists an efficient algorithm A making queries to Watsk … The number of queries made by A to Watsk is exactly the length of text output by A"
cls_evidence_src: Thm 11, §6
cls_reason: "classified on Thm 11's removal attack, not Def 9's undetectability construction, since the paper's own Summary flags §5–§6 as what matters for adversary capability and family/access/write need an explicit adversary. family=evade audit since the attack's goal is making Wat_sk's output indistinguishable from Model's so Detect_sk will not flag it (the wiki's Connections note also calls this attacker 'a query-bounded extraction adversary in all but name', an alternative reading worth a second look). tightness=exponent from the paper's own stated ~2000x-honest-cost pricing ($960.36 vs $0.48 for an 8000-token response, §6). second_notion=time from 'efficient algorithm A' (poly-time) alongside the query count."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The paper that puts watermarking a language model on a cryptographic footing. Earlier schemes embed a
watermark by perceptibly tilting the output distribution, so a user can in principle notice — and
measure — the degradation. This paper asks whether the tilt can be hidden behind a secret key, and
answers yes under one-way functions.

The definition is the contribution. A watermarking scheme is a triple `(Setup, Wat, Detect)`.
**Soundness** says text generated independently of the key is flagged with only negligible
probability. **Completeness**, in the form the paper argues is the only achievable one, says that any
output of `Wat_sk` whose *empirical entropy* under the original model exceeds a threshold `b(|x|)` is
flagged, except with negligible probability; **substring-completeness** demands the same of every
sufficiently high-entropy contiguous substring. **Undetectability** (Definition 9) is a computational
indistinguishability statement: no polynomial-time distinguisher, given adaptive query access to the
original model and to either the original model or the watermarked one, can tell which it is holding.
Only the key is hidden from it. The construction achieves all three simultaneously with
`b(L) = O(λ√L)`.

The mechanism is a pseudorandom function keyed by a hash of the recent output, used to derive the
sampling randomness once enough empirical entropy has accumulated in the context. Because the PRF's
output is pseudorandom, the sampled tokens are distributed as the model would have sampled them, up
to computational indistinguishability; because the PRF is keyed, the holder of `sk` can recompute the
correlation and detect it. A warm-up in Section 3 makes the idea visible with a random oracle and an
expected-polynomial-time watermarker; Section 4 removes both.

Section 5 draws the boundary in two directions and it is the part that matters for a survey of
adversary capability. Undetectability is *necessarily* computational: for any sound scheme, an
unbounded distinguisher recovers the difference with a polynomial number of queries and `exp(K)` time
where `K` is the key length. And undetectability *forbids* watermarking low-entropy outputs: any
scheme that watermarks outputs of empirical entropy at most `t` with non-negligible probability is
detectable in `exp(t) · poly(λ)` queries and time. So the completeness threshold `b(L)` is not an
artefact of the construction.

Section 6 supplies the matching negative result on the other axis. Undetectability and unremovability
are in tension: any undetectable scheme can be stripped by an efficient attacker who feeds each
generated prefix back as a new prompt, provided the model is *prefix-specifiable*. The cost is one
query per output token, which the paper prices out at roughly two thousand times the honest
generation cost for an eight-thousand-token response at then-current GPT-4 rates. Expensive, not
impossible — and the authors draw the right conclusion, that no fully general notion of
unremovability is available.

## Claim Boundary

- **Quantified over:** every language model `Model` over a token set `T` — the construction is
  universal in the model, and existential in the scheme. Undetectability quantifies over all
  polynomial-time distinguishers with adaptive access to both oracles; soundness quantifies over all
  token sequences of length at most `poly(λ)`; completeness quantifies over all prompts of length at
  most `poly(λ)` and holds only where the empirical entropy clears `b(|x|)`.
- **Antecedent:** a **pseudorandom function family**. The paper states the reduction: *"PRFs are a
  standard cryptographic primitive equivalent to one-way functions and can be constructed from
  standard assumptions"*. This is the weakest standard assumption in cryptography, and the only one
  the main construction needs. The Section 3 warm-up additionally uses a random oracle and, in its
  first version, a min-entropy assumption; Sections 3.2 and 3.3 remove them. Theorem 11 additionally
  requires the model to be prefix-specifiable, which the paper argues is close to free in practice
  since a prompt can simply ask for a given prefix.
- **Adversary class and machine model:** polynomial-time, **oracle-aided**, adaptive. Definition 9 is
  a two-oracle indistinguishability game, and *"the notation D O1 ,O2 means that D is allowed to
  adaptively query both O1 and O2 with arbitrary prompts."* This is a standard-model computational
  bound, not a query bound in an idealized model — the query access is to the model, not to an
  idealized primitive. It is uniform p.p.t. as written; the paper does not discuss non-uniform
  distinguishers.
- **Does not establish:** unremovability, robustness to editing, or any guarantee against an adversary
  who paraphrases or perturbs the text. Section 6 proves the opposite for the general case. It does
  not establish detection of *any* AI-generated text — only of text produced by `Wat_sk`, and only
  above the entropy threshold. It does not establish that watermarking is *undetectable* once the key
  is published; publishing `sk` destroys undetectability by construction, and the paper says so,
  keeping only the no-quality-degradation property.
- **Abstract vs theorem:** the abstract's claim that *"it is impossible for a user to observe any
  degradation in the quality of the text"* is a consequence of Definition 9 and is correct as a
  statement about computationally bounded users measuring quality by an efficiently computable
  criterion. Read without that qualification it overstates — Lemma 4 shows an unbounded user *can*
  observe a difference. The body states the qualification: *"in any undetectable watermarking scheme,
  the quality of outputs must be identical between Model and Wat_sk"* is derived from the definition,
  which is itself computational.

## Key Contributions

- **Definition 9**, cryptographic undetectability of a watermark against an adaptively querying
  polynomial-time distinguisher.
- Empirical entropy as the right completeness condition, with Section 5 showing that the usual
  model-level entropy is insufficient (Lemma 3).
- A scheme that is undetectable, sound, and `O(λ√L)`-complete from one-way functions alone
  (Theorem 1), and a variant achieving `O(λ√L)`-substring-completeness (Theorem 2).
- Two impossibility results marking the boundary of undetectability: it must be computational
  (Lemma 4), and it must exclude low-empirical-entropy outputs (Theorem 10).
- A generic removal attack against every undetectable scheme for a prefix-specifiable model
  (Theorem 11), with the number of queries equal to the number of output tokens.

## Key Definitions / Theorems

**Definition 5 (watermarking scheme).** `Setup(1^λ) → sk`; `Wat_sk(prompt)` a randomized generator;
`Detect_sk(x) → {true, false}`.

**Definition 6 (soundness).** For every `λ` and every `x` with `|x| ≤ poly(λ)`,
`Pr_{sk←Setup(1^λ)}[Detect_sk(x) = true] ≤ negl(λ)`.

**Definition 7 (`b(L)`-completeness).** For every `λ` and prompt of length `≤ poly(λ)`,
`Pr[Detect_sk(x) = false and H_e(Model, prompt, x) ≥ b(|x|)] ≤ negl(λ)` over
`sk ← Setup(1^λ)`, `x ← Wat_sk(prompt)`.

**Definition 8 (`b(L)`-substring-completeness).** The same, quantified over every contiguous
substring `x[i : i+L]` with empirical entropy at least `b(L)`.

**Definition 9 (undetectability) — the definition this page exists for. Verbatim:**

> "A watermarking scheme W = (Setup, Wat, Detect) is undetectable if for every security parameter λ
> and all polynomial-time distinguishers D,"

with the displayed inequality
`|Pr[D^{Model,Model}(1^λ) → 1] − Pr_{sk←Setup(1^λ)}[D^{Model,Wat_sk}(1^λ) → 1]| ≤ negl(λ)`, and,
verbatim:

> "where the notation D O1 ,O2 means that D is allowed to adaptively query both O1 and O2 with
> arbitrary prompts."

> **Transcription note.** `pdftotext` drops the absolute-value bars and the second `Pr` from the
> displayed formula and renders the superscripted oracle list as `D O1 ,O2`. The restored inequality
> is given outside the quotation marks; the quoted lines are the extraction verbatim.

**So: undetectable against whom.** Against a **uniform polynomial-time** distinguisher that (i) may
adaptively choose arbitrary prompts, (ii) has oracle access to the *unwatermarked* model as a
reference throughout, and (iii) does not hold `sk`. Nothing weaker would be meaningful — a
distinguisher without reference access to `Model` could not calibrate — and nothing stronger is
achievable, by Lemma 4.

**Theorem 1.** *"For any model Model we construct a watermarking scheme W that is undetectable,
sound, and O(λ L)-complete"* — the extraction has dropped the square root; the completeness parameter
is `O(λ√L)`.

**Theorem 2.** The same with `O(λ√L)`-substring-completeness.

**Lemma 4 (undetectability is necessarily computational).** For a sound scheme with key length at
most `K` bits and a prompt on which watermarked outputs are detected with probability at least
`ε > 1/poly(λ)`, one can distinguish `Model` from `Wat_sk` with probability at least `ε/2` using
`poly(K/ε)` queries and `exp(K)` running time. The section summary, verbatim:

> "Undetectability is possible only against a computationally bounded adversary."

**Theorem 10 (low entropy cannot be watermarked).** If a sound scheme detects watermarked outputs of
empirical entropy at most `t` with probability greater than `1/poly(λ)`, then `Model` and `Wat_sk` are
distinguishable with `O(exp(t) · poly(λ))` queries and time. The section summary, verbatim:

> "Undetectability is impossible if outputs of low empirical entropy are watermarked"

**Theorem 11 (every undetectable watermark is removable), verbatim opening:**

> "Let W = (Setup, Watsk , Detectsk ) be any undetectable watermarking scheme. Assume that the
> underlying model Model is prefix-specifiable."

The conclusion: there is an efficient `A` making queries to `Wat_sk` such that `A^{Wat_sk}(prompt)`
and `Model(prompt)` are `negl(λ)`-close in statistical distance, with the number of queries equal to
the length of the text `A` outputs.

**Why a key is required at all**, verbatim: *"the existence of a secret key is necessary, as
otherwise Properties (1) and (2) would directly contradict each other."*

## Connections

- Concept: [computational indistinguishability](../concepts/computational-indistinguishability.md) —
  Definition 9 is an instance, with the unusual feature that the distinguisher holds a reference
  oracle for the honest object.
- Concept: [pseudorandomness](../concepts/pseudorandomness.md) and
  [one-way functions](../concepts/one-way-functions.md) — the assumption, at its weakest.
- Concept: [undetectable backdoors](../concepts/undetectable-backdoors.md) — the same word,
  a different object. There the hidden modification changes the function's behaviour on a trigger;
  here it changes only the sampling randomness, and the *whole point* is that behaviour is preserved.
- [Planting Undetectable Backdoors in Machine Learning Models](planting-undetectable-backdoors.md) —
  the closest structural neighbour: an undetectability notion for a planted modification, also
  cryptographic, also computational.
- [Undetectable backdoors from indistinguishability obfuscation](io-undetectable-backdoors-nn.md) and
  [Unelicitable backdoors in language models](unelicitable-backdoors-lms.md).
- [Cryptographic backdoors, boon and bane](crypto-backdoor-boon-bane.md).
- [Proof-of-Learning](proof-of-learning.md) and [PoLO](polo-proof-of-learning-ownership.md) — the
  other route to attributing a model output to a training run.
- [Model extraction](../concepts/model-extraction.md) — Theorem 11's attacker is a query-bounded
  extraction adversary in all but name, priced at one query per output token.

## Limits

- **Theorem 11 is a limit on the definition itself, not a neighbouring result.** Undetectability as
  defined here is incompatible with unremovability in general: every scheme meeting Definition 9 is
  stripped by an efficient prefix-feeding attacker whenever the model is prefix-specifiable. The
  authors state the consequence: no sweeping notion of unremovability is achievable, and any such
  notion must exclude adversaries strong enough to run this attack.
- Lemma 3 limits the natural entropy-based reading of completeness: there are models with arbitrarily
  high entropy in which any undetectable, sound scheme watermarks only a vanishing fraction of
  outputs.

## Open Questions / Limitations

- The completeness parameter `O(λ√L)` is acknowledged as suboptimal; closing the gap to the
  `Θ(λ)`-completeness of the inefficient warm-up scheme is posed as an open problem.
- The warm-up scheme of Section 3 has `1/poly(λ)` false positives and an unbounded worst-case running
  time for `Wat_sk`; only the Section 4 construction is efficient and negligibly sound.
- The removal attack's cost is quantified only by a then-current price quotation, not by an
  asymptotic separation, so nothing here says an undetectable watermark is *practically* removable at
  scale.
- Nothing addresses multiple keys, key rotation, or an adversary who holds `Detect_sk` outputs.

## Quotes / Notable Passages

> "PRFs are a standard cryptographic primitive equivalent to one-way functions and can be constructed from standard assumptions"

> "the existence of a secret key is necessary, as otherwise Properties (1) and (2) would directly contradict each other."

> "Undetectability is possible only against a computationally bounded adversary."

> "Undetectability is impossible if outputs of low empirical entropy are watermarked"
