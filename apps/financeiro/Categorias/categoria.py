from django.db import models

class Categoria(models.Model):

    class Tipo(models.TextChoices):
        RECEITA = "R", "Receita"
        DESPESA = "D", "Despesa"

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1, choices=Tipo.choices)
    cor = models.CharField(max_length=7, default="#3B82F6")
    icone = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nome