from django.conf import settings
from django.db import models
from django.utils import timezone


class Tweet(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.created_time.strftime('%Y-%m-%d %H:%M:%S')
