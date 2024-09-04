from django import forms
from .models import Promocao
from produtos.models import Produto

class PromocaoForm(forms.ModelForm):
    produtos = forms.ModelMultipleChoiceField(
        queryset=Produto.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Promocao
        fields = ['percentual', 'produtos']
