from . models import *
from django import forms

class MymodelForm(forms.ModelForm):
    class Meta:
        model = Mymodel
        fields = ['name', 'description']
        