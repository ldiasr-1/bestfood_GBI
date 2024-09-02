from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class UsarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['nome', 'sobrenome', 'email', 'username', 'password1', 'password2']