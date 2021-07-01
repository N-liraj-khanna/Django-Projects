from django.db import models

class UserProfile(models.Model):
    image= models.FileField(upload_to='images')
    # image= models.ImageField(upload_to='images')