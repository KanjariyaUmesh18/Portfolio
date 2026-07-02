from django.shortcuts import render
from .models import * 

# Create your views here.

def home(request):

    data = Home.objects.first()
    skills = Skills.objects.all()

    projects = Projects.objects.prefetch_related('tool').all

    edu = Eduacation.objects.all()

    context = {
        "data" : data,
        "skills" : skills,
        "projects" : projects,
        "edu" : edu
    }
    return render(request,"myapp/index.html",context)

