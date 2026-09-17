#!/usr/bin/env python3
"""Figure: median steps-to-learn a hidden 3-sparse parity against dimension,
log-log, with the fitted power law. One panel, one message."""
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

r = json.load(open("canonical_b128.json"))
d = np.array([row["d"] for row in r["rows"]])
med = np.array([row["median"] for row in r["rows"]], dtype=float)
lo = np.array([np.min(row["steps"]) for row in r["rows"]], dtype=float)
hi = np.array([np.max(row["steps"]) for row in r["rows"]], dtype=float)
slope, intercept = r["loglog_slope"], r["loglog_intercept"]

fig, ax = plt.subplots(figsize=(4.6, 3.4))
ax.errorbar(d, med, yerr=[med - lo, hi - med], fmt="o", color="black",
            capsize=3, markersize=5, lw=1,
            label="median over 8 seeds (range as bars)")
xs = np.linspace(d.min(), d.max(), 100)
ax.plot(xs, np.exp(intercept) * xs**slope, "--", color="black", lw=1,
        label=rf"fit: $t_c \propto d^{{{slope:.2f}}}$")
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xticks(d); ax.set_xticklabels([str(x) for x in d])
ax.minorticks_off()
ax.set_xlabel(r"input dimension $d$")
ax.set_ylabel(r"SGD steps to $90\%$ test accuracy")
ax.legend(frameon=False, fontsize=8)
fig.tight_layout()
fig.savefig("../figures/parity-scaling.pdf")
print("wrote ../figures/parity-scaling.pdf")
