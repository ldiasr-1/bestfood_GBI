from django.db import models
from accounts.models import CustomUser  # Importe o CustomUser de accounts

class Pessoa(CustomUser):
    endereco_pessoa = models.CharField(max_length=100)
    telefone_pessoa = models.CharField(max_length=11)

class Cliente(Pessoa):
    cpf_pessoa = models.CharField(max_length=11, unique=True)

class Vendedor(Pessoa):
    cnpj_pessoa = models.CharField(max_length=14, unique=True)