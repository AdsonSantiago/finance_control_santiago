from apps.financeiro.queries.dashboard_query import DashboardQuery


class DashboardService:

    @staticmethod
    def resumo(usuario):

        saldo = DashboardQuery.saldo_total(usuario)
        receitas = DashboardQuery.receitas_mes(usuario)
        despesas = DashboardQuery.despesas_mes(usuario)
        receber = DashboardQuery.planejado_receber(usuario)
        pagar = DashboardQuery.planejado_pagar(usuario)

        return {
            "saldo_atual": saldo,
            "receitas_mes": receitas,
            "despesas_mes": despesas,
            "saldo_mes": receitas - despesas,
            "planejado_receber": receber,
            "planejado_pagar": pagar,
            "saldo_previsto": saldo + receber - pagar,
        }