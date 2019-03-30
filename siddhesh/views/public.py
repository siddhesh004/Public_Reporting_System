from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView

from ..forms import PublicSignUpForm
from ..models import User, Public


class PublicSignUpView(CreateView):
    model = Public
    form_class = PublicSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'public'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('civic:civic_home')


class PublicHomeView(TemplateView):
    template_name = 'public/public_home.html'
