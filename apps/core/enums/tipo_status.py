from django.db import models

class Status(models.TextChoices):
    PENDENTE = "PEN", "Pendente"
    PAGO = "PAG", "Pago"
    CANCELADO = "CAN", "Cancelado"