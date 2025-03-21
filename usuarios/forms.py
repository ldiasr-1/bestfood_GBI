from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Pessoa
from django.contrib.auth import get_user_model

User = get_user_model()  # Obtém o modelo de usuário ativo (CustomUser ou User padrão)

class PessoaForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)

    class Meta:
        model = Pessoa
        fields = ['nome', 'sobrenome', 'endereco', 'telefone', 'email', 'username', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não correspondem")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'sobrenome', 'endereco', 'telefone', 'email']