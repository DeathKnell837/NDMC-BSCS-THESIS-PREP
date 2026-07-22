# 🔒 ForgeGuard

**CNN-Based Digital Receipt Forgery Detection System**

> BSCS Thesis: *"Securing Mobile Transaction: A Comparative Evaluation of CNN Architectures in Detecting Digital Receipt Forgery"*

---

## 📖 About

ForgeGuard is an AI-powered system that detects forged mobile wallet transaction receipts (GCash, Maya) using Convolutional Neural Networks. It comparatively evaluates **Basic CNN**, **ResNet50**, and **MobileNetV2** architectures to determine the most effective model for receipt forgery detection.

## 👥 Team

* **Rogie P. Bacanto** (BSCS-4)
* **Daniela S. Ungab** (BSCS-4)
* **Adviser:** Ms. Doris Ann Mariano
* **School:** Notre Dame of Midsayap College (NDMC), CITE

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.10+ |
| Deep Learning | TensorFlow / Keras |
| Image Processing | OpenCV, Pillow |
| Preprocessing | Error Level Analysis (ELA) |
| ML Utilities | scikit-learn, SciPy |
| Training | Google Colab (free GPU) |
| Web Demo | Streamlit |
| Statistical Testing | ANOVA / Kruskal-Wallis |

## 🏗️ Project Structure

```
ForgeGuard/
├── dataset/                # Dataset generation & storage
│   ├── generator/          # Receipt forgery generation scripts
│   │   ├── config.py
│   │   ├── authentic_generator.py
│   │   ├── forgery_generator.py
│   │   └── batch_generate.py
│   ├── raw/                # Generated images (gitignored)
│   └── processed/          # ELA-processed images (gitignored)
├── preprocessing/          # ELA + augmentation pipeline
├── models/                 # CNN architectures
│   ├── basic_cnn.py
│   ├── resnet50.py
│   └── mobilenetv2.py
├── training/               # Training scripts
├── evaluation/             # Metrics, stats, visualization
├── explainability/         # Grad-CAM heatmaps
├── webapp/                 # Streamlit demo app
├── notebooks/              # Google Colab notebooks
└── requirements.txt
```

## 📚 Related Repository

* 📄 **Thesis Documents & Proposals:** [NDMC-BSCS-THESIS-PREP](https://github.com/DeathKnell837/NDMC-BSCS-THESIS-PREP)

## 📅 Status

🔄 **In Development** — Dataset generator phase

---

*Notre Dame of Midsayap College — College of Information Technology and Engineering (CITE)*
