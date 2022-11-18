from django.db import models

# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=10)
    password= models.CharField(max_length=60)
    name= models. CharField(max_length=20)
    age = models.CharField(max_length=3)
    createdDate= models.DateTimeField(auto_now_add=True)
    updatedDate= models.DateTimeField(auto_now=True)