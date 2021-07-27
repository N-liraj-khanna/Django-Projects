from django.forms import ModelForm
from .models import ToDo 

class CreateForm(ModelForm):
  class Meta:
    model = ToDo
    fields = ['task']