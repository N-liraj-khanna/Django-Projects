from django.forms import ModelForm
from .models import Weather

class Form(ModelForm):
  class Meta:
    model = Weather
    fields = ['city']
    