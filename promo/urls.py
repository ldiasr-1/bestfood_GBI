# promos/urls.py
from django.urls import path
from . import views
from .views import PromocaoCreateView, PromocaoListView, PromocaoDeleteView

app_name = 'promos'

urlpatterns = [
    path('', views.PromocaoListView.as_view(), name='listar_promocoes'),
    path('criar/', PromocaoCreateView.as_view(), name='criar_promocao'),
    path('<int:pk>/cancelar/', views.cancelar_promocao, name='cancelar_promocao'),
]
