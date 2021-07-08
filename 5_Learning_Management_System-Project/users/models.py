from django.db import models
from django.contrib.auth.admin import User
import os

def media_path_organizer(instance, filename):
    upload_to='images/'
    ext=filename.split('.')[-1]
    if instance.user.username:
        filename = 'User_Profile_Picture/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300, blank=True)
    profile_pic = models.ImageField(upload_to=media_path_organizer, blank=True, verbose_name='Profile Picture')
    
    parent='parent'
    student='student'
    teacher='teacher'
    all_users = [
        (student,'student'),
        (teacher,'teacher'),
        (parent,'parent'),
    ]
    user_type = models.CharField(max_length=30, choices=all_users, default=student)

    def __str__(self):
        return self.user.username