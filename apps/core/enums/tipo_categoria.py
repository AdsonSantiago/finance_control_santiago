from django.db import models

class TipoCategoria(models.TextChoices):

    RECEITA = "REC", "Receita"
    DESPESA = "DES", "Despesa"
    TRANSFERENCIA = "TRA", "Transferência"