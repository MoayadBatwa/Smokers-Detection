
## ⚠️ Note: Test Media Not Included

This repository **includes** the trained `YOLOv11n.torchscript` model file.

However, it **does not include** the test images or videos used for development. To run the `mainImage.py` and `mainVideo.py` scripts, you will need to provide your own media files as described in the "Usage" section.


# 🚭 Smokers Detection System

A real-time smoking detection system using YOLOv11 deep learning model. This project automatically detects the presence of smokers, cigarettes, vape devices, and visible smoke in images or video streams. Designed for application in restricted or anti-smoking areas such as hospitals, shopping malls, and public transportation hubs.

## 👥 Authors
**Moayad Batwa**

## 📋 Table of Contents
- [Problem Definition](#-problem-definition)
- [Dataset](#-dataset)
- [Model Architecture](#-model-architecture)
- [Features](#-features)
- [Performance Results](#-performance-results)
- [Installation](#%EF%B8%8F-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)

## 🎯 Problem Definition

### Background
Object detection is a fundamental task in computer vision that involves identifying and locating instances of specific objects within an image or video frame. Unlike image classification, which assigns a single label to an entire image, object detection provides both the class label and the spatial location of each detected object, typically represented by bounding boxes.

### Problem Statement
This project develops a machine learning model capable of automatically detecting the presence of smokers, cigarettes, vape devices, and visible smoke in images or video streams for automated monitoring in anti-smoking zones.

### Project Objectives
- ✅ Collect and prepare a suitable dataset for training
- ✅ Explore and compare different object detection architectures (Faster R-CNN, SSD, YOLOv11)
- ✅ Implement and train the most appropriate model
- ✅ Evaluate model performance using standard metrics (mAP)
- ✅ Document the entire machine learning process

## 📊 Dataset

### Data Source
Primary dataset sourced from **Roboflow Universe** platform - "Smoking Person Detection v2"

### Dataset Statistics
- **Total Images**: 1,654
- **Training Set**: 1,446 images
- **Validation Set**: 156 images
- **Test Set**: 52 images

### Classes (4)
- 🚬 **Cigarette**
- 👤 **Person**
- 💨 **Vape**
- ☁️ **Smoke**

### Data Characteristics
- **Format**: JPG files
- **Resolutions**: Multi-resolution (HD, 4K, low-res)
- **Color Space**: Primarily RGB
- **Annotation Format**: YOLO format (.txt files)
- **Annotations**: Normalized bounding boxes (x_center, y_center, width, height)

### Data Preprocessing
- **Resizing**: 640×640 pixels
- **Normalization**: Pixel values scaled to [0, 1]
- **Augmentation**: Horizontal flipping and rotation
- **Quality Checks**: Duplicate removal and annotation validation

## 🧠 Model Architecture

### Model Selection Process
We evaluated three prominent architectures:

| Feature | Faster R-CNN | SSD | **YOLOv11** ✓ |
|---------|--------------|-----|---------------|
| Type | Two-Stage | Single-Stage (Classic) | **Single-Stage (Modern)** |
| Speed | Significantly Slower | Fast | **Very Fast** |
| Accuracy | Very Strong | Moderate | **Very High** |
| Small Objects | Very Strong | Weak/Moderate | **Good/Very Good** |
| Complexity | Most Complex | Moderate | **Relatively Simple** |
| Training | Slowest | Moderate | **Fast & Stable** |
| GPU Resources | Highest | Moderate | **Low/Moderate** |

### Why YOLOv11?
**YOLOv11n (Nano)** was selected for:
- ⚡ **Best balance** of speed and accuracy
- 🎯 **Real-time capability** for live monitoring applications
- 🛠️ **Ultralytics framework** - streamlined pipeline and excellent documentation
- 📈 **Scalability** - multiple model sizes (nano, small, medium, large, x-large)
- 🔬 **Modern architecture** incorporating latest object detection advancements
- 🎨 **Strong small object performance** compared to classic single-stage detectors

## 🎯 Features

- **Multi-class Detection**: Detects 4 classes simultaneously
  - 🚬 Cigarette
  - 👤 Person
  - 💨 Vape
  - ☁️ Smoke

- **Multiple Input Sources**:
  - Static images
  - Video files
  - Real-time webcam feed

- **Real-time Performance**:
  - FPS counter
  - Confidence scores for each detection
  - Visual bounding boxes with corner rectangles

- **Functionality:** Includes Python scripts to perform detection on:
   - Single images (`mainImage.py`)
   - Pre-recorded video files (`mainVideo.py`)
   - Live webcam feeds (`mainWebCam.py`)


## � Performance Results

### Training Configuration
- **Model**: YOLOv11n (Nano variant)
- **Input Size**: 640×640 pixels
- **Epochs**: 20
- **Framework**: Ultralytics
- **Pre-training**: COCO dataset weights
- **Development Environment**: Google Colab

### Overall Model Metrics
- **mAP@0.5**: 0.659 (65.9%)
- **mAP@0.5:0.95**: 0.404 (40.4%)
- **Box Loss**: 0.91488
- **Classification Loss**: 0.75898

### Per-Class Performance (AP@0.5)

| Class | Average Precision | Performance |
|-------|-------------------|-------------|
| 👤 **Person** | **0.975** (97.5%) | ⭐ Excellent |
| 🚬 **Cigarette** | **0.761** (76.1%) | ✅ Good |
| 💨 **Vape** | 0.524 (52.4%) | ⚠️ Moderate |
| ☁️ **Smoke** | 0.376 (37.6%) | ⚠️ Needs Improvement |

### Confusion Matrix Analysis
- **Person**: 96% correctly identified
- **Cigarette**: 82% correctly identified, 18% missed
- **Vape**: 33% correctly identified, 17% misclassified as Cigarette, 50% missed
- **Smoke**: 32% correctly identified, 68% missed

### Key Findings
✅ **Strengths**:
- Excellent detection of people (97.5% AP)
- Good cigarette detection (76.1% AP)
- Fast inference suitable for real-time applications
- Robust to various lighting conditions and angles

⚠️ **Limitations**:
- Challenging detection of smoke (37.6% AP) due to its amorphous nature
- Moderate vape detection (52.4% AP) - visual similarity to other objects
- Small object detection accuracy needs improvement
- Some false positives in complex scenes

## �📋 Requirements

### Python Version
- Python 3.8 or higher

### Dependencies
```
ultralytics>=8.3.0
opencv-python>=4.12.0
cvzone>=1.6.1
torch>=2.0.0
numpy>=1.23.0
```

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/MoayadBatwa/Smokers-Detection.git
cd Smokers-Detection
```

2. **Install required packages**
```bash
pip install ultralytics opencv-python cvzone
```

3. **Download the trained model**

The YOLOv11 model file is not included in the repository due to size constraints. You have two options:

**Option A**: Use pre-trained weights (the scripts will download automatically on first run)

**Option B**: Train your own model using the Ultralytics library:
```bash
# The model will be saved after training
yolo train data=your_dataset.yaml model=yolov11n.pt epochs=20 imgsz=640
```

## 🚀 Usage

### 1. Image Detection
Process a single image and display detection results:
```bash
python mainImage.py
```
- Place your test images in the `images/` folder
- Modify the image path in `mainImage.py` (default: `images/6.jpg`)

### 2. Video Detection
Process a video file with real-time detection:
```bash
python mainVideo.py
```
- Place your video files in the `video/` folder
- Modify the video path in `mainVideo.py` (default: `video/1.mp4`)
- Press any key to exit

### 3. Webcam Detection
Real-time detection using your webcam:
```bash
python mainWebCam.py
```
- Requires a connected webcam (default: camera index 0)
- Press any key to exit

## 📁 Project Structure

```
Smokers-Detection/
│
├── mainImage.py           # Image detection script
├── mainVideo.py           # Video detection script
├── mainWebCam.py          # Webcam detection script
├── YOLOv11n.torchscript   # Pre-trained YOLO model
├── images/                # Input images folder
├── video/                 # Input videos folder
└── README.md              # Project documentation
```

## 🧠 Model Information

- **Model**: YOLOv11 Nano (TorchScript format)
- **Framework**: Ultralytics YOLO
- **Format**: `.torchscript` (optimized for inference)
- **Classes**: 4 (Cigarette, Person, Vape, Smoke)

## 🎨 Features Breakdown

### Detection Visualization
- **Corner rectangles** around detected objects (using cvzone)
- **Confidence scores** displayed above each detection
- **Class labels** for each detected object
- **FPS counter** for performance monitoring

### Performance Optimization
- Stream mode for video processing
- Efficient bounding box rendering
- Real-time FPS calculation

## 📊 Output

The system provides:
- Visual bounding boxes with corner rectangles
- Class name and confidence score for each detection
- Real-time FPS in console output
- Live display window showing processed frames

## 🔧 Customization

### Modify Detection Classes
Edit the `classNames` list in the scripts:
```python
classNames = ["Cigarette", "Person", "Vape", "Smoke"]
```

### Change Input Source
- **For images**: Modify the path in `mainImage.py`
- **For videos**: Change the video path in `mainVideo.py`
- **For webcam**: Adjust camera index in `mainWebCam.py` (default: 0)

### Adjust Display Settings
Modify the cvzone parameters for customized visualization:
```python
cvzone.cornerRect(img, (x1, y1, w, h))
cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (x, y), scale=1, thickness=1)
```

## ⚙️ System Requirements

- **OS**: Windows, macOS, or Linux
- **RAM**: 4GB minimum (8GB recommended)
- **GPU**: Optional (CUDA-compatible GPU for faster processing)
- **Webcam**: Required for real-time detection

## � Challenges and Solutions

### Challenges Encountered

1. **Small Object Detection**
   - Cigarettes and vapes can be very small in images
   - **Solution**: Used modern YOLOv11 architecture optimized for multi-scale detection

2. **Class Imbalance**
   - Fewer instances of 'vape' and 'smoke' compared to 'person'
   - **Solution**: Applied data augmentation techniques

3. **Visual Similarity**
   - Vape devices come in many shapes/sizes
   - Smoke plumes are amorphous and difficult to bound
   - **Solution**: Extensive training with diverse dataset

4. **Varying Conditions**
   - Different lighting, angles, occlusions, and image quality
   - **Solution**: Multi-resolution training and augmentation (flip, rotation)

5. **Annotation Consistency**
   - Ensuring high quality across manually annotated data
   - **Solution**: Quality checks and duplicate removal

## 🔮 Future Enhancements

### Short-term Improvements
1. **Extended Training**
   - Train for more epochs to improve convergence
   - Implement early stopping based on validation performance

2. **Enhanced Dataset**
   - Add more diverse images, especially for 'Smoke' and 'Vape' classes
   - Include various lighting conditions and camera angles
   - Balance class distribution

3. **Hyperparameter Tuning**
   - Optimize learning rate and batch size
   - Fine-tune confidence thresholds for each class
   - Reduce false positive rate

### Long-term Goals
4. **Real-World Deployment**
   - Test with live camera feeds in actual environments
   - Optimize for edge devices (Raspberry Pi, NVIDIA Jetson)
   - Implement alert system for detected violations

5. **Model Improvements**
   - Experiment with YOLOv11 larger variants (small, medium)
   - Try ensemble methods for better accuracy
   - Implement temporal tracking for video analysis

6. **Extended Functionality**
   - Add person tracking across frames
   - Integrate with existing security systems
   - Generate automated reports and statistics

## �🐛 Troubleshooting

### Common Issues

1. **Import errors**
   ```bash
   pip install --upgrade ultralytics opencv-python cvzone
   ```

2. **Webcam not detected**
   - Try changing camera index: `cap = cv2.VideoCapture(1)`
   - Check webcam permissions

3. **Model not found**
   - Ensure `YOLOv11n.torchscript` is in the project root directory

4. **Low FPS**
   - Reduce input resolution
   - Use GPU acceleration if available
   - Close other resource-intensive applications

## � Methodology

### Development Process
1. **Data Collection** - Sourced from Roboflow Universe
2. **Data Preprocessing** - Resizing, normalization, augmentation
3. **Model Selection** - Compared Faster R-CNN, SSD, and YOLOv11
4. **Implementation** - Used Ultralytics framework
5. **Training** - 20 epochs with validation monitoring
6. **Evaluation** - Comprehensive metrics analysis (mAP, precision, recall)
7. **Testing** - Real-world performance validation

### Evaluation Metrics
- **mAP (mean Average Precision)**: Primary metric for overall performance
  - mAP@0.5: IoU threshold of 0.5
  - mAP@0.5:0.95: Stricter evaluation across multiple IoU thresholds
- **Precision & Recall**: Per-class performance analysis
- **Confusion Matrix**: Misclassification analysis
- **Loss Functions**: Box localization (box_loss) and classification (cls_loss)

## 🎓 Conclusion

This project successfully developed an automated smoking detection system using YOLOv11, demonstrating:
- **High accuracy** for person detection (97.5% AP)
- **Good performance** for cigarette detection (76.1% AP)
- **Real-time capability** suitable for monitoring applications
- **Practical applicability** in anti-smoking enforcement zones

The system shows promising results for deployment in hospitals, shopping malls, and public transportation hubs, with identified areas for future improvement particularly in smoke and vape detection.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for any improvements. Contributions are welcome in:
- Dataset expansion
- Model optimization
- Performance improvements
- Documentation enhancements

## 📧 Contact

For questions or feedback:
- **Moayad Batwa** - [GitHub](https://github.com/MoayadBatwa)

## 🙏 Acknowledgments

- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) for the YOLOv11 detection framework
- [Roboflow](https://roboflow.com/) for dataset hosting and management
- [cvzone](https://github.com/cvzone/cvzone) for computer vision utilities


## 📚 References

- **YOLOv11**: [Ultralytics Documentation](https://docs.ultralytics.com/)
- **Dataset**: [Roboflow Universe - Smoking Person Detection v2](https://universe.roboflow.com/)
- **Object Detection**: Modern computer vision techniques and deep learning approaches

---

⭐ **If you find this project helpful, please consider giving it a star!**
