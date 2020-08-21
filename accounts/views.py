from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.views import generic


class SignupView(generic.CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = 'timeline'

    def form_valid(self, form):
        user = form.save()
        user.save()
        return super().form_valid(form)


class Login(LoginView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    success_url = 'tweets:timeline'

    def form_valid(self, form):
        return super().form_valid(form)
