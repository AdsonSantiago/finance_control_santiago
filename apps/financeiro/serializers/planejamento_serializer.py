from rest_framework import serializers

from apps.financeiro.models import PlanejamentoFinanceiro


class PlanejamentoSerializer(serializers.ModelSerializer):

    conta_nome = serializers.CharField(
        source="conta.nome",
        read_only=True,
    )

    categoria_nome = serializers.CharField(
        source="categoria.nome",
        read_only=True,
    )

    movimento_id = serializers.IntegerField(
        source="movimento.id",
        read_only=True,
    )

    class Meta:

        model = PlanejamentoFinanceiro

        fields = (
            "id",

            "conta",
            "conta_nome",

            "categoria",
            "categoria_nome",

            "tipo",

            "descricao",

            "valor",

            "data_prevista",

            "status",

            "recorrencia",

            "parcelado",

            "parcela_atual",

            "total_parcelas",

            "prioridade",

            "observacao",

            "movimento",

            "movimento_id",

            "criado_em",

            "atualizado_em",
        )

        read_only_fields = (
            "id",
            "status",
            "movimento",
            "movimento_id",
            "criado_em",
            "atualizado_em",
        )