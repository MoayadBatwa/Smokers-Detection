

from ultralytics import YOLO
import cv2

# Load a model
model = YOLO('YOLOv11n.torchscript')  # load a pretrained model


# Use the model
# Upload your image here
results = model('images/6.jpg', show=True)  # show an image


cv2.waitKey(0)