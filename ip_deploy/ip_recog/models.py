from django.db import models

# Create your models here.

class About_model(models.Model):
    
    name = models.CharField(max_length = 20,null = True)
    image_1 = models.ImageField(upload_to="model_evaluate_img/",null = True)
    image_2 = models.ImageField(upload_to="model_evaluate_img/",null = True)
    image_3 = models.ImageField(upload_to="model_evaluate_img/",null = True)