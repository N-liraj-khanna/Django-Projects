from django.db import models

class Url(models.Model):
  url = models.CharField(max_length=10000)
  uuid = models.CharField(max_length=15)
  
  def __str__(self):
    return self.url