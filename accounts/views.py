from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.views import generic


class SignupView(generic.CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = 'timeline'


class Login(LoginView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    success_url = 'timeline'
