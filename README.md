# 🚬 Smokers Detection using YOLOv11

The project's goal is to develop a machine learning model capable of automatically detecting smokers, cigarettes, vape devices, and visible smoke in images and video streams. The primary application is for automated monitoring in restricted non-smoking areas such as hospitals, shopping malls, and public transportation hubs.

## 📋 Features

* **Model:** Powered by the **YOLOv11n** (nano) model (`YOLOv11n.torchscript`), which is included in this repository via Git LFS.
* **Detections:** Identifies 4 distinct classes: `Cigarette`, `Person`, `Vape`, and `Smoke`.
* **Functionality:** Includes Python scripts to perform detection on:
    * Single images (`mainImage.py`)
    * Pre-recorded video files (`mainVideo.py`)
    * Live webcam feeds (`mainWebCam.py`)

---

## ⚠️ Note: Test Media Not Included

This repository **includes** the trained `YOLOv11n.torchscript` model file.

However, it **does not include** the test images or videos used for development. To run the `mainImage.py` and `mainVideo.py` scripts, you will need to provide your own media files as described in the "Usage" section.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MoayadBatwa/Smokers-Detection.git
cd Smokers-Detection
