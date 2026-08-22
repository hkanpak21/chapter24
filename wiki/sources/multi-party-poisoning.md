---
title: Universal Multi-Party Poisoning Attacks
type: source
date_ingested: 2026-04-12
authors: [Saeed Mahloujifar, Mohammad Mahmoody, Ameer Mohammed]
venue: "ICML 2019 (stated in PDF: \"a full version of a paper that was previously published in the Proceedings of the 36th International Conference on Machine Learning, Long Beach, California, PMLR 97, 2019\")"
year: 2019
tags: [poisoning-attacks, adversarial-ml, cryptography, complexity-theory, byzantine]
claim_quantifier: universal
antecedent: "The adversary is given sampling-oracle access to each party's data distribution and black-box access to the protocol, and the protocol must admit efficient conditional sampling. The corruption is static — the k parties are fixed in advance — and each corrupted message is drawn from a distribution within total-variation distance p of the honest one."
date_verified: 2026-08-20
---

## Summary

This paper (MMM19) introduces the **(k, p)-poisoning model** for multi-party collaborative learning and coin-tossing protocols, and proves a tight universal amplification bound. The model: in an m-party protocol, a Byzantine adversary statically corrupts k out of m parties, and for each corrupted party, for each message that party would send, the adversary samples from any distribution that is p-close (in total variation) to the honest distribution. This interpolates between two previously-studied settings — p-tampering (k = m) and standard static k-corruption in secure multi-party computation (p = 1) — and unifies them.

The main theorem shows that in any m-party protocol, a polynomial-time (k, p)-adversary can increase the probability of any "bad" property B from initial probability μ to **μ^{1 − pk/m}** — a multiplicative amplification that for small μ approximates μ + Ω(pk/m·log(1/μ)). The attack is *online* (no knowledge of future messages), uses *correctly-labeled* examples in the ML setting, and requires only black-box access to the protocol/learner plus sampling access to each party's data distribution.

The technical engine is **generalized p-tampering**: a tampering model on arbitrary discrete random processes x = (x₁, ..., xₙ) where a set S ⊆ [n] of tamperable coordinates is drawn from a distribution with marginal Pr[i ∈ S] = p but possibly correlated. Prior p-tampering proofs [MM17, MDM18] required *independent* tampering — a requirement that broke when k parties are corrupted because correlated messages cause correlated tamperable indices. The paper imports techniques from cryptographic coin-tossing attacks [BOL89, HO14] to handle the correlated case.

The result is "universal" in two senses: (1) it works against *any* efficient protocol regardless of defense mechanism (within the (k, p) trust model), including federated learning with differential privacy or secure aggregation (attacker only needs the public effect of updates on the shared model); and (2) it simultaneously covers secure multi-party coin-tossing and federated / collaborative machine learning under a common framework.

## Claim Boundary

- **Quantified over:** all m-party protocols with arbitrary interaction pattern, and all bad properties B of the trained hypothesis with non-negligible probability under no attack. This is the strong direction of universality — over tasks, learners and defences within the trust model — and it is what "universal" in the title means.
- **Antecedent:** the oracle access named above. The attack needs to sample from each party's data distribution and to run the protocol; without those it is not claimed. The paper argues this is the right cryptographic-style capability, by analogy with chosen-plaintext oracles, which is a defensible convention rather than a proved necessity.
- **Which party is constrained:** the **adversary**, in three resources at once — polynomial running time, a static corruption budget of k out of m parties, and a per-message total-variation budget p. This is the most fully priced adversary in the geometric-inevitability and robust-PAC cluster, and the amplification exponent 1 − pk/m is written directly in those budget parameters. The learner is not constrained at all.
- **Does not establish:** (i) that no defence helps, only that none inside the (k, p) trust model beats the universal bound; the page's own limitations note that task-specific attacks in the federated-learning literature exceed it and that whether robust aggregation can beat it is open; (ii) any bound against adaptive corruption, where the adversary picks parties from the transcript prefix; (iii) that the attack is undetectable, only that it uses correctly-labelled data, which defeats mislabel filtering specifically.
- **Abstract vs theorem:** none found. The abstract states the corruption model, the closeness parameter and the online, clean-label properties of the attack.

## Key Contributions

- **(k, p) model**: Unified corruption model for multi-party protocols; distribution-TV-distance relaxation of static Byzantine corruption.
- **Main theorem (Thm 1.1 / Thm 2.5)**: Poly-time (k, p)-adversary increases any bad-property probability from μ to μ^{1 − pk/m} in any m-party protocol, universal across tasks, algorithms, and hypothesis classes.
- **Interpolation**: Recovers p-tampering bounds [MM17] for k = m (μ → μ^{1−p}) and subsumes static k-corruption for p = 1.
- **Generalized p-tampering (Thm 1.2 / Thm 3.5)**: Biasing attacks on arbitrary random processes with correlated tamperable-index distributions; the technical innovation enabling the (k, p) result.
- **Federated learning corollary**: Attacks apply against DP-SGD / secure aggregation because only the public effect of updates on the central model is needed.
- **Coin-tossing corollary**: In single-round m-party coin tossing, (k, p)-adversary biases output bit from μ to μ^{1−pk/m}.
- **Online + correct-label**: Attack operates online and uses only valid (correctly-labeled) data, limiting defensive options — filtering mislabels does not help.

## Key Definitions / Theorems

- **(k, p)-poisoning adversary**: Statically chooses k of m parties; for each corrupted party's messages, may sample from any distribution that is p-close in total variation to the honest distribution.
- **Tamperable-index distribution S**: distribution over [n] with Pr[i ∈ S] = p for all i; models which coordinates the attacker can override. In (k, p)-poisoning, S is constructed by picking k random parties and, within their messages, marking each with independent probability p.
- **Theorem 1.1 (main, informal)**: For any m-party learning protocol Π and any bad property B with Pr_no-attack[B] ≥ μ, there is a poly-time (k, p)-attacker with oracle access to party distributions achieving Pr_attack[B] ≥ μ^{1 − pk/m}.
- **Theorem 1.2 (engine, informal)**: For any discrete random process x with efficient conditional sampling and any bounded f : Supp(x) → [0, 1], for any S with Pr[i ∈ S] = p there is a poly-time generalized-p-tampering attack raising E[f(x)] from μ to arbitrarily close to μ − p·E[f(x)^{1+p}]. For Boolean f, the bound becomes μ^{1−p}.
- **Proof engine**: Correlation-robust version of the tampering-biasing attack, borrowing from cryptographic coin-tossing [BOL89, HO14].

## Connections

- Generalizes the [p-Tampering Model](../concepts/p-tampering-model.md) (case k = m)
- Companion to [Curse of Concentration (MDM19)](curse-of-concentration.md) poisoning bounds (which handle the stronger offline / choose-locations model on single-party training)
- Synthesized in [A Complexity Theoretic Approach to Adversarial ML](complexity-theoretic-adversarial-ml.md)
- Related: [Poisoning Attacks](../concepts/poisoning-attacks.md), [Evasion Attacks](../concepts/evasion-attacks.md)
- Foundational for formal federated-learning security analyses

**Authors**: [Saeed Mahloujifar](../entities/saeed-mahloujifar.md), [Mohammad Mahmoody](../entities/mohammad-mahmoody.md), [Ameer Mohammed](../entities/ameer-mohammed.md).

## Open Questions / Limitations

- Attacker needs sampling-oracle access to each party's data distribution — a strong capability, though the paper argues this is the correct cryptographic-style security definition (analogous to CPA oracles in encryption security).
- The bound μ^{1 − pk/m} is tight for *universal* attacks; tighter task-specific attacks may exist for particular learners/defenses (and some in the federated-learning literature do surpass it).
- No cryptographic trusted setup or robust aggregation technique is shown to generically beat the bound; open whether such defenses can help within the (k, p) model.
- Extension to adaptive corruption (adversary chooses which k parties to corrupt based on transcript prefix) is suggested but not fully treated.

## Quotes / Notable Passages

> "We prove that for any “bad” property B of the final trained hypothesis h (e.g., h failing on a particular test example or having “large” risk) that has an arbitrarily small constant probability of happening without the attack, there always is a (k, p)-poisoning attack that increases the probability of B from µ to by µ^{1−p·k/m} = µ + Ω(p · k/m)."
>
> _Corrected 2026-08-20 against `raw/MMM19_MultiPartyPoisoning.pdf`. The example clause is restored, and the words "to by" are reproduced as printed; the earlier version of this page silently repaired what appears to be a typo in the source._

> "By corrupting half of the parties (i.e., p = 1, k = m/2) the adversary can increase the probability of any bad event B from 1/100 to 1/10."

> _Not verbatim. Checked against `raw/MMM19_MultiPartyPoisoning.pdf` on 2026-08-20 and not found; an earlier ingest dropped a citation, a parenthetical gloss, and a comma without marking the elisions. Retained unquoted as a summary._
>
> The proof of p-tampering attacks of [MM17, MDM18] crucially rely on the assumption that each message is tamperable with independent probability p, while corrupting k random parties leads to tamperable messages in a correlated way.

The paper's own sentence, verified:

> "the catch is that the proof of p-tampering attacks of [MM17, MDM18a] (and the bitwise version of [ACM+ 17]) crucially rely on the assumption that each message (which in our context corresponds to a training example) is tamperable with independent probability p, while corrupting k random parties, leads to tamperable messages in a correlated way."
