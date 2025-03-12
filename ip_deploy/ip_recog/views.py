from django.shortcuts import render, redirect,HttpResponse
from django.core.files.storage import FileSystemStorage
from ultralytics import YOLO
from . deploy_models.data.description_of_pests import description_of_class
from .deploy_models.data.model_evaluation import metrices
from .models import About_model

#yolo model
from ultralytics import YOLO
import json

def yolo_give_name(path):
    # Load the trained YOLO classification model
    model = YOLO('ip_recog/deploy_models/models/best.pt')

    # Specify the path to the image
    image_path = path

    # Predict the class of the image
    results = model.predict(image_path)
    
    json_file_path = 'ip_recog/deploy_models/data/ip102_class_labels.json'
    # Load the class names from the JSON file
    with open(json_file_path, 'r') as f:
        class_names = json.load(f)

    # Extract the top class and its confidence
    for r in results:
        # Get the index of the class with the highest probability
        class_index = r.probs.top1
        # Load the class names from the JSON file
        class_name = class_names[str(class_index)]
        # Get the confidence score for the top predicted class
        confidence = r.probs.top1conf.item()  # Convert tensor to a Python float

        # Output the result
        print(f"Predicted Class: {class_name}, Confidence: {confidence:.2f}")
        return class_index , class_name


## resnet starts here
import torch
from torchvision import models, transforms
from PIL import Image
import json

def resnet_50_givename(image_path ):
# Set device (CPU since no CUDA is available)
    device = torch.device('cpu')

    # Number of classes in IP102
    num_classes = 102

    # Load the ResNet50 model architecture
    model = models.resnet50()

    # Modify the final fully connected layer to match IP102 classes
    model.fc = torch.nn.Linear(model.fc.in_features, num_classes)

    # Load the model weights from the .pkl file, mapping them to CPU
    model_path = 'ip_recog/deploy_models/models/resnet50_0.497.pkl'
    model.load_state_dict(torch.load(model_path, weights_only= True, map_location=torch.device('cpu')))

    # Move the model to the CPU
    model = model.to(device)

    # Set the model in evaluation mode
    model.eval()

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

    with open('ip_recog/deploy_models/data/ip102_class_labels.json', 'r') as f:
        class_labels = json.load(f)

    #return class name
    class_name = class_labels[str(predicted_class)]
    predicted_class_number = int(predicted_class)
    return predicted_class_number,class_name
## resnet ends here
    
def home(request):
    return render(request, 'ip_recog/home.html')
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        
        selected_model = request.POST.get('select_model')
        
        return redirect('show_image', filename=filename, selected_model=selected_model)
    return render(request, 'ip_recog/upload.html')

def show_image(request, filename, selected_model):
    fs = FileSystemStorage()
    file_url = fs.url(filename)
    
    image_path = fs.path(filename) 
    if selected_model == 'Yolov8n':
       predicted_class_number,predicted_class_name = yolo_give_name(image_path)
    elif selected_model == 'Resnet50':
       predicted_class_number , predicted_class_name = resnet_50_givename(image_path)
    
            
  
    return render(request, 'ip_recog/show_image.html', {
        'file_url': file_url,
        'class_name': predicted_class_name,
        'description': description_of_class[predicted_class_number],
        'model_selected':selected_model,
    })

def about_model(request,selected_model ):
        my_model = None
        models_list = About_model.objects.all()
        for model in models_list:
            if model.name == selected_model:
             my_model = model
        # return HttpResponse(f"{selected_model} {img_url}")
        return render(request, 'ip_recog/about_model.html', {
        'model_selected':selected_model,
        'metrices': metrices[selected_model],
        'my_model':my_model
    })
      


