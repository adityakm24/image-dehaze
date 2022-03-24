from django import forms
from numpy import imag
from .models import Image

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('image',)