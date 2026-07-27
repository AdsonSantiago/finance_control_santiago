from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.financeiro.models import Movimento
from apps.financeiro.serializers import MovimentoSerializer


class MovimentoViewSet(ModelViewSet):

    serializer_class = MovimentoSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):
        return Movimento.objects.filter(
            usuario=self.request.user
        ).select_related(
            "conta",
            "categoria",
        )

    def perform_create(self, serializer):
        serializer.save()