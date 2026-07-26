from django.contrib import admin
from ..Models import Conta


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

    ordering = ("nome",)

    list_select_related = ("usuario",)

    def saldo_atual_display(self, obj):
        return f"R$ {obj.saldo_atual:,.2f}"

    @admin.display(description="Saldo Atual")
    def saldo_atual_display(self, obj):
            ...
