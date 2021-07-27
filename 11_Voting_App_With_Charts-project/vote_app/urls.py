from django.urls import path
from . import views

urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('vote_lists/', views.VoteListView.as_view(), name='vote_list'),
  path('vote_lists/<int:pk>/', views.ChoicesView.as_view(), name='choices'),
  path('vote_lists/<int:pk>/results', views.ResultsView.as_view(), name='results'),
  path('vote_lists/<int:pk>/results_data', views.results_data, name='results_data'),
]