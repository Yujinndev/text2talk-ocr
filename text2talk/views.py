import os
import pytesseract
from text2talk import forms, models
from django.conf import settings
from django.shortcuts import render, redirect
from PIL import Image
from gtts import gTTS

uploaded_image_name = "text2talk\static\images\placeholder-image.png"

def index(request): 
	return render(request, "index.html", {})

def perform_ocr_helper(image_name):
    static_dir = settings.STATICFILES_DIRS[0]
    image_path = os.path.join(static_dir, image_name)

    image = Image.open(image_path)
    # conversion using the pytesseract lib
    ocr_result = pytesseract.image_to_string(image, lang='eng')
    return ocr_result

def image_to_text(request):
    result = perform_ocr_helper(uploaded_image_name)

    return render(request, 'textOcr.html', {'text_result': result, 'image': uploaded_image_name})

def text_to_speech(request):
    static_dir = settings.STATICFILES_DIRS[2]
    result = perform_ocr_helper(uploaded_image_name)

    # conversion from the text to audio
    tts = gTTS(text=result, lang='en')
    os.makedirs(static_dir, exist_ok=True)
    output_path = os.path.join(static_dir, 'tts.mp3')
    tts.save(output_path)

    return render(request, 'talkOcr.html', {'image': uploaded_image_name})
