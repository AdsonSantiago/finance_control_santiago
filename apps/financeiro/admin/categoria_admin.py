from django.contrib import admin
from ..Models import Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    list_display = (
        "nome",
        "usuario",
        "tipo",
        "ativo",
        "criado_em",
    )

    list_filter = (
        "tipo",
        "ativo",
    )

    search_fields = (
        "nome",
        "usuario__email",
    )

    ordering = ("nome",)

    list_select_related = ("usuario",)
