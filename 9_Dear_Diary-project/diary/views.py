from .models import DiaryContent
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView

class IndexView(ListView):
  model=DiaryContent
  template_name = 'home.html'
  context_object_name='diary_content'
  queryset = DiaryContent.objects.order_by('-date')
  
class CreateView(CreateView):
  model=DiaryContent
  template_name = 'create.html'
  fields = ['content']
  context_object_name='form'
  success_url = '/'
