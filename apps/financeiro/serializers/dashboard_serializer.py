from rest_framework import serializers


class DashboardSerializer(serializers.Serializer):

    saldo_atual = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    saldo_previsto = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    receitas_mes = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    despesas_mes = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    planejado_receber = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    planejado_pagar = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )