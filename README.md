# 🎓 NDMC BSCS Thesis Preparation & Info Center

Welcome to the central information center for the BS Computer Science (BSCS) thesis preparation at **Notre Dame of Midsayap College (NDMC)**, College of Information Technology and Engineering (CITE).

---

## 👥 Student & Adviser Profiles
*   **Group Members:**
    *   **Rogie P. Bacanto** (BSCS-4)
    *   **Daniela S. Ungab** (BSCS-4)
*   **Adviser:** **Ms. Doris Ann Mariano**
*   **Subject:** CS Thesis Writing 1 (Enrolled, June 2026)

---

## 📅 Timeline & Key Milestones
Our target is the **Title Defense in Week 4**, where we will present three research titles to the panel.
**IMPORTANT:** The Topic and Statement of the Problem must be finalized and submitted to the Dean/Panel at least **5 days prior to the defense date** (Submission deadline: **July 8, 2026**).

| Week | Dates | Milestone / Task | Description |
|---|---|---|---|
| **Week 1** | June 22-28 | **Topic Exploration** | Brainstormed domains, researched guidelines, and draft structures. (Completed) |
| **Week 2** | June 29 - July 5 | **Reference Compilation** | Finalizing titles, matching references, and drafting Chapter 1.1. (NOW) |
| **Week 3** | July 6-12 | **Defense Submission & Prep** | **🚨 Submit Topic & SOP proposals by July 8** (5 days before defense). Prepare slides. |
| **Week 4** | **July 13-19, 2026** | **🚨 TITLE DEFENSE** | Presenting 3 robust titles to the panel for approval. |
| **Week 5+** | July 20 onwards | **Proposal Writing** | Writing Chapters 1 & 2 of the approved title. |

---

## 🏆 The 3 Thesis Titles for Defense
We have finalized exactly **3 distinct, non-repetitive titles** aligned with the CITE Research Agenda. All topics leverage advanced Artificial Intelligence (AI) but apply to completely different domains.

### 🏚️ Title 1: Concrete Crack Classification & Width Profiling
*   **Robust Title:** **"Concrete Crack Classification and Millimetric Severity Profiling Using Explainable Transfer Learning"**
*   **Domain:** Computer Vision / Civil Safety & Structural Health Monitoring
*   **Research Agenda:** Agenda 1: Emerging Technologies in Computer Science
*   **SDGs:** SDG 9 (Industry & Infrastructure), SDG 11 (Sustainable Cities)
*   **Core Problem:** Manual visual structural inspections are slow, subjective, and prone to human error, especially after disasters like earthquakes when structural engineers are scarce.
*   **Unique Features:**
    *   **Explainable AI (Grad-CAM):** Visualizes exactly where the AI is looking to verify it is analyzing the crack and not wall shadows or dirt.
    *   **Millimetric Estimation:** Calibrates image pixels to physical millimeters using a reference object to grade crack severity (minor, moderate, severe) objectively.
    *   **Building Safety Index:** Aggregates multiple wall/column damage reports to calculate an overall building safety category (Safe, Caution, Danger).

---

### 🔍 Title 2: Zero-Day Phishing Interception
*   **Robust Title:** **"Proactive Phishing Interception: Deconstructing Malicious URL Patterns in Real-Time Using Hybrid Neural Networks"**
*   **Domain:** Cybersecurity / Natural Language Processing (NLP)
*   **Research Agenda:** Agenda 4: Cybersecurity Threat Detection and Mitigation
*   **SDGs:** SDG 16 (Peace, Justice, and Strong Institutions)
*   **Core Problem:** Traditional database-driven blocklists (like Google Safe Browsing) cannot detect brand-new, "zero-day" phishing links. Scammers frequently spoof local mobile wallets (e.g., GCash) and banking sites with these short-lived URLs.
*   **Unique Features:**
    *   **Character-Level Embedding:** Analyzes structural raw character patterns to predict phishing potential without needing a database.
    *   **Redirect Resolver:** Traces shortened URLs (e.g., `bit.ly`) to expose the final target domain before classification.
    *   **Explainability Heatmaps:** Highlights specific substring tokens (e.g., `login`, `verification`) that triggered the security alert.
    *   **Chrome Extension:** Runs the model locally in milliseconds inside a lightweight browser extension.

---

### 🛡️ Title 3: AI-Generated Image & Deepfake Forensics
*   **Robust Title:** **"Digital Authenticity Verification: Classifying GAN and Diffusion-Generated Image Artifacts via Multi-Engine Neural Networks"**
*   **Domain:** Image Forensics / Cybersecurity & Multimedia Security
*   **Research Agenda:** Agenda 4: Cybersecurity Threat Detection and Mitigation
*   **SDGs:** SDG 16 (Peace, Justice, and Strong Institutions)
*   **Core Problem:** Generative AI tools (GANs, Midjourney, DALL-E) make creating hyper-realistic fake images effortless. Scammers use fake selfies to bypass online bank KYC checks, create scam accounts, and propagate visual fake news that is indistinguishable to human eyes.
*   **Unique Features:**
    *   **Generative Artifact Detector:** Focuses on microscopic pixel anomalies and frequency artifacts left behind by generative networks.
    *   **Explainable AI (Grad-CAM):** Highlights specific facial regions (e.g., hair blending, ear asymmetries, pupillary reflection errors) that expose the image as fake.
    *   **Multi-Engine Classification:** Identifies which generator model created the image (GAN vs. Diffusion) to help digital forensic investigators.

---

## 🛠️ The Tech Stack (Cost: ₱0)
To ensure the project is easy to build and test locally:

*   **Model Training:** Google Colab (utilizing free cloud GPUs via the browser)
*   **Languages & Frameworks:** Python, Keras/TensorFlow, TensorFlow.js
*   **Web App Frontend:** React or Next.js (fully hosted for free on Vercel)
*   **Mobile Testing:** Running model inference client-side in phone browsers via WebRTC camera APIs.

---

## 📁 Key Project Files
All critical documents are stored in the root folder of this repository:
*   [student_info.md](file:///C:/Users/ADMIN/OneDrive/Desktop/THESIS/NDMC-BSCS-THESIS-PREP/student_info.md) — Student profiles and timeline checklists.
*   [bscs_thesis_guidelines.md](file:///C:/Users/ADMIN/OneDrive/Desktop/THESIS/NDMC-BSCS-THESIS-PREP/bscs_thesis_guidelines.md) — Recap of formatting styles and CITE research agenda details.
*   [thesis_defense_prep.md](file:///C:/Users/ADMIN/OneDrive/Desktop/THESIS/NDMC-BSCS-THESIS-PREP/thesis_defense_prep.md) — Defense prep document containing SOPs, loopholes, and draft Backgrounds.
*   [summary_for_daniela.md](file:///C:/Users/ADMIN/OneDrive/Desktop/THESIS/NDMC-BSCS-THESIS-PREP/summary_for_daniela.md) — Quick summary sheet for Daniela.
*   [implementation_plan.md](file:///C:/Users/ADMIN/OneDrive/Desktop/THESIS/NDMC-BSCS-THESIS-PREP/implementation_plan.md) — Step-by-step model training and proposal coding plan.
*   [title1_proposal_draft.md](file:///C:/Users/ADMIN/OneDrive/Desktop/THESIS/NDMC-BSCS-THESIS-PREP/title1_proposal_draft.md) — Structural Crack Detection draft proposal text.

### 📚 Official CITE Guidelines (PDFs)
*   [NDMC Thesis Guidelines v5 - 2025.pdf](file:///C:/Users/ADMIN/OneDrive/Desktop/THESIS/NDMC-BSCS-THESIS-PREP/NDMC%20Thesis%20Guidelines%20v5%20-%202025.pdf) — Academic writing format, margins, and chapter details.
*   [CITE Research Agenda for 2024-2030.pdf](file:///C:/Users/ADMIN/OneDrive/Desktop/THESIS/NDMC-BSCS-THESIS-PREP/CITE%20Research%20Agenda%20for%202024-2030.pdf) — Official agenda listing (Emerging Tech & Cybersecurity alignment).
*   [Research Outline for CITE 2024.pdf](file:///C:/Users/ADMIN/OneDrive/Desktop/THESIS/NDMC-BSCS-THESIS-PREP/Research%20Outline%20for%20CITE%202024.pdf) — Specific outline guidelines.

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
