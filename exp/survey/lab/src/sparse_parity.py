#!/usr/bin/env python3
"""Empirical face of the NO AIMING postulate: the cost of obtaining a target model
by learning scales as a measured power law in the problem dimension.

Target class: k-sparse parity on {+-1}^d. The label is the product of the bits on
a hidden k-subset S. This is the cleanest case where the target is one specific
function, the only known way to obtain a model computing it is to train, and the
cost of training with single-pass SGD is known to scale as d^{Theta(k)}.

We train a 2-layer ReLU network with online (fresh-batch) SGD, one gradient step
per batch, so that each step is one correlational statistical query on fresh
samples. We measure the number of steps to reach a test-accuracy threshold, as a
function of d with k fixed, and fit a power law. The fitted exponent is the
measured price of the search that the framework calls NO AIMING.

Determinism: every source of randomness is seeded from a single integer passed in.
"""
import argparse
import json
import sys
import numpy as np
import torch
import torch.nn as nn


def make_batch(rng, d, S, batch):
    x = rng.integers(0, 2, size=(batch, d)).astype(np.float32) * 2 - 1  # +-1
    y = np.prod(x[:, S], axis=1)                                        # +-1 parity
    return torch.from_numpy(x), torch.from_numpy((y > 0).astype(np.int64))


def steps_to_learn(d, k, seed, width, batch, lr, max_steps, thresh, check):
    rng = np.random.default_rng(seed)
    torch.manual_seed(seed)
    S = rng.choice(d, size=k, replace=False)
    net = nn.Sequential(nn.Linear(d, width), nn.ReLU(), nn.Linear(width, 2))
    opt = torch.optim.SGD(net.parameters(), lr=lr, momentum=0.9)
    loss_fn = nn.CrossEntropyLoss()
    # a fixed held-out test set, drawn once
    xt, yt = make_batch(np.random.default_rng(seed + 10_000), d, S, 4096)
    for t in range(1, max_steps + 1):
        x, y = make_batch(rng, d, S, batch)
        opt.zero_grad()
        loss_fn(net(x), y).backward()
        opt.step()
        if t % check == 0 or t == max_steps:
            with torch.no_grad():
                acc = (net(xt).argmax(1) == yt).float().mean().item()
            if acc >= thresh:
                return t
    return None  # did not reach the threshold within the budget


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=3)
    ap.add_argument("--dims", type=int, nargs="+", default=[15, 20, 25, 30])
    ap.add_argument("--seeds", type=int, default=5)
    ap.add_argument("--width", type=int, default=512)
    ap.add_argument("--batch", type=int, default=512)
    ap.add_argument("--lr", type=float, default=0.05)
    ap.add_argument("--max-steps", type=int, default=40_000)
    ap.add_argument("--thresh", type=float, default=0.90)
    ap.add_argument("--check", type=int, default=10)
    ap.add_argument("--out", type=str, default="sparse_parity_results.json")
    a = ap.parse_args()

    rows = []
    for d in a.dims:
        got = []
        for s in range(a.seeds):
            t = steps_to_learn(d, a.k, 1000 * d + s, a.width, a.batch,
                               a.lr, a.max_steps, a.thresh, a.check)
            got.append(t)
            sys.stderr.write(f"d={d} seed={s} steps={t}\n")
        solved = [t for t in got if t is not None]
        rows.append(dict(d=d, k=a.k, steps=got, samples=[t*a.batch if t else None for t in got],
                         median=(float(np.median(solved)) if solved else None),
                         solved=len(solved), total=a.seeds))

    # power-law fit over dimensions where the median is defined
    xs = [np.log(r["d"]) for r in rows if r["median"]]
    ys = [np.log(r["median"]) for r in rows if r["median"]]
    slope = intercept = None
    if len(xs) >= 2:
        slope, intercept = np.polyfit(xs, ys, 1)

    result = dict(k=a.k, width=a.width, batch=a.batch, lr=a.lr,
                  max_steps=a.max_steps, thresh=a.thresh, rows=rows,
                  loglog_slope=(float(slope) if slope is not None else None),
                  loglog_intercept=(float(intercept) if intercept is not None else None))
    open(a.out, "w").write(json.dumps(result, indent=2))
    sys.stderr.write(f"\nfitted log-log slope (steps ~ d^slope): {slope}\n")
    print(json.dumps({k: result[k] for k in ("k", "loglog_slope")}))


if __name__ == "__main__":
    main()
