# SoK: How Hard Is the Attack?

Target venue IEEE S&P, Systematization of Knowledge track. Started 2026-08-05.

## What this is

A complexity-theoretic systematization of machine learning security. We read 200
formal works on the security and privacy of learning and record, for each one,
which party's resources enter its main claim, in what unit, and how tightly. The
subject is the characterization of adversary capability, not the imposition of
bounds and not the efficiency of training or inference. The word efficiency stays
out of the title and the abstract, because to most readers it means quantization
and compute-optimal scaling.

## The claim

Formal claims about the security of machine learning cannot be compared with one
another, because almost none of them states what the attacker may spend, and the
vocabulary for stating it already exists in fine-grained cryptography and has
never been carried across.

Every result in this paper is a measurement of a coded corpus. The paper proves
nothing, and no sentence in it may say that it does.

## People

| Handle | Name | Role |
| --- | --- | --- |
| halil | Halil İbrahim Kanpak | author |

## Terminology ledger

One name for one thing. Every term fixed here is used nowhere else by another
name, in the paper, the code, the figures, or a report.

| Term | Means | Never called |
| --- | --- | --- |
| party | whoever a work's main claim bounds: attacker, learner, auditor, mechanism, or nobody | the actor, the entity, the agent |
| unit | the resource a bound is stated in: time, circuit size, queries, samples, memory, algorithm class, perturbation, corruption, privacy budget | the currency, the resource type, the metric |
| tightness | how a bound is stated: unstated, poly, quasi-poly, conditional, class, budget, exponent, relative, measured | strength, precision, sharpness |
| relative bound | a bound stated as a relation between two parties' work | a two-party bound, a comparative bound, a ratio |
| exponent | a bound stated as an exponent in one party's own resource | a scaling law, a threshold, a power |
| budget | a numeric allowance such as a perturbation radius or a corruption fraction | an allowance, a cap, a limit |
| baseline | what a party with public knowledge alone achieves against the target | the null, the chance rate, the reference |
| adversary class | the set of algorithms a claim quantifies over | the attacker model, the adversary model |
| attack family | the attack, in the standard taxonomy | the attack type, the threat class |
| access | the strongest access a main claim grants | the knowledge level, the visibility |
| phase | when the adversary acts: train time, test time, post hoc | the stage, the timing |
| assessed | whether a work treats its bound as its object or leaves it a side condition | explicit or implicit treatment, the framing |
| near miss | a work whose tightness and assessment disagree | a borderline case, an outlier |
| corpus | the 200 classified works | the dataset, the paper sample, the collection |

## Symbols

| Symbol | Means | Defined in |
| --- | --- | --- |
| $\delta$ | the fine-grained gap, adversary work at least honest work to the power $1+\delta$ | sec-prelim |
| $\eta$ | the tolerance in a reconstruction success criterion | sec-prelim |
| $D$ | the degree bound of a low-degree adversary | sec-prelim |

## lint allowed words

The linter treats each of these as slop unless it is named here. Each is a term
of art in this paper's subject and is used in one sense only.

- party
- budget
- unit
- baseline
- gap
- landscape

## Current state

Text is 12 pages of 13, built from `paper/main.tex`. The classification is
complete at 200 of 200 and every reported number is a macro generated from
`lib/numbers.csv`. Two adversarial review rounds are closed and recorded in
`paper/reviews/sp27/`. The open work is in `lib/issues/` and the author's rulings
are in `lib/profs/rulings.md`. The next S&P cycle closes 2026-11-17 with abstract
registration on 2026-11-10, and the call is the authority on both dates.
