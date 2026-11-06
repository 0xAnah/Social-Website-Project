from django.core.files.base import ContentFile
from django.utils.text import slugify
from .models import Image
from django import forms
import requests

class ImageCreateForm(forms.ModelForm):
    class meta:
        model = Image
        fields =['title', 'url', 'description']
        widget = {
            'url': forms.HiddenInput,
        }

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        # download image from the given URL
        response = requests.get(image_url)
        image.image.save(image_name, ContentFile(response.content), save=False)
        
        if commit:
            image.save()
        return image