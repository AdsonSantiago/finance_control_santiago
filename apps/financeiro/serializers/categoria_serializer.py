from rest_framework import serializers

from apps.financeiro.models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    def validate_nome(self, value):
        return value.strip().title()
    class Meta:
        model = Categoria

        fields = (
            "id",
            "nome",
            "tipo",
            "descricao",
            "ativo",
        )

        read_only_fields = (
            "id",
        )