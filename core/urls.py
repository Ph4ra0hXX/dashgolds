from django.urls import path
from .views import home, registrar_menu, editar_menu, deletar_menu

urlpatterns = [
    path("", home, name="home"),
    path("registrar-menu/", registrar_menu, name="registrar_menu"),
    path("editar-menu/<int:id>/", editar_menu, name="editar_menu"),
    path("deletar-menu/<int:id>/", deletar_menu, name="deletar_menu"),
]
