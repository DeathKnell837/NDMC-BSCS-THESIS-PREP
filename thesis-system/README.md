# 🔒 ForgeGuard — Digital Receipt Forgery Detection System

[![Live Demo](https://img.shields.io/badge/Live_Demo-forgeguard.streamlit.app-0284c7?style=for-the-badge&logo=streamlit)](https://forgeguard.streamlit.app)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13%2B-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)

**Official BSCS Thesis Project** — Notre Dame of Midsayap College (NDMC) | College of Information Technology and Engineering (CITE)  
**Authors:** Rogie P. Bacanto & Daniela S. Ungab  
**Adviser:** Ms. Doris Ann Mariano  
**Title:** *"Securing Mobile Transaction: A Comparative Evaluation of CNN Architectures in Detecting Digital Receipt Forgery"*

---

## 🌐 Live Mobile & Web Demo

Access the live cloud-deployed system on any mobile phone, tablet, or desktop browser:
👉 **[https://forgeguard.streamlit.app](https://forgeguard.streamlit.app)**

---

## 📌 Overview

ForgeGuard is an automated image forensics and deep learning detection system designed to identify digital forgery in mobile wallet receipts (GCash and Maya). 

It evaluates three Convolutional Neural Network (CNN) architectures head-to-head using **Error Level Analysis (ELA)** to highlight pixel-level compression anomalies and text manipulation artifacts.

---

## 🧠 Evaluated CNN Architectures

| Architecture | Paradigm | Parameters | Description |
|---|---|---|---|
| **Basic CNN** | Baseline (Scratch) | ~2.1 M | Custom 4-block Conv2D network trained from scratch. |
| **ResNet50** | Transfer Learning | ~23.5 M | Deep residual benchmark network. |
| **MobileNetV2** | Transfer Learning | ~3.4 M | Lightweight mobile-optimized architecture for edge deployment. |

---

## 🛠️ System Modules

* **`webapp/`**: Responsive Streamlit Web Application (`app.py`) featuring ELA Forensic Detector and interactive Live Receipt Forgery Generator.
* **`preprocessing/`**: Error Level Analysis (ELA) re-compression difference engine (`ela.py`).
* **`tools/`**: Receipt Forgery Editor & Dataset Generator (`receipt_forger.py`, `gcash_receipt_generator.py`).
* **`dataset/`**: Authentic and forged mobile wallet receipt images categorized by forgery type (amount alteration, reference number fabrication, name modification).
* **`models/`**: CNN model definitions and saved `.h5` weight files.

---

## 🚀 Quick Start (Local Run)

```bash
# 1. Clone the repository
git clone https://github.com/DeathKnell837/ForgeGuard.git
cd ForgeGuard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the web application
python -m streamlit run webapp/app.py
```

Open `http://localhost:8501` in your browser.

---

## 📄 License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
