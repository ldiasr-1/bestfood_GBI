from rest_framework import serializers
from produtos.models import Produto, Tag
from mercado.models import Mercado
from promo.models import Promocao

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'nome']

class MercadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mercado
        fields = ['id', 'nome', 'endereco']

class ProdutoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    mercados = MercadoSerializer(many=True, read_only=True)

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco', 'tags', 'mercados']

class PromocaoSerializer(serializers.ModelSerializer):
    produtos = ProdutoSerializer(many=True, read_only=True)

    class Meta:
        model = Promocao
        fields = ['id', 'percentual', 'produtos']