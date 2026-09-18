# 📡 Radar Signals in the Large Language Era: A Systematic Review of Aperture Bounds, Uncertainty Reporting, and Embedded Deployment

[![IEEE Transactions on Instrumentation and Measurement](https://img.shields.io/badge/IEEE%20TIM-Survey%20Manuscript-blue.svg)](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=19)
[![Audited Frameworks](https://img.shields.io/badge/Audited%20Frameworks-51%20Total%20(33%20Inst%20%2B%2018%20SAR)-green.svg)](#-the-three-axis-taxonomy--coverage-matrix)
[![PRISMA 2020 Protocol](https://img.shields.io/badge/PRISMA%202020-Guided%20Retrieval-orange.svg)](#-system-architecture--prisma-methodology)
[![Reproducibility](https://img.shields.io/badge/Code%20%26%20Data-Coming%20Soon-yellow.svg)](./code)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

**Official repository** for the IEEE Transactions on Instrumentation and Measurement (IEEE TIM) survey manuscript:  
**"Radar Signals in the Large Language Era: A Systematic Review of Aperture Bounds, Uncertainty Reporting, and Embedded Deployment"**

---

## 📌 Abstract

Radar instrumentation measures range, Doppler velocity, angle of arrival, and material dielectric properties through adverse environments without optical privacy intrusion. Coupling radar signal processing chains to language models turns fixed-dictionary classifiers into open-vocabulary measurement systems. We systematically audit **51 radar-language frameworks** retrieved under a PRISMA-guided protocol from 1,600+ records (2020–2026), evaluating signal representations ($L1$–$L4$), cross-modal alignment mechanisms ($M1$–$M4b$), and measurement task classes ($T1$–$T6$). Four findings emerge:

1. **The 63.6% L2a Collapse**: Of the 33 instrumentation-side frameworks whose authors held coherent data, **63.6% (21/33)** still collapse the backscatter tensor into a 2D product to reuse optical vision encoders (CLIP, LLaVA, ViT), permanently discarding phase coherence ($2\pi f_c \tau_m$) and polarimetric fidelity.
2. **Aperture Bounds vs. RF Bandwidth**: Under conventional beamforming, descriptive spatial granularity is strictly bounded by array aperture rather than RF bandwidth ($1.3\,\text{m}$ azimuth against $5\,\text{cm}$ range resolution at $5\,\text{m}$ on single-chip MIMO arrays); a bound subspace superresolution relaxes only at an SNR and snapshot cost no surveyed framework reports. Resolvable state capacity ($N_{\mathrm{states}} \propto B f_c M T_{\mathrm{obs}}$) governs spatial detail and biometric identifiability alike.
3. **The 0/51 Reporting Gap (Uncertainty & Calibration)**: Under a 4-item rubric, **no surveyed framework** reports a GUM-compliant uncertainty budget, calibration standard/residual, phase-noise tolerance, or input SNR sensitivity curve on a physical measurand, and none propagates input SNR to the semantic output. We provide a worked GUM budget for permittivity inference ($\epsilon_r = 4$, $U_{95} = 1.59$) as the minimum viable template.
4. **Embedded Edge Feasibility**: Contrastive alignment ($M1$, 9 frameworks) is the **only paradigm admitting decoder-free microcontroller deployment** against precomputed label dictionaries, whereas run-time open-vocabulary querying requires edge GPUs—and no framework reports measured on-device latency, memory, or energy. We propose standardized dual-axis evaluation protocols to anchor cognitive radar in measurement science.

**Index Terms**— *Embedded deployment, frequency-modulated continuous wave (FMCW) radar, large language models, measurement uncertainty, radar signal processing, systematic review.*

---

## 🗺️ System Architecture & PRISMA Methodology

* **Pipeline Architecture**: The radar-to-language processing pipeline spans three orthogonal taxonomy axes: abstraction level ($L1$–$L4$), cross-modal alignment mechanism ($M1$–$M4b$), and task class ($T1$–$T6$).
* **PRISMA 2020 Protocol**: Systematic retrieval from OpenAlex (2020–2026), two-pass automated screening, eligibility assessment on criteria (i)–(iv), and the final 51 included RLM frameworks.
* **Physical Aperture Bounds**: Cross-range scale against azimuth aperture $M_{\mathrm{az}}$ across standoff distances, establishing the two-target Rayleigh beamforming limit vs. single-target CRLB at $\mathrm{SNR}=15\,\text{dB}$.
* **Traditional Domain Scoping**: Coverage of radar–language instantiations across traditional radar domains against screened background literature, analyzing the concentration in lexical tasks vs continuous regression.
* 
---

## 📊 Comprehensive Benchmark Table: All 51 Audited Radar–Language Frameworks (2024–2026)

*Note: Systems marked **● Yes** were audited at full text; systems marked **○ Abs** were admitted via title/abstract screening under criteria (i)–(iv).*

| System | Venue | Yr | RF Band / Hardware | L | M | T | Primary Measurement Task | Full Text? |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: | :--- | :---: |
| **Instrumentation-Side Frameworks** | | | | | | | | |
| [Talk2Radar](https://arxiv.org/abs/2405.12821) | arXiv + ICRA | 2024 | 77 GHz 4D radar (View-of-Delft) | L3 | M2 | T2 | 3D referring expression comprehension | ● Yes |
| [LLMCount](https://arxiv.org/abs/2409.16209) | arXiv | 2024 | 60/77 GHz (TI IWR6843) | L2 | M4b | T1 | Stationary occupant counting | ● Yes |
| [RadarLLM-Motion](https://arxiv.org/abs/2504.09862) | arXiv + AAAI | 2025 | 60 GHz FMCW / POI synthesis | L3 | M3 | T3 | Human motion understanding | ● Yes |
| [RadarPLM-Marine](https://arxiv.org/abs/2509.12089) | arXiv + IGARSS | 2025 | 9.4 GHz X-band (IPIX) | L2 | M2 | T1 | Marine target detection | ● Yes |
| [LLMaterial](https://doi.org/10.1145/3714394.3756289) | UbiComp Comp. | 2025 | 77 GHz FMCW (TI AWR1843) | L4 | M4a | T4 | Material identification (εr, RCS) | ● Yes |
| [Robotic-VLM‡](https://doi.org/10.1145/3680207.3765653) | MobiCom poster | 2025 | 77 GHz mmWave + RGB | L4 | M4a | T4 | Robotic material perception | ● Yes |
| [mmPencil](https://doi.org/10.1145/3749504) | ACM IMWUT | 2025 | 60 GHz FMCW (TI IWR6843ISK) | L3 | M1 | T3 | In-air handwriting recognition | ● Yes |
| [WirelessGPT](https://doi.org/10.1109/JSAC.2025.3640156) | IEEE JSAC | 2025 | 28 GHz / sub-6 GHz array | L1 | M2 | T6 | Multi-task ISAC foundation model | ● Yes |
| [MmExpert](https://doi.org/10.1145/3704413.3764420) | ACM MobiHoc | 2025 | 77 GHz FMCW (TI AWR1843) | L2 | M4b | T3 | Data synthesis and action understanding | ● Yes |
| [Radar2Text](https://doi.org/10.1109/IMBioC63524.2025.10989725) | IEEE IMBioC | 2025 | 77 GHz FMCW sensor | L2 | M2 | T3 | Linguistic summarization of signatures | ● Yes |
| [M²BeamLLM](https://arxiv.org/abs/2506.14532) | arXiv | 2025 | 60 GHz (DeepSense 6G) | L2 | M2 | T6 | mmWave beam prediction | ● Yes |
| [EW-Jamming VLM](https://doi.org/10.1109/TAES.2025.3586834) | IEEE TAES | 2025 | 1--18 GHz EW spectrograms | L2 | M1 | T5 | Active jamming recognition | ● Yes |
| [Sig2text](https://arxiv.org/abs/2503.15213) | arXiv + IET RSN | 2025 | 0.5--18 GHz EW receiver | L2 | M2 | T5 | Non-cooperative signal parsing | ● Yes |
| [RFSensingGPT](https://doi.org/10.1109/TCCN.2025.3558069) | IEEE TCCN | 2026 | sub-6 GHz / mmWave 6G | L4 | M4a | T6 | RAG-enhanced sensing orchestration | ● Yes |
| [HRRP-Proto-LLM](https://doi.org/10.1049/icp.2026.1107) | IET RSN | 2026 | X-band HRRP | L2 | M2 | T1 | Few-shot HRRP target recognition | ○ Abs |
| [UWB-LLM](https://doi.org/10.1049/icp.2026.1107) | DOAJ (OA) | 2026 | Impulse UWB | L1 | M2 | T1 | Counting, respiration and ECG | ○ Abs |
| [mmWave-Bench](https://doi.org/10.48550/arxiv.2608.14179) | arXiv | 2026 | mmWave FMCW | L2 | M2 | T3 | LLM benchmark for mmWave understanding | ○ Abs |
| [RadarChat](https://doi.org/10.1016/j.rineng.2026.111637) | IET RSN | 2026 | Multi-band radar | L2 | M4b | T5 | Radar modulation recognition | ○ Abs |
| [mmMind](https://doi.org/10.48550/arxiv.2608.04127) | arXiv | 2026 | mmWave FMCW | L3 | M2 | T3 | Pose-guided behaviour understanding | ○ Abs |
| [SLM-CogRadar](https://doi.org/10.48550/arxiv.2608.11596) | arXiv | 2026 | Synthetic ULA | L1 | M4b | T6 | Language-conditioned array processing | ○ Abs |
| [RAGent](https://doi.org/10.48550/arxiv.2603.27571) | arXiv | 2026 | mmWave FMCW | L2 | M4b | T3 | Training-free mmWave activity recognition | ○ Abs |
| [RadarSigLIP](https://doi.org/10.48550/arxiv.2605.07367) | arXiv | 2026 | 4D radar (K-Radar) | L2 | M1 | T3 | Weather-robust scene captioning | ○ Abs |
| [PReD](https://doi.org/10.48550/arxiv.2603.28183) | arXiv | 2026 | Multi-band EM | L2 | M2 | T5 | EM perception, recognition and decision | ○ Abs |
| [PISPL](https://doi.org/10.3390/rs18142316) | Remote Sens. | 2026 | Low-altitude radar | L2 | M2 | T1 | Few-shot low-altitude target recognition | ○ Abs |
| [LPI-VLM](https://doi.org/10.1038/s41598-025-15411-z) | Sci. Rep. | 2025 | LPI microwave waveforms | L2 | M1 | T5 | Overlapping LPI waveform recognition | ○ Abs |
| [GPR-OFA](https://doi.org/10.1016/j.autcon.2025.105979) | Autom. Constr. | 2025 | Ground-penetrating radar | L2 | M4b | T1 | One-for-all GPR interpretation | ○ Abs |
| [RF-HAR-MLLM](https://doi.org/10.1109/icmac64768.2025.11003262) | IEEE SPL | 2025 | RF sensing | L2 | M2 | T3 | Human activity recognition | ○ Abs |
| [RadarVLM](https://doi.org/10.48550/arxiv.2511.21105) | arXiv | 2025 | Simulated automotive radar | L2 | M2 | T3 | Radar scene understanding | ○ Abs |
| [CSLR-DeepSeek](https://doi.org/10.1109/jsen.2025.3599380) | IEEE Sens. J. | 2025 | mmWave micro-Doppler | L2 | M4a | T3 | Continuous sign-language recognition | ○ Abs |
| [Psyche-Wave](https://doi.org/10.1109/bibm66473.2025.11356898) | IEEE BIBM | 2025 | mmWave SCG | L4 | M4a | T3 | Psychological state decoding | ○ Abs |
| [RestAware](https://doi.org/10.48550/arxiv.2508.00848) | arXiv | 2025 | 24 GHz FMCW | L4 | M4a | T3 | Sleep-posture monitoring and summary | ○ Abs |
| [KEF-HRRP](https://doi.org/10.1016/j.sigpro.2025.110199) | IET RSN | 2025 | HRRP echoes | L2 | M2 | T1 | Knowledge-fused target recognition | ○ Abs |
| [PseudoText-JAM](https://doi.org/10.1117/12.3060944) | IET RSN | 2025 | Radar interference | L2 | M1 | T5 | Few-shot interference recognition | ○ Abs |
| **Microwave Remote-Sensing / SAR Imagery Frameworks** | | | | | | | | |
| [ATRNet-SARCap](https://doi.org/10.1109/JSTARS.2025.3603036) | IEEE JSTARS | 2025 | C/X-band SAR (Gaofen-3) | L2 | M2 | T3 | SAR image captioning | ● Yes |
| [SARLANG-1M](https://doi.org/10.1109/TGRS.2026.3652099) | IEEE TGRS | 2026 | C-band SAR (Sentinel-1) | L2 | M1 | T3 | SAR vision-language understanding | ● Yes |
| [SARCLIP](https://doi.org/10.1109/tgrs.2025.3630131) | IEEE TGRS | 2025 | Spaceborne SAR | L2 | M1 | T3 | SAR vision-language pre-training | ○ Abs |
| [SARVLM](https://doi.org/10.48550/arxiv.2510.22665) | IEEE TGRS | 2025 | Spaceborne SAR | L2 | M2 | T3 | SAR semantic understanding | ○ Abs |
| [SAR-TEXT](https://doi.org/10.48550/arxiv.2507.18743) | arXiv | 2025 | Spaceborne SAR | L2 | M1 | T3 | SAR image--text corpus (130k pairs) | ○ Abs |
| [SAREval](https://doi.org/10.3390/rs18010082) | arXiv | 2025 | Spaceborne SAR | L2 | M2 | T3 | SAR VLM evaluation benchmark | ○ Abs |
| [SSL-LIP](https://doi.org/10.1109/igarss55030.2025.11243886) | IEEE JSTARS | 2025 | Spaceborne SAR | L2 | M1 | T3 | Two-stage SAR VL pre-training | ○ Abs |
| [RSVQA-SAR](https://doi.org/10.48550/arxiv.2501.08131) | arXiv | 2025 | VHR SAR | L2 | M2 | T3 | Remote-sensing visual question answering | ○ Abs |
| [SAR-RAG](https://doi.org/10.48550/arxiv.2602.04712) | SPIE | 2026 | Spaceborne SAR | L2 | M4b | T1 | ATR visual question answering | ○ Abs |
| [SAR-Caption Ranker](https://doi.org/10.1109/icassp55912.2026.11464332) | arXiv | 2026 | Spaceborne SAR | L2 | M4b | T3 | RLAIF caption ranking | ○ Abs |
| [SAR-GenTrans](https://doi.org/10.22761/gd.2026.0004) | IEEE JSTARS | 2026 | Spaceborne SAR | L2 | M2 | T3 | Semantic interpretation via translation | ○ Abs |
| [TVLightFormer](https://doi.org/10.3390/rs18091430) | Remote Sens. | 2026 | Spaceborne SAR | L2 | M2 | T2 | Language-guided target localization | ○ Abs |
| [DGS-CapNet](https://doi.org/10.12000/jr25250) | IEEE JSTARS | 2026 | Spaceborne SAR | L2 | M2 | T3 | Spatial-frequency SAR captioning | ○ Abs |
| [FSAR-Cap](https://doi.org/10.1109/lgrs.2026.3663901) | arXiv | 2026 | Spaceborne SAR (FAIR-CSAR) | L2 | M2 | T3 | Fine-grained SAR captioning dataset | ○ Abs |
| [InSAR-Chat](https://doi.org/10.1109/IGARSS53475.2024.10641895) | IGARSS | 2026 | InSAR (EGMS) | L2 | M4b | T3 | InSAR deformation question answering | ○ Abs |
| [InSAR-Cap](https://doi.org/10.20944/preprints202605.0685.v1) | arXiv | 2026 | InSAR | L2 | M4b | T3 | InSAR captioning for geophysics | ○ Abs |
| [PolSAR-VQA](https://doi.org/10.1109/igarss53475.2024.10641895) | IGARSS | 2024 | Polarimetric SAR | L2 | M4b | T4 | Wishart H-$\alpha$ scattering-type VQA | ○ Abs |
| [SARShip-VQA](https://doi.org/10.48550/arxiv.2411.01445) | IEEE GRSL | 2024 | Spaceborne SAR | L2 | M4b | T1 | Ship attribute question answering | ○ Abs |

---

## 🛠️ Related Fields & Traditional Radar Applications

For a comprehensive review and bibliography covering traditional mmWave radar signal processing, deep learning baselines, and applications (2021–2026) across:
* Human Activity Recognition (HAR)
* Pose & Skeleton Estimation
* People Counting & Occupancy Detection
* Vital Signs & Cardiorespiratory Monitoring
* Dynamic Gesture & Sign Language Recognition
* In-Air Handwriting & Trajectory Tracking
* Marine & Electronic Warfare Target Recognition
* Material Dielectric Perception

👉 See: [**Related Fields and Traditional Radar Applications Summary & Catalog**](./Related%20Fields%20and%20Traditional%20Radar%20Applications/README.md)

---

## 🧪 Reproducibility & Open Science

> **Code & Data Status**: **Coming Soon** ⏳  
> The complete reproduction suite, PRISMA evaluation logs, and metrological audit scripts are being prepared and will be released in the [`./code`](./code) directory upon formal publication/acceptance of the survey manuscript.

---

## 📜 License

This project and catalog are released under the [MIT License](./LICENSE). All cited works belong to their respective authors and publishers.
