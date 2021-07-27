from django.urls import path
from . import views
urlpatterns=[
  path('', views.Index.as_view(), name="index"),
  path('delete/<int:pk>/', views.Delete.as_view(), name="delete"),
  path('update/<int:pk>/', views.Update.as_view(), name="update"),
  path('complete/<int:pk>/', views.complete, name="complete"),
]