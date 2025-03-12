from ultralytics import YOLO

def yolo_give_name(path):
    # Load a YOLOv8 model trained on the COCO dataset
    model = YOLO('yolov8n.pt')

    # Test the model on an image
    results = model(path)

    # Access the predictions
    result =  results[0]
    # Get the predicted class IDs
    class_ids = result.boxes.cls.numpy()  # Get class IDs as a numpy array
    # Get the predicted class names
    class_names = model.names  # Model's class names based on COCO dataset

    # Print the class names for each predicted box
    predicted_class_name = [class_names[int(cls_id)] for cls_id in class_ids]
    return predicted_class_name[0]
name = yolo_give_name(path = "C:/Users/AB/Desktop/Django/ip_deploy/my bus.jpeg")
print(name)