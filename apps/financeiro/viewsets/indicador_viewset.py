from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.financeiro.serializers.indicador_serializer import IndicadorSerializer
from apps.financeiro.services.indicador_service import IndicadorService


class IndicadorViewSet(ViewSet):

    def list(self, request):

        dados = IndicadorService.resumo(
            request.user
        )

        serializer = IndicadorSerializer(dados)

        return Response(serializer.data)

