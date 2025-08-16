from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    TYPE_CHOICES = [
        ("manager", "Manager"),
        ("employee", "Employee"),
    ]
    type = models.CharField(max_length=8, choices=TYPE_CHOICES)
