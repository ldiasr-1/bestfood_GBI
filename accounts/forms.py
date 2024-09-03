from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from usuarios.models import Cliente, Vendedor
from django.contrib.auth.models import Group

class UsarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    cpf = forms.CharField(required=False, max_length=11)
    cnpj = forms.CharField(required=False, max_length=14)


    class Meta:
        model = CustomUser
        fields = ['nome', 'sobrenome', 'email', 'password1', 'password2']
