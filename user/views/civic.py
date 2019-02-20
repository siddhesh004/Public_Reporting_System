from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView
from ..forms import CivicSignUpForm
from ..models import User, Civic


class CivicSignUpView(CreateView):
    model = Civic
    form_class = CivicSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'civic'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('civic:civic_home')


class CivicHomeView(TemplateView):
    template_name = 'civic/civic_home.html'
