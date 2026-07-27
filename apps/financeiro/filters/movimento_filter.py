

class MovimentoFilter:

    @staticmethod
    def aplicar(queryset, filtros):

        if conta := filtros.get("conta"):
            queryset = queryset.filter(
                conta_id=conta
            )

        if categoria := filtros.get("categoria"):
            queryset = queryset.filter(
                categoria_id=categoria
            )

        if tipo := filtros.get("tipo"):
            queryset = queryset.filter(
                tipo=tipo
            )

        if inicio := filtros.get("inicio"):
            queryset = queryset.filter(
                data_movimento__gte=inicio
            )

        if fim := filtros.get("fim"):
            queryset = queryset.filter(
                data_movimento__lte=fim
            )

        if texto := filtros.get("texto"):
            queryset = queryset.filter(
                descricao__icontains=texto
            )

        return queryset