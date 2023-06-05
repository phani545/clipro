from django.db import models

# Create your models here.

class Studen(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    testscore=models.FloatField()
