"""Reproduce and print the tables from the survey manuscript in Markdown format.

Covers:
1. Coverage Matrix (L x M) across the 51 frameworks with marginals and statistical null test.
2. Table of all 51 included Radar-Language Frameworks (2024-2026).
3. Summary of marginals and core metrological findings.
"""
import os
import re
import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from corpus import SYSTEMS, MECHS, LEVELS

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "corpus_meta.json"), encoding="utf-8") as f:
    META = json.load(f)

def get_system_link(name, key, r2):
    # Direct mappings for the 16 full-text systems
    KNOWN_URLS = {
        "Talk2Radar": "https://arxiv.org/abs/2405.12821",
        "LLMCount": "https://arxiv.org/abs/2409.16209",
        "RadarLLM-Motion": "https://arxiv.org/abs/2504.09862",
        "RadarPLM-Marine": "https://arxiv.org/abs/2509.12089",
        "LLMaterial": "https://doi.org/10.1145/3714394.3756289",
        "Robotic-VLM$^{\\ddagger}$": "https://doi.org/10.1145/3680207.3765653",
        "mmPencil": "https://doi.org/10.1145/3749504",
        "WirelessGPT": "https://doi.org/10.1109/JSAC.2025.3640156",
        "MmExpert": "https://doi.org/10.1145/3704413.3764420",
        "Radar2Text": "https://doi.org/10.1109/IMBioC63524.2025.10989725",
        "M$^2$BeamLLM": "https://arxiv.org/abs/2506.14532",
        "ATRNet-SARCap": "https://doi.org/10.1109/JSTARS.2025.3603036",
        "EW-Jamming VLM": "https://doi.org/10.1109/TAES.2025.3586834",
        "Sig2text": "https://arxiv.org/abs/2503.15213",
        "RFSensingGPT": "https://doi.org/10.1109/TCCN.2025.3558069",
        "SARLANG-1M": "https://doi.org/10.1109/TGRS.2026.3652099",
        "UWB-LLM": "https://doi.org/10.1049/icp.2026.1107", # or DOAJ OA
        "InSAR-Chat": "https://doi.org/10.1109/IGARSS53475.2024.10641895",
    }
    clean_name = name.replace("$^{\\ddagger}$", "").replace("$^2$", "2")
    if name in KNOWN_URLS:
        return KNOWN_URLS[name]
    if clean_name in KNOWN_URLS:
        return KNOWN_URLS[clean_name]
    
    if key.startswith("T:"):
        pref = key[2:]
        if pref in META:
            doi = META[pref].get("doi", "")
            if doi:
                if doi.startswith("http"):
                    return doi
                return f"https://doi.org/{doi}"
    return None

def generate_markdown_table():
    lines = []
    lines.append("| System | Venue | Yr | RF Band / Hardware | L | M | T | Primary Measurement Task | Full Text? |")
    lines.append("| :--- | :---: | :---: | :--- | :---: | :---: | :---: | :--- | :---: |")
    
    lines.append("| **Instrumentation-Side Frameworks** | | | | | | | | |")
    for s in SYSTEMS:
        name, key, yr, venue, band, L, M, T, task, r2, fam = s
        if fam != "inst":
            continue
        clean_name = name.replace("$^{\\ddagger}$", "‡").replace("$^2$", "²").replace("\\,", " ")
        clean_band = band.replace("\\,", " ").replace("\\", "")
        clean_task = task.replace("$\\epsilon_r$", "εr")
        url = get_system_link(name, key, r2)
        link_str = f"[{clean_name}]({url})" if url else clean_name
        ft_str = "● Yes" if r2 else "○ Abs"
        lines.append(f"| {link_str} | {venue} | {yr} | {clean_band} | L{L} | {M} | T{T} | {clean_task} | {ft_str} |")

    lines.append("| **Microwave Remote-Sensing / SAR Imagery Frameworks** | | | | | | | | |")
    for s in SYSTEMS:
        name, key, yr, venue, band, L, M, T, task, r2, fam = s
        if fam != "sar":
            continue
        clean_name = name.replace("$^{\\ddagger}$", "‡").replace("$^2$", "²").replace("\\,", " ")
        clean_band = band.replace("\\,", " ").replace("\\", "")
        clean_task = task.replace("$\\epsilon_r$", "εr").replace("$-\\alpha$", "-α")
        url = get_system_link(name, key, r2)
        link_str = f"[{clean_name}]({url})" if url else clean_name
        ft_str = "● Yes" if r2 else "○ Abs"
        lines.append(f"| {link_str} | {venue} | {yr} | {clean_band} | L{L} | {M} | T{T} | {clean_task} | {ft_str} |")

    return "\n".join(lines)

def generate_coverage_matrix():
    matrix = {(l, m): 0 for l in LEVELS for m in MECHS}
    matrix_l2a = {m: 0 for m in MECHS}
    matrix_l2b = {m: 0 for m in MECHS}
    
    for s in SYSTEMS:
        l, m, fam = s[5], s[6], s[10]
        matrix[(l, m)] += 1
        if l == 2:
            if fam == "inst":
                matrix_l2a[m] += 1
            else:
                matrix_l2b[m] += 1
                
    lines = []
    lines.append("| Abstraction Level (L) | M1 Contr. | M2 Proj. | M3 Code | M4a Scalar+RAG | M4b Prompt Orch. | Total |")
    lines.append("| :--- | :---: | :---: | :---: | :---: | :---: | :---: |")
    
    names = {1: "**L1** Raw Complex I/Q", 2: "**L2** 2D Spectral / Focused", 3: "**L3** 4D Point Cloud", 4: "**L4** Physics Scalars"}
    
    for l in [1, 2, 3, 4]:
        cells = [matrix[(l, m)] for m in MECHS]
        cell_strs = [str(c) if c > 0 else "—" for c in cells]
        tot = sum(cells)
        lines.append(f"| {names[l]} | {' | '.join(cell_strs)} | **{tot}** |")
        if l == 2:
            l2a_cells = [str(matrix_l2a[m]) if matrix_l2a[m] > 0 else "—" for m in MECHS]
            l2b_cells = [str(matrix_l2b[m]) if matrix_l2b[m] > 0 else "—" for m in MECHS]
            lines.append(f"| ↳ *L2a Author-Derived* (Coherent Data) | {' | '.join(l2a_cells)} | *{sum(matrix_l2a.values())}* |")
            lines.append(f"| ↳ *L2b Distributed Product* (Spaceborne SAR) | {' | '.join(l2b_cells)} | *{sum(matrix_l2b.values())}* |")
            
    m_tots = [sum(matrix[(l, m)] for l in LEVELS) for m in MECHS]
    lines.append(f"| **Total** | **{'** | **'.join(str(t) for t in m_tots)}** | **{len(SYSTEMS)}** |")
    return "\n".join(lines)

if __name__ == "__main__":
    print("=== Coverage Matrix ===")
    print(generate_coverage_matrix())
    print("\n=== Corpus Table (First 15 lines) ===")
    print("\n".join(generate_markdown_table().splitlines()[:15]))
