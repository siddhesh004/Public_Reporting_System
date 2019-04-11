from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView
from ..models import Incidence, Vote
from ..forms import IncidenceForm
from django.http import HttpResponse,Http404
from django.db import IntegrityError
from django.shortcuts import render_to_response

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


def upvoteview(request, id):

    try:
        obj = get_object_or_404(Incidence, pk=id)
        temp = obj.upvotes
        temp = temp + 1
        obj.upvotes = temp
        obj.save()

        vote_obj = Vote(user=request.user, incidence=obj)
        vote_obj.save()
    except IntegrityError as e:
        return render_to_response("error.html")

    return redirect(reported)


def downvoteview(request, id):
    try:
        obj = get_object_or_404(Incidence, pk=id)
        temp = obj.downvotes
        temp = temp + 1
        obj.downvotes = temp
        obj.save()

        vote_obj = Vote(user=request.user, incidence=obj)
        vote_obj.save()
    except IntegrityError as e:
        return render_to_response("error.html")

    return redirect(reported)


def reported(request):

    reports = Incidence.objects.all()

    return render(request,'reports.html',context={'reports':reports})

def civicreports(request):

    reports = Incidence.objects.all()

    return render(request,'civicreports.html',context={'reports':reports})
