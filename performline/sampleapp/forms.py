from django import forms
from sampleapp.models import List, Link

class ListForm(forms.ModelForm):
  class Meta:
    model = List
