import torch
from pathlib import Path

def run_yolo(image_path):
    # Load the YOLO model
    for i in range(100):
     print("hello i am in yolo")
    # model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    # # Run inference
    # results = model(image_path)
    # # Parse results
    # classes = results.names
    # class_id = int(results.pred[0][0][5])
    # class_name = classes[class_id]
    # return class_name
