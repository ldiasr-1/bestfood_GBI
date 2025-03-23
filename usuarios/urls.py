from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ClienteViewSet, VendedorViewSet

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.create, name="create"),
    path("list/", views.read, name="read"),
    path("edit/<int:pessoa_id>/", views.update, name="update"),
    path("delete/<int:pessoa_id>/", views.delete, name="delete"),
    path("<int:pessoa_id>/", views.detail, name="detail"),
    ]

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'vendedores', VendedorViewSet)

urlpatterns += [
    path('api/', include(router.urls)),
]