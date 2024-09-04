from django.db import models
from accounts.models import CustomUser, User
# Create your models here.

class Pessoa (CustomUser):
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)

class Cliente (Pessoa):
    cpf = models.CharField(primary_key=True, max_length=11)
    
class Vendedor (Pessoa):
    cnpj = models.CharField(primary_key=True, max_length=14)