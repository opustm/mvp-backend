from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class User(AbstractUser):
    picture = models.CharField(max_length=100, default='pic1')
    theme = models.CharField(max_length=100, default='theme1')
    phone = models.CharField(max_length=100, default='123-456-7890')

class MyGroup(Group):
    picture = models.CharField(max_length=100, default='pic1')
    announcement = models.CharField(max_length=100, default='This is a group')
