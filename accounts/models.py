from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username