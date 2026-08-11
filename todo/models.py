from django.db import models
from django.conf import settings


# Create your models here.

class Todo(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="todos",
    )
    content = models.CharField(max_length=255)
    done = models.BooleanField(default=False)