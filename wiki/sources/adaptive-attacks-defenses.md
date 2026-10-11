---
title: On Adaptive Attacks to Adversarial Example Defenses
type: source
date_ingested: 2026-08-20
authors: [Florian Tramèr, Nicholas Carlini, Wieland Brendel, Aleksander Mądry]
venue: "NeurIPS (Advances in Neural Information Processing Systems 33, 2020, pp. 1633-1645; the PDF carries no venue line, venue read from the bibliographies of CAS+21_RobustBench and AZT24_PrivacyDefensesMisleading in this corpus)"
year: 2020
tags: [adversarial-ml, evasion-attacks, robustness, evaluation-methodology, threat-model]
claim_quantifier: existential
antecedent: none
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: white box
cls_write: read only
cls_frame: capability
cls_party: attacker
cls_unit: perturbation
cls_tightness: budget
cls_baseline: absent
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "Projected Gradient Descent (Madry et al., 2017) is a strategy for finding an adversarial example x0 for an input x that satisfies a given norm-bound."
cls_evidence_src: "Section 2.1, PGD paragraph, p. 5. The sentence continues with the inequality \"kx0-xkp <= [epsilon]\" in the PDF; the epsilon glyph extracts as an unreadable control byte (0x0F) with pdftotext, so the quotation stops before it."
cls_reason: "Hand-classified 2026-08-22 against codebook revision 2, then migrated through revisions 3 to 5. Carries no verbatim evidence quote, unlike the delegated rows."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The follow-up to [Obfuscated Gradients](obfuscated-gradients.md), written after the community adopted its advice. The premise is that adaptive evaluation is now standard — the fraction of defences evaluated adaptively went from "close to zero in 2017" to "one third in 2018" to "nearly all of them today" — and the question is whether that fixed anything. It did not. Thirteen defences from ICLR, ICML and NeurIPS, all of which performed adaptive evaluations, are circumvented.

The paper's own framing of its contribution is methodological rather than technical: "the technical tools to evaluate defenses properly already exist. A better attack can be built using only tools that are well-known in the literature. Thus, the issue with current defense evaluations is methodological rather than technical." Where ACW18 had to invent BPDA and reparameterization, this paper reuses PGD, C&W, BPDA and EOT and wins on loss-function design and targeting.

The structure is unusual and is part of the contribution: each of thirteen sections walks through *how the defence was broken*, in the order the authors actually worked — how the defence works, why it was selected, initial hypotheses from reading the paper and its source code, failed attempts, final attack, lessons learned. The stated purpose is to make the discovery process, not just the result, reproducible.

Six recurring themes are distilled (§4), under a meta-theme T0, "strive for simplicity": T1 attack a function close to the full defence; T2 identify and target the important defence parts; T3 adapt the objective to simplify the attack; T4 ensure the loss function is *consistent*; T5 optimize the loss with different methods, including black-box ones; T6 use a strong adaptive attack for adversarial training. T4 is the deepest of these and is new relative to ACW18: the failure it names is not an optimization failure but a *proxy* failure — "even with an all-powerful optimizer that is guaranteed to find the loss' optimum, an attack may fail." That is a claim about the objective, not about the compute spent on it, and it cuts against the idea that more attack compute is the fix.

The conclusion states an informal "no-free-lunch-theorem": "For any proposed attack, it is possible to build a non-robust defense that prevents that attack." From this the authors conclude that adaptive attacks cannot be automated, and that no automated tool — AutoAttack included — can comprehensively evaluate a defence.

## Claim Boundary

- **Quantified over:** thirteen named defences, selected by two stated criteria (accepted at ICLR/ICML/NeurIPS; illustrating a distinct concept). All thirteen are circumvented in the sense of "substantially reduce the accuracy from what was originally claimed". The authors state explicitly that the selection was not cherry-picked after the fact: "This report contains our evaluations for all of our initially selected defenses. In particular, we did not cherry-pick the defense evaluations to present based on the results of our evaluation." Each break is one existence proof of a stronger attack.
- **Antecedent:** none for the empirical results. The informal no-free-lunch statement has the form ∀ attack ∃ defence — universal over attacks, existential over defences — and is offered as an informal argument, not proved. It is a statement about *non-robust* defences that happen to block a fixed attack, so it does not bear on whether robust defences exist.
- **Does not establish:** (a) that the defensive *techniques* are without merit — the authors say the opposite: "we do not wish to claim that the robustness techniques used by many of these defenses hold no merit whatsoever. It may well be that some instantiations of these techniques can improve model robustness"; (b) that robustness is impossible; (c) that adaptive attacks are impossible to automate as a matter of principle — the argument for "no automated tool will be able to comprehensively evaluate the robustness of a defense" is the informal no-free-lunch plus the observation that AutoAttack only partially succeeds on two of the four overlapping defences, not a proof; (d) that accuracy is reduced to 0% — the stated goal is not to do so, only to degrade it below the reported figure, though the authors add in a footnote that most defences are reduced to baseline-model accuracy.
- **Abstract vs theorem:** the phrase "no-free-lunch-theorem" is in quotation marks and prefaced by "informal" in the paper; a reader citing it as a theorem would be overstating it. Otherwise the abstract matches ("thirteen defenses ... can be circumvented despite attempting to perform evaluations using adaptive attacks").

## Key Contributions

- Thirteen adaptive-attack case studies documented in discovery order, including failed hypotheses.
- The six-theme taxonomy T1–T6 with meta-theme T0 (simplicity), and a table mapping each theme to the defences that illustrate it.
- **Loss consistency (T4)** as a failure mode distinct from optimization difficulty: a loss can be perfectly optimized and still not correspond to attack success.
- The informal no-free-lunch statement, and the resulting recommendation to treat evaluation against prior adaptive attacks as a *sanity check only*, deferring non-adaptive evaluations to an appendix.
- The finding that combining a defence with adversarial training frequently yields *lower* robustness than adversarial training alone (T6), because the weak attack used in training fails to find examples.
- The negative result on automation, exhibited against AutoAttack on four overlapping defences.
- Responsible disclosure to all thirteen author groups; twelve of thirteen confirmed the breaks.

## Key Definitions / Theorems

No formal theorems. Definitions and statements:

- **Adaptive attack**: an attack "specifically designed to target a given defense", constructed after the defence is fully specified.
- **Consistent loss function (T4)**: one for which higher loss values result in strictly stronger attacks. The negation is the failure mode: "even with an all-powerful optimizer that is guaranteed to find the loss' optimum, an attack may fail. Such loss functions are not consistent and should be avoided."
- **Informal no-free-lunch statement**: "For any proposed attack, it is possible to build a non-robust defense that prevents that attack."
- **Feature adversaries (T3)**: pick a natural input `x*` from another class and generate `x'` matching `x*`'s representation at an inner layer — reported effective against detection defences.
- Background attacks used, not introduced: PGD, C&W, BPDA, EOT.

## Connections

- Sequel to [Obfuscated Gradients (ACW18)](obfuscated-gradients.md); shares two authors and reuses its techniques rather than inventing new ones.
- Tests, and finds insufficient, the adaptive-attack recommendation of [On Evaluating Adversarial Robustness (CAP+19)](on-evaluating-adversarial-robustness.md).
- Cited by [RobustBench (CAS+21)](robustbench.md) as the motivation for its three admission restrictions, and as the reason EOT alone is not accepted as a standardized evaluation of randomized defences.
- Its automation-scepticism is the standing objection to [RobustBench](robustbench.md)'s AutoAttack-based leaderboard; RobustBench answers it with the unreliability flag and an invitation for external adaptive evaluations.
- Method extended to a specific defence family by [Evaluating the Adversarial Robustness of Adaptive Test-time Defenses (CGB+22)](adaptive-test-time-defenses-eval.md).
- Concepts: [Adaptive Attacks](../concepts/adaptive-attacks.md), [Obfuscated Gradients](../concepts/obfuscated-gradients.md), [Evasion Attacks](../concepts/evasion-attacks.md).
- Authors: [Florian Tramèr](../entities/florian-tramer.md), [Nicholas Carlini](../entities/nicholas-carlini.md), [Aleksander Madry](../entities/aleksander-madry.md).

## Open Questions / Limitations

- No positive criterion. The paper says what a good adaptive attack looks like after the fact and gives no procedure for producing one, by design — its central claim is that no such procedure exists.
- The no-free-lunch statement is informal and unquantified. It does not distinguish a defence that blocks an attack by removing adversarial examples from one that blocks it by breaking the optimizer, which is the distinction the whole literature turns on.
- T4 (loss consistency) is never formalized. "Higher loss values result in strictly stronger attacks" is a monotonicity condition relating a surrogate to the 0-1 attack success indicator; the paper gives no definition that could be checked.
- The selection criterion "clearly illustrates some concept" is not reproducible, and the authors record a posteriori that some selected defences turned out to fail in similar ways.
- Nothing is said about attacker cost. The evaluations report attack designs, not attack budgets, and the paper's compute position is inherited silently from its predecessors.

## Quotes / Notable Passages

The diagnosis:

> "the technical tools to evaluate defenses properly already exist. A better attack can be built using only tools that are well-known in the literature. Thus, the issue with current defense evaluations is methodological rather than technical."

The informal no-free-lunch statement, quoted in full as it appears:

> "For any proposed attack, it is possible to build a non-robust defense that prevents that attack."

On loss consistency (T4), the failure that is not an optimization failure:

> "even with an all-powerful optimizer that is guaranteed to find the loss' optimum, an attack may fail. Such loss functions are not consistent and should be avoided."

On automation:

> "It is critical that adaptive attacks are hand-designed to target specific defenses. No automated tool will be able to comprehensively evaluate the robustness of a defense, no matter how sophisticated."

On what is not being claimed:

> "we do not wish to claim that the robustness techniques used by many of these defenses hold no merit whatsoever."
