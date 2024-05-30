from django.db import models
from django.contrib.auth.models import User

class Reserva(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    numero_pessoas = models.PositiveIntegerField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.data} {self.hora}"
