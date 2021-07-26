from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

class ReviewView(CreateView):
    model=Review
    template_name = 'review.html'
    form_class = ReviewForm
    success_url = '/thank-you'


# class ReviewView(FormView): # using form view
#     template_name = 'review.html'
#     form_class = ReviewForm
#     success_url = '/thank-you'

#     def form_valid(self, form):
#         form.save()
#         print(type(form))
#         return super().form_valid(form)


# class ReviewView(View): # Normal class type form using basic View module
#     def get(self, request):
#         form=ReviewForm()
#         return render(request,'review.html', {'form':form})            

#     def post(self, request):
#         form=ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/thank-you')
#         return render(request,'review.html', {'form':form})   

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


class ThankYouView(TemplateView):
    template_name='thank_you.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['username']='username'
        return context
    
# class ReviewsListView(TemplateView): # using template view
#     template_name='reviews_list.html'

#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         reviews=Review.objects.all()
#         context['reviews']=reviews
#         return context

class ReviewsListView(ListView): # using listview
    template_name='reviews_list.html'
    model=Review
    context_object_name='reviews'

    # def get_queryset(self): # filtering rating data to less than 5, refer docs for more
    #     query=super().get_queryset()
    #     data=query.filter(rating__lt=5)
    #     return data

# class ReviewDetailsView(TemplateView): # template view
#     template_name='review_details.html'

#     def get_context_data(Self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         review=Review.objects.get(pk=kwargs['id'])
#         print(review)
#         context['review']=review  
#         return context

class ReviewDetailsView(DetailView):
    template_name='review_details.html'
    model=Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded = self.object
        fav = self.request.session.get('fav_id')
        context['fav'] = str(loaded.id) == fav
        return context

class FavoriteView(View):
    def post(self, request):
        id=request.POST['id_review']
        request.session['fav_id'] = id
        return HttpResponseRedirect('/review-detail/'+str(id))
