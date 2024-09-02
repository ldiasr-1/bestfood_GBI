# mercado/forms.py
from django import forms
from .models import Mercado

class MercadoForm(forms.ModelForm):
    class Meta:
        model = Mercado
        fields = ['nome', 'endereco']
