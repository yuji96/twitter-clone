from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .models import Tweet
   

class TimelineView(LoginRequiredMixin, generic.ListView):
    template_name = 'tweets/timeline.html'
    context_object_name = 'timeline'

    def get_queryset(self):
        return Tweet.objects.order_by('-created_time')


class TweetCreate(generic.CreateView):
    template_name = 'tweets/tweet_new.html'
    success_url = reverse_lazy('tweets:timeline')
    model = Tweet
    fields = ['text']

    def form_valid(self, form):
        tweet = form.save(commit=False)
        tweet.author = self.request.user
        tweet.save()
        return super().form_valid(form)
