from .models import Image
from django import forms

class ImageCreateForm(forms.ModelForm):
    class meta:
        model = Image
        fields =['title', 'url', 'description']
        widget = {
            'url': forms.HiddenInput,
        }