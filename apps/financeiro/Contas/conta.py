class Conta(models.Model):

    class Tipo(models.TextChoices):
        CARTEIRA = "CAR", "Carteira"
        CORRENTE = "CC", "Conta Corrente"
        POUPANCA = "CP", "Poupança"
        CARTAO = "CRT", "Cartão"

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=3, choices=Tipo.choices)
    saldo_inicial = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome