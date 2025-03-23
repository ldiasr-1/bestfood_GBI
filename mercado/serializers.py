from rest_framework import serializers
from mercado.models import Mercado

class MercadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mercado
        fields = ['id', 'nome', 'endereco']