from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Todo(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    done = models.BooleanField(default=False)