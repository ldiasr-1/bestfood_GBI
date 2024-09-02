from django.contrib import admin

# Register your models here.
# produtos/admin.py
from django.contrib import admin
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco', 'get_tags', 'get_mercados')
    list_filter = ('tags', 'mercados')

    def get_tags(self, obj):
        return ", ".join(tag.nome for tag in obj.tags.all())
    get_tags.short_description = 'Tags'

    def get_mercados(self, obj):
        return ", ".join(mercado.nome for mercado in obj.mercados.all())
    get_mercados.short_description = 'Mercados'

admin.site.register(Produto, ProdutoAdmin)
