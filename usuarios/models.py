from django.db import models
from accounts.models import Usuario
# Create your models here.

class Pessoa (Usuario):
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)

class Cliente (Pessoa):
    cpf = models.CharField(max_length=11)
    
class Vendedor (Pessoa):
    cnpj = models.CharField(max_length=14)