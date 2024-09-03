from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('<int:pk>/', views.ProdutoDetailView.as_view(), name='produt_detail'),
    path('<int:pk>/editar/', views.editar_produto, name='editar_produto'),
    path('<int:pk>/deletar/', views.deletar_produto, name='deletar_produto'),
]
