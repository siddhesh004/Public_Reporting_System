from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.template.context import RequestContext

# Create your views here.


def home(request):
    context = {}
    return render(request, "home.html", context)

