from django import forms
from .models import Dron

class DronForm(forms.ModelForm):
    class Meta:
        model=Dron
        fields='__all__'