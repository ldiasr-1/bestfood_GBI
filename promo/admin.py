from django.contrib import admin
from .models import Promocao

@admin.register(Promocao)
class PromocaoAdmin(admin.ModelAdmin):
    list_display = ('percentual', 'listar_produtos')
    filter_horizontal = ('produtos',)

    def listar_produtos(self, obj):
        return ", ".join([produto.nome for produto in obj.produtos.all()])
    listar_produtos.short_description = 'Produtos'