from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     username = forms.CharField(max_length=100, label='Your Name', error_messages={
#         'required': "Please don't leave the field Empty",
#         'max_length':"Max length is 100 characters",
#     })
#     feedback = forms.CharField(max_length=300, widget=forms.Textarea, label='Your FeedBack', error_messages={
#         'required': "Please don't leave the field Empty",
#         'max_length':"Max length is 300 characters",
#     })
#     rating = forms.IntegerField( min_value=1, max_value=5, label='Your Rating', error_messages={
#         'required': "Please don't leave the field Empty",
#         'min_value':"Min Value is 1",
#         'max_value':"Min Value is 5",
#     })
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'
        # exclude=['excluded_field']
        labels={
            "username": "Your Username",
            "text": "Your Feedback",
            "rating": "Your Rating",
        }
        error_messages={
            "username": {
                'required': "Please don't leave the field Empty",
                'max_length':"Max length is 100 characters",
            },
            "text": {
                'required': "Please don't leave the field Empty",
                'max_length':"Max length is 500 characters",
            }
        }