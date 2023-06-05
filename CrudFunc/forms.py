
from django import forms
from .models import Studen

class StudentForm(forms.ModelForm):
    class Meta:
        model=Studen
        fields='__all__'
