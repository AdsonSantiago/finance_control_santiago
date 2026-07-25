from django.contrib import admin

from .models import (
    Perfil,
    Conta,
    Categoria,
    Movimento
)


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):

    list_display = (
        "nome",
        "ativo",
        "criado_em",
    )

    list_filter = (
        "ativo",
    )

    search_fields = (
        "nome",
    )


@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):

    list_display = (
        "nome",
        "usuario",
        "tipo",
        "saldo_inicial",
        "saldo_atual_display",
        "ativo",
        )

    list_filter = (
        "tipo",
        "ativo",
    )

    search_fields = (
        "nome",
        "usuario__email",
    )

    def saldo_atual_display(self, obj):
        return f"R$ {obj.saldo_atual:,.2f}"

    saldo_atual_display.short_description = "Saldo Atual"

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


@admin.register(Movimento)
class MovimentoAdmin(admin.ModelAdmin):

    list_display = (
        "descricao",
        "usuario",
        "tipo",
        "valor",
        "conta",
        "categoria",
        "data_movimento",
    )

    list_filter = (
        "tipo",
        "data_movimento",
    )

    search_fields = (
        "descricao",
        "usuario__email",
    )

    date_hierarchy = "data_movimento"