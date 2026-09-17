# -*- coding: utf-8 -*-
"""Figure: what spatial language an aperture can carry.

Writes figures/Figure_Aperture.pdf (Fig. 3 of Sec. II-C).

Sec. II-C previously instantiated its aperture argument at exactly one
configuration -- AWR1843, B = 3 GHz, R = 5 m, SNR = 15 dB -- which makes the
claim an example rather than a bound.  This figure generalises it over the
(M, R) plane so a reader can locate their own instrument and read off the
finest relational descriptor its aperture supports.

Panel (a): two-target Rayleigh cross-range resolution, the bound on language
that SEPARATES objects.
    delta_x = R * theta_3dB,   theta_3dB ~= 2/M rad for a lambda/2 ULA

Panel (b): single-target cross-range CRLB at the stated SNR, the bound on
language that PLACES one object, equation (8).
    sigma_x = R * sqrt(6 / (SNR pi^2 cos^2(theta) M (M^2 - 1)))

The order-of-magnitude gap between the panels is the resolution-versus-accuracy
distinction of Table IV, drawn rather than tabulated.

Run: python make_fig_aperture.py
"""
import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.normpath(os.path.join(HERE, "..", "DOC", "images"))
os.makedirs(OUT_DIR, exist_ok=True)
OUT = os.path.join(OUT_DIR, "Figure_3_Aperture.pdf")
OUT_PNG = os.path.join(OUT_DIR, "Figure_3_Aperture.png")

SNR_DB = 15.0
SNR = 10.0 ** (SNR_DB / 10.0)

# Language classes, coarsest first.  Each is the finest relational descriptor
# a given cross-range scale can support; the wording matches Table IV.
BANDS = [
    (2.00, np.inf, "#d8dee9", "no relational spatial language"),
    (0.50, 2.00, "#bcd2e8", "person-scale: ``two people apart''"),
    (0.10, 0.50, "#91b7d9", "furniture-scale: ``chair by the wall''"),
    (0.00, 0.10, "#5d8fc0", "object-scale: ``cup beside the laptop''"),
]

M_MARK = [2, 8, 16, 86, 192]
RANGES = [1.0, 2.0, 5.0, 10.0]


def rayleigh(M, R):
    return R * (2.0 / M)


def crlb(M, R, theta=0.0):
    M = np.asarray(M, dtype=float)
    var = 6.0 / (SNR * math.pi ** 2 * math.cos(theta) ** 2 * M * (M ** 2 - 1.0))
    return R * np.sqrt(var)


def panel(ax, fn, title, ylab):
    M = np.logspace(math.log10(2), math.log10(256), 400)
    for lo, hi, col, _ in BANDS:
        ax.axhspan(max(lo, 1e-4), min(hi, 1e2), color=col, zorder=0, lw=0)
    for R, ls in zip(RANGES, ["-", "--", "-.", ":"]):
        ax.plot(M, fn(M, R), ls, color="#11223a", lw=1.5, zorder=3,
                label="$R$ = %g m" % R)
    for m in M_MARK:
        ax.axvline(m, color="#55606e", lw=0.6, ls=(0, (1, 2)), zorder=1)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(2, 256)
    ax.set_ylim(1e-3, 3e1)
    ax.set_xticks(M_MARK)
    ax.set_xticklabels([str(m) for m in M_MARK])
    ax.set_xlabel("azimuth aperture $M_{\\mathrm{az}}$ "
                  "($\\lambda/2$ elements)")
    ax.set_ylabel(ylab)
    ax.set_title(title, fontsize=9, pad=4)
    ax.grid(True, which="major", axis="y", color="white", lw=0.5, alpha=0.6)
    ax.tick_params(labelsize=7.5)
    ax.xaxis.label.set_size(8)
    ax.yaxis.label.set_size(8)


def main():
    plt.rcParams.update({"font.family": "serif", "font.size": 8,
                         "axes.linewidth": 0.7, "text.usetex": False})
    fig, axes = plt.subplots(1, 2, figsize=(7.1, 3.05), sharey=True)

    panel(axes[0], rayleigh,
          "(a) Rayleigh two-target resolution $\\Delta x = R\\,\\theta_{3\\mathrm{dB}}$\n"
          "bounds language that $\\mathit{separates}$",
          "cross-range scale (m)")
    panel(axes[1], crlb,
          "(b) single-target CRLB $\\sigma_x$ at SNR = 15 dB\n"
          "bounds language that $\\mathit{places}$",
          "")

    # the single-chip operating point quoted in Sec. II-C
    axes[0].plot([8], [rayleigh(8, 5.0)], "o", ms=5, color="#b5292f", zorder=5)
    axes[0].annotate("1.25 m at $R$ = 5 m", xy=(8, rayleigh(8, 5.0)),
                     xytext=(11, 4.2), fontsize=7, color="#b5292f",
                     arrowprops=dict(arrowstyle="-", lw=0.6, color="#b5292f"))
    axes[1].plot([8], [crlb(8, 5.0)], "o", ms=5, color="#b5292f", zorder=5)
    axes[1].annotate("3.1 cm at $R$ = 5 m", xy=(8, crlb(8, 5.0)),
                     xytext=(2.6, 0.0022), fontsize=7, color="#b5292f",
                     arrowprops=dict(arrowstyle="-", lw=0.6, color="#b5292f"))

    for ax in axes:
        ax.annotate("single\nchip", xy=(8, 2.1e1), fontsize=6.5,
                    color="#55606e", ha="center", va="top")
        ax.annotate("cascade", xy=(86, 2.1e1), fontsize=6.5,
                    color="#55606e", ha="center", va="top")

    handles = [Line2D([], [], color="#11223a", lw=1.5, ls=ls,
                      label="$R$ = %g m" % R)
               for R, ls in zip(RANGES, ["-", "--", "-.", ":"])]
    handles += [Patch(facecolor=c, label=lab) for _, _, c, lab in BANDS[::-1]]
    fig.legend(handles=handles, loc="lower center", ncol=4, fontsize=7,
               frameon=False, bbox_to_anchor=(0.5, -0.16),
               handlelength=1.8, columnspacing=1.2)

    fig.tight_layout()
    fig.savefig(OUT, bbox_inches="tight", pad_inches=0.02)
    fig.savefig(OUT_PNG, bbox_inches="tight", pad_inches=0.02, dpi=300)
    print("wrote %s and %s" % (OUT, OUT_PNG))
    for m in M_MARK:
        print("  M=%3d  R=5m:  Rayleigh %7.3f m   CRLB %7.4f m   ratio %5.1f"
              % (m, rayleigh(m, 5.0), crlb(m, 5.0),
                 rayleigh(m, 5.0) / crlb(m, 5.0)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
