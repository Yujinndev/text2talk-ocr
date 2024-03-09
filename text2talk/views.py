from django.shortcuts import render
from django.conf import settings
from PIL import Image
import pytesseract
import os

def index(request): 
	return render(request, "index.html", {})

def ocr(request):
    static_dir = settings.STATICFILES_DIRS[0]
    image_path = os.path.join(static_dir, 'images\hardwork.jpg')
    
    image = Image.open(image_path)

    # conversion using the pytesseract lib
    text_result = pytesseract.image_to_string(image, lang='eng')

    return render(request, 'ocr.html', {'text_result': text_result})
