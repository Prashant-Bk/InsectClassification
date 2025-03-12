from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),  
    path('upload/', views.upload_image, name='upload_image'),  
    path('about_model/<str:selected_model>/', views.about_model, name='about_model'),  
    path('image/<str:filename>/<str:selected_model>/', views.show_image, name='show_image'),  # Updated pattern
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
