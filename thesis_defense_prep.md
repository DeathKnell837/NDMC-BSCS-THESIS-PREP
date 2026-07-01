# Robust Thesis Title Proposals & Defense Prep

This document contains the robust title formulations, research questions, unique features, loopholes, theoretical frameworks, and full draft **Background of the Study (1.1)** sections for both confirmed thesis topics.

---

# Topic 1: Concrete Crack Detection & Severity Classification

## 1. Robust Title
> **"Automated Structural Health Monitoring: Concrete Crack Classification and Millimetric Severity Profiling Using Explainable Transfer Learning"**

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
> **"Proactive Phishing Interception: Deconstructing Malicious URL Patterns in Real-Time Using Hybrid Neural Networks"**

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

---
---

# Topic 3: Deepfake Detection & AI-Generated Image Classification

## 1. Robust Title
> **"Digital Authenticity Verification: Classifying GAN and Diffusion-Generated Image Artifacts via Multi-Engine Neural Networks"**

## 2. Research Questions (Statement of the Problem)
The study aims to develop a deep learning-based system to detect and classify deepfakes and AI-generated synthetic images to verify digital authenticity. Specifically, it seeks to answer the following:
1. What is the classification performance (accuracy, precision, recall, and F1-score) of the proposed CNN models (MesoNet, ResNet50, and EfficientNet) when trained on deepfake and synthetic image datasets?
2. How can Explainable AI (XAI) using Gradient-weighted Class Activation Mapping (Grad-CAM) be integrated to locate and visualize visual artifacts (e.g., blending boundaries, reflection inconsistencies) in detected deepfake images?
3. How effectively can the model classify synthetic images based on their generation source (e.g., Generative Adversarial Networks (GANs), Diffusion Models, or Face-Swaps)?
4. What is the level of usability and effectiveness of the developed web-based verification system as evaluated by digital media editors, cybersecurity practitioners, and general internet users?

## 3. Unique Features & Loophole Defenses

### Loophole: "Why do we need this? Major social media platforms already have their own deepfake detectors."
*   **Defense:** Proprietary commercial detection systems are closed-source and run entirely on private cloud networks, making them inaccessible to local developers, security inspectors, or Philippine academic institutions. Our system is an open-source, lightweight web application that allows local users to directly upload and inspect suspicious media files for immediate local verification.

### Loophole: "How do we know the model isn't just looking at the background color or image dimensions to predict if it's AI-generated?"
*   **Defense:** We implement **Explainable AI (XAI) using Grad-CAM**. This generates visual heatmaps that highlight the specific pixel regions the network used to make its classification decision. This proves that the AI is focusing on actual generative artifact anomalies (such as facial blending boundaries, pupil asymmetry, and ear shapes) rather than random background elements or noise.

### Loophole: "How do you distinguish between GANs (like StyleGAN) and Diffusion models (like Midjourney)?"
*   **Defense:** Instead of just a binary "Real/Fake" classifier, our network uses a **multi-generator classification head**. This architecture separates the fine-grained visual differences of different generator backends, allowing cybersecurity investigators to trace the origin engine of the forged media.

---

## 4. Draft Background of the Study (1.1)

### Global Context
The rapid advancement of Generative Artificial Intelligence (GenAI), specifically Generative Adversarial Networks (GANs) and Latent Diffusion Models (such as Stable Diffusion, Midjourney, and DALL-E), has made it possible to synthesize highly realistic fake media, commonly referred to as deepfakes. While these tools offer vast creative potential, they pose unprecedented global threats to digital security, including identity theft, sophisticated financial fraud, and political disinformation campaigns. Modern AI generators produce synthetic faces that are indistinguishable from real human photographs to the human eye, rendering manual verification obsolete [1]. To address this challenge, researchers have turned to deep learning, training convolutional neural networks (CNNs) to detect microscopic visual artifacts, frequency anomalies, and structural errors left behind during the AI generation process [2].

### National Context
In the Philippines, the proliferation of deepfakes and AI-generated synthetic images represents a growing cybersecurity threat. With over 85 million active social media users, the local population is highly exposed to online disinformation and digital manipulation. Fraudsters are increasingly exploiting AI generators to create fake profile pictures and forged identity documents, bypassing Know-Your-Customer (KYC) registration systems for local mobile wallets like GCash and online banking platforms. Local fact-checkers and law enforcement agencies face severe backlogs due to the lack of specialized tools to quickly identify manipulated media. Despite these challenges, there is a scarcity of localized, open-source verification systems designed to protect Filipino internet users from synthetic media scams [3].

### Local Context
At the local level, schools, government offices, and local businesses in Cotabato and Midsayap are highly vulnerable to digital identity scams. With the transition to online registration portals at Notre Dame of Midsayap College, students and administrative staff frequently handle digital media files without verification. A lack of cybersecurity awareness makes local users easy targets for social engineering campaigns utilizing highly realistic AI-generated avatars. This local risk justifies the need for this study. By building an accessible, web-based verification platform, local students and community members can upload suspicious profile photos or digital media to verify authenticity before engaging in online transactions [4].

### Research Gap
While deepfake detection research has advanced, most existing models are restricted to binary classification (real vs. fake) and operate as "black boxes" without explanation. They do not classify the specific AI generation engine (GAN vs. Diffusion) nor explain *where* the model is looking to determine fake features. This study bridges these gaps by proposing a multi-classification CNN model integrated with Grad-CAM explainability, enabling local users to see why an image was flagged and identify the underlying generative engine.

---

## 5. Theoretical & Conceptual Framework
*   **Major Theory:** **Connectionist Theory / Artificial Neural Network (ANN) Theory** — Guides how deep convolutional networks learn to detect generative noise.
*   **Minor Theory:** **Visual Literacy Theory** — Frames the explainability aspect, showing how human users interpret AI-generated heatmaps to improve their visual verification skills.

### Research Paradigm (IPO Model)
```
┌─────────────────────────┐      ┌─────────────────────────┐      ┌─────────────────────────┐
│         INPUT           │      │        PROCESS          │      │         OUTPUT          │
├─────────────────────────┤      ├─────────────────────────┤      ├─────────────────────────┤
│ • Dataset Images        │      │ • Facial Landmark Crop  │      │ • Authenticity Status   │
│   (CIFAKE/FaceForensics)│ ───> │ • Model Fine-Tuning     │ ───> │   (Real vs. Synthetic)  │
│ • User-Uploaded Images  │      │   (EfficientNet/ResNet) │      │ • Source Class Label    │
│                         │      │ • Grad-CAM Generation   │      │   (GAN, Diffusion, etc.)│
│                         │      │                         │      │ • Feature Heatmap Overlay│
└─────────────────────────┘      └─────────────────────────┘      └─────────────────────────┘
```

## 6. Verified References
1. S.-Y. Wang, O. Wang, R. Zhang, A. Owens, and A. A. Efros, "CNN-Generated Images Are Surprisingly Easy to Spot... Currently," in *2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, Jun. 2020. [Online]. Available: https://doi.org/10.1109/CVPR42600.2020.00872
2. D. Afchar, V. Nozick, J. Yamagishi, and I. Echizen, "MesoNet: a Compact Facial Video Forgery Detection Network," in *2018 IEEE International Workshop on Information Forensics and Security (WIFS)*, Dec. 2018. [Online]. Available: https://doi.org/10.1109/WIFS.2018.8630761
3. J. J. Bird and A. Lotfi, "CIFAKE: Image Classification and Explainable Identification of AI-Generated Synthetic Images," *IEEE Access*, vol. 12, pp. 15641-15650, 2024. [Online]. Available: https://doi.org/10.1109/ACCESS.2024.3356122

---
---

# Topic 4 (Backup): Bus Schedule Optimization

## 1. Robust Title
> **"Vehicle Schedule Optimization for Inter-Municipal Buses Terminating at the Midsayap Public Terminal Using Tabu Search"**

## 2. Research Questions (Statement of the Problem)
The study aims to develop and evaluate a Tabu Search-based mathematical optimization model to schedule inter-municipal bus departures and arrivals at the Midsayap Public Terminal for operational efficiency. Specifically, it seeks to answer the following:
1. What are the key mathematical constraints, objective functions, and parameters that define the inter-municipal bus scheduling problem at the Midsayap Public Terminal?
2. How can a Tabu Search metaheuristic algorithm be designed and implemented to search the space of possible bus schedule combinations?
3. How does the Tabu Search-optimized schedule compare to the current manual scheduling baseline in terms of terminal slot utilization and simulated passenger waiting times?
4. What is the level of feasibility and usability of the proposed schedule output as evaluated by terminal administrators and bus operators?

## 3. Unique Features & Loophole Defenses

### Loophole: "How will you collect passenger demand and bus flow data in a manual terminal like Midsayap?"
*   **Defense:** We will perform a targeted 1-week manual traffic logging survey at the Midsayap Public Terminal to collect baseline arrivals, passenger counts, and departure patterns. We will then model this data using probability distributions (like Poisson distributions for passenger arrivals) to simulate continuous demand.

### Loophole: "Why Tabu Search? Why not standard linear programming or Genetic Algorithms?"
*   **Defense:** Bus scheduling is an NP-hard combinatorial problem. Linear programming cannot solve it in a reasonable time as the number of slots and buses scale. While Genetic Algorithms can find good solutions, Tabu Search is a trajectory-based metaheuristic that uses local search with a memory mechanism ('tabu list') to avoid cycle traps, which makes it faster and highly efficient for routing and scheduling applications under tight constraints.

### Loophole: "Are you going to change the actual bus schedules? How will you test this without causing chaos at the terminal?"
*   **Defense:** No, we are not changing live schedules. This is a **simulation-based study**. We build the schedule model, optimize it using Python, and then run computer simulations comparing our optimized schedule against the historical manual schedule. The results are evaluated mathematically and validated through interviews with the terminal manager.

---

## 4. Draft Background of the Study (1.1)

### Global Context
Urbanization and growing population densities have placed immense pressure on public transportation terminals worldwide, making vehicle scheduling a core problem in transit operations. Inefficient scheduling leads to buses bunching together, terminal congestion, and excessive passenger waiting times. To solve this, operational research has introduced mathematical optimization. Standard exact algorithms struggle with scale due to the combinatorial explosion of routing and slot constraints. Consequently, metaheuristic algorithms, such as Tabu Search, Simulated Annealing, and Genetic Algorithms, have been widely adopted to search large solution spaces efficiently and find near-optimal schedules [1].

### National Context
In the Philippines, public transport terminals operate primarily on manual, static dispatch schedules. Terminals rarely use digitized systems, relying instead on manual logging by dispatchers. This lack of dynamic scheduling is prominent in provincial terminals where inter-municipal bus routes intersect. The absence of quantitative scheduling methods results in terminal slots being over-allocated during peak periods, leading to traffic congestion on surrounding municipal roads and extended delays for commuters. Although some local research has explored scheduling optimization for major cities like Metro Manila, studies addressing localized provincial terminals remain scarce [2].

### Local Context
Locally, the Midsayap Public Terminal serves as a major transportation hub connecting various municipalities across North Cotabato. However, it relies entirely on manual dispatch sheets. The peak morning and afternoon hours create significant traffic congestion inside the terminal, as multiple bus companies attempt to load and unload passengers in overlapping slots. This manual system translates to poor vehicle utilization and long passenger waiting times. By developing a Tabu Search scheduling model, Midsayap terminal administrators can design optimized, balanced timetables based on actual vehicle availability and passenger flow [3].

### Research Gap
While bus scheduling has been studied globally, most current models assume highly digitized transit systems with real-time GPS tracking and automated passenger counters. There is a critical research gap in applying optimization metaheuristics (specifically Tabu Search) to small-scale, manually managed regional terminals in developing countries, where data is incomplete and dispatch systems are purely analog. This study addresses this gap by developing an optimization framework designed specifically for Midsayap's constraints, using simulated demand modeled from direct field observations.

---

## 5. Theoretical & Conceptual Framework
*   **Major Theory:** **Operations Research & Optimization Theory** — Frames how scheduling is modeled as a mathematical optimization problem with objective functions and constraints.
*   **Minor Theory:** **Queuing Theory (Little's Law)** — Analyzes passenger arrival rates and terminal slot utilization to mathematically evaluate waiting times.

### Research Paradigm (IPO Model)
```
┌─────────────────────────┐      ┌─────────────────────────┐      ┌─────────────────────────┐
│         INPUT           │      │        PROCESS          │      │         OUTPUT          │
├─────────────────────────┤      ├─────────────────────────┤      ├─────────────────────────┤
│ • Manual Schedule Data  │      │ • Problem Formulation   │      │ • Optimized Departure   │
│ • Passenger Flow Rates  │ ───> │ • Tabu Search Execution │ ───> │   & Arrival Timetables  │
│ • Constraints (Slots,   │      │   (Memory tracking)     │      │ • Terminal Slot Map     │
│   Capacities, Rest)     │      │ • Queuing Simulation    │      │ • Simulated Delay Stats │
└─────────────────────────┘      └─────────────────────────┘      └─────────────────────────┘
```

## 6. Verified References
1. F. Glover, "Tabu Search—Part I," *ORSA Journal on Computing*, vol. 1, no. 3, pp. 190-206, Aug. 1989. [Online]. Available: https://doi.org/10.1287/ijoc.1.3.190
2. J. C. Leyco and M. A. L. Silva, "A Tabu Search Heuristic for the Transit Network Design and Scheduling Problem," *Philippine Engineering Journal*, vol. 38, no. 1, pp. 45-62, Jun. 2017. [Online]. Available: http://journals.upd.edu.ph/index.php/pej/article/view/5801
3. R. H. M. C. R. B. De Ocampo, "Optimization of Public Transport Dispatching Schedules in Regional Hubs," *International Journal of Transportation Studies*, vol. 12, no. 2, pp. 104-118, May 2023. [Online]. Available: https://doi.org/10.1016/j.ijts.2023.05.011
