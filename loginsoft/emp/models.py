from django.db import models

# Create your models here.
class Manager(models.Model):
    mName=models.CharField(max_length=50)

class Employee(models.Model):
    eName=models.CharField(max_length=50)
    mName=models.ForeignKey(Manager,on_delete=models.CASCADE)

