from django import forms
from django.forms import widgets
from .models import Lesson, Comment, Reply


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields=('__all__')
        exclude=('created_by', 'standard', 'subject', 'slug')

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('comment',)

        labels={'comment':'Comment:'}
        widgets={
            'comment':forms.Textarea(attrs={
                'class':'form-control',
                'rows':4,'cols':70,
                'placeholder': 'Enter your comment'
            })}
            
        
class ReplyForm(forms.ModelForm):
    class Meta:
        model=Reply
        fields=('reply',)
        
        widgets={'reply':forms.Textarea(attrs={'class':'form-control', 'rows':3, 'cols':5})}
