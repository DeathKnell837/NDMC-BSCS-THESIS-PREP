# 🎓 NDMC BSCS Thesis Preparation & Info Center

Welcome to the central information center for the BS Computer Science (BSCS) thesis preparation at **Notre Dame of Midsayap College (NDMC)**, College of Information Technology and Engineering (CITE).

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
Our target is the **Title Defense in Week 4**, where we will present three research titles to the panel.
**IMPORTANT:** The Topic and Statement of the Problem must be finalized and submitted to the Dean/Panel at least **5 days prior to the defense date** (Submission deadline: **July 8, 2026**).

| Week | Dates | Milestone / Task | Description |
|---|---|---|---|
| **Week 1** | June 22-28 | **Topic Exploration** | Brainstormed domains, researched guidelines, and draft structures. ✅ |
| **Week 2** | June 29 - July 5 | **Reference Compilation** | Finalizing titles, matching references, and drafting Chapter 1.1. ✅ |
| **Week 3** | July 6-12 | **Defense Submission & Prep** | **🚨 Submit Topic & SOP proposals by July 8** (5 days before defense). Prepare slides. (NOW) |
| **Week 4** | **July 13-19, 2026** | **🚨 TITLE DEFENSE** | Presenting 3 robust titles to the panel for approval. |
| **Week 5+** | July 20 onwards | **Proposal Writing** | Writing Chapters 1 & 2 of the approved title. |

---

## 🏆 The 3 Thesis Titles for Defense

We have finalized exactly **3 distinct, non-repetitive titles** aligned with the CITE Research Agenda. All topics leverage advanced Artificial Intelligence (AI) but apply to completely different domains. Full Chapter 1 drafts (Background, Objectives, Scope, References) are available in the `title_proposals/` folder.

---

### #1 🔍 Phishing Detection & Interception (Browser Extension)
*   **Final Title:** **"Proactive Phishing Detection and Interception via a Character-Level Hybrid CNN-LSTM Model"**
*   **Alternative:** *"Real-Time Phishing URL Interception Using a Hybrid CNN-LSTM Neural Network"*
*   **Algorithms:** Hybrid CNN-LSTM (character-level embedding)
*   **Domain:** Cybersecurity / Natural Language Processing (NLP)
*   **Research Agenda:** Agenda 4: Cybersecurity Threat Detection and Mitigation
*   **SDGs:** SDG 16 (Peace, Justice, and Strong Institutions)
*   **Core Problem:** Traditional database-driven blocklists cannot detect brand-new, "zero-day" phishing links. Philippine phishing websites surged 423% in a single year (2024-2025). Over 3.4 billion phishing emails sent daily worldwide.
*   **Deliverable:** A Google Chrome browser extension performing real-time, client-side inference via TensorFlow.js
*   **Chapter 1 Draft:** [`#1 PHISHING.docx`](title_proposals/%231%20PHISHING.docx) — Complete Background, Objectives, Scope & Delimitations, and References

---

### #2 🛡️ AI-Generated Image Detection (Comparative Study)
*   **Final Title:** **"Digital Fingerprints: A Comparative Evaluation of Neural Networks in Detecting GAN and Diffusion Image Artifacts"**
*   **Alternatives:**
    *   *"Catch Me If You GAN: Benchmarking Neural Networks Against Generative Image Artifacts"*
    *   *"Pixels Don't Lie (Or Do They?): A Comparative Study on Detecting AI-Generated Image Artifacts"*
    *   *"Seeing Isn't Believing: Benchmarking Neural Networks for AI-Generated Image Detection"*
    *   *"Beyond the Naked Eye: A Comparative Analysis of Neural Network Algorithms for AI-Generated Image Detection"*
*   **Algorithms:** ResNet vs. EfficientNet vs. Vision Transformer (ViT) — **Comparative evaluation of 3 architectures**
*   **Domain:** Image Forensics / Cybersecurity & Multimedia Security
*   **Research Agenda:** Agenda 4: Cybersecurity Threat Detection and Mitigation
*   **SDGs:** SDG 16 (Peace, Justice, and Strong Institutions)
*   **Core Problem:** 500 million AI-generated images created daily. Philippines saw 4,500% increase in deepfake-related fraud in 2023. Government officials themselves circulated deepfake videos.
*   **Deliverable:** A tool that benchmarks which neural network algorithm is best at detecting AI-generated images (accuracy vs. speed trade-off)
*   **Chapter 1 Draft:** [`#2 AI GENERATED IMAGES.docx`](title_proposals/%232%20AI%20GENERATED%20IMAGES.docx) — Complete Background, Objectives, and References

---

### #3 🏚️ Concrete Crack Classification & Severity Grading
*   **Final Title:** **"Concrete Crack Classification and Severity Grading Using Explainable Transfer Learning"**
*   **Alternative:** *"Concrete Crack Classification and Millimetric Severity Profiling Using Explainable Transfer Learning"*
*   **Algorithms:** Transfer Learning (pretrained CNN fine-tuning) + Grad-CAM (explainability)
*   **Domain:** Computer Vision / Civil Safety & Structural Health Monitoring
*   **Research Agenda:** Agenda 1: Emerging Technologies in Computer Science
*   **SDGs:** SDG 9 (Industry & Infrastructure), SDG 11 (Sustainable Cities)
*   **Core Problem:** Manual visual structural inspections are slow and subjective. Magnitude 7.8 earthquake hit Mindanao in June 2026. DPWH assessed 21,000+ buildings in 2025 alone.
*   **Deliverable:** A model that classifies cracks AND grades severity (hairline → minor → moderate → severe) with visual Grad-CAM explanations
*   **Chapter 1 Draft:** [`#3 CRACK GRADING.docx`](title_proposals/%233%20CRACK%20GRADING.docx) — Complete Background, Objectives, and References

---

## 🔄 Backup Titles
If any of the 3 primary titles are rejected by the panel:

1. **"Improving Scheduling Efficiency Using Constraint Satisfaction Programming"**
   *   Algorithm: Constraint Satisfaction Programming (CSP)
   *   Use case: Automating exam proctor scheduling and room assignments at NDMC

2. **"Machine Learning-Based Phishing Email Detection: A Comparative Analysis of Classification Algorithms"**
   *   Algorithms: Comparative analysis of multiple ML classifiers (e.g., Random Forest, SVM, Naive Bayes)
   *   Use case: Email-level phishing detection (complementary to URL-level Title #1)

---

## 🛠️ The Tech Stack (Cost: ₱0)
To ensure the project is easy to build and test locally:

*   **Model Training:** Google Colab (utilizing free cloud GPUs via the browser)
*   **Languages & Frameworks:** Python, Keras/TensorFlow, TensorFlow.js
*   **Web App Frontend:** React or Next.js (fully hosted for free on Vercel)
*   **Browser Extension:** Chrome Manifest V3 + TensorFlow.js (client-side inference)
*   **Mobile Testing:** Running model inference client-side in phone browsers via WebRTC camera APIs.

---

## 📁 Key Project Files
All critical documents are stored in the root folder of this repository:

### 📝 Chapter 1 Drafts (Full Proposals)
*   [`title_proposals/`](title_proposals/) — **Contains the finalized Chapter 1 drafts for all 3 titles** (Background, Objectives, Scope, References)
*   [`TITLES.docx`](title_proposals/TITLES.docx) — Master title list with alternatives and backups
*   [`ADVISER PROPOSAL.docx`](title_proposals/ADVISER%20PROPOSAL.docx) — Adviser assignment form (Ms. Doris Ann Mariano)

### 📋 Planning & Prep Documents
*   [student_info.md](student_info.md) — Student profiles and timeline checklists.
*   [bscs_thesis_guidelines.md](bscs_thesis_guidelines.md) — Recap of formatting styles and CITE research agenda details.
*   [thesis_defense_prep.md](thesis_defense_prep.md) — Defense prep document containing SOPs, loopholes, and draft Backgrounds.
*   [summary_for_daniela.md](summary_for_daniela.md) — Quick summary sheet for Daniela.

### 📚 Official CITE Guidelines (PDFs)
*   [NDMC Thesis Guidelines v5 - 2025.pdf](NDMC%20Thesis%20Guidelines%20v5%20-%202025.pdf) — Academic writing format, margins, and chapter details.
*   [CITE Research Agenda for 2024-2030.pdf](CITE%20Research%20Agenda%20for%202024-2030.pdf) — Official agenda listing (Emerging Tech & Cybersecurity alignment).
*   [Research Outline for CITE 2024.pdf](Research%20Outline%20for%20CITE%202024.pdf) — Specific outline guidelines.

### 🎨 Prototype
*   [`prototype_title2/`](prototype_title2/) — Interactive phishing detection dashboard & Chrome extension mockup.

---

## 🎨 CITE Formatting Guidelines Cheat Sheet
To ensure our proposals do not get rejected by CITE panel for formatting layout:
*   **Paper Size:** A4
*   **Margins:** Left: **1.50 in** (for binding) | Right: **1.0 in** | Top: **1.20 in** | Bottom: **1.0 in**
*   **Spacing:** Double-spaced body text, 12pt Times New Roman, justified.
*   **Citations:** Strict **IEEE numeric format** (e.g., `[1]`, `[2]`).
*   **Casing Color:** **Gray** hard-bound casing (assigned color for CITE).

---

## 💻 Git Synchronization & Multi-Device Setup
This repository is configured to sync changes easily between devices.

*   **Repository URL:** [DeathKnell837/NDMC-BSCS-THESIS-PREP](https://github.com/DeathKnell837/NDMC-BSCS-THESIS-PREP)
*   **To sync changes on your laptop:**
    1.  Open Git Bash or terminal on your laptop.
    2.  Run `git pull origin main` to fetch the latest titles and documents.
    3.  Make changes, then run `git add -A; git commit -m "update message"; git push origin main`.
