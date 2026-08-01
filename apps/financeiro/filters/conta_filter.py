from django_filters import rest_framework as filters

from apps.financeiro.models import Conta


class ContaFilter(filters.FilterSet):

    class Meta:

        model = Conta

        fields = [
            "tipo",
            "ativo",
        ]