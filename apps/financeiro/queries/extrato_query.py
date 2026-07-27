from apps.financeiro.models import Movimento
from apps.financeiro.filters.movimento_filter import MovimentoFilter


class ExtratoQuery:

    @staticmethod
    def listar(usuario, filtros):

        queryset = Movimento.objects.filter(
            usuario=usuario
        ).select_related(
            "conta",
            "categoria",
        )

        return MovimentoFilter.aplicar(
            queryset,
            filtros,
        )