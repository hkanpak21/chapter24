---
title: Covert Learning — How to Learn with an Untrusted Intermediary
type: source
date_ingested: 2026-04-12
authors: [Ran Canetti, Ari Karchmer]
venue: "the PDF in `raw/` is dated 17 September 2021 and names no venue. The TCC attribution carried on this page is unconfirmed from the primary source."
year: 2021
tags: [cryptography, learning-theory, covert-computation, pseudorandomness, PAC-learning]
claim_quantifier: conditional
antecedent: "hardness of Learning Parity with Noise. The noisy-parity result needs low-noise LPN; every other construction needs sub-exponential hardness of standard LPN. No LWE assumption appears in the paper."
adversary_bound: "polynomial-time. In Covert Learning the untrusted intermediary is a passive eavesdropper on the query channel; in Covert Verifiable Learning it may also modify oracle responses."
model_class: "concepts given by a concept oracle over {0,1}^n; hypothesis classes of parities, bounded-degree Fourier characters, polynomial-size decision trees, s-DNF, s-juntas"
algorithm_class: "polynomial-time learners with membership-query access, plus random examples in the verifiable model"
date_verified: 2026-08-20
cls_target: training run
cls_family: none
cls_phase: train time
cls_access: hard label
cls_write: read only
cls_frame: compute
cls_party: attacker
cls_unit: time
cls_tightness: poly
cls_baseline: stated
cls_second: none
cls_assessed: explicit
cls_evidence: "every query and response obtained by the learner is also obtained by a computationally bounded adversary"
cls_evidence_src: §1.1.1
cls_reason: "Wiki page flagged unreliable per assignment (invented LWE/halfspace/theorem content); classified fresh from raw/CK21_CovertLearning.pdf. family=none per codebook convention for foundational cryptographic works, since the eavesdropping intermediary does not fit membership/reconstruct/extract/forge/evade/poison/backdoor. target=training run because the privacy goal covers the query-response transcript and the learner's hypothesis-class choice jointly (hypothesis-hiding), not a static dataset. access=hard label because the concept oracle returns y in {0,1} (Def 2.5); the intermediary receives this passively rather than querying itself, a nuance worth flagging. write=read only reflects the base Covert Learning model (Def 1.1/2.7, the abstract's first bullet); Covert Verifiable Learning (second bullet) additionally lets the intermediary modify oracle responses, which fits no write value cleanly."
cls_prov: P
cls_date: 2026-08-22
---

## Summary
Canetti and Karchmer consider learning a function by oracle queries where the queries and responses are monitored, and possibly modified, by an untrusted intermediary. They formalise two models. **Covert Learning** asks that the intermediary gain no information about either the concept or the learner's intentions — including which hypothesis class the learner has chosen. **Covert Verifiable Learning** additionally asks that an intermediary who tampers with responses cannot make the learner accept a bad hypothesis; the learner is given ground-truth random examples and may abort.

Privacy is **simulation-based**, not a comparison against a fixed benign transcript. The requirement is that there exist a polynomial-time simulator which, given access to additional random examples from the concept, generates a distribution of queries and responses computationally indistinguishable from the real interaction — with no further oracle access and no knowledge of the target hypothesis class.

Hypothesis-hiding is a deliberate part of the definition. In the agnostic setting the choice of hypothesis class encodes the learner's prior beliefs about the concept, so it is itself worth protecting.

Covert learning can only be interesting where learning from random examples is hard but learning with membership queries is feasible, and the authors note that for all known membership-query algorithms an observer can learn the function just by watching the queries.

**Correction, 2026-08-20.** This page previously described covertness as indistinguishability "from a fixed, benign reference distribution", which is not the definition; it also listed LWE among the assumptions, halfspaces among the classes learned, and a theorem of the form "covertly learnable but not SQ-learnable implies one-way functions". None of the three is in the paper. LWE does not occur in it; halfspaces occur only in bibliography entries; and there is no such win-win theorem. What the paper does show in that direction is that its covert learner for noisy parities, up to syntactic modification, is a key exchange protocol, which the KEM paradigm turns into public-key encryption.

## Claim Boundary

- **Quantified over:** specific hypothesis-class collections and concept classes, named in each theorem. Every positive result is a construction for one collection; none is a statement about learning in general. The one general statement is negative in flavour and informal: covert learning is only meaningful where random-example learning is hard and membership-query learning is feasible.
- **Antecedent:** hardness of Learning Parity with Noise. Theorem 1.3 needs **low-noise** LPN, where each bit of the secret is Bernoulli with mean `1/√n` and labels are flipped with probability `1/√n`. Theorems 1.4 through 1.8 need **sub-exponential** hardness of standard LPN, which is a stronger assumption than plain LPN. Theorem 1.9 needs no computational assumption. LWE is not used anywhere.
- **Which party is constrained:** the *untrusted intermediary*, to polynomial time — passive in the Covert Learning model, and able to modify oracle responses but not queries in the Covert Verifiable model. The paper explains the last restriction: an intermediary that could modify queries could arguably learn the function itself. The learner is also polynomial-time and needs membership-query access.
- **Does not establish:** covert learning for classes outside those named; anything about halfspaces; any characterisation of covert learnability by a complexity measure; or any lower bound of the form "covert learnability implies a cryptographic primitive". The one cryptographic construction runs the other way, from the noisy-parity learner to key exchange.
- **Abstract vs theorem:** none found. The abstract states the LPN assumption and names the two classes it covers.

## Key Contributions
- Two new learning models, Covert Learning and Covert Verifiable Learning, inspired by Ishai et al. (Crypto 2019) and Goldwasser et al. (ITCS 2021).
- Covert learners in the agnostic setting for parity functions and decision trees, under LPN, where a polynomial-time eavesdropper observing all queries and responses learns nothing about the function or the learned hypothesis.
- Covert verifiable learners giving the same learning and privacy guarantees against an intermediary that can modify all oracle responses, with the learner granted additional random examples and allowed to abort.
- The covert learner for noisy parities doubles as a key exchange protocol, and hence a public-key encryption scheme by the KEM paradigm — one sending nearly `√n` bits at once, where Alekhnovich's scheme encrypts a single bit.
- The first verifiable PAC learning protocol without any private examples (Theorem 1.8 / Theorem 3.10).
- A stated consequence for defences against **model extraction** attacks.

## Key Definitions / Theorems
- **Covert Learning (Definition 1.1, formal at Definition 2.7)**: *Completeness* — the algorithm outputs an ε-good hypothesis with probability `1 − δ`. *Privacy* — there is a probabilistic polynomial-time simulator that, given access to additional random examples from the concept, generates a distribution of queries and responses computationally indistinguishable from the real interaction, without further oracle access and without knowing the target hypothesis class.
- **Covert Verifiable Learning (Definition 1.2, formal at Definition 3.3)**: adds *soundness* — for any computationally bounded intermediary that tampers with responses, if the learner does not reject then its output fails to be ε-good with probability at most δ — and adapts privacy to a simulator that interacts with the intermediary. Three variants differ in when the learner's ground-truth random examples become known to the intermediary: never, after the interaction, or publicly in advance.
- **Theorem 1.3 (formal at Theorem 2.15)**: assuming hardness of **low-noise** LPN, there is a covert learning algorithm for the collection `C = {H_T | T ⊆ [n]}` with respect to the concept class `D_LPN` and loss `L_D`.
- **Theorem 1.4 (formal at Theorem 2.26)**: assuming **sub-exponential** hardness of standard LPN, there is a covert learning algorithm for learning the heavy low-degree Fourier coefficients of an arbitrary Boolean function, for `b ≤ O(log n)` and `τ ≥ 1/poly(n)`.
- **Theorem 1.5 (formal at Theorem 2.34)**: under the same assumption, a covert learning algorithm for polynomial-size decision trees, built on the Fourier result.
- **Theorems 1.6 and 1.7**: covert *verifiable* learning in the intermediate model, for the Fourier collection and for decision trees, under sub-exponential LPN.
- **Theorem 1.8 (formal at Theorem 3.10)**: public covert verifiable learning for the Fourier collection with respect to size-`s` DNF concepts, under sub-exponential LPN. The paper notes this gives the first verifiable PAC learning protocol without any private examples.
- **Theorem 1.9 (formal at Theorem 3.20)**: a covert verifiable learning algorithm with fully private examples for `s`-juntas with `s ≤ O(log n)`, achieving **statistical** soundness and **perfect** privacy — the one result in the paper that needs no computational assumption.
- **The necessary condition, stated informally in §1.1.2**: meaningful covert learning can exist only where learning from random examples is hard and learning with membership queries is feasible.

## Connections
- Uses [pseudorandomness](../concepts/pseudorandomness.md), [computational indistinguishability](../concepts/computational-indistinguishability.md).
- Source: [Active Learning and Model Extraction](active-learning-model-extraction.md) — the paper's stated application is that its results "uncover limitations of current techniques for defending against model extraction attacks", specifically query-monitoring defences deployed by machine-learning-as-a-service providers.
- Related to [statistical-query-model](../concepts/statistical-query-model.md) and [PAC-learning](../concepts/pac-learning.md).
- Win-win style reductions echo [win-win-theorem](../concepts/win-win-theorem.md) (Degwekar et al.).
- Authors: [Ran Canetti](../entities/ran-canetti.md), [Ari Karchmer](../entities/ari-karchmer.md).

## Open Questions / Limitations
- Covert learnability of broader classes is unresolved. The paper's positive results cover parities, low-degree heavy Fourier coefficients, polynomial-size decision trees, `s`-DNF and `s`-juntas. **Correction, 2026-08-20:** halfspaces were named here and in the summary; they appear in the paper only as bibliography entries.
- Whether covert learning relative to *adaptive* observers requires stronger primitives.
- Interaction with differential privacy: is covertness strictly stronger or incomparable?
- The intermediary is not permitted to modify the learner's queries, only the oracle's responses. The paper gives a reason rather than a proof: an intermediary able to modify queries "is arguably able to learn the function to begin with".

## Quotes / Notable Passages

> _Not verbatim. Checked against `raw/CK21_CovertLearning.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> The learner's interaction with the world should look, to any computationally bounded observer, like an interaction that could have been generated without any learning taking place.

Verified against `raw/CK21_CovertLearning.pdf` on 2026-08-20.

> "We consider the task of learning a function via oracle queries, where the queries and responses are monitored (and perhaps also modified) by an untrusted intermediary."

— abstract, the setting.

> "Privacy. There exists a p.p.t. simulation algorithm that, given access to additional random examples from the concept, generates a distribution of queries and responses which is computationally indistinguishable from that of the real interaction. The simulation algorithm should function without further access to the oracle, or knowledge of the target hypothesis class within the collection."

— Definition 1.1, the privacy condition, which is simulation-based rather than a comparison against a reference transcript.

> "As discussed, meaningful covert learning algorithms can exist only for learning problems where learning from random examples is hard, whereas learning with membership queries is feasible."

— §1.1.2, the necessary condition on where the model applies.
