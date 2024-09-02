from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class UsarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ['nome', 'sobrenome', 'endereco', 'telefone', 'email', 'username', 'password1', 'password2']