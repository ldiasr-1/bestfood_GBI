# mercado/urls.py
from django.urls import path
from . import views

app_name = 'mercado'

urlpatterns = [
    path('', views.listar_mercados, name='listar_mercados'),
    path('criar/', views.criar_mercado, name='criar_mercado'),
    path('editar/<int:pk>/', views.editar_mercado, name='editar_mercado'),
    path('deletar/<int:pk>/', views.deletar_mercado, name='deletar_mercado'),
]
