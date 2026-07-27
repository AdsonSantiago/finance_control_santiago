from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.financeiro.serializers import DashboardSerializer
from apps.financeiro.services.dashboard_service import DashboardService


class DashboardViewSet(ViewSet):

    def list(self, request):

        dados = DashboardService.resumo(
            usuario=request.user
        )

        serializer = DashboardSerializer(dados)

        return Response(serializer.data)