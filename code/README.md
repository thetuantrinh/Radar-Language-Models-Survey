# 🧪 Reproducible Code and Metrological Audit Artifacts

This directory contains the single-source-of-truth dataset and reproducible scripts that generate all numbers, tables, and physical derivations for the IEEE Transactions on Instrumentation and Measurement (IEEE TIM) survey:

> **"Radar Signals in the Large Language Era: A Systematic Review of Aperture Bounds, Uncertainty Reporting, and Embedded Deployment"**  
> *The Tuan Trinh, Khoa Nguyen Dang, Xuanque Nguyen, Minhhuy Le\**

---

## 📁 Directory Contents

* **`corpus.py`**: The single source of truth defining the analytical corpus of 51 Radar–Language Model (RLM) frameworks (33 instrumentation-side + 18 microwave remote-sensing / SAR frameworks), including Abstraction Level ($L1$–$L4$), Alignment Mechanism ($M1$–$M4b$), Task Class ($T1$–$T6$), and RF hardware specifications.
* **`prisma_assessment.csv`**: The complete PRISMA 2020 screening and eligibility audit log across 360 examined records, documenting stage counts and explicit inclusion/exclusion decisions under criteria (i)–(iv).
* **`corpus_meta.json`**: Bibliographical metadata (DOIs, titles, authors, venues, volumes) retrieved directly from OpenAlex and CrossRef for the audited corpus.
* **`reproduce_tables.py`**: Emits the complete Markdown format of Table II (all 51 included systems) and the $L \times M$ coverage matrix with marginal distributions.
* **`emit_gum.py`**: Computes the worked GUM (JCGM 100:2008) uncertainty budget for relative permittivity estimation ($\epsilon_r = 4$, $\Gamma = -0.333$) at 77 GHz, demonstrating expanded uncertainty $U_{95} = 1.59$ under single-frame measurement.
* **`taxonomy_null.py`**: Implements the permutation null hypothesis test ($3 \times 10^5$ replicates) preserving marginal distributions, proving that coverage matrix sparsity is an artifact of marginals ($P = 0.435$) while the association between abstraction level and alignment mechanism is statistically significant ($P = 0.0002$, Cramér's $V = 0.45$).
* **`make_fig_aperture.py`**: Generates the cross-range physical aperture bounds plot comparing single-target CRLB precision with two-target Rayleigh beamforming separation across array apertures ($M_{\mathrm{az}}$) and standoff distances ($R$).
* **`requirements.txt`**: Minimal Python dependencies (`numpy`, `scipy`, `matplotlib`, `tabulate`).

---

## 🚀 Reproduction Instructions

### 1. Environment Setup

```bash
git clone https://github.com/thetuantrinh/Radar-Language-Models-Survey.git
cd Radar-Language-Models-Survey/code
pip install -r requirements.txt
```

### 2. Generate Coverage Matrix & Corpus Tables

```bash
python reproduce_tables.py
```

### 3. Run Permutation Null Test on Taxonomy Matrix

```bash
python taxonomy_null.py
```

### 4. Compute Worked GUM Permittivity Uncertainty Budget

```bash
python emit_gum.py
```

### 5. Generate Aperture Bounds Plot

```bash
python make_fig_aperture.py
```
