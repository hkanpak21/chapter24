# Rulings

The author's decisions, in the author's words, each one a slug. A ruling is
reopened only by a later ruling that names it. The rounds that produced them are
in `lib/profs/<date>-<handle>.md` and in `paper/reviews/`.

## Scope and framing

### 2026-08-05-measure-the-attack-do-not-prove-it-hard
The near-term goal is to measure an attack's capability against a concrete
adversary. Hardness comes later, and a defence mechanism is not being proposed.
No sentence in the paper may claim a hardness result.

### 2026-08-20-the-subject-is-characterization-not-imposition
The paper characterizes adversary capability in complexity-theoretic terms. It
does not impose bounds and it does not concern the efficiency of training or
inference. The word efficiency stays out of the title and the abstract, because
to most readers it means quantization and compute-optimal scaling.

### 2026-08-20-crypto-with-no-learning-content-enters-as-a-destination
Fine-grained cryptography and the bounded-storage line enter the corpus although
they contain no machine learning, because each is the formal home of a quantity
machine learning measures without defining. They enter as destinations, and the
paper reports that nothing in the machine learning half has travelled to either.

### 2026-08-20-the-frame-has-an-outside
Pure expressivity results, accuracy-against-robustness tradeoffs and geometric
inevitability results fall outside the frame, and the paper says so. A frame
that holds everything asserts nothing.

### 2026-08-22-membership-inference-is-not-the-running-example
Membership inference states the three problems of Section 2 and carries no
further. It is the subject of none of the regions of Section 6, and it appears
in 21 of the 200 source pages. Each part carries its own worked case.

## The codebook

### 2026-09-03-a-bare-two-party-inequality-is-relative
A bound stated as a relation between two parties' work is `relative` whether or
not it carries an exponent, a class or a security parameter. Proof-of-learning's
Property 2 is therefore `relative`. This moved the headline pair to 18 and 6.

### 2026-09-03-a-radius-a-theorem-outputs-binds-nobody
A perturbation radius that a theorem concludes, as in the concentration of
measure results, is the conclusion and not a restriction on any party. Those
works bind nobody. A radius a paper fixes in advance as its threat model is a
`budget` on the attacker, and the two cases stay apart.

### 2026-09-03-a-restricted-class-lower-bound-binds-the-learner
A lower bound against a restricted algorithm class with no security role in the
work binds the `learner`. This covers the statistical-query and low-degree
bounds that three classifiers had coded to three different parties.

### 2026-09-03-a-catalogued-definition-is-not-an-asserted-bound
A work that restates another paper's definition in a catalogue asserts no bound.
`sok-differential-privacies` is `party=none`, which is the reading its sibling
systematization already carried.

## Sources and citation

### 2026-08-22-citation-hierarchy
When two sources support one point, cite and quote in this order. First, a
peer-reviewed paper at a top venue in the relevant field: CRYPTO, EUROCRYPT,
ASIACRYPT, TCC, IEEE S&P, USENIX Security, ACM CCS, NDSS for security and
cryptography; STOC, FOCS, SODA, COLT for theory; NeurIPS, ICML, ICLR for machine
learning. Second, a peer-reviewed paper at any other venue. Third, a preprint or
a work whose venue the corpus could not confirm. A third-tier source may be
cited, may not carry an argument alone when a higher tier says the same thing,
and is named as a preprint where it is load-bearing. `lab/src/cite-weight.py`
reports the tier of every citation in a section.

### 2026-08-22-recency-is-checked-not-assumed
A result from two years ago may already have been abandoned. Prefer the most
recent work that addresses a verdict, and check whether a later paper measured
the hypothesis or refuted the claim before repeating it. A citation from 2024 is
not current by default. The repository's record of refuted claims is in the root
`CLAUDE.md` and is read before any novelty claim enters the paper.

### 2026-08-22-author-standing-is-a-tiebreaker
Author standing breaks a tie between two sources of the same tier and the same
recency. It never outranks the citation hierarchy or the recency rule, because
this corpus already holds cases where a well-cited paper's headline overstated
its own theorem.

### 2026-08-20-an-unverified-count-is-not-written
A quantitative claim enters the paper after a count, never from memory. The rule
exists because a recommendation in this project once asserted that membership
inference appeared in five of six regions when the true figure was zero, and the
claim survived two turns because nothing forced it through a count.

## Layout

### 2026-09-17-the-survey-is-the-project-root
`exp/survey` is the project root and carries the research skill's layout, with
`lab/`, `lib/`, `paper/` and `sink/` beneath it. The repo-root `wiki/` and
`raw/` stay outside it under the repo-root `CLAUDE.md`, because they are a
literature knowledge base and not this paper's working directory.
