---
title: On Evaluating Neural Network Backdoor Defenses
type: source
date_ingested: 2026-08-20
authors: [Akshaj Kumar Veldanda, Siddharth Garg]
venue: venue unconfirmed from PDF (arXiv:2010.12186, cs.LG, 23 Oct 2020)
year: 2020
tags: [adversarial-ml, poisoning-attacks, backdoor, evaluation-methodology]
claim_quantifier: existential
antecedent: none
---

## Summary

**Weakest of the backdoor-evaluation critiques; retained for the historical record.** A four-page 2020 note, superseded in scope and rigour by [QMZ+22](critical-evaluation-backdoor-countermeasures.md) and [AKK+25](sok-backdoor-defense-evaluation.md), but it is the earliest statement in this wiki of the three pitfalls that the later work confirms at scale, and it is worth having for priority. It is a critique of **practice**.

VG20 identifies three pitfalls in backdoor defenses and checks five of them (Fine-pruning, Neural Cleanse, ABS, STRIP, Qiao et al.'s generative distribution modelling) against a database of BadNets attacks the authors construct — eight attack settings spanning MNIST, CIFAR-10, GTSRB and YouTube Face, covering all-to-all, clean-label, trigger-combination, multi-trigger-single-target and multi-trigger-multi-target objectives. The pitfalls: (1) insufficient or absent evaluation across attack hyperparameters; (2) restrictive assumptions on backdoor structure and impact — small, contiguous, additive, known-size triggers and all-to-one targeting; (3) adaptive attacks against the defense's explicit assumptions never explored.

The headline empirical result is that no defense works across the board. Even with a generous 20% ASR success threshold, Fine-pruning succeeds only on the clean-label attack; Neural Cleanse succeeds on three of eight, and in two of those only when given oracular knowledge of the target label; STRIP succeeds on two and fails entirely on the all-to-all attack, as predicted from its assumption that all backdoored inputs map to one target label; the generative-modelling defense is out of scope for four settings because there is no way to supply trigger size and location, and times out or misidentifies the target on the rest. ABS could be evaluated on only one setting, because it ships as an executable bound to CIFAR-10 and one architecture, and fails there.

The paper's mechanism claims are worth keeping. Fine-pruning's premise — backdoor and clean inputs excite different neurons — is falsified simply by retraining the *same* BadNet with a different learning rate, batch size, initialization, preprocessing or optimizer. Neural Cleanse's trigger reconstruction fails on a large but semantically meaningful trigger (sunglasses on a face-recognition model), recovering triggers that match neither size, shape nor colour. ABS's single-backdoor-neuron premise is bypassed by a backdoor triggered on a conjunction of input features.

## Claim Boundary

- **Quantified over:** existentially, and over a small population. For each of five named defenses, *there exist* attack settings in the authors' constructed BadNet database on which it fails. Five defenses, eight attack settings, four datasets. No claim about the field's distribution of practice, and no statistical claim of any kind.
- **Antecedent:** none. The threat model is stated in §2 — attacker trains and uploads θ_bd to a model repository, defender evaluates on a small held-out clean validation set — and everything is measured inside it. The one deviation is generous: several defenses are *given* oracular knowledge (marked † in Table 3) and still fail.
- **Does not establish:** (i) prevalence — five defenses is not a survey, and the paper makes no prevalence claim; (ii) that the defenses are broken in their own declared settings, since several failures come from attacks outside the assumptions the defense authors stated, which is the paper's Pitfall 2 argument and not a soundness refutation; (iii) anything about attacker compute or budget. Pitfall 1 varies *training* hyperparameters of the BadNet, which is configuration variation, not additional attacker resource.
- **Abstract vs theorem:** minor overstatement. The abstract promises "a comprehensive database of backdoor attacks"; the database is eight settings, and the paper concedes "A detailed description of the attacks is not possible due to space constraints", so several attacks are named without being specified. The stated intention to release the attacks publicly is not evidenced in the PDF.

## Key Contributions

- **The three-pitfall taxonomy** (Table 1), with a per-defense presence table for Fine-pruning, Neural Cleanse, ABS, STRIP and generative modelling. This is the earliest instance in the wiki of "unstated or restrictive threat-model assumptions" as the named defect in backdoor defense evaluation.
- **A BadNet attack database** (Table 2) deliberately spanning attack objectives, not just trigger appearance: all-to-all (y → y+1), clean-label, trigger-combination (yellow triangle AND red square, the authors' own), post-it note, feature-space (Gotham filter), and multi-trigger single/multi target on face data.
- **First side-by-side evaluation** of these five defenses on a common attack set (Table 3).
- **Three mechanism-level falsifications**: Fine-pruning's neuron-separation premise, Neural Cleanse's small-contiguous-trigger premise, ABS's single-backdoor-neuron premise.
- **Forward-looking recommendations**, including the suggestion to treat attacker and defender hyperparameters jointly and seek "game theoretic equilibria between the attack and defense hyper-parameters" — the closest thing in the backdoor-evaluation literature to a resource-indexed framing, and it is a single sentence with no development.

## Key Definitions / Theorems

No theorems. Threat model only (§2): clean training set D^cl_train yields clean network f_θcl; the attacker poisons via poison: x^cl → x^p and/or relabels, producing f_θbd with f_θbd(x^cl) = f_θcl(x^cl) but arbitrary behaviour on x^p; the defender downloads θ_bd and validates on a small clean D^cl_valid. The authors note Tran et al. assume a weaker model in which the defender also has access to poisoned images.

Metrics: clean accuracy (CA), attack success rate (ASR), and for STRIP the false-acceptance rate at a fixed 3% false-rejection rate.

## Connections

- Direct ancestor of [Towards a Critical Evaluation of Robustness for DL Backdoor Countermeasures (QMZ+22)](critical-evaluation-backdoor-countermeasures.md) — same three defenses among its targets (Neural Cleanse, ABS), same brittleness finding, but QMZ+22 separates configuration failure from adaptive attack, which VG20 does not.
- Superseded in scope by [SoK: The Last Line of Defense (AKK+25)](sok-backdoor-defense-evaluation.md), whose R8 (evaluate across difficulty levels including adaptive attackers) and C8 (hyperparameter sensitivity) are VG20's Pitfalls 3 and 1 at 183-paper scale.
- VG20's opening analogy, that backdoor defenses are being broken as fast as early adversarial-example defenses were, points at [Obfuscated Gradients](obfuscated-gradients.md) and [On Adaptive Attacks to Adversarial Example Defenses](adaptive-attacks-defenses.md).
- Contemporary of the field-wide [Dos and Don'ts of Machine Learning in Computer Security](dos-and-donts-ml-security.md); VG20's Pitfall 2 is a backdoor-specific instance of pitfall P10, and Pitfall 1 of P5.
- Theory side: [Planting Undetectable Backdoors](planting-undetectable-backdoors.md) and [iO-Undetectable Backdoors in Neural Networks](io-undetectable-backdoors-nn.md) give the strong form of VG20's informal observation that "attackers are far from being restricted to specific types of backdoors".
- Concepts: [Poisoning Attacks](../concepts/poisoning-attacks.md), [Undetectable Backdoors](../concepts/undetectable-backdoors.md), [Backdoor Defense Evaluation](../concepts/backdoor-defense-evaluation.md).

## Open Questions / Limitations

- Four pages, no released artifact evidenced in the PDF, no statistical treatment, no repeated runs, single-number table entries.
- ABS is evaluated on one setting only, because the released artifact is an executable tied to CIFAR-10 and one architecture. The paper reports this as a finding about the defense's availability rather than about the defense.
- Pitfall 3 (adaptive attacks) is asserted and partly demonstrated for ABS via the conjunction backdoor, but no systematic adaptive attack is constructed for the other four defenses.
- The game-theoretic-equilibrium suggestion for joint attacker/defender hyperparameter optimization is proposed and abandoned in one sentence; nothing in the batch develops it.
- The paper does not distinguish failures caused by attacks outside a defense's declared assumptions from failures inside them — the distinction QMZ+22 later makes central.

## Quotes / Notable Passages

> "mirroring the early work on adversarial defenses, most backdooring defenses have been circumvented soon after publication."

> "In practice, however, attackers are far from being restricted to specific types of backdoors and can have a range of attack objectives."

> "We argue that a defense is incomplete unless it contends with the broadest possible class of attacks."

> "To characterize the inter-play between attackers and defender, defenses should seek to optimize both the attacker hyper-parameters to circumvent the defenses and, of course, vice-versa, using, for instance, the game theoretic equilibria between the attack and defense hyper-parameters."
