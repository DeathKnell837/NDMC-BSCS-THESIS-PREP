# Thesis Summary for Daniela 📋

**Group Members:** Rogie P. Bacanto & Daniela S. Ungab
**Subject:** CS Thesis Writing 1 (BSCS-4, NDMC)
**Adviser:** Ms. Rezzie R. Cadungog

---

## ⏰ Our Timeline

| Week | Dates | What We Do |
|---|---|---|
| **Week 1** | June 22-28 (NOW) | Research & Topic Selection |
| **Week 2** | June 29 - July 5 | Research & Topic Selection |
| **Week 3** | July 6-12 | Research & Topic Selection |
| **Week 4** | **July 13-19** | **🚨 TITLE DEFENSE (defend 3 titles to panelists)** |

---

## What We Need: 3 Thesis Titles

We must present **3 thesis titles** at the Week 4 title defense. The panel picks the best one. All 3 use the same core technology: **AI / Computer Vision / Deep Learning (CNN)**.

| Slot | Topic | Status |
|---|---|---|
| **Title 1** | 🏚️ Post-Earthquake Structural Damage Assessment | ✅ Decided by Rogie |
| **Title 2** | 🔍 Deepfake Detection | ✅ Decided by Rogie |
| **Title 3** | ❓ **Daniela's pick** | ❓ Waiting for Daniela |

### Options for Title 3 (Daniela picks one):
- 🍫 Cacao Bean Quality Grading (agriculture, Cotabato-specific)
- 🤟 Filipino Sign Language Recognition (accessibility)
- 🔥 Smoke/Fire Detection from CCTV (disaster/safety)
- 🐟 Fish Freshness Detection (local markets)
- Or suggest your own idea!

---

## Title 1: 🏚️ Post-Earthquake Structural Damage Assessment System

### The Problem
After an earthquake (like the one this year), inspecting buildings for damage is slow and manual. There aren't enough structural engineers to check every building quickly.

### What It Does
An AI-powered web app where an inspector photographs a building's walls, columns, ceiling, and foundation. The AI analyzes each photo and gives an overall safety assessment.

### Full Feature List
| # | Feature | Description |
|---|---|---|
| 1 | Crack/damage detection | AI detects cracks, spalling, exposed rebar |
| 2 | Crack type classification | Hairline, linear, branching, alligator pattern |
| 3 | Severity scoring | Rates damage 1-10 |
| 4 | Risk level | 🟢 SAFE → 🟡 CAUTION → 🟠 DANGER → 🔴 EVACUATE |
| 5 | Heat map overlay | Highlights where damage is in the photo |
| 6 | Multi-photo inspection | Take 4-12 photos per building (walls, columns, ceiling, floor) |
| 7 | Overall building score | Combines all photos into one assessment |
| 8 | Damage map (blueprint-style) | Visual map showing where damage is in the building |
| 9 | PDF report | Auto-generated damage report for LGU/DPWH |
| 10 | GPS-tagged map dashboard | See all inspected buildings on a map, color-coded by risk |
| 11 | Priority ranking | Rank which buildings need repair first |
| 12 | Before vs After comparison | Compare old vs post-earthquake photos |
| 13 | Inspection history | Track damage over time |
| 14 | Multi-user access | Multiple inspectors can use it |
| 15 | Offline mode | Works without internet after disaster |
| 16 | Building shape templates | Pick building layout for the damage map |

### Possible Title
> *"A Deep Learning-Based Post-Earthquake Structural Damage Assessment System Using Convolutional Neural Networks with Transfer Learning"*

### Research Agenda: Agenda 1 (Emerging Technologies) | SDG 9 & SDG 11

---

## Title 2: 🔍 Deepfake Detection System

### The Problem
AI-generated fake images and videos are everywhere (Midjourney, DALL-E, face swaps). People get scammed, misinformation spreads, and nobody can tell what's real anymore.

### What It Does
A web app where you upload a photo or video, and the AI tells you if it's real or fake, with a confidence score and a heat map showing which part was manipulated.

### Full Feature List
| # | Feature | Description |
|---|---|---|
| 1 | Real vs Fake image detection | Is this photo real or AI-generated? |
| 2 | Face swap detection | Detect if someone's face was swapped |
| 3 | AI-generated image detection | Catch Midjourney, DALL-E, Stable Diffusion images |
| 4 | AI-generated text detection | Check if text was written by ChatGPT |
| 5 | Manipulation heat map | Shows WHERE the image was faked |
| 6 | Confidence score | "94.7% likely fake" |
| 7 | Video analysis | Frame-by-frame deepfake detection |
| 8 | Single image upload | Upload one image → get result |
| 9 | Batch upload | Upload multiple images at once |
| 10 | URL paste check | Paste image URL → auto-check |
| 11 | Side-by-side comparison | Show original vs manipulated areas |
| 12 | Detection report | Explains why AI flagged it as fake |
| 13 | History log | Record of all checked images |
| 14 | Dashboard | Stats: checked, fake, real |
| 15 | Share result | Share analysis as a link |

### Possible Title
> *"A Convolutional Neural Network Approach for Real-Time Detection and Classification of Deepfake Images and AI-Generated Media"*

### Research Agenda: Agenda 1 (Emerging Tech) + Agenda 4 (Cybersecurity) | SDG 16

---

## Tech Stack (Same for All 3 Titles)

| Component | Technology | Cost |
|---|---|---|
| AI Model | Python + TensorFlow/Keras (CNN with Transfer Learning) | FREE |
| Model Training | Google Colab (free GPU in browser) | FREE |
| Web App | Next.js or React | FREE |
| Hosting | Vercel (test via phone browser) | FREE |
| Native App (later) | React Native or Flutter + TensorFlow Lite | FREE |
| Datasets | Kaggle / public datasets | FREE |

**Total cost: ₱0**

---

## How the Work is Split

| Who | What They Do |
|---|---|
| **AI Assistant** | Writes all code, builds the AI model, writes thesis chapters, finds verified references |
| **Rogie & Daniela** | Run the training on Google Colab (click "Run"), understand the code for defense, collect local photos if needed, present at defense |

---

## What Daniela Needs to Do

1. ✅ **Pick Title 3** from the options above (or suggest her own idea)
2. ✅ **Confirm** she's okay with Title 1 (Earthquake Damage) and Title 2 (Deepfake Detection)
3. ✅ Tell Rogie so we can start preparing all 3 titles for the Week 4 defense
