from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from usuarios.models import Cliente, Vendedor
from django.contrib.auth.models import Group

class UsarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    cpf = forms.CharField(required=False, max_length=11)
    cnpj = forms.CharField(required=False, max_length=14)
    endereco = forms.CharField(required=False, max_length=100)
    telefone = forms.CharField(required=False, max_length=20)

    class Meta:
        model = CustomUser
        fields = ['nome', 'sobrenome', 'endereco', 'telefone' ,'email', 'password1', 'password2']
