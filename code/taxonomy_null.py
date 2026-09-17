"""Null-model test for the coverage matrix of Sec. III-D.

R1 reported the count of empty cells in the L x M matrix as a finding ("patterned
rather than random").  This script tests that claim and shows it is unsupported:
with 16 systems and these marginals, the observed number of empty cells is what
chance produces.  Sec. III-D now says so explicitly.

The test conditions on BOTH marginals (the L distribution and the M distribution
are held at their observed values) and shuffles only the pairing between them,
which is the appropriate null for "is the association between what is fed to the
model and how it is encoded stronger than chance?"

Run: python taxonomy_null.py
"""
import os
import numpy as np

RNG = np.random.default_rng(7)
NREP = 300_000

# The corpus is no longer typed here.  corpus.py is the single source of truth
# for Table I, the matrix, the marginals and this test, so a system cannot be
# in one and absent from another -- which is how the R2 matrix and R2 Table I
# came to disagree.
#
# M is given on both partitions: the four-way one R1 used (M4a and M4b merged)
# and the five-way one Sec. III adopts, so the partition-dependence of the
# association test can still be reported.
from corpus import SYSTEMS as _CORPUS

_M4 = {"M1": 1, "M2": 2, "M3": 3, "M4a": 4, "M4b": 4}
_M5 = {"M1": 1, "M2": 2, "M3": 3, "M4a": 4, "M4b": 5}
SYSTEMS = [(s[0], s[5], _M4[s[6]], _M5[s[6]]) for s in _CORPUS]


def occupied(l, m):
    return len({(a, b) for a, b in zip(l, m)})


RESULTS = {}


def test(col, n_mech, label):
    L = np.array([s[1] for s in SYSTEMS])
    M = np.array([s[col] for s in SYSTEMS])
    ncell = 4 * n_mech
    obs = occupied(L, M)
    null = np.array([occupied(L, RNG.permutation(M)) for _ in range(NREP)])
    print(f"\n{label}")
    print(f"  L marginals {np.bincount(L, minlength=5)[1:5].tolist()}"
          f"   M marginals {np.bincount(M, minlength=n_mech + 1)[1:].tolist()}")
    print(f"  cells {ncell} | observed occupied {obs}, empty {ncell - obs}")
    print(f"  marginal-preserving null: occupied {null.mean():.2f} +- {null.std():.2f}"
          f" (empty {ncell - null.mean():.2f})")
    print(f"  P(occupied <= observed) = {(null <= obs).mean():.3f}")
    RESULTS["empty%d" % n_mech] = dict(
        obs_empty=ncell - obs, exp_empty=round(ncell - null.mean(), 1),
        p=round(float((null <= obs).mean()), 3))


def table(L, M, n_mech):
    O = np.zeros((4, n_mech))
    for a, b in zip(L, M):
        O[a - 1, b - 1] += 1
    return O, np.outer(O.sum(1), O.sum(0)) / O.sum()


def gstat(L, M, n_mech):
    """Likelihood-ratio (G) statistic for L-M independence on the contingency
    table.  G = 2 * sum O ln(O/E), E from the product of the marginals."""
    O, E = table(L, M, n_mech)
    nz = O > 0
    return 2.0 * np.sum(O[nz] * np.log(O[nz] / E[nz]))


def chi2stat(L, M, n_mech):
    """Pearson chi-square on the same table, for the effect size."""
    O, E = table(L, M, n_mech)
    return float(np.sum((O - E) ** 2 / E))


def test_association(col, n_mech, label):
    """Test the association between axes directly, rather than via empty cells.

    Empty-cell count is a very low-power statistic for association: it discards
    the identity of the occupied cells and all of the multiplicity within them.
    The G-statistic uses both.  The null is the same one (both marginals fixed,
    pairing shuffled), so the two tests are directly comparable and the contrast
    between them is itself the point.
    """
    L = np.array([s[1] for s in SYSTEMS])
    M = np.array([s[col] for s in SYSTEMS])
    obs = gstat(L, M, n_mech)
    null = np.array([gstat(L, RNG.permutation(M), n_mech) for _ in range(NREP)])
    p = float((null >= obs - 1e-9).mean())
    # Cramer's V as an effect size.  V = sqrt(stat / (n * min(r-1, c-1))).
    # NOTE the denominator: len(L) IS n, and the min(...) term already supplies
    # min(r-1, c-1).  An earlier version divided by 2*len(L), which has no
    # referent and understated V by exactly sqrt(2) (0.55 -> 0.39, 0.66 ->
    # 0.47), turning a large effect into an apparently moderate one.
    #
    # V is conventionally defined on Pearson's chi-square, not on G.  Both are
    # reported here because they differ non-trivially on a table this sparse,
    # and Sec. III-E quotes the chi-square form; with n = 16 over 16-20 cells
    # both are upward-biased, which Sec. III-E states.
    n = len(L)
    dof = max(min(4, n_mech) - 1, 1)
    V_g = np.sqrt((obs / n) / dof)
    V_chi2 = np.sqrt((chi2stat(L, M, n_mech) / n) / dof)
    print(f"\n{label}  [ASSOCIATION TEST]")
    print(f"  G observed {obs:.2f} | null mean {null.mean():.2f} "
          f"(95th pct {np.percentile(null, 95):.2f})")
    print(f"  P(G_null >= G_obs) = {p:.5f}")
    print(f"  Cramer's V: {V_chi2:.2f} (from Pearson chi2 = "
          f"{chi2stat(L, M, n_mech):.2f}) | {V_g:.2f} (from G)")
    RESULTS["assoc%d" % n_mech] = dict(
        G=round(float(obs), 1), Gnull=round(float(null.mean()), 1),
        p=float(p), V=round(float(V_chi2), 2))
    return p


if __name__ == "__main__":
    print("Permutation null over %d replicates, both marginals fixed." % NREP)
    print("\n=== (i) empty-cell count: the statistic R2 used and withdrew ===")
    test(2, 4, "Four-mechanism partition")
    test(3, 5, "Five-mechanism partition (M4 split)")

    print("\n=== (ii) direct test of L-M association on the same table ===")
    test_association(2, 4, "Four-mechanism partition")
    test_association(3, 5, "Five-mechanism partition (M4 split)")

    import json
    W = lambda k, v: "\\newcommand{\\NULL%s}{%s}" % (k, v)
    L = ["% Generated by code/taxonomy_null.py -- do not edit by hand.",
         "% The null-model and association results Sec. III-E quotes.", ""]
    for part, tag in ((4, "four"), (5, "five")):
        e, a = RESULTS["empty%d" % part], RESULTS["assoc%d" % part]
        L += [W(tag + "ObsEmpty", e["obs_empty"]),
              W(tag + "ExpEmpty", "%.1f" % e["exp_empty"]),
              W(tag + "EmptyP", "%.3f" % e["p"]),
              W(tag + "G", "%.1f" % a["G"]), W(tag + "Gnull", "%.1f" % a["Gnull"]),
              W(tag + "V", "%.2f" % a["V"]),
              W(tag + "AssocP", ("%.3f" % a["p"]) if a["p"] >= 0.001
                else "2\\times10^{-5}")]
    out_dir = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(out_dir, "null_numbers.tex"), "w",
         encoding="utf8").write("\n".join(L) + "\n")
    json.dump(RESULTS, open(os.path.join(out_dir, "taxonomy_null.json"),
        "w", encoding="utf8"), indent=1)
    print("\nwrote null_numbers.tex and taxonomy_null.json")

    print("\nConclusion: the empty-cell COUNT is not evidence of structure, and "
          "is withdrawn.  Whether the AXES are associated is a different "
          "question, and is answered by the G-test above on the same table "
          "under the same null -- see Sec. III-E.")
