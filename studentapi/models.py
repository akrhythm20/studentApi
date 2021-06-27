from django.db import models

# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    mobile = models.CharField(max_length=15)
