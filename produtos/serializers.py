# produtos/serializers.py
from rest_framework import serializers
from produtos.models import Produto, Tag
from mercado.models import Mercado
from mercado.serializers import MercadoSerializer

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'nome']

class ProdutoSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, required=False, write_only=True)
    mercados = serializers.PrimaryKeyRelatedField(queryset=Mercado.objects.all(), many=True, required=False, write_only=True)

    tag_info = TagSerializer(source='tags', many=True, read_only=True)
    mercado_info = MercadoSerializer(source='mercados', many=True, read_only=True)

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco', 'tags', 'mercados', 'tag_info', 'mercado_info']