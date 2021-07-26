from django.db import models

class Weather(models.Model):
  temperature = models.CharField(max_length=5)
  icon= models.CharField(max_length=5)
  description = models.CharField(max_length=50)
  city= models.CharField(max_length=50)
  
  def __str__(self):
    return self.city