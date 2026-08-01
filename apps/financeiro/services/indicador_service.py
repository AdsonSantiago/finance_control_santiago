from apps.financeiro.queries.indicador_query import IndicadorQuery


class IndicadorService:

    @staticmethod
    def resumo(usuario):

        receitas = IndicadorQuery.total_receitas(usuario)
        despesas = IndicadorQuery.total_despesas(usuario)

        saldo = receitas - despesas

        if receitas > 0:
            economia = (saldo / receitas) * 100
        else:
            economia = 0

        return {
            "receitas": receitas,
            "despesas": despesas,
            "saldo": saldo,
            "percentual_economia": round(economia, 2),
            "movimentos": IndicadorQuery.quantidade_movimentos(usuario),
        }