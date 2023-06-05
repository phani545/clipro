from django.db import models

# Create your models here.
class Employee(models.Model):
    firstName = models.CharField(max_length=30)
    lasstName = models.CharField(max_length=30)
    salary = models.FloatField()
    email = models.CharField(max_length=30)


class Project(models.Model):
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    name = models.CharField(max_length=30)
    assigned = models.CharField(max_length=30)
    priority = models.IntegerField()

