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

## 🏆 The 3 Thesis Titles

### ✅ Title I: Phishing URL Detection (APPROVED)
*   **Title:** **"Proactive Phishing URL Detection Using Feature-Based Machine Learning Classifiers"**
*   **Domain:** Cybersecurity / Machine Learning
*   **Research Agenda:** Agenda 4: Cybersecurity Threat Detection and Prevention
*   **SDGs:** SDG 16 (Peace, Justice & Strong Institutions)
*   **Core Problem:** Traditional phishing defenses (blacklists) are reactive — they can't catch zero-day phishing URLs that haven't been reported yet. This study builds a proactive detection approach using engineered URL features (length, hyphens, "@" symbol, subdomain count, HTTPS status, brand-name similarity) and compares Random Forest, SVM, and XGBoost classifiers.
*   **Algorithms:** Random Forest, Support Vector Machine (SVM), XGBoost

---

### ✅ Title II: GAN & Diffusion Image Artifact Detection (APPROVED)
*   **Title:** **"Digital Fingerprints: A Comparative Evaluation of Neural Networks in Detecting GAN and Diffusion Image Artifacts"**
*   **Domain:** Image Forensics / Deep Learning
*   **Research Agenda:** Agenda 1: Emerging Technologies in Computer Science
*   **SDGs:** SDG 16 (Peace, Justice & Strong Institutions)
*   **Core Problem:** AI-generated images (from GANs and diffusion models like Stable Diffusion, Midjourney) are now good enough to pass as real, enabling disinformation, fraud, and impersonation. Existing detection tools focus on only one generator type. This study compares ResNet, EfficientNet, and Vision Transformer (ViT) across both GAN and diffusion artifacts.
*   **Algorithms:** ResNet, EfficientNet, Vision Transformer (ViT)

---

### 🆕 Title III: Mobile Wallet Receipt Forgery Detection (NEW — Pending Approval)
*   **Title:** **"Accuracy Evaluation of a Fine-Tuned Convolutional Neural Network for Forgery Detection in Mobile Wallet Receipts"**
*   **Domain:** Image Forensics / Fraud Detection
*   **Research Agenda:** Agenda 4: Cybersecurity Threat Detection and Prevention
*   **SDGs:** SDG 16 (Peace, Justice & Strong Institutions)
*   **Core Problem:** Scammers in Philippine online selling fabricate fake GCash/Maya receipt screenshots to trick sellers into shipping goods without payment. No automated tool exists to verify receipt authenticity — sellers rely on manual visual inspection which fails against sophisticated edits and AI-generated fakes. This study evaluates a fine-tuned CNN (ResNet-50 or DenseNet-121) for binary classification of receipts as authentic or forged.
*   **Key Stats:** CICC recorded 10,004 cybercrime complaints in 2024 (3× increase from 2023); GCash users lost ₱76.49M to fraud; PH digital fraud rate is 13.4% (148% above global average).

---

## 🛠️ Tech Stack (Cost: ₱0)

| Component | Technology | Cost |
|---|---|---|
| AI Model | Python + TensorFlow/Keras + scikit-learn | FREE |
| Model Training | Google Colab (free GPU in browser) | FREE |
| Web App Frontend | React / Next.js | FREE |
| Hosting | Vercel | FREE |
| Datasets | Kaggle / public datasets / self-collected | FREE |

---

## 📁 Key Project Files
*   [README.md](README.md) — This file. Central info hub with all titles, timeline, and links.
*   [student_info.md](student_info.md) — Student profile and confirmed titles list.
*   [bscs_thesis_guidelines.md](bscs_thesis_guidelines.md) — NDMC-specific thesis outline, formatting rules (A4, margins, IEEE citation).
*   [summary_for_daniela.md](summary_for_daniela.md) — Clean, shareable review sheet for Daniela.
*   [implementation_plan.md](implementation_plan.md) — 10-phase thesis completion plan.
*   `.agents/AGENTS.md` — Custom AI workspace rules.

---

## 💻 Git Synchronization & Multi-Device Setup
*   **Repository URL:** [DeathKnell837/NDMC-BSCS-THESIS-PREP](https://github.com/DeathKnell837/NDMC-BSCS-THESIS-PREP)
*   **Google Drive:** [Open Shared Folder](https://drive.google.com/drive/folders/1bzRsI6Ywo2yRni5Ij7InCLh0CL0OO90_?usp=drive_link)
*   **To sync changes on your laptop:**
    1.  Open Git Bash or terminal on your laptop.
    2.  Run `git pull origin main` to fetch the latest titles and documents.
    3.  Make changes, then run `git add -A; git commit -m "update message"; git push origin main`.
