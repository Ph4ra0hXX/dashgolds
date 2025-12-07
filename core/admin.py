from django.contrib import admin
from .models import Menu, ConfiguracaoSistema


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("nome", "url", "ativo")
    list_filter = ("ativo",)
    search_fields = ("nome", "url")


@admin.register(ConfiguracaoSistema)
class ConfiguracaoSistemaAdmin(admin.ModelAdmin):
    list_display = ("sistema_aberto",)

    def has_add_permission(self, request):
        # Limitar a apenas uma configuração
        return not ConfiguracaoSistema.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Não permitir deletar a configuração
        return False
