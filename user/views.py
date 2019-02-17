from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.form import UserCreationForm

# Create your views here.


def home(request):

    context = {}
    return render(request, "home.html", context)

