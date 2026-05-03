from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Todo(models.Model):
    owner = models.CharField(max_length=30)
    content = models.CharField(max_length=255)
    done = models.BooleanField(default=False)