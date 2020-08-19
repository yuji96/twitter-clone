import datetime
from datetime import time

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .forms import TweetForm
from .models import Tweet


def create_tweet(author, text, time):
    Tweet.objects.create(
        author=author, text=text, created_date=time
    )


def strftime(time):
    return time.strftime('%Y-%m-%d %H:%M:%S')


class TimelineViewTests(TestCase):
    def test_no_tweets(self):
        response = self.client.get(reverse('tweets:timeline'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "no tweets")
        self.assertQuerysetEqual(response.context['timeline'], [])

    def test_past_tweet(self):
        author = User.objects.create_user("tester")
        time = timezone.now() - datetime.timedelta(days=1)
        create_tweet(author=author, text="Past Tweet.", time=time)
        response = self.client.get(reverse('tweets:timeline'))
        self.assertQuerysetEqual(
            response.context['timeline'],
            [f'<Tweet: {strftime(time)}>']
        )

    def test_two_past_tweets(self):
        author = User.objects.create_user("tester")
        time1 = timezone.now() - datetime.timedelta(days=1)
        time2 = timezone.now() - datetime.timedelta(days=3)
        create_tweet(author=author, text="Past Tweet 1.", time=time1)
        create_tweet(author=author, text="Past Tweet 2.", time=time2)
        response = self.client.get(reverse('tweets:timeline'))
        self.assertQuerysetEqual(
            response.context['timeline'],
            [f'<Tweet: {strftime(time1)}>', f'<Tweet: {strftime(time2)}>']
        )


class TweetCreateViewTest(TestCase):
    def test_form(self):
        data = {'text': 'test'}
        form = TweetForm(data)
        self.assertTrue(form.is_valid())


class TweetModelTests(TestCase):
    pass
