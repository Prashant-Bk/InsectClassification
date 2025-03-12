# IP102 Insect Classification

This project is an insect classification system based on the IP102 dataset. It uses a deep learning model for classifying insect pests and is deployed using Django.

## Features

- Insect classification using a trained ResNet-50 and YOLOv8 model.
- Web-based interface built with Django.
- Image upload functionality for classification.
- JSON-based label mapping for classification results.

## Dataset

The IP102 dataset consists of 102 categories of insect pests, making it one of the largest publicly available insect pest datasets. It contains images of various insect species commonly found in agriculture.

## Installation

### Prerequisites

- Python 3.x
- Django
- PyTorch
- OpenCV
- Pillow
- NumPy

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Prashant-Bk/insectclassification.git
   cd ip102-classification
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Run the Django server:
   ```bash
   python manage.py runserver
   ```
5. Access the web app at `http://127.0.0.1:8000/`

## Usage

1. Upload an image of an insect.
2. The model will classify the image into one of the 102 insect classes.
3. Results will be displayed along with the predicted label and confidence score.

## Deployment

The project is deployed using Django and can be hosted on platforms like Render, Heroku, or an AWS/Azure VM.

## Future Improvements

- Enhance model accuracy with additional training.
- Integrate real-time insect detection using a camera.
- Develop a mobile-friendly interface.

## License

- This project is licensed under the MIT License.

## Author

Developed by:

- **Django App**: Prashant B.K
- **Classification Models**: Prashant B.K, Bibek Gurung, Bishan Adhikari

This project was completed under the guidance of **Dr. Yagya Raj Pandeya and Rojina Shakya**.

For any queries, contact: prashantbk314@gmail.com
