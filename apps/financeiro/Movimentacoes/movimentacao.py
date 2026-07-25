from django.contrib.auth.models import User

class Movimentacao(models.Model):

    class Tipo(models.TextChoices):
        RECEITA = "R", "Receita"
        DESPESA = "D", "Despesa"

    class Status(models.TextChoices):
        PENDENTE = "P", "Pendente"
        PAGO = "PG", "Pago"

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    descricao = models.CharField(max_length=200)

    valor = models.DecimalField(max_digits=10, decimal_places=2)

    tipo = models.CharField(max_length=2, choices=Tipo.choices)

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    conta = models.ForeignKey(Conta, on_delete=models.PROTECT)

    vencimento = models.DateField()

    pagamento = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.PENDENTE
    )

    observacao = models.TextField(blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao 