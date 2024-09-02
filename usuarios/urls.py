from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.create, name="create"),
    path("list/", views.read, name="read"),
    path("edit/<int:pessoa_id>/", views.update, name="update"),
    path("delete/<int:pessoa_id>/", views.delete, name="delete"),
    path("<int:pessoa_id>/", views.detail, name="detail"),
    ]