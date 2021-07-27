from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView
from django.views.generic.edit import DeleteView, UpdateView
from .models import ToDo
from .forms import CreateForm

class Index(ListView, FormView):
  model = ToDo
  template_name = 'todo/index.html'
  context_object_name="tasks"
  fields = ['task', 'completed',]
  form_class = CreateForm
  success_url = '/'
    
  def post(self, request):
    form = CreateForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('index')
    
    return render(request, 'todo/index.html', context={"error": True, "tasks": ToDo.objects.all(), "form": self.form_class})
  
class Delete(DeleteView):
  template_name='todo/delete.html'
  model=ToDo
  success_url = '/'

class Update(UpdateView):
  template_name='todo/update.html'
  fields = ['task', 'completed',]
  model=ToDo
  success_url = '/'

def complete(request, pk):
  obj=ToDo.objects.get(id=pk)
  obj.completed=not obj.completed
  obj.save()
  return redirect('index')