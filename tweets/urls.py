from django.urls import path
from . import views

urlpatterns = [
    path('', views.TimelineView.as_view(), name='timeline'),
    path('tweet/new/', views.tweet_new, name='tweet_new'),
]
