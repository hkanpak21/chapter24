---
title: Francesco Croce
type: entity
entity_type: author
tags: [adversarial-ml, robustness, evaluation-methodology, certification]
---

## About

Researcher at the University of Tübingen. With Matthias Hein, author of AutoAttack — the parameter-free ensemble of APGD (cross-entropy and difference-of-logits-ratio losses), targeted FAB and the black-box Square Attack — which became the field's de facto standard robustness evaluation, and the engine of the [RobustBench](../sources/robustbench.md) leaderboard.

Croce occupies both sides of the standardization debate. [RobustBench](../sources/robustbench.md) is the attempt to make robustness evaluation automatic and comparable; [CGB+22](../sources/adaptive-test-time-defenses-eval.md) is his own hand-built case study of the defence family RobustBench had to exclude, and concedes that "the most effective attack differs across cases". The compute remark that the survey strand tracks — that defender computation might be justified if it imposes more computation on the attacker — is from the conclusion of that second paper.

## Contributions / Works

- **[RobustBench: a standardized adversarial robustness benchmark (CAS+21)](../sources/robustbench.md)** (NeurIPS 2021, Datasets and Benchmarks track) — leaderboard, Model Zoo, three admission restrictions, AutoAttack unreliability flag.
- **[Evaluating the Adversarial Robustness of Adaptive Test-time Defenses (CGB+22)](../sources/adaptive-test-time-defenses-eval.md)** (ICML 2022) — taxonomy of test-time-optimization defences; nine defences shown to overestimate robustness, four of them weakening their own static base.
- AutoAttack and APGD (Croce & Hein 2020) are cited as the standard evaluation throughout the batch; the original paper is not itself ingested here.

## Connections

- [Matthias Hein](matthias-hein.md) — long-running co-author, on both works above.
- [Prateek Mittal](prateek-mittal.md) — RobustBench co-author.
- His AutoAttack is the target of the automation scepticism in [TCBM20](../sources/adaptive-attacks-defenses.md), which reports it only partially succeeding on two of four shared defences.
