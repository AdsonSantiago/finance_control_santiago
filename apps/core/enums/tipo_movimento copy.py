from django.db import models


class TipoMovimento(models.TextChoices):
    RECEITA = "REC", "Receita"
    DESPESA = "DES", "Despesa"
    TRANSFERENCIA = "TRA", "Transferência"