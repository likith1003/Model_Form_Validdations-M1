from django.db import models

# Create your models here.

class School(models.Model):
    sname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    loc = models.CharField(max_length=50)
    princy = models.CharField(max_length=50)

    def __str__(self):
        return self.sname  

class Student(models.Model):
    sname = models.ForeignKey(School, on_delete=models.CASCADE)
    stdname = models.CharField(max_length=50) 
        

class Register(models.Model):
    name = models.CharField(max_length=50)
    pno = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name