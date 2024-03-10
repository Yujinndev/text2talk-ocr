# forms.py
from django import forms
from text2talk import models

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = models.UploadedImage
        fields = ['image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Check if the file is an image
            allowed_types = ['image/jpeg', 'image/png', 'image/gif']
            if image.content_type not in allowed_types:
                raise forms.ValidationError('File type is not supported. Please upload a valid image.')
        return image
