from django.db import models

class TipoConta(models.TextChoices):
    DINHEIRO = "DIN", "Dinheiro"
    CORRENTE = "CC", "Conta Corrente"
    POUPANCA = "CP", "Poupança"
    CARTAO = "CAR", "Cartão de Crédito"
    INVESTIMENTO = "INV", "Investimento"