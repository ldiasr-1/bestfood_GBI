from rest_framework import serializers
from promo.models import Promocao
from produtos.serializers import ProdutoSerializer

class PromocaoSerializer(serializers.ModelSerializer):
    produtos = ProdutoSerializer(many=True, read_only=True)

    class Meta:
        model = Promocao
        fields = ['id', 'percentual', 'produtos']