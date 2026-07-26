from django.contrib import admin
from ..Models import PlanejamentoFinanceiro

from django.contrib import messages

from apps.financeiro.exceptions import PlanejamentoException
from apps.financeiro.services.planejamento_service import PlanejamentoService


@admin.register(PlanejamentoFinanceiro)
class PlanejamentoFinanceiroAdmin(admin.ModelAdmin):
    list_display = (
    "descricao",
    "usuario",
    "tipo",
    "valor",
    "prioridade",
    "data_prevista",
    "status",
    "recorrencia",
    "parcelado",
    )

    list_filter = (
    "tipo",
    "status",
    "recorrencia",
    "parcelado",
    )

    actions = ["marcar_como_pago"]
    @admin.action(description="Marcar planejamento(s) como pago(s)")
    def marcar_como_pago(self, request, queryset):

        pagos = 0

        for planejamento in queryset:
            try:
                PlanejamentoService.marcar_como_pago(planejamento)
                pagos += 1

            except PlanejamentoException as erro:
                self.message_user(
                    request,
                    f"{planejamento.descricao}: {erro}",
                    level=messages.ERROR,
                )

        if pagos:
            self.message_user(
                request,
                f"{pagos} planejamento(s) processado(s) com sucesso.",
                level=messages.SUCCESS,
            )
            
    list_select_related = (
    "usuario",
    "conta",
    "categoria",
    )

    search_fields = (
        "descricao",
        "usuario__email",
        "categoria__nome",
        "conta__nome",
    )

    date_hierarchy = "data_prevista"
