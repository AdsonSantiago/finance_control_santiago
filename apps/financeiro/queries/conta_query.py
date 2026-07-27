from django.db.models import Sum
from django.utils import timezone

from apps.financeiro.models import Conta



class ContaQuery:

    @staticmethod
    def contas_ativas(usuario):
        return Conta.objects.filter(
            usuario=usuario,
            ativo=True,
        )

    @staticmethod
    def saldo_total(usuario):

        total = 0

        for conta in ContaQuery.contas_ativas(usuario):
            total += conta.saldo_atual

        return total
