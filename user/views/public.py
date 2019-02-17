from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from ..forms import PublicSignUpForm
from ..models import User


class PublicSignUpView(CreateView):
    model = User
    form_class = PublicSignUpForm
    template_name = 'registration/signup_form.html'

