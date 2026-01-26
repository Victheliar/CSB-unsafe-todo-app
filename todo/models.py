from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    username = models.TextField(User, on_delete=models.CASCADE)
    password = models.TextField(User)