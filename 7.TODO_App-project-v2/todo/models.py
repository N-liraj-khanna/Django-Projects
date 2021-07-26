from django.db import models

class Todo(models.Model):
  content = models.CharField(max_length=1000)
  date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.content