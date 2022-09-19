from operator import mod
from django.db import models

# Create your models here.
class Health_Data(models.Model):
    """This will store data about a user's health info"""
    weight = models.IntegerField()
    height = models.IntegerField()
    age = models.IntegerField()

    