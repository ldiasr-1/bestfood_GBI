# promo/serializers.py
from rest_framework import serializers
from promo.models import Promocao
from produtos.models import Produto
from produtos.serializers import ProdutoSerializer

class PromocaoSerializer(serializers.ModelSerializer):
    produtos = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all(), many=True, required=False, write_only=True)

    produto_info = ProdutoSerializer(source='produtos', many=True, read_only=True)

    preco_antigo = serializers.SerializerMethodField()
    preco_novo = serializers.SerializerMethodField()

    class Meta:
        model = Promocao
        fields = ['id', 'percentual', 'produtos', 'produto_info', 'preco_antigo', 'preco_novo']

    def get_preco_antigo(self, obj):
        return [produto.preco for produto in obj.produtos.all()]

    def get_preco_novo(self, obj):
        return [produto.preco * (1 - obj.percentual / 100) for produto in obj.produtos.all()]