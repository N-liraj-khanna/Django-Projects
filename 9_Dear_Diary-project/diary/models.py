from django.db import models
from django.urls import reverse

class DiaryContent(models.Model):
  date = models.DateTimeField(auto_now_add=True)
  content = models.TextField(max_length=100000)
  
  def __str__(self):
    return self.content
  
  def get_absolute_url(self):
    return reverse('index', kwargs={'pk': self.pk})