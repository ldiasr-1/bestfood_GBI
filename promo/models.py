#promo\models.py
from django.db import models
from produtos.models import Produto

class Promocao(models.Model):
    percentual = models.DecimalField(max_digits=10, decimal_places=0)
    produtos = models.ManyToManyField(Produto, related_name='promocoes')

    def __str__(self):
        return f"{self.percentual}%"