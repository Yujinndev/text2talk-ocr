from django.urls import path 
from text2talk import views 

urlpatterns = [
	path("", views.index),
	path("ocr", views.ocr),
]
