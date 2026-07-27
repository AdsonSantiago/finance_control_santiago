from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from apps.financeiro.queries.extrato_query import ExtratoQuery
from apps.financeiro.serializers import MovimentoSerializer


class ExtratoViewSet(ViewSet):

    def list(self, request):

        queryset = ExtratoQuery.listar(
            request.user,
            request.query_params,
        )

        serializer = MovimentoSerializer(
            queryset,
            many=True,
        )

        return Response(serializer.data)