from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class CustomUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = CustomUser
        fields = ['id', 'user', 'cpf', 'cnpj', 'endereco', 'telefone']