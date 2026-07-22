# 🎓 NDMC BSCS Thesis — Securing Mobile Transactions

**"Securing Mobile Transaction: A Comparative Evaluation of CNN Architectures in Detecting Digital Receipt Forgery"**

📁 **Google Drive (All Thesis Files):** [Open Shared Folder](https://drive.google.com/drive/folders/1bzRsI6Ywo2yRni5Ij7InCLh0CL0OO90_?usp=drive_link)

---

## 👥 Student & Adviser Profiles
*   **Group Members:**
    *   **Daniela S. Ungab** (BSCS-4)
    *   **Rogie P. Bacanto** (BSCS-4)
*   **Adviser:** **Ms. Doris Ann Mariano**
*   **Research Teacher / Research Coordinator:** **Mr. Nero L. Hontiveros**
*   **Dean:** **Engr. Mark Bryan C. Tenebroso, PCPE, ME-CPE**
*   **School:** Notre Dame of Midsayap College (NDMC), College of Information Technology and Engineering (CITE)
*   **Program:** Bachelor of Science in Computer Science
*   **Subject:** CS Thesis Writing 1 (Enrolled, June 2026)

---

## 📅 Timeline & Milestones

| Week | Dates | Milestone | Status |
|---|---|---|---|
| Week 1 | June 22-28 | Topic Exploration & Brainstorming | ✅ Done |
| Week 2 | June 29 - July 5 | Reference Compilation & Title Refinement | ✅ Done |
| Week 3 | July 6-12 | Defense Preparation & Title Finalization | ✅ Done |
| Week 4 | July 13-19 | **Title Defense** — Approved by panel ✅ | ✅ Done |
| **Week 5+** | **July 20 onwards** | **Proposal Writing — Chapters 1 & 2** | 🔄 In Progress |

---

## 📖 About the Study

### Problem
Mobile wallet and e-payment platforms have become frequent targets of screenshot-based fraud, in which manipulated or fabricated transaction receipts are used to deceive sellers into releasing goods or services without actual payment [1]. Local online sellers, small business owners, and student entrepreneurs — including those at Notre Dame of Midsayap College — are especially vulnerable due to limited access to fraud-detection tools.

### Objective
This study aims to comparatively evaluate the performance of three CNN architectures — **Basic/Baseline CNN**, **ResNet50**, and **MobileNetV2** — in detecting digital forgery and pixel-level tampering in mobile wallet transaction receipts, in terms of classification accuracy, processing efficiency, and practical deployability.

### Research Questions
1. What is the classification accuracy of the Basic CNN, ResNet50, and MobileNetV2 models in detecting:
   - 1.1. Manually edited transaction receipts (e.g., modified text or amounts)
   - 1.2. Programmatically generated fake transaction receipts
2. What is the performance of the three models in terms of: (2.1) Precision, (2.2) Recall, (2.3) F1-score?
3. What is the inference speed and computational resource requirement of each model?
4. Is there a significant difference in classification accuracy among the three models when analyzing:
   - 4.1. Original high-resolution screenshots
   - 4.2. Heavily compressed images
5. Which architecture offers the most practical balance of accuracy and efficiency for real-world transaction verification by local online sellers and student entrepreneurs at NDMC?

### Hypothesis (H₀)
There is no significant difference in the classification accuracy among the Basic CNN, ResNet50, and MobileNetV2 models in detecting forgery in mobile wallet transaction receipts.

### Beneficiaries
- **Local Online Sellers** — practical tool to verify receipt authenticity before releasing goods.
- **Small Business Owners in Midsayap** — fast, reliable way to verify incoming receipts on the spot.
- **Student Entrepreneurs (NDMC)** — accessible means of confirming mobile wallet transactions.
- **Mobile Wallet Providers** — comparative findings for strengthening fraud detection architectures.
- **Cybersecurity Researchers** — domain-specific comparative benchmark of CNN architectures.

---

## 🛠️ Feasibility & Tech Stack

| Component | Technology |
|---|---|
| **Data Source** | Custom dataset of simulated GCash receipts (authentic + forged) |
| **Training Environment** | Google Colab (free GPU access) |
| **Core Models** | Basic CNN, ResNet50, MobileNetV2 |
| **Backend** | Python (TensorFlow/Keras, OpenCV, Pillow, scikit-learn, SciPy) |
| **Frontend** | Streamlit or Flask web application |
| **Statistical Testing** | SciPy (ANOVA / Kruskal-Wallis) |

---

## 📚 References
- [1] C. Artaud et al., "Receipt dataset for fraud detection," in *Proc. 1st Int. Workshop on Computational Document Forensics (IWCDF)*, 2017.
- [2] K. S. Vaishnavi and K. P. Narayan, "FakePay: A real-time UPI fraud detection system using OCR, CNN, and ensemble ML," Technical Report, Mar. 2026.
- [3] A. M. Nagm et al., "Detecting image manipulation with ELA-CNN integration," *PeerJ Computer Science*, vol. 10, p. e2205, 2024.
- [4] K. He et al., "Deep residual learning for image recognition," in *Proc. IEEE CVPR*, 2016, pp. 770-778.
- [5] M. Sandler et al., "MobileNetV2: Inverted residuals and linear bottlenecks," in *Proc. IEEE CVPR*, 2018, pp. 4510-4520.

---

## 📁 Key Project Files
*   📄 [README.md](README.md) — This file.
*   📄 [student_info.md](student_info.md) — Student profiles.
*   📄 [bscs_thesis_guidelines.md](bscs_thesis_guidelines.md) — NDMC thesis formatting rules.
*   📄 `NDMC Thesis Guidelines v5 - 2025.pdf` — Official thesis guidelines.
*   📄 `Research Outline for CITE 2024.pdf` — BSCS research outline.

---

## 💻 Repository & Links
*   **Thesis Documents:** [DeathKnell837/NDMC-BSCS-THESIS-PREP](https://github.com/DeathKnell837/NDMC-BSCS-THESIS-PREP)
*   **🔒 ForgeGuard System Code:** [DeathKnell837/ForgeGuard](https://github.com/DeathKnell837/ForgeGuard)
*   **Google Drive:** [Shared Folder](https://drive.google.com/drive/folders/1bzRsI6Ywo2yRni5Ij7InCLh0CL0OO90_?usp=drive_link)
