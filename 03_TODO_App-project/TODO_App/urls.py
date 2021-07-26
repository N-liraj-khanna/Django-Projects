"""TODO_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views

app_name = 'todo'

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('sign-up/', views.signupuser, name='signupuser'),
    path('log-in/', views.loginuser, name='loginuser'),
    path('log-out/', views.logoutuser, name='logoutuser'),

    # todo's
    path('', views.home, name='home'),
    path('create-todo/', views.create_todo, name='create_todo'),
    path('todos/', views.current_todo_page, name='current_todo_page'),
    path('completed_todos/', views.completed_todos_page, name='completed_todos_page'),
    path('todo/<int:todo_pk>', views.view_todo_page, name='view_todo_page'),
    path('todo/<int:todo_pk>/complete', views.complete_todo, name='complete_todo'),
    path('todo/<int:todo_pk>/deleted', views.delete_todo, name='delete_todo'),
    path('todo/<int:todo_pk>/move_back', views.move_back, name='move_back'),
]
