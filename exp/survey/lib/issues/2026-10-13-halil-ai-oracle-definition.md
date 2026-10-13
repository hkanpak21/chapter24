---
slug: 2026-10-13-halil-ai-oracle-definition
opened: 2026-10-13
assignee: halil
status: open
raised_by: halil
closed_by:
source: the 2026-10-13 discussion
---

# Define an AI oracle in which membership leakage can be bounded

## What this is

An idealized model of training, called the AI oracle, in which statements about
what an adversary learns of the training data can be proved, with adversaries
classified by the operations they may use and by their computational power.
The record of the discussion that opened it follows, in the order it ran.

### The author's conjecture

White-box membership inference is at least as strong as black-box, because a
white-box attacker can simulate the black-box one. The question is whether
black-box can be as strong as white-box, and if not, what limits it, with
examples where white-box is far stronger whatever the black-box attacker does.

The author expects the gap to appear only for computationally bounded
attackers. An unbounded attacker with unlimited queries can, intuitively, try
every model in the class and recover the white-box model up to noise.

The wider point: attacks in the literature already restrict the attacker, to
gradient updates and not to search over the hypothesis class, without saying
so formally. Training is not understood, just as hash functions are not, and
cryptography handles hash functions with an oracle model. Other oracle models
exist in mathematics, among them one on a ring structure.

### Anchors found so far

- Code access against oracle access is the obfuscation question. Barak,
  Goldreich, Impagliazzo, Rudich, Sahai, Vadhan, Yang (CRYPTO 2001) give
  function families whose code reveals a secret that no efficient algorithm
  with oracle access learns. Proven. Not yet in the library, to open.
- Unlimited queries return the function, not the weights. A learner can store
  information in parameters that do not affect any output, which a white-box
  attacker reads and an unbounded black-box attacker never sees. So an
  information gap exists whenever the weights carry more than the function.
  Proven by that construction, which is trivial.
- SDSOJ19 (ICML 2019): if training is modelled as sampling from a Gibbs
  posterior, the Bayes-optimal membership attack reads the weights only through
  the loss, so white-box gains nothing. Proven under that model. The Gibbs
  posterior is itself an idealized model of training, the role a random oracle
  plays for a hash function.
- CJM20 and CCHRSS24: ReLU networks can be extracted up to functional
  equivalence in polynomial time from black-box queries. For that class the
  computational gap between black-box and white-box is bounded by the
  representation, not by the function.
- Gradient-based attackers are attackers with a first-order oracle, a standard
  class in optimization (oracle complexity). Heuristic as a reading of the
  attack literature.

### Open

- Which oracle is training: the trained model's input-output map, the learning
  algorithm queried on chosen datasets, or the posterior it samples from?
- The random oracle methodology has known failures, schemes secure with a
  random oracle and insecure with every concrete hash (Canetti, Goldreich,
  Halevi, 1998). What is the analogue for an idealized model of training?
- Which ring oracle the author found: the generic ring model, or black-box fields.

### The author's clarifications, same day

The unbounded attacker tries every function in the family with unlimited
queries and picks the one that matches. The response recorded here: picking
the function fixes the weights only up to the weights that compute the same
function. So the unbounded black-box attacker equals the white-box one exactly
when what the weights reveal about membership is already a property of the
input-output map. For ReLU networks the function fixes the weights up to
permutation and scaling, which is what the extraction attacks exploit, so for
that class the author's intuition holds and any gap must be computational.

By oracle the author means delegating the training function to an abstract
entity and proving statements relative to it. The example: in one-shot
federated learning with an aggregation that is symmetric in the clients'
updates, no adversary that sees the aggregate can tell which of two clients
held which of two challenge distributions, since swapping them leaves the
aggregate unchanged. That proof needs no knowledge of training. Membership of
one training point is different. A proof about it needs to know what happens
when a point enters the training function, and the author has no handle on
that.

Recorded response: the federated proof uses a property of the protocol.
Membership needs a property of training itself. Three existing abstractions
state such a property and prove membership bounds relative to it without
opening training:

- differential privacy, a bound on how much one point moves the output distribution;
- the Gibbs posterior of SDSOJ19;
- information measures between the training set and the output (CMI, SZ20 in the information sweep).

Open: an idealized training oracle that, like the random oracle, assumes no
quantitative property, and under which black-box against white-box and bounded
against unbounded can be separated.

### Utility, the manifold, and a definition free of learner choices

The author: data on a low-dimensional manifold gives emergent zero-shot
behaviour. In the version-space note this is the case where a model trained
without a point predicts it anyway, so the point leaks nothing. Leakage
concentrates off the manifold, on the long tail.

The author wants the definition simpler, independent of the learner's choices,
with only the data and the model class specified. Recorded proposal: remove the
learner by quantifying over it. Fix the data distribution, the class, a utility
level, and the attacker's access and power. Two quantities follow.

- Necessary leakage: the least leakage every learner with that utility has.
  This is the form of Feldman (STOC 2020) and Brown et al. (STOC 2021).
- Achievable leakage: the least leakage some learner with that utility reaches.
  This is the form of differential privacy upper bounds.

For unbounded parties, black-box and white-box coincide on the achievable side,
because a learner can output a canonical description of its function, for
example the first parameter vector in a fixed order that computes it. Proven,
trivially. The question then becomes computational: whether an efficient
learner can hide its representation. That is the question indistinguishability
obfuscation answers as best-possible obfuscation (Goldwasser, Rothblum, TCC
2007, to open). So the black-box against white-box question, stated free of
learner choices, is an obfuscation question for learners.

### The oracle as something to query

The author: what matters is that leakage depends on the training data, not
that it is small. Pre-training confounds this, since a point can be predicted
because pre-training saw it. The counting step and the two leakage frontiers
are set aside as off the objective.

The author's aim: an AI oracle that can be queried, so that leakage is measured
or bounded by simulations curated with it.

Recorded reading: the oracle is the training procedure itself, called on a
dataset of the caller's choice and returning a model. Leakage of a point is how
well the outputs on a dataset with the point can be told from the outputs on
the same dataset without it, measured against the pre-trained starting point so
that pre-training is not counted. The resource is the number of oracle calls,
which is training runs.

The practice already does this without naming it.

- Shadow models (Shokri et al., S&P 2017, wiki: membership-inference-shokri)
  are calls to the training oracle on curated datasets.
- LiRA (Carlini et al., S&P 2022, wiki: mia-from-first-principles) fits the
  with-point and without-point output distributions from such calls. Its cost
  is counted in training runs.
- Privacy auditing lower-bounds a DP parameter from calls on datasets with
  planted canaries. HSU25 gives the sample complexity of auditing.

Open, and to check for prior art before any claim: a formal model with the
training procedure as an oracle and calls as the resource, in which black-box
access to the target plus oracle calls can be compared with white-box access.

### Why the question does not yet bite

The author: the black-box plus oracle-calls question does not make sense yet,
and the problem is not fully stated.

Recorded diagnosis: the answer is fixed by the choice of learner before any
attacker is considered.

- Learner arbitrary: white-box wins trivially. Store the training set in
  weights that never affect an output. Utility is untouched.
- Learner idealized (Gibbs posterior, version space): no gap, proven (SDSOJ19,
  the version-space note).
- Learner real (SGD on deep networks): any gap is empirical. Nothing about it
  is provable today.

A meaningful version sits between the first and the third: a training paradigm
fixed tightly enough to forbid deliberate hiding and loose enough to leave a
gap. The backdoor papers make exactly this move when they fix the paradigm
(random Fourier features, a frozen random first layer) and prove inside it.

### The interface does not bound leakage

The author: the generic-model draft cannot bound membership leakage. It is an
interface of deep learning.

Recorded answer: correct. The draft fixes the operations and idealizes the
weights given the function, and leaves the distribution of the learned function
free. An arbitrary training procedure can leak everything, so no bound follows.
The random oracle model is powerful because it fixes a distribution, uniform
values, and not only an interface. A training oracle that bounds leakage has to
fix the distribution of the function it returns. Two candidates, both
quantitative:

- Version space, the zero-temperature case: advantage equals one minus the
  probability that a model trained without the point predicts it. Exact, in the
  version-space note.
- Gibbs at temperature T with a loss in [0, 1]: this is the exponential
  mechanism, epsilon-DP with epsilon = 2/T (McSherry and Talwar, FOCS 2007;
  posterior sampling, Wang, Fienberg, Smola, ICML 2015, to open), so
  membership advantage is bounded through DP (Yeom et al., CSF 2018).
  Temperature trades utility against leakage.

Tension: any oracle that fixes the function distribution this way also makes
white-box equal black-box (SDSOJ19). Inside such an oracle the only room for a
bounded-against-unbounded difference is the attacker's inability to compute the
likelihoods, which is the counting step set aside earlier.

### What the coded field says, 2026-10-13

Source: `lib/literature/ontology/onto.tsv` and `views.md` beside it, 237 works coded by five agents from
wiki pages and sweep sheets, 92 core, 98 peripheral, 47 out. Labels are the
coders' readings, often `inferred`, so the counts are empirical on our coding,
not on the papers.

- Training is measured or quantified over, almost never idealized. Of the 190
  relevant works, 40 study concrete deep networks, 36 quantify over all
  learners, 30 assume DP. One assumes a Gibbs posterior (SDSOJ19), two assume
  stability, none a version space. Seven treat training as an opaque call:
  the shadow-model membership works, an adversary-knowledge SoK, two others,
  and Villa et al.'s AIOracle.
- Access is white-box (55) or black-box queries (34). Gradient access is a
  formal object in four works. Calls to training appear in ten.
- No attacker is a formal first-order class. All 13 first-order entries are
  learners, the SGD exponent papers. Gradient attacks exist and are never
  given a class.
- Attackers are unbounded (58), polynomial-time (52), or one fixed attack
  algorithm (33). Among core works, 27 analyse one fixed attack.
- 47 of the 92 core works state no utility condition.

## What closes it

A definition of the AI oracle that the author accepts, written as a report,
that fixes the distribution of the learned function, states a utility
condition, and supports at least one proved bound on membership advantage.

## Where it touches

lib/reports/2026-10-13-halil-version-space-oracle.pdf
lib/reports/2026-10-13-halil-ai-oracle-definition.pdf
lib/literature/ontology/onto.tsv
lib/literature/ontology/papers.tsv
The wiki page extending-formalism-cryptography-ai, the published AIOracle to position against
