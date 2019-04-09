from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView
from ..forms import CivicSignUpForm
from ..models import User, Civic
from django.shortcuts import render
from leaflet.forms.fields import PointField

def incidence_view(request):
    context={}
    return render(request,"incidence.html",context)