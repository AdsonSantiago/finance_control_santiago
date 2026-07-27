from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.financeiro.models import PlanejamentoFinanceiro
from apps.financeiro.serializers.planejamento_serializer import PlanejamentoSerializer
from apps.financeiro.services.planejamento_service import PlanejamentoService


class PlanejamentoViewSet(ModelViewSet):

    serializer_class = PlanejamentoSerializer

    def get_queryset(self):
        return (
            PlanejamentoFinanceiro.objects
            .filter(usuario=self.request.user)
            .select_related(
                "conta",
                "categoria",
                "movimento",
            )
        )

    def perform_create(self, serializer):
        serializer.save(
            usuario=self.request.user
        )

    @action(
        detail=True,
        methods=["post"],
        url_path="pagar",
    )
    def pagar(self, request, pk=None):

        planejamento = self.get_object()

        movimento = PlanejamentoService.marcar_como_pago(
            planejamento
        )

        return Response(
            {
                "message": "Planejamento pago com sucesso.",
                "movimento_id": movimento.id,
            },
            status=status.HTTP_200_OK,
        )