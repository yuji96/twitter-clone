from django.shortcuts import redirect, render
from django.utils import timezone
from django.views import generic

from .forms import TweetForm
from .models import Tweet


class TimelineView(generic.ListView):
    template_name = 'tweets/timeline.html'
    context_object_name = 'timeline'

    def get_queryset(self):
        """Return the last five published questions."""
        return Tweet.objects.order_by('-created_date')


def tweet_new(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.author = request.user
            tweet.published_date = timezone.now()
            tweet.save()
            return redirect('timeline')
    else:
        form = TweetForm()
    return render(request, 'tweets/tweet_new.html', {'form': form})
