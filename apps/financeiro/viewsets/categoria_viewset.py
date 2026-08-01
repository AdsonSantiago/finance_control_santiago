
from apps.financeiro.models import Categoria
from apps.financeiro.serializers import CategoriaSerializer

from apps.core.viewsets.base_viewset import BaseViewSet


class CategoriaViewSet(BaseViewSet):

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    default_ordering = ["nome"]
