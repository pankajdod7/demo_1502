from django.db import models

# Create your models here.

class Student(models.Model):
    std_name = models.CharField(max_length=100)
    std_address = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.std_name

# from django.contrib.auth.models import AbstractUser

# class Employee(AbstractUser):
#     emp_pic = models.ImageField()
    