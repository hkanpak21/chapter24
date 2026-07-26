# The Fiber of the Training Map

*An introduction. Companion to [intro-computational-security-of-learning.md](intro-computational-security-of-learning.md).*

---

## 1. Training is a map, and it is not injective

Begin with the least controversial thing one can say about machine learning: training is a function.
It takes a dataset and returns weights.

```
L : D ↦ w
```

Fix the architecture, the optimizer, the hyperparameters, and the random seed, and this is a
deterministic map from datasets to parameter vectors. Nothing here is specific to deep learning.
Linear regression has such a map. So does k-means. So does fitting a histogram.

The map is not injective. Many different datasets produce the same weights. For a given `w` in the
image, write

```
L⁻¹(w) = { D : L(D) = w }
```

and call this the **fiber over `w`** — the set of all datasets that would have produced exactly this
model.

Every question about what a trained model reveals about its training data is a question about this
set. That is the claim this note develops, and the reason for introducing the vocabulary.

## 2. Two parties looking at one object from opposite sides

The person training the model wants some `w` for which the model is accurate. They do not care which
one. If many parameter settings work, that is good news: the search has many acceptable targets.

The person attacking the model sees `w` and wants to know something about `D` — whether a particular
record was in it, what a particular record was, whether a trigger was implanted. Every element of the
fiber is a candidate answer. If many datasets produce this `w`, the attacker cannot tell which one
did.

These are the same fact. **The multiplicity that makes training tractable is the multiplicity that
obstructs inversion.**

This is worth dwelling on, because it is not how security is usually described. The standard picture
has two parties with different resources — one holds a key, one does not; one runs in polynomial time,
one does not. Here there is no resource asymmetry at all. Both parties run efficient algorithms on the
same kind of input. What separates them is only which direction they are traversing a map that is
lossy in one direction and cheap in the other.

## 3. The story we already tell about this is a story about size

The existing formal account of what a model leaks is differential privacy, and in this language it is
a statement about how much the fiber *moves* when you change one record. If swapping a single training
example barely changes the distribution over outputs, then the fibers over nearby `w` overlap heavily,
and observing `w` cannot tell you which of two neighbouring datasets you had.

This is a good theory and it is correct as far as it goes. What it measures is a **size**: how much
probability mass sits over each `w`, and how that mass shifts under a one-record perturbation. It
makes no reference to computation. The adversary in a differential privacy guarantee is allowed
unlimited time.

## 4. Size is not the security question

Here is the problem with stopping at size. A haystack is only a hiding place if you cannot sort hay.

Take the simplest possible case: ordinary least squares. With design matrix `X ∈ ℝⁿˣᵈ` and targets
`y ∈ ℝⁿ`, the fitted weights are

```
w = (XᵀX)⁻¹ Xᵀy
```

The weights depend on the data only through the two summaries `A = XᵀX` and `b = Xᵀy`. So the fiber
over `w` contains every dataset whose summaries satisfy `A⁻¹b = w` — a set of dimension roughly `nd`,
constrained by only `d` equations. It is enormous. By any measure of size, the model has hidden its
training data in a very large haystack.

Now try to walk into it. Choose any full-rank `X` you like. Then solve

```
Xᵀ y = (XᵀX) w
```

for `y`. That is `d` linear equations in `n` unknowns with `n > d`, so the solutions form an affine
subspace of dimension `n − d`, and picking a point in it is one linear solve. **A member of that
enormous fiber can be produced in polynomial time, by hand, on the first attempt.**

Worse, and this is the part that matters. Suppose the attacker already knows most of the data — say
all of `X`, and all of `y` except one entry `yⱼ`. That knowledge is itself an affine constraint.
Intersect it with the fiber: now the same system has `d` equations and one unknown, is
overdetermined, and has a unique solution. **The attacker recovers `yⱼ` exactly.**

This is the classical reconstruction attack, and in this language it is not a clever trick. It is the
observation that the fiber was an affine subspace, the side information was an affine constraint, and
intersecting affine objects is linear algebra.

The lesson generalizes past this example: **the fiber was huge and it protected nothing, because it
was flat.** What failed was not size. It was that the set had no computational structure — you could
compute inside it as easily as you could describe it.

## 5. Navigability

So the security question is not how large the fiber is. It is:

> **Given `w`, and given whatever side information the attacker holds, is it computationally feasible
> to find a point of the fiber consistent with that information?**

Call this the **navigability** of the fiber. It is a search problem: the search space is defined by the
training process itself, and the constraints are supplied by the attacker's knowledge.

Two quantities move against each other:

- **Side information shrinks the fiber.** Every fact the attacker knows about `D` is a constraint that
  cuts the candidate set down.
- **Computation searches what remains.** Whatever the constraints leave, the attacker must actually
  find a point in it.

Security, if there is any, is the region where the attacker has cut the fiber down as far as its
knowledge allows and *still* cannot find a point in what remains. The exchange rate between these two
— how much search cost one unit of side information buys off — is the quantity worth measuring, and
it is a computational quantity that no size-based theory can see.

## 6. Two refinements the setup needs

**Randomness.** Real training is stochastic: minibatch order, initialization, dropout. Then `L` is not
a function but a randomized map, and the fiber is properly the conditional distribution of `D` given
`w` rather than a set. Nothing essential changes — the questions become "is this conditional
distribution efficiently samplable" and "can a high-probability point be found" — but the deterministic
picture is the one to hold in mind first.

**Two different many-to-one-nesses, which must not be confused.** Neural networks are redundantly
parameterized: permuting hidden units or rescaling across a ReLU gives a different `w` computing the
identical function. That is a symmetry of the *evaluation* map `w ↦ M_w`, and it says the
parameterization is wasteful. It is not the fiber. The fiber concerns the *training* map `D ↦ w`, and
it says training is lossy. Only the second is a statement about data.

The two do interact, and the interaction explains something. An attacker with the weights sees which
representative of the symmetry class training happened to land in — and where you land depends on the
trajectory, which depends on the data. An attacker restricted to querying the model as a black box
sees only the function, so its fiber is the union of the fibers over every `w` realizing that function:
strictly larger, and therefore strictly less informative. **This is why white-box access is more
dangerous than black-box access, stated as a containment rather than as an intuition.**

## 7. Why this framing is worth adopting

Three reasons, in increasing order of importance.

It requires no imported cryptography. Existing computational results in this area typically attach a
cryptographic object to a learner — a signature appended to each input, labels generated by a
pseudorandom function — and derive hardness from the attached object. Such results are correct, but
the hardness is a property of the attachment, not of learning: delete the learner and the theorem
survives intact. The fiber question has no attachment to delete. Its hardness, if any, is a property
of the training map.

It makes the black-box/white-box distinction a theorem rather than a convention.

And it converts the security question into a search problem over a concretely defined set, which is
the kind of object complexity theory knows how to reason about — average-case, structured, with a
tunable amount of side information.

## 8. What is not known

Almost everything, which is the point.

For linear models the fibers are affine and navigable, and there is no protection. For a model that
memorizes its training set the fiber is a single point, and there is no protection either. Between
those extremes sits every model anyone actually deploys, and the shape of the fiber there — its
dimension, whether it is connected, whether a point in it can be found efficiently from partial
knowledge — is not known for any realistic architecture.

The first question worth answering is the smallest one: for a single-index model on Gaussian data with
a fixed architecture, what does the fiber of the training map look like, and can a point in it be
found in polynomial time given the weights and a bounded amount of side information? If the answer is
that it can, the geometric route closes and one learns so quickly. If it cannot, there is a
computational security statement about learning that owes nothing to an appended primitive.
