#mercado/models.py
from django.db import models

class Tag(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField(Tag, blank=True)
    mercados = models.ManyToManyField('mercado.Mercado', related_name='produtos')

    def __str__(self):
        return self.nome

    def atualizar_preco(self, novo_preco):
        self.preco = novo_preco
        self.save()

    def aplicar_promocao(self, desconto):
        """
        Aplica um desconto percentual ao preço do produto.
        Exemplo: desconto=10 para 10% de desconto.
        """
        self.preco = self.preco * (1 - desconto / 100)
        self.save()