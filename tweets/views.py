from django.views import generic

from .models import Tweet


class TimelineView(generic.ListView):
    template_name = 'tweets/timeline.html'
    context_object_name = 'timeline'

    def get_queryset(self):
        """Return the last five published questions."""
        return Tweet.objects.order_by('-pub_date')[:5]
