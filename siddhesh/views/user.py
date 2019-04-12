from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView
from ..models import Incidence, Vote
from ..forms import IncidenceForm
from django.http import HttpResponse,Http404
from django.db import IntegrityError
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):

    return render(request, 'home.html')


@login_required
def IncidenceReport(request):

        form = IncidenceForm(request.POST or None)

        if form.is_valid():
            form.save()
            form = IncidenceForm()

        context = {'form': form}

        return render(request,"incidence.html",context)


def signupview(request):

    return render(request, 'signup.html')

@login_required
def upvoteview(request, id):
    obj = get_object_or_404(Incidence, pk=id)
    try:


        vote_obj = Vote(user=request.user, incidence=obj)
        vote_obj.save()
    except IntegrityError as e:
        return render_to_response("error.html")


    temp = obj.upvotes
    temp = temp + 1
    obj.upvotes = temp
    obj.save()

    return redirect(reported)

@login_required
def downvoteview(request, id):
    obj = get_object_or_404(Incidence, pk=id)

    try:


        vote_obj = Vote(user=request.user, incidence=obj)
        vote_obj.save()
    except IntegrityError as e:
        return render_to_response("error.html")


    temp = obj.downvotes
    temp = temp + 1
    obj.downvotes = temp
    obj.save()

    return redirect(reported)


def reported(request):

    reports = Incidence.objects.all()

    return render(request,'reports.html',context={'reports':reports})

@login_required
def civicreports(request):

    reports = Incidence.objects.all()

    return render(request,'civicreports.html',context={'reports':reports})
