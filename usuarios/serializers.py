from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cliente, Vendedor

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ClienteSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Cliente
        fields = ['id', 'user', 'cpf', 'endereco', 'telefone']

class VendedorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Vendedor
        fields = ['id', 'user', 'cnpj', 'endereco', 'telefone']