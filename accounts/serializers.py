from rest_framework import serializers
from .models import CustomUser  # Substitua User por CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser  # Substitua User por CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class CustomUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = CustomUser
        fields = ['id', 'user', 'cpf', 'cnpj', 'endereco', 'telefone']