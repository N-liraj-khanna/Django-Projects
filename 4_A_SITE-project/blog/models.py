from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.deletion import SET_NULL

class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}" 

    def __str__(self):
        return self.full_name()

class Post(models.Model):
    title=models.CharField(max_length=100)
    excerpt=models.CharField(max_length=250)
    image=models.CharField(max_length=150)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True, db_index=True) 
    # slug-> it makes it unique, only one value for one object, have a index value for this field, easy fr querying by defualt it already has it.
    content=models.TextField(max_length=5000,validators=[MinLengthValidator(50)])

    # Relations
    author=models.ForeignKey(Author, on_delete=SET_NULL, null=True, related_name='posts')
    tags=models.ManyToManyField(Tag)
