from rest_framework import serializers


class IndicadorSerializer(serializers.Serializer):

    receitas = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    despesas = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    saldo = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    percentual_economia = serializers.FloatField()

    movimentos = serializers.IntegerField()