from django.db import models
from django.conf import settings

class Perfil(models.Model):

    nome = models.CharField(
        max_length=50,unique=True
    )

    descricao = models.TextField(
        blank=True
    )

    ativo = models.BooleanField(
        default=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"
        ordering = ["nome"]

    def __str__(self):
        return self.nome

class Conta(models.Model):

    class TipoConta(models.TextChoices):
        DINHEIRO = "DIN", "Dinheiro"
        CORRENTE = "CC", "Conta Corrente"
        POUPANCA = "CP", "Poupança"
        CARTAO = "CAR", "Cartão de Crédito"
        INVESTIMENTO = "INV", "Investimento"

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contas"
    )

    nome = models.CharField(
        max_length=100
    )

    tipo = models.CharField(
        max_length=3,
        choices=TipoConta.choices,
        default=TipoConta.CORRENTE
    )

    saldo_inicial = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    ativo = models.BooleanField(
        default=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    ordem = models.PositiveSmallIntegerField(
        default=1
    )

    @property
    def saldo_atual(self):

        receitas = self.movimentos.filter(
            tipo="REC"
        ).aggregate(
            total=models.Sum("valor")
        )["total"] or 0


        despesas = self.movimentos.filter(
            tipo="DES"
        ).aggregate(
            total=models.Sum("valor")
        )["total"] or 0


        return self.saldo_inicial + receitas - despesas

    class Meta:
        ordering = ["ordem", "nome"]
        verbose_name = "Conta"
        verbose_name_plural = "Contas"

    def __str__(self):
        return f"{self.nome} ({self.usuario.email})"

class Categoria(models.Model):

    class TipoCategoria(models.TextChoices):

        RECEITA = "REC", "Receita"
        DESPESA = "DES", "Despesa"
        TRANSFERENCIA = "TRA", "Transferência"

    usuario = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="categorias"
    )

    nome = models.CharField(
        max_length=100
    )

    tipo = models.CharField(
        max_length=3,
        choices=TipoCategoria.choices
    )

    descricao = models.TextField(
        blank=True,
        null=True
    )

    ativo = models.BooleanField(
        default=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["nome"]

        constraints = [
            models.UniqueConstraint(
                fields=["usuario", "nome", "tipo"],
                name="categoria_unica_usuario"
            )
        ]

    def __str__(self):
        return f"{self.nome} - {self.tipo}"

class Movimento(models.Model):

    class TipoMovimento(models.TextChoices):
        RECEITA = "REC", "Receita"
        DESPESA = "DES", "Despesa"
        TRANSFERENCIA = "TRA", "Transferência"


    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="movimentos"
    )


    conta = models.ForeignKey(
        Conta,
        on_delete=models.CASCADE,
        related_name="movimentos"
    )


    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="movimentos"
    )


    tipo = models.CharField(
        max_length=3,
        choices=TipoMovimento.choices
    )


    descricao = models.CharField(
        max_length=150
    )


    valor = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )


    data_movimento = models.DateField()


    observacao = models.TextField(
        blank=True,
        null=True
    )


    criado_em = models.DateTimeField(
        auto_now_add=True
    )


    atualizado_em = models.DateTimeField(
        auto_now=True
    )


    class Meta:
        ordering = ["-data_movimento", "-criado_em"]


    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"

class PlanejamentoFinanceiro(models.Model):

    class TipoPlanejamento(models.TextChoices):
        RECEITA = "REC", "Receita"
        DESPESA = "DES", "Despesa"


    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="planejamentos"
    )


    conta = models.ForeignKey(
        Conta,
        on_delete=models.CASCADE,
        related_name="planejamentos"
    )


    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="planejamentos"
    )


    tipo = models.CharField(
        max_length=3,
        choices=TipoPlanejamento.choices
    )


    descricao = models.CharField(
        max_length=150
    )


    valor = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )


    data_prevista = models.DateField()


    realizado = models.BooleanField(
        default=False
    )


    observacao = models.TextField(
        blank=True,
        null=True
    )


    criado_em = models.DateTimeField(
        auto_now_add=True
    )


    atualizado_em = models.DateTimeField(
        auto_now=True
    )


    class Meta:
        ordering = ["data_prevista"]


    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"

