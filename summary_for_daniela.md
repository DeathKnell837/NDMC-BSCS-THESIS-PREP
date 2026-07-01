# Thesis Summary for Daniela 📋

**Group Members:** Rogie P. Bacanto & Daniela S. Ungab
**Subject:** CS Thesis Writing 1 (BSCS-4, NDMC)
**Adviser:** Ms. Doris Ann Mariano

---

## ⏰ Our Timeline

| Week | Dates | What We Do |
|---|---|---|
| **Week 1** | June 22-28 (Completed) | Research & Topic Selection |
| **Week 2** | June 29 - July 5 (NOW) | Refine Titles, Gather References, and Outline Chapter 1 |
| **Week 3** | July 6-12 | Finalize Title Defense Slides & Practice |
| **Week 4** | **July 13-19** | **🚨 TITLE DEFENSE (defend 3 titles to panelists)** |

---

## Our 3 Thesis Titles for the Defense

We must present exactly **3 thesis titles** at the Week 4 title defense. The panel will pick the best one. All 3 use advanced Artificial Intelligence (Machine Learning / Computer Vision / Natural Language Processing) to solve critical real-world problems.

| Slot | Topic / Title | Domain |
|---|---|---|
| **Title 1** | **Automated Structural Health Monitoring** | Computer Vision / Civil Safety |
| **Title 2** | **Proactive Phishing Interception** | NLP / Cybersecurity |
| **Title 3** | **Digital Authenticity Verification** | Image Forensics / Multimedia Security |



---

## Title 1: 🏚️ Automated Concrete Crack Analysis System

### Robust Title
> *"Automated Structural Health Monitoring: Concrete Crack Classification and Millimetric Severity Profiling Using Explainable Transfer Learning"*

### The Problem
Traditional manual inspections of cracked buildings are slow, subjective, and prone to human error. Following earthquakes or during regular maintenance, licensed structural engineers are in short supply.

### Unique Features
*   **Explainable AI (Grad-CAM):** Generates a heatmap over the concrete surface, showing the panel exactly which crack features the AI is focusing on to make its decision.
*   **Physical Width Measurement (mm):** Converts image pixels into physical millimeters using a calibration algorithm (with a standard reference object) to grade severity objectively.
*   **Building-Level Safety Aggregator:** Combines multiple damage photos of walls, columns, and foundations to calculate an overall building safety index (Safe, Caution, Danger) based on structural engineering heuristics.

### Research Agenda & SDGs
*   **Agenda 1:** Emerging Technologies in Computer Science (AI)
*   **SDGs:** SDG 9 (Industry, Innovation & Infrastructure), SDG 11 (Sustainable Cities)

---

## Title 2: 🔍 Proactive Phishing Interception System

### Robust Title
> *"Proactive Phishing Interception: Deconstructing Malicious URL Patterns in Real-Time Using Hybrid Neural Networks"*

### The Problem
Central database-driven blocklists (like Google Safe Browsing) cannot detect "zero-day" phishing links that were created 5 minutes ago. Attackers frequently spoof local services (e.g., GCash, BDO/BPI) using these new URLs.

### Unique Features
*   **Zero-Day Proactive Analysis:** Instead of matching against a database, the AI analyzes the *character patterns* of a raw URL string (e.g., character sequences, keywords, subdomains) to predict maliciousness.
*   **Redirect Resolver Integration:** Traces shorteners (e.g., `bit.ly` or `tinyurl`) to extract the final destination domain *before* sending it to the model.
*   **Explainability Heatmaps:** Visualizes which character sequences/substrings (e.g., `login`, `verification`) contributed most to the malicious classification.
*   **Chrome Extension:** Runs the model locally in milliseconds to intercept pages in real-time.

### Research Agenda & SDGs
*   **Agenda 1:** Emerging Tech (AI/NLP) + **Agenda 4:** Cybersecurity Threat Detection
*   **SDG:** SDG 16 (Peace, Justice & Strong Institutions)

---

## Title 3: 🛡️ Digital Authenticity Verification System

### Robust Title
> *"Digital Authenticity Verification: Classifying GAN and Diffusion-Generated Image Artifacts via Multi-Engine Neural Networks"*

### The Problem
The rise of generative AI makes it easy to create highly realistic fake profile pictures, scams, and identity fraud (e.g., bypassing GCash/bank ID verification using fake selfies). These fakes are indistinguishable to the human eye.

### Unique Features
*   **Generative Artifact Detector:** Inspects microscopic pixel patterns and frequency anomalies that are invisible to humans.
*   **Explainable AI (Grad-CAM):** Highlights the specific parts of the face (e.g., eyes, ears, jawline blending) where the AI detected fake generation artifacts.
*   **Multi-Engine Classification:** Identifies the type of fake (e.g., GAN-generated, Diffusion-generated, or Face-swapped) to trace the source engine.

### Research Agenda & SDGs
*   **Agenda 1:** Emerging Tech (AI/Vision) + **Agenda 4:** Cybersecurity Threat Detection
*   **SDG:** SDG 16 (Peace, Justice & Strong Institutions)

---

## Tech Stack (Same for All 3 Titles)

| Component | Technology | Cost |
|---|---|---|
| AI Model | Python + TensorFlow/Keras | FREE |
| Model Training | Google Colab (free GPU in browser) | FREE |
| Web App Frontend | React / Next.js | FREE |
| Hosting | Vercel (test via phone browser) | FREE |
| Native App (later) | React Native or Flutter + TensorFlow Lite | FREE |
| Datasets | Kaggle / public datasets | FREE |

**Total cost: ₱0**

---

## How the Work is Split

*   **AI Assistant:** Writes all code, trains the model templates, drafts thesis chapters, and compiles verified references.
*   **Rogie & Daniela:** Run the training on Google Colab (just click "Run"), collect some local test samples, study the concepts for the defense, and present the slides.
