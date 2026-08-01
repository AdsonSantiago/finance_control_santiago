from decimal import Decimal

from apps.financeiro.queries.extrato_query import ExtratoQuery


class FluxoCaixaService:

    @staticmethod
    def gerar(usuario, filtros):

        movimentos = ExtratoQuery.listar(
            usuario,
            filtros,
        )

        saldo = Decimal("0.00")

        fluxo = []

        for movimento in movimentos:

            if movimento.tipo == "REC":
                saldo += movimento.valor
            else:
                saldo -= movimento.valor

            fluxo.append({
                "movimento": movimento,
                "saldo": saldo,
            })

        return fluxo