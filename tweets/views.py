from django.views import generic

from .forms import TweetForm
from .models import Tweet


class TimelineView(generic.ListView):
    template_name = 'tweets/timeline.html'
    context_object_name = 'timeline'

    def get_queryset(self):
        """Return the last five published questions."""
        return Tweet.objects.order_by('-created_date')


class TweetCreate(generic.FormView):
    template_name = 'tweets/tweet_new.html'
    form_class = TweetForm
    success_url = '/'

    def form_valid(self, form):
        form.tweet_new(self.request)
        return super().form_valid(form)
