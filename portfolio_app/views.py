from django.http import HttpResponse
from django.shortcuts import render
from .models import Project
from .forms import ContactForm
from django.shortcuts import render, redirect
from .models import Project, Skill, Contact
import os


def index(request):
    return render(request, 'base.html')


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_app/portfolio_list.html', {'projects': projects})

def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'skills/skill_list.html', {'skills': skills})
def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})

def thanks(request):
    return render(request, 'contacts/thanks.html')


def certificate(request, certificate):
    return HttpResponse(certificate)