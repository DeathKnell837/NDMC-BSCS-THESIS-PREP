# Thesis Summary for Daniela

**Group Members:** Rogie P. Bacanto & Daniela S. Ungab
**Subject:** CS Thesis Writing 1 (BSCS-4, NDMC)
**Adviser:** Ms. Doris Ann Mariano
**Research Teacher / Research Coordinator:** Mr. Nero L. Hontiveros
**Dean:** Engr. Mark Bryan C. Tenebroso, PCPE, ME-CPE

---

## Our Timeline
**Note:** The final Topic and Statement of the Problem (SOP) must be submitted at least **5 days before the defense** (Submission deadline: **July 8, 2026**).

| Week | Dates | What We Do |
|---|---|---|
| **Week 1** | June 22-28 | Research & Topic Selection (Done) |
| **Week 2** | June 29 - July 5 | Refine Titles, Gather References, and Draft Chapter 1 (Done) |
| **Week 3** | July 6-12 (NOW) | **Submit Topic & SOP by July 8. Prepare slides.** |
| **Week 4** | **July 13-19** | **TITLE DEFENSE (defend 3 titles to panelists)** |

---

## Our 3 Thesis Titles for the Defense

We must present exactly **3 thesis titles** at the Week 4 title defense. The panel will pick the best one. All 3 use advanced Artificial Intelligence (Machine Learning / Computer Vision / Natural Language Processing) to solve critical real-world problems.

Full Chapter 1 drafts (Background, Objectives, Scope, References) are in the `title_proposals/` folder.

| # | Final Title | Domain | Algorithms |
|---|---|---|---|
| **Title 1** | Phishing Detection & Interception | NLP / Cybersecurity | Hybrid CNN-LSTM |
| **Title 2** | AI-Generated Image Detection | Image Forensics / Multimedia Security | ResNet vs. EfficientNet vs. ViT |
| **Title 3** | Concrete Crack Classification & Grading | Computer Vision / Civil Safety | Transfer Learning + Grad-CAM |

---

## Title 1: Phishing Detection & Interception (Browser Extension)

### Final Title
> *"Proactive Phishing Detection and Interception via a Character-Level Hybrid CNN-LSTM Model"*

### Alternative
> *"Real-Time Phishing URL Interception Using a Hybrid CNN-LSTM Neural Network"*

### The Problem
Traditional database-driven blocklists cannot detect brand-new, "zero-day" phishing links. Philippine phishing websites surged 423% in a single year (2024-2025). Over 3.4 billion phishing emails sent daily worldwide. Median time for a victim to click a malicious link: just 21 seconds.

### Algorithms
*   **CNN:** Extracts local character-level patterns (suspicious substrings, unusual characters, abnormal TLDs)
*   **LSTM:** Captures sequential dependencies across the full URL string

### Unique Features
*   **Zero-Day Proactive Analysis:** Analyzes the raw character patterns of a URL to predict maliciousness (no database lookup needed).
*   **Chrome Extension:** Runs the model locally in milliseconds via TensorFlow.js (client-side, no server needed).
*   **Scope:** URL-level detection only (not email content, attachments, or SMS body analysis).

### Research Agenda & SDGs
*   **Agenda 4:** Cybersecurity Threat Detection and Mitigation
*   **SDG:** SDG 16 (Peace, Justice & Strong Institutions)

---

## Title 2: AI-Generated Image Detection (Comparative Study)

### Final Title
> *"Digital Fingerprints: A Comparative Evaluation of Neural Networks in Detecting GAN and Diffusion Image Artifacts"*

### Alternatives
> *"Catch Me If You GAN: Benchmarking Neural Networks Against Generative Image Artifacts"*
> *"Pixels Don't Lie (Or Do They?): A Comparative Study on Detecting AI-Generated Image Artifacts"*
> *"Seeing Isn't Believing: Benchmarking Neural Networks for AI-Generated Image Detection"*
> *"Beyond the Naked Eye: A Comparative Analysis of Neural Network Algorithms for AI-Generated Image Detection"*

### The Problem
500 million AI-generated images are created every day. The Philippines saw 4,500% increase in deepfake-related fraud in 2023. Philippine government officials themselves circulated a deepfake video. The DOJ, PCO, and DICT signed a whole-of-government campaign against deepfakes.

### Algorithms (Comparative — 3 architectures head-to-head)
*   **ResNet** — Classic deep convolutional architecture
*   **EfficientNet** — Efficiency-optimized convolutional architecture
*   **Vision Transformer (ViT)** — Attention-based architecture

### What This Study Does
Compares all 3 algorithms on the **same dataset** (real, GAN-generated, and diffusion-generated images) measuring:
1. Classification accuracy (per-algorithm and per-artifact type: GAN vs. Diffusion)
2. Processing (inference) speed
3. Statistical significance of differences
4. Which algorithm offers the most practical accuracy-speed trade-off

### Research Agenda & SDGs
*   **Agenda 4:** Cybersecurity Threat Detection and Mitigation
*   **SDG:** SDG 16 (Peace, Justice & Strong Institutions)

---

## Title 3: Concrete Crack Classification & Severity Grading

### Final Title
> *"Concrete Crack Classification and Severity Grading Using Explainable Transfer Learning"*

### Alternative
> *"Concrete Crack Classification and Millimetric Severity Profiling Using Explainable Transfer Learning"*

### The Problem
Manual visual inspections are slow, subjective, and inconsistent. Magnitude 7.8 earthquake hit Mindanao in June 2026 (8+ deaths, P1B damage). DPWH assessed over 21,000 buildings in 2025. Engineers are stretched thin across thousands of structures.

### Algorithms
*   **Transfer Learning:** Fine-tunes a pretrained CNN (not trained from scratch)
*   **Grad-CAM:** Explainability method that highlights which image regions influenced the classification

### What This Study Does
1. Classifies concrete images as cracked or non-cracked
2. Grades severity into tiers (hairline, minor, moderate, severe) based on structural inspection criteria
3. Generates Grad-CAM visual explanations so engineers can trust/override the AI's judgment

### Research Agenda & SDGs
*   **Agenda 1:** Emerging Technologies in Computer Science
*   **SDGs:** SDG 9 (Industry & Infrastructure), SDG 11 (Sustainable Cities)

---

## Tech Stack (Same for All 3 Titles)

| Component | Technology | Cost |
|---|---|---|
| AI Model | Python + TensorFlow/Keras | FREE |
| Model Training | Google Colab (free GPU in browser) | FREE |
| Web App Frontend | React / Next.js | FREE |
| Browser Extension | Chrome Manifest V3 + TensorFlow.js | FREE |
| Hosting | Vercel (test via phone browser) | FREE |
| Datasets | Kaggle / public datasets | FREE |

**Total cost: P0**

---

## How the Work is Split

*   **AI Assistant:** Writes all code, trains the model templates, drafts thesis chapters, and compiles verified references.
*   **Rogie & Daniela:** Run the training on Google Colab (just click "Run"), collect some local test samples, study the concepts for the defense, and present the slides.

---

## Backup Titles
If the panel rejects any of our primary 3 titles, we can instantly pivot to one of these backups:

### Backup 1: Scheduling Optimization
*   **Title:** *"Improving Scheduling Efficiency Using Constraint Satisfaction Programming"*
*   **Algorithm:** Constraint Satisfaction Programming (CSP)
*   **Use case:** Automating exam proctor scheduling and room assignments at NDMC. Eliminates time conflicts and unequal workloads.

### Backup 2: Phishing Email Detection (Comparative)
*   **Title:** *"Machine Learning-Based Phishing Email Detection: A Comparative Analysis of Classification Algorithms"*
*   **Algorithms:** Comparative analysis of ML classifiers (Random Forest, SVM, Naive Bayes, etc.)
*   **Use case:** Email-level phishing detection. Complementary to URL-level Title #1.
