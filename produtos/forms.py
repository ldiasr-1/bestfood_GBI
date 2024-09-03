from django import forms
from .models import Produto, Tag

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'tags', 'mercados']
        widgets = {
            'mercados': forms.CheckboxSelectMultiple(),  # Checkbox para mercados
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['tags'].widget = forms.CheckboxSelectMultiple()
            self.fields['tags'].queryset = Tag.objects.all()