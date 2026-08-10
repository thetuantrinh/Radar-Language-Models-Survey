# 📡 Radar–Language Models (RLMs) Survey

Official repository for the survey manuscript:
**"Radar-Language Integration for Sensing Instrumentation: Signal Decoding, Measurement Uncertainty, and Multimodal Semantic Reasoning"**

**Authors**: The Tuan Trinh, Khoa Nguyen Dang, Xuanque Nguyen, Minhhuy Le*

---

## 📌 Abstract

Millimeter-wave (mmWave) and radar sensing instruments operate under severe physical constraints, where Range-Doppler-Angle (RDA) maps and 4D point clouds suffer from spatial sparsity, clutter backscatter, hardware non-idealities, and inherent signal measurement uncertainty. Recently, Radar-Language Models (RLMs) have emerged to address these instrumentation limitations, functioning as cognitive measurement decoders that couple physical electromagnetic feature extraction with Large Language Models (LLMs) and Vision-Language Models (VLMs) to translate raw radar measurements into semantically grounded physical parameters and natural language outputs. Unlike conventional deep-learning classifiers limited to closed-set categorical labels, RLMs project physical radar measurements into linguistic embedding spaces to perform open-set material property inference, spatial grounding, and adaptive instrumentation control. This paper presents a systematic survey reviewing 20 core RLM frameworks (2020–2026) alongside 3 background literature frameworks across 24, 60, and 77\,GHz FMCW and Ultra-Wideband (UWB) platforms, while strictly categorizing safety-only and image-only models as external background literature. We establish a three-axis taxonomy encompassing physical signal representations, cross-modal tokenization architectures, and measurement applications. Furthermore, we provide a critical trade-off analysis comparing signal tokenization information loss, spatial-temporal resolution bounds, and computational self-attention complexity ($O(N^2)$) on embedded edge processors. Crucially, we analyze measurement uncertainty propagation—tracing how phase noise, thermal noise, and antenna array mutual coupling impact LLM token probabilities and hallucination behavior. Finally, we outline key open challenges in hardware calibration drift, phase noise, and cross-frequency-band transferability, providing a strategic roadmap toward standardized, hardware-agnostic cognitive radar instrumentation.

**Index Terms**— *Millimeter-wave radar, FMCW radar, Radar-Language Models (RLMs), Cross-modal tokenization, Large language models, Multimodal semantic reasoning*

---

<p align="center">
  <img src="DOC/images/RADAR-LLMs.png" width="95%" alt="Radar-to-Language Processing Pipeline">
  <br>
  <em>Overview of the Radar-to-Language pipeline. Raw mmWave radar signals are transformed into structured representations, aligned with language embeddings through multimodal learning, and processed by large language models to enable semantic perception, reasoning, and human-computer interaction.</em>
</p>

---

## 🎯 Primary Contributions

1. **Systematic Three-Axis Taxonomy & Scope Definition**: We establish a unified taxonomy categorizing 20 core RLMs across physical signal representations, cross-modal tokenization architectures, and measurement tasks, strictly separating physical models from text-only safety and optical baselines.
2. **Measurement Uncertainty Propagation (MUQ) Analysis**: We formulate how low-level physical measurement uncertainties (noise, phase jitter, ADC quantization) and hardware non-idealities (chirp non-linearity, mutual coupling, temperature drift) propagate through tokenizers into LLM token probabilities and hallucination behavior.
3. **Comparative Quantification of Tokenization Paradigms**: We evaluate trade-offs across VQ-VAE codebooks, continuous linear projections, and physics-informed RAG in terms of information loss, spatial-temporal resolution bounds, and edge self-attention complexity ($O(N^2)$).
4. **Open-Science Reproducibility Catalog**: We compile a catalog of public datasets, open code repositories, and metrics spanning measurement science (mAP, Detection Rate) and NLP generation (BLEU-4, Word Accuracy).
5. **Strategic Research Roadmap**: We delineate a multi-horizon roadmap addressing calibration drift, multi-user RF interference, and the UWB integration gap toward hardware-agnostic cognitive radar.

---

## 🗺️ Survey Structure

<p align="center">
  <img src="DOC/images/structure.png" width="95%" alt="Radar-Language Models Survey Organization">
  <br>
  <em>High-level organization of this survey on Radar–Language Models, presenting foundational background, a unified taxonomy, datasets and evaluation methodologies, critical challenges, and future research opportunities.</em>
</p>

---

## 🏗️ Cross-Modal Tokenization Paradigms Trade-Off Matrix

| Tokenization Paradigm | Primary Representation | Attention Complexity | Phase Noise / Jitter Sensitivity | Edge Real-Time Suitability |
| :--- | :--- | :--- | :--- | :--- |
| **Discrete Codebook (VQ-VAE)** | Discrete codebook indices ($k^* \in \{1..K\}$) | $O(L^2)$ ($L \ll N$ tokens) | **High** (Voronoi boundary flips $k^* \to k'$ under low SNR) | **High** ($>30$ FPS, compact quantized sequence length) |
| **Continuous Projection (FPN/Linear)** | Continuous embeddings ($\mathbf{h} \in \mathbb{R}^d$) | $O(N^2)$ ($N \approx 10^3$ points) | **Medium** (Continuous error propagation into soft prompt spaces) | **Low–Medium** (Self-attention memory bottleneck on edge GPUs) |
| **Physics-Informed RAG** | Distilled scalars ($\epsilon_r, \sigma$) + Prompts | $O(1)$ token overhead | **Low** (Bounded by front-end physical parameter estimator) | **High** (Minimal prompt tokens, zero raw tensor FLOPs) |

---

## 📊 Technical Comparison of Reviewed Radar-LLM Literature (2024–2026)

| Work | Year | Radar Modality | RF Band / Hardware | Representation | Task | Language Component |
| :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| **Core Physical Radar-Language Models (RLMs)** | | | | | | |
| [Talk2Radar](https://arxiv.org/abs/2405.12821) | 2024 | 4D mmWave Radar | 77 GHz (TI AWR1843/AWA2243) | 4D Point Cloud | 3D Referring Expression | Alignment |
| [LLMCount](https://arxiv.org/abs/2409.16209) | 2024 | Stationary mmWave | 60/77 GHz (TI IWR6843) | micro-Doppler | Target Counting | Alignment |
| [RadarLLM-Motion](https://arxiv.org/abs/2504.09862) | 2025 | mmWave Radar | 60 GHz FMCW / POI Synth | Point Cloud Seq. | Human Motion Understanding | Agentic Reasoning |
| [RadarPLM](https://arxiv.org/abs/2509.12089) | 2025 | Marine Radar | 9.4 GHz X-band (IPIX Radar) | Signal / Images | Target Detection | Alignment |
| [Marine Radar LLM](https://doi.org/10.1109/IGARSS55030.2025.11313965) | 2025 | Marine Radar | 9.4 GHz Dual-Pol X-band | Signal / Images | Target Detection | Alignment |
| [Multimodal ISAC LLM](https://doi.org/10.1109/MCOM.004.2400281) | 2025 | Multimodal ISAC | Sub-6 GHz / 28 GHz ISAC | Waveforms / Bits | Integrated Sensing/Comm | Agentic Reasoning |
| [LLMaterial](https://doi.org/10.1145/3714394.3756289) | 2025 | Radar Signals | 77 GHz FMCW (TI AWR1843) | Signatures ($\epsilon_r$, RCS) | Material Identification | Agentic Reasoning |
| [Robotic Material Perception](https://doi.org/10.1145/3680207.3765653) | 2025 | Radar + Vision | 77 GHz mmWave + RGB | Point Cloud / RGB | Material Perception | Agentic Reasoning |
| [mmPencil](https://doi.org/10.1145/3749504) | 2025 | mmWave Radar | 60 GHz FMCW (TI IWR6843ISK) | Trajectories | In-air Handwriting | Alignment / Generation |
| [WirelessGPT](https://doi.org/10.1109/JSAC.2025.3640156) | 2025 | Wireless / ISAC | 28 GHz / Sub-6 GHz Array | Waveforms | Multi-task ISAC Foundation | Generation |
| [MmExpert](https://doi.org/10.1145/3704413.3764420) | 2025 | mmWave Radar | 77 GHz FMCW (TI AWR1843) | Heatmaps / Raw | Data Synthesis/Understand | Gen. / Agentic Reasoning |
| [Radar2Text](https://doi.org/10.1109/IMBioC63524.2025.10989725) | 2025 | mmWave Radar | 77 GHz FMCW Sensor | Signatures / Spectra | Linguistic Summarization | Generation |
| [IoT ISAC LLM](https://doi.org/10.1109/MIOT.2025.3575888) | 2025 | IoT / ISAC | Sub-6 GHz / 60 GHz IoT | Sensing Data | Network Orchestration | Agentic Reasoning |
| [M2BeamLLM](https://arxiv.org/abs/2506.14532) | 2025 | mmWave | 60 GHz (DeepSense 6G Unit) | Beam Patterns | Beam Prediction | Alignment / Generation |
| [SAR Image Captioning](https://doi.org/10.1109/JSTARS.2025.3603036) | 2025 | SAR (Satellite) | C/X-band SAR (Gaofen-3) | SAR Images | Image Captioning | Generation |
| [Jamming VLM](https://doi.org/10.1109/TAES.2025.3586834) | 2025 | Electronic Warfare | 1–18 GHz EW Spectrograms | Spectrograms | Jamming Recognition | Alignment (VLMs) |
| [Sig2text](https://arxiv.org/abs/2503.15213) | 2025 | Non-coop. Radar | 0.5–18 GHz EW Receiver | Pulse / Signal | Radar Signal Parsing | Generation |
| [Signal Deinterleaving](https://doi.org/10.3390/s26010248) | 2026 | Pulse Radar Signal | Non-coop. Pulse Stream | Pulse (PRI) Stream | Signal Deinterleaving | Reasoning / Generation |
| [RFSensingGPT](https://doi.org/10.1109/TCCN.2025.3558069) | 2026 | RF / 6G Networks | Sub-6 GHz / mmWave 6G | Signal Features | RAG-enhanced Sensing | Gen. / Agentic Reasoning |
| [SARLANG-1M](https://doi.org/10.1109/TGRS.2026.3652099) | 2026 | SAR (Satellite) | C-band SAR (Sentinel-1) | SAR Images | Signal Understanding | Alignment / Generation |
| **External Background Literature** | | | | | | |
| [RADAR (Safety)](https://arxiv.org/abs/2509.25271)† | 2025 | N/A (Safety) | N/A (Text Prompts) | Textual / Logic | LLM Safety Evaluation | Agentic Reasoning |
| [Radar NLP Trends](https://doi.org/10.1109/MAES.2025.3533946)† | 2025 | General Radar | Multi-band Radar | Signals / Texts | Review: NLP Trends | Alignment / Generation |
| [RADAR (Fake Image)](https://doi.org/10.3390/technologies13070280)† | 2025 | N/A (Image-based) | Optical Camera | Semantic Features | Fake Image Detection | Agentic Reasoning |

*\*† Categorized as external background literature as defined by the operational scope criteria in Section I.*

---

## 🛠️ Summary of mmWave Radar Sensing Applications and Recent Advancements (2021–2026)

| Application Area | Radar Modality | Key Technical Focus | Year | Representative Works / Citations |
| :--- | :--- | :--- | :---: | :--- |
| **Human Activity Recognition** | 4D Point Cloud / Micro-Doppler | Multi-link channel robustness, in-memory computing for healthcare, TinyML implementations, and non-line-of-sight (NLOS) spectrogram analysis. | 2022–2026 | [Miazek, et al. (2024)](https://doi.org/10.1109/ACCESS.2024.3474100), [Li, et al. (2023)](https://doi.org/10.1038/s41598-023-30631-x), [Kurtoğlu, et al. (2025)](https://ieeexplore.ieee.org/document/11126867), [Wang, et al. (2025)](https://doi.org/10.1109/OJAP.2025.3638652), [Nikpour, et al. (2025)](https://doi.org/10.1109/TNNLS.2024.3360990), [Ji, et al. (2026)](https://doi.org/10.1109/JBHI.2024.3392648), [Hossan, et al. (2025)](https://doi.org/10.1109/LES.2025.363994), [Ding, et al. (2025)](https://doi.org/10.1109/TAES.2025.3579771), [Wang, et al. (2025)](https://doi.org/10.1109/JIOT.2025.3580799), [Hu, et al. (2025)](https://doi.org/10.1109/TIM.2025.3558216), [Zhang, et al. (2024)](https://doi.org/10.1109/TIM.2024.3365155) |
| **Human / Hand / Skeleton Pose Estimation** | Sparse Point Clouds / Raw Cubes | Transformer-based end-to-end estimation, skeletal probability map-guided fusion, egocentric radar-IMU integration, and RF vision for occluded hands. | 2023–2026 | Zhou, et al. (2025), [Chen, et al. (2026)](https://doi.org/10.1109/JIOT.2026.3651437), [Dong, et al. (2026)](https://doi.org/10.1109/JSEN.2026.3650914), [Engel, et al. (2025)](https://doi.org/10.1109/JMW.2025.3535525), [Chen, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3542078), [Zhu, et al. (2025)](https://doi.org/10.1109/TAES.2025.3594328), [Wu, et al. (2025)](https://doi.org/10.1109/JIOT.2024.3476350), [Shi, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3577772), [Xu, et al. (2024)](https://doi.org/10.1109/JIOT.2023.3312316), [Lv, et al. (2025)](https://doi.org/10.48550/arXiv.2501.13805), [Yuan, et al. (2026)](https://doi.org/10.1145/3793858), [Yuanzhi et al. (2026)](https://doi.org/10.1016/j.measurement.2025.118851), [Li, et al. (2024)](https://doi.org/10.1145/3625687.3625799), [Sun, et al. (2026)](https://doi.org/10.1109/TIM.2026.3712914), [Chen, et al. (2025)](https://doi.org/10.1109/TIM.2025.3569914), [Trinh, et al. (2026)](https://doi.org/10.1109/JSEN.2026.3686129) |
| **People Counting & Occupancy** | Stationary / 4D mmWave | Stationary detection via Multimodal-LLMs, hybrid DCNN-transfer learning for clutter mitigation, and door open-close discrimination. | 2023–2025 | [Mboyi et al. (2025)](https://doi.org/10.1109/TIM.2025.3545718), [Yang, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3609465), [Vales, et al. (2024)](https://doi.org/10.1109/JIOT.2024.3434707), [Ren, et al. (2023)](https://doi.org/10.1109/JIOT.2023.3282797), [Martin-Martin, et al. (2025)](https://doi.org/10.1109/ACCESS.2025.3557317), [Cheng, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3577228), [Shenglei et al. (2023)](https://doi.org/10.1016/j.ifacol.2023.10.577), [Mauro, et al. (2023)](https://doi.org/10.1007/s10489-023-04778-z), [Ange et al. (2024)](https://doi.org/10.1016/j.sasc.2024.200095) |
| **Vital Sign & Health Monitoring** | FMCW Phase / Higher Harmonics | Nonlinear spectral approaches for heartbeat estimation, mitigation of respiration harmonics, and missing data models for body movement robustness. | 2022–2025 | Li, et al. (2024), [Singh, et al. (2024)](https://doi.org/10.1109/THMS.2024.3381074), [Shirazi, et al. (2025)](https://doi.org/10.1016/j.measurement.2025.117707), [Qiao, et al. (2025)](https://doi.org/10.1109/TIM.2025.3547495), [Park, et al. (2025)](https://doi.org/10.1109/JSEN.2024.3491753), [Shimomura, et al. (2025)](https://doi.org/10.1109/LMWT.2025.3650557), [En-Kang et al. (2025)](https://doi.org/10.1016/j.measurement.2024.116144), [Wang, et al. (2024)](https://doi.org/10.1109/TMC.2023.3288850), [Grisot, et al. (2023)](https://doi.org/10.1109/TRS.2023.3298348), [Jiang, et al. (2024)](https://doi.org/10.1109/TAES.2024.3379492), [Vilesov, et al. (2022)](https://doi.org/10.1145/3528223.3530161), [Xu, et al. (2024)](https://doi.org/10.1109/TIM.2024.3450071) |
| **Hand Gesture & Sign Language** | Micro-Doppler / UWB / Range-Doppler | Continuous Chinese sign language via DeepSeek semantic enhancement, uncertainty-aware deep learning, and cumulative distribution density features. | 2020–2026 | Chen, et al. (2026), Han, et al. (2025), [Wang, et al. (2021)](https://doi.org/10.1109/THMS.2020.3036637), [Qiu, et al. (2024)](https://doi.org/10.4236/jcc.2024.126008), [Jin, et al. (2024)](https://doi.org/10.1109/THMS.2024.3385124), [Zhang, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3599380), [Lin, et al. (2026)](https://doi.org/10.1109/JIOT.2025.3644894), [Trinh, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3573743), [Li, et al. (2021)](https://doi.org/10.1109/TIM.2021.3092072), [Li, et al. (2023)](https://doi.org/10.1109/TGRS.2023.3278298), [Jiayi et al. (2025)](https://doi.org/10.1016/j.measurement.2025.117545), [Yu, et al. (2022)](https://doi.org/10.1109/THMS.2022.3149408), [Trinh, et al. (2023)](https://doi.org/10.1109/ICCAIS59597.2023.10382331), [Chen, et al. (2026)](https://doi.org/10.3390/electronics15020437), [Towakel, et al. (2023)](https://doi.org/10.1109/TIM.2023.3307768), [Han, et al. (2025)](https://doi.org/10.1109/TIM.2025.3582311), [Trinh, et al. (2026)](https://doi.org/10.1109/TAES.2026.3709269) |
| **Air-Writing & Handwriting** | FMCW / Acoustic-Radar | Writing-style-independent recognition, alphanumeric gesture classification, and optimized ResYOLO-Transformers. | 2024–2025 | [Arsalan, et al. (2024)](https://doi.org/10.1007/978-3-658-45318-3_4), [Satti, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3645357), [Kim, et al. (2025)](https://doi.org/10.1109/TIM.2025.3573779), [Pan, et al. (2025)](https://doi.org/10.1109/TMC.2025.3526185), [Lamaakal, et al. (2026)](https://doi.org/10.1109/JIOT.2025.3624283), [Tian, et al. (2025)](https://doi.org/10.1109/JIOT.2024.3507369), [Huang, et al. (2025)](https://doi.org/10.1007/978-3-031-78104-9_29) |
| **Target Detection & Recognition** | Graph Fourier / IQ Signals | Marine target detection with preference-aware loss, zero-shot active jamming recognition, and spatial-temporal graph transforms. | 2021–2026 | [Wee, et al. (2021)](https://doi.org/10.1109/THMS.2021.3076044), [Salehi, et al. (2024)](https://doi.org/10.1109/TCCN.2024.3391327), [Lian, et al. (2025)](https://doi.org/10.1109/TAES.2024.3510687), [Jingang et al. (2025)](https://doi.org/10.1016/j.sigpro.2025.110034), [Chen, et al. (2026)](https://doi.org/10.1109/JMASS.2026.3656926), [Nikaein, et al. (2026)](https://doi.org/10.1109/TRS.2026.3658846), [Zeng, et al. (2024)](https://doi.org/10.1109/TIM.2024.3400347) |
| **Imaging, SAR & Displacement** | Complex Phase / SAR | Joint phase-envelope autofocus for backprojection, SAR image captioning via multimodal large models, and real-time displacement evaluation. | 2021–2026 | Lee, et al. (2025), [Wan, et al. (2025)](https://doi.org/10.1109/LGRS.2025.3580587), [Xie, et al. (2022)](https://doi.org/10.3390/s22155757), [Ferro, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3594433), [Hu, et al. (2025)](https://doi.org/10.1109/TAES.2025.3617036), [Yiming et al. (2026)](https://doi.org/10.1016/j.ndteint.2025.103529), [Alicia et al. (2023)](https://doi.org/10.1016/j.engappai.2023.106305), [Zhang, et al. (2025)](https://doi.org/10.1109/JSTARS.2024.3509477), [Tong, et al. (2025)](https://doi.org/10.1109/TIM.2025.3550226) |
| **Material & Object Perception** | Sub-THz / Microwave Pulse | Sub-THz classification for ISAC, nondestructive testing of debonding defects, and complex permittivity extraction. | 2021–2025 | Song, et al. (2025), [Martínez-Cesteros, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3614471), [Zhu, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3582609), [Kim, et al. (2025)](https://doi.org/10.1109/LAWP.2025.3593991), [Liu, et al. (2021)](https://doi.org/10.1109/TIM.2021.3113118), [Karatay, et al. (2024)](https://doi.org/10.1109/TIM.2024.3428598) |

---

## 📚 Categorized Paper Catalog

### Core Physical Radar-Language Models (RLMs)

#### 2024
* [**Talk2Radar: Bridging Natural Language with 4D mmWave Radar for 3D Referring Expression Comprehension**](https://arxiv.org/abs/2405.12821) — R. Guan et al. [[Code]](https://github.com/GuanRunwei/Talk2Radar)
* [**LLMCount: Enhancing Stationary mmWave Detection with Multimodal-LLM**](https://arxiv.org/abs/2409.16209) — B. Li et al.

#### 2025
* [**RadarLLM: Empowering Large Language Models to Understand Human Motion from Millimeter-Wave Point Cloud Sequence**](https://arxiv.org/abs/2504.09862) — Z. Lai et al. [[Code]](https://github.com/Inowlzy/RadarLLM)
* [**RadarPLM: Adapting Pre-trained Language Models for Marine Radar Target Detection by Selective Fine-Tuning**](https://arxiv.org/abs/2509.12089) — Q. Hu
* [**When Marine Radar Target Detection Meets Pre-trained Large Language Models**](https://doi.org/10.1109/IGARSS55030.2025.11313965) — Q. Hu et al.
* [**Large Language Models Empower Multimodal Integrated Sensing and Communication**](https://doi.org/10.1109/MCOM.004.2400281) — L. Cheng et al.
* [**Can Large Language Models Identify Materials from Radar Signals?**](https://doi.org/10.1145/3714394.3756289) — J. Zhu, H. Deng, and H. Chen
* [**Radar-Enhanced Robotic Material Perception with Vision Language Models**](https://doi.org/10.1145/3680207.3765653) — H. Deng, J. Zhu, and H. Chen
* [**mmPencil: Toward Writing-Style-Independent In-Air Handwriting Recognition via mmWave Radar and Large Vision-Language Model**](https://doi.org/10.1145/3749504) — Y. Guo et al. [[Dataset]](https://www.kaggle.com/datasets/mmpencil/mmpencil-dataset)
* [**WirelessGPT: A Generative Foundation Model for Multi-Task Integrated Sensing and Communication**](https://doi.org/10.1109/JSAC.2025.3640156) — T. Yang et al.
* [**MmExpert: Integrating Large Language Models for Comprehensive mmWave Data Synthesis and Understanding**](https://doi.org/10.1145/3704413.3764420) — Y. Yan et al.
* [**Radar2Text: Generation of Linguistic Summary from mmWave Radar Signatures Using Fine-Tuned Multimodal Language Models**](https://doi.org/10.1109/IMBioC63524.2025.10989725) — K. E. O. Jauregui and D. V. D. Q. Rodrigues
* [**Multi-Modal Integrated Sensing and Communication in Internet of Things with Large Language Models**](https://doi.org/10.1109/MIOT.2025.3575888) — A. Liu et al.
* [**M2BeamLLM: Multimodal Sensing-Empowered mmWave Beam Prediction with Large Language Models**](https://arxiv.org/abs/2506.14532) — C. Zheng et al. [[Data]](https://deepsense6g.net/)
* [**Multimodal Large Models Driven SAR Image Captioning: A Benchmark Dataset and Baselines**](https://doi.org/10.1109/JSTARS.2025.3603036) — Z. Gao et al.
* [**Few-Shot and Zero-Shot Radar Active Jamming Recognition Based on a Vision-Language Model**](https://doi.org/10.1109/TAES.2025.3586834) — X. Cao
* [**Sig2Text: A Vision-Language Model for Non-Cooperative Radar Signal Parsing**](https://arxiv.org/abs/2503.15213) — H. Feng et al. [[Code]](https://github.com/Na-choneko/sig2text)
* [**Emerging Trends in Radar: Natural Language Processing**](https://doi.org/10.1109/MAES.2025.3533946) — R. M. Narayanan et al. *(Background Literature)*
* [**RADAR: A Risk-Aware Dynamic Multi-Agent Framework for LLM Safety Evaluation via Role-Specialized Collaboration**](https://arxiv.org/abs/2509.25271) — X. Chen et al. *(Background Literature)*
* [**RADAR: Reasoning AI-Generated Image Detection for Semantic Fakes**](https://doi.org/10.3390/technologies13070280) — H. Wang et al. *(Background Literature)*

#### 2026
* [**The Intelligent Evolution of Radar Signal Deinterleaving: A Systematic Review from Foundational Algorithms to Cognitive AI Frontiers**](https://doi.org/10.3390/s26010248) — Z. Qu, J. Zhang, Y. Zhou, and L. Ni
* [**RFSensingGPT: A Multi-Modal RAG-Enhanced Framework for Integrated Sensing and Communications Intelligence in 6G Networks**](https://doi.org/10.1109/TCCN.2025.3558069) — M. Z. Khan et al.
* [**SARLANG-1M: A Benchmark for Vision-Language Modeling in SAR Image Understanding**](https://doi.org/10.1109/TGRS.2026.3652099) — Y. Wei et al.

---


### 🛠️ Recent Advancements in mmWave Radar Sensing Literature (2021–2026)

#### Human Activity Recognition

* [**Human Behavior Analysis Using Radar Data: A Survey**](https://doi.org/10.1109/ACCESS.2024.3474100) (2024) — Miazek, Patrycja et al.
* [**Radar-based human activity recognition with adaptive thresholding towards resource constrained platforms**](https://doi.org/10.1038/s41598-023-30631-x) (2023) — Li, Zhenghui et al.
* [**Human-Centered Fully Adaptive Radar for Gesture Recognition in Smart Environments**](https://ieeexplore.ieee.org/document/11126867) (2025) — Kurtoğlu, Emre and Gurbuz, Sevgi Z.
* [**Performance Enhancement of Human Activity Recognition Using Millimeter-Wave Multi-Link Channels**](https://doi.org/10.1109/OJAP.2025.3638652) (2025) — Wang, Y. et al.
* [**Deep Reinforcement Learning in Human Activity Recognition: A Survey and Outlook**](https://doi.org/10.1109/TNNLS.2024.3360990) (2025) — Nikpour, B., Sinodinos, D., and Armanfard, N.
* [**An Efficient Human Activity Recognition In-Memory Computing Architecture Development for Healthcare Monitoring**](https://doi.org/10.1109/JBHI.2024.3392648) (2026) — Ji, X. and others
* [**TinyHAR-Net: Design and Implementation of a TinyML-Based Human Activity Recognition Framework on STM32**](https://doi.org/10.1109/LES.2025.363994) (2025) — Hossan, I., Mary, M. N. J., and Motin, M. A.
* [**A Non-Line-of-Sight Human Activity Recognition Method Based on Radar Multispectrogram**](https://doi.org/10.1109/TAES.2025.3579771) (2025) — Ding, C. and others
* [**Crucial Region Search and Feature Discrimination for Radar-Based Human Activity Recognition**](https://doi.org/10.1109/JIOT.2025.3580799) (2025) — Wang, D. et al.
* [**Human Activity Recognition Trained on Simulated Millimeter-Wave Radar Data**](https://doi.org/10.1109/TIM.2025.3558216) (2025) — Hu, Y. et al.
* [**Multi-STMT: Multi-Level Network for Human Activity Recognition Based on mmWave Radar**](https://doi.org/10.1109/TIM.2024.3365155) (2024) — Zhang, H. and Xu, L.

#### Human / Hand / Skeleton Pose Estimation

* **Learning to Analyze Human Skeletal by Radar-Camera Supervision** (2025) — Zhou, Y. et al.
* [**RF-PoseR: A Human Pose Rectifier for mmWave Radar-based Pose Estimation**](https://doi.org/10.1109/JIOT.2026.3651437) (2026) — Chen, Q. and others
* [**A Global-Local Network for Human Pose Estimation with Completed mmWave Radar Point Clouds**](https://doi.org/10.1109/JSEN.2026.3650914) (2026) — Dong, M. et al.
* [**Advanced Millimeter Wave Radar-Based Human Pose Estimation Enabled by a Deep Learning Neural Network Trained With Optical Motion Capture Ground Truth Data**](https://doi.org/10.1109/JMW.2025.3535525) (2025) — Engel, L. and others
* [**CPFormer: End-to-End Multi-Person Human Pose Estimation From Raw Radar Cubes With Transformers**](https://doi.org/10.1109/JSEN.2025.3542078) (2025) — Chen, L. and Wang, G.
* [**ProbRadarM3F: mmWave Radar-Based Human Skeletal Pose Estimation With Probability Map-Guided Multiformat Feature Fusion**](https://doi.org/10.1109/TAES.2025.3594328) (2025) — Zhu, B. and others
* [**mmHPE: Robust Multiscale 3-D Human Pose Estimation Using a Single mmWave Radar**](https://doi.org/10.1109/JIOT.2024.3476350) (2025) — Wu, Y. and others
* [**mmPoint-Attention: A Unified Attention Framework for Human Pose and Activity Recognition From mmWave Radar Point Clouds**](https://doi.org/10.1109/JSEN.2025.3577772) (2025) — Shi, X., Bouazizi, M., and Ohtsuki, T.
* [**Ske-Fi: Estimating Hand Poses via RF Vision Under Low Contrast and Occlusion**](https://doi.org/10.1109/JIOT.2023.3312316) (2024) — Xu, J. and others
* [**mmEgoHand: Egocentric Hand Pose Estimation and Gesture Recognition with Head-mounted Millimeter-wave Radar and IMU**](https://doi.org/10.48550/arXiv.2501.13805) (2025) — Lv, Y. and others
* [**3D-Sitpose: Millimeter Wave Radar-Based Human Sitting Posture Estimation**](https://doi.org/10.1145/3793858) (2026) — Yuan, Wenyang et al.
* [**PoseGraphNet: Pose prior and graph structure for 3D human pose estimation using mmWave radar**](https://doi.org/10.1016/j.measurement.2025.118851) (2026) — Yuanzhi Su et al.
* [**Egocentric Human Pose Estimation using Head-mounted mmWave Radar**](https://doi.org/10.1145/3625687.3625799) (2024) — Li, Wenwei et al.
* [**Through-Wall Multiperson 3-D Pose Estimation With MIMO Radar in Low SNR**](https://doi.org/10.1109/TIM.2026.3712914) (2026) — Sun, S. et al.
* [**Knowledge-Embedded Transformer for 3-D Human Pose Estimation**](https://doi.org/10.1109/TIM.2025.3569914) (2025) — Chen, S. and He, Y.
* [**Real-Time Hand Pose Estimation Using FMCW Radar on Resource-Limited Edge Devices**](https://doi.org/10.1109/JSEN.2026.3686129) (2026) — Trinh, T. T. et al.

#### People Counting & Occupancy

* [**Hybrid DCNN–Transfer Learning Model Coupled With Background Clutter Mitigation for FMCW Radar-Based People Counting Improvement**](https://doi.org/10.1109/TIM.2025.3545718) (2025) — Mboyi Gilles Yowel, M., Oh, D.-H., and Han, J.-H.
* [**Bi-Direction People Counting Exploiting Door Open-Close Discrimination Using 4D Millimeter Wave Radar**](https://doi.org/10.1109/JSEN.2025.3609465) (2025) — Yang, Z. et al.
* [**An IoT System for Smart Building Combining Multiple mmWave FMCW Radars Applied to People Counting**](https://doi.org/10.1109/JIOT.2024.3434707) (2024) — Vales, Valentín Barral et al.
* [**Grouped People Counting Using mm-Wave FMCW MIMO Radar**](https://doi.org/10.1109/JIOT.2023.3282797) (2023) — Ren, Liyuan, Yarovoy, Alexander G., and Fioranelli, Francesco
* [**Spiking Neural Networks for People Counting Based on FMCW Radar**](https://doi.org/10.1109/ACCESS.2025.3557317) (2025) — Martin-Martin, Alberto et al.
* [**Space Boundary-Aware People Tracking and Counting Method Using MIMO Radar**](https://doi.org/10.1109/JSEN.2025.3577228) (2025) — Cheng, Qiaoling et al.
* [**An Indoor People Counting and Tracking System using mmWave sensor and sub-sensors**](https://doi.org/10.1016/j.ifacol.2023.10.577) (2023) — Shenglei Li and Reiko Hishiyama
* [**Context-adaptable radar-based people counting via few-shot learning and active learning**](https://doi.org/10.1007/s10489-023-04778-z) (2023) — Mauro, Gianluca et al.
* [**People counting using IR-UWB radar sensors and machine learning techniques**](https://doi.org/10.1016/j.sasc.2024.200095) (2024) — Ange Joel Nounga Njanda et al.

#### Vital Sign & Health Monitoring

* **RadarNet: Non-Contact ECG Signal Measurement Based on FMCW Radar** (2024) — Li, B. et al.
* [**Human Vital Signs Estimation Using Resonance Sparse Spectrum Decomposition**](https://doi.org/10.1109/THMS.2024.3381074) (2024) — Singh, Anuradha et al.
* [**A survey on machine learning approaches for vital sign monitoring using radar**](https://doi.org/10.1016/j.measurement.2025.117707) (2025) — Shirazi, M. H. and others
* [**Millimeter-Wave Radar Vital Signs Measurement With Random Body Movement Using Missing Data Model**](https://doi.org/10.1109/TIM.2025.3547495) (2025) — Qiao, X. et al.
* [**Heart Rate Extraction Technique With Mitigation of Respiration Harmonic for Bio-Radar Sensors**](https://doi.org/10.1109/JSEN.2024.3491753) (2025) — Park, J.-E. et al.
* [**A Nonlinear Spectral Approach for Radar-Based Heartbeat Estimation via Autocorrelation of Higher Harmonics**](https://doi.org/10.1109/LMWT.2025.3650557) (2025) — Shimomura, K., Lee, C.-H., and Sakamoto, T.
* [**Non-contact monitoring of human cardiorespiratory activity during sleep using FMCW millimeter wave radar**](https://doi.org/10.1016/j.measurement.2024.116144) (2025) — En-Kang Wu et al.
* [**Vital Sign Monitoring in Dynamic Environment via mmWave Radar and Camera Fusion**](https://doi.org/10.1109/TMC.2023.3288850) (2024) — Wang, Yingqi et al.
* [**Monitoring of Heart Movements Using an FMCW Radar and Correlation With an ECG**](https://doi.org/10.1109/TRS.2023.3298348) (2023) — Grisot, Rémi et al.
* [**Vision-Guided MIMO Radar Beamforming for Enhanced Vital Signs Detection in Crowds**](https://doi.org/10.1109/TAES.2024.3379492) (2024) — Jiang, Shuaifeng et al.
* [**Blending camera and 77 GHz radar sensing for equitable, robust plethysmography**](https://doi.org/10.1145/3528223.3530161) (2022) — Vilesov, Alexander et al.
* [**Vital Signs Detection in the Presence of Nonperiodic Body Movement via mmWave Radar**](https://doi.org/10.1109/TIM.2024.3450071) (2024) — Xu, D. et al.

#### Hand Gesture & Sign Language

* **Domain-Generalized Gesture Recognition via mmWave Radar Signal Multiview Learning** (2026) — Chen, Q. et al.
* **A Robust Real-Time Multiuser Gesture Recognition System for Human--Computer Interaction Using mmWave Radar Sensors** (2025) — Han, W., Hasan, K., and Yuce, M. R.
* [**Gesture-Radar: A Dual Doppler Radar Based System for Robust Recognition and Quantitative Profiling of Human Gestures**](https://doi.org/10.1109/THMS.2020.3036637) (2021) — Wang, Zhu et al.
* [**A Survey of Gesture Recognition Using Frequency Modulated Continuous Wave Radar**](https://doi.org/10.4236/jcc.2024.126008) (2024) — Qiu, X. and others
* [**Gesture-mmWAVE: Compact and Accurate Millimeter-Wave Radar-Based Dynamic Gesture Recognition for Embedded Devices**](https://doi.org/10.1109/THMS.2024.3385124) (2024) — Jin, Biao et al.
* [**Continuous Chinese Sign Language Recognition Using Millimeter-Wave Radar with DeepSeek Semantic Enhancement**](https://doi.org/10.1109/JSEN.2025.3599380) (2025) — Zhang, L. and others
* [**mmWave Radar-Based Continuous Sign Language Recognition: Lightweight Modeling, Contextual Optimization, and Embedded Implementation**](https://doi.org/10.1109/JIOT.2025.3644894) (2026) — Lin, Z. et al.
* [**Hand Gesture Recognition With Uncertainty Awareness via FMCW Radar Sensing and Deep Learning**](https://doi.org/10.1109/JSEN.2025.3573743) (2025) — Trinh, T. T. et al.
* [**Sign Language/Gesture Recognition Based on Cumulative Distribution Density Features Using UWB Radar**](https://doi.org/10.1109/TIM.2021.3092072) (2021) — Li, B. et al.
* [**Objective Evaluation of Clutter Suppression for Micro-Doppler Spectrograms of Hand Gesture/Sign Language Based on Pseudo-Reference Image**](https://doi.org/10.1109/TGRS.2023.3278298) (2023) — Li, B. et al.
* [**Robust hand gesture detection and recognition using 4D millimeter-wave radar in a ubiquitous scene**](https://doi.org/10.1016/j.measurement.2025.117545) (2025) — Jiayi Cai et al.
* [**SoDar: Multitarget Gesture Recognition Based on SIMO Doppler Radar**](https://doi.org/10.1109/THMS.2022.3149408) (2022) — Yu, Zhiwen et al.
* [**2023 12th International Conference on Control, Automation and Information Sciences (ICCAIS)**](https://doi.org/10.1109/ICCAIS59597.2023.10382331) (2023) — Trinh, The Tuan et al.
* [**Fine-Grained Radar Hand Gesture Recognition Method Based on Variable-Channel DRSN**](https://doi.org/10.3390/electronics15020437) (2026) — Chen, Penghui et al.
* [**Deep Combination of Radar With Optical Data for Gesture Recognition**](https://doi.org/10.1109/TIM.2023.3307768) (2023) — Towakel, P., Windridge, D., and Nguyen, H.
* [**A Robust Real-Time Multiuser Gesture Recognition System for Human--Computer Interaction**](https://doi.org/10.1109/TIM.2025.3582311) (2025) — Han, W., Hasan, K., and Yuce, M.
* [**Complex-Valued (2+1)D Convolutional Neural Networks for Real-Time Hand Gesture Recognition on Edge Devices With FMCW Radar**](https://doi.org/10.1109/TAES.2026.3709269) (2026) — Trinh, T. T. and others

#### Air-Writing & Handwriting

* [**Radar-based Air-writing for Embedded Devices**](https://doi.org/10.1007/978-3-658-45318-3_4) (2024) — Arsalan, Muhammad
* [**Air-Written Multi-Character Detection and Classification Using Vision-Based Hand Gestures and an Optimized ResYOLO-Transformer**](https://doi.org/10.1109/JSEN.2025.3645357) (2025) — Satti, S. K. and Prasad, M.
* [**FMCW Radar-Based In-Air Alphanumeric Gesture Recognition With Machine Learning**](https://doi.org/10.1109/TIM.2025.3573779) (2025) — Kim, W. and others
* [**MagicWrite: One-Dimensional Acoustic Tracking-Based Air Writing System**](https://doi.org/10.1109/TMC.2025.3526185) (2025) — Pan, H. and others
* [**Tiny Deep Learning Models With Hybrid Compression Techniques for Gesture-Based Air Handwriting Recognition of English Alphabets on Edge Device**](https://doi.org/10.1109/JIOT.2025.3624283) (2026) — Lamaakal, Ismail et al.
* [**mmDigit: A Real-Time Digit Recognition Framework in Air-Writing Using FMCW Radar**](https://doi.org/10.1109/JIOT.2024.3507369) (2025) — Tian, Jiake et al.
* [**mmAlphabet: Air Writing Alphabet Recognition System Based on mmWave FMCW Radar and Convolutional Neural Network**](https://doi.org/10.1007/978-3-031-78104-9_29) (2025) — Huang, Chao-Wang, Wang, Chien-Yao, and Wang, Jia-Ching

#### Target Detection & Recognition

* [**Radar Command Group Time Entropy Signature as a Visual Monitoring Enhancement for Air Traffic Controllers**](https://doi.org/10.1109/THMS.2021.3076044) (2021) — Wee, Hong Jie et al.
* [**Learning and Model-Based Approaches for Radar Target Detection**](https://doi.org/10.1109/TCCN.2024.3391327) (2024) — Salehi, Ahmadreza et al.
* [**Distributed MIMO Radar Target Detection in Multipath Clutter Environments With Time Reversal**](https://doi.org/10.1109/TAES.2024.3510687) (2025) — Lian, H. and others
* [**Radar target tracking based on motion characteristic and distribution pattern matching**](https://doi.org/10.1016/j.sigpro.2025.110034) (2025) — Jingang Wang, Songbin Li, and Ke Shi
* [**Digital Array Ubiquitous Radar Target Detection via Graph Representation and Spatial-Temporal Graph Fourier Transform**](https://doi.org/10.1109/JMASS.2026.3656926) (2026) — Chen, X. and others
* [**Moving Target Detection Using Passive Bistatic Radars in Presence of Interfering Target and I/Q Imbalances**](https://doi.org/10.1109/TRS.2026.3658846) (2026) — Nikaein, Hossein, Jabbari, Mohammad Reza, and Gazor, Saeed
* [**Camera-Assisted Radar Detection Clustering for Extended Target Tracking**](https://doi.org/10.1109/TIM.2024.3400347) (2024) — Zeng, J. et al.

#### Imaging, SAR & Displacement

* **Integration of mmWave FMCW Radar and Stereo Camera for 3D Automotive SAR Imaging** (2025) — Lee, H. et al.
* [**Phase-Envelope Joint Autofocus Algorithm for Backprojection Imaging**](https://doi.org/10.1109/LGRS.2025.3580587) (2025) — Wan, B. and others
* [**Resolution Enhancement for Millimeter-Wave Radar ROI Image with Bayesian Compressive Sensing**](https://doi.org/10.3390/s22155757) (2022) — Xie, P. and others
* [**An Insight Into the Displacement Evaluation During Real-Time Radar Measurements**](https://doi.org/10.1109/JSEN.2025.3594433) (2025) — Ferro, L. et al.
* [**Millimeter-Wave SAR imaging of Sparse Trajectory via Untrained Complex-valued Neural Network**](https://doi.org/10.1109/TAES.2025.3617036) (2025) — Hu, Tingkai et al.
* [**A near-field 30–40 GHz millimeter-wave phase imaging method for non-destructive testing and evaluation**](https://doi.org/10.1016/j.ndteint.2025.103529) (2026) — Yiming Ding et al.
* [**Synthetic Aperture Radar image analysis based on deep learning: A review of a decade of research**](https://doi.org/10.1016/j.engappai.2023.106305) (2023) — Alicia Passah et al.
* [**Multichannel Enhanced Millimeter-Wave SAR Imaging via Low-Rank Tensor-Train Decomposition**](https://doi.org/10.1109/JSTARS.2024.3509477) (2025) — Zhang, Bangjie et al.
* [**Active Multikernel Sparse Representation for Synthetic Aperture Radar Imaging**](https://doi.org/10.1109/TIM.2025.3550226) (2025) — Tong, X. and Wang, Y.

#### Material & Object Perception

* **Small Distance Increment Method for Measuring Complex Permittivity With mmWave Radar** (2025) — Song, H. et al.
* [**Characterization and Comparison of Piezoresistive Materials and Their Performance on Pressure-Sensitive Mats**](https://doi.org/10.1109/JSEN.2025.3614471) (2025) — Martínez-Cesteros, J. and others
* [**Nondestructive Testing of Debonding Defects in Radar Absorbing Materials Based on Microwave Pulse Thermography Method**](https://doi.org/10.1109/JSEN.2025.3582609) (2025) — Zhu, X. and others
* [**An Accelerated GSTC-Based Integral Equation Method Using Characteristic Basis Functions for Metasurface-Based Radar Absorbing Material**](https://doi.org/10.1109/LAWP.2025.3593991) (2025) — Kim, I. and others
* [**Permittivity Extraction From Synthetic Aperture Radar (SAR) Imagery**](https://doi.org/10.1109/TIM.2021.3113118) (2021) — Liu, C., Qaseer, M., and Zoughi, R.
* [**Mixture-Based Dielectric Permittivity Measurements Through Gallium-Liquid Metal-Loaded Radar Sensors**](https://doi.org/10.1109/TIM.2024.3428598) (2024) — Karatay, A. and Yaman, F.


---

## 💾 Representative Public Datasets & Repositories

| Dataset / Framework | Radar Representation | Primary Scenario | Task | Public Code & Data |
| :--- | :--- | :--- | :--- | :--- |
| **Talk2Radar** | 4D mmWave point clouds + LiDAR | Urban traffic / outdoor driving | 3D REC (Grounding) | [GitHub Repo](https://github.com/GuanRunwei/Talk2Radar) |
| **mmPencil** | 60 GHz 3D trajectory images | Indoor office | In-air handwriting | [Kaggle Dataset](https://www.kaggle.com/datasets/mmpencil/mmpencil-dataset) |
| **RadarLLM-Motion** | 4D mmWave point cloud sequences | Human motion capture | Motion understanding | [GitHub Repo](https://github.com/Inowlzy/RadarLLM) |
| **M²BeamLLM** | 77 GHz Range-Angle Maps + GPS + LiDAR | V2I Communication | mmWave Beam Prediction | [DeepSense 6G](https://deepsense6g.net/) |
| **Sig2text** | STFT Magnitude Spectrograms | Non-cooperative Intercept (EW) | Symbolic modulation parsing | [GitHub Repo](https://github.com/Na-choneko/sig2text) |
