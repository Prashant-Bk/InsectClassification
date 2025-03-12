import torch
from torchvision import models, transforms
from PIL import Image
import json

def resnet50_givename(image_path ):
    """_summary_

    Args:
        image_path (string): path of image

    Returns:
        string: name of the class of given image
    """
# Set device (CPU since no CUDA is available)
    device = torch.device('cpu')

    # Number of classes in IP102
    num_classes = 102

    # Load the ResNet50 model architecture
    model = models.resnet50()

    # Modify the final fully connected layer to match IP102 classes
    model.fc = torch.nn.Linear(model.fc.in_features, num_classes)

    # Load the model weights from the .pkl file, mapping them to CPU
    # model_path = '../models/resnet50_0.497.pkl' #relative path
    model_path = "C:/Users/AB/Desktop/Django/ip_deploy/ip_recog/deploy_models/code_files/resnet50.py"
    #####
    for i in range(5):
     print("Model path loaded")
    
    
    model.load_state_dict(torch.load(model_path,weights_only= True, map_location=torch.device('cpu')))

    # Move the model to the CPU
    model = model.to(device)

    # Set the model in evaluation mode
    model.eval()
    
     #####
    for i in range(5):
     print("Model loaded")

    # Define the transformation for the input image (ResNet50 requires 224x224 images)
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    # Function to predict the class of a single image
    def predict_image(image_path, model):
        # Load the image
        image = Image.open(image_path).convert('RGB')
        
        # Apply transformations
        image = transform(image).unsqueeze(0)  # Add batch dimension
        
        # Move the image to the device (CPU in this case)
        image = image.to(device)
        
        # Make prediction
        with torch.no_grad():
            output = model(image)
            _, predicted_class = torch.max(output, 1)
        
        # Return the predicted class index
        return predicted_class.item()

    # Predict the class of the image
    predicted_class = predict_image(image_path, model)

    with open("C:/Users/AB/Desktop/Django/ip_deploy/ip_recog/deploy_models/data/ip102_class_labels.json", 'r') as f:
        class_labels = json.load(f)

    # Print the predicted class label
    print(f'Predicted class: {class_labels[str(predicted_class)]}')
    class_name = class_labels[str(predicted_class)]
    return class_name
