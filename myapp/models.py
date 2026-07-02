from django.db import models

# Create your models here.

class Home(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.TextField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.firstname + self.lastname
    
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
