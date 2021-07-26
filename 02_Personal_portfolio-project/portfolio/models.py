from django.db import models

class Project(models.Model):
    image = models.ImageField(upload_to='portfolio/images/')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title