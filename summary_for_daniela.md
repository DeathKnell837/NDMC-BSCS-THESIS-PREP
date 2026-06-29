# Thesis Summary for Daniela 📋

**Group Members:** Rogie P. Bacanto & Daniela S. Ungab
**Subject:** CS Thesis Writing 1 (BSCS-4, NDMC)
**Adviser:** Ms. Rezzie R. Cadungog

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

We must present exactly **3 thesis titles** at the Week 4 title defense. The panel will pick the best one. All 3 use the same core technology: **AI / Deep Learning / Convolutional Neural Networks (CNN)**.

| Slot | Topic / Title | Domain |
|---|---|---|
| **Title 1** | **Structural Crack Detection and Severity Classification** | AI + Computer Vision + Civil Safety |
| **Title 2** | **Malicious URL Detection & Phishing Prevention** | AI + Natural Language Processing + Cybersecurity |
| **Title 3** | **Deepfake Image/Video Detection** | AI + Computer Vision + Cybersecurity |

---

## Title 1: 🏚️ Structural Crack Detection and Severity Classification System

### Robust Title
> *"A Deep Learning-Based Structural Crack Detection and Severity Classification System Using Convolutional Neural Networks with Transfer Learning for Building Safety Assessment"*

### The Problem
Traditional manual inspections of cracked buildings are slow, subjective, and prone to human error. Following earthquakes or during regular maintenance, licensed structural engineers are in short supply.

### Unique Features
*   **Explainable AI (Grad-CAM):** Generates a heatmap over the concrete surface, showing the panel exactly which crack features the AI is focusing on to make its decision.
*   **Physical Width Measurement (mm):** Converts image pixels into physical millimeters using a calibration algorithm (with a standard reference object) to grade severity objectively.
*   **Building-Level Safety Aggregator:** Allows inspectors to create a "Building Profile" and take multiple photos (walls, columns, foundation). The system combines these to calculate an overall building safety index (Safe, Caution, Danger) based on structural engineering heuristics.

### Research Agenda
*   **Agenda 1:** Emerging Technologies in Computer Science (AI)
*   **SDGs:** SDG 9 (Industry, Innovation & Infrastructure), SDG 11 (Sustainable Cities)

---

## Title 2: 🔍 Malicious URL Detection & Phishing Prevention System

### Robust Title
> *"Character-Level Deep Learning-Based Detection and Classification of Malicious URLs Using Hybrid CNN-LSTM Networks for Phishing Prevention"*

### The Problem
 centrale database-driven blocklists (like Google Safe Browsing) cannot detect "zero-day" phishing links that were created 5 minutes ago. Attackers frequently spoof local services (e.g., GCash, BDO/BPI) using these new URLs.

### Unique Features
*   **Zero-Day Proactive Analysis:** Instead of matching against a database, the AI analyzes the *character patterns* of a raw URL string (e.g., character sequences, keywords, subdomains) to predict maliciousness.
*   **Redirect Resolver Integration:** Traces shorteners (e.g., `bit.ly` or `tinyurl`) to extract the final destination domain *before* sending it to the model.
*   **Explainability Heatmaps:** Visualizes which character sequences/substrings (e.g., `login`, `verification`) contributed most to the malicious classification.
*   **Chrome Extension:** Runs the model locally in milliseconds to intercept pages in real-time.

### Research Agenda
*   **Agenda 1:** Emerging Tech (AI/NLP) + **Agenda 4:** Cybersecurity Threat Detection
*   **SDG:** SDG 16 (Peace, Justice & Strong Institutions)

---

## Title 3: 🕵️‍♂️ Deepfake Image/Video Detection System

### Robust Title
> *"A Convolutional Neural Network Approach for Real-Time Detection and Classification of Deepfake Images and AI-Generated Media"*

### The Problem
With the rise of Midjourney, DALL-E, and advanced face-swap models, fake media is widely used for scams, identity theft, and spreading misinformation online.

### Unique Features
*   **Multiclass Detection:** Detects face-swaps, AI-generated art, and manipulated images.
*   **Manipulation Heat Map:** Highlights exactly which region of the image shows signs of AI manipulation or pixel tempering.
*   **Video Analysis:** Scans uploads frame-by-frame for temporal inconsistencies.

### Research Agenda
*   **Agenda 1:** Emerging Tech (AI/Computer Vision)
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
