

class FinanceiroException(Exception):
    """Exceção base do módulo financeiro."""
    pass


class PlanejamentoException(FinanceiroException):
    """Exceção relacionada ao planejamento financeiro."""
    pass


class MovimentoException(FinanceiroException):
    """Exceção relacionada às movimentações financeiras."""
    pass


class ContaException(FinanceiroException):
    """Exceção relacionada às contas."""
    pass