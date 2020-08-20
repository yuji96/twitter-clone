from django.contrib.auth.forms import UserCreationForm
from django.views import generic


class SignupView(generic.CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = 'timeline'

    def form_valid(self, form):
        user = form.save()
        user.save()
        return super().form_valid(form)
