from django.db import transaction
from apps.financeiro.models import Movimento
from apps.financeiro.services.movimento_service import MovimentoService
from apps.core.exceptions.transferencia import TransferenciaException
from apps.financeiro.models.categoria import Categoria

class TransferenciaService:

    @staticmethod
    @transaction.atomic
    def transferir(
        *,
        usuario,
        conta_origem,
        conta_destino,
        categoria,
        valor,
        descricao,
        data_movimento,
        observacao=None,
    ):
        if conta_origem == conta_destino:
            raise TransferenciaException(
                "A conta de origem deve ser diferente da conta destino."
            )

        if valor <= 0:
            raise TransferenciaException(
                "O valor deve ser maior que zero."
            )

        if not conta_origem.ativo:
            raise TransferenciaException(
                "A conta de origem está inativa."
            )

        if not conta_destino.ativo:
            raise TransferenciaException(
                "A conta de destino está inativa."
            )

        if categoria.tipo != Categoria.TipoCategoria.TRANSFERENCIA:
            raise TransferenciaException(
                "A categoria deve ser do tipo Transferência."
            )

        movimento_saida = MovimentoService.criar_movimento(
            usuario=usuario,
            conta=conta_origem,
            categoria=categoria,
            tipo=Movimento.TipoMovimento.DESPESA,
            descricao=descricao,
            valor=valor,
            data_movimento=data_movimento,
            observacao=observacao,
        )

        movimento_entrada = MovimentoService.criar_movimento(
            usuario=usuario,
            conta=conta_destino,
            categoria=categoria,
            tipo=Movimento.TipoMovimento.RECEITA,
            descricao=descricao,
            valor=valor,
            data_movimento=data_movimento,
            observacao=observacao,
        )

        return {
            "saida": movimento_saida,
            "entrada": movimento_entrada,
        }