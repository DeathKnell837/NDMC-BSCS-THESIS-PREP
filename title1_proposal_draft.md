# NOTRE DAME OF MIDSAYAP COLLEGE
## College of Information Technology and Engineering (CITE)
## Midsayap, Cotabato, Philippines
### Bachelor of Science in Computer Science

### AUTOMATED STRUCTURAL HEALTH MONITORING: CONCRETE CRACK CLASSIFICATION AND MILLIMETRIC SEVERITY PROFILING USING EXPLAINABLE TRANSFER LEARNING

### A Thesis Proposal
### Presented to the Faculty of the
### College of Information Technology and Engineering
### Notre Dame of Midsayap College

### In Partial Fulfillment
### of the Requirements for the Degree
### Bachelor of Science in Computer Science

### ROGIE P. BACANTO
### DANIELA S. UNGAB

### MS. DORIS ANN MARIANO
### Thesis Adviser

### June 2026

---

# CHAPTER 1: INTRODUCTION

### 
### 
### 
## 1.1 Background of the Study

### Global Context
Structural health monitoring (SHM) is critical for maintaining public safety, extending the lifespan of civil infrastructure, and preventing catastrophic structural failures. Globally, manual visual inspection remains the dominant method for assessing concrete structures. However, manual inspections are inherently subjective, labor-intensive, error-prone, and visually challenging when dealing with high-rise structures or hard-to-reach locations [1]. To automate this process, computer vision techniques have been introduced. Early traditional image processing methods, such as Sobel and Canny edge detection, were highly sensitive to environmental noise, surface textures, and variable lighting conditions, leading to high false-positive rates [2]. The emergence of deep learning, specifically Convolutional Neural Networks (CNNs), has revolutionized structural defect detection. Pre-trained deep models can extract low-level and high-level spatial features directly from raw pixels, achieving classification accuracy exceeding 95% under controlled environments. Furthermore, transfer learning enables model optimization even with limited localized datasets, reducing computational training overhead [3]. 

However, standard deep learning models operate as "black boxes," providing predictions without explaining the underlying decision-making process. To address this limitation, Explainable Artificial Intelligence (XAI) frameworks have emerged. Specifically, Gradient-weighted Class Activation Mapping (Grad-CAM) generates coarse localization maps highlighting the important regions in an image that the model uses to predict a class [4]. In civil engineering applications, XAI provides structural inspectors with visual proof that the neural network is targeting actual crack geometries rather than surface stains, shadows, or background noise, thereby building trust in machine decisions.

### National Context
In the Philippines, the need for rapid and automated structural safety assessment is highly urgent. Situated along the Pacific Ring of Fire and the typhoon belt, the country is exposed to frequent seismic activities and extreme weather events. Following major natural disasters, the Department of Public Works and Highways (DPWH) and municipal engineering offices face the massive challenge of inspecting thousands of public buildings, bridges, and school facilities. The limited number of licensed structural engineers nationwide results in long delays, leaving potentially compromised buildings occupied and endangering lives. 

In local research, Philippine scientists have begun integrating automated systems for infrastructure inspections. For example, Sorilla and Chua developed a two-stage convolutional neural network utilizing transfer learning on Unmanned Aerial Vehicle (UAV) feeds to automate concrete crack detection in GNSS-denied environments [5]. While such systems demonstrate high segmentation accuracy, the deployment of local, accessible, and lightweight web applications that can perform real-time millimeter-level crack width measurement remains underutilized in municipal building inspection workflows.

### Local Context
Locally, the Province of Cotabato and the Municipality of Midsayap have experienced recurring earthquakes that have caused significant visible damage to school buildings, market facilities, and residential structures. A notable series of seismic events in recent years has left communities in Pigcawayan and Midsayap anxious about the safety of local educational and public facilities, including structures within Notre Dame of Midsayap College (NDMC). Currently, local municipal offices and school maintenance departments lack access to automated structural health tools, relying entirely on visual assessments using clipboards and manual measurements. 

This local challenge provides the direct justification for this study. By developing a lightweight, computer vision-driven system deployed as a web application, local building administrators and inspectors can photograph concrete elements, receive an instant severity classification, and generate localized building safety reports.

### Research Gap
Although numerous crack detection models exist, most are limited to binary classification (crack vs. no crack) and are evaluated solely on theoretical datasets. There is a distinct lack of research focusing on: (1) converting image pixels to physical millimeter dimensions for objective severity grading without heavy laboratory equipment, (2) integrating Grad-CAM explainability to verify model decisions in real-world noisy environments, and (3) aggregating multiple image-level results into a unified building-level safety index. This study addresses these gaps by proposing a unified framework that combines CNN-based transfer learning, pixel-to-physical millimeter calibration, and rules-based building safety evaluation heuristics.

### 
### 
### 
## 1.2 Objectives of the Study

The primary purpose of this study is to develop a computer vision-driven structural health monitoring system that classifies concrete crack severity and profiles crack dimensions in millimeters using explainable transfer learning.

Specifically, the study aims to achieve the following objectives:
1. To design and train three Convolutional Neural Network (CNN) architectures (MobileNetV2, ResNet50, and VGG16) using transfer learning to classify concrete surfaces into cracked and uncracked states.
2. To integrate Gradient-weighted Class Activation Mapping (Grad-CAM) to generate visual explanation heatmaps highlighting the concrete crack features targeted by the models.
3. To implement a pixel-to-millimeter scale calibration algorithm that estimates the physical width of detected cracks using a standard reference object.
4. To develop a heuristic rules-based aggregation algorithm that combines multiple crack severity inputs to calculate a unified building-level safety index (Safe, Caution, Danger).
5. To evaluate the usability and effectiveness of the developed web-based application among civil engineers, building inspectors, and maintenance personnel using the System Usability Scale (SUS).

### 
### 
### 
## 1.3 Significance of the Study

The developed system is expected to benefit the following sectors:

*   **NDMC Administration and Facilities Office:** Provides school administrators with a rapid, low-cost tool to perform preliminary safety checks on school buildings after seismic events, ensuring the safety of students and staff.
*   **Municipal Engineering Offices (LGUs):** Empowers local government inspectors to conduct faster visual screening of public infrastructure and prioritize critical buildings for professional structural engineering audits.
*   **Structural and Civil Engineers:** Serves as a digital assistant that reduces visual fatigue during visual surveys by automating data collection, width profiling, and report generation.
*   **Future Computer Science Researchers:** Offers an open-source reference implementation of explainable computer vision models and scaling heuristics applied to structural safety monitoring.

---

# REFERENCES

[1] C. V. Dung and L. D. Anh, "Autonomous concrete crack detection using deep fully convolutional neural network," *Automation in Construction*, vol. 99, pp. 52-58, Mar. 2019. [Online]. Available: https://doi.org/10.1016/j.autcon.2018.11.028

[2] Q. Zou, Z. Zhang, Q. Li, X. Qi, Q. Wang, and S. Wang, "DeepCrack: Learning Hierarchical Convolutional Features for Crack Detection," *IEEE Transactions on Image Processing*, vol. 28, no. 3, pp. 1498-1512, Mar. 2018. [Online]. Available: https://doi.org/10.1109/TIP.2018.2878966

[3] R. A. Swarna, M. M. Hossain, M. R. Khatun, M. M. Rahman, and A. Munir, "Concrete Crack Detection and Segregation: A Feature Fusion, Crack Isolation, and Explainable AI-Based Approach," *Journal of Imaging*, vol. 10, no. 9, p. 215, Sep. 2024. [Online]. Available: https://doi.org/10.3390/jimaging10090215

[4] R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, and D. Batra, "Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization," in *2017 IEEE International Conference on Computer Vision (ICCV)*, Oct. 2017. [Online]. Available: https://doi.org/10.1109/ICCV.2017.74

[5] J. Sorilla and A. Y. Chua, "A UAV Based Concrete Crack Detection and Segmentation Using 2-Stage Convolutional Network with Transfer Learning," *HighTech and Innovation Journal*, vol. 5, no. 3, 2024. [Online]. Available: https://doi.org/10.28991/HIJ-2024-05-03-010
