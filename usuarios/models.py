from django.db import models
from accounts.models import CustomUser  # Importe o CustomUser de accounts

class Pessoa(CustomUser):
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)

class Cliente(Pessoa):
    cpf = models.CharField(max_length=11, unique=True)

class Vendedor(Pessoa):
    cnpj = models.CharField(max_length=14, unique=True)