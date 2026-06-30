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

| Week | Dates | Milestone / Task | Description |
|---|---|---|---|
| **Week 1** | June 22-28 | **Topic Exploration** | Brainstormed domains, researched guidelines, and draft structures. (Completed) |
| **Week 2** | June 29 - July 5 | **Reference Compilation** | Finalizing titles, matching references, and drafting Chapter 1.1. (NOW) |
| **Week 3** | July 6-12 | **Defense Preparation** | Building slides and preparing for potential panel questions. |
| **Week 4** | **July 13-19, 2026** | **🚨 TITLE DEFENSE** | Presenting 3 robust titles to the panel for approval. |
| **Week 5+** | July 20 onwards | **Proposal Writing** | Writing Chapters 1 & 2 of the approved title. |

---

## 🏆 The 3 Thesis Titles for Defense
We have finalized exactly **3 distinct, non-repetitive titles** aligned with the CITE Research Agenda. All topics leverage advanced Artificial Intelligence (AI) but apply to completely different domains.

### 🏚️ Title 1: Concrete Crack Classification & Width Profiling
*   **Robust Title:** **"Automated Structural Health Monitoring: Concrete Crack Classification and Millimetric Severity Profiling Using Explainable Transfer Learning"**
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
*   [student_info.md](file:///c:/Users/USER/Desktop/THESIS/student_info.md) — Student profile, scheduler, and confirmed titles list.
*   [bscs_thesis_guidelines.md](file:///c:/Users/USER/Desktop/THESIS/bscs_thesis_guidelines.md) — NDMC-specific paper formatting rules (A4 size, margins, citation styles).
*   [thesis_defense_prep.md](file:///c:/Users/USER/Desktop/THESIS/thesis_defense_prep.md) — Complete defense preparation sheet containing Statement of the Problem (SOP) questions, loophole defenses, theoretical frameworks, and draft Background of the Study (1.1) sections.
*   [summary_for_daniela.md](file:///c:/Users/USER/Desktop/THESIS/summary_for_daniela.md) — Clean, shareable review sheet for Daniela.
*   [implementation_plan.md](file:///c:/Users/USER/Desktop/THESIS/implementation_plan.md) — 10-phase thesis completion plan.
*   `.agents/AGENTS.md` — Custom AI workspace rules to maintain project guidelines.

---

## 💻 Git Synchronization & Multi-Device Setup
This repository is configured to sync changes easily between devices.

*   **Repository URL:** [DeathKnell837/NDMC-BSCS-THESIS-PREP](https://github.com/DeathKnell837/NDMC-BSCS-THESIS-PREP)
*   **To sync changes on your laptop:**
    1.  Open Git Bash or terminal on your laptop.
    2.  Run `git pull origin main` to fetch the latest titles and documents.
    3.  Make changes, then run `git add -A; git commit -m "update message"; git push origin main`.
