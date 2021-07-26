from django.db import models
from django.template.defaultfilters import slugify
import os
from django.contrib.auth.admin import User
from django.urls import reverse

class Standard(models.Model):
    standard= models.CharField(max_length=150)
    slug= models.SlugField(blank=True, null=True, max_length=150)
    description= models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.standard
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.standard)
        super().save(*args, **kwargs)

def subject_pictures_path_organizer(instance, filename):
    upload_to='images/'
    ext=filename.split('.')[-1]
    if instance.subject_id:
        filename = 'Subject Pictures/{}.{}'.format(instance.subject_id, ext)
    return os.path.join(upload_to, filename)

class Subject(models.Model):
    subject_id=models.CharField(max_length=100)
    subject=models.CharField(max_length=200)
    slug=models.SlugField(null=True, blank=True)
    standard=models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='subjects')
    image=models.ImageField(upload_to=subject_pictures_path_organizer, blank=True, verbose_name='Subject Image')
    description=models.TextField(max_length=1000)

    def __str__(self):
        return self.subject
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.subject_id)
        super().save(*args, **kwargs)
    


def lesson_files_path_organizer(instance, filename):
    upload_to='images/'
    ext=filename.split('.')[-1]
    if instance.lesson_id:
        filename='Lesson Files/{}/{}.{}'.format(instance.lesson_id, instance.lesson_id, ext)
        if os.path.exists(filename):
            new_name=str(instance.lesson_id)+str('(1)')
            filename='Lesson Files/{}/{}.{}'.format(instance.lesson_id, new_name, ext)
    return os.path.join(upload_to, filename)


class Lesson(models.Model):

    lesson_id=models.CharField(max_length=100)
    lesson_name=models.CharField(max_length=200)
    slug=models.SlugField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    chapter_num=models.PositiveSmallIntegerField(verbose_name='Chapter Number')
    
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)
    standard= models.ForeignKey(Standard, on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='lessons')

    slug=models.SlugField(blank=True, null=True)

    video=models.FileField(blank=True, null=True, verbose_name='video', upload_to=lesson_files_path_organizer)
    ppt=models.FileField(blank=True, verbose_name='ppt', upload_to=lesson_files_path_organizer)
    notes=models.FileField(blank=True, verbose_name='note', upload_to=lesson_files_path_organizer)

    class Meta:
        ordering = ['chapter_num']

    def __str__(self):
        return self.lesson_name
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.lesson_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('lesson_details', kwargs={'slug': self.subject.slug, 'standard':self.standard.slug})


class Comment(models.Model):
    comment_slug=models.CharField(max_length=150, blank=True)
    comment=models.TextField(max_length=750)

    author=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='comments')

    date=models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.comment_slug=slugify("Comment By - " + str(self.author) + ' ' + str(self.lesson))
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.comment_slug
    
    class Meta:
        ordering =['-date']
    
class Reply(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')

    reply = models.TextField(max_length=500)
    date= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return "Reply    to " + str(self.comment) + ' by ' + str(self.author)
