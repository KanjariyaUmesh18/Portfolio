from django.shortcuts import render,redirect
from .models import * 
from django.conf import settings
from django.core.mail import EmailMessage

# Create your views here.

def home(request):

    display_skills = DisplaySkills.objects.all()

    print("DISPLAY SKILLS:", list(display_skills))

    for skill in display_skills:
        print("SKILL NAME:", skill.skill_name)

    data = Home.objects.first()
    skills = Skills.objects.all()
    projects = Projects.objects.prefetch_related('tool').all()
    edu = Eduacation.objects.all()
    about_info = About.objects.all()
    about = AboutCard.objects.all()
    ser = Services.objects.all()
    context = {
        "data": data,
        "skills": skills,
        "projects": projects,
        "edu": edu,
        "about": about,
        "about_info": about_info,
        "ser": ser,
        "display_skills" : display_skills
    }
    return render(request,"myapp/index.html",context)

def contact(request):
    if request.method == "POST":

        print("POST RECEIVED")

        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        attechment = request.FILES.get('attechment')
        print(request.POST)
        Contact.objects.create(
            fullname = fullname,
            email = email,
            subject = subject,
            message = message,
            attechment = attechment
        )
        mail = EmailMessage(
            subject   = f"New contact : {subject} ",
            body=f"""
Name : {fullname}
Email : {email}
Message : {message},
""",
    from_email=settings.EMAIL_HOST_USER,
        to=["kanjariyaumesh18@gmail.com"],
        reply_to=[email]
        )
        if attechment:
            mail.attach(
                attechment.name,
                attechment.read(),
                attechment.content_type
            )

        mail.send()

    data = Home.objects.first()
    skills = Skills.objects.all()

    projects = Projects.objects.prefetch_related('tool').all()

    edu = Eduacation.objects.all()

    about_info = About.objects.all()
    about = AboutCard.objects.all()

    ser = Services.objects.all()

    dis_skill = Home.objects.prefetch_related('display_skill').all()

    context = {
        "data" : data,
        "skills" : skills,
        "projects" : projects,
        "edu" : edu,
        "about" : about,
        "about_info" : about_info,
        "ser" : ser,
        "dis_skill" : dis_skill
    }
    return render(request,"myapp/index.html",context)


