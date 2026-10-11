---
title: Aleksander Mądry
type: entity
entity_type: author
tags: [adversarial-ml, robustness, learning-theory, evaluation-methodology]
---

## About

Professor at MIT. Source of the min-max formulation of adversarial training and of the adversarial-risk objective `E_{(x,y)~D}[ max_{‖δ‖_p ≤ ε} L(f(x+δ), y) ]` that every paper in this evaluation batch takes as its definition of the quantity being estimated. The PGD-adversarially-trained model from that work is the baseline that survives both major break papers: [ACW18](../sources/obfuscated-gradients.md) reports it at 47% robust accuracy on CIFAR-10 at `ε∞ = 0.031`, one of only two of nine ICLR 2018 defences not relying on obfuscated gradients, and it remains the reference model on the [RobustBench](../sources/robustbench.md) leaderboards.

## Contributions / Works

- **[On Evaluating Adversarial Robustness (CAP+19)](../sources/on-evaluating-adversarial-robustness.md)** (2019, nine authors) — co-author of the community evaluation checklist.
- **[On Adaptive Attacks to Adversarial Example Defenses (TCBM20)](../sources/adaptive-attacks-defenses.md)** (2020, with Tramèr, Carlini and Brendel).
- The adversarial-risk objective and PGD adversarial training (Madry et al. 2017) are cited as the definitional baseline in [ACW18](../sources/obfuscated-gradients.md), [CAP+19](../sources/on-evaluating-adversarial-robustness.md), [TCBM20](../sources/adaptive-attacks-defenses.md), [CGB+22](../sources/adaptive-test-time-defenses-eval.md) and [RobustBench](../sources/robustbench.md). The original paper is not itself ingested in this wiki.

## Connections

- [Nicholas Carlini](nicholas-carlini.md), [Florian Tramèr](florian-tramer.md) — co-authors.
- His robustness-versus-accuracy line of work is represented in the wiki by [Robustness May Be at Odds with Accuracy](../sources/robustness-at-odds-accuracy.md) (Tsipras et al.), whose co-author Dimitris Tsipras is also a CAP+19 co-author.
