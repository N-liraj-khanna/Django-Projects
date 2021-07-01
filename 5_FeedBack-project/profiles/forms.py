from django import forms

class ProfileForm(forms.Form):
    profile_picture = forms.FileField()
    # profile_picture = forms.ImageField()