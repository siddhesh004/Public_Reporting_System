from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from ..models import Incidence
from ..forms import IncidenceForm

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):

    return render(request, 'home.html')


def IncidenceReport(request):

        form = IncidenceForm(request.POST or None)

        if form.is_valid():
            form.save()
            form = IncidenceForm()

        context = {'form': form}

        return render(request,"incidence.html",context)


def signupview(request):

    return render(request, 'signup.html')


def reported(request):

    reports = Incidence.objects.all()

    return render(request,'reports.html',context={'reports':reports})
