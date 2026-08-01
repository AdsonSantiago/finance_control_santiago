from apps.core.viewsets.base_viewset import BaseViewSet

from apps.financeiro.models import Movimento
from apps.financeiro.serializers import MovimentoSerializer


class MovimentoViewSet(BaseViewSet):

    queryset = Movimento.objects.all()
    serializer_class = MovimentoSerializer