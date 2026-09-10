# NDMC BSCS Thesis Research Workspace

<div align="center">

### **Notre Dame of Midsayap College**
**College of Information Technology and Engineering (CITE)**  
*Bachelor of Science in Computer Science (BSCS)*

---

## **Receipt or Deceit: A Cross-Architecture Analysis of Convolutional Neural Network Models in Detecting Forged Digital Transaction Receipts**

**System Name:** ForgeGuard  
**Academic Subject:** CS Thesis Writing 1 (A.Y. 2026–2027)

---

[![Thesis Status](https://img.shields.io/badge/Proposal-Chapters_1_%26_2_Completed-007ACC?style=for-the-badge)](thesis-docs/THESIS1UNGAB_BACANTO.md)
[![Title Defense](https://img.shields.io/badge/Title_Defense-PASSED-10B981?style=for-the-badge)](thesis-docs/)
[![Live System Demo](https://img.shields.io/badge/Live_System-forgeguard.streamlit.app-8B5CF6?style=for-the-badge&logo=streamlit)](https://forgeguard.streamlit.app/)
[![System Repo](https://img.shields.io/badge/System_Repo-DeathKnell837%2FForgeGuard-1E293B?style=for-the-badge&logo=github)](https://github.com/DeathKnell837/ForgeGuard)
[![Google Drive](https://img.shields.io/badge/Google_Drive-Thesis_Archive-F59E0B?style=for-the-badge&logo=googledrive)](https://drive.google.com/drive/folders/1bzRsI6Ywo2yRni5Ij7InCLh0CL0OO90_?usp=drive_link)

[Latest Manuscript (Word)](thesis-docs/THESIS1UNGAB_BACANTO.docx) &bull; [Latest Manuscript (Markdown)](thesis-docs/THESIS1UNGAB_BACANTO.md) &bull; [System Architecture](thesis-docs/forgeguard_system_architecture.svg) &bull; [Live Demo](https://forgeguard.streamlit.app/)

</div>

---

## Research Group & Faculty Profile

| Role | Name | Designation / Affiliation |
|:---|:---|:---|
| **Lead Researcher** | **Daniela S. Ungab** | BSCS-4 Student Candidate, NDMC CITE |
| **Co-Researcher** | **Rogie P. Bacanto** | BSCS-4 Student Candidate, NDMC CITE |
| **Thesis Adviser** | **Ms. Doris Ann Mariano** | Faculty Adviser, NDMC CITE |
| **Research Teacher** | **Mr. Nero L. Hontiveros** | CS Thesis Writing 1 Instructor |
| **Dean of CITE** | **Engr. Mark Bryan C. Tenebroso, PCPE, ME-CPE** | Dean, College of Information Technology & Engineering |
| **Academic Term** | **Academic Year 2026–2027** | CS Thesis Writing 1 (Enrolled, June 2026) |

---

### Research Overview & Abstract

Digital payment channels account for over **57.4% of monthly retail transactions** in the Philippines (Bangko Sentral ng Pilipinas 2024 Report). However, peer-to-peer mobile wallet confirmation receipts (specifically within the **GCash** ecosystem) have become a primary attack surface for receipt-based fraud. Scammers utilize image editing tools and programmatic template generators to modify transaction amounts, reference numbers, and recipient names without transferring actual funds.

Because proof-of-payment receipts shared over messaging platforms (Facebook Messenger) undergo lossy re-compression, conventional visual inspection and raw Error Level Analysis (ELA) frequently fail to expose subtle tampering. 

This study addresses this challenge through a **cross-architecture comparative evaluation of three Convolutional Neural Network (CNN) architectures**:
1. **Basic CNN (Custom sequential baseline, ~2.1M parameters)**
2. **MobileNetV2 (Inverted residual mobile architecture, ~3.4M parameters)**
3. **ResNet50 (Deep 50-layer residual network, ~23.5M parameters)**

Each architecture is evaluated across both **Standard (high-resolution downloadable)** and **Compressed (Facebook Messenger re-compressed)** conditions across accuracy, precision, recall, F1-score, steady-state latency, and peak memory footprint.

---

## Statement of the Problem (SOP)

This research investigates the following specific research questions:

1. **Classification Performance:**
   * What is the diagnostic performance of Basic CNN, ResNet50, and MobileNetV2 in terms of **Accuracy**, **Precision**, **Recall**, and **F1-score**?
2. **Detection by Forgery Modality:**
   * What is the accuracy of each architecture across digitally edited receipts (amount, recipient name, reference number, font tampering) versus programmatically generated fake receipts?
3. **Computational Efficiency & Resource Footprint:**
   * What is the difference in **inference speed (ms)**, **peak memory (MB)**, and model footprint among the three architectures?
4. **Resilience to Messaging Platform Compression:**
   * Does social media compression (Facebook Messenger transmission) degrade or alter the detection efficacy of the CNN models?
5. **Practical Edge Deployability:**
   * Which CNN architecture provides the optimal balance of classification accuracy and execution latency for real-time mobile payment verification?

---

## Empirical Model Benchmark Results

All architectures were benchmarked under identical hardware conditions on the balanced 1:1 empirical dataset across both Standard and Compressed conditions:

| Architecture | Condition | Accuracy (%) | Compression Delta (&Delta;Acc) | Precision (%) | Recall (%) | F1-Score (%) | Latency (ms) | Peak Memory (MB) | Params | Architectural Finding |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **Basic CNN** | Standard | **92.92%** | Baseline | **98.99%** | **86.73%** | **92.45%** | **22.51 ms** | **626.5 MB** | **~2.1M** | Most balanced, dependable model for uncompressed receipts; near-zero false alarms (FP=2 of 226). |
| **Basic CNN** | Compressed | **99.56%** | **+6.64%** | **99.56%** | **99.56%** | **99.56%** | **24.12 ms** | **638.3 MB** | **~2.1M** | Top-performing architecture under Messenger compression; only 2 errors across all 456 tested receipts. |
| **MobileNetV2** | Standard | **86.06%** | Baseline | **89.76%** | **81.42%** | **85.38%** | **215.75 ms** | **632.2 MB** | **~3.4M** | Inverted residual mobile architecture; lightweight ~3.4M parameter footprint for mobile edge devices. |
| **MobileNetV2** | Compressed | **93.42%** | **+7.36%** | **92.67%** | **94.30%** | **93.48%** | **221.40 ms** | **638.3 MB** | **~3.4M** | Strong resilience under compression with 94.30% fraud catch rate (TP=215 of 228). |
| **ResNet50** | Standard | **53.54%** | Baseline | **51.83%** | **100.00%** | **68.28%** | **395.03 ms** | **638.0 MB** | **~23.5M** | 100% recall on forgeries, but excessive false alarms (FP=210 of 226) due to deep-layer noise overfitting. |
| **ResNet50** | Compressed | **53.95%** | **+0.41%** | **52.05%** | **100.00%** | **68.47%** | **405.18 ms** | **638.8 MB** | **~23.5M** | Heavy 23.5M footprint; proves the hypothesis that excessive layer depth over-analyzes routine background noise. |

> **Key Takeaway:** Simpler, compact convolutional architectures (Basic CNN and MobileNetV2) decisively outperform heavy 50-layer deep networks for ELA digital receipt verification, proving that excessive network depth over-fits to normal compression variance and produces untenable false-positive rates.

---

## Dual Repository Architecture & Boundary Rules

To ensure clean separation between academic thesis documentation and live software engineering deployment, this research maintains two synchronized Git remotes:

| Remote | Target Repository | Scope & Purpose |
|:---|:---|:---|
| **`origin`** | [`DeathKnell837/NDMC-BSCS-THESIS-PREP`](https://github.com/DeathKnell837/NDMC-BSCS-THESIS-PREP) | **Academic Thesis Preparation Repository.** Contains all proposal documents (`thesis-docs/`), thesis manuscripts (`.docx` & `.md`), IEEE literature reviews, defense slides, guidelines, and research outlines. |
| **`forgeguard`** | [`DeathKnell837/ForgeGuard`](https://github.com/DeathKnell837/ForgeGuard) | **Software Engineering & Deployment Repository.** Contains the production Streamlit web application (`app.py`), serialized `.keras` models, ELA preprocessing engine, dataset generator tools, and deployment configs for [forgeguard.streamlit.app](https://forgeguard.streamlit.app/). |

### Non-Interference Push Policy
1. **Thesis Documentation updates** (`thesis-docs/`, manuscripts, proposal writing) must always be committed and pushed to `origin`.
2. **System & Webapp updates** (`thesis-system/`, models, UI components) are synced to `origin` (for complete archival) and pushed to `forgeguard` (for live Streamlit Cloud rebuilds).
3. The root `README.md` in `origin` represents the **Academic Thesis Workspace Hub**, while the root `README.md` in `forgeguard` represents the **ForgeGuard Software System Guide**.

---

## Workspace Directory Structure

```
THESIS/
├── README.md                           # Master Academic Workspace Hub (this file)
├── app.py                              # Streamlit Cloud deployment entrypoint
├── requirements.txt                    # System Python runtime dependencies
├── deploy-forgeguard.ps1               # Automated dual-remote deployment script
├── .agents/                            # Antigravity assistant customization rules
│   └── AGENTS.md                       # Canonical rules, boundary policies & thesis context
├── thesis-docs/                        # ACADEMIC THESIS DOCUMENTATION (Manuscripts & Guidelines)
│   ├── THESIS1UNGAB_BACANTO.docx       # Official compiled Chapters 1 & 2 Word Document
│   ├── THESIS1UNGAB_BACANTO.md         # Full Markdown transcript of latest manuscript
│   ├── Chapter1_Digital_Deception_Mobile_Wallet.md
│   ├── Chapter2_Review_of_Related_Literature.md
│   ├── Chapter3_System_Architecture_and_Methodology.md
│   ├── SECURING MOBILE TRANSACTIONS (1).pptx # Defense presentation slides
│   ├── bscs_thesis_guidelines.md       # NDMC CITE BSCS Thesis formatting standards
│   ├── student_info.md                 # Student profiles & thesis timeline
│   └── forgeguard_system_architecture.svg
└── thesis-system/                      # SYSTEM IMPLEMENTATION & EXPERIMENTAL PIPELINE
    ├── README.md                       # ForgeGuard Software System Guide
    ├── dataset/                        # Empirical Dataset (1:1 balanced evaluation: 456 base receipts)
    │   ├── authentic/                  # 228 authentic receipts (highres & compressed)
    │   └── forged/                     # 849 forged receipts (stratified attack vectors)
    ├── models/                         # Serialized weights (.keras) & evaluation_metrics.json
    ├── preprocessing/                  # Error Level Analysis (ELA) signal pipeline
    ├── generator/                      # GCash template synthesis engine
    └── webapp/                         # Streamlit application source & premium CSS
```

---

## Key Academic Thesis Documents

* **[Master Defense Study & System Guide (PDF)](thesis-docs/FORGEGUARD_MASTER_DEFENSE_GUIDE.pdf)** — All-in-One comprehensive study guide, plain-English translator, proposal ground truth, system guide, and presentation script.
* **[Master Defense Study & System Guide (Markdown)](thesis-docs/FORGEGUARD_MASTER_DEFENSE_GUIDE.md)** — Readable Markdown edition of the all-in-one master defense guide for instant viewing in code editors.
* **[Official Thesis Manuscript (Word)](thesis-docs/THESIS1UNGAB_BACANTO.docx)** — Complete Chapters 1 and 2 manuscript submitted for review (September 2026).
* **[Official Thesis Manuscript (Markdown)](thesis-docs/THESIS1UNGAB_BACANTO.md)** — Accessible Markdown version of the compiled manuscript.
* **[Chapter 1: Background & Problem Statement](thesis-docs/Chapter1_Digital_Deception_Mobile_Wallet.md)** — Detailed introduction, research gap, SOP, and SDG alignment.
* **[Chapter 2: Review of Related Literature](thesis-docs/Chapter2_Review_of_Related_Literature.md)** — Comprehensive 7-stage thematic synthesis with IEEE citations.
* **[Chapter 3: System Architecture & Methodology](thesis-docs/Chapter3_System_Architecture_and_Methodology.md)** — Five-tier forensic pipeline and CNN evaluation framework.
* **[BSCS Thesis Guidelines](thesis-docs/bscs_thesis_guidelines.md)** — NDMC CITE formatting and defense specifications.
* **[Student Information & Schedule](thesis-docs/student_info.md)** — Team contact details and academic schedule.

---

## Live System & Public Resources

* **Live Forensic Web Application:** [https://forgeguard.streamlit.app/](https://forgeguard.streamlit.app/)
* **Software System Repository:** [https://github.com/DeathKnell837/ForgeGuard](https://github.com/DeathKnell837/ForgeGuard)
* **Master Thesis Workspace Repository:** [https://github.com/DeathKnell837/NDMC-BSCS-THESIS-PREP](https://github.com/DeathKnell837/NDMC-BSCS-THESIS-PREP)
* **Google Drive Document Archive:** [NDMC BSCS Thesis Drive Folder](https://drive.google.com/drive/folders/1bzRsI6Ywo2yRni5Ij7InCLh0CL0OO90_?usp=drive_link)

---

&copy; 2026 Daniela S. Ungab & Rogie P. Bacanto. Notre Dame of Midsayap College, CITE. All rights reserved.
