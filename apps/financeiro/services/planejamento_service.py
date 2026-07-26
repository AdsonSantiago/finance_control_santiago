from django.db import transaction
from apps.financeiro.exceptions import PlanejamentoException
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from apps.financeiro.Models import (
    Movimento,
    PlanejamentoFinanceiro,
)


class PlanejamentoService:
    @staticmethod
    def _gerar_proxima_recorrencia(
        planejamento: PlanejamentoFinanceiro
    ):
        pass

        if planejamento.recorrencia == PlanejamentoFinanceiro.TipoRecorrencia.NENHUMA:
            return None

        nova_data = PlanejamentoService._calcular_proxima_data(
            planejamento
        )

        return PlanejamentoFinanceiro.objects.create(
            usuario=planejamento.usuario,
            conta=planejamento.conta,
            categoria=planejamento.categoria,
            tipo=planejamento.tipo,
            descricao=planejamento.descricao,
            valor=planejamento.valor,
            data_prevista=nova_data,
            status=PlanejamentoFinanceiro.Status.PENDENTE,
            recorrencia=planejamento.recorrencia,
            prioridade=planejamento.prioridade,
            parcelado=False,
            parcela_atual=1,
            total_parcelas=1,
            observacao=planejamento.observacao,
        )
    
    @staticmethod
    def _gerar_proxima_recorrencia(
        planejamento: PlanejamentoFinanceiro,
    ):
        """
        Gera automaticamente o próximo planejamento recorrente.
        """

        pass

    @staticmethod
    def _calcular_proxima_data(
        planejamento: PlanejamentoFinanceiro,
    ):
        """
        Calcula a próxima data baseada na recorrência.
        """

        data = planejamento.data_prevista

        if planejamento.recorrencia == PlanejamentoFinanceiro.TipoRecorrencia.DIARIA:
            return data + timedelta(days=1)

        if planejamento.recorrencia == PlanejamentoFinanceiro.TipoRecorrencia.SEMANAL:
            return data + timedelta(weeks=1)

        if planejamento.recorrencia == PlanejamentoFinanceiro.TipoRecorrencia.MENSAL:
            return data + relativedelta(months=1)

        if planejamento.recorrencia == PlanejamentoFinanceiro.TipoRecorrencia.ANUAL:
            return data + relativedelta(years=1)

        return None
    
    @staticmethod
    @transaction.atomic
    def marcar_como_pago(planejamento: PlanejamentoFinanceiro, data_pagamento=None,):

        """
        Converte um planejamento pendente em um movimento financeiro.
        """

        PlanejamentoService._validar_pagamento(planejamento)

        movimento = PlanejamentoService._criar_movimento(planejamento)

        PlanejamentoService._atualizar_status(planejamento, movimento)

        PlanejamentoService._gerar_proxima_recorrencia(planejamento)

        return movimento

    @staticmethod
    def _validar_pagamento(planejamento: PlanejamentoFinanceiro):
        """
        Valida se o planejamento pode ser pago.
        """

        if planejamento.status == PlanejamentoFinanceiro.Status.PAGO:
            raise PlanejamentoException(
                "Este planejamento já foi pago."
            )

        if planejamento.status == PlanejamentoFinanceiro.Status.CANCELADO:
            raise PlanejamentoException(
                "Este planejamento foi cancelado."
            )

    @staticmethod
    def _criar_movimento(planejamento: PlanejamentoFinanceiro):
        """
        Cria um movimento financeiro baseado no planejamento.
        """

        return Movimento.objects.create(
            usuario=planejamento.usuario,
            conta=planejamento.conta,
            categoria=planejamento.categoria,
            tipo=planejamento.tipo,
            descricao=planejamento.descricao,
            valor=planejamento.valor,
            data_movimento=planejamento.data_prevista,
            observacao=planejamento.observacao,
        )

    @staticmethod
    def _atualizar_status(planejamento: PlanejamentoFinanceiro, movimento: Movimento,):
        """
        Atualiza o status do planejamento para pago.
        """

        planejamento.status = PlanejamentoFinanceiro.Status.PAGO
        planejamento.movimento = movimento

        planejamento.save(
            update_fields=[
                "status",
                "movimento",
            ]
        )