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
