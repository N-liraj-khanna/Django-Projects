from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('create/', views.create, name="create"),
  path('delete/<pk>/', views.delete, name="delete"),
]