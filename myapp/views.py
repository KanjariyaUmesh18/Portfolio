from django.shortcuts import render
from .models import * 

# Create your views here.

def home(request):

    data = Home.objects.first()
    skills = Skills.objects.all()

    for skill in skills:
        print(skill.icon)
        print(skill.icon.url)
    context = {
        "data" : data,
        "skills" : skills
    }
    return render(request,"myapp/index.html",context)

