
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Account(AbstractUser):
    email = models.EmailField(max_length=60, unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    username = models.CharField(max_length=200, unique=True)
    weight = models.IntegerField()
    age = models.IntegerField()
    height_in_inches = models.CharField(max_length=5)
    height = models.CharField(max_length=3)


  
