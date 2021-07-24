from .models import Todo
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
  qs=Todo.objects.all().order_by('-date')
  todos=[]
  
  for todo in qs:
    todos+=[{"title": todo.content}]
      
  return render(request, 'index.html', context={"todos":qs})


def create(request):
  if request.method == 'POST':
    new_todo_data = request.POST.get('todo')
    # new_todo_data = request.POST.get('content')
    if new_todo_data and len(new_todo_data)!=0:
      new_todo_obj = Todo(content=new_todo_data)
      new_todo_obj.save()
      # return HttpResponse(str(new_todo_data)+" "+str(new_todo_obj.id))
    
  return redirect('index')
    


def delete(request, pk):
  obj= get_object_or_404(Todo, pk=pk)
  obj.delete()
  return redirect('index')