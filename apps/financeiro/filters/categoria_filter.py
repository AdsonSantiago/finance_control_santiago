from django_filters import rest_framework as filters

from apps.financeiro.models import Categoria


class CategoriaFilter(filters.FilterSet):

    class Meta:

        model = Categoria

        fields = [
            "tipo",
            "ativo",
        ]