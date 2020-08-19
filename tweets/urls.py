from django.urls import path
from . import views

urlpatterns = [
    path('', views.TimelineView.as_view(), name='timeline'),
    path('tweet/new/', views.TweetCreate.as_view(), name='tweet_new'),
]
