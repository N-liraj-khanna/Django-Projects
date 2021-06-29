from django.db import models

class Review(models.Model):
    username=models.CharField(max_length=100)
    text=models.CharField(max_length=500)
    rating=models.IntegerField()