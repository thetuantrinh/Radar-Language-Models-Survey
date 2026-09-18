# 🧪 Code & Metrological Audit Artifacts

> **Status**: **Coming Soon** ⏳  
> The complete reproduction codebase, PRISMA evaluation datasets, and metrological audit scripts will be made publicly available here upon publication / acceptance of our survey paper:

---

## 📦 Planned Release Artifacts

Upon acceptance and publication, the following artifacts and reproducibility tools will be released in this directory:

* **Analytical Corpus (`corpus.py`, `corpus_meta.json`)**:
  The complete single-source-of-truth dataset defining all 51 evaluated Radar–Language Model (RLM) frameworks (33 instrumentation-side + 18 microwave remote-sensing / SAR frameworks), including Abstraction Level ($L1$–$L4$), Alignment Mechanism ($M1$–$M4b$), Task Class ($T1$–$T6$), hardware specifications, and bibliographical metadata.

* **PRISMA 2020 Systematic Assessment Log (`prisma_assessment.csv`)**:
  Full evaluation decisions across all 360 screened candidate papers documenting stage counts and explicit inclusion/exclusion rationales under criteria (i)–(iv).

* **Taxonomy Permutation Null Test (`taxonomy_null.py`)**:
  Stratified Monte Carlo permutation test routine ($3 \times 10^5$ replicates) preserving marginal distributions, evaluating coverage matrix sparsity and cross-modal association significance ($P = 0.0002$, Cramér's $V = 0.45$).

* **GUM Permittivity Uncertainty Budget (`emit_gum.py`)**:
  Worked JCGM 100:2008 metrological uncertainty budget calculation for 77 GHz relative permittivity estimation, establishing expanded uncertainty bounds ($U_{95} = 1.59$).

* **Table & Figure Reproduction Tools (`reproduce_tables.py`, `make_fig_aperture.py`)**:
  Automated scripts to regenerate Table II, the $L \times M$ coverage matrix with marginal distributions, and physical Rayleigh-vs-CRLB aperture resolution curves.
