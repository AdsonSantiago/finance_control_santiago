from rest_framework import serializers

from apps.usuarios.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):

    perfil = serializers.StringRelatedField()

    class Meta:
        model = Usuario

        fields = (
            "id",
            "nome",
            "sobrenome",
            "email",
            "timezone",
            "perfil",
            "is_active",
            "date_joined",
        )

        read_only_fields = (
            "id",
            "date_joined",
        )