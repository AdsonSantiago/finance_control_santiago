from django.db import models


class TipoPlanejamento(models.TextChoices):
    RECEITA = "REC", "Receita"
    DESPESA = "DES", "Despesa"

class TipoRecorrencia(models.TextChoices):
    NENHUMA = "NEN", "Nenhuma"
    DIARIA = "DIA", "Diária"
    SEMANAL = "SEM", "Semanal"
    MENSAL = "MEN", "Mensal"
    ANUAL = "ANU", "Anual"
    QUINZENAL = "QUI", "Quinzenal"


class Prioridade(models.IntegerChoices):
    ALTA = 1, "Alta"
    MEDIA = 2, "Média"
    BAIXA = 3, "Baixa"