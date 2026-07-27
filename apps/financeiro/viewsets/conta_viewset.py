from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.financeiro.models import Conta
from apps.financeiro.serializers import ContaSerializer


class ContaViewSet(ModelViewSet):

    serializer_class = ContaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Conta.objects.filter(
            usuario=self.request.user
        ).order_by("ordem", "nome")

    def perform_create(self, serializer):
        serializer.save(
            usuario=self.request.user
        )