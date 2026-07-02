from django.db import models

# Create your models here.

class Home(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.TextField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.firstname + self.lastname

class About(models.Model):
    title = models.CharField(max_length=50)
    paragraph1 = models.TextField()
    paragraph2 = models.TextField(blank=True,null=True)
    paragraph3 = models.TextField(blank=True,null=True)

class AboutCard(models.Model):
    about = models.ForeignKey(About,on_delete=models.CASCADE)
    icon = models.ImageField(upload_to="about/icons/")
    cardtitle = models.CharField(max_length=30)
    description_a = models.TextField()

    def __str__(self):
        return self.cardtitle
    
class Skills(models.Model):
    skill_name = models.CharField(max_length=20)
    icon = models.ImageField(upload_to="skills/")
    skill_percentage = models.IntegerField()
    skill_description = models.TextField()

    def __str__(self):
        return self.skill_name

class Tool(models.Model):
    tool_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tool_name

class Projects(models.Model):
    project_name = models.CharField(max_length=50)
    pro_description = models.TextField()
    pro_image = models.ImageField(upload_to="projects/")
    git_link = models.URLField()
    live_link = models.URLField(blank=True)

    tool = models.ManyToManyField(Tool,related_name="projects")

    def __str__(self):
        return self.project_name

class Eduacation(models.Model):
    year = models.CharField(max_length=30)
    course = models.CharField(max_length=40)
    institute = models.CharField(max_length=30)
    edu_description = models.TextField()

    def __str__(self):
        return self.course

class Services(models.Model):
    s_icon = models.ImageField(upload_to="services/icon")
    ser_name = models.CharField(max_length=20)
    ser_desc = models.TextField()
    li1 = models.CharField(max_length=30)
    li2 = models.CharField(max_length=30,blank=True,null=True)
    li3 = models.CharField(max_length=30,blank=True,null=True)

    def __str__(self):
        return self.ser_name

class Contact(models.Model):
    fullname = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.TextField()
    attechment = models.FileField(upload_to="attechment",blank=True,null=True)

    def __str__(self):
        return self.fullname





