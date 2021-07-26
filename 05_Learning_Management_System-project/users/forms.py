from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    model=User
    fields=('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    labels={
        'password1':'Password: ',
        'password2':'Confirm Password: '
    }    

class UserProfileForm(forms.ModelForm):
    bio=forms.CharField(required=False)
    
    parent='parent'
    student='student'
    all_users = [
        (student,'student'),
        (parent,'parent'),
    ]
    user_type = forms.ChoiceField(required=True, choices=all_users)

    class Meta:
        model = UserProfile 
        fields = ('bio', 'profile_pic', 'user_type')



