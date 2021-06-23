from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'todo/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('current_todo_page')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'Username taken, Provide new Username'})
        else:
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords Mismatch'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('current_todo_page')
        else:
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(), 'error': 'The Username and Password do not match'})

# will work only if they're authenticated(imported from django login_required)
@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def create_todo(request):
    if request.method == 'GET':
        return render(request, 'todo/create_todo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False) # Won't directly put in db, only creaes a form object
            new_todo.user = request.user
            new_todo.save()
            return redirect('current_todo_page')
        except ValueError:
            return render(request, 'todo/create_todo.html', {'form': TodoForm(), 'error': 'Bad Input Data'})

@login_required
def current_todo_page(request):
    todos = Todo.objects.filter(user=request.user, completed_time__isnull=True)
    return render(request, 'todo/current_todo_page.html',{'todos': todos})

@login_required
def view_todo_page(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/view_todo_page.html', {'todo': todo, 'todo_form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('current_todo_page')
        except ValueError:
            return render(request, 'todo/create_todo.html', {'form': TodoForm(), 'error': 'Bad Input Data'})

@login_required
def complete_todo(request, todo_pk):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
        todo.completed_time = timezone.now()
        todo.save()
        return redirect('current_todo_page')
    else:
        return redirect('current_todo_page')

@login_required
def delete_todo(request, todo_pk):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
        todo.delete()
    return redirect('current_todo_page')

@login_required
def completed_todos_page(request):
    todos = Todo.objects.filter(user=request.user, completed_time__isnull=False).order_by('-completed_time')
    return render(request, 'todo/completed_todos.html',{'todos': todos}) 

@login_required
def move_back(request, todo_pk):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
        todo.completed_time = None
        todo.save()
    return redirect('current_todo_page')


