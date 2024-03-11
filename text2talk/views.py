import json
import os
import pytesseract
import base64
from text2talk import forms, models
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from PIL import Image
from gtts import gTTS

current_image = "text2talk\static\images\placeholder-image.png"

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
    result = perform_ocr_helper(current_image)

    return render(request, 'textOcr.html', {'text_result': result, 'image': current_image})

def text_to_speech(request):
    static_dir = settings.STATICFILES_DIRS[2]
    result = perform_ocr_helper(current_image)

    # conversion from the text to audio
    tts = gTTS(text=result, lang='en')
    os.makedirs(static_dir, exist_ok=True)
    output_path = os.path.join(static_dir, 'tts.mp3')
    tts.save(output_path)

    return render(request, 'talkOcr.html', {'image': current_image})

def file_upload(request):
    if request.method == 'POST':
        form = forms.ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            
            global current_image
            current_image = uploaded_image.image.name

            return redirect('textOcr')

    else:
        form = forms.ImageUploadForm()
    return render(request, 'file_upload.html', {'form': form})

def live_cam(request):
    return render(request, 'live_camera.html')

@csrf_exempt
def handle_video(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        image_data = data.get('image_data', '')

        # Decode base64 image data
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        image_data = ContentFile(base64.b64decode(imgstr), name=f'captured_image.{ext}')

        # Save the image to a specific folder
        static_dir = settings.STATICFILES_DIRS[1]
        save_path = os.path.join(static_dir, f'captured_image.{ext}')

        global current_image
        current_image = save_path
        print(current_image)

        with open(save_path, 'wb') as f:
            f.write(image_data.read())

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def text_input(request):
    if request.method == 'POST':
        form = forms.TextInputForm(request.POST)
        if form.is_valid():
            result = form.save()

            static_dir = settings.STATICFILES_DIRS[2]
            # conversion from the text to audio
            tts = gTTS(text=result.text, lang='en')
            os.makedirs(static_dir, exist_ok=True)
            output_path = os.path.join(static_dir, 'output.mp3')
            tts.save(output_path)

            return redirect('input')

    else:
        form = forms.TextInputForm()
    return render(request, 'text_input.html', {'form': form})