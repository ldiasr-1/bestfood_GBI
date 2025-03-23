from django.urls import path, include
from rest_framework.routers import DefaultRouter
from produtos.views import ProdutoViewSet, TagViewSet
from mercado.views import MercadoViewSet
from promo.views import PromocaoViewSet
from usuarios.views import ClienteViewSet, VendedorViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'tags', TagViewSet)
router.register(r'mercados', MercadoViewSet)
router.register(r'promocoes', PromocaoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'vendedores', VendedorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]