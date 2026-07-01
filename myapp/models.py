from django.db import models

# Create your models here.

class Home(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.TextField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.firstname + self.lastname
