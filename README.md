# 🎓 NDMC BSCS Thesis Preparation & Info Center

Welcome to the central information center for the BS Computer Science (BSCS) thesis preparation at **Notre Dame of Midsayap College (NDMC)**, College of Information Technology and Engineering (CITE).

📁 **Google Drive (All Thesis Files):** [Open Shared Folder](https://drive.google.com/drive/folders/1bzRsI6Ywo2yRni5Ij7InCLh0CL0OO90_?usp=drive_link)

---

## 👥 Student & Adviser Profiles
*   **Group Members:**
    *   **Rogie P. Bacanto** (BSCS-4)
    *   **Daniela S. Ungab** (BSCS-4)
*   **Adviser:** **Ms. Doris Ann Mariano**
*   **Research Teacher / Research Coordinator:** **Mr. Nero L. Hontiveros**
*   **Dean:** **Engr. Mark Bryan C. Tenebroso, PCPE, ME-CPE**
*   **School:** Notre Dame of Midsayap College (NDMC), College of Information Technology and Engineering (CITE)
*   **Subject:** CS Thesis Writing 1 (Enrolled, June 2026)

---

## 📅 Timeline & Key Milestones

| Week | Dates | Milestone / Task | Status |
|---|---|---|---|
| **Week 1** | June 22-28 | Topic Exploration & Brainstorming | ✅ Done |
| **Week 2** | June 29 - July 5 | Reference Compilation & Title Refinement | ✅ Done |
| **Week 3** | July 6-12 | Defense Preparation & Title Finalization | ✅ Done |
| **Week 4** | July 13-19, 2026 | **🚨 TITLE DEFENSE** — Presented 3 titles to panel | ✅ Done (2 approved, 1 rejected) |
| **Week 5+** | July 20 onwards | **Proposal Writing** — Chapters 1 & 2 of approved titles | 🔄 In Progress |

---

## 🏆 Summary of Thesis Proposals

### ✅ Title I: Phishing URL Detection (APPROVED)
*   **Full Title:** **"Proactive Phishing URL Detection Using Feature-Based Machine Learning Classifiers"**
*   **Domain:** Cybersecurity / Machine Learning / NLP
*   **Research Agenda:** Agenda 4: Cybersecurity Threat Detection and Prevention
*   **SDGs:** SDG 16 (Peace, Justice & Strong Institutions)
*   **Core Problem:** Traditional phishing defenses (blacklists) are reactive — they cannot detect zero-day phishing URLs that haven't been reported yet. Scammers spoof local platforms (GCash, BDO, BPI).
*   **Solution & Algorithms:** Benchmarks Random Forest, Support Vector Machine (SVM), and XGBoost using engineered lexical and structural features (URL length, hyphen count, "@" symbol, subdomain count, HTTPS status, brand-name similarity).
*   **Target Beneficiaries:** Online users, local banking customers, cybersecurity researchers.

---

### ✅ Title II: GAN & Diffusion Image Artifact Detection (APPROVED)
*   **Full Title:** **"Digital Fingerprints: A Comparative Evaluation of Neural Networks in Detecting GAN and Diffusion Image Artifacts"**
*   **Domain:** Image Forensics / Deep Learning / Computer Vision
*   **Research Agenda:** Agenda 1: Emerging Technologies in Computer Science
*   **SDGs:** SDG 16 (Peace, Justice & Strong Institutions)
*   **Core Problem:** AI-generated synthetic images (from GANs and diffusion models like Stable Diffusion and Midjourney) bypass human verification and are used for online identity fraud, fake KYC checks, and deepfakes. Existing tools focus on only one model type.
*   **Solution & Algorithms:** Comparative evaluation of ResNet, EfficientNet, and Vision Transformer (ViT) across both GAN and diffusion generator artifacts.
*   **Target Beneficiaries:** Digital forensic investigators, financial institutions (KYC verification), media platforms.

---

### 🆕 Title III: Mobile Wallet Receipt Forgery Detection (REPLACEMENT FOR REJECTED COMPRESSION TITLE)
*   **Full Title:** **"Accuracy Evaluation of a Fine-Tuned Convolutional Neural Network for Forgery Detection in Mobile Wallet Receipts"**
*   **Domain:** Image Forensics / Deep Learning / E-Commerce Safety
*   **Research Agenda:** Agenda 4: Cybersecurity Threat Detection and Prevention
*   **SDGs:** SDG 16 (Peace, Justice & Strong Institutions)
*   **Adviser Alignment:** Replaces the rejected *Lossless Compression* title. Fulfills the adviser's strict mandate of having a **clear victim (online sellers)**, **identifiable respondents**, and **high real-world urgency**.

#### 📌 Problem Summary & Key Statistics:
- **Scam Modus:** Fraudulent buyers use image editing tools and AI receipt generators to edit GCash/Maya screenshots (modifying amounts, names, reference numbers) to scam online sellers into shipping goods.
- **National Impact (2024–2025 Data):**
  - CICC recorded **10,004 cybercrime complaints** in 2024 (3× increase from 2023).
  - Online selling scams: **3,025 cases** (PNP-ACG).
  - GCash specific user losses: **₱76.49 million** in 2024.
  - Total PH cyber losses: **₱5.82 billion** (BSP 2024).
  - Suspected digital fraud rate in PH: **13.4%** (148% higher than global average of 5.4%, TransUnion).
  - Social engineering schemes account for **76% of total fraud losses** (BSP H1 2025).

#### ❓ Research Questions (Statement of the Problem):
1. What is the classification accuracy, precision, recall, F1-score, and AUC-ROC of the fine-tuned CNN in distinguishing authentic from forged mobile wallet receipt images?
2. Is there a significant difference between the classification accuracy of the fine-tuned CNN and chance level (50%) in detecting forged mobile wallet receipt images?
3. Is there a significant difference in the model's detection accuracy across the following forgery techniques:
   - 3.1. Amount alteration
   - 3.2. Reference number fabrication
   - 3.3. Recipient/sender name modification
   - 3.4. Full template-based fabrication
4. What is the average inference time of the fine-tuned model per receipt image?

#### 🎯 Objectives of the Study:
1. Collect and curate a labeled dataset of authentic and forged GCash and Maya receipt images.
2. Preprocess receipt images using Error Level Analysis (ELA) and normalization techniques.
3. Fine-tune pre-trained CNN architectures (ResNet-50 / DenseNet-121) using transfer learning.
4. Evaluate performance metrics (Accuracy, Precision, Recall, F1-Score, AUC-ROC).
5. Analyze detection performance across specific forgery techniques.
6. Determine average inference speed per receipt image for real-time verification feasibility.

#### ⚖️ Null Hypotheses ($H_0$):
- **$H_{01}$:** The fine-tuned CNN does not achieve a classification accuracy significantly greater than 50% (chance level).
- **$H_{02}$:** There is no significant difference in the model's detection accuracy across different forgery techniques.

#### 👥 Beneficiaries:
Online Sellers, E-Wallet Providers (GCash, Maya), Law Enforcement (PNP-ACG, CICC), Regulatory Bodies (BSP), Academic Researchers, and Students.

---

## ❌ Rejected Titles Record & Lessons Learned
1. **"Learning-Based Algorithm Selection for Lossless File Compression"**
   - **Reason for Rejection:** Technical optimization lacking a clear human victim or societal urgency. Panel/adviser evaluates topics based on *"Who is suffering/victim?"* rather than purely algorithmic efficiency.

---

## 🛠️ Technology Stack (Cost: ₱0)

| Layer | Technologies | Cost |
|---|---|---|
| AI / ML Models | Python, Keras / TensorFlow, scikit-learn, OpenCV | FREE |
| Training Environment | Google Colab (Cloud T4 GPUs) | FREE |
| Web Application | React / Next.js | FREE |
| Web Hosting | Vercel | FREE |
| Version Control | Git / GitHub | FREE |

---

## 📁 Key Project Files in Workspace

*   📄 [README.md](README.md) — Central project hub and status dashboard.
*   📄 [student_info.md](student_info.md) — Student profiles, confirmed titles, and scheduler.
*   📄 [bscs_thesis_guidelines.md](bscs_thesis_guidelines.md) — NDMC CITE Thesis Guidelines & Outline summary.
*   📄 `NDMC Thesis Guidelines v5 - 2025.pdf` — Official college-wide thesis guidelines PDF.
*   📄 `Research Outline for CITE 2024.pdf` — Official BSCS research outline PDF.
*   📄 [summary_for_daniela.md](summary_for_daniela.md) — Summary review sheet for Daniela.
*   📄 [implementation_plan.md](implementation_plan.md) — Complete 10-phase thesis implementation roadmap.

---

## 💻 Git Synchronization & Multi-Device Setup

*   **Repository URL:** [DeathKnell837/NDMC-BSCS-THESIS-PREP](https://github.com/DeathKnell837/NDMC-BSCS-THESIS-PREP)
*   **Google Drive Folder:** [Shared Drive Link](https://drive.google.com/drive/folders/1bzRsI6Ywo2yRni5Ij7InCLh0CL0OO90_?usp=drive_link)
*   **Sync Commands for Laptop/PC:**
    ```bash
    git pull origin main
    git add -A
    git commit -m "update message"
    git push origin main
    ```
