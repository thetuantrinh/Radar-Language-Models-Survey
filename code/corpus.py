"""The analytical corpus: one row per included system, with its axis triple.

SINGLE SOURCE OF TRUTH.  Table I, the coverage matrix of Table IV, the
marginals quoted in Sec. III-E, the permutation nulls of taxonomy_null.py and
the domain counts of Table III are all derived from this list by
emit_corpus.py.  Nothing downstream is typed, because every drift defect this
manuscript has had came from a number written twice.

Provenance of the rows
----------------------
The 16 systems marked `r2=True` were assessed at full text for the previous
version and carry the axis assignments published there.  The 35 systems marked
`r2=False` were admitted by the eligibility assessment of
`assess_fulltext.py` over the re-executed retrieval, and **their axis triples
are assigned from the title and abstract, not from a full-text reading**.
Sec. III states this, and it is the honest limitation of a corpus that trebled
in one revision: the marginals are robust to a handful of misassignments (each
would require several to overturn), but no individual cell should be relied on.

Axis codes (Sec. III)
  L1 raw I/Q or array snapshots      M1  contrastive dual-encoder
  L2 2D spectral / profile / imagery M2  continuous projection
  L3 4D point cloud                  M3  discrete codebook
  L4 physics-distilled scalars       M4a physics-scalar serialization + RAG
                                     M4b prompt orchestration, frozen backbone
  T1 detection/counting/recognition  T4 intrinsic material/parameter
  T2 spatial grounding               T5 waveform/modulation parsing
  T3 kinematic/behavioural           T6 instrumentation & link control
"""

# name, key, year, venue, band/hardware, L, M, T, task, r2, family
#
# `key` is a BibTeX key for the 16 previously assessed systems, whose entries
# already exist in References.bib.  For the 35 newly admitted systems it is
# "T:<normalised title prefix>" -- a join key into prisma_assessment.csv.
# emit_corpus.py resolves it, retrieves the real byline, and derives the
# citation key from that.  Inventing a key from a guessed first author is
# exactly the defect round 7 found in the bibliography, and this is the
# structural fix for it: there is no place to write a name by hand.
SYSTEMS = [
    # ---- the 16 assessed for the previous version -------------------------
    ("Talk2Radar", "guan2024talk2radar", 2024, "arXiv + ICRA", "77\\,GHz 4D radar (View-of-Delft)", 3, "M2", 2, "3D referring expression comprehension", True, "inst"),
    ("LLMCount", "li2024llmcount", 2024, "arXiv", "60/77\\,GHz (TI IWR6843)", 2, "M4b", 1, "Stationary occupant counting", True, "inst"),
    ("RadarLLM-Motion", "lai2025radarllm", 2025, "arXiv + AAAI", "60\\,GHz FMCW / POI synthesis", 3, "M3", 3, "Human motion understanding", True, "inst"),
    ("RadarPLM-Marine", "hu2025radarllm", 2025, "arXiv + IGARSS", "9.4\\,GHz X-band (IPIX)", 2, "M2", 1, "Marine target detection", True, "inst"),
    ("LLMaterial", "zhu2025identify", 2025, "UbiComp Comp.", "77\\,GHz FMCW (TI AWR1843)", 4, "M4a", 4, "Material identification ($\\epsilon_r$, RCS)", True, "inst"),
    ("Robotic-VLM$^{\\ddagger}$", "deng2025robotic", 2025, "MobiCom poster", "77\\,GHz mmWave + RGB", 4, "M4a", 4, "Robotic material perception", True, "inst"),
    ("mmPencil", "guo2025mmpencil", 2025, "ACM IMWUT", "60\\,GHz FMCW (TI IWR6843ISK)", 3, "M1", 3, "In-air handwriting recognition", True, "inst"),
    ("WirelessGPT", "yang2025wirelessgpt", 2025, "IEEE JSAC", "28\\,GHz / sub-6\\,GHz array", 1, "M2", 6, "Multi-task ISAC foundation model", True, "inst"),
    ("MmExpert", "yan2025mmexpert", 2025, "ACM MobiHoc", "77\\,GHz FMCW (TI AWR1843)", 2, "M4b", 3, "Data synthesis and action understanding", True, "inst"),
    ("Radar2Text", "jauregui2025radar2text", 2025, "IEEE IMBioC", "77\\,GHz FMCW sensor", 2, "M2", 3, "Linguistic summarization of signatures", True, "inst"),
    ("M$^2$BeamLLM", "zheng2025m2beamllm", 2025, "arXiv", "60\\,GHz (DeepSense 6G)", 2, "M2", 6, "mmWave beam prediction", True, "inst"),
    ("ATRNet-SARCap", "gao2025multimodal", 2025, "IEEE JSTARS", "C/X-band SAR (Gaofen-3)", 2, "M2", 3, "SAR image captioning", True, "sar"),
    ("EW-Jamming VLM", "cao2025fewshot", 2025, "IEEE TAES", "1--18\\,GHz EW spectrograms", 2, "M1", 5, "Active jamming recognition", True, "inst"),
    ("Sig2text", "feng2025sig2text", 2025, "arXiv + IET RSN", "0.5--18\\,GHz EW receiver", 2, "M2", 5, "Non-cooperative signal parsing", True, "inst"),
    ("RFSensingGPT", "khan2026rfsensinggpt", 2026, "IEEE TCCN", "sub-6\\,GHz / mmWave 6G", 4, "M4a", 6, "RAG-enhanced sensing orchestration", True, "inst"),
    ("SARLANG-1M", "wei2026sarlang", 2026, "IEEE TGRS", "C-band SAR (Sentinel-1)", 2, "M1", 3, "SAR vision-language understanding", True, "sar"),

    # ---- 35 admitted by the re-executed retrieval --------------------------
    # SAR / microwave remote-sensing imagery (16)
    ("SARCLIP", "T:sarclipthefirstvisionlanguagefoundationmodel", 2025, "IEEE TGRS", "Spaceborne SAR", 2, "M1", 3, "SAR vision-language pre-training", False, "sar"),
    ("SARVLM", "T:sarvlmavisionlanguagefoundationmodel", 2025, "IEEE TGRS", "Spaceborne SAR", 2, "M2", 3, "SAR semantic understanding", False, "sar"),
    ("SAR-TEXT", "T:sartextalargescalesarimagetextdataset", 2025, "arXiv", "Spaceborne SAR", 2, "M1", 3, "SAR image--text corpus (130k pairs)", False, "sar"),
    ("SAREval", "T:sarevalamultidimensionalandmultitaskbenchmark", 2025, "arXiv", "Spaceborne SAR", 2, "M2", 3, "SAR VLM evaluation benchmark", False, "sar"),
    ("SSL-LIP", "T:ssllipatwostagepretrainingfoundationmodel", 2025, "IEEE JSTARS", "Spaceborne SAR", 2, "M1", 3, "Two-stage SAR VL pre-training", False, "sar"),
    ("RSVQA-SAR", "T:sarstrikesbackanewhopeforrsvqa", 2025, "arXiv", "VHR SAR", 2, "M2", 3, "Remote-sensing visual question answering", False, "sar"),
    ("SAR-RAG", "T:sarragatrvisualquestionanswering", 2026, "SPIE", "Spaceborne SAR", 2, "M4b", 1, "ATR visual question answering", False, "sar"),
    ("SAR-Caption Ranker", "T:sarcaptionrankeroptimizingautomaticsar", 2026, "arXiv", "Spaceborne SAR", 2, "M4b", 3, "RLAIF caption ranking", False, "sar"),
    ("SAR-GenTrans", "T:extendingsemanticinterpretationandvisual", 2026, "IEEE JSTARS", "Spaceborne SAR", 2, "M2", 3, "Semantic interpretation via translation", False, "sar"),
    ("TVLightFormer", "T:tvlightformeralightweightcrossmodal", 2026, "Remote Sens.", "Spaceborne SAR", 2, "M2", 2, "Language-guided target localization", False, "sar"),
    ("DGS-CapNet", "T:dgscapnetaspatialfrequencyawaremodel", 2026, "IEEE JSTARS", "Spaceborne SAR", 2, "M2", 3, "Spatial-frequency SAR captioning", False, "sar"),
    ("FSAR-Cap", "T:fsarcapafinegrainedtwostageannotated", 2026, "arXiv", "Spaceborne SAR (FAIR-CSAR)", 2, "M2", 3, "Fine-grained SAR captioning dataset", False, "sar"),
    ("InSAR-Chat", "T:chatwithpointllmdrivenvisualquestion", 2026, "IGARSS", "InSAR (EGMS)", 2, "M4b", 3, "InSAR deformation question answering", False, "sar"),
    ("InSAR-Cap", "T:generativeandretrievalimagecaptioning", 2026, "arXiv", "InSAR", 2, "M4b", 3, "InSAR captioning for geophysics", False, "sar"),
    ("PolSAR-VQA", "T:visualquestionansweringforwishart", 2024, "IGARSS", "Polarimetric SAR", 2, "M4b", 4, "Wishart H-$\\alpha$ scattering-type VQA", False, "sar"),
    ("SARShip-VQA", "T:avisualquestionansweringmethodforsarship", 2024, "IEEE GRSL", "Spaceborne SAR", 2, "M4b", 1, "Ship attribute question answering", False, "sar"),

    # Instrumentation-side systems (19)
    ("HRRP-Proto-LLM", "T:teachinglargelanguagemodelstoseeinradar", 2026, "IET RSN", "X-band HRRP", 2, "M2", 1, "Few-shot HRRP target recognition", False, "inst"),
    ("UWB-LLM", "T:uwbllmultrawidebandradarmultitaskingbased", 2026, "DOAJ (OA)", "Impulse UWB", 1, "M2", 1, "Counting, respiration and ECG", False, "inst"),
    ("mmWave-Bench", "T:canlanguagemodelsunderstandmmwavedata", 2026, "arXiv", "mmWave FMCW", 2, "M2", 3, "LLM benchmark for mmWave understanding", False, "inst"),
    ("RadarChat", "T:radarchatadvancingradarmodulation", 2026, "IET RSN", "Multi-band radar", 2, "M4b", 5, "Radar modulation recognition", False, "inst"),
    ("mmMind", "T:teachingfoundationmodelstoreadmmwave", 2026, "arXiv", "mmWave FMCW", 3, "M2", 3, "Pose-guided behaviour understanding", False, "inst"),
    ("SLM-CogRadar", "T:smalllanguagemodelenabledautonomousagent", 2026, "arXiv", "Synthetic ULA", 1, "M4b", 6, "Language-conditioned array processing", False, "inst"),
    ("RAGent", "T:ragentphysicsawareagenticreasoning", 2026, "arXiv", "mmWave FMCW", 2, "M4b", 3, "Training-free mmWave activity recognition", False, "inst"),
    ("RadarSigLIP", "T:weatherrobustscenesemanticswithvision", 2026, "arXiv", "4D radar (K-Radar)", 2, "M1", 3, "Weather-robust scene captioning", False, "inst"),
    ("PReD", "T:predanllmbasedfoundationmultimodalmodel", 2026, "arXiv", "Multi-band EM", 2, "M2", 5, "EM perception, recognition and decision", False, "inst"),
    ("PISPL", "T:physicsinformedsemanticpromptlearning", 2026, "Remote Sens.", "Low-altitude radar", 2, "M2", 1, "Few-shot low-altitude target recognition", False, "inst"),
    # Key carries the discriminating suffix "ofoverlappingsignals": the
    # 36-character prefix this row used until the present revision also
    # matches "Automatic LPI Radar Waveform Recognition Using Vision
    # Transformer" (2023, excluded under excl_ii), which sorts first in
    # prisma_assessment.csv and so captured the join.  See check_keys().
    ("LPI-VLM", "T:automaticlpiradarwaveformrecognitionofoverlappingsignals", 2025, "Sci. Rep.", "LPI microwave waveforms", 2, "M1", 5, "Overlapping LPI waveform recognition", False, "inst"),
    ("GPR-OFA", "T:guidinggptmodelsforspecificoneforall", 2025, "Autom. Constr.", "Ground-penetrating radar", 2, "M4b", 1, "One-for-all GPR interpretation", False, "inst"),
    ("RF-HAR-MLLM", "T:anovelmultimodalllmdrivenrfsensingmethod", 2025, "IEEE SPL", "RF sensing", 2, "M2", 3, "Human activity recognition", False, "inst"),
    ("RadarVLM", "T:rlmavisionlanguagemodelapproachforradar", 2025, "arXiv", "Simulated automotive radar", 2, "M2", 3, "Radar scene understanding", False, "inst"),
    ("CSLR-DeepSeek", "T:continuouschinesesignlanguagerecognition", 2025, "IEEE Sens. J.", "mmWave micro-Doppler", 2, "M4a", 3, "Continuous sign-language recognition", False, "inst"),
    ("Psyche-Wave", "T:psychewavefusingvectorquantizedmorphology", 2025, "IEEE BIBM", "mmWave SCG", 4, "M4a", 3, "Psychological state decoding", False, "inst"),
    ("RestAware", "T:restawarenoninvasivesleepmonitoring", 2025, "arXiv", "24\\,GHz FMCW", 4, "M4a", 3, "Sleep-posture monitoring and summary", False, "inst"),
    ("KEF-HRRP", "T:knowledgeembeddingfusionbasedonlanguagemodel", 2025, "IET RSN", "HRRP echoes", 2, "M2", 1, "Knowledge-fused target recognition", False, "inst"),
    ("PseudoText-JAM", "T:syntheticpseudotextaidedradarinterference", 2025, "IET RSN", "Radar interference", 2, "M1", 5, "Few-shot interference recognition", False, "inst"),
]

# The systems Table VIII reports an evaluation protocol for.  Every one is
# marked * in Table I (r2=True), but not every marked system is here: four of
# the sixteen report results in a form that reduces to no single comparable
# figure, so they carry the mark and are absent from Table VIII.  Sec. I-B
# quotes len(EVAL), never a typed number.
EVAL = [
    "Talk2Radar", "LLMCount", "RadarLLM-Motion", "RadarPLM-Marine",
    "LLMaterial", "mmPencil", "MmExpert", "M$^2$BeamLLM", "Sig2text",
    "ATRNet-SARCap", "SARLANG-1M", "RFSensingGPT",
]

MECHS = ["M1", "M2", "M3", "M4a", "M4b"]
LEVELS = [1, 2, 3, 4]
