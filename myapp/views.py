from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"myapp/index.html")

def about(request):
    return render(request,"myapp/index.html")

def skills(request):
    return render(request,"myapp/index.html")

def projects(request):
    return render(request,"myapp/index.html")

def experience(request):
    return render(request,"myapp/index.html")

def services(request):
    return render(request,"myapp/index.html")

def contact(request):
    return render(request,"myapp/index.html")