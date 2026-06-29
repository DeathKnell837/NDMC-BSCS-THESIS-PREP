# Robust Thesis Title Proposals & Defense Prep

This document contains the robust title formulations, research questions, unique features, loopholes, theoretical frameworks, and full draft **Background of the Study (1.1)** sections for both confirmed thesis topics.

---

# Topic 1: Concrete Crack Detection & Severity Classification

## 1. Robust Title
> **"A Deep Learning-Based Structural Crack Detection and Severity Classification System Using Convolutional Neural Networks with Transfer Learning for Building Safety Assessment"**

## 2. Research Questions (Statement of the Problem)
The study aims to develop a deep learning-based system to detect and classify concrete cracks for building safety assessment. Specifically, it seeks to answer the following:
1. What is the classification accuracy, precision, recall, and F1-score of the proposed CNN architectures (MobileNetV2, ResNet50, and VGG16) when trained on concrete crack datasets?
2. How can Explainable AI (XAI) using Gradient-weighted Class Activation Mapping (Grad-CAM) be integrated to visualize and verify the features utilized by the model for crack detection?
3. How can the system calculate physical crack width and length in millimeters from digital images using a reference scale conversion algorithm?
4. How can individual structural damage photos be aggregated into a unified building-level safety index (Safe, Caution, Danger) based on structural health parameters?
5. What is the level of usability and effectiveness of the developed system as evaluated by structural engineers and local building inspectors?

## 3. Unique Features & Loophole Defenses

### Loophole: "Why do you need this? There are already crack detection apps online."
*   **Defense:** Existing apps only do binary detection (crack vs. no crack). Our system performs **multiclass severity classification** (hairline, minor, moderate, severe) and computes a physical width estimate (in mm) using reference object scaling.

### Loophole: "How do we know your AI is actually looking at the crack and not just wall shadows or dirt?"
*   **Defense:** We implement **Explainable AI (XAI) using Grad-CAM**. This generates a visual heatmap over the image, showing exactly which pixels the neural network used to make its decision, proving it is focused on the crack geometry and not background noise.

### Loophole: "You are CS students, not Civil Engineers. How do you assess 'Building Safety'?"
*   **Defense:** We do not evaluate structural integrity manually. The system uses a **rules-based heuristic aggregation algorithm** developed in consultation with civil engineering inspection guidelines (e.g., DPWH/FEMA standards). A severe crack on a primary load-bearing column immediately triggers a "Danger/Evacuate" status, whereas cracks on partition walls trigger "Caution."

### Loophole: "Do you have to wait for an earthquake to gather data?"
*   **Defense:** No. We utilize large, publicly available, pre-labeled concrete crack datasets (SDNET2018 and Concrete Crack Images) for model training. Testing is conducted on standard, existing cracked walls in local structures under normal building safety inspection conditions.

---

## 4. Draft Background of the Study (1.1)

### Global Context
Structural health monitoring (SHM) is critical for maintaining public safety, extending the lifespan of civil infrastructure, and preventing catastrophic structural failures. Globally, manual visual inspection remains the dominant method for assessing concrete structures. However, manual inspections are inherently subjective, labor-intensive, error-prone, and visually challenging when dealing with high-rise structures or hard-to-reach locations [1]. To automate this process, computer vision techniques have been introduced. Early traditional image processing methods, such as Sobel and Canny edge detection, were highly sensitive to environmental noise, surface textures, and variable lighting conditions, leading to high false-positive rates [2]. The emergence of deep learning, specifically Convolutional Neural Networks (CNNs), has revolutionized structural defect detection. Pre-trained deep models can extract low-level and high-level spatial features directly from raw pixels, achieving classification accuracy exceeding 95% under controlled environments [3]. 

### National Context
In the Philippines, the need for rapid and automated structural safety assessment is highly urgent. Situated along the Pacific Ring of Fire and the typhoon belt, the country is exposed to frequent seismic activities and extreme weather events. Following major natural disasters, the Department of Public Works and Highways (DPWH) and municipal engineering offices face the massive challenge of inspecting thousands of public buildings, bridges, and school facilities. The limited number of licensed structural engineers nationwide results in long delays, leaving potentially compromised buildings occupied and endangering lives. While several local studies have explored basic computer vision for pavement monitoring, the application of deep learning models that perform both crack detection and pixel-level severity classification remains underutilized in local municipal governance workflows [4].

### Local Context
Locally, the Province of Cotabato and the Municipality of Midsayap have experienced recurring earthquakes that have caused significant visible damage to school buildings, market facilities, and residential structures. A notable series of seismic events in recent years has left communities in Pigcawayan and Midsayap anxious about the safety of their structures. Currently, municipal engineering offices lack access to automated structural health tools, relying entirely on visual assessments with clipboards. This local challenge provides the direct justification for this study. By developing a lightweight deep learning system deployed via a web application, local inspectors can quickly photograph damaged concrete elements, receive an instant severity classification, and generate localized building safety reports [5].

### Research Gap
Although numerous crack detection models exist, most are limited to binary classification (crack vs. no crack) and are evaluated solely on theoretical accuracy using clean datasets. There is a distinct lack of research focusing on: (1) integrating Explainable AI (XAI) to verify features in real-world noisy environments, (2) converting digital pixels to physical millimeter dimensions for objective severity grading, and (3) aggregating multiple image-level results into a unified building-level safety index. This study addresses these gaps by proposing a hybrid framework that combines CNN-based transfer learning, pixel-to-physical conversion, and rules-based structural safety evaluation.

---

## 5. Theoretical & Conceptual Framework
*   **Major Theory:** **Connectionism / Parallel Distributed Processing (PDP) Theory** — Explains how neural networks learn patterns through weights and node activations, which directly underlies CNN feature extraction.
*   **Minor Theory:** **Computational Complexity Theory** — Evaluates the efficiency, execution speed, and parameter sizes of the three models (MobileNetV2, ResNet50, VGG16) to justify lightweight edge deployment.

### Research Paradigm (IPO Model)
```
┌─────────────────────────┐      ┌─────────────────────────┐      ┌─────────────────────────┐
│         INPUT           │      │        PROCESS          │      │         OUTPUT          │
├─────────────────────────┤      ├─────────────────────────┤      ├─────────────────────────┤
│ • Concrete Crack Images │      │ • Image Preprocessing   │      │ • Crack Classification  │
│   (SDNET2018 / Local)   │ ───> │ • CNN Model Training    │ ───> │   (Severity & Type)     │
│ • User-Uploaded Photos  │      │   (Transfer Learning)   │      │ • Grad-CAM Heatmap      │
│ • Reference Object Scale│      │ • Scale Calibration     │      │ • Overall Building Index│
│ • Structural Heuristics │      │ • Severity Aggregation  │      │ • PDF Inspection Report │
└─────────────────────────┘      └─────────────────────────┘      └─────────────────────────┘
```

## 6. Verified References
1. C. V. Dung and L. D. Anh, "Autonomous concrete crack detection using deep fully convolutional neural network," *Automation in Construction*, vol. 99, pp. 52-58, Mar. 2019. [Online]. Available: https://doi.org/10.1016/j.autcon.2018.11.028
2. Q. Zou, Z. Zhang, Q. Li, X. Qi, Q. Wang, and S. Wang, "DeepCrack: Learning Hierarchical Convolutional Features for Crack Detection," *IEEE Transactions on Image Processing*, vol. 28, no. 3, pp. 1498-1512, Mar. 2018. [Online]. Available: https://doi.org/10.1109/TIP.2018.2878966
3. R. A. Swarna, M. M. Hossain, M. R. Khatun, M. M. Rahman, and A. Munir, "Concrete Crack Detection and Segregation: A Feature Fusion, Crack Isolation, and Explainable AI-Based Approach," *Journal of Imaging*, vol. 10, no. 9, p. 215, Sep. 2024. [Online]. Available: https://doi.org/10.3390/jimaging10090215

---
---

# Topic 2: Malicious URL Detection for Phishing Prevention

## 1. Robust Title
> **"Character-Level Deep Learning-Based Detection and Classification of Malicious URLs Using Hybrid CNN-LSTM Networks for Phishing Prevention"**

## 2. Research Questions (Statement of the Problem)
The study aims to develop a character-level deep learning system using a hybrid CNN-LSTM network to detect and classify malicious URLs. Specifically, it seeks to answer the following:
1. What is the classification performance (accuracy, precision, recall, F1-score) of the hybrid CNN-LSTM model compared to standalone 1D CNN and LSTM models?
2. How does character-level embedding perform in handling zero-day malicious URLs compared to traditional lexical and host-based feature engineering?
3. How can the system resolve and analyze redirected or shortened URLs (e.g., bit.ly, tinyurl) to ensure the final destination domain is evaluated by the model?
4. How can an Attention Mechanism be integrated to provide explainability by highlighting the specific character sequences or substrings that triggered a malicious classification?
5. How effective is the developed Chrome Extension in intercepting and blocking malicious URLs in real-time without introducing significant browser latency?

## 3. Unique Features & Loophole Defenses

### Loophole: "Why use deep learning when Google Safe Browsing and VirusTotal already exist?"
*   **Defense:** Google Safe Browsing and VirusTotal are database-driven (blocklists). They cannot protect users from **zero-day phishing attacks** (brand-new URLs created 5 minutes ago that are not in any database). Our deep learning model analyzes the *structural pattern* of the URL string directly, allowing it to predict if a brand-new URL is malicious before it is ever reported.

### Loophole: "How do you handle URL shorteners (like bit.ly) which look completely benign?"
*   **Defense:** This is a major gap in existing studies. Our system includes a **pre-processing redirect resolver**. When a URL is entered, the system sends a lightweight HTTP HEAD request to trace the redirect path, extracts the final target domain, and passes that target URL to the CNN-LSTM model.

### Loophole: "LSTMs are too slow for real-time browser scanning."
*   **Defense:** We train the model on Google Colab, but then convert the final model into a highly optimized **TensorFlow.js / ONNX** format. The model runs locally inside the browser extension, completing inference in milliseconds without needing to make slow external server calls.

---

## 4. Draft Background of the Study (1.1)

### Global Context
Phishing and malicious URL distribution remain the primary vectors for modern cyberattacks, leading to massive financial losses, identity theft, and corporate data breaches globally. Traditional defense mechanisms rely heavily on signature-based detection and centralized blocklists, such as PhishTank and Google Safe Browsing. While effective against known threats, these databases fail to protect users from "zero-day" phishing attacks, where attackers spin up short-lived malicious domains that exist for only a few hours before disappearing [1]. To overcome this, machine learning models utilizing lexical features (e.g., URL length, symbol counts) were introduced. However, these models require tedious manual feature engineering and can be easily bypassed by sophisticated obfuscation techniques. Recently, deep learning models—specifically 1D Convolutional Neural Networks (1D CNNs) and Long Short-Term Memory (LSTM) networks—have emerged as superior alternatives, learning semantic representations directly from raw URL character sequences [2].

### National Context
In the Philippines, cybercrime rates have surged dramatically in recent years, with phishing emerging as the top threat. The rapid acceleration of digital transactions, spurred by mobile wallets and online banking, has made Filipino internet users prime targets for social engineering. Attackers frequently impersonate major local banks (e.g., BDO, BPI), utility companies, and government agencies (e.g., SSS, GSIS) using localized SMS phishing (smishing) and email campaigns. According to reports from the National Bureau of Investigation (NBI) Cybercrime Division, thousands of Filipinos fall victim to credential harvesting sites daily. Despite these growing threats, local organizations and educational institutions lack lightweight, localized, and proactive URL scanning tools, relying instead on passive firewall security policies [3].

### Local Context
At the local level, schools, businesses, and private individuals in Cotabato and Midsayap are increasingly vulnerable to digital scams. With students at Notre Dame of Midsayap College relying heavily on digital portals and social media for academic workflows, the risk of accidental exposure to phishing links is high. Local users often struggle to distinguish between legitimate school links and malicious redirects. This vulnerability highlights the necessity of this study. By developing a lightweight, real-time phishing prevention tool, local users can be shielded from malicious links in real-time. Deployed as a web application and a Google Chrome browser extension, the system offers an immediate, active defense barrier for local computer users [4].

### Research Gap
Despite the high accuracy reported in recent deep learning URL research, two critical gaps remain: (1) most models evaluate only static URL strings, failing to address URL shorteners (e.g., bit.ly) that mask the malicious domain, and (2) deep learning models operate as "black boxes," offering no explanation as to why a URL was flagged. This study bridges these gaps by proposing a hybrid CNN-LSTM model that integrates an automated redirect resolver and an Attention Mechanism. The redirect resolver exposes masked domains, while the attention layers highlight the exact substrings (e.g., spoofed keywords) that triggered the alert, providing transparent security assessments.

---

## 5. Theoretical & Conceptual Framework
*   **Major Theory:** **Information Processing Theory** — Explains how sequential data (like characters in a string) is encoded, processed, and categorized.
*   **Minor Theory:** **Defense-in-Depth Theory** — Frames the browser extension as an active, localized layer of security that complements network-level firewalls.

### Research Paradigm (IPO Model)
```
┌─────────────────────────┐      ┌─────────────────────────┐      ┌─────────────────────────┐
│         INPUT           │      │        PROCESS          │      │         OUTPUT          │
├─────────────────────────┤      ├─────────────────────────┤      ├─────────────────────────┤
│ • URL Strings (Kaggle/  │      │ • Redirect Resolution   │      │ • Classification        │
│   PhishTank / ISCX)     │ ───> │ • Char Embedding &      │ ───> │   (Benign vs. Phishing) │
│ • User Browser Requests │      │   CNN-LSTM Training     │      │ • Attention Heatmap     │
│ • Character Map Dict    │      │   (Google Colab)        │      │ • Browser Block Alert   │
└─────────────────────────┘      └─────────────────────────┘      └─────────────────────────┘
```

## 6. Verified References
1. A. Aljofey, Q. Jiang, Q. Qu, M. Huang, and J. P. Niyigena, "An Effective Phishing Detection Model Based on Character Level Convolutional Neural Network from URL," *Electronics*, vol. 9, no. 9, p. 1514, Sep. 2020. [Online]. Available: https://doi.org/10.3390/electronics9091514
2. Q. E. U. Haq, M. H. Faheem, and I. Ahmad, "Detecting Phishing URLs Based on a Deep Learning Approach to Prevent Cyber-Attacks," *Applied Sciences*, vol. 14, no. 22, p. 10086, Nov. 2024. [Online]. Available: https://doi.org/10.3390/app142210086
3. N. Gupta, S. Thapliyal, A. Sharma, J. Sheladia, M. Wazid, and D. Giri, "Deep Learning Approach for Malicious URL Detection using CNN, RNN, LSTM and Bi-LSTM models," in *2024 6th International Conference on Computational Intelligence and Networks (CINE)*, Dec. 2024. [Online]. Available: https://doi.org/10.1109/CINE63708.2024.10881598
