from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.StandardView.as_view(), name='curriculum'),
    path('<slug:slug>/', views.SubjectView.as_view(), name='subjects_details'),
    path('<slug:standard>/<slug:slug>/', views.LessonView.as_view(), name='lesson_details'),
    path('<slug:standard>/<slug:slug>/create', views.LessonCreateView.as_view(), name='create_lesson'),
    path('<slug:standard>/<slug:chapter>/<slug:slug>/', views.LessonContentsView.as_view(), name='lesson_contents'),
    path('<slug:standard>/<slug:chapter>/<slug:slug>/update', views.LessonUpdateView.as_view(), name='update_lesson'),
    path('<slug:standard>/<slug:chapter>/<slug:slug>/delete', views.LessonDeleteView.as_view(), name='delete_lesson'),
]