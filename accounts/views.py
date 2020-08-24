from django.contrib.auth.forms import UserCreationForm
from django.views import generic


class SignupView(generic.CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = 'timeline'
