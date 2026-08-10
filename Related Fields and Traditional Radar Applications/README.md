# 🛠️ Related Fields and Traditional Radar Applications

This directory contains a comprehensive overview and survey of traditional millimeter-wave (mmWave) radar sensing applications and recent technical advancements (2021–2026), serving as background and related literature for Radar–Language Models (RLMs).

---

## 🛠️ Summary of mmWave Radar Sensing Applications and Recent Advancements (2021–2026)

| Application Area | Radar Modality | Key Technical Focus | Year | Representative Works / Citations |
| :--- | :--- | :--- | :---: | :--- |
| **Human Activity Recognition** | 4D Point Cloud / Micro-Doppler | Multi-link channel robustness, in-memory computing for healthcare, TinyML implementations, and non-line-of-sight (NLOS) spectrogram analysis. | 2022–2026 | [Miazek, et al. (2024)](https://doi.org/10.1109/ACCESS.2024.3474100), [Li, et al. (2023)](https://doi.org/10.1038/s41598-023-30631-x), [Kurtoğlu, et al. (2025)](https://doi.org/10.1109/THMS.2025.3591369), [Wang, et al. (2025)](https://doi.org/10.1109/OJAP.2025.3638652), [Nikpour, et al. (2025)](https://doi.org/10.1109/TNNLS.2024.3360990), [Ji, et al. (2026)](https://doi.org/10.1109/JBHI.2024.3392648), [Hossan, et al. (2025)](https://doi.org/10.1109/LES.2025.363994), [Ding, et al. (2025)](https://doi.org/10.1109/TAES.2025.3579771), [Wang, et al. (2025)](https://doi.org/10.1109/JIOT.2025.3580799), [Hu, et al. (2025)](https://doi.org/10.1109/TIM.2025.3558216), [Zhang, et al. (2024)](https://doi.org/10.1109/TIM.2024.3365155) |
| **Human / Hand / Skeleton Pose Estimation** | Sparse Point Clouds / Raw Cubes | Transformer-based end-to-end estimation, skeletal probability map-guided fusion, egocentric radar-IMU integration, and RF vision for occluded hands. | 2023–2026 | [Zhou, et al. (2025)](https://doi.org/10.1109/TIM.2025.3538102), [Chen, et al. (2026)](https://doi.org/10.1109/JIOT.2026.3651437), [Dong, et al. (2026)](https://doi.org/10.1109/JSEN.2026.3650914), [Engel, et al. (2025)](https://doi.org/10.1109/JMW.2025.3535525), [Chen, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3542078), [Zhu, et al. (2025)](https://doi.org/10.1109/TAES.2025.3594328), [Wu, et al. (2025)](https://doi.org/10.1109/JIOT.2024.3476350), [Shi, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3577772), [Xu, et al. (2024)](https://doi.org/10.1109/JIOT.2023.3312316), [Lv, et al. (2025)](https://doi.org/10.48550/arXiv.2501.13805), [Yuan, et al. (2026)](https://doi.org/10.1145/3793858), [Yuanzhi et al. (2026)](https://doi.org/10.1016/j.measurement.2025.118851), [Li, et al. (2024)](https://doi.org/10.1145/3625687.3625799), [Sun, et al. (2026)](https://doi.org/10.1109/TIM.2026.3712914), [Chen, et al. (2025)](https://doi.org/10.1109/TIM.2025.3569914), [Trinh, et al. (2026)](https://doi.org/10.1109/JSEN.2026.3686129) |
| **People Counting & Occupancy** | Stationary / 4D mmWave | Stationary detection via Multimodal-LLMs, hybrid DCNN-transfer learning for clutter mitigation, and door open-close discrimination. | 2023–2025 | [Mboyi et al. (2025)](https://doi.org/10.1109/TIM.2025.3545718), [Yang, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3609465), [Vales, et al. (2024)](https://doi.org/10.1109/JIOT.2024.3434707), [Ren, et al. (2023)](https://doi.org/10.1109/JIOT.2023.3282797), [Martin-Martin, et al. (2025)](https://doi.org/10.1109/ACCESS.2025.3557317), [Cheng, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3577228), [Shenglei et al. (2023)](https://doi.org/10.1016/j.ifacol.2023.10.577), [Mauro, et al. (2023)](https://doi.org/10.1007/s10489-023-04778-z), [Ange et al. (2024)](https://doi.org/10.1016/j.sasc.2024.200095) |
| **Vital Sign & Health Monitoring** | FMCW Phase / Higher Harmonics | Nonlinear spectral approaches for heartbeat estimation, mitigation of respiration harmonics, and missing data models for body movement robustness. | 2022–2025 | [Li, et al. (2024)](https://doi.org/10.1109/TIM.2024.3476545), [Singh, et al. (2024)](https://doi.org/10.1109/THMS.2024.3381074), [Shirazi, et al. (2025)](https://doi.org/10.1016/j.measurement.2025.117707), [Qiao, et al. (2025)](https://doi.org/10.1109/TIM.2025.3547495), [Park, et al. (2025)](https://doi.org/10.1109/JSEN.2024.3491753), [Shimomura, et al. (2025)](https://doi.org/10.1109/LMWT.2025.3650557), [En-Kang et al. (2025)](https://doi.org/10.1016/j.measurement.2024.116144), [Wang, et al. (2024)](https://doi.org/10.1109/TMC.2023.3288850), [Grisot, et al. (2023)](https://doi.org/10.1109/TRS.2023.3298348), [Jiang, et al. (2024)](https://doi.org/10.1109/TAES.2024.3379492), [Vilesov, et al. (2022)](https://doi.org/10.1145/3528223.3530161), [Xu, et al. (2024)](https://doi.org/10.1109/TIM.2024.3450071) |
| **Hand Gesture & Sign Language** | Micro-Doppler / UWB / Range-Doppler | Continuous Chinese sign language via DeepSeek semantic enhancement, uncertainty-aware deep learning, and cumulative distribution density features. | 2020–2026 | [Chen, et al. (2026)](https://doi.org/10.1109/TIM.2025.3637962), [Han, et al. (2025)](https://doi.org/10.1109/TIM.2025.3582311), [Wang, et al. (2021)](https://doi.org/10.1109/THMS.2020.3036637), [Qiu, et al. (2024)](https://doi.org/10.4236/jcc.2024.126008), [Jin, et al. (2024)](https://doi.org/10.1109/THMS.2024.3385124), [Zhang, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3599380), [Lin, et al. (2026)](https://doi.org/10.1109/JIOT.2025.3644894), [Trinh, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3573743), [Li, et al. (2021)](https://doi.org/10.1109/TIM.2021.3092072), [Li, et al. (2023)](https://doi.org/10.1109/TGRS.2023.3278298), [Jiayi et al. (2025)](https://doi.org/10.1016/j.measurement.2025.117545), [Yu, et al. (2022)](https://doi.org/10.1109/THMS.2022.3149408), [Trinh, et al. (2023)](https://doi.org/10.1109/ICCAIS59597.2023.10382331), [Chen, et al. (2026)](https://doi.org/10.3390/electronics15020437), [Towakel, et al. (2023)](https://doi.org/10.1109/TIM.2023.3307768), [Han, et al. (2025)](https://doi.org/10.1109/TIM.2025.3582311), [Trinh, et al. (2026)](https://doi.org/10.1109/TAES.2026.3709269) |
| **Air-Writing & Handwriting** | FMCW / Acoustic-Radar | Writing-style-independent recognition, alphanumeric gesture classification, and optimized ResYOLO-Transformers. | 2024–2025 | [Arsalan, et al. (2024)](https://doi.org/10.1007/978-3-658-45318-3_4), [Satti, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3645357), [Kim, et al. (2025)](https://doi.org/10.1109/TIM.2025.3573779), [Pan, et al. (2025)](https://doi.org/10.1109/TMC.2025.3526185), [Lamaakal, et al. (2026)](https://doi.org/10.1109/JIOT.2025.3624283), [Tian, et al. (2025)](https://doi.org/10.1109/JIOT.2024.3507369), [Huang, et al. (2025)](https://doi.org/10.1007/978-3-031-78104-9_29) |
| **Target Detection & Recognition** | Graph Fourier / IQ Signals | Marine target detection with preference-aware loss, zero-shot active jamming recognition, and spatial-temporal graph transforms. | 2021–2026 | [Wee, et al. (2021)](https://doi.org/10.1109/THMS.2021.3076044), [Salehi, et al. (2024)](https://doi.org/10.1109/TCCN.2024.3391327), [Lian, et al. (2025)](https://doi.org/10.1109/TAES.2024.3510687), [Jingang et al. (2025)](https://doi.org/10.1016/j.sigpro.2025.110034), [Chen, et al. (2026)](https://doi.org/10.1109/JMASS.2026.3656926), [Nikaein, et al. (2026)](https://doi.org/10.1109/TRS.2026.3658846), [Zeng, et al. (2024)](https://doi.org/10.1109/TIM.2024.3400347) |
| **Imaging, SAR & Displacement** | Complex Phase / SAR | Joint phase-envelope autofocus for backprojection, SAR image captioning via multimodal large models, and real-time displacement evaluation. | 2021–2026 | [Lee, et al. (2025)](https://doi.org/10.1109/TIM.2025.3551416), [Wan, et al. (2025)](https://doi.org/10.1109/LGRS.2025.3580587), [Xie, et al. (2022)](https://doi.org/10.3390/s22155757), [Ferro, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3594433), [Hu, et al. (2025)](https://doi.org/10.1109/TAES.2025.3617036), [Yiming et al. (2026)](https://doi.org/10.1016/j.ndteint.2025.103529), [Alicia et al. (2023)](https://doi.org/10.1016/j.engappai.2023.106305), [Zhang, et al. (2025)](https://doi.org/10.1109/JSTARS.2024.3509477), [Tong, et al. (2025)](https://doi.org/10.1109/TIM.2025.3550226) |
| **Material & Object Perception** | Sub-THz / Microwave Pulse | Sub-THz classification for ISAC, nondestructive testing of debonding defects, and complex permittivity extraction. | 2021–2025 | [Song, et al. (2025)](https://doi.org/10.1109/TIM.2025.3584141), [Martínez-Cesteros, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3614471), [Zhu, et al. (2025)](https://doi.org/10.1109/JSEN.2025.3582609), [Kim, et al. (2025)](https://doi.org/10.1109/LAWP.2025.3593991), [Liu, et al. (2021)](https://doi.org/10.1109/TIM.2021.3113118), [Karatay, et al. (2024)](https://doi.org/10.1109/TIM.2024.3428598) |

---

### 🛠️ Recent Advancements in mmWave Radar Sensing Literature (2021–2026)

#### Human Activity Recognition

* [**Human Behavior Analysis Using Radar Data: A Survey**](https://doi.org/10.1109/ACCESS.2024.3474100) (2024) — Miazek, Patrycja et al.
* [**Radar-based human activity recognition with adaptive thresholding towards resource constrained platforms**](https://doi.org/10.1038/s41598-023-30631-x) (2023) — Li, Zhenghui et al.
* [**Human-Centered Fully Adaptive Radar for Gesture Recognition in Smart Environments**](https://doi.org/10.1109/THMS.2025.3591369) (2025) — Kurtoğlu, Emre and Gurbuz, Sevgi Z.
* [**Performance Enhancement of Human Activity Recognition Using Millimeter-Wave Multi-Link Channels**](https://doi.org/10.1109/OJAP.2025.3638652) (2025) — Wang, Y. et al.
* [**Deep Reinforcement Learning in Human Activity Recognition: A Survey and Outlook**](https://doi.org/10.1109/TNNLS.2024.3360990) (2025) — Nikpour, B., Sinodinos, D., and Armanfard, N.
* [**An Efficient Human Activity Recognition In-Memory Computing Architecture Development for Healthcare Monitoring**](https://doi.org/10.1109/JBHI.2024.3392648) (2026) — Ji, X. and others
* [**TinyHAR-Net: Design and Implementation of a TinyML-Based Human Activity Recognition Framework on STM32**](https://doi.org/10.1109/LES.2025.363994) (2025) — Hossan, I., Mary, M. N. J., and Motin, M. A.
* [**A Non-Line-of-Sight Human Activity Recognition Method Based on Radar Multispectrogram**](https://doi.org/10.1109/TAES.2025.3579771) (2025) — Ding, C. and others
* [**Crucial Region Search and Feature Discrimination for Radar-Based Human Activity Recognition**](https://doi.org/10.1109/JIOT.2025.3580799) (2025) — Wang, D. et al.
* [**Human Activity Recognition Trained on Simulated Millimeter-Wave Radar Data**](https://doi.org/10.1109/TIM.2025.3558216) (2025) — Hu, Y. et al.
* [**Multi-STMT: Multi-Level Network for Human Activity Recognition Based on mmWave Radar**](https://doi.org/10.1109/TIM.2024.3365155) (2024) — Zhang, H. and Xu, L.

#### Human / Hand / Skeleton Pose Estimation

* [**Learning to Analyze Human Skeletal by Radar-Camera Supervision**](https://doi.org/10.1109/TIM.2025.3538102) (2025) — Zhou, Y. et al.
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

* [**RadarNet: Non-Contact ECG Signal Measurement Based on FMCW Radar**](https://doi.org/10.1109/TIM.2024.3476545) (2024) — Li, B. et al.
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

* [**Domain-Generalized Gesture Recognition via mmWave Radar Signal Multiview Learning**](https://doi.org/10.1109/TIM.2025.3637962) (2026) — Chen, Q. et al.
* [**A Robust Real-Time Multiuser Gesture Recognition System for Human--Computer Interaction Using mmWave Radar Sensors**](https://doi.org/10.1109/TIM.2025.3582311) (2025) — Han, W., Hasan, K., and Yuce, M. R.
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

* [**Integration of mmWave FMCW Radar and Stereo Camera for 3D Automotive SAR Imaging**](https://doi.org/10.1109/TIM.2025.3551416) (2025) — Lee, H. et al.
* [**Phase-Envelope Joint Autofocus Algorithm for Backprojection Imaging**](https://doi.org/10.1109/LGRS.2025.3580587) (2025) — Wan, B. and others
* [**Resolution Enhancement for Millimeter-Wave Radar ROI Image with Bayesian Compressive Sensing**](https://doi.org/10.3390/s22155757) (2022) — Xie, P. and others
* [**An Insight Into the Displacement Evaluation During Real-Time Radar Measurements**](https://doi.org/10.1109/JSEN.2025.3594433) (2025) — Ferro, L. et al.
* [**Millimeter-Wave SAR imaging of Sparse Trajectory via Untrained Complex-valued Neural Network**](https://doi.org/10.1109/TAES.2025.3617036) (2025) — Hu, Tingkai et al.
* [**A near-field 30–40 GHz millimeter-wave phase imaging method for non-destructive testing and evaluation**](https://doi.org/10.1016/j.ndteint.2025.103529) (2026) — Yiming Ding et al.
* [**Synthetic Aperture Radar image analysis based on deep learning: A review of a decade of research**](https://doi.org/10.1016/j.engappai.2023.106305) (2023) — Alicia Passah et al.
* [**Multichannel Enhanced Millimeter-Wave SAR Imaging via Low-Rank Tensor-Train Decomposition**](https://doi.org/10.1109/JSTARS.2024.3509477) (2025) — Zhang, Bangjie et al.
* [**Active Multikernel Sparse Representation for Synthetic Aperture Radar Imaging**](https://doi.org/10.1109/TIM.2025.3550226) (2025) — Tong, X. and Wang, Y.

#### Material & Object Perception

* [**Small Distance Increment Method for Measuring Complex Permittivity With mmWave Radar**](https://doi.org/10.1109/TIM.2025.3584141) (2025) — Song, H. et al.
* [**Characterization and Comparison of Piezoresistive Materials and Their Performance on Pressure-Sensitive Mats**](https://doi.org/10.1109/JSEN.2025.3614471) (2025) — Martínez-Cesteros, J. and others
* [**Nondestructive Testing of Debonding Defects in Radar Absorbing Materials Based on Microwave Pulse Thermography Method**](https://doi.org/10.1109/JSEN.2025.3582609) (2025) — Zhu, X. and others
* [**An Accelerated GSTC-Based Integral Equation Method Using Characteristic Basis Functions for Metasurface-Based Radar Absorbing Material**](https://doi.org/10.1109/LAWP.2025.3593991) (2025) — Kim, I. and others
* [**Permittivity Extraction From Synthetic Aperture Radar (SAR) Imagery**](https://doi.org/10.1109/TIM.2021.3113118) (2021) — Liu, C., Qaseer, M., and Zoughi, R.
* [**Mixture-Based Dielectric Permittivity Measurements Through Gallium-Liquid Metal-Loaded Radar Sensors**](https://doi.org/10.1109/TIM.2024.3428598) (2024) — Karatay, A. and Yaman, F.

