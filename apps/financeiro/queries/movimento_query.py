from django.db.models import Sum
from django.utils import timezone


from apps.financeiro.models import Movimento

class MovimentoQuery:

    @staticmethod
    def movimentos_mes(usuario):

        hoje = timezone.localdate()

        return Movimento.objects.filter(
            usuario=usuario,
            data_movimento__year=hoje.year,
            data_movimento__month=hoje.month,
        )

