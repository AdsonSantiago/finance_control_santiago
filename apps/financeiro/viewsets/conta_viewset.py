from apps.core.viewsets.base_viewset import BaseViewSet

from apps.financeiro.models import Conta
from apps.financeiro.serializers import ContaSerializer


class ContaViewSet(BaseViewSet):

    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

    default_ordering = ["ordem"]

