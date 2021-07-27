from django.db import models
from django.forms import widgets

class ToDo(models.Model):
  task = models.CharField(max_length=5000)
  completed = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    verbose_name_plural="Todos"
    # ordering=("-created",)
    
  def __str__(self):
    return self.task
  
  