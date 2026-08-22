---
title: Adi Shamir
type: entity
entity_type: author
tags: [cryptography, adversarial-ml, cryptanalysis]
---

## About

Cryptographer at the Weizmann Institute of Science, per the affiliation given in the ingested source
below. Known for public-key cryptography and for differential cryptanalysis of block ciphers. The
work catalogued here applies the second of those to neural networks.

## Contributions / Works

- **[Polynomial Time Cryptanalytic Extraction of Neural Network Models](../sources/polynomial-time-cryptanalytic-extraction.md)**
  (Canales-Martínez, Chávez-Saab, Hambitzer, Rodríguez-Henríquez, Satpute, Shamir; 2024) — removes the
  exponential sign-recovery step from cryptanalytic extraction, making parameter recovery of a ReLU
  deep network polynomial in both queries and time, and demonstrating it on a 1.2-million-parameter
  network.
- An abstract-model account of why adversarial examples exist, cited as Shamir et al. in the related
  work of [Cryptanalytic Extraction of Neural Network Models](../sources/cryptanalytic-extraction-nn.md).
  Not ingested here.

## Connections

- [Nicholas Carlini](nicholas-carlini.md) — the extraction attack that this line accelerates is
  Carlini, Jagielski and Mironov's, and its threat model is carried over unchanged.
