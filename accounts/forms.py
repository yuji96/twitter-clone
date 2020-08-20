from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def create_user(self):
        user = User(username=self.cleaned_data.pop('username'),
                    password=self.cleaned_data.pop('password'))
        user.save()
