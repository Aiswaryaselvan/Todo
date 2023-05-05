from .models import Mytask
from django import forms


class Todoform(forms.ModelForm):
    class Meta:
        model = Mytask
        fields = ['taskname', 'priority', 'date']