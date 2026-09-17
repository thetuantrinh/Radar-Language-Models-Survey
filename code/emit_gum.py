# -*- coding: utf-8 -*-
"""Worked GUM uncertainty budget for a permittivity measurand.

Writes sections/gum_budget.tex (Table: the minimum viable budget of Sec. IV-B).

Sec. IV-B reports that no surveyed framework publishes an uncertainty budget.
That finding invites the obvious question -- what would one contain? -- and the
answer is short enough that its absence is hard to excuse.  This script works
it through for the measurand a corpus framework actually reports and
serializes into a prompt: the relative permittivity that LLMaterial infers
from the Fresnel reflection coefficient.

Model (Sec. II-B):
    Gamma  = (1 - sqrt(eps_r)) / (1 + sqrt(eps_r))
    eps_r  = ((1 - Gamma) / (1 + Gamma))**2
    d eps_r / d Gamma = -4 (1 - Gamma) / (1 + Gamma)**3

Every number in the emitted table is computed here.  Nothing is typed into the
LaTeX, for the same reason nothing else in this manuscript is.

Run: python emit_gum.py
"""
import io
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))

# ---- operating point: the configuration of Table IV --------------------
EPS_R = 4.0            # measurand value, a representative low-loss dielectric
SNR_DB = 15.0          # post-integration, single-target, in the cell under test
F_C = 77e9             # carrier, Hz
C = 299_792_458.0
N_FRAMES = 16          # coherent frames averaged in the second column
R_STANDOFF = 0.50      # m, target standoff for the material measurement
U_R = 0.01             # m, standoff known to +/- 1 cm  (rectangular)
U_CAL_DB = 0.5         # reference-reflector RCS stated to +/- 0.5 dB (rect.)
THETA_MIS_DEG = 5.0    # incidence alignment, +/- 5 deg  (rectangular)
SIGMA_H = 100e-6       # surface roughness RMS height, m


def gamma_of(eps):
    return (1.0 - math.sqrt(eps)) / (1.0 + math.sqrt(eps))


def eps_of(g):
    return ((1.0 - g) / (1.0 + g)) ** 2


def sens(g):
    """|d eps_r / d Gamma|, equation (11)."""
    return abs(4.0 * (1.0 - g) / (1.0 + g) ** 3)


def budget():
    g = gamma_of(EPS_R)
    snr = 10.0 ** (SNR_DB / 10.0)

    # --- Type A: thermal noise on the coherent amplitude estimate.
    # For a deterministic signal in complex Gaussian noise the ML amplitude
    # estimate has u(A)/A = 1/sqrt(2 SNR); averaging N independent frames
    # divides by sqrt(N).  Gamma is proportional to that amplitude ratio.
    rel_noise_1 = 1.0 / math.sqrt(2.0 * snr)
    rel_noise_n = rel_noise_1 / math.sqrt(N_FRAMES)

    # --- Type B: calibration transfer from the reference reflector.
    # A rectangular +/- U_CAL_DB on RCS is +/- U_CAL_DB/2 dB in amplitude.
    rel_cal = (10.0 ** (U_CAL_DB / 20.0) - 1.0) / math.sqrt(3.0)

    # --- Type B: range normalisation.  Amplitude goes as R^-2, so a relative
    # range error propagates with a factor of two.
    rel_range = 2.0 * (U_R / R_STANDOFF) / math.sqrt(3.0)

    # --- Type B: incidence-angle misalignment.  Normal incidence is a
    # stationary point of cos(theta), so a +/- 5 deg error is second order --
    # which is exactly the sort of term a budget makes visible and intuition
    # gets wrong.
    rel_theta = (1.0 - math.cos(math.radians(THETA_MIS_DEG))) / math.sqrt(3.0)

    rows = []
    for label, rel, typ, dist, note in [
        (r"Thermal noise on amplitude, single frame", rel_noise_1, "A",
         "Normal", r"$1/\sqrt{2\,\mathrm{SNR}}$ at \SNRDB"),
        (r"Calibration transfer, reference reflector", rel_cal, "B",
         "Rect.", r"$\pm$\UCALDB\ on reference RCS"),
        (r"Range normalisation ($A \propto R^{-2}$)", rel_range, "B",
         "Rect.", r"$\pm$1\,cm at \RSTAND"),
        (r"Incidence-angle misalignment", rel_theta, "B",
         "Rect.", r"$\pm$\THETAMIS; second order at normal incidence"),
    ]:
        rows.append((label, typ, dist, rel, abs(rel * g), note))

    uc_g_1 = math.sqrt(sum(r[4] ** 2 for r in rows))
    uc_g_n = math.sqrt(
        (rel_noise_n * abs(g)) ** 2
        + sum(r[4] ** 2 for r in rows[1:]))
    s = sens(g)

    # --- surface roughness: a one-sided BIAS, not an uncertainty.
    k = 2.0 * math.pi * F_C / C
    rho = math.exp(-2.0 * (k * SIGMA_H) ** 2)
    g_rough = g * rho          # |Gamma| attenuated, Gamma here is negative
    bias = eps_of(g_rough) - EPS_R

    return dict(g=g, s=s, rows=rows, uc_g_1=uc_g_1, uc_g_n=uc_g_n,
                uc_e_1=s * uc_g_1, uc_e_n=s * uc_g_n,
                U_1=2.0 * s * uc_g_1, U_n=2.0 * s * uc_g_n,
                rel_noise_1=rel_noise_1, rel_noise_n=rel_noise_n,
                rho=rho, bias=bias, k=k)


def main():
    b = budget()
    sub = {
        r"\SNRDB": "%g\\,dB" % SNR_DB,
        r"\UCALDB": "%g\\,dB" % U_CAL_DB,
        r"\RSTAND": "%g\\,m" % R_STANDOFF,
        r"\THETAMIS": "%g$^\\circ$" % THETA_MIS_DEG,
    }

    def fix(s):
        for k, v in sub.items():
            s = s.replace(k, v)
        return s

    L = [r"\begin{table}[t]",
         r"	\centering",
         r"	\scriptsize",
         r"	\renewcommand{\arraystretch}{1.15}",
         r"	\rowcolors{2}{bluerow}{white}",
         r"	\caption{Worked GUM Budget for the Permittivity Measurand "
         r"of \cite{zhu2025identify} at $\epsilon_r = %.0f$, $\Gamma = %.3f$, "
         r"and the Operating Point of \autoref{tab:semantic_limits}; "
         r"Sensitivity $|\partial \epsilon_r / \partial \Gamma| = %.1f$ "
         r"\eqref{eq:sigma_eps}.}" % (EPS_R, b["g"], b["s"]),
         r"	\label{tab:gum_budget}",
         r"	\begin{tabularx}{\columnwidth}{",
         r"			>{\RaggedRight\arraybackslash}X",
         r"			>{\centering\arraybackslash}p{0.62cm}",
         r"			>{\centering\arraybackslash}p{0.70cm}",
         r"			>{\raggedleft\arraybackslash}p{1.15cm}",
         r"			>{\raggedleft\arraybackslash}p{1.15cm}}",
         r"		\hline",
         r"		\rowcolor{bluehead}",
         r"		\textbf{Uncertainty component} & \textbf{Type} & "
         r"\textbf{Distr.} & \textbf{Rel.\%} & "
         r"\textbf{$u(\Gamma)$} \\",
         r"		\hline"]
    for label, typ, dist, rel, ug, note in b["rows"]:
        L.append("		%s & %s & %s & %.2f & %.4f \\\\"
                 % (fix(label), typ, dist, 100.0 * rel, ug))
    L += [r"		\hline",
          r"		\textbf{Combined, single frame} & & & & "
          r"\textbf{%.4f} \\" % b["uc_g_1"],
          r"		\textbf{Combined, %d frames averaged} & & & & "
          r"\textbf{%.4f} \\" % (N_FRAMES, b["uc_g_n"]),
          r"		\hline",
          r"		\multicolumn{5}{l}{\cellcolor{blueA}\textbf{Propagated to "
          r"the measurand}} \\",
          r"		\hline",
          r"		Combined standard uncertainty $u_c(\epsilon_r)$, single "
          r"frame & & & & %.2f \\" % b["uc_e_1"],
          r"		Expanded $U_{95} = 2u_c$, single frame & & & & "
          r"\textbf{%.2f} \\" % b["U_1"],
          r"		Combined $u_c(\epsilon_r)$, %d frames & & & & %.2f \\"
          % (N_FRAMES, b["uc_e_n"]),
          r"		Expanded $U_{95} = 2u_c$, %d frames & & & & \textbf{%.2f} \\"
          % (N_FRAMES, b["U_n"]),
          r"		\hline",
          r"		\multicolumn{5}{l}{\cellcolor{blueA}\textbf{Known bias, "
          r"reported separately}} \\",
          r"		\hline",
          r"		Surface roughness, $\sigma_h = %g$\,\textmu m, "
          r"$\rho_{\mathrm{rough}} = %.3f$ & B & --- & --- & "
          r"$%+.2f$ \\" % (SIGMA_H * 1e6, b["rho"], b["bias"]),
          r"		\hline",
          r"		\multicolumn{5}{p{\dimexpr\columnwidth-2\tabcolsep}}"
          r"{\footnotesize Columns 4 and 5 give each component as a relative "
          r"standard uncertainty on the measured amplitude and as its "
          r"contribution to $u(\Gamma)$. Type~A is evaluated statistically, "
          r"Type~B otherwise \cite{jcgm100}. \textbf{Read the two rows in "
          r"bold against each other}: at one frame the budget is noise "
          r"dominated, and averaging %d frames moves the dominant term to "
          r"calibration transfer, so a budget of this kind tells the "
          r"experimenter which term to attack next---which is what a single "
          r"accuracy figure cannot do. Roughness is listed apart because it "
          r"is one-sided: $\rho_{\mathrm{rough}} \le 1$ can only attenuate "
          r"the specular return, so an uncompensated rough surface can only "
          r"\emph{under}-estimate $\epsilon_r$, never over-estimate it. "
          r"Because the model is markedly non-linear near $\Gamma = -1$, the "
          r"first-order propagation used here should be replaced by the Monte "
          r"Carlo method of \cite{jcgm101} for conductive media "
          r"(\autoref{sec:phys_extraction}).} \\" % N_FRAMES,
          r"		\hline",
          r"	\end{tabularx}",
          r"\end{table}"]

    out_path = os.path.join(HERE, "gum_budget.tex")
    io.open(out_path, "w", encoding="utf8").write("\n".join(L) + "\n")

    print("Gamma = %.4f, sensitivity |d eps/d Gamma| = %.2f" % (b["g"], b["s"]))
    print("  u_c(Gamma) 1 frame  = %.4f -> u_c(eps) = %.3f, U95 = %.2f"
          % (b["uc_g_1"], b["uc_e_1"], b["U_1"]))
    print("  u_c(Gamma) %2d frames = %.4f -> u_c(eps) = %.3f, U95 = %.2f"
          % (N_FRAMES, b["uc_g_n"], b["uc_e_n"], b["U_n"]))
    print("  interval, single frame: %.2f to %.2f"
          % (EPS_R - b["U_1"], EPS_R + b["U_1"]))
    print("  roughness rho = %.4f -> bias %+.3f in eps_r" % (b["rho"], b["bias"]))
    print("wrote gum_budget.tex")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
