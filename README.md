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
| **Week 4** | July 13-19, 2026 | **🚨 TITLE DEFENSE** — Presented 3 titles to panel | ✅ Done |
| **Week 5+** | July 20 onwards | **Proposal Writing** — Chapters 1 & 2 | 🔄 In Progress |

---

## 🏆 The 3 Thesis Titles

> **Main Title (Priority):** Title 2 — Mobile Wallet Receipt Forgery Detection

---

### Title 1: Digital Fingerprints — GAN & Diffusion Image Artifact Detection
*   **Full Title:** **"Digital Fingerprints: A Comparative Evaluation of Neural Networks in Detecting GAN and Diffusion Image Artifacts"**
*   **Domain:** Image Forensics / Deep Learning / Computer Vision
*   **Research Agenda:** Agenda 1: Emerging Technologies in Computer Science
*   **SDGs:** SDG 16 (Peace, Justice & Strong Institutions)
*   **Algorithms Compared:** ResNet, EfficientNet, Vision Transformer (ViT)

#### Objectives:
1. Determine classification accuracy of each algorithm in detecting GAN-generated and diffusion-generated image artifacts.
2. Determine average processing (inference) speed of each algorithm.
3. Determine whether there is a statistically significant difference among the three algorithms in classification accuracy and processing speed.
4. Identify which algorithm offers the most practical trade-off between accuracy and speed for real-world deployment.

#### Statement of the Problem:
> The rapid advancement of GANs and Diffusion models has made it increasingly difficult to distinguish authentic from AI-generated images [1]. While various neural network architectures are employed, there remains a critical gap in understanding how different models compare when balancing detection accuracy with computational efficiency, as detectors trained on one generative family often fail to generalize to the other [3].

#### Research Questions:
1. What is the classification accuracy of ResNet, EfficientNet, and ViT in detecting: (1.1) GAN-generated artifacts? (1.2) Diffusion-generated artifacts?
2. What is the average processing speed of each algorithm?
3. Is there a statistically significant difference among the three in: (3.1) Classification accuracy? (3.2) Processing speed?
4. Which offers the most practical trade-off between accuracy and speed?

#### Beneficiaries:
Social Media Platforms, Digital Forensic Units, Journalists & Fact-Checkers, AI/ML Researchers, The General Public.

#### Hypotheses (H₀):
- H₀₁: No significant difference among ResNet, EfficientNet, and ViT in classification accuracy.
- H₀₂: No significant difference among the three in inference speed.

#### References:
- [1] H. Chen et al., "Comprehensive exploration of diffusion models in image generation: A survey," *Artificial Intelligence Review*, vol. 58, no. 99, 2025.
- [2] N. Tasnim, K. Uddin, and K. M. Malik, "AI-generated image detection: An empirical study and future research directions," arXiv:2511.02791, 2025.
- [3] S. Wu et al., "Few-shot learner generalizes across AI-generated image detection," arXiv:2501.08763, 2025.

---

### ⭐ Title 2: Digital Deception in Your Pocket — Mobile Wallet Receipt Forgery Detection (MAIN TITLE)
*   **Full Title:** **"Digital Deception in Your Pocket: A Comparative Evaluation of CNN Architectures in Detecting Mobile Wallet Receipt Forgery"**
*   **Domain:** Image Forensics / Deep Learning / E-Commerce Safety
*   **Research Agenda:** Agenda 4: Cybersecurity Threat Detection and Prevention
*   **SDGs:** SDG 16 (Peace, Justice & Strong Institutions)
*   **Algorithms Compared:** Basic/Baseline CNN, ResNet50, MobileNetV2

#### Objectives:
1. Determine and compare the classification accuracy of Basic CNN, ResNet50, and MobileNetV2 in detecting:
   - 1.1. Manually edited transaction receipts (e.g., modified text or amounts)
   - 1.2. Programmatically generated fake transaction receipts
2. Compare performance using standard ML metrics: (2.1) Precision, (2.2) Recall, (2.3) F1-Score.
3. Compare inference speed and computational resource requirements for lightweight, GPU-free deployment.
4. Determine whether there is a significant difference in classification accuracy among the three models when analyzing: (4.1) Original high-resolution screenshots, (4.2) Heavily compressed images (e.g., transmitted via messaging platforms).
5. Identify which architecture offers the most practical balance of accuracy and efficiency for real-world transaction verification by local online sellers and student entrepreneurs at NDMC.

#### Statement of the Problem:
> Mobile wallet and e-payment platforms have become frequent targets of screenshot-based fraud, in which manipulated or fabricated transaction receipts are used to deceive sellers into releasing goods or services without actual payment [1]. Recent systems combining OCR with CNNs have demonstrated that tampered payment screenshots can be flagged effectively even on lightweight, GPU-free infrastructure [2]. Techniques such as ELA integrated with CNNs have proven effective in detecting pixel-level manipulations, although robustness against heavy compression typical of messaging platforms remains underexplored [3]. Deeper architectures such as ResNet have shown strong feature-extraction through residual learning [4], while MobileNetV2 has been purpose-built for efficient inference on resource-constrained devices [5].

#### Research Questions:
1. What is the classification accuracy of Basic CNN, ResNet50, and MobileNetV2 in detecting: (1.1) Manually edited receipts? (1.2) Programmatically generated fake receipts?
2. What is the performance of the three models in terms of: (2.1) Precision, (2.2) Recall, (2.3) F1-score?
3. What is the inference speed and computational resource requirement of each model?
4. Is there a significant difference in classification accuracy among the three when analyzing: (4.1) Original high-res screenshots? (4.2) Heavily compressed images?
5. Which architecture offers the most practical balance of accuracy and efficiency for real-world use by local online sellers and student entrepreneurs at NDMC?

#### Beneficiaries:
- **Local Online Sellers** — practical benchmarked tool to verify receipt authenticity before releasing goods.
- **Student Entrepreneurs (NDMC)** — accessible means of confirming mobile wallet transactions for small-scale businesses.
- **Mobile Wallet Providers** — comparative findings for strengthening fraud detection architectures.
- **Cybersecurity Researchers** — domain-specific comparative benchmark of CNN architectures.

#### Hypothesis (H₀):
- H₀: There is no significant difference in the classification accuracy among the Basic CNN, ResNet50, and MobileNetV2 models in detecting forgery in mobile wallet transaction receipts.

#### References:
- [1] C. Artaud et al., "Receipt dataset for fraud detection," in *Proc. 1st Int. Workshop on Computational Document Forensics (IWCDF)*, 2017.
- [2] K. S. Vaishnavi and K. P. Narayan, "FakePay: A real-time UPI fraud detection system using OCR, CNN, and ensemble ML," Technical Report, Mar. 2026.
- [3] A. M. Nagm et al., "Detecting image manipulation with ELA-CNN integration," *PeerJ Computer Science*, vol. 10, p. e2205, 2024.
- [4] K. He et al., "Deep residual learning for image recognition," in *Proc. IEEE CVPR*, 2016, pp. 770-778.
- [5] M. Sandler et al., "MobileNetV2: Inverted residuals and linear bottlenecks," in *Proc. IEEE CVPR*, 2018, pp. 4510-4520.

---

### Title 3: Proactive Phishing URL Detection
*   **Full Title:** **"Proactive Phishing URL Detection Using Feature-Based Machine Learning Classifiers"**
*   **Domain:** Cybersecurity / Machine Learning / NLP
*   **Research Agenda:** Agenda 4: Cybersecurity Threat Detection and Prevention
*   **SDGs:** SDG 16 (Peace, Justice & Strong Institutions)
*   **Algorithms Compared:** Random Forest, Support Vector Machine (SVM), XGBoost

#### Objectives:
1. Identify engineered features extractable from URL datasets (URL length, hyphen count, "@" symbol, subdomain count, HTTPS status, Levenshtein brand-name similarity).
2. Evaluate RF, SVM, and XGBoost performance using accuracy, precision, recall, F1-score, and AUC-ROC.
3. Compare training time and prediction latency across three classifiers.
4. Determine which classifier yields the best balance of detection performance and computational efficiency.

#### Statement of the Problem:
> Phishing remains one of the most prevalent cyberattack forms, with attackers continuously modifying URL structures to evade blacklist-based defenses, which are inherently reactive [1]. ML classifiers on lexical/structural features show strong potential, with ensemble methods achieving high accuracy [2]. However, existing works rarely compare detection performance against computational efficiency for real-time deployment [3].

#### Research Questions:
1. What are the engineered features extractable from a URL dataset? (1.1–1.6)
2. What is the performance of RF, SVM, and XGBoost on the same feature set? (accuracy, precision, recall, F1, AUC-ROC)
3. Is there a significant difference among the three in: (3.1) Training time? (3.2) Prediction latency?
4. Which classifier yields the most favorable balance of detection performance and efficiency?

#### Beneficiaries:
Internet Users, Cybersecurity Practitioners, System Developers, Future Researchers, NDMC.

#### Hypothesis (H₀):
- H₀: There is no significant difference in the detection performance of RF, SVM, and XGBoost when trained on the same engineered URL features.

#### References:
- [1] S. Hamadouche et al., "Combining lexical, host, and content-based features for phishing websites detection using ML models," *EAI Endorsed Trans. on Scalable Information Systems*, vol. 11, no. 6, 2024.
- [2] M. Tellakula et al., "ML-based phishing URL detection using lexical and structural features," *Int. J. Computer Applications*, vol. 187, no. 96, pp. 1–5, Apr. 2026.
- [3] B. Gupta et al., "A novel approach for phishing URLs detection using lexical based ML in a real-time environment," *Computer Communications*, vol. 175, pp. 47–57, 2021.

---

## ❌ Rejected Titles Record
1. ~~"Learning-Based Algorithm Selection for Lossless File Compression"~~ — Rejected (no clear victim/respondents).
2. ~~"Accuracy Evaluation of a Fine-Tuned Convolutional Neural Network for Forgery Detection in Mobile Wallet Receipts"~~ — Replaced by the new comparative version (Title 2 above).

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

## 📁 Key Project Files

*   📄 [README.md](README.md) — Central project hub (this file).
*   📄 [student_info.md](student_info.md) — Student profiles and confirmed titles.
*   📄 [bscs_thesis_guidelines.md](bscs_thesis_guidelines.md) — NDMC thesis formatting rules.
*   📄 `NDMC Thesis Guidelines v5 - 2025.pdf` — Official college-wide thesis guidelines.
*   📄 `Research Outline for CITE 2024.pdf` — Official BSCS research outline.
*   📄 [summary_for_daniela.md](summary_for_daniela.md) — Summary review sheet for Daniela.
*   📄 [implementation_plan.md](implementation_plan.md) — Thesis implementation roadmap.

---

## 💻 Git Synchronization

*   **Repository:** [DeathKnell837/NDMC-BSCS-THESIS-PREP](https://github.com/DeathKnell837/NDMC-BSCS-THESIS-PREP)
*   **Google Drive:** [Shared Folder](https://drive.google.com/drive/folders/1bzRsI6Ywo2yRni5Ij7InCLh0CL0OO90_?usp=drive_link)
*   **Sync Commands:**
    ```bash
    git pull origin main
    git add -A && git commit -m "update" && git push origin main
    ```
