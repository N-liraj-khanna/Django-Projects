from .models import VoteTitle, Vote

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView


class IndexView(TemplateView):
  template_name = 'vote/index.html'
  
  
class VoteListView(ListView):
  model = VoteTitle
  fields = ['title']
  template_name = 'vote/list_votes.html'
  context_object_name="votes_list"
  ordering = ['-date']
  
    
class ChoicesView(DetailView):
  model = VoteTitle
  template_name= 'vote/choices.html'
  context_object_name="question"
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    obj=VoteTitle.objects.get(id=context['object'].id)
    choices = obj.question_ref.all()
    
    context['choices']=choices
    return context


class ResultsView(DetailView):
  template_name = 'vote/results.html'
  model=VoteTitle
  context_object_name="question"
  
  def get(self, request, pk):
    question_obj = VoteTitle.objects.get(id=pk)
    question_choices_obj = question_obj.question_ref.all()
    
    return render(request, 'vote/results.html', context={'choices':question_choices_obj, 'pk': pk})
          
  def post(self, request, pk):
    obj=Vote.objects.get(id=request.POST.get('choice'))
    obj.votes+=1
    obj.save()
    return redirect('results', pk)
  
def results_data(request, pk):
  results_obj = VoteTitle.objects.get(id=pk)
  results_obj_data = results_obj.question_ref.all()

  results = []
  for data in results_obj_data:
    results.append([data.choice, data.votes])

  return JsonResponse(results, safe=False)