from django import forms

from .models import Tweet


class TweetForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

    def create_tweet(self, request):
        tweet = Tweet(author=request.user,
                      text=self.cleaned_data.pop('text'))
        tweet.save()
