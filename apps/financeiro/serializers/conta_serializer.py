from rest_framework import serializers

from apps.financeiro.models import Conta


class ContaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conta

        fields = (
            "id",
            "nome",
            "tipo",
            "saldo_inicial",
            "saldo_atual",
            "ordem",
            "ativo",
        )

        read_only_fields = (
            "id",
            "saldo_atual",
        )