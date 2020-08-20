from django.views import generic

from .forms import SignupForm


class SignupView(generic.FormView):
    template_name = 'accounts/signup.html'
    form_class = SignupForm
    success_url = 'timeline'

    def form_valid(self, form):
        form.create_user()
        return super().form_valid(form)

