from django.db.models import Sum
from apps.financeiro.models import PlanejamentoFinanceiro
from apps.financeiro.queries.movimento_query import MovimentoQuery
from apps.financeiro.models.conta import Conta
from apps.core.enums.tipo_planejamento import TipoPlanejamento
from apps.core.enums.tipo_movimento import TipoMovimento
from apps.core.enums.tipo_status import Status

class DashboardQuery:

    @staticmethod
    def saldo_total(usuario):
        saldo = 0

        contas = Conta.objects.filter(
            usuario=usuario,
            ativo=True,
        )

        for conta in contas:
            saldo += conta.saldo_atual

        return saldo
    
    @staticmethod
    def receitas_mes(usuario):

        return (
            MovimentoQuery.movimentos_mes(usuario)
            .filter(
                tipo=TipoMovimento.RECEITA
            )
            .aggregate(total=Sum("valor"))["total"] or 0
        )

    @staticmethod
    def despesas_mes(usuario):

        return (
            MovimentoQuery.movimentos_mes(usuario)
            .filter(
                tipo=TipoMovimento.DESPESA
            )
            .aggregate(total=Sum("valor"))["total"] or 0
        )
    
    @staticmethod
    def planejado_receber(usuario):
        return (
            PlanejamentoFinanceiro.objects.filter(
                usuario=usuario,
                tipo=TipoPlanejamento.RECEITA,
                status=Status.PENDENTE,
            ).aggregate(
                total=Sum("valor")
            )["total"] or 0
        )
    
    @staticmethod
    def planejado_pagar(usuario):
        return (
            PlanejamentoFinanceiro.objects.filter(
                usuario=usuario,
                tipo=TipoPlanejamento.DESPESA,
                status=Status.PENDENTE,
            ).aggregate(
                total=Sum("valor")
            )["total"] or 0
        )
    
    @staticmethod
    def saldo_previsto(usuario):
        return (
            DashboardQuery.saldo_total(usuario)
            + DashboardQuery.planejado_receber(usuario)
            - DashboardQuery.planejado_pagar(usuario)
        )