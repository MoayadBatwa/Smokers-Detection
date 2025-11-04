# 🚬 Smokers Detection using YOLOv11

[cite_start]This repository contains the source code for the **"Smokers Detection"** project, completed for the CPCS331 course at King Abdulaziz University[cite: 2, 5].

[cite_start]The project's goal is to develop a machine learning model capable of automatically detecting smokers, cigarettes, vape devices, and visible smoke in images and video streams[cite: 19]. [cite_start]The primary application is for automated monitoring in restricted non-smoking areas such as hospitals, shopping malls, and public transportation hubs[cite: 20].

## 📋 Features

* [cite_start]**Model:** Powered by the **YOLOv11n** (nano) model, chosen for its excellent balance of speed and accuracy[cite: 106, 115].
* [cite_start]**Detections:** Identifies 4 distinct classes: `Cigarette`, `Person`, `Vape`, and `Smoke`[cite: 45].
* **Functionality:** Includes Python scripts to perform detection on:
    * Single images (`mainImage.py`)
    * Pre-recorded video files (`mainVideo.py`)
    * Live webcam feeds (`mainWebCam.py`)

---

## ‼️ Important: Missing Files

As noted, this repository **does not include** the trained model weights, test images, or test videos.

To run the scripts, you will need to provide your own:

1.  **Model Weights:** The code expects a trained model file named `YOLOv11n.torchscript` in the root directory. You must obtain or train your own model and place it here.
2.  **Test Files:**
    * `mainImage.py` requires an image. You must create an `images/` directory, add your own image (e.g., `images/my_image.jpg`), and update the path on line 9 of the script.
    * `mainVideo.py` requires a video. You must create a `video/` directory, add your own video (e.g., `video/my_video.mp4`), and update the path on line 8 of the script.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone [URL_OF_YOUR_REPO]
cd [REPO_NAME]
