from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario (User):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    