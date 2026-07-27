from django.db.models import Sum
from django.utils import timezone

from apps.financeiro.models import PlanejamentoFinanceiro

class PlanejamentoQuery:

    @staticmethod
    def pendentes(usuario):

        return PlanejamentoFinanceiro.objects.filter(
            usuario=usuario,
            status=PlanejamentoFinanceiro.Status.PENDENTE,
        )