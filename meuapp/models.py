from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    endereco = models.CharField(max_length=20, null=True, blank=True)

