from django.db import models

# Create your models here.
class Employee(models.Model):
    firstName = models.CharField(max_length=30)
    lasstName = models.CharField(max_length=30)
    salary = models.FloatField()
    email = models.CharField(max_length=30)

