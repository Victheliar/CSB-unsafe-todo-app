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

# from django.db import models
# from django.conf import settings


# # Create your models here.

# class Todo(models.Model):
#     owner = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name="todos",
#     )
#     content = models.CharField(max_length=255)
#     done = models.BooleanField(default=False)