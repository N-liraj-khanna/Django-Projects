from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View

class ReviewView(View):
    def get(self, request):
        form=ReviewForm()
        return render(request,'review.html', {'form':form})            

    def post(self, request):
        form=ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
        return render(request,'review.html', {'form':form})            



# def review(request):  # instead of fucntion view, class view modified above for this fucntion
#     if request.method == 'POST':
#         form=ReviewForm(request.POST)
#         if form.is_valid():
#             # review=Review(username=form.cleaned_data['username'],
#             # text=form.cleaned_data['feedback'],
#             # rating=form.cleaned_data['rating'])
#             # review.save() # No need for this, since we using modelforms not we created forms
#             form.save()
#             return HttpResponseRedirect('/thank-you')
#     else:  # if the request is get, normal form, else the form with the user input(i.e.,POST)
#         form=ReviewForm()
#     return render(request,'review.html', {'form':form})            

def thank_you(request):
    return render(request,'thank_you.html', {'username':'username'})