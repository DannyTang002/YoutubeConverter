from django import forms
from .import models

class CreateVideo(forms.ModelForm):
    class Meta:
        model = models.Video
        fields = ['title','field_name']