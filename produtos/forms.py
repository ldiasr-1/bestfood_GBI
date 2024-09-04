from django import forms
from .models import Produto, Tag
from promo.models import Promocao



class ProdutoForm(forms.ModelForm):
    class Meta:
        tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'tags', 'mercados']
        widgets = {
            'mercados': forms.CheckboxSelectMultiple(),  # Checkbox para mercados
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['tags'].widget = forms.CheckboxSelectMultiple()
            self.fields['tags'].queryset = Tag.objects.all()

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['nome']

