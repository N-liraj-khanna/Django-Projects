from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view(), name='review'),
    path('thank-you/', views.ThankYouView.as_view(), name='thank_you'),
    path('reviews-list/', views.ReviewsListView.as_view(), name='reviews_list'),
    path('review-detail/favorite', views.FavoriteView.as_view(), name='review_detail-favorite'),
    path('review-detail/<int:pk>', views.ReviewDetailsView.as_view(), name='review_detail'),
]
