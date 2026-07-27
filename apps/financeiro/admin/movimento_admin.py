from django.contrib import admin
from ..models import Movimento

from apps.financeiro.services.planejamento_service import PlanejamentoService


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
        "criado_em",
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

    ordering = (
    "-data_movimento",
    "-criado_em",
    )
