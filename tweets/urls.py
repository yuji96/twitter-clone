from django.urls import path
from . import views

app_name= 'tweets'

urlpatterns = [
    path('timeline', views.TimelineView.as_view(), name='timeline'),
    path('tweet/new/', views.TweetCreate.as_view(), name='tweet_new'),
]
