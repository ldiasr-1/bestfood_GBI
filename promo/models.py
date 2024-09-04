from django.db import models

class Promocao(models.Model):
    percentual = models.DecimalField(max_digits=10, decimal_places=0)
    produtos = models.ManyToManyField('produtos.Produto', related_name='promocoes')  # Referência de string

    def __str__(self):
        return f"{self.percentual}%"