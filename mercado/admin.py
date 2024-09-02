from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Mercado

@admin.register(Mercado)
class MercadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco')
    search_fields = ('nome', 'endereco')