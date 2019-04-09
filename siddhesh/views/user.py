from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from ..forms import IncidenceForm

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):

    return render(request, 'home.html')

class MapView(TemplateView):

    template_name = 'incidence.html'

    def get_context(self, **kwargs):
        context = {'incidenceform': IncidenceForm()}
        return context
