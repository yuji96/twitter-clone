from django.views import generic

from .models import Tweet


class TimelineView(generic.ListView):
    template_name = 'tweets/timeline.html'
    context_object_name = 'timeline'

    def get_queryset(self):
        """Return the last five published questions."""
        return Tweet.objects.order_by('-created_time')


class TweetCreate(generic.CreateView):
    template_name = 'tweets/tweet_new.html'
    success_url = '/'
    model = Tweet
    fields = ['text']

    def form_valid(self, form):
        tweet = form.save(commit=False)
        tweet.author = self.request.user
        tweet.save()
        return super().form_valid(form)
