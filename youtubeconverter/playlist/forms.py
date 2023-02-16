from django import forms
from .import models

class CreatePlayList(forms.ModelForm):
    class Meta:
        model = models.PlayList
        fields = ['title']