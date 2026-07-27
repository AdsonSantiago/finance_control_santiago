from rest_framework import serializers

from apps.core.exceptions import MovimentoException
from apps.financeiro.models import Movimento
from apps.financeiro.services.movimento_service import MovimentoService


class MovimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movimento

        fields = (
            "id",
            "conta",
            "categoria",
            "tipo",
            "descricao",
            "valor",
            "data_movimento",
            "observacao",
        )

        read_only_fields = (
            "id",
        )

    def validate(self, attrs):

        try:

            MovimentoService.validar(
                usuario=self.context["request"].user,
                conta=attrs["conta"],
                categoria=attrs.get("categoria"),
                tipo=attrs["tipo"],
                valor=attrs["valor"],
            )

        except MovimentoException as e:
            raise serializers.ValidationError(str(e))

        return attrs

    def create(self, validated_data):

        return Movimento.objects.create(
            usuario=self.context["request"].user,
            **validated_data
        )