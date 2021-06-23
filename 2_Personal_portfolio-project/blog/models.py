from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    content = models.TextField(max_length=5000)

    def __str__(self):
        return self.title