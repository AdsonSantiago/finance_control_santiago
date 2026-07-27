from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.financeiro.models import Categoria
from apps.financeiro.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):

    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Categoria.objects.filter(
            usuario=self.request.user
        ).order_by("nome")

    def perform_create(self, serializer):
        serializer.save(
            usuario=self.request.user
        )