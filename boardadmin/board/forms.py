from django.forms import ModelForm
from django.forms import forms
from .models import *

class AddAdvForm(ModelForm):
    class Meta:
        model = Board
        fields = {"name","descrip", "position", "photo", "price"}