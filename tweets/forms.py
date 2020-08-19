from django import forms
from django.utils import timezone

from .models import Tweet


class TweetForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

    def tweet_new(self, request):
        tweet = Tweet(author=request.user,
                      text=self.cleaned_data.pop('text'),
                      created_date=timezone.now())
        tweet.save()
